---
title: ブロードリスニング
aliases: [ブロードリスニング]
tags: [dd2030, concept]
sources:
  - raw/history/week14_20250618/slack.md
  - raw/history/week29_20251001/slack.md
  - raw/history/week37_20251126/slack.md
  - raw/broad-listening-book/01_ブロードリスニングとは何か？.md
  - raw/broad-listening-book/02_ブロードリスニングとアンケートの違い、定量分析から定性分析へ.md
  - raw/broad-listening-book/03_デジタル民主主義とブロードリスニング、新しい民意の届け方.md
  - raw/broad-listening-book/04_日本国内におけるブロードリスニングの広がり.md
  - raw/broad-listening-book/04_01_安野貴博の取り組み.md
  - raw/broad-listening-book/04_02_国民民主の国会質問.md
  - raw/broad-listening-book/04_03_sumino_日テレ選挙特番.md
  - raw/broad-listening-book/04_04_Polisで世論の地図を作る.md
  - raw/broad-listening-book/04_05_朝日新聞の特設記事.md
  - raw/broad-listening-book/05_東京都、シン東京2050、ブロードリスニングによる政策転換.md
  - raw/broad-listening-book/06_国政選挙でのブロードリスニングの利用.md
  - raw/broad-listening-book/06_01_チームみらい.md
  - raw/broad-listening-book/06_02_チームみらい2026年衆院選.md
  - raw/broad-listening-book/06_03_日本維新の会.md
  - raw/broad-listening-book/06_04_国民民主党.md
  - raw/broad-listening-book/06_05_公明党.md
  - raw/broad-listening-book/07_地方選挙での活用.md
  - raw/broad-listening-book/07_02_いでい良輔氏のケース.md
  - raw/broad-listening-book/07_03_再生の道_尾花山和哉.md
  - raw/broad-listening-book/10_00_DD2030による広聴AIの開発活動.md
  - raw/broad-listening-book/10_ビジネスになったブロードリスニング.md
  - raw/broad-listening-book/10_01_株式会社ブーツ.md
  - raw/broad-listening-book/10_02_Code for Japan.md
  - raw/broad-listening-book/10_03_多元現実.md
  - raw/broad-listening-book/10_04_Democracy X.md
  - raw/broad-listening-book/10_05_litela_田中魁.md
  - raw/broad-listening-book/11_海外におけるブロードリスニングの流れ.md
  - raw/broad-listening-book/11_05_Connective_Actionを力に変える.md
  - raw/broad-listening-book/12_ブロードリスニング要素技術解説.md
  - raw/broad-listening-book/13_広聴AIの技術スタック解説.md
  - raw/broad-listening-book/99_付録_公開事例一覧.md
  - digitaldemocracy2030/slack-logs/mirror/slack/C09J7A6HKRA.jsonl.gz
created: 2026-04-18
updated: 2026-06-30
---

# ブロードリスニング

## 概要

**ブロードリスニング（Broad Listening）** とは、大量の市民の声をAI技術を用いて収集・分析・可視化し、政策形成に活用するアプローチ。従来の「ブロードキャスティング（広報＝一方向の情報発信）」に対する概念で、「広く聴く」ことを重視する。

dd2030では[[広聴AI]]がこの概念を技術的に実現するプロダクトとして位置づけられている。

ブロードリスニングの主要な成果物は[[論点地図]]である。これは自由記述を分類・要約し、「何が論点なのか」を人間が読み解ける構造として示すもので、民意の比率を測るものではない。

選挙時には争点になっていなかった新規課題に任期中対応するとき、政治家や行政には[[正統性の空白]]が生じる。ブロードリスニングは、この空白に対して、論点把握、政策立案、説明、再収集のループを補助するものとして説明されている。

2026年の[[コアループ]]では、[[AIディープサーベイ]]がオンライン詐欺広告対策について市民の声を集め、法規制検討や熟議設計へ接続する入口として使われた。これは、通報データだけでなく自由記述の意見・対策案を政策形成に使うブロードリスニング型の実践として読める。

## 核心的なアイデア

従来の意見聴取（パブリックコメント、アンケート等）には以下の問題がある：

- **量の壁**: 数千〜数万件の意見を人間が読みきれない
- **AI生成スパム**: 大量のAI生成コメントが制度を機能不全にする懸念
- **形骸化**: パブコメ制度が形式的になり、市民の「意見が届いた実感」がない

ブロードリスニングは、AIを使って：
1. 大量の意見をクラスタリング・要約する
2. 論点ごとに可視化する
3. 対立軸や合意点を明らかにする
4. 「意見が届いている実感」を市民にフィードバックする

## 書籍化

2025年秋から[[ブロードリスニング本]]の執筆が開始された。

- 仮タイトル:「選挙を変えたブロードリスニング──生成AIが実現する民意の可視化と分析」
- 出版社: インプレス
- 規模: 約37.9万文字（2026年6月21日のPDF Build時点）
- 内容: SNS運動の歴史、vTaiwan事例、Connective Action理論、国内外の実践事例
- 2026年4月時点で校正段階、2026年6月時点でもPDFビルドと校正コメント対応が継続

## 関連する理論・概念

- **Connective Action** — ネットワーク化された市民行動の理論
- **熟議民主主義** — 対話を通じて合意形成する民主主義のモデル
- **vTaiwan** — 台湾のデジタル民主主義プラットフォーム（オードリー・タンが推進）
- **Polis** — 意見のクラスタリング・可視化ツール（広聴AIの参考となったシステム）

## もっと詳しく

- [[sources/broad-listening-book-manuscript|ブロードリスニング本 原稿]] — 概念・事例・技術解説の原稿コレクション要約
- [[sources/broad-listening-book-core-concepts|ブロードリスニング本 概念編]] — ブロードリスニングの定義、アンケートとの差分、デジタル民主主義との接続を確認する個別章ソース
- [[sources/broad-listening-book-domestic-spread|ブロードリスニング本 国内広がり章]] — 国内の選挙・政党・報道・新聞社での実践を確認する事例章
- [[sources/broad-listening-book-shin-tokyo-2050|ブロードリスニング本 シン東京2050章]] — 東京都の長期戦略策定における論点地図の使い方を確認する個別章ソース
- [[sources/broad-listening-book-national-elections|ブロードリスニング本 国政選挙章]] — 複数政党が国政選挙でブロードリスニングを使い分けた事例章
- [[sources/broad-listening-book-team-mirai|ブロードリスニング本 チームみらい章]] — 入口設計・大量提案処理・フィードバック設計の事例章
- [[sources/broad-listening-book-local-elections|ブロードリスニング本 地方選挙章]] — 地方選挙での問いの設計、チャネル差、候補者の学習を確認する事例章
- [[sources/broad-listening-book-local-government|ブロードリスニング本 地方自治体での活用章]] — 自治体の広聴業務・住民会議に接続する事例章
- [[sources/broad-listening-book-enterprise|ブロードリスニング本 企業での活用章]] — 企業内のVOC分析・合意形成に接続する事例章
- [[sources/broad-listening-book-kouchou-ai-development|ブロードリスニング本 DD2030による広聴AI開発活動章]] — ブロードリスニングを支える広聴AIの開発史・OSS運営・普及活動の事例章
- [[sources/broad-listening-book-business-ecosystem|ブロードリスニング本 ビジネス化章]] — 現場導入・伴走支援・事業化の論点を確認する事例章
- [[sources/broad-listening-book-overseas|ブロードリスニング本 海外事例章]] — 熟議文化、Polis、Connective Action、制度接続の論点を確認する事例章
- [[sources/broad-listening-book-element-technologies|ブロードリスニング本 要素技術解説章]] — ブロードリスニングを支えるLLM・エンベディング・UMAP・クラスタリングの解説章
- [[sources/broad-listening-book-kouchou-ai-technical-stack|ブロードリスニング本 広聴AI技術スタック解説章]] — 広聴AIの処理パイプラインと設計トレードオフの解説章
- [[sources/broad-listening-book-public-cases|ブロードリスニング本 公開事例一覧]] — 公開URLつきの実践事例をカテゴリ別に確認する付録ソース
- [[sources/broad-listening-book-meeting|ブロードリスニング本 執筆定例 議事録]] — 書籍化と広聴AI開発定例のソース要約
- [[sources/idobata-project-minutes|いどばた プロジェクト議事録]] — ブロードリスニング型プロダクトの設計メモ
- [[topics/local-government-broad-listening|地方自治体でのブロードリスニング活用]] — 自治体の広聴業務・住民会議に接続する実践の整理
- [ブロードリスニング本 1章「ブロードリスニングとは何か？」](https://github.com/digitaldemocracy2030/broad-listening-book/blob/main/01_%E3%83%96%E3%83%AD%E3%83%BC%E3%83%89%E3%83%AA%E3%82%B9%E3%83%8B%E3%83%B3%E3%82%B0%E3%81%A8%E3%81%AF%E4%BD%95%E3%81%8B%EF%BC%9F.md) — 概念の詳細な解説
- [ブロードリスニング本 3章「デジタル民主主義とブロードリスニング」](https://github.com/digitaldemocracy2030/broad-listening-book/blob/main/03_%E3%83%87%E3%82%B8%E3%82%BF%E3%83%AB%E6%B0%91%E4%B8%BB%E4%B8%BB%E7%BE%A9%E3%81%A8%E3%83%96%E3%83%AD%E3%83%BC%E3%83%89%E3%83%AA%E3%82%B9%E3%83%8B%E3%83%B3%E3%82%B0%E3%80%81%E6%96%B0%E3%81%97%E3%81%84%E6%B0%91%E6%84%8F%E3%81%AE%E5%B1%8A%E3%81%91%E6%96%B9.md) — 理論的な位置づけ

## 関連ページ

- [[広聴AI]] — ブロードリスニングを実現するツール
- [[sources/broad-listening-book-core-concepts|ブロードリスニング本 概念編]] — ブロードリスニングの基本概念を確認する個別章ソース
- [[sources/broad-listening-book-domestic-spread|ブロードリスニング本 国内広がり章]] — 日本国内での初期実践と運用上の注意点を確認する個別章ソース
- [[sources/broad-listening-book-shin-tokyo-2050|ブロードリスニング本 シン東京2050章]] — 大都市行政でのブロードリスニング事例を確認する個別章ソース
- [[sources/broad-listening-book-national-elections|ブロードリスニング本 国政選挙章]] — 国政選挙におけるブロードリスニングの使い分けを確認する個別章ソース
- [[sources/broad-listening-book-local-elections|ブロードリスニング本 地方選挙章]] — 地方政治の現場でのブロードリスニング事例を確認する個別章ソース
- [[sources/broad-listening-book-kouchou-ai-development|ブロードリスニング本 DD2030による広聴AI開発活動章]] — 広聴AIの開発史からブロードリスニングの実装条件を確認する個別章ソース
- [[sources/broad-listening-book-business-ecosystem|ブロードリスニング本 ビジネス化章]] — 現場導入と事業化の観点からブロードリスニングを確認する個別章ソース
- [[sources/broad-listening-book-overseas|ブロードリスニング本 海外事例章]] — 海外の熟議実践から制度接続としてのブロードリスニングを確認する個別章ソース
- [[sources/broad-listening-book-element-technologies|ブロードリスニング本 要素技術解説章]] — 技術基礎からブロードリスニングを確認する個別章ソース
- [[sources/broad-listening-book-kouchou-ai-technical-stack|ブロードリスニング本 広聴AI技術スタック解説章]] — 広聴AIの実装からブロードリスニングを確認する個別章ソース
- [[sources/broad-listening-book-public-cases|ブロードリスニング本 公開事例一覧]] — 公開事例のURL索引を確認する個別章ソース
- [[いどばた]] — 対話プラットフォーム
- [[熟議民主主義]] — ブロードリスニングの後段にある合意形成の理論
- [[論点地図]] — ブロードリスニングが作る主要な成果物
- [[正統性の空白]] — ブロードリスニングが補完しようとする選挙サイクルの限界
- [[ミニ・パブリックス]] — ブロードリスニングに代表性を補う熟議参加者選定の考え方
- [[討論型世論調査]] — ブロードリスニングで発見した論点を、熟議前後の測定に接続する手法
- [[ボイス効果]] — 意見が届いた実感をどう設計するか
- [[ブロードリスニング本]] — 書籍化プロジェクト
- [[コアループ]] — ブロードリスニングを含む熟議プロセス設計
- [[多元現実]] — ブロードリスニング技術を住民会議・企業内合意形成に届ける企業
- [[倍速会議]] — 会議参加者の認識を事前に構造化し、熟議の前提共有に使うAI支援ツール
- [[ストップ詐欺広告]] — 通報データを政策形成に接続する実践例
- [[AIディープサーベイ]] — オンライン詐欺広告対策の自由記述を政策検討へ接続する調査入口
- [[events/2025-05-16-shabereru-manifesto|しゃべれるマニフェスト公開]] — 入口を対話UIに変えた大規模な政策提案受付の事例
- [[events/2025-06-12-kouchou-ai-reading-vol-1|広聴AI読書会vol.1]] — Pluralityとブロードリスニングの背景を読む初期読書会
- [[events/2025-08-hiroshima-kouchou-ai|広島県 広聴AI活用事例]] — 自治体でのブロードリスニング実践例
- [[events/2025-08-cybozu-idobata-workshop|サイボウズ社内AI利用推進ワークショップ]] — 企業内で見えにくい声を論点化した事例
- [[events/2025-11-ota-jibungotoka-baisoku|太田市 自分ごと化会議へのAI導入]] — 住民会議で議論前の認識を可視化した事例
- [[events/2025-11-29-code-for-japan-summit|Code for Japan Summit 2025 登壇]] — ブロードリスニングの流れとインサイト分類が外部共有されたイベント
- [[時系列まとめ]] — 四半期ごとの活動記録
- [[初年度まとめ]] — 立ち上がりから1年の詳細な時系列
- [[overview]] — プロジェクト全体の概要
