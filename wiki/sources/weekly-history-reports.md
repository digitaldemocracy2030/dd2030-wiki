---
title: 週次Historyレポート
aliases: [週次Historyレポート, raw/history, プロジェクトの歴史, Historyレポート]
tags: [dd2030, source, history, weekly-report]
sources:
  - raw/history/
  - raw/history/_data.ts
  - raw/history/index.vto
created: 2026-06-30
updated: 2026-06-30
---

# 週次Historyレポート

## 概要

`raw/history/` は、dd2030.org の「プロジェクトの歴史」に表示するための週次レポート群。ほぼすべてが [[OSS Weekly Reporter]] によって自動生成されたMarkdownで、SlackやGitHub活動から「その週に何があったか」をプロジェクト別に読める形へ整えている。

このページは、50週分のレポート全体を読むためのコレクション要約である。個別週・個別ファイルの1ソース1ページ化は、必要になった週から追加していく。

活動には波があるため、週次Historyを全週機械的に個別ページ化する必要はない。節目になる出来事、複数ページから繰り返し参照する根拠、あとから状態確認の境界として使う週だけを個別ページ化し、内容の薄い週はこのコレクション要約や時系列ページから辿れればよい。

## 収録範囲

- 対象期間: week1（2025-03-19）〜week50（2026-04-15）
- 週ディレクトリ数: 50
- Markdownファイル数: 218
- 公開側の生成: `raw/history/_data.ts` と `raw/history/index.vto` が週ディレクトリを走査し、History一覧を作る

## ファイル種別

| ファイル | 件数 | 内容 |
|---|---:|---|
| `slack.md` | 50 | Slack上の横断的な週次まとめ |
| `kouchou-ai.md` | 46 | 広聴AIの開発・導入・運用の週次まとめ |
| `website.md` | 46 | dd2030.org やHistoryページ更新の週次まとめ |
| `idobata.md` | 39 | いどばたの開発・利用事例の週次まとめ |
| `polimoney.md` | 36 | Polimoneyの開発・広報・利用者接点の週次まとめ |
| `digest.md` | 1 | 初期週の要約 |

## 読み方

1. まず [[時系列まとめ]] で四半期ごとの大きな流れを見る。
2. 月別・チャンネル別の詳しい流れは [[初年度まとめ]] を読む。
3. 具体的な週の出来事を確認するときに `raw/history/week*_YYYYMMDD/` を読む。
4. Historyレポートに載っていない詳細を掘るときは、Slackログ本体の `digitaldemocracy2030/slack-logs` や、補助アーカイブとしての `nishio/oss_weekly_reporter` dataブランチを検索する。

## 個別週ページ

- [[sources/history-week33-20251029|週次History week33（2025-10-29）]] — ウェルカムミート#3告知、Cartographer・farbrain、認証・公開方式の検討が並ぶ2025年10月下旬のSlack週次まとめ
- [[sources/history-week43-20260114|週次History week43（2026-01-14）]] — 熟議ワークショップ、Project Coreloopキックオフ、Polimoneyの外向け発信が並ぶ2026年1月中旬のSlack週次まとめ
- [[sources/history-week50-20260415|週次History week50（2026-04-15）]] — raw/historyに取り込まれている最後の週。ブロードリスニング本、Coreloop、Polimoney、広聴AIの2026年4月中旬時点を確認する個別週ページ

## 注意点

- `raw/history/` は公開サイト向けに加工済みの週次レポートであり、Slackログそのものではない。
- 個別週ページは網羅率を上げるためではなく、後から参照価値がある週に絞って作る。実施済みか未実施か曖昧なイベントや、活動量が少ない週は、独立ページ化よりも既存ページの注記や導線改善を優先する。
- 取得対象チャンネルや対象リポジトリは時期によって変わっているため、全公開チャンネルの完全な記録ではない。
- LLM生成の週次まとめを含むため、細部の確認には元ログや議事録との突き合わせが必要。
- 2026年4月15日の[[sources/history-week50-20260415|week50]]までがこのリポジトリに取り込まれている。以後のSlackチャットログ本体は `digitaldemocracy2030/slack-logs`、週次AIレポート補助アーカイブは `nishio/oss_weekly_reporter` を参照する。

## 関連ページ

- [[sources/index|ソースカタログ]] — Wikiで参照している根拠ソースの入口
- [[時系列まとめ]] — 四半期ごとの整理
- [[初年度まとめ]] — 月別の詳細整理
- [[events/2025-04-12-1day-meetup|1Day Meetup（2025-04-12）]] — Historyレポートに残る初期ミートアップ
- [[events/2025-05-16-shabereru-manifesto|しゃべれるマニフェスト公開]] — 週次Historyに残るチームみらいベータテストといどばた改善文脈
- [[events/2025-05-17-team-mirai-idobata-vision|チームみらい選挙ボランティア向けミートアップでのいどばたビジョン活用]] — 週次Historyに残るチームみらいベータテストといどばた改善文脈
- [[events/2025-05-25-meetup-2|デジタル民主主義2030 MEETUP #2]] — Historyレポートに残る2025年5月のミートアップ
- [[events/2025-06-12-kouchou-ai-reading-vol-1|広聴AI読書会vol.1]] — Historyレポートと外部アーカイブに残る2025年6月の読書会
- [[events/2025-06-21-welcome-meet-2|ウェルカムミート#2]] — Historyレポートに残る2025年6月のオンボーディングイベント
- [[events/2025-07-18-meetup-3|デジタル民主主義2030 MEETUP #3]] — Historyレポートに残る2025年7月のミートアップ
- [[events/2025-08-hiroshima-kouchou-ai|広島県 広聴AI活用事例]] — Historyレポートに残る2025年8月の自治体活用事例
- [[events/2025-11-28-welcome-meet-3|ウェルカムミート#3]] — Historyレポートに残る2025年10月のオンボーディング告知
- [[sources/history-week33-20251029|週次History week33（2025-10-29）]] — ウェルカムミート#3の根拠になった個別週ソース
- [[events/2025-11-29-code-for-japan-summit|Code for Japan Summit 2025 登壇]] — Historyレポートに残る2025年11月の外部発表
- [[events/2026-01-09-burikaigi-polimoney|ぶり会議2026 Polimoney登壇]] — Historyレポートに残る2026年1月の外部発表準備
- [[events/2026-01-10-deliberation-workshop|熟議民主主義プロセス ワークショップ（2026-01-10）]] — Historyレポートに残る熟議実験
- [[sources/history-week43-20260114|週次History week43（2026-01-14）]] — 熟議ワークショップとCoreloop本格化の根拠になった個別週ソース
- [[sources/history-week50-20260415|週次History week50（2026-04-15）]] — raw/historyの終端と2026年4月中旬時点の各プロジェクト状態を確認する個別週ソース
- [[sources/broad-listening-book-manuscript|ブロードリスニング本 原稿]] — 書籍原稿側から見たdd2030の概念・事例整理
- [[OSS Weekly Reporter]] — 週次レポート生成パイプライン
- [[Slackログアーカイブ]] — 現在のSlackチャットログ本体の読み方
