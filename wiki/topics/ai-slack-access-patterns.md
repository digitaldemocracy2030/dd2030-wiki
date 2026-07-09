---
title: AI から Slack ログを参照するパターン
aliases: [AI から Slack ログを参照するパターン, ai-slack-access-patterns, AI と Slack 参照]
tags: [dd2030, tooling, archive, ai]
sources:
  - raw/documents/2026-06-09_archive-pipeline-design-note.md
  - digitaldemocracy2030/slack-logs/mirror/sync.json
  - digitaldemocracy2030/slack-logs/raw/slack/
  - oss_weekly_reporter/data/
created: 2026-06-09
updated: 2026-07-09
---

# AI から Slack ログを参照するパターン

> [[アーカイブパイプライン設計]] と [[OSS Weekly Reporter]] の実装が一通り終わったあと、「AI が Slack を読みたいシチュエーション」について整理した考察。dd2030 内で AI（Claude / LLM パイプライン / wiki ingest 自動化）が Slack ログを必要とする場面を分類し、それぞれが要求する鮮度・完全性と、`digitaldemocracy2030/slack-logs` を含む既存基盤がどう応えるかを書く。

## 現在の結論（2026-06-30）

`digitaldemocracy2030/slack-logs` は、月次保全用の `raw/` と直近参照用の `mirror/` の二層構成になった。したがって、現在は **歴史的問い合わせも現状クエリも、まず `slack-logs` を見る**のが基本。ただし、2026年6月30日時点で確認した `raw/` は、2025-01〜2026-02の月次ファイルがチャンネルメタデータのみで本文0件だった。2026-03以降は本文が入っているため、古い期間の本文確認では `oss_weekly_reporter` の週次raw/markdownを補助根拠として併用する。

| 用途 | まず読む場所 | 補足 |
|---|---|---|
| 歴史的問い合わせ | `raw/slack/<channel_id>/<YYYY-MM>.jsonl.gz` | 月次 canonical。まず本文件数を確認し、2025-01〜2026-02のように本文0件なら `oss_weekly_reporter` を併用 |
| 現状クエリ | `mirror/slack/<channel_id>.jsonl.gz` | 直近14日程度を6時間ごとに上書き更新 |
| 週次の要約・GitHub横断 | `nishio/oss_weekly_reporter` data ブランチ | `ai_reports/` と GitHub Issues/PR の補助アーカイブ |

2026-06-30 時点の `mirror/sync.json` は、58チャンネル・506メッセージ・window 14日（`2026-06-16T04:12:50Z` 〜 `2026-06-30T04:12:50Z`）を示している。

## 2つのタイプ

「AI が Slack を読みたい」は実は単一の要件ではなく、要求される鮮度とスレッド完全性が大きく異なる **2タイプ** が混ざっている。

| タイプ | 何をしたい | 鮮度要件 | スレッド完全性要件 |
|---|---|---|---|
| **A. 歴史的問い合わせ** | 「coreloop はどう始まった？」「2025-09 の移管議論はどんなだった？」 | **緩い**（数ヶ月遅れOK） | 高い（議論の流れ全部欲しい） |
| **B. 現状クエリ** | 「今 dd2030 で何が起きてる？」「先週の Discord 移行議論はどうなった？」「この Issue は Slack で誰がボールを持ってる？」 | **厳しい**（1週間以内） | 中程度（スレッド末尾の数件は欠けてもいい） |

当初の `slack-logs` は月次 + 2ヶ月遅延だけだったため **タイプ A 専用**だった。2026-06-09 に `mirror/` が追加され、タイプ B も同じリポジトリから読めるようになった。

## なぜ 2ヶ月遅延か

`slack-logger-cli-action` の README より:

> スレッド返信はその発言元の時刻でしか取得できない。9/30 投稿に 10/2 にスレッド返信 → 10/1 に9月分を取ると 10/2 の返信はどこにも残らない。

これは Slack API 自体の制約。**「保全」一次なら2ヶ月遅延は妥当**だが、「現状参照」用途には容認できない。

## それぞれのタイプの具体的シチュエーション

### タイプ A — raw/ で読む

- 新規参加者の onboarding 質問（「広聴AIってどう始まった？」）
- 議事録/PR の cross-reference（「この PR の背景となった Slack 議論は？」）
- 1年振り返り記事の素材集め
- 同じ話題が複数 ch でどう変遷したか
- 過去の意思決定の根拠を辿る（「なぜ X を採用した？」）

→ wiki ingest と同じ流れ。`slack-logs` を `gh api repos/.../contents/raw/slack/<ch>/<YYYY-MM>.jsonl.gz` で取って `zcat | jq` する。ただし、月次ファイルがメタデータだけの期間では、`oss_weekly_reporter/data/<week>/raw/slack/` または `markdown/slack/` で本文を確認する。

### タイプ B — mirror/ で読む

- nishio が PR #211 滞留に気づいたみたいな「**動いてるはずのものが詰まってる検知**」
- Discord 移行決定後の「**今週の遷移状況はどう？**」
- 「**この Issue の Slack 言及はあるか**」（タイミング不明、新しい可能性）
- 緊急トリアージ（インシデント発生時の文脈集め）
- AI による週次/日次レポート生成（OSS Weekly Reporter の本来用途）
- 「**誰が今ボールを持ってる議題**」リアルタイムマップ
- **dd2030-wiki の自動更新**（議事録の更新検知だけでなく Slack 起点の話題も即取り込み）

→ 月次 + 2ヶ月遅延では遅すぎるため、`mirror/slack/<channel_id>.jsonl.gz` を読む。

## 解決策の3案（検討履歴）

### 案1. 既存の併用を明文化する（当面ゼロコスト）

- タイプ A → slack-logs。月次canonicalに本文がない古い期間は `oss_weekly_reporter` も併用
- タイプ B → [`nishio/oss_weekly_reporter`](https://github.com/nishio/oss_weekly_reporter) の data ブランチ（毎週水曜更新、最大遅延1週間、`ai_reports/slack.md` で要約済み）

**メリット**: 何もしなくて済む。[`archive_index.md`](https://github.com/nishio/dd2030-wiki/blob/main/archive_index.md) と [`scripts/search-archive.py`](https://github.com/nishio/dd2030-wiki/blob/main/scripts/search-archive.py) で既に動いている。  
**デメリット**: 脱-nishio-依存になっていない。Slack→Discord 移行で oss_weekly_reporter 側が止まるリスク。

→ 2026-06-09 時点では暫定案。2026-06-30 現在は案2が実装済みなので、現状クエリの第一候補ではない。

### 案2. slack-logs に「現状ミラー」ワークフローを追加する

```yaml
# .github/workflows/slack-mirror.yml （新規）
on:
  schedule:
    - cron: '0 */6 * * *'   # 6時間ごと
jobs:
  mirror:
    # 過去 14 日ぶんだけ取得して mirror/ 配下に上書き保存
    # 2ヶ月遅延の slack-backup.yml とは独立して走らせる
```

- **monthly canonical** (`raw/slack/`) と **rolling mirror** (`mirror/slack/`) の二層化
- mirror は毎回上書き。履歴を持たない（履歴は raw 側の責務）
- thread のラグは数日で吸収（14日 window）
- 上流の slack-logger-cli-action は month 単位の引数しか持たない → **Python + slack_sdk で別実装**（`oss_weekly_reporter` の `slack_to_json.py --last-days 14` と同じ仕組み）

**メリット**: slack-logs に保全と現状の両方が集約、脱-nishio が完結。  
**デメリット**: 実装あり（~100行）。slack_sdk への依存追加。

### 案3. AI が必要時に Slack API を直接叩くツールを持つ

- Claude や自動化エージェントが MCP/関数呼び出しで Slack API を即時クエリ
- 蓄積しないので「現状」は常に最新
- slack-logs は完全に「歴史的アーカイブ」専用に

**メリット**: 最も柔軟・最も新鮮。on-demand。  
**デメリット**: AI に Slack token を渡す（権限管理）。共有 wiki ビルドには使えない。tool 実行時のレート制限。

## 採用方針（2026-06-09）

3案を順番に積み重ねる:

1. **当面: 案1** — `archive_index.md` の参照優先順位を明文化する
2. **直後（2026-06-09 着手、実装済み）: 案2** — slack-logs に mirror ワークフローを追加。Python + slack_sdk で `mirror/slack/<channel_id>.jsonl.gz` を 6時間ごとに上書き、`mirror/sync.json` に最終同期時刻を残す
3. **将来: 案3** — wiki ingest を半自動化したくなったとき（ユーザーが Slack URL を貼ったら AI が API で fetch してスレッドを取り込む）に MCP/tool 形態を検討

## 案2 実装結果（2026-06-09）

- `digitaldemocracy2030/slack-logs` 3e62c7f (workflow) → da1f293 (cache: pip 削除)
- 動作確認 run [27214269117](https://github.com/digitaldemocracy2030/slack-logs/actions/runs/27214269117) success: 57 channels, 556 messages, window 2026-05-26〜2026-06-09
- AI が直近の Slack 状態を参照するには:

```bash
# 最新同期時刻と channel/message 数
gh api repos/digitaldemocracy2030/slack-logs/contents/mirror/sync.json \
  --jq '.content' | base64 -d | jq '. | del(.channels)'

# 特定チャンネルの直近14日メッセージ
gh api repos/digitaldemocracy2030/slack-logs/contents/mirror/slack/<channel_id>.jsonl.gz \
  --jq '.download_url' | xargs curl -sL | zcat
```

- 履歴は `raw/` 側に蓄積されるので `mirror/` は常に上書きでOK
- 月次 canonical (`raw/`) と rolling mirror (`mirror/`) の **二層構成** が完成

## 関連ページ

- [[topics/first-reader-guide|初めて読む人へ]] — Wiki全体とアーカイブ関連ページへの入り方
- [[Slackログアーカイブ]] — `slack-logs` の `raw/` / `mirror/` の読み方
- [[アーカイブパイプライン設計]] — slack-logs の保全層の設計判断
- [[sources/archive-pipeline-design-note|アーカイブパイプライン設計メモ]] — raw/mirror前提の設計ソース要約
- [[OSS Weekly Reporter]] — 週次レポート生成側のパイプライン
- [[dd2030-wiki の dd2030 org 移行]] — Wiki本体をdd2030 org側でAIメンテナンスしやすくしつつ、旧URLを残す作業メモ
- [archive_index.md](https://github.com/nishio/dd2030-wiki/blob/main/archive_index.md) — 既存アーカイブの参照ガイド
