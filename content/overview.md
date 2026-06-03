---
title: dd2030 プロジェクト概要
aliases: [overview]
tags: [dd2030, overview]
sources: [raw/history/week1_20250319/slack.md, raw/history/week50_20260415/slack.md, raw/broad-listening-book/10_00_DD2030による広聴AIの開発活動.md]
created: 2026-04-18
updated: 2026-04-18
---

# デジタル民主主義2030（dd2030）プロジェクト概要

## プロジェクトとは

**デジタル民主主義2030（dd2030）** は、デジタル技術とAIを活用して民主主義のプロセスをアップデートすることを目指すオープンソースコミュニティプロジェクト。

- **設立**: 2025年1月
- **共同創設者**: 安野たかひろ（AIエンジニア）＋ 鈴木健（スマートニュース取締役会長・東京大学特任研究員、『なめらかな社会とその敵』著者）
- **OSS公開**: 2025年3月16日（[[entities/kouchou-ai|広聴AI]]と[[entities/idobata|いどばた]]のGitHubリポジトリ公開）
- **コミュニティ**: Slack上で1,574名（2026年4月時点）。エンジニア、デザイナー、PdM、自治体職員、研究者、学生など多様なメンバーが参加

設立時に3つの開発プロジェクトを公表: [[entities/kouchou-ai|広聴AI]]、[[entities/idobata|いどばた]]、[[entities/polimoney|Polimoney]]。

## ビジョン

「デジタルで社会を変える」を共通の思いに、以下を実現する：

- **市民の声を可視化する**（[[entities/kouchou-ai|広聴AI]]による[[concepts/broad-listening|ブロードリスニング]]）
- **大規模な熟議を可能にする**（[[entities/idobata|いどばた]]による意見集約・対話）
- **政治の透明性を高める**（[[entities/polimoney|Polimoney]]による政治資金の可視化）
- **市民が政策形成に参加できる仕組みをつくる**（[[entities/coreloop|コアループ]]による[[concepts/deliberative-democracy|熟議民主主義]]プロセス設計）

## 3つの柱となるプロダクト

| プロダクト | 概要 | 状態 |
|---|---|---|
| [[entities/kouchou-ai|広聴AI]] | 大量の市民意見をAIで分析・可視化するツール | 安定期（v5.0へ移行中） |
| [[entities/idobata|いどばた]] | 市民が政策テーマについて対話できるプラットフォーム | 再設計・横展開期 |
| [[entities/polimoney|Polimoney]] | 政治資金収支報告書を可視化するツール | Ledger機能完成、UI/UX調整中 |

## プロジェクトの歩み

- **2025年1月**: DD2030設立（安野たかひろ＋鈴木健）
- **2025年3月16日**: [[entities/kouchou-ai|広聴AI]]・[[entities/idobata|いどばた]]のGitHubリポジトリをOSS公開。Slack参加者250人超
- **2025年4月**: 第1回ミートアップ。[[entities/polimoney|Polimoney]]公開
- **2025年5月7日**: 安野たかひろがDD2030ボードメンバーを退任
- **2025年5月8日**: チームみらい結党
- **2025年5月16日**: 「しゃべれるマニフェスト」公開。[[entities/idobata|いどばた]]政策で参院選で8,559件のPR、254件が政策に採用
- **2025年5月**: [[entities/kouchou-ai|広聴AI]] v3.0.0リリース。新ボードメンバー就任
- **2025年夏**: 自治体（宇多津町・広島県等）での導入。広島県は2,953件の意見を約15分で分析
- **2025年秋**: [[entities/broad-listening-book|ブロードリスニング本]]の執筆開始
- **2025年冬**: Code for Japan Summit登壇。Polimoneyテレビ紹介
- **2026年1月**: DD2030が2期目に移行。[[entities/coreloop|コアループ]]プロジェクト始動
- **2026年3月19日**: 「ストップ詐欺広告」記者会見（15社参加）。クラウドファンディング開始
- **2026年6月1日**: 法人名称「[[entities/legal-entity|デジタル民主主義推進機構]]（Digital Democracy Builders）」が決定（一般社団法人）
- **2026年6月14日**: DP（討論型世論調査）実施予定

詳細は [[timeline/quarterly-summary|時系列まとめ]] を参照。

## 開発の規模

プロジェクト全期間（2025年2月〜2026年2月）の実績:
- 総コミット数: 2,756件
- マージされたPR: 807本
- Devinによるコミット: 210件（約7.6%、24人中5位）
- 2025年9月にはGitHubのissueをAIにアサインするだけでコードが自動生成される体制に

## 組織・コミュニティ

- **法人**: [[entities/legal-entity|デジタル民主主義推進機構]]（英文: Digital Democracy Builders、一般社団法人、2026年6月1日に名称決定）。「デジタル民主主義2030（dd2030）」は法人化後もフラッグシップ・プログラム名として継続
- Slack上のオープンコミュニティ。誰でも参加可能
- ボードメンバー制（鈴木健・中室・関、Code for Japan等の団体が参加）
- 各プロダクトにPO（プロダクトオーナー）を配置
- 毎週の全体定例、定期的なオフラインミートアップ
- GitHub上でのオープンソース開発（`good first issue` で初心者歓迎）
- DevinやClaude Codeなど、AI開発ツールを積極活用

## もっと詳しく

- [週次全体定例 議事録（Google Docs）](https://docs.google.com/document/d/1tBhaer67U9LbASfqPrg0rpmv0Tt4K7zFUTTzscKXj_I) — 毎週の全体定例の生の議事録
- [プロジェクトの歴史（Webサイト）](https://dd2030.org/history/) — 週ごとの活動まとめ
- [ブロードリスニング本 原稿（GitHub）](https://github.com/digitaldemocracy2030/broad-listening-book) — DD2030の歴史や事例を詳しく解説した書籍原稿
- [dd2030.org](https://dd2030.org/) — 公式サイト

## 関連ページ

- [[index]] — Wiki目次
- [[timeline/quarterly-summary|時系列まとめ]] — 週次・四半期の活動記録
- [[topics/key-people|主要メンバー]] — プロジェクトの主要人物
- [[topics/community-operations|コミュニティ運営]] — コミュニティの運営体制
