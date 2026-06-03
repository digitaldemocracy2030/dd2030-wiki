---
title: Wiki作業ログ
tags: [dd2030, log]
created: 2026-04-18
updated: 2026-06-03
---

# Wiki 作業ログ

取り込み・更新・メンテナンスの記録。

## [2026-04-18] init | Wiki構造の初期化

- ディレクトリ構成を作成（raw/, wiki/, content/, scripts/）
- CLAUDE.md（スキーマ）を作成
- index.md, overview.md, log.md を作成
- Quartz公開用の設定ファイルを準備

## [2026-04-18] ingest | website歴史データ50週分の取り込み

- digitaldemocracy2030/website の src/history/ から50週分のデータを取得
- raw/history/ に配置（218ファイル）
- 以下のWikiページを生成:
  - overview.md — プロジェクト全体の概要
  - entities/kouchou-ai.md — 広聴AI
  - entities/idobata.md — いどばた
  - entities/polimoney.md — Polimoney
  - entities/coreloop.md — コアループ
  - entities/broad-listening-book.md — ブロードリスニング本
  - concepts/broad-listening.md — ブロードリスニング
  - concepts/deliberative-democracy.md — 熟議民主主義
  - timeline/quarterly-summary.md — 時系列まとめ（四半期）
- index.md を更新

## [2026-04-18] deploy | GitHub Pages公開

- GitHubリポジトリ nishio/dd2030-wiki を作成
- Quartzフレームワークを導入（テンプレートからコピー）
- GitHub Actionsワークフロー（deploy.yml）を設定
- GitHub Pagesを有効化、自動デプロイ成功
- 公開URL: https://nishio.github.io/dd2030-wiki/

## [2026-04-18] fix | Wikilinkの解決方法を仕組み化

- 問題: `[[entities/kouchou-ai|広聴AI]]` のような日本語wikilinkがQuartzのファイル名解決で404になる
- aliasesフロントマターで対応→baseUrl欠落の問題が残る
- 解決策: scripts/resolve-links.py を作成
  - wiki/のシンプルな`ページ名`をtitle/aliasesからファイルパスに自動解決
  - content/に出力、ビルド時にリンク検証
  - GitHub Actionsにも組み込み
- wiki/では`ページ名`と書くだけでOKに

## [2026-04-18] ingest | Google Docs議事録4件の取り込み

- 取得した議事録:
  - weekly-general-meeting.txt（全体定例、3,500行）
  - community-operations.txt（コミュニティ運営、1,100行）
  - broad-listening-book-meeting.txt（BL本執筆定例、6,800行）
  - project-coreloop.txt（コアループ企画書・議事録、6,500行）
- Wikiの大幅更新:
  - coreloop.md — チーム構成5チーム、DP設計、台湾視察、自民党PTとの関係
  - broad-listening-book.md — 全章構成・執筆者・スケジュール
  - 新規: topics/community-operations.md（メンバー数推移、オンボーディング課題）
  - 新規: topics/key-people.md（30名以上のキーパーソンと役割）

## [2026-04-18] ingest | Polimoney・いどばた議事録の取り込み

- 取得した議事録:
  - polimoney.txt（5,000行）
  - idobata-project.txt（2,700行）
- Wikiの更新:
  - polimoney.md — 3ペルソナ戦略、Ledger/SaaS化、ロードマップ6ステップ、チームみらい棲み分け
  - idobata.md — サブプロダクト構成、参院選8,559件PR・254件採用、サイボウズ実験、2プロジェクト体制

## [2026-04-18] ingest | ブロードリスニング本リポジトリの取り込み

- digitaldemocracy2030/broad-listening-book から55ファイルを取得
- raw/broad-listening-book/ に配置
- Wikiの更新:
  - overview.md — 設立日（2025年1月）、共同創設者（安野＋鈴木健）、開発統計（2,756コミット、807PR、Devin 7.6%）
  - 各ページの精度向上（日付・数値の確認）

## [2026-04-18] docs | ソース更新手順の文書化

- CLAUDE.mdに全ソースのGoogle Doc ID・curlコマンド・更新頻度を記載
- READMEに「ソースの更新」セクションを追加
- README全体を整備（Fork手順、ローカル確認、GitHub Pages設定）

## [2026-04-18] enhance | 「もっと詳しく」セクションの追加

- 全Wikiページに一次ソースへのリンクを追加:
  - Google Docs議事録、GitHubリポジトリ、公開サイト、発表スライド、書籍原稿の該当章

## [2026-06-03] ingest | 法人名称決定アナウンス（2026-06-01）の取り込み

- 取り込み元: 鈴木健による6/1 Slackアナウンス「法人名称が決定しました」
- raw/documents/2026-06-01_legal-entity-name-announcement.md として保存
- 新規ページ: entities/legal-entity.md（デジタル民主主義推進機構 / Digital Democracy Builders）
  - ボード（鈴木・中室・関）の協議で決定
  - ドメイン: digitaldemocracy.jp
  - 候補比較（ジャパン／実装ハブ／2030）と見送り理由を整理
  - 「2030」はフラッグシップ・プログラム名として継続
- 更新:
  - overview.md — プロジェクトの歩みに 2026-06-01 を追加、組織・コミュニティ節に法人情報を追記
  - index.md — 「組織」セクションを新設し、法人ページへリンク

## [2026-06-03] explainer | コミュニティと法人の関係 解説ページ作成

- 元情報: raw/a.txt（OSS財団事例のリサーチと、コミュニティ／法人の並走関係についての対話）
- 方針: 設計提案ではなく、「コミュニティと法人が並走する」状況の解説に絞る（元の対話で明示された要望）
- 新規ページ: topics/community-and-legal-entity.md
  - 役割の違い（コミュニティ vs 法人）
  - OSS事例（Apache / Linux Foundation / Mozilla / Ethereum / OpenStreetMap / Decidim）の役割分担パターン
  - 「法人は代表者ではなく責任の受け皿」「コミュニティは法人の部門ではない」の整理
  - 政治的中立性の三層（党派中立／手続き中立／個人の自由）
- index.md — 「組織」「テーマ」セクションに新ページへのリンクを追加
