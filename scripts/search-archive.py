#!/usr/bin/env python3
"""Search helper for dd2030 external archives.

Default source:
  digitaldemocracy2030/slack-logs
  local clone root: /tmp/slack-logs

Use --source oss-weekly-reporter for the legacy weekly AI/GitHub archive:
  nishio/oss_weekly_reporter data branch
  local data root: /tmp/oss_weekly_reporter/data

Typical use:
  # Search recent Slack mirror logs
  python3 scripts/search-archive.py "Discord"

  # Search monthly canonical Slack logs
  python3 scripts/search-archive.py --layer raw --month 2026-04 "熟議"

  # List Slack channels available in the latest mirror metadata
  python3 scripts/search-archive.py --list-channels

  # Restrict Slack search by channel id or channel name substring
  python3 scripts/search-archive.py --channel コアループ "提言"

  # Search legacy weekly AI reports
  python3 scripts/search-archive.py --source oss-weekly-reporter --layer ai_reports "Polimoney"

  # List legacy weekly snapshot directories
  python3 scripts/search-archive.py --source oss-weekly-reporter --list-weeks

The script does not modify the archives. It prints matches with enough
context to decide which file to open next.
"""

from __future__ import annotations

import argparse
import gzip
import json
import re
import sys
from pathlib import Path
from typing import Iterable

DEFAULT_SLACK_LOGS_ROOT = Path("/tmp/slack-logs")
DEFAULT_OSS_ROOT = Path("/tmp/oss_weekly_reporter/data")

SOURCES = ("slack-logs", "oss-weekly-reporter")
SLACK_LAYERS = ("mirror", "raw")
OSS_LAYERS = ("ai_reports", "markdown", "raw")


def compile_pattern(query: str, regex: bool) -> re.Pattern[str]:
    flags = 0 if regex else re.IGNORECASE
    raw_pat = query if regex else re.escape(query)
    return re.compile(raw_pat, flags)


def shorten(text: str, limit: int = 220) -> str:
    snippet = text.replace("\n", " ").strip()
    if len(snippet) > limit:
        snippet = snippet[:limit] + "..."
    return snippet


def iter_string_values(item: object) -> Iterable[str]:
    if isinstance(item, str):
        yield item
    elif isinstance(item, dict):
        for value in item.values():
            yield from iter_string_values(value)
    elif isinstance(item, list):
        for value in item:
            yield from iter_string_values(value)


def resolve_root(source: str, root: Path | None) -> Path:
    if root is not None:
        resolved = root
    elif source == "slack-logs":
        resolved = DEFAULT_SLACK_LOGS_ROOT
    else:
        resolved = DEFAULT_OSS_ROOT

    if source == "oss-weekly-reporter" and (resolved / "data").is_dir():
        return resolved / "data"
    return resolved


def clone_hint(source: str) -> str:
    if source == "slack-logs":
        return "gh repo clone digitaldemocracy2030/slack-logs /tmp/slack-logs -- --depth 1"
    return (
        "gh repo clone nishio/oss_weekly_reporter /tmp/oss_weekly_reporter -- "
        "--depth 1 --branch data --single-branch"
    )


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


def iter_oss_files_for_layer(week_dir: Path, layer: str):
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


def search_text_file(path: Path, pattern: re.Pattern[str]) -> list[tuple[int, str]]:
    hits: list[tuple[int, str]] = []
    try:
        with path.open(encoding="utf-8") as fh:
            for i, line in enumerate(fh, 1):
                if pattern.search(line):
                    hits.append((i, shorten(line)))
    except (OSError, UnicodeDecodeError):
        pass
    return hits


def search_json_file(path: Path, pattern: re.Pattern[str]) -> list[tuple[str, str]]:
    """Search legacy Slack/GitHub JSON. Returns (locator, snippet) tuples."""
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
        for field in ("text_readable", "text", "title", "body"):
            value = item.get(field)
            if isinstance(value, str) and pattern.search(value):
                if "ts" in item:
                    locator = f"[{idx}] ts={item.get('ts')} user={item.get('user_name', item.get('user', '?'))}"
                elif "number" in item:
                    locator = f"[{idx}] #{item.get('number')} ({item.get('type', '?')}) {item.get('user', '?')}"
                else:
                    locator = f"[{idx}]"
                hits.append((locator, f"{field}: {shorten(value)}"))
                break
    return hits


def read_slack_channel_meta(path: Path) -> tuple[str, str]:
    """Return (channel_id, channel_name) from a Slack jsonl.gz file."""
    channel_id = path.parent.name if path.parent.name != "slack" else path.name.removesuffix(".jsonl.gz")
    channel_name = "?"

    try:
        with gzip.open(path, "rt", encoding="utf-8") as fh:
            for _, line in zip(range(20), fh):
                try:
                    item = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if not isinstance(item, dict):
                    continue

                if "channel_id" in item:
                    channel_id = str(item.get("channel_id") or channel_id)
                if "channel_name" in item:
                    channel_name = str(item.get("channel_name") or channel_name)
                if channel_name != "?" and channel_id != "?":
                    break
    except OSError:
        pass

    return channel_id, channel_name


def slack_channel_matches(path: Path, root: Path, channel: str) -> bool:
    channel_lower = channel.lower()
    channel_id, channel_name = read_slack_channel_meta(path)
    haystacks = [
        channel_id,
        channel_name,
        path.name,
        path.parent.name,
        str(path),
    ]
    try:
        haystacks.append(str(path.relative_to(root)))
    except ValueError:
        pass
    return any(channel_lower in value.lower() for value in haystacks)


def iter_slack_log_files(root: Path, layer: str, month: str | None, channel: str | None) -> Iterable[Path]:
    if layer == "mirror":
        files = sorted((root / "mirror" / "slack").glob("*.jsonl.gz"))
    else:
        files = sorted((root / "raw" / "slack").glob("*/*.jsonl.gz"))
        if month:
            files = [p for p in files if p.name == f"{month}.jsonl.gz"]

    if channel:
        files = [p for p in files if slack_channel_matches(p, root, channel)]
    yield from files


def search_slack_jsonl_gz(path: Path, root: Path, pattern: re.Pattern[str]) -> list[tuple[str, str]]:
    hits: list[tuple[str, str]] = []
    channel_id = path.parent.name if path.parent.name != "slack" else path.name.removesuffix(".jsonl.gz")
    channel_name = "?"

    try:
        with gzip.open(path, "rt", encoding="utf-8") as fh:
            for lineno, line in enumerate(fh, 1):
                try:
                    item = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if not isinstance(item, dict):
                    continue

                if "channel_name" in item:
                    channel_name = str(item.get("channel_name") or channel_name)
                if "channel_id" in item:
                    channel_id = str(item.get("channel_id") or channel_id)

                searchable = " ".join(iter_string_values(item))
                if not pattern.search(searchable):
                    continue

                rel = path.relative_to(root)
                text = item.get("text")
                if not isinstance(text, str) or not text.strip():
                    text = searchable
                ts = item.get("ts", "?")
                user = item.get("user") or item.get("username") or item.get("bot_id") or "?"
                locator = f"{rel}:{lineno} channel={channel_name}({channel_id}) ts={ts} user={user}"
                hits.append((locator, shorten(text)))
    except OSError:
        return hits

    return hits


def list_slack_channels(root: Path) -> int:
    sync_path = root / "mirror" / "sync.json"
    if sync_path.exists():
        try:
            data = json.loads(sync_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            data = {}
        channels = data.get("channels") if isinstance(data, dict) else None
        if isinstance(channels, list):
            for ch in channels:
                if isinstance(ch, dict):
                    channel_id = ch.get("id") or ch.get("channel_id") or "?"
                    name = ch.get("name") or ch.get("channel_name") or "?"
                    print(f"{channel_id}\t{name}")
            return 0

    for path in sorted((root / "mirror" / "slack").glob("*.jsonl.gz")):
        channel_id, channel_name = read_slack_channel_meta(path)
        print(f"{channel_id}\t{channel_name}")
    return 0


def search_slack_logs(args: argparse.Namespace, root: Path) -> int:
    if not root.exists():
        print(f"No slack-logs clone found under {root}.", file=sys.stderr)
        print("Clone it first:", file=sys.stderr)
        print(f"  {clone_hint('slack-logs')}", file=sys.stderr)
        return 2

    if args.list_channels:
        return list_slack_channels(root)

    if args.list_weeks:
        print("--list-weeks is only valid with --source oss-weekly-reporter", file=sys.stderr)
        return 2

    if not args.query:
        raise SystemExit("query is required unless --list-channels is given")

    layers = SLACK_LAYERS if args.layer == "all" else (args.layer,)
    unknown = [layer for layer in layers if layer not in SLACK_LAYERS]
    if unknown:
        print(f"Invalid layer for slack-logs: {', '.join(unknown)}. Use mirror, raw, or all.", file=sys.stderr)
        return 2

    if args.month and not re.match(r"^\d{4}-\d{2}$", args.month):
        print("--month must be YYYY-MM", file=sys.stderr)
        return 2

    pattern = compile_pattern(args.query, args.regex)
    total = 0
    for layer in layers:
        for path in iter_slack_log_files(root, layer, args.month, args.channel):
            for locator, snippet in search_slack_jsonl_gz(path, root, pattern):
                print(f"{locator}\n    {snippet}")
                total += 1
                if total >= args.limit:
                    print(f"\n[stopped at --limit {args.limit}]", file=sys.stderr)
                    return 0

    if total == 0:
        print("(no matches)", file=sys.stderr)
    return 0


def search_oss_weekly(args: argparse.Namespace, root: Path) -> int:
    weeks = list_week_dirs(root)
    if not weeks:
        print(f"No week directories found under {root}.", file=sys.stderr)
        print("Clone the archive first:", file=sys.stderr)
        print(f"  {clone_hint('oss-weekly-reporter')}", file=sys.stderr)
        return 2

    if args.list_channels:
        print("--list-channels is only valid with --source slack-logs", file=sys.stderr)
        return 2

    if args.list_weeks:
        for week in weeks:
            print(week.name)
        return 0

    if not args.query:
        raise SystemExit("query is required unless --list-weeks is given")

    layers = OSS_LAYERS if args.layer == "all" else (args.layer,)
    unknown = [layer for layer in layers if layer not in OSS_LAYERS]
    if unknown:
        print(f"Invalid layer for oss-weekly-reporter: {', '.join(unknown)}. Use ai_reports, markdown, raw, or all.", file=sys.stderr)
        return 2

    pattern = compile_pattern(args.query, args.regex)
    total = 0
    for week in weeks:
        if not in_date_range(week.name, args.since, args.until):
            continue
        for layer in layers:
            for path in iter_oss_files_for_layer(week, layer):
                rel = path.relative_to(root)
                inner = rel.relative_to(week.name)
                if path.suffix == ".json":
                    results = search_json_file(path, pattern)
                    for loc, snip in results:
                        print(f"{week.name}/{inner}  {loc}\n    {snip}")
                        total += 1
                        if total >= args.limit:
                            print(f"\n[stopped at --limit {args.limit}]", file=sys.stderr)
                            return 0
                else:
                    results = search_text_file(path, pattern)
                    for lineno, snip in results:
                        print(f"{week.name}/{inner}:{lineno}\n    {snip}")
                        total += 1
                        if total >= args.limit:
                            print(f"\n[stopped at --limit {args.limit}]", file=sys.stderr)
                            return 0

    if total == 0:
        print("(no matches)", file=sys.stderr)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query", nargs="?", help="Keyword or regex")
    ap.add_argument("--source", choices=SOURCES, default="slack-logs", help="Archive source (default: %(default)s)")
    ap.add_argument("--root", type=Path, help="Archive root. Defaults depend on --source.")
    ap.add_argument("--layer", default="mirror", help="Layer to search. slack-logs: mirror/raw/all. oss: ai_reports/markdown/raw/all.")
    ap.add_argument("--month", help="For slack-logs raw search: YYYY-MM")
    ap.add_argument("--channel", help="Restrict slack-logs search to a channel id, channel name, or path substring")
    ap.add_argument("--since", help="For oss-weekly-reporter: lower bound date YYYY-MM-DD (week end >= since)")
    ap.add_argument("--until", help="For oss-weekly-reporter: upper bound date YYYY-MM-DD (week start <= until)")
    ap.add_argument("--regex", action="store_true", help="Treat query as regex (default is literal substring, case-insensitive)")
    ap.add_argument("--limit", type=int, default=50, help="Max number of hit lines to print (default: %(default)s)")
    ap.add_argument("--list-channels", action="store_true", help="For slack-logs: list channels from mirror metadata")
    ap.add_argument("--list-weeks", action="store_true", help="For oss-weekly-reporter: list available week dirs")
    args = ap.parse_args()

    if args.source == "oss-weekly-reporter" and args.layer == "mirror":
        args.layer = "ai_reports"

    root = resolve_root(args.source, args.root)
    if args.source == "slack-logs":
        return search_slack_logs(args, root)
    return search_oss_weekly(args, root)


if __name__ == "__main__":
    sys.exit(main())
