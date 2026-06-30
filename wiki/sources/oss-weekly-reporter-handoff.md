---
title: OSS Weekly Reporter 移管Slackメモ
aliases: [OSS Weekly Reporter 移管Slackメモ, oss-weekly-reporter-handoff]
tags: [dd2030, source, slack, archive]
sources: [raw/slack/2026-06-04_oss-weekly-reporter-handoff.md]
created: 2026-06-30
updated: 2026-06-30
---

# OSS Weekly Reporter 移管Slackメモ

## 概要

`raw/slack/2026-06-04_oss-weekly-reporter-handoff.md` は、OSS Weekly Reporter と `digitaldemocracy2030/slack-logs` の移管をめぐる nishio と kuboon のSlackやりとりを保存したソース。`slack-logs` が空のままだった理由、実装候補、dd2030-wikiへの吸収案が出た経緯を確認できる。

## 主な内容

- nishioが、Slackログを入れる仕組みを自分が作るべきか確認した
- kuboonは、リポジトリ招待がexpireしてしまったことを説明した
- kuboonは `kuboon/slack-logger-cli-action` を実装基盤候補として提示した
- nishioは、OSS Weekly Reporter がまだ個人リポジトリで動いていることを確認し、当時は dd2030-wiki への吸収案も考えていた

## Wikiでの使い方

[[OSS Weekly Reporter]] の移管状況と、[[アーカイブパイプライン設計]] の方針転換を説明する根拠として使う。個別発言は最小限に要約し、Wikiでは「なぜそういう設計判断になったか」を中心に扱う。

## 関連ページ

- [[sources/index|ソースカタログ]] — Wikiで参照している根拠ソースの入口
- [[OSS Weekly Reporter]] — 週次レポート生成パイプラインと移管状況
- [[アーカイブパイプライン設計]] — slack-logs data repo化の設計判断
- [[Slackログアーカイブ]] — 現在のSlackログ保全先
