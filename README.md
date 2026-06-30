# dd2030 Wiki

[デジタル民主主義2030（dd2030）](https://dd2030.org)プロジェクトの活動を整理したWikiです。Slackログ、議事録、週次レポート、資料から情報を抽出し、プロジェクトに初めて来た人が理解しやすい形にまとめています。

**公開サイト**: https://nishio.github.io/dd2030-wiki/

## 仕組み

[LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) パターンに基づいています。LLMがソース資料を読み、Wikiページを生成・維持します。人間はソースの追加と方向づけを行い、LLMが要約・相互参照・整理を担当します。

```
wiki/（シンプルな [[ページ名]] で記述）
  ↓ pnpm build（Quartz が wiki/ を直接読む）
public/（HTML）
  ↓ GitHub Actions
GitHub Pages
```

## Forkして自分で動かす

### 1. Forkとクローン

```bash
# GitHubでForkしてから
git clone https://github.com/<your-username>/dd2030-wiki.git
cd dd2030-wiki
```

### 2. 依存のインストール

```bash
# Node.js (22+) と Python (3.10+) が必要
corepack enable
pnpm install
```

### 3. ローカルで確認

```bash
pnpm serve  # http://localhost:8080 で確認
```

### 4. GitHub Pagesの設定

1. `quartz.config.ts` の `baseUrl` を `<your-username>.github.io/dd2030-wiki` に変更
2. GitHubリポジトリの Settings → Pages → Build and deployment の Source を **GitHub Actions** に設定
3. pushすると自動でビルド・デプロイされる

### 5. Wikiの編集

`wiki/` 配下のMarkdownを編集してpushするだけです。

```bash
# 例: 新しいページを追加
vim wiki/concepts/new-concept.md

# ローカル確認
pnpm build && pnpm check:pages-links
pnpm serve

# pushすれば自動デプロイ
git add wiki/
git commit -m "Add new concept page"
git push
```

リンクは `[[ページタイトル]]` とシンプルに書けます。Quartz が `wiki/` を直接読み、`title` / `aliases` を使って解決します。

## ディレクトリ構成

```
dd2030-wiki/
├── wiki/                    # LLMが生成・維持するWikiページ（ここを編集する）
│   ├── index.md             # 目次
│   ├── overview.md          # プロジェクト概要
│   ├── entities/            # プロダクト・組織のページ
│   ├── concepts/            # 概念・用語の説明
│   ├── events/              # イベント・会議
│   ├── topics/              # テーマ別の横断整理
│   ├── timeline/            # 時系列の活動まとめ
│   └── sources/             # ソース資料の要約
├── raw/                     # 元資料（不変）
│   ├── history/             # websiteリポジトリの週次レポート（50週分）
│   └── minutes/             # Google Docsからエクスポートした議事録
├── scripts/
│   ├── check_pages_links.py # GitHub Pages上のリンク検査
│   ├── lint-wiki.py         # Wiki整合性チェック
│   └── search-archive.py    # 外部アーカイブ検索ヘルパー
├── quartz/                  # Quartzフレームワーク
├── quartz.config.ts         # Quartz設定
├── archive_index.md         # 外部アーカイブ参照ガイド
├── CLAUDE.md                # LLM向けスキーマ（ページ規約・操作フロー）
└── .github/workflows/       # GitHub Actions（自動デプロイ）
```

## ソースの更新

議事録や週次レポートは継続的に更新されるため、定期的に再取得してWikiに反映する。

### 議事録の再取得

```bash
# Google Docsから最新の議事録をダウンロード（上書き）
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

### 週次レポートの再取得

```bash
gh repo clone digitaldemocracy2030/website /tmp/dd2030-website -- --depth 1
cp -r /tmp/dd2030-website/src/history/ raw/history/
```

### 外部アーカイブの参照

Slack のチャットログ本体は dd2030-wiki にはコピーせず、外部リポジトリ [`digitaldemocracy2030/slack-logs`](https://github.com/digitaldemocracy2030/slack-logs) を検索して参照する。

```bash
gh repo clone digitaldemocracy2030/slack-logs /tmp/slack-logs -- --depth 1

# 直近 mirror を検索
python3 scripts/search-archive.py "キーワード"

# チャンネル名で絞って検索（IDでも可）
python3 scripts/search-archive.py --channel コアループ "提言"

# 月次 canonical を検索
python3 scripts/search-archive.py --layer raw --month 2026-04 "キーワード"
```

週次AIレポートと GitHub Issues/PR の補助アーカイブは `nishio/oss_weekly_reporter` の `data` ブランチを使う。

```bash
gh repo clone nishio/oss_weekly_reporter /tmp/oss_weekly_reporter -- \
  --depth 1 --branch data --single-branch

python3 scripts/search-archive.py --source oss-weekly-reporter --layer ai_reports "キーワード"
```

詳細は [archive_index.md](archive_index.md) を参照。

### Wikiの更新

ソースを再取得したら、LLMに差分を読ませてWikiを更新する。

```bash
# LLMに指示する例:
# 「raw/minutes/ の議事録が更新されたので、wiki/ の関連ページを更新して」
```

ソースの一覧と Google Doc ID は [CLAUDE.md](CLAUDE.md) の「ソースの更新」セクションにまとめてある。

更新後は次を確認する:

```bash
python3 scripts/lint-wiki.py
pnpm build && pnpm check:pages-links
```

## LLMと一緒に使う

このWikiはLLM（Claude Code等）と一緒にメンテナンスすることを前提としています。LLM向けの規約は [CLAUDE.md](CLAUDE.md) に記載しています。他のLLMエージェント（Codex, OpenCode等）を使う場合は、CLAUDE.mdの内容をそのエージェントの設定ファイル（AGENTS.md等）にコピーしてください。

## ライセンス

Wikiコンテンツ（`wiki/`, `raw/`）: CC BY 4.0
Quartzフレームワーク: MIT（[jackyzha0/quartz](https://github.com/jackyzha0/quartz)）
