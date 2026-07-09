"""Upload docs/outline-mcp-evaluation.md to Outline under Welcome collection.

- strip leading H1 (title becomes a separate field)
- rewrite relative links to GitHub blob URLs so they resolve in Outline
"""
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from outline_mcp import call_tool, call_tool_multi  # noqa: E402

WELCOME_COLLECTION_ID = "dd59eb70-cab2-4146-a16a-decb39af2388"
GH_BLOB = "https://github.com/digitaldemocracy2030/dd2030-wiki/blob/main"
SRC = Path(__file__).resolve().parent.parent / "docs" / "outline-mcp-evaluation.md"


def prepare(text: str) -> tuple[str, str]:
    """Return (title, body) ready for Outline create_document."""
    # Pull title from first H1
    m = re.match(r"#\s+(.+?)\n", text)
    title = m.group(1).strip() if m else SRC.stem
    body = text[m.end():] if m else text
    body = body.lstrip()

    # Rewrite relative links pointing up out of docs/ to github blob URLs.
    # docs/outline-mcp-evaluation.md sits in docs/, so ../foo means repo root.
    def rewrite(m):
        text_, target = m.group(1), m.group(2)
        # Skip absolute URLs, anchors, and absolute paths (those are Outline-internal
        # examples inside the doc body like /doc/...).
        if target.startswith(("http://", "https://", "mailto:", "#", "/")):
            return m.group(0)
        # Normalize ../scripts/x.py to repo-root scripts/x.py
        if target.startswith("../"):
            target = target[3:]
        else:
            target = "docs/" + target
        return f"[{text_}]({GH_BLOB}/{target})"

    # Avoid rewriting inside inline code spans / fenced code blocks. Split on
    # backtick code regions and only rewrite outside them.
    parts = re.split(r"(`[^`]*`|```[\s\S]*?```)", body)
    for i, part in enumerate(parts):
        if part.startswith("`"):
            continue
        parts[i] = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", rewrite, part)
    body = "".join(parts)
    return title, body


def main():
    title, body = prepare(SRC.read_text())
    print(f"Title: {title}")
    print(f"Body: {len(body)} chars")

    # Check if a doc with this title already exists in Welcome to avoid duplicates
    existing = call_tool_multi(
        "list_collection_documents", {"collectionId": WELCOME_COLLECTION_ID}
    )
    flat = []
    def collect(items):
        for it in items:
            flat.append(it)
            collect(it.get("children", []))
    collect(existing)
    for e in flat:
        if e.get("title") == title:
            print(f"Document already exists: {e['url']} — updating instead")
            resp = call_tool(
                "update_document",
                {"id": e["id"], "text": body, "editMode": "replace"},
            )
            print("update_document response:", list(resp.keys()) if isinstance(resp, dict) else resp)
            return

    resp = call_tool(
        "create_document",
        {
            "collectionId": WELCOME_COLLECTION_ID,
            "title": title,
            "text": body,
            "publish": True,
        },
    )
    doc = resp.get("document", resp)
    print(f"Created: {doc.get('url')}")
    print(f"ID: {doc.get('id')}")


if __name__ == "__main__":
    if not os.environ.get("OUTLINE_TOKEN"):
        sys.exit("Set OUTLINE_TOKEN")
    main()
