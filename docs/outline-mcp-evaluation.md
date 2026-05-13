# Outline MCP 検証メモ（dd2030-docs.kbn.one）

kuboon さんが立てた Outline インスタンス（`https://dd2030-docs.kbn.one`、Outline v1.7.1）に対して、dd2030-wiki を移行できるかを 2026-05-11 に検証したときの記録。

**結論を先に**: MCP 経由での import・編集は技術的に可能。ただし「MCP の `fetch` が本文を返さない」「`[[wiki-link]]` がリンク化されない」の 2 つのハマりどころがあり、**現 `wiki/` を source of truth に保ったまま Outline へ片方向 sync する構成**が一番事故が少ない。

## Outline とは（前提）

- チーム向けの社内 Wiki / ナレッジベース。Notion と Confluence の中間ぐらいの位置づけ
- Markdown 編集・リアルタイム共同編集（CRDT）・全文検索・Slack 連携・MCP 対応
- `https://dd2030-docs.kbn.one/mcp` が MCP エンドポイント
- 既に Polymoney / 広聴AI / いどばた / Welcome の 4 collection が作成済（kuboon さん作）

## アクセス手順

1. https://dd2030-docs.kbn.one/ にサインアップ
2. Settings → API Tokens で個人トークンを発行（`ol_api_...` 形式）
3. ローカルの Claude Code に MCP 登録:
   ```bash
   claude mcp add outline https://dd2030-docs.kbn.one/mcp \
     -t http -s user \
     -H "Authorization: Bearer ol_api_..."
   ```
   user scope なので `~/.claude.json` に平文保存される点に注意

## MCP で使えるツール（抜粋）

| ツール | 用途 | 補足 |
|---|---|---|
| `list_collections` | コレクション一覧 | — |
| `create_collection` / `update_collection` / `delete_collection` | コレクション操作 | — |
| `list_documents` | 全文検索 | クエリなしで最近の document を返す。**本文は返さない**（snippet のみ） |
| `list_collection_documents` | 階層付き document tree | 本文なし、メタ情報のみ |
| `create_document` | 新規 document 作成 | `text` で markdown 本文を渡す。**先頭の H1 は禁止**（title は別フィールド） |
| `update_document` | 編集 | `editMode: "patch"` + `findText` で部分更新を推奨（replace はフォーマットが壊れる） |
| `fetch` | document/collection/user 取得 | **本文 `text` を返さない**（後述） |
| `delete_document` | 削除（trash 行き） | `archive: true` でアーカイブにできる |

## ハマりどころ 3 つ

### 1. MCP `fetch` は本文 `text` を返さない

`fetch` の戻り値には title・id・URL・作成者などのメタ情報しか含まれない。AI が「読んで書き換える」を MCP だけでやろうとすると、空文字列を取得 → 全置換 → **本文消失**という事故になる（実際に最初のテストで踏んだ）。

回避策:
- **本文取得は Outline REST API を直接叩く**:
  ```bash
  curl -X POST https://dd2030-docs.kbn.one/api/documents.info \
    -H "Authorization: Bearer ol_api_..." \
    -H "Content-Type: application/json" \
    -H "User-Agent: any-non-default" \
    -d '{"id":"<doc-id>"}'
  ```
  `data.text` に markdown 本文が入る
- もしくは `update_document` を `editMode: "patch"` + `findText` で使えば read 不要で安全に部分更新できる

### 2. `[[wiki-link]]` はリンク化されない

Outline の markdown パーサは `[[X]]` を未知の構文として **エスケープした素のテキスト**（`\[\[X\]\]`）として保存する。ユーザには `[[X]]` というプレーンテキストが見えるだけ。

回避策: import 前に `name → /doc/URL` のマップを作って、`[[X]]` を Markdown リンク `[X](/doc/...)` に置換する。手順:
1. まず全 document を `create_document` で空〜本文付きで作成（URL が確定）
2. `list_collection_documents` で `title → url` マップを構築
3. 各 document の本文の `[[X]]` を `[X](url)` に置換
4. `update_document` で full replace（または patch）

エイリアス（`aliases` フロントマター）がある場合はマップに追加する。未解決のリンクは `[[X]]` のまま残すかプレーンテキストに落とすか方針を決める。

### 3. Cloudflare WAF が python-urllib のデフォルト UA を 403 で蹴る

`curl` だと通るが、`urllib.request` だと `User-Agent: Python-urllib/3.x` のままだと 403。**`User-Agent` ヘッダを明示**すれば通る（適当な文字列でよい）。

```python
req = urllib.request.Request(url, headers={"User-Agent": "dd2030-wiki-importer/0.1", ...})
```

## レイテンシ実測値

dd2030-wiki の concept ページ（~2KB）で計測:

| 操作 | 所要時間 |
|---|---|
| `create_document` | 約 0.3s |
| `update_document` (patch) | 約 0.17s |
| `update_document` (replace, 全置換) | 約 1.2s |
| REST 本文 read | 約 0.1s |
| `delete_document` | 約 0.1s |

→ 100 ページの初回 import で約 2〜3 分。

## 移行アーキテクチャの考察

### 推奨: `wiki/` を source of truth に保ち、片方向 sync

- AI 編集は git 上の `wiki/*.md` で行う（高速・revert 可能・差分が見える）
- cron や手動で Outline へ push
- Outline は「人間の閲覧 / Slack 連携 / 共同編集を一時的に受け付ける場所」と割り切る
- Quartz による GitHub Pages 公開は維持

### 双方向 sync は避ける

理由:
- Outline 側で人間がページ rename → URL 変更 → 既存の name→URL マップが壊れる → リンク切れ
- CRDT で同時編集された内容を git 側にマージするのが複雑
- 競合解決のルールを決める手間と事故リスクに見合わない

kuboon さんの提案「ログ生データは GitHub、整理済を Outline に置く」もこの方針と整合的（生データ・AI整理層は git、人間が読む確定版は Outline）。

## 検証用スクリプト

`scripts/` 配下に検証時に書いたもの:

- [scripts/outline_mcp.py](../scripts/outline_mcp.py) — MCP JSON-RPC 用の薄いラッパー。`OUTLINE_TOKEN` 環境変数で動く
- [scripts/import_test.py](../scripts/import_test.py) — 2 ページの import スモークテスト
- [scripts/link_convert_test.py](../scripts/link_convert_test.py) — `[[wiki-link]]` → `[name](/doc/...)` 変換の PoC

実行例:
```bash
export OUTLINE_TOKEN=ol_api_...
python3 scripts/outline_mcp.py list_collections
python3 scripts/import_test.py        # ※ 中の COLLECTION_ID を有効なものに差し替えること
```

## 未着手の課題

- 全 wiki ページの一括 import スクリプト（現状は 2 ページの PoC のみ）
- alias / 表記ゆれの吸収（`broad-listening.md` の frontmatter `aliases: [ブロードリスニング]` を name→URL マップに反映する）
- 画像（`raw/assets/`）の `create_attachment` 経由アップロード
- GitHub Actions での自動 sync
- Outline の Slack 連携の設定（`/outline search ...`、新規 document の通知）
