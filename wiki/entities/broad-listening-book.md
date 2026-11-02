---
title: ブロードリスニング本
aliases: [ブロードリスニング本]
tags: [dd2030, project, book]
sources:
  - raw/minutes/broad-listening-book-meeting.txt
  - raw/minutes/weekly-general-meeting.txt
  - digitaldemocracy2030/slack-logs/mirror/slack/C09J7A6HKRA.jsonl.gz
  - digitaldemocracy2030/slack-logs/mirror/slack/C08F7JZPD63.jsonl.gz
created: 2026-04-18
updated: 2026-11-03
---

# ブロードリスニング本

## 概要

dd2030コミュニティから生まれた書籍プロジェクト。[[ブロードリスニング]]の実践と理論を体系的にまとめた本。

## 書誌情報

- **タイトル**: 政治・自治体・企業に広がるブロードリスニング（2026年7月27日の定例メモで変更。2026年5月25日時点の案では副題「～生成AIによる民意の可視化と分析」が付いていた）
  - 旧仮タイトル: 選挙を変えたブロードリスニング──生成AIが実現する民意の可視化と分析。「自治体の話も多いので『選挙』は違うのでは」という議論（2026年4月27日）を経て変更された
- **出版社**: インプレス（担当編集: 片岡氏）
- **発売時期**: 未定（2026年11月2日時点）。2026年7月27日の定例メモでは「10〜11月目処」だったが、11月2日に中山が「原稿の直しが止まっているので未定」と答えた（Slack `#2_開発_広聴ai`）
- **規模**: 約37.9万文字（2026年6月21日のPDF Build時点）
- **推薦文**: オードリー・タン（Audrey Tang）
- **序文**: 安野たかひろ
- **あとがき**: 鈴木健（2026年5月に4ページで依頼、進行中）
- **原稿のライセンス**: CC-BY-NC（2026年5月4日にCC-BYから変更）
- **Webサイト**: [broadlisteningbook.com](https://broadlisteningbook.com/)（Luke Closs氏が構築・運営）
- **プロジェクトリーダー**: 中山心太（tokoroten）
- **印税契約**: 中山・西尾・角野の3名が印税契約、その他の執筆者は原稿料支払いとする案（2026年5月25日に提示）

## 進捗

- **2025年10月**: 出版決定（インプレスよりGO）
- **2025年12月**: マイルストーンM1（原稿締切目標）
- **2026年1月**: 定例を「ブロードリスニング本執筆定例」に改名、月曜20時に移動
- **2026年2月**: Audrey Tangのendorsement取得。30万文字規模に到達
- **2026年3月**: 原稿フリーズ・インプレスへ渡し。校正開始
- **2026年4月時点**: 修正・レビュー完了、5月の編集・組版、6月予約開始、9月発刊が最速予定として共有された
- **2026年4月20日**: インプレス社内レビューの結果を受けて図表の書き直し・リライトを開始。Code for Japanの原稿が届き、全記事が揃った
- **2026年4月27日**: Luke Closs氏が書籍Webサイト `broadlisteningbook.com` を公開（英語版はフル公開、日本語版は序文・技術章以外をパスワード制御）。日テレから画像引用許諾を取得
- **2026年5月4日**: 原稿執筆をいったん終了し、インプレスへ引き渡すことを決定。ライセンスをCC-BY-NCに変更。この回を最後に定例はいったん休止（ゲラが上がった時点などで再開）
- **2026年5月25日**: タイトルを「政治・自治体・企業に広がるブロードリスニング」の方向に。印税契約者と原稿料支払い者の整理、2色刷り（黒＋赤）向けの図表入稿方法を確認。インプレス側は原稿整理・紙面デザイン段階
- **2026年6月21日**: GitHub Actions の `PDF Build 20260621` がSlackに通知され、合計文字数は379,104字。尾花山担当章などのインプレス校正コメント対応PRも引き続き動いていた
- **2026年7月27日**: 定例メモで書籍タイトルを「政治・自治体・企業に広がるブロードリスニング」に変更、発売は10〜11月目処と記録

2026年4月時点では「6月予約開始・9月発刊」が最速予定として共有されていたが、2026年7月27日の定例メモでは発売は10〜11月目処に後ろ倒しされた。2026年11月2日時点では、出版時期を尋ねられた中山が「原稿の直しが止まっているので未定」と答えており、発売日は決まっていない。

## 章構成

| 章 | 内容 | 主な執筆者 |
|----|------|-----------|
| 序文 | 安野たかひろ | 安野 |
| 推薦文 | Audrey Tang | Tang |
| 1章 | [[sources/broad-listening-book-core-concepts|ブロードリスニングとは何か？]] | tokoroten |
| 2章 | [[sources/broad-listening-book-core-concepts|アンケートとの違い・定量→定性分析]] | tokoroten |
| 3章 | [[sources/broad-listening-book-core-concepts|デジタル民主主義とブロードリスニング]] | tokoroten |
| 4章 | [[sources/broad-listening-book-domestic-spread|国内ブロードリスニングの広がり]] | 複数 |
| — 4-1 | [[sources/broad-listening-book-domestic-spread|安野貴博の取り組み]] | nishio |
| — 4-2 | [[sources/broad-listening-book-domestic-spread|国民民主の国会質問]] | tokoroten |
| — 4-3 | [[sources/broad-listening-book-domestic-spread|日テレ選挙特番]] | sumino |
| — 4-4 | [[sources/broad-listening-book-domestic-spread|Polisで世論の地図を作る]] | nishio |
| — 4-5 | [[sources/broad-listening-book-domestic-spread|朝日新聞の特設記事]] | tokoroten |
| 5章 | [[sources/broad-listening-book-shin-tokyo-2050|東京都・シン東京2050]] | tokoroten |
| 6章 | [[sources/broad-listening-book-national-elections|国政選挙でのブロードリスニング]] | 複数 |
| — 6-1 | [[sources/broad-listening-book-team-mirai|チームみらい参院選・しゃべれるマニフェスト]] | nishio |
| — 6-2 | [[sources/broad-listening-book-national-elections|チームみらい2026衆院選]] | sumino |
| — 6-3〜5 | [[sources/broad-listening-book-national-elections|維新・国民民主・公明]] | tokoroten |
| 7章 | [[sources/broad-listening-book-local-elections|地方選挙での活用]] | 複数 |
| 8章 | 地方自治体での活用 | 複数 |
| — 8-1 | [[events/2025-11-ota-jibungotoka-baisoku|群馬県太田市の自分ごと化会議]] | — |
| — 8-2 | [[events/2025-08-hiroshima-kouchou-ai|広島県の事例]] | tokoroten |
| 9章 | 企業・NPOでの活用 | 複数 |
| — 9-1 | アルティウスリンク | — |
| — 9-2 | [[events/2025-08-cybozu-idobata-workshop|サイボウズ]] | nishio |
| 10章 | [[sources/broad-listening-book-business-ecosystem|ビジネスになったブロードリスニング]] | 複数 |
| — 10-0 | [[sources/broad-listening-book-kouchou-ai-development|DD2030による広聴AI開発]] | — |
| — 10-2 | Code for Japan | Code for Japan（2026年4月20日に原稿到着） |
| — 10-3 | [[多元現実]]（[[倍速会議]]） | bluemo |
| 11章 | [[sources/broad-listening-book-overseas|海外のブロードリスニング]] | 複数 |
| — 11-1 | 台湾 | nishio |
| — 11-2 | Polisの誕生 | — |
| — 11-4 | イスラエル・パレスチナ（Remesh事例） | — |
| — 11-5 | Connective Actionを力に変える | — |
| 12章 | [[sources/broad-listening-book-element-technologies|ブロードリスニング要素技術解説]] | tokoroten |
| 13章 | [[sources/broad-listening-book-kouchou-ai-technical-stack|広聴AIの技術スタック解説]] | tokoroten |
| 付録 | [[sources/broad-listening-book-public-cases|公開事例一覧]] | Ohki |
| あとがき | 解説・[[コアループ]]への接続（予定） | 鈴木健 |

上記は原稿リポジトリ上の構成。2026年5月4日の定例で、前付け（「本書の読み方」・用語集）を追加し、インプレス側で前付けを2部構成に書き直すこと、10章では[[多元現実]]の節を後ろに移して「1万人の声を集めて気づいたこと」と結合すること、8章の太田市と広島の順序を入れ替えたいことが挙げられている。最終的な章立ては `book_order.txt` と出版時の目次で確認が必要。

## 英語版

- lukec（@lukec、Luke Closs）が英語訳を進め、GitHubに公開済み。2026年6月時点でも英語版翻訳更新PRが動いており、2026年7月27日時点でも英語版は更新済み
- 2026年4月27日の定例で、Luke氏を「ブロードリスニング本Webサイトプロジェクト」および「英語版作成プロジェクト」のプロジェクトオーナーとし、dd2030の活動の一環として位置づけることにした（将来、他言語版を作りたい人が現れた場合も同様にプロジェクト化する）
- Webサイト `broadlisteningbook.com`（コード: `lukec/broad-listening-book-site`）は英語版をフル公開、日本語版は序文と技術章（00, 12, 13）以外をパスワード制御。2026年5月に「この本について」「本の問題を報告する」ページとGitHub Issueフォーム、引用共有機能（Share passage）が追加された
- 日本語版のオンライン公開はインプレス発売後6〜12か月経過してからが望ましい（カニバリゼーション懸念）。それまでは日本語版の技術章のみWeb公開し、他はインプレス公式サイトへのリンクにとどめる方針
- 2色刷りのCMYK入稿が必要なため、Web公開版・Kindle版との図版の整合は要検討（2026年5月25日）

## 2026年4月時点のステータス

- 校正・インプレス意見反映中
- 政党からの画像利用許諾待ち（維新・公明は反応なし、画像作り直しの方向）
- 日テレへの修正版原稿・スクショ引用許可依頼中（→ 4月27日に条件付きで許諾取得）
- Code for Japanの原稿が未提出（→ 4月20日に到着）

## 2026年4月下旬〜7月の動き（執筆定例より）

- **インプレス社内レビューへの対応**（4月20日〜）: 図表の書き直し（東京都の図など）、維新・公明の画像はリライトして著作権問題を回避、国民民主党は伊藤議員から画像提供を受けて差し替え。削った技術章の文章はオンライン版向けに復活させる方針。捨てたコラムはブログに焼き直す
- **引用許諾**: 日テレ（zero選挙）から出典明記・本文内のみ・改変禁止などの条件で画像引用の許諾を取得（4月27日）。朝日新聞の図表はインプレスに著作物利用申請を依頼（5月4日）
- **原稿の整理**（5月4日）: 「民意」を「民意」と「統計的世論」に分離、前書き・用語集・「本書の読み方」を作成、広島県・国民民主党からの修正依頼に対応。インプレスの社内評価で「節単位では面白いが、章単位で結合したPDFだと話の切れ目が分からない」という指摘があり、レイアウトで節の区切りを明示することになった
- **追加事例**: 自民党がブロードリスニングを行うという情報（2026年4月のX投稿）を受けて追記（4月20日）
- **契約・部数**（5月25日）: 企画案は最大4000部程度、12か月程度で増刷。印税契約者を3名に絞るのは、契約更新リスクと事務の手間を抑えるため。誰がどれだけ書いたかの一覧は中山が作成（リポジトリのcontributorは13人、AI・翻訳・誤字修正を除くと10人）
- **公式サイトでの見せ方**（5月4日）: dd2030.org では広聴AIを従来どおり主要プロダクトとして見せつつ、ブロードリスニング本を「第5の活動」として並べ、broadlisteningbook.com と相互リンクする方向で合意（大木氏の提案を受けて西尾が修正PRを作成予定）
- **イベント連携**（6月22日）: 8月2日の[[デジタル民主主義サミット2026]]でブロードリスニングに関するセッション（国会・地方政治の実践、技術、ツール）を出す案が議論された
- **執筆定例の位置づけ**: 5月4日以降、定例は書籍の進行報告と[[広聴AI]]の開発報告（大リファクタリング完了、Azureデモ環境の障害対応など）が混在する場になった。詳細は [[sources/broad-listening-book-meeting|ブロードリスニング本 執筆定例 議事録]] を参照

## 2026年10月の動き（Slack `#2_broad-listening-book` より）

- 7月の全体定例で「インプレスからのレスポンスが悪い」と報告されて以降、編集側とのやりとりが止まっていたが、10月13日に中山が編集をキックしたところ、**双方が相手の作業待ちだと思い込むデッドロック**だったことが判明し、作業を再開した
- 同日、**表紙案**を受領。オードリー・タンの名前の位置は上にある案で合意。序文でしか触れていない「AIインタビュアー」の語を表紙から外すかを検討。表紙の日本地図で北方四島・根室・沖縄の離島が切れていることが問題になり（安野（国政政党党首）の名前も載るため不要な憶測を呼ぶ、という指摘が10月27日にあった）、出版社側が生成AIで作った図だったため、中山が国土地理院の地図データと統計局の人口メッシュから図を作り直した（10月27〜28日）
- 原稿は AI（Opus 5.5）によるレビューを終え、中山が最終チェックのうえ提出した。この半年で語彙が変わり「生成AI」でなく単に「AI」と呼ぶ方向で揃える
- [[広聴AI]]側では、書籍刊行に合わせてメジャーリリース（5.0）を打つ方針（10月13日）

## 2026年11月の動き（Slack `#2_開発_広聴ai` より）

- 11月2日、西尾が出版時期を尋ね（出版前に、想定読者のペルソナを立てて公式ページやドキュメントを見直すスプリントをしたい、という文脈）、中山が「原稿の直しが止まっているので未定」と答えた。7月27日の「10〜11月目処」はこの時点で未達のまま、新しい目処は示されていない

## 2026年6月時点で確認できた動き

- 2026年6月21日に `PDF Build 20260621` が生成され、書籍全体は379,104字として集計された
- インプレス校正コメントへの対応PR、英語版翻訳更新PR、定例リマインドが `2_broad-listening-book` チャンネルで継続していた
- 予約開始や発売日の確定アナウンスは、このWikiが参照した6月後半のSlack mirror内では確認していない（その後、7月27日の定例メモで「10〜11月発売目処」と記録された）

## もっと詳しく

- [[sources/broad-listening-book-manuscript|ブロードリスニング本 原稿]] — `raw/broad-listening-book/` の原稿コレクション要約
- [[sources/broad-listening-book-core-concepts|ブロードリスニング本 概念編]] — 1〜3章の定義・アンケートとの差分・民主主義プロセスへの接続を確認する個別章ソース
- [[sources/broad-listening-book-domestic-spread|ブロードリスニング本 国内広がり章]] — 4章の安野都知事選・国民民主・日テレ・世論地図・朝日新聞事例を確認する個別章ソース
- [[sources/broad-listening-book-shin-tokyo-2050|ブロードリスニング本 シン東京2050章]] — 5章の東京都長期戦略策定事例を確認する個別章ソース
- [[sources/broad-listening-book-national-elections|ブロードリスニング本 国政選挙章]] — 6章の国政選挙事例を確認する個別章ソース
- [[sources/broad-listening-book-team-mirai|ブロードリスニング本 チームみらい章]] — 6章のしゃべれるマニフェスト事例を確認する個別章ソース
- [[sources/broad-listening-book-local-elections|ブロードリスニング本 地方選挙章]] — 7章の八代市長選・いでい良輔氏・尾花山和哉氏の事例を確認する個別章ソース
- [[sources/broad-listening-book-local-government|ブロードリスニング本 地方自治体での活用章]] — 8章の広島県・太田市事例を確認する個別章ソース
- [[sources/broad-listening-book-enterprise|ブロードリスニング本 企業での活用章]] — 9章のアルティウスリンク・サイボウズ事例を確認する個別章ソース
- [[sources/broad-listening-book-kouchou-ai-development|ブロードリスニング本 DD2030による広聴AI開発活動章]] — 10章0節のDD2030設立経緯・広聴AI開発史を確認する個別章ソース
- [[sources/broad-listening-book-business-ecosystem|ブロードリスニング本 ビジネス化章]] — 10章の導入伴走・自治体支援・熟議支援事例を確認する個別章ソース
- [[sources/broad-listening-book-overseas|ブロードリスニング本 海外事例章]] — 11章の台湾・Polis・ボーリンググリーン・Remesh・Connective Actionを確認する個別章ソース
- [[sources/broad-listening-book-element-technologies|ブロードリスニング本 要素技術解説章]] — 12章のLLM・エンベディング・UMAP・クラスタリング解説を確認する個別章ソース
- [[sources/broad-listening-book-kouchou-ai-technical-stack|ブロードリスニング本 広聴AI技術スタック解説章]] — 13章の広聴AI処理パイプラインを確認する個別章ソース
- [[sources/broad-listening-book-public-cases|ブロードリスニング本 公開事例一覧]] — 付録の公開URL一覧を確認する個別章ソース
- [[sources/broad-listening-book-meeting|ブロードリスニング本 執筆定例 議事録]] — 執筆・校正定例のWiki内ソース要約
- [[sources/weekly-general-meeting|週次全体定例 議事録]] — 全体定例側の進捗共有
- [[sources/history-week50-20260415|週次History week50（2026-04-15）]] — 2026年4月中旬時点の書籍編集・翻訳・章構成レビューを確認する個別週ソース
- [broad-listening-book GitHubリポジトリ](https://github.com/digitaldemocracy2030/broad-listening-book) — 書籍原稿の全文（Markdown）
- [ブロードリスニング本 執筆定例 議事録（Google Docs）](https://docs.google.com/document/d/1plggszRTxEEYUcZuCLiHkPrBsMtxr3RQpctKtZe5y4M) — 執筆・校正の進捗議事録

## 関連ページ

- [[ブロードリスニング]] — 本書のテーマ
- [[論点地図]] — 概念編・国内事例・行政事例で繰り返し扱われる主要成果物
- [[正統性の空白]] — 本書の概念編が示す、選挙サイクルだけでは新規争点を扱いにくい課題
- [[sources/broad-listening-book-core-concepts|ブロードリスニング本 概念編]] — 1〜3章の概念整理を確認する個別章ソース
- [[sources/broad-listening-book-domestic-spread|ブロードリスニング本 国内広がり章]] — 4章の国内事例を確認する個別章ソース
- [[sources/broad-listening-book-shin-tokyo-2050|ブロードリスニング本 シン東京2050章]] — 5章の東京都事例を確認する個別章ソース
- [[sources/broad-listening-book-national-elections|ブロードリスニング本 国政選挙章]] — 6章の国政選挙事例を確認する個別章ソース
- [[広聴AI]] — 技術解説の対象
- [[コアループ]] — 本書と連動するプロジェクト
- [[topics/local-government-broad-listening|地方自治体でのブロードリスニング活用]] — 8章の自治体事例を横断した整理
- [[events/2025-05-16-shabereru-manifesto|しゃべれるマニフェスト公開]] — 6章で扱うチームみらい参院選の主要事例
- [[sources/broad-listening-book-team-mirai|ブロードリスニング本 チームみらい章]] — 6章のチームみらい参院選事例を確認する個別章ソース
- [[sources/broad-listening-book-local-elections|ブロードリスニング本 地方選挙章]] — 7章の地方選挙事例を確認する個別章ソース
- [[sources/broad-listening-book-kouchou-ai-development|ブロードリスニング本 DD2030による広聴AI開発活動章]] — 10章0節の広聴AI開発史を確認する個別章ソース
- [[sources/broad-listening-book-business-ecosystem|ブロードリスニング本 ビジネス化章]] — 10章の事業化・現場導入支援を確認する個別章ソース
- [[多元現実]] — 10章で扱われる合意形成・拡張熟議支援の企業
- [[倍速会議]] — 8章・10章で扱われる住民会議/熟議支援ツール
- [[sources/broad-listening-book-overseas|ブロードリスニング本 海外事例章]] — 11章の海外事例と制度接続論を確認する個別章ソース
- [[sources/broad-listening-book-element-technologies|ブロードリスニング本 要素技術解説章]] — 12章の技術基礎を確認する個別章ソース
- [[sources/broad-listening-book-kouchou-ai-technical-stack|ブロードリスニング本 広聴AI技術スタック解説章]] — 13章の広聴AI実装解説を確認する個別章ソース
- [[sources/broad-listening-book-public-cases|ブロードリスニング本 公開事例一覧]] — 付録の公開事例URL一覧を確認する個別章ソース
- [[events/2025-08-hiroshima-kouchou-ai|広島県 広聴AI活用事例]] — 地方自治体でのブロードリスニング事例
- [[events/2025-08-cybozu-idobata-workshop|サイボウズ社内AI利用推進ワークショップ]] — 9章で扱う企業内いどばた活用事例
- [[events/2025-11-ota-jibungotoka-baisoku|太田市 自分ごと化会議へのAI導入]] — 住民会議にAI支援を入れた地方自治体事例
- [[events/2025-11-29-code-for-japan-summit|Code for Japan Summit 2025 登壇]] — 書籍構成やブロードリスニング説明と接続した外部発表
- [[デジタル民主主義サミット2026]] — 2026年8月2日のサミット。執筆定例でブロードリスニング関連セッションの構想が議論された
- [[時系列まとめ]] — 四半期ごとの活動記録
- [[初年度まとめ]] — 立ち上がりから1年の詳細な時系列
- [[主要メンバー]] — プロジェクトの主要な人物
- [[コミュニティと法人の関係]] — コミュニティ成果と法人の関係
- [[overview]] — プロジェクト全体の概要
