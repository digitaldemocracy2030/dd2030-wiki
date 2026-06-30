# Archive Index — 外部アーカイブの参照ガイド

dd2030-wiki は基本的に `raw/` の資料だけを ingest して `wiki/` を生成するが、それとは別に **大量の Slack/GitHub ログを持つ外部リポジトリ** を「検索ベースで部分的に読む」ためのアーカイブとして扱う。

このファイルは、その外部アーカイブが何で、どこにあって、どう読めばいいかを書く。2026-06-30 現在、Slack のチャットログ本体は `digitaldemocracy2030/slack-logs` を正とし、`nishio/oss_weekly_reporter` は週次AIレポートと GitHub Issues/PR データを読むための補助アーカイブとして扱う。

## アーカイブ本体（Slack チャットログ）

- **リポジトリ**: [`digitaldemocracy2030/slack-logs`](https://github.com/digitaldemocracy2030/slack-logs)
- **ブランチ**: `main`
- **想定 clone 先**: `/tmp/slack-logs/`（一時的に使う前提）

```bash
gh repo clone digitaldemocracy2030/slack-logs /tmp/slack-logs -- --depth 1
```

更新を取り込むときは `cd /tmp/slack-logs && git pull`。

## 配置されているデータ

`digitaldemocracy2030/slack-logs` は Slack public channel ログのためのリポジトリで、月次 canonical と rolling mirror の二層構成。

```
slack-logs/
├── raw/
│   └── slack/<channel_id>/<YYYY-MM>.jsonl.gz   # 月次 canonical（保全用）
├── mirror/
│   ├── slack/<channel_id>.jsonl.gz             # 直近14日程度の rolling snapshot
│   ├── sync.json                               # 最終同期時刻・対象チャンネル一覧
│   └── users.json                              # 最新 users.list snapshot
└── state/
    └── users-<YYYY-MM>.json                    # 月次 users.list snapshot
```

各 `.jsonl.gz` は 1行目が channel meta、2行目以降が Slack API の message/reply オブジェクト。本文は `text`、スレッドは `thread_ts` と `reply_count`、ユーザー名解決は `mirror/users.json` または `state/users-<YYYY-MM>.json` を使う。

## 補助アーカイブ（週次AIレポート / GitHub）

Slack の「チャットログ置き場」は上記 `digitaldemocracy2030/slack-logs` だが、以下が必要な場合は引き続き `nishio/oss_weekly_reporter` の data ブランチを読む:

- 週次単位の LLM 要約（`ai_reports/slack.md`）
- チャンネル横断で整形された週次 Markdown（`markdown/slack/all_summary.md`）
- GitHub Issues/PR の週次スナップショット（`raw/github/`, `markdown/github/`, `ai_reports/<repo>.md`）

- **リポジトリ**: [`nishio/oss_weekly_reporter`](https://github.com/nishio/oss_weekly_reporter)
- **ブランチ**: `data`
- **想定 clone 先**: `/tmp/oss_weekly_reporter/`

```bash
gh repo clone nishio/oss_weekly_reporter /tmp/oss_weekly_reporter -- \
  --depth 1 --branch data --single-branch
```

更新を取り込むときは `cd /tmp/oss_weekly_reporter && git pull`。

`/tmp/oss_weekly_reporter/data/` 配下に **週次スナップショット**ディレクトリが並ぶ（2025-03 〜 2026-05、約14ヶ月、67ディレクトリ、合計 117MB）。

ディレクトリ名は `YYYY-MM-DD_to_YYYY-MM-DD` 形式。一部 `*-2` のような重複ディレクトリがあるので注意（同期ジョブの再走で生成されたもの）。

各週は3層に積まれている:

```
2025-12-24_to_2025-12-31/
├── raw/                 # ナマのデータ
│   ├── slack/<channel>.json   # Slack API 形式（blocks/reactions/thread_ts 込み）
│   └── github/<repo>.json     # issues/PR の本文+メタデータ
├── markdown/            # 整形済み Markdown（人間可読）
│   ├── slack/all_summary.md
│   └── github/github_report-<repo>.md
└── ai_reports/          # LLM が生成したチャンネル/リポジトリ単位の週次サマリ
    ├── slack.md
    ├── kouchou-ai.md
    ├── idobata.md
    ├── polimoney.md
    └── website.md
```

### 旧アーカイブの Slack チャンネル一覧（おおよそ）

週によって増減があるが、典型的には以下が存在する:

- `0_全体お知らせ`
- `2_broad-listening-book`
- `2_開発_polimoney`, `2_開発_polimoney_ocr`
- `2_開発_広聴ai`, `2_開発_cartographer`, `2_開発_slackbot`
- `2_広報_pr`
- `2_いどばたp1_opt1_基本機能`
- `2_コミュニティ運営`
- `2_熟議民主主義プロセスやってみよう`
- `2_コアループ_*`（communication / policy / process / tech / オンライン広告詐欺対策など）
- `3_デジタル資産_権限管理`, `3_ボードメンバーロール`
- `7_雑談`, `7_x_投稿ネタ`
- `8_人数推移`

### GitHub リポジトリ一覧

各週の `raw/github/` には:

- `idobata.json` / `kouchou-ai.json` / `polimoney.json` / `website.json`
- 同名 `github_summary_*.json`（PR のサマリ）

## 読む順序のルール（重要）

LLM が context を爆発させずにこのアーカイブから情報を取るための順序:

### Slack チャットログ

1. **現状を知りたい時は `slack-logs/mirror/sync.json` をまず見る** — 対象チャンネル名、最終同期時刻、window を確認する
2. **直近の発言検索は `mirror/slack/*.jsonl.gz`** — `scripts/search-archive.py --source slack-logs --layer mirror <keyword>` で検索する
3. **チャンネルを絞る時は `--channel` を使う** — `--list-channels` で確認した channel id だけでなく、`--channel コアループ` のようにチャンネル名の一部でも絞れる
4. **過去月の発言検索は `raw/slack/<channel_id>/<YYYY-MM>.jsonl.gz`** — `scripts/search-archive.py --source slack-logs --layer raw --month YYYY-MM <keyword>` で検索する
5. **月次ファイルがメタデータだけの期間は補助アーカイブへ戻る** — 2026-06-30時点では `slack-logs/raw/slack/*/2025-01.jsonl.gz` 〜 `2026-02.jsonl.gz` は各チャンネル1行のメタデータのみで、本文は入っていなかった。2026年3月・4月は本文あり。古い出来事の告知本文などを確認する場合は `oss_weekly_reporter/data/<week>/raw/slack/` や `markdown/slack/` を併用する
6. **ユーザー名解決は `mirror/users.json` または `state/users-<YYYY-MM>.json`** — wiki へは個人の雑談・私的な発言を持ち込まない

### 週次AIレポート / GitHub

`nishio/oss_weekly_reporter` を読む時は、Slack 側は `ai_reports/slack.md` → `markdown/slack/all_summary.md` → `raw/slack/<channel>.json` の順に読む。GitHub 側も同様に `ai_reports/<repo>.md` → `markdown/github/github_report-<repo>.md` → `raw/github/<repo>.json` の順で。

## wiki への取り込みルール

- アーカイブから引用して wiki ページを書く時は、出典として **リポジトリ名 + ファイルパス** を残す。
  - slack-logs の例: `(出典: digitaldemocracy2030/slack-logs/raw/slack/C08F7JZPD63/2026-04.jsonl.gz)`
  - oss_weekly_reporter の例: `(出典: oss_weekly_reporter/data/2025-12-24_to_2025-12-31/ai_reports/slack.md)`
- 個人の雑談・私的な発言は wiki に持ち込まない（CLAUDE.md「dd2030プロジェクト固有の注意」）
- アーカイブ自体は **dd2030-wiki リポジトリには含めない**。Quartz で公開する wiki に Slack の生発言をそのまま載せるとプライバシー事故になるため、構造的に分離している

## 検索ヘルパー

- `python3 scripts/search-archive.py --help` で外部アーカイブに対する keyword 検索ができる
- 直近 Slack: `python3 scripts/search-archive.py --source slack-logs --layer mirror "キーワード"`
- チャンネル指定: `python3 scripts/search-archive.py --channel コアループ "提言"`
- 月次 Slack: `python3 scripts/search-archive.py --source slack-logs --layer raw --month 2026-04 "キーワード"`
- 週次AI/GitHub: `python3 scripts/search-archive.py --source oss-weekly-reporter --layer ai_reports "キーワード"`
- 詳細は [scripts/search-archive.py](scripts/search-archive.py) のヘッダコメント
