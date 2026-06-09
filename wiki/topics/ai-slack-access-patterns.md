---
title: AI から Slack ログを参照するパターン
aliases: [AI から Slack ログを参照するパターン, ai-slack-access-patterns, AI と Slack 参照]
tags: [dd2030, tooling, archive, ai]
sources:
  - raw/documents/2026-06-09_archive-pipeline-design-note.md
created: 2026-06-09
updated: 2026-06-09
---

# AI から Slack ログを参照するパターン

> [[アーカイブパイプライン設計]] と [[OSS Weekly Reporter]] の実装が一通り終わったあと、「AI が Slack を読みたいシチュエーション」について整理した考察。dd2030 内で AI（Claude / LLM パイプライン / wiki ingest 自動化）が Slack ログを必要とする場面を分類し、それぞれが要求する鮮度・完全性と、`digitaldemocracy2030/slack-logs` を含む既存基盤がどう応えるかを書く。

## 2つのタイプ

「AI が Slack を読みたい」は実は単一の要件ではなく、要求される鮮度とスレッド完全性が大きく異なる **2タイプ** が混ざっている。

| タイプ | 何をしたい | 鮮度要件 | スレッド完全性要件 |
|---|---|---|---|
| **A. 歴史的問い合わせ** | 「coreloop はどう始まった？」「2025-09 の移管議論はどんなだった？」 | **緩い**（数ヶ月遅れOK） | 高い（議論の流れ全部欲しい） |
| **B. 現状クエリ** | 「今 dd2030 で何が起きてる？」「先週の Discord 移行議論はどうなった？」「この Issue は Slack で誰がボールを持ってる？」 | **厳しい**（1週間以内） | 中程度（スレッド末尾の数件は欠けてもいい） |

[`digitaldemocracy2030/slack-logs`](https://github.com/digitaldemocracy2030/slack-logs) の現状（月次 + 2ヶ月遅延）は **タイプ A 専用**。タイプ B は別の仕組みが要る。

## なぜ 2ヶ月遅延か

`slack-logger-cli-action` の README より:

> スレッド返信はその発言元の時刻でしか取得できない。9/30 投稿に 10/2 にスレッド返信 → 10/1 に9月分を取ると 10/2 の返信はどこにも残らない。

これは Slack API 自体の制約。**「保全」一次なら2ヶ月遅延は妥当**だが、「現状参照」用途には容認できない。

## それぞれのタイプの具体的シチュエーション

### タイプ A — slack-logs だけで足りる

- 新規参加者の onboarding 質問（「広聴AIってどう始まった？」）
- 議事録/PR の cross-reference（「この PR の背景となった Slack 議論は？」）
- 1年振り返り記事の素材集め
- 同じ話題が複数 ch でどう変遷したか
- 過去の意思決定の根拠を辿る（「なぜ X を採用した？」）

→ wiki ingest と同じ流れ。slack-logs を `gh api repos/.../contents/raw/slack/<ch>/<YYYY-MM>.jsonl.gz` で取って `zcat | jq` する。

### タイプ B — slack-logs だけでは足りない

- nishio が PR #211 滞留に気づいたみたいな「**動いてるはずのものが詰まってる検知**」
- Discord 移行決定後の「**今週の遷移状況はどう？**」
- 「**この Issue の Slack 言及はあるか**」（タイミング不明、新しい可能性）
- 緊急トリアージ（インシデント発生時の文脈集め）
- AI による週次/日次レポート生成（OSS Weekly Reporter の本来用途）
- 「**誰が今ボールを持ってる議題**」リアルタイムマップ
- **dd2030-wiki の自動更新**（議事録の更新検知だけでなく Slack 起点の話題も即取り込み）

→ 月次 + 2ヶ月遅延では遅すぎる。

## 解決策の3案

### 案1. 既存の併用を明文化する（当面ゼロコスト）

- タイプ A → slack-logs
- タイプ B → [`nishio/oss_weekly_reporter`](https://github.com/nishio/oss_weekly_reporter) の data ブランチ（毎週水曜更新、最大遅延1週間、`ai_reports/slack.md` で要約済み）

**メリット**: 何もしなくて済む。[`archive_index.md`](https://github.com/nishio/dd2030-wiki/blob/main/archive_index.md) と [`scripts/search-archive.py`](https://github.com/nishio/dd2030-wiki/blob/main/scripts/search-archive.py) で既に動いている。  
**デメリット**: 脱-nishio-依存になっていない。Slack→Discord 移行で oss_weekly_reporter 側が止まるリスク。

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
2. **直後（2026-06-09 着手）: 案2** — slack-logs に mirror ワークフローを追加。Python + slack_sdk で `mirror/slack/<channel_id>.jsonl.gz` を 6時間ごとに上書き、`mirror/sync.json` に最終同期時刻を残す。詳細は実装後に [[OSS Weekly Reporter]] 末尾に追記
3. **将来: 案3** — wiki ingest を半自動化したくなったとき（ユーザーが Slack URL を貼ったら AI が API で fetch してスレッドを取り込む）に MCP/tool 形態を検討

## 関連ページ

- [[アーカイブパイプライン設計]] — slack-logs の保全層の設計判断
- [[OSS Weekly Reporter]] — 週次レポート生成側のパイプライン
- [archive_index.md](https://github.com/nishio/dd2030-wiki/blob/main/archive_index.md) — 既存アーカイブの参照ガイド
