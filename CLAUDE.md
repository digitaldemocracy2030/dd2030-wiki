# dd2030 Wiki — Schema

dd2030プロジェクトの1年間の活動（Slackログ、議事録、資料等）を整理し、プロジェクトに初めて来た人が理解しやすいWikiを構築・維持するためのスキーマ。

## ディレクトリ構成

```
dd2030-wiki/
├── raw/                    # 元資料（不変、LLMは読むだけ）
│   ├── slack/              # Slackログ
│   ├── minutes/            # 議事録
│   ├── documents/          # その他資料
│   └── assets/             # 画像等
├── wiki/                   # LLMが生成・維持するWikiページ群
│   ├── index.md            # Wikiの目次・カタログ
│   ├── log.md              # 作業ログ（時系列）
│   ├── overview.md         # プロジェクト全体の概要
│   ├── entities/           # 人物・組織・チームのページ
│   ├── concepts/           # 概念・用語のページ
│   ├── events/             # イベント・会議・マイルストーン
│   ├── topics/             # テーマ・論点ごとの整理
│   ├── timeline/           # 時系列の活動まとめ
│   └── sources/            # 各ソースの要約ページ
├── content/                # Quartz公開用（wiki/からコピーまたはシンボリックリンク）
├── scripts/                # ユーティリティスクリプト
├── CLAUDE.md               # このファイル（スキーマ）
├── LOG.md                  # 作業ログ
└── PLAN.md                 # 現在の計画
```

## rawディレクトリの規約

- `raw/` 配下のファイルは**絶対に変更しない**。ソースオブトゥルース。
- ファイル名は `YYYY-MM-DD_概要.md` の形式を推奨。
- Slackログは `raw/slack/チャンネル名/` 配下に置く。
- 議事録は `raw/minutes/YYYY-MM-DD_会議名.md` の形式。

## Wikiページの規約

### フロントマター

すべてのWikiページにYAMLフロントマターを付ける:

```yaml
---
title: ページタイトル
tags: [dd2030, カテゴリタグ]
sources: [参照したrawファイルのパス]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

### 内部リンク

- `wiki/` ではシンプルな `[[ページ名]]` 記法を使う（例: `[[広聴AI]]`, `[[overview]]`）。
- パスの指定は不要。`scripts/resolve-links.py` がビルド時に自動でパスに解決する。
- リンク先がまだ存在しない場合でもリンクを張ってよい（プレーンテキストに変換される）。
- **content/ は直接編集しない。** wiki/ を編集し、スクリプトで content/ を生成する。

### カテゴリ別の書き方

**entities/**（人物・組織）:
- 役割、関わった活動、発言の要点をまとめる
- 個人の評価や主観的判断は書かない

**concepts/**（概念・用語）:
- プロジェクト固有の用語、略語、概念を説明
- 初めての人が読んで理解できる平易な言葉で

**events/**（イベント）:
- 日付、参加者、議題、決定事項、アクションアイテム
- 議事録の要約として機能する

**topics/**（テーマ）:
- プロジェクトの論点・テーマごとの横断的整理
- 複数のソースからの情報を統合

**timeline/**（時系列）:
- 月次または四半期ごとの活動サマリ
- 何が起きて何が決まったかの時系列整理

**sources/**（ソース要約）:
- 各rawファイルの要約。1ソース1ページ
- 元ファイルへの参照パスを必ず含める

## 操作フロー

### Ingest（取り込み）

1. `raw/` に新しいソースを配置
2. LLMがソースを読み、`wiki/sources/` に要約ページを作成
3. 関連する既存ページ（entities, concepts, events, topics）を更新
4. `wiki/index.md` にエントリを追加
5. `wiki/log.md` に作業記録を追記
6. 必要に応じて新しいページを作成

### ソースの更新

#### 議事録（Google Docs）の再取り込み

議事録は継続的に更新されるため、定期的に再取得してWikiに反映する。

```bash
# 1. Google Docsからテキストをダウンロード（上書き）
curl -sL "https://docs.google.com/document/d/1tBhaer67U9LbASfqPrg0rpmv0Tt4K7zFUTTzscKXj_I/export?format=txt" \
  -o raw/minutes/weekly-general-meeting.txt

curl -sL "https://docs.google.com/document/d/1dn9R9WLaGNMDO-t1w7m8-2gZRSrgZI4glDvSIr101J4/export?format=txt" \
  -o raw/minutes/community-operations.txt

curl -sL "https://docs.google.com/document/d/1plggszRTxEEYUcZuCLiHkPrBsMtxr3RQpctKtZe5y4M/export?format=txt" \
  -o raw/minutes/broad-listening-book-meeting.txt

curl -sL "https://docs.google.com/document/d/1isqRSUvvympiNp8uKBWYHIAI8-CGNjePriZUfrN4qig/export?format=txt" \
  -o raw/minutes/project-coreloop.txt

curl -sL "https://docs.google.com/document/d/19Kn6ekK3twMVcVaSyUgptvmfzrXEJezA6GXTbPXjm9M/export?format=txt" \
  -o raw/minutes/polimoney.txt

curl -sL "https://docs.google.com/document/d/1cK5i3ATo1OXsy-oicllY6-YlI-q0AJVtqQW7a71V-AU/export?format=txt" \
  -o raw/minutes/idobata-project.txt
```

```bash
# 2. LLMに差分を読ませてWikiを更新
# 例: 「raw/minutes/ の議事録が更新されたので、wiki/ の関連ページを更新して」
```

#### 週次レポート（GitHub）の再取り込み

websiteリポジトリに新しいweekが追加されたら取り込む。

```bash
# 最新のhistoryデータを取得
gh repo clone digitaldemocracy2030/website /tmp/dd2030-website -- --depth 1
cp -r /tmp/dd2030-website/src/history/ raw/history/
```

#### ブロードリスニング本（GitHub）の再取り込み

```bash
gh repo clone digitaldemocracy2030/broad-listening-book /tmp/bl-book -- --depth 1
mkdir -p raw/broad-listening-book
cp /tmp/bl-book/*.md raw/broad-listening-book/
cp -r /tmp/bl-book/column raw/broad-listening-book/
```

| ソース | 場所 | Google Doc ID | 更新頻度 |
|--------|------|--------------|----------|
| 全体定例 | raw/minutes/weekly-general-meeting.txt | `1tBhaer67U9LbASfqPrg0rpmv0Tt4K7zFUTTzscKXj_I` | 毎週 |
| コミュニティ運営 | raw/minutes/community-operations.txt | `1dn9R9WLaGNMDO-t1w7m8-2gZRSrgZI4glDvSIr101J4` | 毎週 |
| BL本執筆定例 | raw/minutes/broad-listening-book-meeting.txt | `1plggszRTxEEYUcZuCLiHkPrBsMtxr3RQpctKtZe5y4M` | 毎週 |
| Project Coreloop | raw/minutes/project-coreloop.txt | `1isqRSUvvympiNp8uKBWYHIAI8-CGNjePriZUfrN4qig` | 毎週 |
| Polimoney | raw/minutes/polimoney.txt | `19Kn6ekK3twMVcVaSyUgptvmfzrXEJezA6GXTbPXjm9M` | 毎週 |
| いどばた | raw/minutes/idobata-project.txt | `1cK5i3ATo1OXsy-oicllY6-YlI-q0AJVtqQW7a71V-AU` | 毎週 |
| 週次レポート | raw/history/week*/ | GitHub digitaldemocracy2030/website | 毎週 |

### Query（質問）

1. `wiki/index.md` を読んで関連ページを特定
2. 関連ページを読んで回答を合成
3. 有用な回答は `wiki/topics/` に新ページとして保存可能

### Lint（整合性チェック）

- 孤立ページ（インバウンドリンクなし）の検出
- 赤リンク（リンク先不在）の検出
- 古い情報の更新
- 矛盾する記述の発見と解消
- indexへの未登録ページの検出

## ビルドパイプライン

`wiki/` → (resolve-links.py) → `content/` → (Quartz) → `public/` → GitHub Pages

1. `wiki/` のMarkdownを編集する（シンプルな `[[ページ名]]` でリンク）
2. `python3 scripts/resolve-links.py` が `wiki/` を読み、リンクをファイルパスに解決して `content/` に出力
3. `npx quartz build` が `content/` からHTMLを生成
4. GitHub Actions が自動でこの全ステップを実行してデプロイ

ローカルでの確認: `python3 scripts/resolve-links.py && npx quartz build --serve`

## 補助ドキュメント (docs/)

繰り返し参照する可能性のある運用知識は `docs/` に置く:

- [docs/quartz-github-pages-setup.md](docs/quartz-github-pages-setup.md) — Quartz + GitHub Pages の構成を他リポジトリに移植するためのガイド
- [docs/outline-mcp-evaluation.md](docs/outline-mcp-evaluation.md) — Outline (dd2030-docs.kbn.one) への MCP 経由 import 検証メモ。ハマりどころと移行方針

## dd2030プロジェクト固有の注意

- プロジェクトに初めて来た人が対象読者。専門用語は必ず説明する。
- 日本語で記述する。
- Slackの発言は要約・整理して使う。個人の雑談や私的な内容は含めない。
- 議論の経緯と結論を区別して書く。「何が決まったか」を明確に。
