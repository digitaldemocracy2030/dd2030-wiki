#!/usr/bin/env python3
"""dd2030 の「最近の動き」を一度に集めて、Wiki に未反映のものを見つけるための下調べスクリプト。

やること（raw/ を書き換えるのは議事録の再取得だけで、--no-apply-minutes で止められる）:

  1. Slack   work/slack-logs を pull し、mirror の直近メッセージをチャンネル別・人名解決済みで一覧にする
  2. 議事録  CLAUDE.md の Google Docs 6本を再取得し、raw/minutes/ の現行版と比べて新しい冒頭部分を抜き出す
  3. GitHub  主要リポジトリのリリース・コミット数・merged PR・新規 Issue を期間で集める
  4. 照合    Slack で共有された URL が wiki/ に既に出ているかを突き合わせ、wiki/log.md の直近エントリを添える

結果は work/catch-up/<日付>/report.md（git 管理外）に書き、標準出力にも出す。

使い方:
  python3 scripts/catch-up.py                 # wiki/log.md の最新エントリ日から今日まで
  python3 scripts/catch-up.py --since 2026-10-26
  python3 scripts/catch-up.py --days 7 --no-github
  python3 scripts/catch-up.py --no-apply-minutes   # 議事録は work/ に落とすだけで raw/ を触らない
"""

from __future__ import annotations

import argparse
import datetime as dt
import gzip
import json
import re
import shutil
import subprocess
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
WORK = REPO_ROOT / "work"
SLACK_ROOT = WORK / "slack-logs"
MIRROR = SLACK_ROOT / "mirror"
JST = dt.timezone(dt.timedelta(hours=9))
BOM = "\N{ZERO WIDTH NO-BREAK SPACE}"

MINUTES = {
    "weekly-general-meeting": "1tBhaer67U9LbASfqPrg0rpmv0Tt4K7zFUTTzscKXj_I",
    "community-operations": "1dn9R9WLaGNMDO-t1w7m8-2gZRSrgZI4glDvSIr101J4",
    "broad-listening-book-meeting": "1plggszRTxEEYUcZuCLiHkPrBsMtxr3RQpctKtZe5y4M",
    "project-coreloop": "1isqRSUvvympiNp8uKBWYHIAI8-CGNjePriZUfrN4qig",
    "polimoney": "19Kn6ekK3twMVcVaSyUgptvmfzrXEJezA6GXTbPXjm9M",
    "idobata-project": "1cK5i3ATo1OXsy-oicllY6-YlI-q0AJVtqQW7a71V-AU",
}

DEFAULT_REPOS = [
    "digitaldemocracy2030/kouchou-ai",
    "digitaldemocracy2030/website",
    "digitaldemocracy2030/idobata",
    "digitaldemocracy2030/polimoney",
    "digitaldemocracy2030/polimoney_hub",
    "digitaldemocracy2030/broad-listening-book",
    "digitaldemocracy2030/coreloop-ref-fraudbuster",
    "digitaldemocracy2030/slack-logs",
]

# 本文が bot 通知だけのチャンネル（GitHub 連携など）は既定で省く
SKIP_CHANNEL_PATTERNS = (r"_github$",)

# URL 照合で無視するもの（会議リンク、議事録 Doc 自身、Slack 内リンク）
SKIP_URL_PARTS = (
    "slack.com/archives",
    "dd2030.slack.com",
    "meet.google.com",
    *(f"docs.google.com/document/d/{i}" for i in MINUTES.values()),
)


def run(cmd: list[str], check: bool = True, timeout: int = 120) -> str:
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if check and p.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd)}\n{p.stderr.strip()}")
    return p.stdout


def last_log_date() -> dt.date | None:
    log = REPO_ROOT / "wiki" / "log.md"
    if not log.exists():
        return None
    for line in log.read_text(encoding="utf-8").splitlines():
        m = re.match(r"## \[(\d{4}-\d{2}-\d{2})\]", line)
        if m:
            return dt.date.fromisoformat(m.group(1))
    return None


# ---------------------------------------------------------------- Slack

def ensure_slack_logs(pull: bool) -> str:
    if not SLACK_ROOT.exists():
        WORK.mkdir(exist_ok=True)
        run(["gh", "repo", "clone", "digitaldemocracy2030/slack-logs", str(SLACK_ROOT), "--", "--depth", "1"], timeout=600)
        return "cloned"
    if pull:
        out = run(["git", "-C", str(SLACK_ROOT), "pull", "--ff-only"], check=False, timeout=600)
        return "already up to date" if "Already up to date" in out else "pulled"
    return "not pulled"


def slack_section(since: dt.date, maxlen: int, include_bots: bool) -> tuple[list[str], set[str]]:
    sync = json.loads((MIRROR / "sync.json").read_text(encoding="utf-8"))
    names = {c["id"]: c["name"] for c in sync["channels"]}
    users = {}
    for u in json.load(open(MIRROR / "users.json", encoding="utf-8"))["members"]:
        if isinstance(u, dict):
            users[u.get("id")] = u.get("real_name") or u.get("name") or u.get("id")
    since_ts = dt.datetime.combine(since, dt.time(0, 0), tzinfo=JST).timestamp()
    lines = [f"## Slack（mirror synced_at={sync['synced_at']}、{since} 以降）", ""]
    urls: set[str] = set()
    total = 0
    for path in sorted(MIRROR.glob("slack/*.jsonl.gz")):
        ch_id = path.name.split(".")[0]
        ch = names.get(ch_id, ch_id)
        if not include_bots and any(re.search(p, ch) for p in SKIP_CHANNEL_PATTERNS):
            continue
        msgs = []
        with gzip.open(path, "rt", encoding="utf-8") as f:
            f.readline()  # 1行目はチャンネルのメタデータ
            for line in f:
                m = json.loads(line)
                if float(m.get("ts", 0)) < since_ts:
                    continue
                if not include_bots and not m.get("text", "").strip():
                    continue
                msgs.append(m)
        if not msgs:
            continue
        msgs.sort(key=lambda m: float(m["ts"]))
        total += len(msgs)
        lines.append(f"### #{ch}（{len(msgs)}件）")
        lines.append("")
        for m in msgs:
            t = dt.datetime.fromtimestamp(float(m["ts"]), JST).strftime("%m-%d %H:%M")
            u = users.get(m.get("user"), m.get("user") or m.get("username") or m.get("bot_id") or "?")
            txt = re.sub(r"<@(\w+)>", lambda mo: "@" + str(users.get(mo.group(1), mo.group(1))), m.get("text", ""))
            for raw in re.findall(r"<(https?://[^>|]+)", txt):
                urls.add(raw.replace("&amp;", "&"))
            txt = re.sub(r"<(https?://[^>|]+)\|[^>]*>", r"\1", txt)
            txt = txt.replace("\n", " ⏎ ")
            thr = "  ↳" if m.get("thread_ts") and m.get("thread_ts") != m.get("ts") else ""
            rc = f" [replies:{m['reply_count']}]" if m.get("reply_count") else ""
            if len(txt) > maxlen:
                txt = txt[:maxlen] + "…"
            lines.append(f"- {t}{thr} **{u}**{rc}: {txt}")
        lines.append("")
    lines.insert(2, f"合計 {total} 件（bot 通知チャンネルと本文なしを除く）")
    lines.insert(3, "")
    return lines, urls


# -------------------------------------------------------------- Minutes

def fetch_doc(doc_id: str) -> bytes:
    url = f"https://docs.google.com/document/d/{doc_id}/export?format=txt"
    with urllib.request.urlopen(url, timeout=60) as r:
        return r.read()


def norm(b: bytes) -> str:
    """比較・切り出し用。保存は元のバイト列のまま（curl での取得と同じ結果になる）。"""
    return b.decode("utf-8", errors="replace").replace("\r\n", "\n").lstrip(BOM)


def new_head(old: str, new: str, max_lines: int) -> tuple[str, bool]:
    """議事録は新しい回が先頭に足されるので、旧版の先頭行が新版のどこにあるかで新規部分を切り出す。"""
    anchor = next((l.strip() for l in old.splitlines() if len(l.strip()) >= 8), None)
    if anchor and anchor in new:
        head = new[: new.index(anchor)].rstrip()
        if not head:
            return "", True
        lines = head.splitlines()
        more = len(lines) > max_lines
        return "\n".join(lines[:max_lines]) + ("\n…（続きあり）" if more else ""), True
    return "", False


def minutes_section(outdir: Path, apply: bool, max_lines: int) -> list[str]:
    lines = ["## 議事録（Google Docs 再取得）", ""]
    mdir = outdir / "minutes"
    mdir.mkdir(parents=True, exist_ok=True)
    for name, doc_id in MINUTES.items():
        raw_path = REPO_ROOT / "raw" / "minutes" / f"{name}.txt"
        try:
            new = fetch_doc(doc_id)
        except Exception as e:  # noqa: BLE001
            lines.append(f"- **{name}**: 取得失敗 {e}")
            continue
        (mdir / f"{name}.txt").write_bytes(new)
        old = raw_path.read_bytes() if raw_path.exists() else b""
        if old == new:
            lines.append(f"- **{name}**: 変更なし")
            continue
        old_t, new_t = norm(old), norm(new)
        head, found = new_head(old_t, new_t, max_lines)
        delta = len(new_t.splitlines()) - len(old_t.splitlines())
        state = "raw/minutes/ を上書き" if apply else "work/ に保存のみ"
        lines.append(f"- **{name}**: 変更あり（行数差 {delta:+d}、{state}）")
        if found and head:
            lines.append("")
            lines.append("  新しい冒頭部分:")
            lines.append("")
            lines.append("  ```")
            lines.extend("  " + l for l in head.splitlines())
            lines.append("  ```")
        elif found:
            lines.append("  冒頭に追記はない（既存の回の本文が編集された）。`diff` で確認する")
        else:
            lines.append("  旧版の先頭行が見つからず差分を切り出せない。`diff` で確認する")
        if apply:
            shutil.copyfile(mdir / f"{name}.txt", raw_path)
        lines.append("")
    lines.append("")
    return lines


# --------------------------------------------------------------- GitHub

def gh_json(args: list[str]) -> list | dict | None:
    out = run(["gh", *args], check=False, timeout=120)
    try:
        return json.loads(out) if out.strip() else None
    except json.JSONDecodeError:
        return None


def github_repo(repo: str, since: dt.date) -> list[str]:
    since_iso = f"{since.isoformat()}T00:00:00Z"
    rel = gh_json(["api", f"repos/{repo}/releases?per_page=10"]) or []
    rel = [r for r in rel if isinstance(r, dict) and (r.get("published_at") or "") >= since_iso]
    commits = gh_json(["api", f"repos/{repo}/commits?since={since_iso}&per_page=100"]) or []
    n_commits = len(commits) if isinstance(commits, list) else 0
    prs = gh_json(["pr", "list", "--repo", repo, "--state", "merged", "--search", f"merged:>={since.isoformat()}",
                   "--json", "number,title,mergedAt,author", "--limit", "100"]) or []
    issues = gh_json(["issue", "list", "--repo", repo, "--state", "all", "--search", f"created:>={since.isoformat()}",
                      "--json", "number,title,createdAt,author,state", "--limit", "100"]) or []
    if not (rel or n_commits or prs or issues):
        return [f"- **{repo}**: 動きなし"]
    lines = [f"- **{repo}**: commits {n_commits}{'+' if n_commits >= 100 else ''}、merged PR {len(prs)}、新規 Issue {len(issues)}"]
    for r in rel:
        lines.append(f"  - release **{r.get('tag_name')}** {r.get('published_at', '')[:10]} {r.get('name', '')} {r.get('html_url', '')}")
    for p in prs[:15]:
        lines.append(f"  - PR #{p['number']} {p['mergedAt'][:10]} {p['title']}（{p.get('author', {}).get('login', '?')}）")
    if len(prs) > 15:
        lines.append(f"  - …ほか merged PR {len(prs) - 15} 件")
    for i in issues[:15]:
        lines.append(f"  - Issue #{i['number']} {i['createdAt'][:10]} [{i['state']}] {i['title']}（{i.get('author', {}).get('login', '?')}）")
    if len(issues) > 15:
        lines.append(f"  - …ほか新規 Issue {len(issues) - 15} 件")
    return lines


def github_section(repos: list[str], since: dt.date) -> list[str]:
    lines = [f"## GitHub（{since} 以降）", ""]
    with ThreadPoolExecutor(max_workers=4) as ex:
        for part in ex.map(lambda r: github_repo(r, since), repos):
            lines.extend(part)
    lines.append("")
    return lines


# ----------------------------------------------------------- Wiki check

def wiki_section(urls: set[str]) -> list[str]:
    wiki_text = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in (REPO_ROOT / "wiki").rglob("*.md"))
    lines = ["## Wiki との照合", ""]
    log = REPO_ROOT / "wiki" / "log.md"
    heads = [l for l in log.read_text(encoding="utf-8").splitlines() if l.startswith("## [")][:3]
    lines.append("wiki/log.md の直近エントリ:")
    lines.extend(f"- {h[3:]}" for h in heads)
    lines.append("")
    if urls:
        lines.append("Slack で共有された URL（✓ = wiki に既出、✗ = 未出）:")
        for u in sorted(urls):
            if any(s in u for s in SKIP_URL_PARTS):
                continue
            key = re.sub(r"^https?://(www\.)?", "", u).rstrip("/").split("#")[0]
            mark = "✓" if key and key in wiki_text else "✗"
            lines.append(f"- {mark} {u}")
        lines.append("")
    return lines


# ----------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--since", help="この日付（JST）以降を対象にする。省略時は wiki/log.md の最新エントリ日")
    ap.add_argument("--days", type=int, help="--since の代わりに、今日から N 日前以降を対象にする")
    ap.add_argument("--out", help="出力ディレクトリ（既定: work/catch-up/<今日>）")
    ap.add_argument("--repos", help="GitHub リポジトリをカンマ区切りで指定（既定: 主要8リポジトリ）")
    ap.add_argument("--maxlen", type=int, default=400, help="Slack 1件あたりの表示文字数")
    ap.add_argument("--minutes-lines", type=int, default=80, help="議事録の新規冒頭部分を何行まで載せるか")
    ap.add_argument("--include-bots", action="store_true", help="bot 通知チャンネルと本文なしメッセージも載せる")
    ap.add_argument("--no-slack", action="store_true")
    ap.add_argument("--no-pull", action="store_true", help="slack-logs を pull しない")
    ap.add_argument("--no-minutes", action="store_true")
    ap.add_argument("--no-apply-minutes", action="store_true", help="議事録を raw/minutes/ に上書きしない")
    ap.add_argument("--no-github", action="store_true")
    a = ap.parse_args()

    today = dt.datetime.now(JST).date()
    if a.days:
        since = today - dt.timedelta(days=a.days)
    elif a.since:
        since = dt.date.fromisoformat(a.since)
    else:
        since = last_log_date() or (today - dt.timedelta(days=7))

    outdir = Path(a.out) if a.out else WORK / "catch-up" / today.isoformat()
    outdir.mkdir(parents=True, exist_ok=True)

    report = [f"# dd2030 catch-up report（{today}、対象: {since} 以降）", ""]
    urls: set[str] = set()

    if not a.no_slack:
        try:
            state = ensure_slack_logs(pull=not a.no_pull)
            report.append(f"slack-logs: {state}")
            report.append("")
            sec, urls = slack_section(since, a.maxlen, a.include_bots)
            report.extend(sec)
        except Exception as e:  # noqa: BLE001
            report.append(f"## Slack: 失敗 {e}")
            report.append("")

    if not a.no_minutes:
        report.extend(minutes_section(outdir, apply=not a.no_apply_minutes, max_lines=a.minutes_lines))

    if not a.no_github:
        repos = a.repos.split(",") if a.repos else DEFAULT_REPOS
        report.extend(github_section(repos, since))

    report.extend(wiki_section(urls))

    text = "\n".join(report)
    (outdir / "report.md").write_text(text, encoding="utf-8")
    print(text)
    print(f"\n（保存先: {outdir / 'report.md'}）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
