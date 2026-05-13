"""Smoke test: import 2 cross-linked wiki pages into Outline, measure timing.

Tests:
1. Raw [[wiki-link]] preservation (does Outline render or break?)
2. Bulk-edit timing (update content via update_document)
3. Outline-native link conversion (replace [[X]] with [text](/doc/...))
"""
import os
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from outline_mcp import call_tool  # noqa: E402

COLLECTION_ID = "5cc4a60d-fa8b-4ca6-9981-82674481d79d"  # import-test
WIKI = Path(__file__).resolve().parent.parent / "wiki"


def strip_frontmatter(text: str) -> tuple[dict, str]:
    """Strip YAML frontmatter, return (front_dict_lite, body_without_h1)."""
    front = {}
    body = text
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            for line in text[4:end].splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    front[k.strip()] = v.strip()
            body = text[end + 5 :]
    # Outline requires no leading H1 (title is separate)
    body = re.sub(r"^# .+?\n+", "", body.lstrip(), count=1)
    return front, body.lstrip()


def import_page(path: Path) -> dict:
    raw = path.read_text()
    front, body = strip_frontmatter(raw)
    title = front.get("title") or path.stem
    t0 = time.time()
    resp = call_tool(
        "create_document",
        {
            "collectionId": COLLECTION_ID,
            "title": title,
            "text": body,
            "publish": True,
        },
    )
    doc = resp.get("document", resp)
    dt = time.time() - t0
    print(f"  created {title!r}  id={doc.get('id','?')[:8]}…  {dt:.2f}s  url={doc.get('url')}")
    return doc


def main():
    pages = [
        WIKI / "concepts" / "broad-listening.md",
        WIKI / "concepts" / "deliberative-democracy.md",
    ]
    print("=== Phase 1: import with raw [[wiki-link]] preserved ===")
    docs = {}
    for p in pages:
        d = import_page(p)
        docs[p.stem] = d

    print("\n=== Phase 2: list collection to verify ===")
    from outline_mcp import call_tool_multi
    listed = call_tool_multi("list_collection_documents", {"collectionId": COLLECTION_ID})
    for entry in listed:
        print(f"  {entry}")

    # MCP fetch does not return body text. Use REST API instead.
    import json as _json
    import urllib.request as _ur
    TOKEN = os.environ["OUTLINE_TOKEN"]

    def doc_text_rest(doc_id):
        req = _ur.Request(
            "https://dd2030-docs.kbn.one/api/documents.info",
            data=_json.dumps({"id": doc_id}).encode(),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {TOKEN}",
                "User-Agent": "dd2030-wiki-importer/0.1",
            },
            method="POST",
        )
        with _ur.urlopen(req, timeout=30) as r:
            return _json.loads(r.read())["data"]["text"]

    print("\n=== Phase 3: read body via REST, then patch-mode append via MCP ===")
    for stem, doc in docs.items():
        t0 = time.time()
        body = doc_text_rest(doc["id"])
        t_read = time.time() - t0
        # Use patch mode to append a marker after a known anchor without overwriting
        # Pick the last existing section to append after
        anchor = "## 関連ページ"
        if anchor not in body:
            print(f"  WARN: anchor not in {stem}")
            continue
        t1 = time.time()
        call_tool(
            "update_document",
            {
                "id": doc["id"],
                "editMode": "patch",
                "findText": anchor,
                "text": anchor + "\n\n<!-- patched via MCP -->\n",
            },
        )
        t_patch = time.time() - t1
        print(f"  {stem}: read {t_read:.2f}s (REST, {len(body)} chars), patch {t_patch:.2f}s")

    print("\n=== Phase 4: verify [[wiki-link]] preserved after import ===")
    for stem, doc in docs.items():
        body = doc_text_rest(doc["id"])
        wiki_links = re.findall(r"\[\[([^\]]+)\]\]", body)
        markdown_links = re.findall(r"\[([^\]]+)\]\([^)]+\)", body)
        print(f"  {stem}: stored len={len(body)}  [[wiki-link]]={wiki_links}")
        print(f"    markdown links: {len(markdown_links)} (sample: {markdown_links[:3]})")


if __name__ == "__main__":
    if not os.environ.get("OUTLINE_TOKEN"):
        sys.exit("Set OUTLINE_TOKEN")
    main()
