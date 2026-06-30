---
title: アーカイブパイプライン設計メモ
aliases: [アーカイブパイプライン設計メモ, archive-pipeline-design-note]
tags: [dd2030, source, archive, tooling]
sources: [raw/documents/2026-06-09_archive-pipeline-design-note.md]
created: 2026-06-30
updated: 2026-06-30
---

# アーカイブパイプライン設計メモ

## 概要

`raw/documents/2026-06-09_archive-pipeline-design-note.md` は、Slack/Scrapbox/CosenseログをGitHub上に蓄積する設計についての検討メモ。コード用repoとデータ用repoを分ける理由、workflow配置、Slack API制約、保存形式、commit戦略、失敗モードを整理している。

## 主な内容

- 推奨構成: code repo と data repo を分離し、workflowは原則 data repo 側に置く
- rawデータと加工済みデータを分ける
- Slackは `conversations.history` と `conversations.replies` を使い、差分取得・冪等保存を前提にする
- Scrapbox/Cosenseは日次exportと更新ページ差分取得を組み合わせる
- GitHubは中規模テキストログには有用だが、巨大バックアップや添付ファイル込みの恒久保存には限界がある
- 保存形式は JSONL gzip/zstd、状態管理は watermark と重複排除を前提にする
- 一番危ない失敗モードは「保存できていないのにwatermarkだけ進む」こと

## Wikiでの使い方

[[アーカイブパイプライン設計]] の主要根拠。`digitaldemocracy2030/slack-logs` の raw/mirror 二層構成や、[[OSS Weekly Reporter]] からSlackログ保全を分離する判断を理解するときに読む。

## 関連ページ

- [[sources/index|ソースカタログ]] — Wikiで参照している根拠ソースの入口
- [[アーカイブパイプライン設計]] — dd2030文脈での設計整理
- [[Slackログアーカイブ]] — 実装済みのSlackログ保全・mirrorの読み方
- [[AI から Slack ログを参照するパターン]] — AIがログを読む用途別整理
- [[OSS Weekly Reporter]] — 週次AIレポート生成側の補助アーカイブ
