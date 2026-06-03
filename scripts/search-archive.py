#!/usr/bin/env python3
"""Search helper for the external oss_weekly_reporter archive.

The archive is described in ../archive_index.md. It lives outside this repo
(default: /tmp/oss_weekly_reporter, data branch) and contains 67 weekly
snapshots of Slack and GitHub activity.

Typical use:
  # Find all weeks where a keyword appears in slack ai_reports
  python3 scripts/search-archive.py "熟議"

  # Search inside raw slack JSON, with text snippets
  python3 scripts/search-archive.py "Polimoney" --layer raw --limit 20

  # Restrict to a date range and a layer
  python3 scripts/search-archive.py "コアループ" --since 2025-09 --layer ai_reports

  # List available weeks
  python3 scripts/search-archive.py --list-weeks

The script does not modify the archive. It prints matches with enough
context to decide which file to open next.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

DEFAULT_ARCHIVE_ROOT = Path("/tmp/oss_weekly_reporter/data")
LAYERS = ("ai_reports", "markdown", "raw")


def list_week_dirs(root: Path) -> list[Path]:
    if not root.exists():
        return []
    pattern = re.compile(r"^\d{4}-\d{2}-\d{2}_to_\d{4}-\d{2}-\d{2}(-\d+)?$")
    return sorted(p for p in root.iterdir() if p.is_dir() and pattern.match(p.name))


def in_date_range(week_name: str, since: str | None, until: str | None) -> bool:
    # week_name format: 2025-12-24_to_2025-12-31[-2]
    start = week_name[:10]
    end = week_name[14:24]
    if since and end < since:
        return False
    if until and start > until:
        return False
    return True


def iter_files_for_layer(week_dir: Path, layer: str):
    if layer == "ai_reports":
        d = week_dir / "ai_reports"
        if d.exists():
            yield from sorted(d.glob("*.md"))
    elif layer == "markdown":
        d = week_dir / "markdown"
        if d.exists():
            yield from sorted(d.rglob("*.md"))
    elif layer == "raw":
        d = week_dir / "raw"
        if d.exists():
            yield from sorted(d.rglob("*.json"))


def search_text_file(path: Path, pattern: re.Pattern) -> list[tuple[int, str]]:
    hits: list[tuple[int, str]] = []
    try:
        with path.open(encoding="utf-8") as fh:
            for i, line in enumerate(fh, 1):
                if pattern.search(line):
                    snippet = line.strip()
                    if len(snippet) > 200:
                        snippet = snippet[:200] + "…"
                    hits.append((i, snippet))
    except (OSError, UnicodeDecodeError):
        pass
    return hits


def search_json_file(path: Path, pattern: re.Pattern) -> list[tuple[str, str]]:
    """Search Slack/GitHub JSON. Returns (locator, snippet) tuples."""
    hits: list[tuple[str, str]] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return hits

    if not isinstance(data, list):
        return hits

    for idx, item in enumerate(data):
        if not isinstance(item, dict):
            continue
        # Slack: text / text_readable. GitHub: title / body
        for field in ("text_readable", "text", "title", "body"):
            v = item.get(field)
            if isinstance(v, str) and pattern.search(v):
                snippet = v.replace("\n", " ").strip()
                if len(snippet) > 200:
                    snippet = snippet[:200] + "…"
                # Build locator
                if "ts" in item:
                    locator = f"[{idx}] ts={item.get('ts')} user={item.get('user_name', item.get('user', '?'))}"
                elif "number" in item:
                    locator = f"[{idx}] #{item.get('number')} ({item.get('type', '?')}) {item.get('user', '?')}"
                else:
                    locator = f"[{idx}]"
                hits.append((locator, f"{field}: {snippet}"))
                break  # one hit per item is enough
    return hits


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query", nargs="?", help="Keyword or regex")
    ap.add_argument("--root", type=Path, default=DEFAULT_ARCHIVE_ROOT, help="Archive data root (default: %(default)s)")
    ap.add_argument("--layer", choices=LAYERS, default="ai_reports", help="Which layer to search (default: %(default)s)")
    ap.add_argument("--since", help="Lower bound date YYYY-MM-DD (week end >= since)")
    ap.add_argument("--until", help="Upper bound date YYYY-MM-DD (week start <= until)")
    ap.add_argument("--regex", action="store_true", help="Treat query as regex (default is literal substring, case-insensitive)")
    ap.add_argument("--limit", type=int, default=50, help="Max number of hit lines to print (default: %(default)s)")
    ap.add_argument("--list-weeks", action="store_true", help="Just list available week dirs and exit")
    args = ap.parse_args()

    weeks = list_week_dirs(args.root)
    if not weeks:
        print(f"No week directories found under {args.root}.", file=sys.stderr)
        print("Clone the archive first:", file=sys.stderr)
        print("  gh repo clone nishio/oss_weekly_reporter /tmp/oss_weekly_reporter -- --depth 1 --branch data --single-branch", file=sys.stderr)
        return 2

    if args.list_weeks:
        for w in weeks:
            print(w.name)
        return 0

    if not args.query:
        ap.error("query is required unless --list-weeks is given")

    flags = 0 if args.regex else re.IGNORECASE
    raw_pat = args.query if args.regex else re.escape(args.query)
    pattern = re.compile(raw_pat, flags)

    total = 0
    for week in weeks:
        if not in_date_range(week.name, args.since, args.until):
            continue
        for path in iter_files_for_layer(week, args.layer):
            if path.suffix == ".json":
                results = [(loc, snip) for loc, snip in search_json_file(path, pattern)]
                for loc, snip in results:
                    rel = path.relative_to(args.root)
                    print(f"{week.name}/{rel.relative_to(week.name)}  {loc}\n    {snip}")
                    total += 1
                    if total >= args.limit:
                        print(f"\n[stopped at --limit {args.limit}]", file=sys.stderr)
                        return 0
            else:
                results = search_text_file(path, pattern)
                for lineno, snip in results:
                    rel = path.relative_to(args.root)
                    print(f"{week.name}/{rel.relative_to(week.name)}:{lineno}\n    {snip}")
                    total += 1
                    if total >= args.limit:
                        print(f"\n[stopped at --limit {args.limit}]", file=sys.stderr)
                        return 0

    if total == 0:
        print("(no matches)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
