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
  - raw/minutes/2026-08-16_kouchou-idobata-joint-meeting-prep.txt
  - raw/minutes/weekly-general-meeting.txt
  - "digitaldemocracy2030/slack-logs mirror/slack/C08F7JZPD63.jsonl.gz (#2_開発_広聴ai, 2026-10)"
  - "GitHub digitaldemocracy2030/kouchou-ai releases v4.1.0 (2026-10-13), v4.2.0 (2026-10-26), security advisory GHSA-xr6j-6w48-xh62"
  - "GitHub digitaldemocracy2030/website PR #224, #225, #227（韓国日報の事例ページ）"
created: 2026-04-18
updated: 2026-10-30
---

# 広聴AI（kouchou-ai）

## 概要

**広聴AI**は、大量の市民意見（パブリックコメント、アンケート、SNS等）をAIで分析・クラスタリングし、論点ごとに可視化する[[ブロードリスニング]]ツール。dd2030の中核プロダクトの1つ。

「広聴」とは市民の声を広く聴くことを意味し、従来の行政の「広報」（情報を発信する）に対する概念。

## 技術スタック

- フロントエンド: Next.js
- バックエンド: Python
- LLM: OpenAI / Azure OpenAI / OpenRouter / Gemini / ローカルLLM（Ollama 等。マルチプロバイダ対応）
- 次元圧縮・クラスタリング: UMAP, K-means, Ward法（書籍原稿10章・13章時点）
- 分析コア: `packages/analysis-core`。PyPI に `kouchou-ai-analysis-core` として公開され、Web UI なしで CLI（`kouchou-analyze`）から使える（2026年）
- デプロイ: Docker, Azure（GitHub Actionsで自動デプロイ。2026年10月に認証を OIDC へ移行）
- ドキュメント: MkDocs によるドキュメントサイト https://digitaldemocracy2030.github.io/kouchou-ai/ （2026年）
- ライセンス: AGPL-3.0（基盤にした Talk to the City と同じ。analysis-core が誤って MIT 表記になっていたのを 2026年10月に訂正）

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

### 大規模リファクタリング（2026年1月〜7月）
- 年末年始から大規模リファクタリングを開始。安定運用したいコアと実験的な拡張を分離する設計変更
- **プラグイン方式**への転換（入力・分析・可視化を独立拡張可能に）。5月末時点で「可視化部分と分析部分をプラグイン化して別々に改善できる形へ」と全体定例で共有
- **PyPI（Pythonパッケージ）化**で CLI 提供（1/19 に analysis-core を切り出し）。pandas から polars へ移行
- Next.js 16.xへのアップデート（セキュリティ修正含む）
- 5/18、Claude Code に「このデータを広聴AIで分析して」と言うだけで散布図 HTML が出る CLI ワークフローを整備。5/20 に WebUI も analysis-core を使う形になり、5/24 に大リファクタリング完了（[[sources/broad-listening-book-meeting|執筆定例 議事録]]）。LLM グルーピング実験は「ラベル品質は改善、散布図の見え方は従来法が優位」で CLI 版にマージ
- 6月、Azure デモ環境で散布図が出なくなる障害（デプロイ CI が旧 revision で成功判定、メモリ 1GiB で Next.js ビルドが OOM）を修正。開発者向け Wiki を作成。「ローカルLLMで動かせればセットアップが楽になる可能性」が共有された
- 7月、横浜市のブロードリスニング事例が全体定例で共有された
- この期間の成果は 2026年10月13日の **v4.1.0** としてまとめてリリースされた（当初「v5.0」と呼んでいた計画は、書籍刊行に合わせるメジャーリリースとして後ろに置かれた）

### ブラウザ版（サーバーレス）の登場（2026年8月）
- tokoroten（中山心太）が広聴AIをペライチのHTMLにした [kouchou-ai-serverless](https://tokoroten.github.io/kouchou-ai-serverless/) を公開。設定画面から OpenAI API Key を差し込むだけで動き、Chrome 内蔵の Gemini Nano を使えば無料で動作する
- tokoroten は「これを広聴AIの本流とするのが良いのでは」と提案し、西尾も「ライトなユーザにはインストールのトラブルがなくなる」と同意（[[sources/kouchou-idobata-joint-meeting-prep|合同ミーティング事前まとめ]]）
- 位置づけの議論は [[topics/nl-data-collection-tools-collaboration|自然言語データ収集ツールの関係と「一本化しない」協働]] を参照

### v4.1.0・v4.2.0 と棚卸し（2026年10月）

10月は西尾泰和が AI コーディングエージェントを使って集中的に作業し、リリース2本と Issue/PR の棚卸しを行った。10月のコミットは185件。

- **v4.1.0（10/13）**: 上記リファクタリングの成果をまとめたリリース。同日、Azure デプロイの認証情報（client secret）の期限切れでデプロイが止まり、OIDC 認証へ移行した
- **ドキュメント改善スプリント（10/13）**: ドキュメントサイトに「始め方の選び方」ページ、レポートの責任の所在（免責の3レイヤー）、リンク切れ検知 CI、リダイレクト設定を追加。README の見出しへの外部直リンクに依存しない方針にした
- **ライセンス訂正（10/12）**: analysis-core が最初から誤って MIT 表記だったことが分かり、AGPL に訂正。PyPI も差し替えた
- **Issue 棚卸し（10/12、10/29）**: 古い Issue を AI で全件照合。10/29 は open 89件を複数エージェントで約3時間かけて確認し、38件を close または実装済みと判定。2025年から残っていた「元コメント本文を公開レポートに含める」（#56）も実装された
- **v4.2.0（10/26）**: **セキュリティ修正を含む**。レポート作成画面の任意「APIキー」欄に入力したキーが結果ファイルと公開ページに平文で書き出されていた（勧告 [GHSA-xr6j-6w48-xh62](https://github.com/digitaldemocracy2030/kouchou-ai/security/advisories/GHSA-xr6j-6w48-xh62)、severity: medium）。サーバー側の `.env` に設定したキーは対象外。確認・除去スクリプトと[手順ページ](https://digitaldemocracy2030.github.io/kouchou-ai/self-hosting/security/user-api-key-leak-2026-10.html)を同梱。ほかに公開ビューアの日本語・英語・韓国語切替と翻訳 CLI、1万件規模のメモリ不足解消、10MB超 CSV 対応、Azure Blob で非公開化・削除が再起動で戻る問題の修正。PyPI の analysis-core は 0.2.0（10/29 に 0.3.0）
- **外部からの貢献**: 小嶋（名古屋、新規参加）が Ollama のポート衝突修正と韓国語 README を提出。大木真吾が Windows 11 + WSL2 + Docker Engine での自治体向けセットアップ手順をまとめた（自治体では Docker Desktop が有料のため）。yasumorishima がドキュメント修正
- **韓国日報との協働分析**: 韓国の新聞社・韓国日報の取材（10/8）に合わせ、韓国の政治 YouTube 6チャンネルのチャットを広聴AIで分析。記事は10/18・10/20 に掲載され、10/30 に分析結果の全体を dd2030.org の事例ページとして公開した。これを機に、広聴AI・いどばた・Polimoney の dd2030.org 上のページを英訳する方針（最終翻訳日時と日本語版へのリンクを付ける）が示された
- **コーディングエージェントで分析する事例（10/30）**: 「今はコーディングエージェントに分析を任せればよいのではないか」という議論を、ドキュメントサイトの[事例ページ](https://digitaldemocracy2030.github.io/kouchou-ai/user-guide/coding-agent-case-study.html)にまとめた
- **データセットの整備（10/30）**: いどばたで集めた約2万件の市民意見のデータセット（チームみらい 2025）に英訳を併記し、生成に使ったシステムとモデルの情報も含めて Hugging Face に公開した。それまで Google Docs や GitHub に散っていた情報を一か所にまとめたもの
- **次に向けて**: v4.2.0 はマイナーリリースと位置づけ、[[ブロードリスニング本]]の刊行に合わせてメジャーリリース（5.0）を打つ方針。意見ごとの賛否・新規性スコア、階層リストの詳細モード、API 利用料の目安表示などの PR がレビュー待ち。Amazon Bedrock による国内完結の分析（大木）、Anthropic API 対応（tokoroten）が Issue として提起された
- **Slack での論点**: ローカル LLM は「動く」ことと「十分な精度が出る」ことは別で、モデルごとの誤読率が分かるとよい（西尾）。余った AI サブスクリプションのトークンを OSS に回す案は [[topics/token-donation|トークンドネーション]] を参照

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
- [広聴AI ドキュメントサイト](https://digitaldemocracy2030.github.io/kouchou-ai/) — 始め方の選び方、セルフホスティング、CLI、プラグインのガイド
- [リリース一覧](https://github.com/digitaldemocracy2030/kouchou-ai/releases) — v4.1.0（2026-10-13）、v4.2.0（2026-10-26）の変更点
- [韓国日報との協働分析の事例ページ](https://dd2030.org/kouchou-ai/hankookilbo-2026/) — 2026年10月30日公開。韓国の政治 YouTube チャットの分析結果（日・英・韓）
- [事例: コーディングエージェントで分析する](https://digitaldemocracy2030.github.io/kouchou-ai/user-guide/coding-agent-case-study.html) — 広聴AI のパイプラインを使わず、コーディングエージェントに直接分析させた事例（2026年10月30日）
- [team-mirai-2025-embeddings（Hugging Face）](https://huggingface.co/datasets/nishiohirokazu/team-mirai-2025-embeddings) — いどばたで集めた約2万件の意見データセット。英訳併記、生成に使ったモデルの情報付き
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
