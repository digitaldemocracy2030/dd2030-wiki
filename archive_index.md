# Archive Index — 外部アーカイブの参照ガイド

dd2030-wiki は基本的に `raw/` の資料だけを ingest して `wiki/` を生成するが、それとは別に **大量の Slack/GitHub ログを持つ外部リポジトリ** を「検索ベースで部分的に読む」ためのアーカイブとして扱う。

このファイルは、その外部アーカイブが何で、どこにあって、どう読めばいいかを書く。

## アーカイブ本体

- **リポジトリ**: [`nishio/oss_weekly_reporter`](https://github.com/nishio/oss_weekly_reporter)
- **ブランチ**: `data`（コードは `main` だが、ログデータは `data` ブランチにある）
- **想定 clone 先**: `/tmp/oss_weekly_reporter/`（一時的に使う前提）

```bash
gh repo clone nishio/oss_weekly_reporter /tmp/oss_weekly_reporter -- \
  --depth 1 --branch data --single-branch
```

更新を取り込むときは `cd /tmp/oss_weekly_reporter && git pull`。

## 配置されているデータ

`data/` 配下に **週次スナップショット**ディレクトリが並ぶ（2025-03 〜 2026-05、約14ヶ月、67ディレクトリ、合計 117MB）。

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

### Slack チャンネル一覧（おおよそ）

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

1. **`ai_reports/slack.md` をまず読む** — 各週5KB 程度。67週分でも全部読むのは現実的。「いつ何があったか」のインデックスとして使う
2. **`markdown/slack/all_summary.md` を次に読む** — チャンネル横断の整形済みログ。grep で発言検索
3. **`raw/slack/<channel>.json` は最後** — 特定発言の正確なタイムスタンプ・thread構造・user_id が必要な時のみ。`scripts/search-archive.py` 経由で抽出する

GitHub 側も同様に `ai_reports/<repo>.md` → `markdown/github/github_report-<repo>.md` → `raw/github/<repo>.json` の順で。

## wiki への取り込みルール

- アーカイブから引用して wiki ページを書く時は、出典として **週ディレクトリ名 + ファイルパス** を残す。例: `(出典: oss_weekly_reporter/data/2025-12-24_to_2025-12-31/ai_reports/slack.md)`
- 個人の雑談・私的な発言は wiki に持ち込まない（CLAUDE.md「dd2030プロジェクト固有の注意」）
- アーカイブ自体は **dd2030-wiki リポジトリには含めない**。Quartz で公開する wiki に Slack の生発言を載せるとプライバシー事故になるため、構造的に分離している

## 検索ヘルパー

- `python3 scripts/search-archive.py --help` でアーカイブ全体に対する keyword 検索ができる
- 詳細は [scripts/search-archive.py](scripts/search-archive.py) のヘッダコメント
