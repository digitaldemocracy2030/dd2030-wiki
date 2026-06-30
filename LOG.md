# LOG

## 2026-05-11（続き）

### 初年度（2025-03〜2026-03）まとめページの作成
- Explore エージェントで全67週の `ai_reports/slack.md` を月ごとに集約させ、それを骨子として `wiki/timeline/first-year.md` を新規作成
- 補強のため、`ai_reports` に章として現れていない or 取得対象に入っていない可能性のあるチャンネルを `raw/slack/` から直接サンプル抽出:
  - `2_新しいプロジェクトの種` — OSS Weekly Reporter 自体の発生（2025-04-02）、KJ法×広聴AI実験（2025-05、tsuzumik氏）、予測市場プロジェクト（2025-07）、ボイス効果議論（2025-08、中山心太氏）
  - `2_開発_cartographer` — 2025-10-22 新設、広聴AI/いどばた定例での実証
  - `7_広聴ai読書会` — 2025-06-11 vol.1（Plurality本）
  - `2_学生のためのデジタル民主主義` — 2025-05 高校公民授業モデル検討
- 「アーカイブのカバレッジ自体に穴がある」ことを末尾の `## 含まれていない可能性があるもの` セクションで明記
- `wiki/index.md` を更新: 「まずはここから」セクションに [[初年度まとめ]] を追加、末尾に外部アーカイブの参照案内セクションを追加

### 副次的に判明したこと
- `oss_weekly_reporter` の各週 `raw/slack/` は **公開全チャンネルではなく、設定された購読リスト**（直近の 2026-04-29 週で 11 チャンネル）。設定の変遷で取得対象が時期によって異なる
- 67週通算で 80+ 個の異なるチャンネル名が登場するが、これは累積であり、いずれかの時点でしか取得されていないチャンネルが多い

### アーカイブからの fill-back（3ページ追加）
アーカイブにあるが wiki に entity / concept ページがなかったものを 3 件追加:

- `wiki/entities/oss-weekly-reporter.md` — このアーカイブ自体を生んだプロジェクト。`2_新しいプロジェクトの種`（2025-04-02）での発生経緯、kuboon/gsheet-slack-logger から派生した構造、追跡対象が購読リスト方式である制約、dd2030 wiki との循環構造を記述
- `wiki/entities/cartographer.md` — 2025-10-22 立ち上がりの試作プロダクト。広聴AI/いどばた定例で実証中。「点推定問題」「訂正フェーズの欠落」「じぶんレポートをオンボーディングに使う案」等を整理
- `wiki/concepts/voice-effect.md` — 中山心太氏が 2025-08 に持ち込んだ「手続き的公正・ボイス効果」概念。ブロードリスニング系ツールの設計上の盲点を指摘した議論。西尾の「両方向トレーサビリティ」「うなづきリソース配分」再定式化、海外事例の参照（JOIN、Polis、オードリー・タンの「可視の応答責任」）も収録

`wiki/index.md` を更新して 3 ページを目次に追加。resolve-links と lint-wiki ともに broken link なしで通過。

## 2026-05-11

### Outline MCP（dd2030-docs.kbn.one）の検証
- kuboon さん設置の Outline インスタンス（v1.7.1）に対し MCP の挙動を調査
- `claude mcp add outline https://dd2030-docs.kbn.one/mcp -t http -s user -H "Authorization: Bearer ol_api_..."` で user scope に登録（`~/.claude.json`）
- 追加したスクリプト:
  - `scripts/outline_mcp.py` — MCP JSON-RPC 用の薄いラッパー（call_tool / call_tool_multi）
  - `scripts/import_test.py` — 2ページのインポート＋patch-mode 更新のスモークテスト
  - `scripts/link_convert_test.py` — `[[wiki-link]]` → `[name](/doc/...)` 変換テスト
- 検証は sandbox collection `import-test` を作成して実施し、終了後に collection ごと削除
- 主な発見:
  - **MCP `fetch` は本文 `text` を返さない**。読み戻しは `/api/documents.info` (REST) を使う必要がある
  - **`[[wiki-link]]` はエスケープされて素のテキストとして保存される**。リンク化するには事前に `[name](/doc/...)` への変換が必要
  - `update_document` は editMode=`patch` + `findText` で部分更新可能（フォーマット保持）。盲目的な read-modify-write より安全
  - Cloudflare WAF が python-urllib の default UA を 403 で蹴る → User-Agent ヘッダ必須
  - レイテンシ目安: create_document ~0.3s, patch ~0.17s, full-replace ~1.2s。100ページの初回 import で2〜3分
- 既存 collection（Polymoney / 広聴AI / いどばた / Welcome）には触っていない

## 2026-05-09

### 外部アーカイブ（Slack/GitHub 生ログ）の参照基盤を整備
- 過去1年分の Slack 生ログと GitHub Issues/PR データが `nishio/oss_weekly_reporter` の `data` ブランチに保管されているとのこと
- 追記（2026-06-30）: Slack チャットログ本体の正置き場は `digitaldemocracy2030/slack-logs` に移行。`nishio/oss_weekly_reporter` は週次AIレポートと GitHub Issues/PR の補助アーカイブとして扱う
- 物量（67週分・117MB・チャンネル毎の Slack JSON 含む）と privacy リスクを考え、`raw/` には取り込まず外部アーカイブとして検索ベースで参照する方針にした
- 追加・変更したファイル:
  - `archive_index.md`（新規） — アーカイブの場所・構造・読む順序のガイド
  - `scripts/search-archive.py`（新規） — 週ディレクトリを横断して `ai_reports`/`markdown`/`raw` の各層を keyword 検索する CLI。`--list-weeks`, `--since/--until`, `--layer`, `--regex`, `--limit` をサポート
  - `CLAUDE.md` — ディレクトリ構成図に `archive_index.md` を追加し、ソース表に外部アーカイブ行を追加。読む順序を CLAUDE.md にも明記
- スモークテスト: `python3 scripts/search-archive.py "Polimoney" --layer ai_reports --since 2025-12-01 --until 2026-01-31` と `... "ピンマイク" --layer raw ...` で複数件ヒット確認

### 次の作業
- アーカイブ（特に各週の `ai_reports/slack.md`）を読んで dd2030 初年度のまとめを作成する

## 2026-04-18

### Wiki構造の初期化
- ディレクトリ構成を作成: `raw/`, `wiki/`, `content/`, `scripts/`, `.github/workflows/`
- `raw/` のサブディレクトリ: `slack/`, `minutes/`, `documents/`, `assets/`
- `wiki/` のサブディレクトリ: `entities/`, `concepts/`, `events/`, `topics/`, `timeline/`, `sources/`
- CLAUDE.md（スキーマ）を作成
- wiki/index.md, wiki/overview.md, wiki/log.md を作成
- content/_index.md を作成（Quartz公開用トップページ）

### ソースの取り込みとWikiページ生成
- digitaldemocracy2030/website リポジトリから `src/history/` を取得
- 50週分（week1_20250319〜week50_20260415）、218個のMarkdownファイルを `raw/history/` に配置
- 全週のslack.mdとプロダクト別mdをスキャンし、以下のWikiページを生成:
  - wiki/overview.md — プロジェクト全体の概要
  - wiki/entities/kouchou-ai.md — 広聴AI
  - wiki/entities/idobata.md — いどばた
  - wiki/entities/polimoney.md — Polimoney
  - wiki/entities/coreloop.md — コアループ（Project Coreloop）
  - wiki/entities/broad-listening-book.md — ブロードリスニング本
  - wiki/concepts/broad-listening.md — ブロードリスニング
  - wiki/concepts/deliberative-democracy.md — 熟議民主主義
  - wiki/timeline/quarterly-summary.md — 時系列まとめ（四半期）
  - wiki/index.md — 目次を更新
