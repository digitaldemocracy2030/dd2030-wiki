"""Test: replace [[wiki-link]] with [text](outline-url) so Outline renders real links.

Strategy: build a name->url map from imported docs, then patch each doc's body.
"""
import os
import re
import sys
import time
import json
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from outline_mcp import call_tool, call_tool_multi  # noqa: E402

COLLECTION_ID = "5cc4a60d-fa8b-4ca6-9981-82674481d79d"
TOKEN = os.environ["OUTLINE_TOKEN"]


def doc_text_rest(doc_id):
    req = urllib.request.Request(
        "https://dd2030-docs.kbn.one/api/documents.info",
        data=json.dumps({"id": doc_id}).encode(),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {TOKEN}",
            "User-Agent": "dd2030-wiki-importer/0.1",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())["data"]["text"]


def main():
    docs = call_tool_multi("list_collection_documents", {"collectionId": COLLECTION_ID})
    name_to_url = {d["title"]: d["url"] for d in docs}
    # Note: aliases — broad-listening's title is ブロードリスニング, also referenced as [[ブロードリスニング]]
    # In this small test, titles already match the [[X]] strings used in source markdown.
    print("name → url map:")
    for k, v in name_to_url.items():
        print(f"  {k!r} → {v}")

    # Build relative-url version (strip domain) so links work whatever the deploy domain
    def to_path(url):
        # https://dd2030-docs.kbn.one/doc/SLUG → /doc/SLUG
        return url.split("/doc/", 1)[1] and "/doc/" + url.split("/doc/", 1)[1]

    name_to_path = {k: to_path(v) for k, v in name_to_url.items()}

    print("\nConverting links in each doc:")
    pattern = re.compile(r"\\\[\\\[([^\]]+?)\\\]\\\]")  # matches escaped \[\[X\]\]
    for d in docs:
        body = doc_text_rest(d["id"])
        n_total = 0
        n_resolved = 0
        def repl(m):
            nonlocal n_total, n_resolved
            n_total += 1
            name = m.group(1)
            if name in name_to_path:
                n_resolved += 1
                return f"[{name}]({name_to_path[name]})"
            # Leave unresolved as plain text (no escape, not a fake link)
            return name
        new_body = pattern.sub(repl, body)
        print(f"  {d['title']}: {n_resolved}/{n_total} links resolved")
        if n_total == 0:
            continue
        t0 = time.time()
        call_tool(
            "update_document",
            {"id": d["id"], "text": new_body, "editMode": "replace"},
        )
        print(f"    replaced full body in {time.time()-t0:.2f}s")

    print("\nVerify rendered body:")
    for d in docs:
        body = doc_text_rest(d["id"])
        # Check for both escaped wiki links and real markdown links
        remaining = pattern.findall(body)
        # Markdown links that point to /doc/...
        outline_links = re.findall(r"\[([^\]]+)\]\((/doc/[^)]+)\)", body)
        print(f"  {d['title']}: {len(remaining)} unresolved [[..]] left, {len(outline_links)} outline links: {outline_links[:3]}")


if __name__ == "__main__":
    main()
