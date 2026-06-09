---
title: Index
tags: [dd2030, index]
created: 2026-04-18
updated: 2026-04-18
---

# dd2030 Wiki — 目次

dd2030プロジェクトの知識ベース。プロジェクトに初めて参加する人が全体像を把握できることを目指しています。

## まずはここから

- [[overview]] — プロジェクト全体の概要
- [[初年度まとめ]] — 2025年3月〜2026年3月の月ごと詳細サマリ（外部アーカイブ参照版）
- [[時系列まとめ]] — 1年間の活動を四半期ごとに整理（骨子版）

## プロダクト

- [[広聴AI]] — 大量の市民意見をAIで分析・可視化するツール
- [[いどばた]] — 市民が政策テーマについて対話できるプラットフォーム
- [[Polimoney]] — 政治資金収支報告書を可視化するツール
- [[Cartographer]] — 個人の考えを深掘りして「じぶんレポート」を生成する試作ツール

## プロジェクト

- [[コアループ]] — 詐欺広告対策の市民熟議プロジェクト（2026年〜）
- [[ブロードリスニング本]] — 書籍化プロジェクト（インプレスから出版予定）
- [[OSS Weekly Reporter]] — dd2030のSlack/GitHub週次アーカイブを生成するツール

## 概念・用語

- [[ブロードリスニング]] — 大量の市民の声をAIで可視化するアプローチ
- [[熟議民主主義]] — 対話を通じた合意形成の民主主義モデル
- [[ボイス効果]] — 「聞いてもらえた」感が満足度を生む設計原則（手続き的公正）

## 組織

- [[デジタル民主主義推進機構]] — 法人名（一般社団法人、Digital Democracy Builders、2026/6/1決定）
- [[コミュニティと法人の関係]] — DD2030と推進機構はどう並走するか（解説）

## テーマ

- [[主要メンバー]] — プロジェクトに関わる主要な人物
- [[コミュニティ運営]] — Slackコミュニティの運営・オンボーディング課題
- [[コミュニティと法人の関係]] — OSS事例から見たコミュニティと法人の役割分担
- [[アーカイブパイプライン設計]] — Slack/Scrapboxログを GitHub に溜めるときの設計選択（[[OSS Weekly Reporter]] の脱-nishio-依存の文脈）

## ソース要約

### 週次レポート（raw/history/）
50週分（week1〜week50）の週次レポート。各週に以下のファイルが含まれる：

| ファイル | 内容 |
|---|---|
| `slack.md` | Slackの週次まとめ（全週にあり） |
| `kouchou-ai.md` | 広聴AIの開発進捗 |
| `idobata.md` | いどばたの開発進捗 |
| `polimoney.md` | Polimoneyの開発進捗 |
| `website.md` | Webサイトの更新 |

### 議事録（raw/minutes/）

| ファイル | 内容 |
|---|---|
| `weekly-general-meeting.txt` | 週次全体定例の議事録 |
| `community-operations.txt` | コミュニティ運営議事録 |
| `broad-listening-book-meeting.txt` | ブロードリスニング本執筆定例 |
| `project-coreloop.txt` | Project Coreloop 企画書・議事録 |
| `polimoney.txt` | Polimoney プロジェクト議事録 |
| `idobata-project.txt` | いどばた プロジェクト全体 |

### ブロードリスニング本（raw/broad-listening-book/）

digitaldemocracy2030/broad-listening-book リポジトリから取得した書籍原稿（全13章＋コラム）。dd2030の歴史・事例の詳細な解説を含む。

### 外部アーカイブ（リポジトリ外）

Slack の生ログとGitHub Issues/PR の生データは、67週分・117MBあるため dd2030-wiki には取り込まず、別リポジトリ `nishio/oss_weekly_reporter`（`data` ブランチ）に保管している。検索ベースで参照する。

- 概要・参照手順: [archive_index.md](https://github.com/nishio/dd2030-wiki/blob/main/archive_index.md)
- 検索ヘルパー: `python3 scripts/search-archive.py <keyword> --layer ai_reports`
