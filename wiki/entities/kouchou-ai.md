---
title: 広聴AI
aliases: [広聴AI]
tags: [dd2030, product, kouchou-ai]
sources:
  - raw/history/week1_20250319/kouchou-ai.md
  - raw/history/week10_20250521/kouchou-ai.md
  - raw/history/week20_20250730/kouchou-ai.md
  - raw/history/week30_20251008/kouchou-ai.md
  - raw/history/week44_20260121/kouchou-ai.md
  - raw/history/week50_20260415/kouchou-ai.md
  - raw/broad-listening-book/06_01_チームみらい.md
  - raw/broad-listening-book/08_02_広島県の事例.md
  - raw/broad-listening-book/10_00_DD2030による広聴AIの開発活動.md
  - raw/broad-listening-book/12_ブロードリスニング要素技術解説.md
  - raw/broad-listening-book/13_広聴AIの技術スタック解説.md
created: 2026-04-18
updated: 2026-06-30
---

# 広聴AI（kouchou-ai）

## 概要

**広聴AI**は、大量の市民意見（パブリックコメント、アンケート、SNS等）をAIで分析・クラスタリングし、論点ごとに可視化する[[ブロードリスニング]]ツール。dd2030の中核プロダクトの1つ。

「広聴」とは市民の声を広く聴くことを意味し、従来の行政の「広報」（情報を発信する）に対する概念。

## 技術スタック

- フロントエンド: Next.js
- バックエンド: Python
- LLM: OpenAI / Azure OpenAI / OpenRouter / Gemini（マルチプロバイダ対応）
- 次元圧縮・クラスタリング: UMAP, K-means, Ward法（書籍原稿10章・13章時点）
- デプロイ: Docker, Azure（GitHub Actionsで自動デプロイ）

## 機能

- CSVアップロードによる大量意見の取り込み
- AIによる意見のクラスタリング・要約
- セグメントビュー（全体・濃い意見・階層）の切り替え表示
- 属性フィルタ機能
- トークン使用量の可視化
- Windows / Mac / Linux対応

## 開発の歩み

### 初期（2025年3月〜4月）
- GitHubリポジトリ公開。Docker環境でのローカル実行が可能に
- 数百件のサンプルデータでレポート生成を確認
- 3万件規模のパブコメ対応を想定した設計議論
- Azure対応、APIコスト最適化が課題として浮上

### 成長期（2025年5月〜7月）
- **v3.0.0リリース**（2025年5月）
- OpenRouter対応でマルチLLMプロバイダ化
- Windows直実行サポート
- Embedding時のAzure/OpenRouter対応
- 技術解説スライドが「神資料」と評判に
- 宇多津町（香川）での実証が公開

### 社会実装期（2025年8月〜12月）
- [[events/2025-08-hiroshima-kouchou-ai|広島県で市民向け活用事例]]が公開・拡散
- LGWAN環境対応の議論（自治体イントラへの導入）
- APIキーのサーバーサイド管理強化（セキュリティ向上）
- 4パターンの提供形態を整理（研究用Jupyter・CLIツール・WebUI・お試しホスティング）
- AIツール利用時のコントリビュートルールを文書化

### v5.0への移行（2026年1月〜）
- 大規模リファクタリング開始
- **プラグイン方式**への転換（入力・分析・可視化を独立拡張可能に）
- **PyPI（Pythonパッケージ）化**によるCLI提供を構想
- Next.js 16.xへのアップデート（セキュリティ修正含む）

## 自治体での導入事例

- 宇多津町（香川県）— 実証実験
- [[events/2025-08-hiroshima-kouchou-ai|広島県]] — 市民向け活用事例
- [[topics/local-government-broad-listening|地方自治体でのブロードリスニング活用]] — 広島県・太田市の事例を横断した整理
- 奈良市 — 導入議論
- その他複数の自治体が関心を表明

## もっと詳しく

- [[sources/weekly-general-meeting|週次全体定例 議事録]] — 全体定例側の進捗共有
- [[sources/broad-listening-book-manuscript|ブロードリスニング本 原稿]] — 広聴AIの開発史・要素技術解説を含む原稿コレクション
- [[sources/broad-listening-book-core-concepts|ブロードリスニング本 概念編]] — 広聴AIが担うブロードリスニングの定義・役割・限界を確認する個別章ソース
- [[sources/broad-listening-book-team-mirai|ブロードリスニング本 チームみらい章]] — しゃべれるマニフェスト提案の内部可視化・観察を確認する個別章ソース
- [[sources/broad-listening-book-enterprise|ブロードリスニング本 企業での活用章]] — コンタクトセンターVOC分析への広聴AI活用を含む企業事例章
- [[sources/broad-listening-book-kouchou-ai-development|ブロードリスニング本 DD2030による広聴AI開発活動章]] — TTTCからのフォーク、Webアプリ化、2025年5月以降の開発史、AIコーディング、普及活動の整理
- [[sources/broad-listening-book-business-ecosystem|ブロードリスニング本 ビジネス化章]] — 広聴AIが自治体・選挙・熟議支援の現場へ届くまでの導入伴走と事業化の整理
- [[sources/broad-listening-book-public-cases|ブロードリスニング本 公開事例一覧]] — 広聴AIを含む公開事例URLの付録ソース
- [[sources/broad-listening-book-element-technologies|ブロードリスニング本 要素技術解説章]] — LLM、エンベディング、UMAP、クラスタリングなどの基礎技術
- [[sources/broad-listening-book-kouchou-ai-technical-stack|ブロードリスニング本 広聴AI技術スタック解説章]] — 抽出、埋め込み、UMAP、K-means、Ward法、ラベリング、要約の処理パイプライン
- [[sources/broad-listening-book-meeting|ブロードリスニング本 執筆定例 議事録]] — 広聴AI開発定例と書籍化のソース要約
- [広聴AI GitHubリポジトリ](https://github.com/digitaldemocracy2030/kouchou-ai) — ソースコード・Issue・PR
- [ブロードリスニング本 10章「DD2030による広聴AIの開発活動」](https://github.com/digitaldemocracy2030/broad-listening-book/blob/main/10_00_DD2030%E3%81%AB%E3%82%88%E3%82%8B%E5%BA%83%E8%81%B4AI%E3%81%AE%E9%96%8B%E7%99%BA%E6%B4%BB%E5%8B%95.md) — 開発の歴史と技術的背景
- [ブロードリスニング本 12章「要素技術解説」](https://github.com/digitaldemocracy2030/broad-listening-book/blob/main/12_%E3%83%96%E3%83%AD%E3%83%BC%E3%83%89%E3%83%AA%E3%82%B9%E3%83%8B%E3%83%B3%E3%82%B0%E8%A6%81%E7%B4%A0%E6%8A%80%E8%A1%93%E8%A7%A3%E8%AA%AC.md) — UMAP・クラスタリング等の技術解説
- [広聴AI技術解説スライド](https://www.docswell.com/s/tokoroten/ZL1M88-2025-06-14-014546) — 2025年6月公開の解説資料

## 関連ページ

- [[ブロードリスニング]] — 広聴AIが実現する概念
- [[sources/broad-listening-book-core-concepts|ブロードリスニング本 概念編]] — 広聴AIが実装するブロードリスニング概念を確認する個別章ソース
- [[sources/broad-listening-book-kouchou-ai-development|ブロードリスニング本 DD2030による広聴AI開発活動章]] — 広聴AIの開発活動史を確認する個別章ソース
- [[sources/broad-listening-book-business-ecosystem|ブロードリスニング本 ビジネス化章]] — 広聴AIの現場導入・伴走支援を確認する個別章ソース
- [[sources/broad-listening-book-public-cases|ブロードリスニング本 公開事例一覧]] — 広聴AIの公開事例URLを確認する個別章ソース
- [[sources/broad-listening-book-element-technologies|ブロードリスニング本 要素技術解説章]] — 広聴AIを支える基礎技術を確認する個別章ソース
- [[sources/broad-listening-book-kouchou-ai-technical-stack|ブロードリスニング本 広聴AI技術スタック解説章]] — 広聴AIの処理パイプラインを確認する個別章ソース
- [[sources/history-week50-20260415|週次History week50（2026-04-15）]] — 2026年4月中旬の依存関係更新とメンテナンス状況を確認する個別週ソース
- [[熟議民主主義]] — 理論的背景
- [[ボイス効果]] — 聴いた声をどう返すかの設計論
- [[ブロードリスニング本]] — 書籍化プロジェクト
- [[いどばた]] — 姉妹プロダクト（対話型）
- [[Cartographer]] — 個人の考えを深掘りする関連試作
- [[コアループ]] — 熟議プロセスの社会実装
- [[多元現実]] — ブロードリスニング技術を現場実装する企業
- [[倍速会議]] — 会議前・会議中の合意点・相違点・不確実性を可視化するAI支援ツール
- [[events/2025-04-12-1day-meetup|1Day Meetup（2025-04-12）]] — 初期に広聴AIが体験・検証されたイベント
- [[events/2025-05-16-shabereru-manifesto|しゃべれるマニフェスト公開]] — 提案の可視化・観察に広聴AIが内部利用された事例
- [[events/2025-05-25-meetup-2|デジタル民主主義2030 MEETUP #2]] — 広聴AIを含む開発・運営テーマが持ち寄られたイベント
- [[events/2025-06-12-kouchou-ai-reading-vol-1|広聴AI読書会vol.1]] — 広聴AIの理論的背景を学ぶ非同期読書会
- [[events/2025-06-21-welcome-meet-2|ウェルカムミート#2]] — 技術解説が新規参加者の関心を集めたオンボーディングイベント
- [[events/2025-07-18-meetup-3|デジタル民主主義2030 MEETUP #3]] — 広聴AIの開発・活用状況が共有されたイベント
- [[events/2025-08-hiroshima-kouchou-ai|広島県 広聴AI活用事例]] — 自治体でのブロードリスニング実践例
- [[events/2025-11-29-code-for-japan-summit|Code for Japan Summit 2025 登壇]] — 広聴AIの利用シーンとインサイト分類が外部共有されたイベント
- [[時系列まとめ]] — 四半期ごとの活動記録
- [[初年度まとめ]] — 立ち上がりから1年の詳細な時系列
- [[主要メンバー]] — プロジェクトの主要な人物
- [[コミュニティと法人の関係]] — OSSコミュニティと法人の役割分担
- [[overview]] — プロジェクト全体の概要
