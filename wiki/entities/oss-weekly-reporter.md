---
title: OSS Weekly Reporter
aliases: [OSS Weekly Reporter, oss_weekly_reporter, 週次レポーター]
tags: [dd2030, project, tooling, archive]
sources:
  - oss_weekly_reporter/README.md
  - oss_weekly_reporter/data/2025-04-02_to_2025-04-09/raw/slack/2_新しいプロジェクトの種.json
created: 2026-05-11
updated: 2026-05-11
---

# OSS Weekly Reporter

## 概要

**OSS Weekly Reporter** は、OSSプロジェクトの週次活動報告を省力化するための西尾製ツール。Slack ログと GitHub の Issue/PR を抽出し、LLM に渡す Markdown 形式に変換して、「今週何が起きたか」のレポートを半自動で生成する。

リポジトリ: [`nishio/oss_weekly_reporter`](https://github.com/nishio/oss_weekly_reporter)

dd2030 においては、これが**[[初年度まとめ|過去1年間のSlackログとGitHub活動データの一次アーカイブ]]**になっており、[[overview|dd2030 wiki]] 自体の基盤データ源として機能している。詳細な参照手順は [archive_index.md](/archive_index.md) を参照。

## 由来 — `2_新しいプロジェクトの種` から生まれた

2025年4月初旬、`2_新しいプロジェクトの種` チャンネルで生まれたプロジェクト。前身は kuboon 氏の [`gsheet-slack-logger`](https://github.com/kuboon/gsheet-slack-logger)（Slack ログを Google Spreadsheet に保存する Bot）。

西尾の整理（出典: `oss_weekly_reporter/data/2025-04-02_to_2025-04-09/raw/slack/2_新しいプロジェクトの種.json`）:

> オリジナルの実装は「Slackからの抽出」と「Google Spreadsheetへのアップロード」がセットになっていた。これはログを保存するという目的には合理的。… 毎週の更新レポートをLLMで作りたいという目的に使おうと思った時、Google Spreadsheetを経由するのは無駄に複雑では？となった。それはそう、目的が変わったから適切な構成も変わる。

すなわち、**「ログ保全」と「週次レポート生成」を分離**し、後者を `oss_weekly_reporter` として切り出した。kuboon オリジナルは月次バッチでログ保存を継続、こちらは週次でレポート生成と JSON アーカイブを担当する、という分業構造になっている。

## 構成

```
Slack API → slack_to_json.py → raw/slack/<channel>.json
GitHub API → github_report.py → raw/github/<repo>.json
              ↓
         json_to_markdown.py → markdown/
              ↓
         call_openai_api.py（LLM） → ai_reports/
```

主要スクリプト:

| スクリプト | 役割 |
|------------|------|
| `slack_to_json.py` | チャンネルごとに JSON で抽出。日付範囲フォルダを作成 |
| `github_report.py` | リポジトリの Issue/PR を JSON 抽出（オプションで Markdown も） |
| `json_to_markdown.py` | LLM 入力用の Markdown に変換 |
| `call_openai_api.py` | OpenAI o1 を呼んで週次サマリを生成 |
| `json_to_gsheet.py` | （旧用途） Google Spreadsheet への保存 |

データは GitHub の `data` ブランチに `YYYY-MM-DD_to_YYYY-MM-DD/` 形式で push される。2026年5月時点で67週分・117MB。

## どのチャンネル・リポジトリを追跡しているか

`config.yaml` で設定する。**全公開チャンネルではなく、購読リスト方式**。

時期によって追跡対象が変わってきた経緯があり、初期のチャンネル（例: `2_学生のためのデジタル民主主義`）が後期には取得対象から外れていたり、後から追加されたチャンネル（例: `2_開発_cartographer` は2025-10から）があったりする。**67週通算で 80+ 個のチャンネル名が登場**するが、各週の取得対象は10〜20チャンネル程度。

追跡対象に入っていなかったチャンネルの議論は、このアーカイブには残らない。これは dd2030 wiki の構築上の重要な制約となる（→ [[初年度まとめ]] 末尾「含まれていない可能性があるもの」セクション）。

## dd2030 wiki におけるメタ循環構造

dd2030 wiki は次のような依存関係を持つ:

```
dd2030 Slack ──→ oss_weekly_reporter ──→ aiレポート/Markdown/生JSON
                                              ↓
                                         dd2030 wiki（このリポジトリ）
                                              ↑
                                        OSS Weekly Reporter の解説
                                        （このページ）
```

- アーカイブ自体は dd2030-wiki リポジトリには取り込まない（プライバシー・サイズ）
- 検索ベースで参照する（[scripts/search-archive.py](/scripts/search-archive.py)）
- このアーカイブを生んだプロジェクト自体が dd2030 の中で `2_新しいプロジェクトの種` から立ち上がったもの

## 関連ページ

- [archive_index.md](/archive_index.md) — アーカイブの参照ガイド
- [[初年度まとめ]] — このアーカイブから構築した時系列まとめ
- [[overview]] — プロジェクト全体の概要
