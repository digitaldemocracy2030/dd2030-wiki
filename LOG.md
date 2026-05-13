# LOG

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
