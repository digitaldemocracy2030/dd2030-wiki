---
title: Slackログアーカイブ
aliases: [Slackログアーカイブ, slack-log-archive, Slack チャットログ]
tags: [dd2030, tooling, archive, slack]
sources:
  - digitaldemocracy2030/slack-logs/README.md
  - digitaldemocracy2030/slack-logs/mirror/sync.json
created: 2026-06-30
updated: 2026-07-09
---

# Slackログアーカイブ

dd2030 の Slack public channel ログは、dd2030-wiki には直接取り込まず、外部リポジトリ [`digitaldemocracy2030/slack-logs`](https://github.com/digitaldemocracy2030/slack-logs) に置く。wiki では、個別発言をそのまま転載するのではなく、必要な範囲を検索して要約・整理して使う。

## 現在の構成

| 層 | パス | 用途 |
|---|---|---|
| 月次 canonical | `raw/slack/<channel_id>/<YYYY-MM>.jsonl.gz` | 過去の議論を確実に辿る。スレッド完全性を優先するため遅延あり |
| rolling mirror | `mirror/slack/<channel_id>.jsonl.gz` | 直近14日程度の現状確認。6時間ごとに上書き更新 |
| 同期メタデータ | `mirror/sync.json` | 最終同期時刻、対象チャンネル、件数を見る |
| ユーザー情報 | `mirror/users.json`, `state/users-<YYYY-MM>.json` | user_id を表示名に解決する |

2026-06-30 時点で確認した mirror は、58チャンネル・506メッセージ・14日 window（`2026-06-16T04:12:50Z` 〜 `2026-06-30T04:12:50Z`）を持つ。

同日時点で、`raw/slack/*/2025-01.jsonl.gz` から `2026-02.jsonl.gz` までの月次canonicalは各チャンネルのメタデータのみで、本文メッセージは入っていなかった。2026年3月・4月には本文メッセージが入っているため、過去月を調べるときは「月次ファイルが存在する」だけでなく、本文行があるかを確認する。本文がない期間のSlack根拠は、補助アーカイブの `oss_weekly_reporter/data/<week>/raw/slack/` や `markdown/slack/` を併用する。

## 読む順序

1. 直近の状況を知りたい時は `mirror/sync.json` で同期時刻と対象チャンネルを確認する。
2. 直近14日程度の発言は `mirror/slack/*.jsonl.gz` を検索する。
3. 過去月の議論は `raw/slack/<channel_id>/<YYYY-MM>.jsonl.gz` を検索する。
4. 月次canonicalに本文がない期間、または週次の要約や GitHub Issues/PR との横断整理が必要な場合は、補助アーカイブとして [[OSS Weekly Reporter]] を読む。

## 検索例

ローカル checkout は `/tmp` ではなく、このリポジトリ直下の `work/` に置く。`/tmp` は消える可能性があり、検索結果が空の時にデータ欠落と未checkoutを区別しにくくなる。

```bash
# 初回だけ clone
mkdir -p work
gh repo clone digitaldemocracy2030/slack-logs work/slack-logs -- --depth 1

# 直近 mirror を検索
python3 scripts/search-archive.py "キーワード"

# チャンネル名で絞って検索（IDでも可）
python3 scripts/search-archive.py --channel コアループ "提言"

# 過去月の canonical を検索
python3 scripts/search-archive.py --layer raw --month 2026-04 "キーワード"

# 月次ファイルに本文がない時は補助アーカイブを検索
python3 scripts/search-archive.py --source oss-weekly-reporter --layer raw --since 2025-10-22 --until 2025-10-29 "キーワード"

# チャンネル一覧
python3 scripts/search-archive.py --list-channels
```

詳細な運用手順は [archive_index.md](https://github.com/digitaldemocracy2030/dd2030-wiki/blob/main/archive_index.md) を参照。

## wiki に使う時の注意

- Slack の発言は、原則として要約・整理して使う。
- 個人の雑談や私的な内容は wiki に持ち込まない。
- 出典には `digitaldemocracy2030/slack-logs/raw/slack/...` または `digitaldemocracy2030/slack-logs/mirror/slack/...` のように、リポジトリ名とファイルパスを残す。
- `mirror/` は上書きされるため、長期的な根拠として残したい場合は `raw/` の月次 canonical を優先する。
- 月次canonicalに本文がない過去期間は、`oss_weekly_reporter` の週次 raw/markdown を補助根拠として使い、ページ内でその出典を明記する。

## 関連ページ

- [[dd2030 Wikiとは]] — このWikiがSlackログをどう要約・参照するかの前提
- [[topics/first-reader-guide|初めて読む人へ]] — Wiki全体と根拠ソースへの入り方
- [[sources/index|ソースカタログ]] — Wikiで参照している根拠ソースの入口
- [[sources/weekly-history-reports|週次Historyレポート]] — dd2030.org History 用に加工された週次レポート群
- [[sources/history-week33-20251029|週次History week33（2025-10-29）]] — 週次まとめを個別ソース化し、必要に応じてSlack canonicalで再確認する例
- [[events/2025-11-28-welcome-meet-3|ウェルカムミート#3]] — 2025年10月canonicalに本文がないため、補助アーカイブの週次rawログで告知本文を確認した例
- [[sources/history-week43-20260114|週次History week43（2026-01-14）]] — Coreloop・Polimoneyの週次まとめを個別ソース化した例
- [[sources/history-week50-20260415|週次History week50（2026-04-15）]] — raw/history終端週と、以後はslack-logsへ移る境界を確認する例
- [[初年度まとめ]] — `oss_weekly_reporter` 由来の初年度整理を、現在のSlack canonicalで再確認する対象
- [[AI から Slack ログを参照するパターン]] — 歴史的問い合わせと現状クエリの使い分け
- [[アーカイブパイプライン設計]] — なぜ data repo と workflow をこの形にしたか
- [[events/2026-06-21-coreloop-online-deliberation|コアループ オンライン熟議（2026-06-21）]] — mirror から当日運用を確認した例
- [[sources/archive-pipeline-design-note|アーカイブパイプライン設計メモ]] — raw/mirror構成の背景にある設計メモ要約
- [[sources/oss-weekly-reporter-handoff|OSS Weekly Reporter 移管Slackメモ]] — slack-logs移管の経緯ソース要約
- [[OSS Weekly Reporter]] — 週次AIレポートと GitHub Issues/PR 補助アーカイブ
- [[dd2030-wiki の dd2030 org 移行]] — Slackで出たWiki本体のorg移行相談と、旧URLを残す作業チェックリスト
