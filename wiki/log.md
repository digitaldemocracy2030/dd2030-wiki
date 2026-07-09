---
title: Wiki作業ログ
tags: [dd2030, log]
created: 2026-04-18
updated: 2026-07-09
---

# Wiki 作業ログ

取り込み・更新・メンテナンスの記録。

## [2026-07-09] file back | Devin.aiの課金・予算経緯を発掘して追記

- 更新: [[Devin.ai]]
- 追加確認した根拠: `nishio/oss_weekly_reporter/data/2025-05-21_to_2025-05-28/raw/slack/3_ボードメンバーロール.json`, `2025-09-17_to_2025-09-24/raw/slack/3_ボードメンバーロール.json`, `2025-12-24_to_2025-12-31/raw/slack/0_全体お知らせ.json`, `2026-06-10_to_2026-06-17/raw/slack/7_雑談.json`, `2026-06-17_to_2026-06-24/raw/slack/7_雑談.json`
- 保存した整理: 2026-06-23の「Devinの使い方・課金・トークン代を明文化したい」という質問を起点に、2025-05-23の月額10万円上限目安とクレジット購入、2025-09-23の337.50ドル/150ACU追加チャージ、2025-12-27の残予算認識、2026-06-13の未使用トークン活用問題まで遡って、課金運用を時系列で整理した
- 未確認として残した点: 2026-07時点の正確な残高・料金プラン・billing権限者・予算管理スプレッドシートの現在の扱い

## [2026-07-09] file back | Devin.aiの説明ページを追加

- 新規ページ: [[Devin.ai]]
- 元情報: ユーザー提供のSlack抜粋（課金・トークン・invite・用途の混乱）と、`digitaldemocracy2030/slack-logs/mirror/slack/C08PRQVQWSE.jsonl.gz` の `8_devinと人間たちの部屋` ログ
- 保存した整理: DevinはSlack botではなくGitHub連携を中心に動くAI開発エージェントであり、dd2030では対象リポジトリ・用途・費用見込みを明示して使う。課金残量はSlack botではなくDevinダッシュボードで確認する
- 更新: `wiki/index.md`, [[overview]], [[sources/broad-listening-book-kouchou-ai-development|ブロードリスニング本 DD2030による広聴AI開発活動章]], [[AI から Slack ログを参照するパターン]], [[dd2030-wiki の dd2030 org 移行]], [[Wiki保守運用]] から導線を追加

## [2026-07-09] file back | dd2030 Wikiとはページを追加

- 新規ページ: [[dd2030 Wikiとは]]
- 目的: このWikiの目的、載っているもの、載っていないもの、根拠確認の読み方を初見者向けに説明する入口を作成
- 更新: `wiki/index.md` の「まずはここから」「テーマ」に導線を追加し、[[overview]]、[[初めて読む人へ]]、[[sources/index|ソースカタログ]]、[[Slackログアーカイブ]]、[[Wiki保守運用]] からの戻り導線を追加

## [2026-07-09] migration | dd2030-wiki 新orgリポジトリを作成

- 作成: `digitaldemocracy2030/dd2030-wiki`
- 初期push: 旧 `nishio/dd2030-wiki` の `main` に移行準備コミットをpushした後、同じ `main` を新リポジトリへpush
- 新リポジトリ側の更新: `quartz.config.ts` の `baseUrl`、READMEの公開URL、Wiki内の自己参照GitHub URL、`scripts/upload_outline_eval.py` の GitHub blob URL を `digitaldemocracy2030/dd2030-wiki` へ切り替え
- 公開確認: `https://digitaldemocracy2030.github.io/dd2030-wiki/` がHTTP 200で公開済み
- 旧サイト対応: 旧 `nishio/dd2030-wiki` は `old-site/` 配信に切り替え、既存HTML 428ページ分を同じパスの新URLへ案内する「移動しました」告知ページに置換済み
- local remote: `origin` を `digitaldemocracy2030/dd2030-wiki`、旧repoを `nishio` remote に整理済み

## [2026-07-09] file back | dd2030-wiki org移行方針を二段階方式に修正

- 元情報: repository transfer で旧 `nishio.github.io/dd2030-wiki` が消えると、既存リンクがリンク切れになる可能性があるという指摘
- 方針修正: GitHub の repository transfer は使わず、`digitaldemocracy2030/dd2030-wiki` を新規作成して新サイトを公開し、旧 `nishio/dd2030-wiki` は残して「移動しました」告知サイトにする
- 更新: [[dd2030-wiki の dd2030 org 移行]], `wiki/index.md`, [[Wiki保守運用]], [[Slackログアーカイブ]], [[AI から Slack ログを参照するパターン]], [[OSS Weekly Reporter]]

## [2026-07-09] file back | dd2030-wiki org移行の作業ページを追加

- 元情報: 2026-07-03〜2026-07-04の Slack `2_コミュニティ運営` で、`nishio.github.io/dd2030-wiki` を dd2030 のリポジトリと AI で運用したいという相談があり、来週半ばごろに移管作業する方向になった
- 確認: 2026-07-09時点で `nishio/dd2030-wiki` は存在し、`digitaldemocracy2030/dd2030-wiki` は未作成。`nishio` は現リポジトリ admin かつ `digitaldemocracy2030` org admin
- 新規ページ: [[dd2030-wiki の dd2030 org 移行]]
- 保存した知見:
  - 初回整理では repository transfer を想定したが、旧URLのリンク切れリスクを踏まえて、後続の方針修正で二段階移行に更新した
  - 新リポジトリ側では `quartz.config.ts` の `baseUrl`、README、Wiki内の自己参照URL、GitHub Pages設定を確認する
  - `nishio/oss_weekly_reporter` は補助アーカイブとして意図的に残す参照なので、単純置換しない
- 更新: `wiki/index.md`, [[Wiki保守運用]], [[Slackログアーカイブ]], [[AI から Slack ログを参照するパターン]], [[OSS Weekly Reporter]]

## [2026-07-09] maintenance | 外部アーカイブcheckout先をworkに統一

- 目的: `slack-logs` などの外部リポジトリを `/tmp` に clone すると、予期せず消えた時に検索結果0件の原因を判別しにくいため、checkout 先をリポジトリ直下の `work/` に統一する
- 更新: `AGENTS.md`、`CLAUDE.md`、`README.md`、`archive_index.md`、[[Slackログアーカイブ]]、`scripts/search-archive.py`、`.gitignore`
- 方針: `work/` は git 管理外にし、`scripts/search-archive.py` の既定検索先も `work/slack-logs` と `work/oss_weekly_reporter/data` に変更した

## [2026-06-30] maintenance | website history更新の滞留を再確認

- 目的: [[OSS Weekly Reporter]] 周辺に残る `2026-06-04現在` の時間依存情報を、2026-06-30時点の GitHub 状態で再確認する
- 確認: `gh` で `digitaldemocracy2030/website` の PR #211 と Issue #170/#173/#177 を確認。PR #211 は OPEN（2026-04-22作成、2026-06-24更新、未merge）、Issue #170/#173/#177 もすべて OPEN
- 更新: [[OSS Weekly Reporter]] に「website history 更新の現状（2026-06-30）」を追加し、`draft PR` という不正確な表現を「自動生成PRの確認・merge」に補正。[[アーカイブパイプライン設計]]の残課題にも、PR/Issue がOPENのままであることを追記

## [2026-06-30] maintenance | Slack過去月canonicalの注意を導線へ反映

- 目的: `digitaldemocracy2030/slack-logs` の `raw/` が正規置き場である一方、2025-01〜2026-02の月次canonicalには本文が入っていない制約を、初見者向け導線とAI向け参照パターンにも反映する
- 確認: `slack-logs/raw/slack/*/*.jsonl.gz` の行数を月別集計し、2025-01〜2026-02は本文0件、2026-03は1,255件、2026-04は868件の本文メッセージがあることを確認
- 更新: [[topics/first-reader-guide|初めて読む人へ]]、[[AI から Slack ログを参照するパターン]]、[[OSS Weekly Reporter]]、[[アーカイブパイプライン設計]] に、古いSlack本文確認では `oss_weekly_reporter` の週次raw/markdownを補助根拠として併用する注意を追記

## [2026-06-30] events | ウェルカムミート#3の日付と根拠を補正

- 変更: [[events/2025-11-28-welcome-meet-3|ウェルカムミート#3]]を、2025年10月24日開催ではなく、2025年10月27日に告知された2025年11月28日開催予定のオンボーディングイベントとして整理し直した
- 根拠: `raw/minutes/weekly-general-meeting.txt` では10月3日・10月24日の企画メモがあり、`oss_weekly_reporter/data/2025-10-22_to_2025-10-29/raw/slack/0_全体お知らせ.json` では10月27日の告知本文に11月28日21:00〜21:40と記録されている
- 注意: 2026年6月30日時点の `digitaldemocracy2030/slack-logs` では、2025年10月canonicalがチャンネルメタデータのみだったため、古い出来事の本文確認には補助アーカイブも併用する必要がある
- 更新: [[Slackログアーカイブ]] と `archive_index.md` に、月次canonicalが本文を持たない期間の確認方法と補助アーカイブ併用ルールを追記

## [2026-06-30] concepts | 正統性の空白を追加

- 追加: [[正統性の空白]]
- 目的: [[ブロードリスニング]]が補おうとする選挙サイクル上の限界を、[[論点地図]]、[[熟議民主主義]]、[[ミニ・パブリックス]]、[[討論型世論調査]]の前提概念として辿れるようにする
- 根拠: `raw/broad-listening-book/03_デジタル民主主義とブロードリスニング、新しい民意の届け方.md`、`raw/broad-listening-book/05_東京都、シン東京2050、ブロードリスニングによる政策転換.md`、`raw/minutes/project-coreloop.txt`
- 注意: 選挙を否定する概念ではなく、任期中に急浮上する新規争点について、市民の論点把握・熟議・説明責任で補完する課題として整理する
- 更新: [[index]]、[[ブロードリスニング]]、[[論点地図]]、[[熟議民主主義]]、[[コアループ]]、自治体活用ページ、関連ソースページから導線を追加

## [2026-06-30] concepts | 論点地図を追加

- 追加: [[論点地図]]
- 目的: [[ブロードリスニング]]の成果物を「民意の比率」ではなく、自由記述から論点構造を作り、既存政策との差分や熟議の問いを見つける見取り図として説明する
- 根拠: `raw/broad-listening-book/03_デジタル民主主義とブロードリスニング、新しい民意の届け方.md`、`raw/broad-listening-book/04_02_国民民主の国会質問.md`、`raw/broad-listening-book/05_東京都、シン東京2050、ブロードリスニングによる政策転換.md`、`raw/minutes/project-coreloop.txt`
- 注意: 件数やクラスタの大きさを社会全体の支持率として扱わない。論点地図は政策判断・熟議設計の材料であり、AIが答えを出すものではない
- 更新: [[index]]、[[ブロードリスニング]]、[[討論型世論調査]]、[[ミニ・パブリックス]]、[[コアループ]]、[[倍速会議]]、自治体活用ページ、関連ソースページから導線を追加

## [2026-06-30] concepts | 討論型世論調査を追加

- 追加: [[討論型世論調査]]
- 目的: [[ブロードリスニング]]による論点発見、[[ミニ・パブリックス]]による参加者選定、熟議前後の意見測定を分けて理解できるようにし、[[コアループ]]のDP設計を初見者が追えるようにする
- 根拠: `raw/broad-listening-book/03_デジタル民主主義とブロードリスニング、新しい民意の届け方.md`、`raw/broad-listening-book/11_01_台湾.md`、`raw/minutes/project-coreloop.txt`、`raw/minutes/weekly-general-meeting.txt`
- 注意: Stanford Deliberate platform を使ったオンライン熟議と、正式な討論型世論調査という手法名を混同しない。コアループ資料では用語・監修・主催者と設計者の分離が確認論点として残っている
- 更新: [[index]]、[[熟議民主主義]]、[[ミニ・パブリックス]]、[[ブロードリスニング]]、[[コアループ]]、関連イベント・ソースページから導線を追加

## [2026-06-30] concepts | ミニ・パブリックスを追加

- 追加: [[ミニ・パブリックス]]
- 目的: [[ブロードリスニング]]の論点発見と、[[熟議民主主義]]で必要になる代表性の設計を分けて理解できるようにし、太田市事例・台湾事例・[[コアループ]]の討論型世論調査検討を横断して辿れるようにする
- 根拠: `raw/broad-listening-book/03_デジタル民主主義とブロードリスニング、新しい民意の届け方.md`、`raw/broad-listening-book/08_01_群馬県太田市の自分ごと化会議.md`、`raw/broad-listening-book/11_01_台湾.md`、`raw/minutes/project-coreloop.txt`
- 注意: 無作為抽出・層化抽出をしても応募者バイアスや運営設計の影響は残るため、AIによる論点整理と熟議の正統性を混同しない
- 更新: [[index]]、[[ブロードリスニング]]、[[熟議民主主義]]、[[コアループ]]、[[倍速会議]]、[[多元現実]]、太田市イベント、関連ソースページから導線を追加

## [2026-06-30] entities | 多元現実を追加

- 追加: [[多元現実]]
- 目的: [[倍速会議]]、太田市の住民会議、サイボウズ社内ワークショップ、[[コアループ]]前段のAI支援熟議を、ブロードリスニング技術を現場に届ける主体から辿れるようにする
- 根拠: `raw/broad-listening-book/10_03_多元現実.md`、`raw/broad-listening-book/08_01_群馬県太田市の自分ごと化会議.md`、`raw/broad-listening-book/column/1万件の声を集めて気づいたこと.md`
- 注意: 書籍原稿の自己紹介・事例紹介を広告的評価として扱わず、現場導入・プロセス設計・技術協力の役割として整理する
- 更新: [[index]]、[[overview]]、[[ブロードリスニング]]、[[熟議民主主義]]、[[広聴AI]]、[[いどばた]]、[[コアループ]]、[[ブロードリスニング本]]、[[倍速会議]]、関連イベント・ソースページから導線を追加

## [2026-06-30] file back | 薄いページを無理に作らない方針を追記

- 背景: Wiki改善の進捗確認中に、活動には波があり、内容の薄いページを無理に作る必要はないという運用判断を確認した
- 方針: イベントページや週次History個別ページは、節目性・参照価値・根拠の強さがあるものに絞る。実施済みか未実施か曖昧なイベントや活動量の少ない週は、独立ページ化より既存ページの注記や導線改善を優先する
- 更新: [[sources/weekly-history-reports|週次Historyレポート]]、[[index]]、`PLAN.md` に、全週・全イベントを機械的に個別ページ化しない方針を追記

## [2026-06-30] entities | 倍速会議を追加

- 追加: [[倍速会議]]
- 目的: 太田市の無作為抽出型住民会議、dd2030の1月10日熟議実験、コアループ前段のツール検討を、AIファシリテーション支援ツールとして一箇所から辿れるようにする
- 根拠: `raw/broad-listening-book/08_01_群馬県太田市の自分ごと化会議.md`、`raw/broad-listening-book/10_03_多元現実.md`、`raw/history/week43_20260114/slack.md`、`raw/minutes/project-coreloop.txt`
- 注意: 倍速会議の出力を社会全体の代表意見として扱わず、参加者設計・募集経路・ファシリテーターによる確認と分けて読む
- 更新: [[index]]、[[overview]]、[[ブロードリスニング]]、[[熟議民主主義]]、[[コアループ]]、[[ブロードリスニング本]]、[[topics/local-government-broad-listening|地方自治体でのブロードリスニング活用]]、関連イベント・ソースページから導線を追加

## [2026-06-30] entities | AIディープサーベイを追加

- 追加: [[AIディープサーベイ]]
- 目的: [[コアループ]]のオンライン詐欺広告対策で、通報基盤とは別に市民の意見・対策案をAI対話で集め、法規制検討・ワークショップ・熟議設計へ渡す入口を辿れるようにする
- 根拠: `raw/minutes/project-coreloop.txt`、`raw/minutes/weekly-general-meeting.txt`、`raw/history/week50_20260415/slack.md`
- 注意: 回答結果を社会全体の代表意見として扱わず、募集経路・回答者属性・分析方法・熟議参加者抽出とは分けて確認する
- 更新: [[index]]、[[overview]]、[[コアループ]]、[[ストップ詐欺広告]]、[[ブロードリスニング]]、[[熟議民主主義]]、[[events/2026-04-18-coreloop-workshop|コアループ ワークショップ]]、[[events/2026-06-21-coreloop-online-deliberation|コアループ オンライン熟議]]、関連ソースページから導線を追加

## [2026-06-30] sources | 週次History week50を個別ソース化

- 追加: [[sources/history-week50-20260415|週次History week50（2026-04-15）]]
- 目的: `raw/history/` に取り込まれている最後の週を個別ページ化し、2026年4月中旬時点の[[ブロードリスニング本]]、[[コアループ]]、[[Polimoney]]、[[広聴AI]]の状態と、以後は `digitaldemocracy2030/slack-logs` を参照する境界を明確にする
- 根拠: `raw/history/week50_20260415/slack.md`、`raw/history/week50_20260415/kouchou-ai.md`、`raw/history/week50_20260415/website.md`
- 注意: 週次HistoryはSlack/GitHub活動を加工したまとめであり、2026年4月15日以後の状態や細部の確認には[[Slackログアーカイブ]]からSlack canonical/mirrorを検索する
- 更新: [[sources/index|ソースカタログ]]、[[sources/weekly-history-reports|週次Historyレポート]]、[[Slackログアーカイブ]]、[[index]]、[[ブロードリスニング本]]、[[コアループ]]、[[Polimoney]]、[[広聴AI]] から導線を追加

## [2026-06-30] sources | ブロードリスニング本 公開事例一覧を個別ソース化

- 追加: [[sources/broad-listening-book-public-cases|ブロードリスニング本 公開事例一覧]]
- 目的: 行政・自治体、政党・政治、メディア、選挙関連、企業の公開事例URLを、章本文とは別の索引として辿れるようにする
- 根拠: `raw/broad-listening-book/99_付録_公開事例一覧.md`
- 注意: 付録は公開URLの確認先であり、各事例の成果や評価を証明する表ではない。件数や実施時期を使う場合は、原稿脚注や外部公開資料まで戻って確認する
- 更新: [[sources/index|ソースカタログ]]、[[sources/broad-listening-book-manuscript|ブロードリスニング本 原稿]]、[[ブロードリスニング本]]、[[ブロードリスニング]]、関連する章ソース、[[topics/local-government-broad-listening|地方自治体でのブロードリスニング活用]] から導線を追加

## [2026-06-30] sources | ブロードリスニング本 ビジネス化章を個別ソース化

- 追加: [[sources/broad-listening-book-business-ecosystem|ブロードリスニング本 ビジネス化章]]
- 目的: DD2030のOSS開発だけでは届ききらない現場導入を、ブーツ、Code for Japan、多元現実、Democracy X、Litelaの伴走・事業化・熟議支援・対面議論支援から辿れるようにする
- 根拠: `raw/broad-listening-book/10_ビジネスになったブロードリスニング.md`、`raw/broad-listening-book/10_00_DD2030による広聴AIの開発活動.md`、`raw/broad-listening-book/10_01_株式会社ブーツ.md`、`raw/broad-listening-book/10_02_Code for Japan.md`、`raw/broad-listening-book/10_03_多元現実.md`、`raw/broad-listening-book/10_04_Democracy X.md`、`raw/broad-listening-book/10_05_litela_田中魁.md`
- 注意: 各企業・団体の自己紹介や展望を広告的評価として扱わず、ブロードリスニングが現場に届くための役割分担、自治体実務制約、参加プロセス設計の知識として読む
- 更新: [[sources/index|ソースカタログ]]、[[sources/broad-listening-book-manuscript|ブロードリスニング本 原稿]]、[[ブロードリスニング本]]、[[ブロードリスニング]]、[[広聴AI]]、[[いどばた]]、[[熟議民主主義]]、[[sources/broad-listening-book-kouchou-ai-development|ブロードリスニング本 DD2030による広聴AI開発活動章]]、[[sources/broad-listening-book-local-government|ブロードリスニング本 地方自治体での活用章]]、[[sources/broad-listening-book-enterprise|ブロードリスニング本 企業での活用章]]、[[sources/broad-listening-book-local-elections|ブロードリスニング本 地方選挙章]]、[[topics/local-government-broad-listening|地方自治体でのブロードリスニング活用]] から導線を追加

## [2026-06-30] sources | ブロードリスニング本 国政選挙章を個別ソース化

- 追加: [[sources/broad-listening-book-national-elections|ブロードリスニング本 国政選挙章]]
- 目的: チームみらい、維新、国民民主、公明の国政選挙事例を、各党の収集チャネル、分析設計、政策反映、組織運用の違いから比較できるようにする
- 根拠: `raw/broad-listening-book/06_国政選挙でのブロードリスニングの利用.md`、`raw/broad-listening-book/06_01_チームみらい.md`、`raw/broad-listening-book/06_02_チームみらい2026年衆院選.md`、`raw/broad-listening-book/06_03_日本維新の会.md`、`raw/broad-listening-book/06_04_国民民主党.md`、`raw/broad-listening-book/06_05_公明党.md`
- 注意: 政党・候補者の評価ではなく、国政選挙でのブロードリスニング実装の違いとして扱う。意見件数や投稿数を有権者全体の支持率として読まない
- 更新: [[sources/index|ソースカタログ]]、[[sources/broad-listening-book-manuscript|ブロードリスニング本 原稿]]、[[ブロードリスニング本]]、[[ブロードリスニング]]、[[sources/broad-listening-book-domestic-spread|ブロードリスニング本 国内広がり章]]、[[sources/broad-listening-book-team-mirai|ブロードリスニング本 チームみらい章]]、[[sources/broad-listening-book-local-elections|ブロードリスニング本 地方選挙章]] から導線を追加

## [2026-06-30] sources | ブロードリスニング本 地方選挙章を個別ソース化

- 追加: [[sources/broad-listening-book-local-elections|ブロードリスニング本 地方選挙章]]
- 目的: 八代市長選、いでい良輔氏、尾花山和哉氏の事例を通じて、地方選挙での[[ブロードリスニング]]が候補者の問いの設計、チャネル差、政策判断にどう関わるかを辿れるようにする
- 根拠: `raw/broad-listening-book/07_地方選挙での活用.md`、`raw/broad-listening-book/07_02_いでい良輔氏のケース.md`、`raw/broad-listening-book/07_03_再生の道_尾花山和哉.md`、補助参照として `raw/broad-listening-book/10_04_Democracy X.md`
- 注意: 八代市長選の詳細節は現状の7章配下にはなく、導入章とDemocracy X章の補助記述を合わせて読む。意見件数やクラスタの大きさを有権者全体の支持率として扱わない
- 更新: [[sources/index|ソースカタログ]]、[[sources/broad-listening-book-manuscript|ブロードリスニング本 原稿]]、[[ブロードリスニング本]]、[[ブロードリスニング]]、[[sources/broad-listening-book-domestic-spread|ブロードリスニング本 国内広がり章]]、[[sources/broad-listening-book-local-government|ブロードリスニング本 地方自治体での活用章]] から導線を追加

## [2026-06-30] sources | ブロードリスニング本 国内広がり章を個別ソース化

- 追加: [[sources/broad-listening-book-domestic-spread|ブロードリスニング本 国内広がり章]]
- 目的: 2024年東京都知事選の安野貴博氏の取り組みから、国民民主党の国会質問、日テレ選挙特番、JAPAN CHOICE世論地図、朝日新聞のデータジャーナリズムへ広がった国内実践を、[[ブロードリスニング]]の初期展開として辿れるようにする
- 根拠: `raw/broad-listening-book/04_日本国内におけるブロードリスニングの広がり.md`、`raw/broad-listening-book/04_01_安野貴博の取り組み.md`、`raw/broad-listening-book/04_02_国民民主の国会質問.md`、`raw/broad-listening-book/04_03_sumino_日テレ選挙特番.md`、`raw/broad-listening-book/04_04_Polisで世論の地図を作る.md`、`raw/broad-listening-book/04_05_朝日新聞の特設記事.md`
- 注意: 章内の事例は政党・候補者・報道機関の実践を扱うが、Wikiでは支持や評価ではなく、データ取得設計、代表性の説明、人間レビュー、組織内の受け取り手という運用知として整理する
- 更新: [[sources/index|ソースカタログ]]、[[sources/broad-listening-book-manuscript|ブロードリスニング本 原稿]]、[[ブロードリスニング本]]、[[ブロードリスニング]]、[[sources/broad-listening-book-core-concepts|ブロードリスニング本 概念編]]、[[sources/broad-listening-book-overseas|ブロードリスニング本 海外事例章]] から導線を追加

## [2026-06-30] sources | ブロードリスニング本 海外事例章を個別ソース化

- 追加: [[sources/broad-listening-book-overseas|ブロードリスニング本 海外事例章]]
- 目的: 台湾、Polis、ボーリンググリーン、イスラエル・パレスチナのRemesh事例、Connective Actionを、[[ブロードリスニング]]と[[熟議民主主義]]の制度接続論として辿れるようにする
- 根拠: `raw/broad-listening-book/11_海外におけるブロードリスニングの流れ.md`、`raw/broad-listening-book/11_01_台湾.md`、`raw/broad-listening-book/11_02_Polisの誕生.md`、`raw/broad-listening-book/11_03_ボーリンググリーン.md`、`raw/broad-listening-book/11_04_イスラエルパレスチナRemesh事例.md`、`raw/broad-listening-book/11_05_Connective_Actionを力に変える.md`
- 注意: 章内のConnective Action四象限や制度接続論は書籍側の独自整理を含む。合意率の高さを政策実現や紛争解決の成功と同一視しない
- 更新: [[sources/index|ソースカタログ]]、[[sources/broad-listening-book-manuscript|ブロードリスニング本 原稿]]、[[ブロードリスニング本]]、[[ブロードリスニング]]、[[熟議民主主義]]、[[sources/broad-listening-book-core-concepts|ブロードリスニング本 概念編]] から導線を追加

## [2026-06-30] sources | ブロードリスニング本 シン東京2050章を個別ソース化

- 追加: [[sources/broad-listening-book-shin-tokyo-2050|ブロードリスニング本 シン東京2050章]]
- 目的: 東京都「シン東京2050」プロジェクトを、大都市行政における[[ブロードリスニング]]活用事例として辿れるようにする。27,915件の意見収集だけでなく、複数チャネル設計、若者・子どもの声、観光独立の解釈、論点地図と政策体系の関係を整理する
- 根拠: `raw/broad-listening-book/05_東京都、シン東京2050、ブロードリスニングによる政策転換.md`
- 注意: 章には筆者の検証・推測が含まれるため、「ブロードリスニングが政策を変えた」という因果関係は断定せず、公開情報から確認できる範囲と推測を分けて読む
- 更新: [[sources/index|ソースカタログ]]、[[sources/broad-listening-book-manuscript|ブロードリスニング本 原稿]]、[[ブロードリスニング本]]、[[ブロードリスニング]]、[[topics/local-government-broad-listening|地方自治体でのブロードリスニング活用]]、[[sources/broad-listening-book-core-concepts|ブロードリスニング本 概念編]] から導線を追加

## [2026-06-30] sources | ブロードリスニング本 概念編を個別ソース化

- 追加: [[sources/broad-listening-book-core-concepts|ブロードリスニング本 概念編]]
- 目的: [[ブロードリスニング]]を、AI分析ツールだけではなく、定性分析・論点地図・拡張熟議・デジタル民主主義プロセスに接続する概念として辿れるようにする
- 根拠: `raw/broad-listening-book/01_ブロードリスニングとは何か？.md`、`raw/broad-listening-book/02_ブロードリスニングとアンケートの違い、定量分析から定性分析へ.md`、`raw/broad-listening-book/03_デジタル民主主義とブロードリスニング、新しい民意の届け方.md`
- 注意: ブロードリスニングは民意の比率を測る道具ではなく、論点探索・仮説生成のための定性分析として扱う。意見件数と社会全体の支持率を混同しない
- 更新: [[sources/index|ソースカタログ]]、[[sources/broad-listening-book-manuscript|ブロードリスニング本 原稿]]、[[ブロードリスニング本]]、[[ブロードリスニング]]、[[熟議民主主義]]、[[広聴AI]]、技術章ソースページから導線を追加

## [2026-06-30] sources | ブロードリスニング本 技術章を個別ソース化

- 追加:
  - [[sources/broad-listening-book-element-technologies|ブロードリスニング本 要素技術解説章]]
  - [[sources/broad-listening-book-kouchou-ai-technical-stack|ブロードリスニング本 広聴AI技術スタック解説章]]
- 目的: [[広聴AI]]の技術説明を、外部GitHubリンクだけでなくWiki内のソース要約から辿れるようにし、LLM・エンベディング・UMAP・K-means・Ward法・ラベリング・賛否分離課題の位置づけを初見者向けに整理する
- 根拠: `raw/broad-listening-book/12_ブロードリスニング要素技術解説.md`、`raw/broad-listening-book/13_広聴AIの技術スタック解説.md`
- 注意: 原稿は技術思想の説明であり、GitHubリポジトリの最新実装仕様そのものではない。外部研究やモデル提供状況を厳密に使う場合は原稿脚注や一次資料へ戻る
- 更新: [[sources/index|ソースカタログ]]、[[sources/broad-listening-book-manuscript|ブロードリスニング本 原稿]]、[[ブロードリスニング本]]、[[広聴AI]]、[[ブロードリスニング]]、[[sources/broad-listening-book-kouchou-ai-development|ブロードリスニング本 DD2030による広聴AI開発活動章]] から導線を追加。[[広聴AI]]の技術スタック欄を、書籍10章・13章に合わせてUMAP、K-means、Ward法の説明へ補正

## [2026-06-30] sources | ブロードリスニング本 広聴AI開発活動章を個別ソース化

- 追加: [[sources/broad-listening-book-kouchou-ai-development|ブロードリスニング本 DD2030による広聴AI開発活動章]]
- 目的: [[広聴AI]]が Talk to the City 由来のツールからWebアプリ化され、DD2030の政治的中立性、OSSフォーク、AIコーディング、自治体普及活動と結びついて発展した経緯を、原稿コレクションから一段深く辿れるようにする
- 根拠: `raw/broad-listening-book/10_00_DD2030による広聴AIの開発活動.md`
- 注意: 本章は開発活動史と普及活動の整理であり、詳細な要素技術仕様は原稿12章・13章もあわせて確認する
- 更新: [[sources/index|ソースカタログ]]、[[sources/broad-listening-book-manuscript|ブロードリスニング本 原稿]]、[[ブロードリスニング本]]、[[overview]]、[[広聴AI]]、[[ブロードリスニング]]、[[events/2025-05-16-shabereru-manifesto|しゃべれるマニフェスト公開]]、[[sources/broad-listening-book-team-mirai|ブロードリスニング本 チームみらい章]] から導線を追加

## [2026-06-30] sources | ブロードリスニング本 チームみらい章を個別ソース化

- 追加: [[sources/broad-listening-book-team-mirai|ブロードリスニング本 チームみらい章]]
- 目的: [[events/2025-05-16-shabereru-manifesto|しゃべれるマニフェスト公開]]、[[いどばた]]政策、[[広聴AI]]による内部可視化、[[ボイス効果]]につながる両方向トレーサビリティの学びを、原稿コレクションから一段深く辿れるようにする
- 根拠: `raw/broad-listening-book/06_01_チームみらい.md`
- 注意: チームみらいの活動そのものを評価・支持するのではなく、dd2030由来のOSSプロダクト利用事例と設計上の学びとして扱う
- 更新: [[sources/index|ソースカタログ]]、[[sources/broad-listening-book-manuscript|ブロードリスニング本 原稿]]、[[ブロードリスニング本]]、[[events/2025-05-16-shabereru-manifesto|しゃべれるマニフェスト公開]]、[[いどばた]]、[[広聴AI]]、[[ブロードリスニング]]、[[ボイス効果]] から導線を追加

## [2026-06-30] events/sources | サイボウズ企業事例を追加

- 追加:
  - [[events/2025-08-cybozu-idobata-workshop|サイボウズ社内AI利用推進ワークショップ]]
  - [[sources/broad-listening-book-enterprise|ブロードリスニング本 企業での活用章]]
- 目的: [[いどばた]]の企業内活用と、[[ブロードリスニング]]が政治・行政以外の組織運営にも展開していることを辿れるようにする
- 根拠: `raw/broad-listening-book/09_企業での活用.md`、`raw/broad-listening-book/09_01_アルティウスリンク_取材記事.md`、`raw/broad-listening-book/09_02_サイボウズ.md`、`raw/minutes/idobata-project.txt`
- 注意: 2025年8月の約50人ワークショップと、2025年10月メモにある後続の80人規模社内実験を混同しないよう本文で分けた
- 更新: [[index]]、[[overview]]、[[時系列まとめ]]、[[初年度まとめ]]、[[いどばた]]、[[ブロードリスニング]]、[[ブロードリスニング本]]、関連ソースページから導線を追加

## [2026-06-30] events | しゃべれるマニフェスト公開をイベント化

- 追加: [[events/2025-05-16-shabereru-manifesto|しゃべれるマニフェスト公開]]
- 目的: [[いどばた]]政策が大規模に使われた初期事例を、入口設計・大量提案処理・両方向トレーサビリティの学びとして辿れるようにする
- 根拠: `raw/broad-listening-book/06_01_チームみらい.md`、`raw/minutes/idobata-project.txt`、`raw/minutes/weekly-general-meeting.txt`、`raw/history/week10_20250521/slack.md`
- 更新: [[index]]、[[overview]]、[[時系列まとめ]]、[[初年度まとめ]]、[[いどばた]]、[[広聴AI]]、[[ブロードリスニング]]、[[ブロードリスニング本]]、関連ソースページから導線を追加

## [2026-06-30] events | チームみらいいどばたビジョン活用をイベント化

- 追加: [[events/2025-05-17-team-mirai-idobata-vision|チームみらい選挙ボランティア向けミートアップでのいどばたビジョン活用]]
- 目的: [[いどばた]]ビジョンの初期外部利用事例を、特定政党の支持ではなくOSSプロダクトの実利用から得た学びとして辿れるようにする
- 根拠: `raw/minutes/idobata-project.txt`、`raw/minutes/weekly-general-meeting.txt`、`raw/history/week10_20250521/slack.md`
- 更新: [[index]]、[[overview]]、[[時系列まとめ]]、[[初年度まとめ]]、[[いどばた]]、[[events/2025-05-25-meetup-2|MEETUP #2]]、関連ソースページから導線を追加

## [2026-06-30] sources | ブロードリスニング本 地方自治体章を個別ソース化

- 追加: [[sources/broad-listening-book-local-government|ブロードリスニング本 地方自治体での活用章]]
- 目的: 広島県・太田市の自治体事例を、原稿コレクションから一段深く辿れるようにする
- 根拠: `raw/broad-listening-book/08_地方自治体での活用.md`、`raw/broad-listening-book/08_01_群馬県太田市の自分ごと化会議.md`、`raw/broad-listening-book/08_02_広島県の事例.md`
- 更新: [[sources/index|ソースカタログ]]、[[sources/broad-listening-book-manuscript|ブロードリスニング本 原稿]]、[[topics/local-government-broad-listening|地方自治体でのブロードリスニング活用]]、関連イベント、[[ブロードリスニング本]]、[[ブロードリスニング]]、[[index]] から導線を追加

## [2026-06-30] sources | 週次History week43を個別ソース化

- 追加: [[sources/history-week43-20260114|週次History week43（2026-01-14）]]
- 目的: [[events/2026-01-10-deliberation-workshop|熟議民主主義プロセス ワークショップ]]、[[コアループ]]キックオフ、[[events/2026-01-09-burikaigi-polimoney|ぶり会議2026 Polimoney登壇]]直後の外向け発信強化を、同じ週の文脈で辿れるようにする
- 根拠: `raw/history/week43_20260114/slack.md`
- 更新: [[sources/index|ソースカタログ]]、[[sources/weekly-history-reports|週次Historyレポート]]、[[Slackログアーカイブ]]、[[index]]、関連イベント、[[Polimoney]]、[[コアループ]] から導線を追加

## [2026-06-30] sources | 週次History week33を個別ソース化

- 追加: [[sources/history-week33-20251029|週次History week33（2025-10-29）]]
- 目的: [[events/2025-11-28-welcome-meet-3|ウェルカムミート#3]]の根拠になった週次Historyを、コレクション要約から一段深く辿れるようにする
- 根拠: `raw/history/week33_20251029/slack.md`
- 更新: [[sources/index|ソースカタログ]]、[[sources/weekly-history-reports|週次Historyレポート]]、[[Slackログアーカイブ]]、[[index]]、[[events/2025-11-28-welcome-meet-3|ウェルカムミート#3]] から導線を追加

## [2026-06-30] maintenance | 初年度まとめの外部アーカイブ説明を補正

- 対象: [[初年度まとめ]]、[[Slackログアーカイブ]]
- 目的: 初年度まとめが主に `raw/history/` と `oss_weekly_reporter` をもとに作成されたページであることと、現在のSlackチャットログ本体は `digitaldemocracy2030/slack-logs` で再確認することを分けて読めるようにする
- 更新: [[初年度まとめ]] の冒頭と「含まれていない可能性があるもの」を補正し、[[Slackログアーカイブ]] への再確認導線を追加

## [2026-06-30] events | ウェルカムミート#3を追加

- 追加: [[events/2025-11-28-welcome-meet-3|ウェルカムミート#3（2025-11-28）]]
- 目的: 2025年10月時点の参加導線を、[[コミュニティ運営]]と時系列から辿れるようにする
- 根拠: `raw/history/week33_20251029/slack.md`、`raw/minutes/weekly-general-meeting.txt`
- 注意: 参照できたのは告知と企画メモであり、当日の詳細議事録や参加者の個別発言は扱わない
- 更新: [[index]]、[[overview]]、[[コミュニティ運営]]、[[sources/weekly-history-reports|週次Historyレポート]]、[[sources/weekly-general-meeting|週次全体定例 議事録]]、[[時系列まとめ]]、[[初年度まとめ]] から導線を追加

## [2026-06-30] events | ぶり会議2026 Polimoney登壇を追加

- 追加: [[events/2026-01-09-burikaigi-polimoney|ぶり会議2026 Polimoney登壇（2026-01-09）]]
- 目的: [[Polimoney]]が政治資金データの扱いにくさを、外部のエンジニア向けシビックテック文脈で説明した節目を辿れるようにする
- 根拠: `raw/minutes/polimoney.txt`、`raw/history/week42_20260107/slack.md`、`raw/history/week43_20260114/slack.md`
- 注意: 議事録内の記事草稿・動画案は未確認の公開素材を含むため、Wikiでは長い引用や公開断定を避け、登壇の位置づけに絞って要約
- 更新: [[index]]、[[Polimoney]]、[[topics/political-funds-and-campaign-expenses|政治資金収支報告書と選挙運動費用収支報告書]]、[[sources/polimoney-minutes|Polimoney 議事録]]、[[sources/weekly-history-reports|週次Historyレポート]]、[[時系列まとめ]]、[[初年度まとめ]]、[[overview]] から導線を追加

## [2026-06-30] topics | Polimoneyの対象書類の違いを整理

- 追加: [[topics/political-funds-and-campaign-expenses|政治資金収支報告書と選挙運動費用収支報告書]]
- 目的: [[Polimoney]]の進捗を「政治資金の可視化」「選挙運動費用への対応」「Ledgerによる入力支援」に分けて読めるようにする
- 根拠: `raw/minutes/polimoney.txt`、`raw/minutes/weekly-general-meeting.txt`、`raw/history/week25_20250903/polimoney.md`、`raw/history/week26_20250910/polimoney.md`
- 更新: [[Polimoney]]、[[sources/polimoney-minutes|Polimoney 議事録]]、[[overview]]、[[index]] から導線を追加し、Polimoneyの状態表現を日付つきに補正

## [2026-06-30] topics | 地方自治体でのブロードリスニング活用を追加

- 追加: [[topics/local-government-broad-listening|地方自治体でのブロードリスニング活用]]
- 目的: 広島県と太田市の自治体事例を、個別イベントではなく「自治体でどう使うか」という観点から横断して読めるようにする
- 根拠: `raw/broad-listening-book/08_地方自治体での活用.md`、広島県・太田市の事例章、関連する週次History
- 更新: [[index]]、[[ブロードリスニング]]、[[広聴AI]]、[[熟議民主主義]]、[[ブロードリスニング本]]、関連イベント、[[sources/broad-listening-book-manuscript|ブロードリスニング本 原稿]] から導線を追加

## [2026-06-30] events | 太田市 自分ごと化会議へのAI導入を追加

- 追加: [[events/2025-11-ota-jibungotoka-baisoku|太田市 自分ごと化会議へのAI導入（2025年度）]]
- 目的: [[ブロードリスニング]]を住民会議・[[熟議民主主義]]の前提共有に使う外部事例を辿れるようにする
- 根拠: `raw/broad-listening-book/08_01_群馬県太田市の自分ごと化会議.md`、`raw/broad-listening-book/08_地方自治体での活用.md`、`raw/history/week40_20251217/slack.md`、`raw/history/week42_20260107/slack.md`、`raw/history/week43_20260114/slack.md`
- 注意: 原稿内に成果測定・コメント引用許諾の確認メモが残るため、成果数値は原稿時点の整理として扱う
- 更新: [[index]]、[[ブロードリスニング]]、[[熟議民主主義]]、[[ブロードリスニング本]]、[[sources/broad-listening-book-manuscript|ブロードリスニング本 原稿]]、[[events/2026-01-10-deliberation-workshop|熟議民主主義プロセス ワークショップ]] から導線を追加

## [2026-06-30] events | 広島県 広聴AI活用事例を追加

- 追加: [[events/2025-08-hiroshima-kouchou-ai|広島県 広聴AI活用事例（2025年8月）]]
- 目的: [[広聴AI]]の自治体活用を、単なる「導入事例」ではなく、[[ブロードリスニング]]の収集設計・プロンプト調整・庁内政策議論への接続という学びから辿れるようにする
- 根拠: `raw/broad-listening-book/08_02_広島県の事例.md`、`raw/broad-listening-book/08_地方自治体での活用.md`、`raw/history/week24_20250827/slack.md`、`raw/history/week25_20250903/slack.md`
- 更新: [[index]]、[[overview]]、[[広聴AI]]、[[ブロードリスニング]]、[[ブロードリスニング本]]、[[時系列まとめ]]、[[初年度まとめ]]、関連ソースページから導線を追加

## [2026-06-30] maintenance | 古い予定表現の点検と日付つき表現への補正

- 対象: [[熟議民主主義]]、[[コアループ]]、[[ブロードリスニング本]]、[[events/2025-11-29-code-for-japan-summit|Code for Japan Summit 2025 登壇]]、[[events/2026-04-18-coreloop-workshop|コアループ ワークショップ（2026-04-18）]]
- `予定`、`現在`、`進行中`、`調整中` などの時間依存表現を検索し、根拠があるものは日付つきの記録へ補正
- `slack-logs` mirror でブロードリスニング本の予約・発売確定とコアループ提言完了を再検索したが、今回参照した範囲では確定情報を確認できなかったため、未確認注記は維持

## [2026-06-30] events | Code for Japan Summit 2025登壇をイベント化

- 追加: [[events/2025-11-29-code-for-japan-summit|Code for Japan Summit 2025 登壇]]
- 目的: [[広聴AI]]と[[ブロードリスニング]]の外部発表を、書籍化・社会実装・インサイト分類の文脈から辿れるようにする
- 根拠: `raw/history/week35_20251112/slack.md`、`raw/history/week36_20251119/slack.md`、`raw/history/week37_20251126/slack.md`、`raw/history/week38_20251203/slack.md`、`raw/minutes/weekly-general-meeting.txt`、`raw/minutes/broad-listening-book-meeting.txt`
- 更新: [[index]]、[[overview]]、[[時系列まとめ]]、[[初年度まとめ]]、[[広聴AI]]、[[ブロードリスニング]]、[[ブロードリスニング本]]、関連ソースページから導線を追加

## [2026-06-30] events | 広聴AI読書会vol.1をイベント化

- 追加: [[events/2025-06-12-kouchou-ai-reading-vol-1|広聴AI読書会vol.1]]
- 目的: 開発・Meetupだけでなく、Pluralityやブロードリスニングの理論を学ぶ入口も時系列から辿れるようにする
- 根拠: `raw/history/week14_20250618/slack.md`、`raw/history/week16_20250702/slack.md`、`oss_weekly_reporter/data/2025-06-04_to_2025-06-11/raw/slack/7_広聴ai読書会.json`、`oss_weekly_reporter/data/2025-06-11_to_2025-06-18/raw/slack/7_広聴ai読書会.json`
- 更新: [[index]]、[[overview]]、[[時系列まとめ]]、[[初年度まとめ]]、[[広聴AI]]、[[ブロードリスニング]]、[[熟議民主主義]]、[[sources/weekly-history-reports|週次Historyレポート]] から導線を追加

## [2026-06-30] events | ウェルカムミート#2をイベント化

- 追加: [[events/2025-06-21-welcome-meet-2|ウェルカムミート#2]]
- 目的: 初見者の参加導線として重要なオンボーディングイベントを、[[コミュニティ運営]]と時系列から辿れるようにする
- 根拠: `raw/history/week14_20250618/slack.md`、`raw/history/week15_20250625/slack.md`、`raw/minutes/weekly-general-meeting.txt`
- 更新: [[index]]、[[overview]]、[[時系列まとめ]]、[[初年度まとめ]]、[[コミュニティ運営]]、[[広聴AI]]、関連ソースページからイベントページへの導線を追加

## [2026-06-30] events | MEETUP #2をイベント化

- 追加: [[events/2025-05-25-meetup-2|デジタル民主主義2030 MEETUP #2]]
- 目的: 4月の1Day Meetupと7月のMEETUP #3の間にある、5月のアンカンファレンス形式ミートアップを初見者が辿れるようにする
- 根拠: `raw/history/week10_20250521/slack.md`、`raw/history/week11_20250528/slack.md`、`raw/minutes/weekly-general-meeting.txt`、`raw/minutes/broad-listening-book-meeting.txt`、`raw/minutes/polimoney.txt`、`raw/minutes/idobata-project.txt`
- 更新: [[index]]、[[overview]]、[[時系列まとめ]]、[[初年度まとめ]]、[[コミュニティ運営]]、[[広聴AI]]、[[いどばた]]、[[Polimoney]]、関連ソースページからイベントページへの導線を追加

## [2026-06-30] sources | ソースカタログを追加

- 追加: [[sources/index|ソースカタログ]]
- 目的: `wiki/sources/` が12ページまで増えたため、議事録・History・書籍原稿・個別ドキュメント・外部アーカイブを用途別に辿れる入口を作る
- 更新: [[index]]、[[overview]]、[[時系列まとめ]]、[[初年度まとめ]]、[[Slackログアーカイブ]]、各ソース要約ページからカタログへの導線を追加

## [2026-06-30] events | コアループ4/18ワークショップをイベント化

- 追加: [[events/2026-04-18-coreloop-workshop|コアループ ワークショップ（2026-04-18）]]
- 目的: 6月熟議に向けた中間検証イベントを、[[コアループ]]の時系列から根拠付きで辿れるようにする
- 根拠: `raw/minutes/project-coreloop.txt`、`raw/minutes/weekly-general-meeting.txt`、`digitaldemocracy2030/slack-logs/raw/slack/C0A3ZG16TEY/2026-04.jsonl.gz`
- 更新: [[コアループ]]の4/25・5/16を実施済み断定から「当初計画・未確認」に補正。[[時系列まとめ]]、[[熟議民主主義]]、関連イベント、関連ソースページから導線を追加

## [2026-06-30] events | MEETUP #3をイベント化

- 追加: [[events/2025-07-18-meetup-3|デジタル民主主義2030 MEETUP #3]]
- 目的: 2025年7月のコミュニティイベントを、[[コミュニティ運営]]と各プロダクトの接点として辿れるようにする
- 根拠: `raw/history/week18_20250716/slack.md`、`raw/minutes/community-operations.txt`、`raw/minutes/weekly-general-meeting.txt`、`raw/minutes/broad-listening-book-meeting.txt`
- 更新: [[時系列まとめ]]、[[初年度まとめ]]、[[コミュニティ運営]]、[[広聴AI]]、[[いどばた]]、[[Polimoney]]、関連ソースページからイベントページへの導線を追加

## [2026-06-30] events | Meetupと熟議ワークショップをイベント化

- 追加:
  - [[events/2025-04-12-1day-meetup|1Day Meetup（2025-04-12）]]
  - [[events/2026-01-10-deliberation-workshop|熟議民主主義プロセス ワークショップ（2026-01-10）]]
- 目的: PLANに残っていたMeetup/ワークショップ系の未整理イベントから、根拠が明確で初見者の文脈理解に効く2件を `wiki/events/` に追加
- 根拠: `raw/history/week4_20250409/slack.md`、`raw/history/week5_20250416/slack.md`、`raw/history/week43_20260114/slack.md`、`raw/minutes/project-coreloop.txt`、`raw/minutes/weekly-general-meeting.txt`
- 注意: 2026-01-10ワークショップはソース間でテーマ名に揺れがあるため、ページ本文では「AI支援の熟議運用を試した内部実験」として扱い、断定を避けた
- 更新: [[overview]]、[[時系列まとめ]]、[[初年度まとめ]]、[[コミュニティ運営]]、[[コアループ]]、主要プロダクト、関連ソースページからイベントページへの導線を追加

## [2026-06-30] events | コアループの主要イベントページを追加

- 追加:
  - [[events/2026-03-19-stop-fraud-ads-press-conference|ストップ詐欺広告 記者会見]]
  - [[events/2026-06-21-coreloop-online-deliberation|コアループ オンライン熟議（2026-06-21）]]
- 目的: `wiki/events/` が空だったため、初見者が[[コアループ]]の公開化と熟議実施の節目を個別イベントとして辿れるようにする
- 根拠: `raw/minutes/project-coreloop.txt`、`raw/minutes/weekly-general-meeting.txt`、`digitaldemocracy2030/slack-logs/mirror/slack/C0BACQUGQ5R.jsonl.gz`
- 更新: [[overview]]、[[時系列まとめ]]、[[初年度まとめ]]、[[コアループ]]、[[ストップ詐欺広告]]、[[熟議民主主義]]、[[KYA]]、関連ソースページからイベントページへの導線を追加

## [2026-06-30] docs | Slackチャットログ参照先を slack-logs に更新

- 元情報: nishio からの共有「新しいチャットログ置き場は `digitaldemocracy2030/slack-logs`」
- 方針: Slack のチャットログ本体は `digitaldemocracy2030/slack-logs` を正とし、`nishio/oss_weekly_reporter` は週次AIレポートと GitHub Issues/PR の補助アーカイブとして残す
- 更新:
  - `archive_index.md` — Slackログ本体、週次AI/GitHub補助アーカイブ、読む順序、引用ルールを分離して記述
  - `scripts/search-archive.py` — `slack-logs` の `mirror/` と `raw/` の `.jsonl.gz` 検索をデフォルトにし、`--source oss-weekly-reporter` で旧週次アーカイブ検索も継続。`--channel` はチャンネルIDだけでなくチャンネル名の一部でも絞れるように更新
  - `CLAUDE.md` / `AGENTS.md` / `wiki/index.md` — 外部アーカイブ参照先と検索例を更新
  - `wiki/topics/slack-log-archive.md` — wiki 内の読み方ページを新規作成
  - `wiki/topics/ai-slack-access-patterns.md` / `wiki/topics/archive-pipeline-design.md` / `wiki/entities/oss-weekly-reporter.md` — `slack-logs` 実装後の現在状態（raw + mirror 二層、2026-06-30 mirror 同期確認）を冒頭に追記
  - `wiki/entities/coreloop.md` / `wiki/overview.md` / `wiki/timeline/quarterly-summary.md` / `wiki/entities/broad-listening-book.md` — 2026年6月末時点で過去日付になった「予定」表現を、未確認の結果と混同しないよう「2026年4月時点の計画」と明記
  - `wiki/entities/broad-listening-book.md` / `wiki/concepts/broad-listening.md` — `slack-logs` mirror の `2_broad-listening-book` から 2026-06-21 の `PDF Build 20260621` を確認し、書籍規模を379,104字、6月時点でも校正コメント対応とPDFビルドが継続している状態に更新
  - `wiki/entities/coreloop.md` / `wiki/overview.md` / `wiki/timeline/quarterly-summary.md` — `slack-logs` mirror の `delib-20260621-japan` から、2026-06-21 にオンライン熟議本番が Stanford Deliberate platform 上で運用されたことを確認。6/14は当初予定、6/30提言提出は完了未確認として整理
  - `wiki/entities/stop-fraud-ads.md` — [[コアループ]] の Reference Product である「ストップ詐欺広告」を独立ページ化。市民通報、可視化、熟議の材料化、政策実装の参照という位置づけを整理
  - `wiki/concepts/kya.md` — オンライン詐欺広告対策の主要論点である KYA（Know Your Advertiser / 広告主本人確認）を用語ページ化

## [2026-06-30] sources | 議事録6本のソース要約ページを追加

- 目的: `wiki/sources/` が未整備だったため、主要議事録を初見でも読める入口にする
- 追加:
  - [[sources/weekly-general-meeting|週次全体定例 議事録]]
  - [[sources/community-operations-minutes|コミュニティ運営 議事録]]
  - [[sources/broad-listening-book-meeting|ブロードリスニング本 執筆定例 議事録]]
  - [[sources/project-coreloop-minutes|Project Coreloop 議事録]]
  - [[sources/polimoney-minutes|Polimoney 議事録]]
  - [[sources/idobata-project-minutes|いどばた プロジェクト議事録]]
- 更新: `wiki/index.md` の議事録一覧から各ソース要約ページへリンク

## [2026-06-30] sources | raw/history の週次レポート入口を追加

- 追加: [[sources/weekly-history-reports|週次Historyレポート]]
- 対象: `raw/history/` の week1（2025-03-19）〜week50（2026-04-15）、50週・218 Markdown
- 目的: dd2030.org の History 表示に使う週次レポート群について、収録範囲・ファイル種別・読み方・限界を初見で分かるようにする
- 更新: `wiki/index.md` の週次レポート欄、[[時系列まとめ]]、[[初年度まとめ]]、[[OSS Weekly Reporter]]、[[Slackログアーカイブ]] から導線を追加

## [2026-06-30] sources | ブロードリスニング本原稿の入口を追加

- 追加: [[sources/broad-listening-book-manuscript|ブロードリスニング本 原稿]]
- 対象: `raw/broad-listening-book/` の章本文・推薦文・付録など43 Markdown、コラム10 Markdown、コラム画像7ファイル
- 目的: 書籍原稿群を、出版進行ではなく「概念・事例・技術解説の一次ソース」として読めるようにする
- 更新: `wiki/index.md` のブロードリスニング本欄、[[ブロードリスニング本]]、[[ブロードリスニング]]、[[広聴AI]]、[[overview]]、[[sources/broad-listening-book-meeting|ブロードリスニング本 執筆定例 議事録]] から導線を追加

## [2026-06-30] sources | 個別ドキュメント・Slackメモのソース要約を追加

- 追加:
  - [[sources/legal-entity-name-announcement|法人名称決定アナウンス]]
  - [[sources/oss-foundation-survey|OSS財団事例サーベイ]]
  - [[sources/archive-pipeline-design-note|アーカイブパイプライン設計メモ]]
  - [[sources/oss-weekly-reporter-handoff|OSS Weekly Reporter 移管Slackメモ]]
- 目的: `raw/documents/` と `raw/slack/` にある個別ソースを、既存の解説ページから根拠として辿れるようにする
- 更新: `wiki/index.md` に個別ドキュメント・Slackメモ欄を追加し、関連する法人・アーカイブ系ページから導線を追加

## [2026-04-18] init | Wiki構造の初期化

- ディレクトリ構成を作成（raw/, wiki/, content/, scripts/）
- CLAUDE.md（スキーマ）を作成
- index.md, overview.md, log.md を作成
- Quartz公開用の設定ファイルを準備

## [2026-04-18] ingest | website歴史データ50週分の取り込み

- digitaldemocracy2030/website の src/history/ から50週分のデータを取得
- raw/history/ に配置（218ファイル）
- 以下のWikiページを生成:
  - overview.md — プロジェクト全体の概要
  - entities/kouchou-ai.md — 広聴AI
  - entities/idobata.md — いどばた
  - entities/polimoney.md — Polimoney
  - entities/coreloop.md — コアループ
  - entities/broad-listening-book.md — ブロードリスニング本
  - concepts/broad-listening.md — ブロードリスニング
  - concepts/deliberative-democracy.md — 熟議民主主義
  - timeline/quarterly-summary.md — 時系列まとめ（四半期）
- index.md を更新

## [2026-04-18] deploy | GitHub Pages公開

- GitHubリポジトリ nishio/dd2030-wiki を作成
- Quartzフレームワークを導入（テンプレートからコピー）
- GitHub Actionsワークフロー（deploy.yml）を設定
- GitHub Pagesを有効化、自動デプロイ成功
- 公開URL: https://nishio.github.io/dd2030-wiki/

## [2026-04-18] fix | Wikilinkの解決方法を仕組み化

- 問題: `[[広聴AI]]` のような日本語wikilinkがQuartzのファイル名解決で404になる
- aliasesフロントマターで対応→baseUrl欠落の問題が残る
- 解決策: scripts/resolve-links.py を作成
  - wiki/のシンプルな`[[ページ名]]`をtitle/aliasesからファイルパスに自動解決
  - content/に出力、ビルド時にリンク検証
  - GitHub Actionsにも組み込み
- wiki/では`[[ページ名]]`と書くだけでOKに

## [2026-04-18] ingest | Google Docs議事録4件の取り込み

- 取得した議事録:
  - weekly-general-meeting.txt（全体定例、3,500行）
  - community-operations.txt（コミュニティ運営、1,100行）
  - broad-listening-book-meeting.txt（BL本執筆定例、6,800行）
  - project-coreloop.txt（コアループ企画書・議事録、6,500行）
- Wikiの大幅更新:
  - coreloop.md — チーム構成5チーム、DP設計、台湾視察、自民党PTとの関係
  - broad-listening-book.md — 全章構成・執筆者・スケジュール
  - 新規: topics/community-operations.md（メンバー数推移、オンボーディング課題）
  - 新規: topics/key-people.md（30名以上のキーパーソンと役割）

## [2026-04-18] ingest | Polimoney・いどばた議事録の取り込み

- 取得した議事録:
  - polimoney.txt（5,000行）
  - idobata-project.txt（2,700行）
- Wikiの更新:
  - polimoney.md — 3ペルソナ戦略、Ledger/SaaS化、ロードマップ6ステップ、チームみらい棲み分け
  - idobata.md — サブプロダクト構成、参院選8,559件PR・254件採用、サイボウズ実験、2プロジェクト体制

## [2026-04-18] ingest | ブロードリスニング本リポジトリの取り込み

- digitaldemocracy2030/broad-listening-book から55ファイルを取得
- raw/broad-listening-book/ に配置
- Wikiの更新:
  - overview.md — 設立日（2025年1月）、共同創設者（安野＋鈴木健）、開発統計（2,756コミット、807PR、Devin 7.6%）
  - 各ページの精度向上（日付・数値の確認）

## [2026-04-18] docs | ソース更新手順の文書化

- CLAUDE.mdに全ソースのGoogle Doc ID・curlコマンド・更新頻度を記載
- READMEに「ソースの更新」セクションを追加
- README全体を整備（Fork手順、ローカル確認、GitHub Pages設定）

## [2026-04-18] enhance | 「もっと詳しく」セクションの追加

- 全Wikiページに一次ソースへのリンクを追加:
  - Google Docs議事録、GitHubリポジトリ、公開サイト、発表スライド、書籍原稿の該当章

## [2026-06-03] ingest | 法人名称決定アナウンス（2026-06-01）の取り込み

- 取り込み元: 鈴木健による6/1 Slackアナウンス「法人名称が決定しました」
- raw/documents/2026-06-01_legal-entity-name-announcement.md として保存
- 新規ページ: entities/legal-entity.md（デジタル民主主義推進機構 / Digital Democracy Builders）
  - ボード（鈴木・中室・関）の協議で決定
  - ドメイン: digitaldemocracy.jp
  - 候補比較（ジャパン／実装ハブ／2030）と見送り理由を整理
  - 「2030」はフラッグシップ・プログラム名として継続
- 更新:
  - overview.md — プロジェクトの歩みに 2026-06-01 を追加、組織・コミュニティ節に法人情報を追記
  - index.md — 「組織」セクションを新設し、法人ページへリンク

## [2026-06-10] decision | slack-logs リポのライセンス確定（データ CC BY 4.0 / コード MIT）

- 元情報: nishio との対話「CC-BYは確定 / ログはCC-BY、コードはMIT」
- 確定事項:
  - **データ** (`raw/`, `mirror/`, `state/`) → CC BY 4.0
  - **コード** (`scripts/`, `.github/workflows/`, ドキュメント) → MIT
- 実装: slack-logs リポに `LICENSE` (MIT) と `LICENSE-DATA` (CC BY 4.0 公式 legalcode) を追加、README の「ライセンス」節を更新、移行ロードマップ表のフェーズ4 (ライセンス確定) を完了に
- 関連: [[OSS Weekly Reporter]] のフェーズ2残作業から CC-BY 項目が消える（残りは脱-nishio token と過去ログ 67週分の再公開経路）

## [2026-06-09] feature | slack-logs に mirror layer を追加（案2 実装）

- 元情報: [[AI から Slack ログを参照するパターン]] の採用方針「案2: 現状ミラー workflow 追加」
- 実装:
  - `scripts/slack_mirror.py` — Python + slack_sdk、直近14日分の public ch メッセージ＋スレッドを取得
  - `.github/workflows/slack-mirror.yml` — 6時間ごと cron、429 retry、push race 対策、失敗時 issue 起票
  - 出力: `mirror/slack/<channel_id>.jsonl.gz` を毎回上書き、`mirror/sync.json` に最終同期メタ、`mirror/users.json`
- 動作確認: run [27214269117](https://github.com/digitaldemocracy2030/slack-logs/actions/runs/27214269117) で success（57 channels, 556 messages, window 2026-05-26〜2026-06-09）
- 初回 run は `cache: pip` が requirements.txt を要求して失敗 → da1f293 で削除して再試行成功（issue #3 を close）
- これで slack-logs は raw/ (月次 canonical, 2ヶ月遅延) と mirror/ (rolling 14日 snapshot, 6時間ごと) の二層構成に
- AI の現状クエリは `gh api repos/digitaldemocracy2030/slack-logs/contents/mirror/...` で参照可能

## [2026-06-09] explainer | AI から Slack ログを参照するパターンの整理

- 元情報: nishio との対話「AIが最新のSlackログを読みたいシチュエーションに関して考えて」
- 整理結果: AI の Slack 参照は (A) 歴史的問い合わせ と (B) 現状クエリ の2タイプで、要求される鮮度・スレッド完全性が異なる。slack-logs の月次+2ヶ月遅延設計はタイプ A 専用
- 解決策3案を提示: (1) 既存併用、(2) slack-logs に mirror ワークフロー追加、(3) AI が直接 Slack API を叩く tool
- 採用方針: 案1 → 案2 → 案3 の順で積む。**今回は案2に着手**
- 新規ページ: wiki/topics/ai-slack-access-patterns.md
- 更新: wiki/index.md「テーマ」に追加

## [2026-06-09] bootstrap | digitaldemocracy2030/slack-logs を立ち上げ + 過去16ヶ月分埋め戻し完了

- bootstrap commit: `digitaldemocracy2030/slack-logs` 33dfe5a（README + slack-backup.yml workflow + ディレクトリ枠）
- SLACK_TOKEN: nishio が `nishio/oss_weekly_reporter` で使っている既存 bot token を流用（案C: ハイブリッドで「まず動かす」フェーズ）
- 動作テスト (2026-04): run [27199100824](https://github.com/digitaldemocracy2030/slack-logs/actions/runs/27199100824) で成功。58 public ch、gzip後 ~250KB/月
- 過去分埋め戻し: **2025-01〜2026-04 の 16ヶ月分すべて success**（2026-05 は cron が 7/1 に拾う）
- repo サイズ: 773 KB（推奨 1GB に対し余裕）
- 途中で発生した2つのバグを修正:
  1. **`concurrency: cancel-in-progress: false` でも中間 pending は cancel される** → 並列 dispatch は不可。`/tmp/backfill-sequential.sh` で sequential 実行する形に変更
  2. **`git push` race condition**: 連続実行で2つ目以降が `[rejected]` → workflow の commit step に `git pull --rebase` retry ループを追加（commit 39a299e）
- 残課題: 案C の後半（脱-nishio token 化）、CC-BY ライセンス化決定、Discord 移行後の対応

## [2026-06-09] decision | slack-logs 保全パイプライン方針確定 + slack-logger-cli-action paper exercise

- 元情報: nishio との対話（B. data repo の場所決定 + C. paper exercise 依頼）
- 確定事項:
  - **保全 data repo = `digitaldemocracy2030/slack-logs`**（dd2030-wiki は report システムなので生ログ保管先に向かない）
  - **collector = `kuboon/slack-logger-cli-action` を fork なし `uses:` 導入**
  - **保全（月次 slack-logs）と週次レポート生成（`nishio/oss_weekly_reporter`）は当面分離して併走**
- paper exercise 結果（[[アーカイブパイプライン設計]] に追記）:
  - そのまま `uses:` で動く部分（案A適合、autoJoin、スレッド取得、過去分埋め戻し、60日inactivity対策）
  - workflow 側で足す部分（rename `<channel_id>/<YYYY>-<MM>.jsonl` + gzip + users.list snapshot + 失敗通知）
  - 要確認: dd2030 Slack bot が internal customer-built として登録されているか（2025-05-29 rate limit の前提）
- 更新:
  - wiki/topics/archive-pipeline-design.md — 「方針確定」「paper exercise」「残った宿題」節を追加
  - wiki/entities/oss-weekly-reporter.md — 「方針確定 — 2026-06-09 nishio との対話で」節を追加（dd2030-wiki吸収案の撤回を明記）

## [2026-06-09] promote | アーカイブパイプライン設計メモをトピックに昇格 + raw/b.txt を rename

- 元情報: nishio が並行整理していたアーキ設計メモ（code repo / data repo 分離、Slack/Scrapbox API 制約、JSONL gz、commit 戦略、失敗モード）
- 仮の名前 `raw/b.txt` を `raw/documents/2026-06-09_archive-pipeline-design-note.md` に rename
- CLAUDE.md「rawディレクトリの規約」に「仮の名前で置かれたファイルは内容を読んだら `git mv` で `YYYY-MM-DD_概要.md` にrenameする」というルールを追加
- 新規ページ: wiki/topics/archive-pipeline-design.md
  - 設計メモ本体を整理・節立て直し
  - 末尾に「dd2030 文脈での当てはめ」表を追加（nishio個人repo / website weekly-summary.yml / 空の slack-logs / kuboon の slack-logger-cli-action / dd2030-wiki 吸収案 を案A/案B のどちらに対応するか）
  - 「未決事項」として data repo の所在、public/private、collector code 配置、過去ログ移送経路を列挙
- 更新: wiki/index.md「テーマ」に新ページを追加
- 更新: entities/oss-weekly-reporter.md「Slack上のやりとり」末尾から新ページへリンク

## [2026-06-09] ingest | OSS Weekly Reporter 移管 Slack やりとり（2026-06-04）の取り込み

- 元情報: ユーザー貼り付けの Slack 抜粋（nishio 23:43 + kuboon 13:01 返信 + nishio 6/4 23:46）
- raw/slack/2026-06-04_oss-weekly-reporter-handoff.md として保存（raw/slack/ 初の保存物）
- 新規に判明した3点を entities/oss-weekly-reporter.md「## Slack上のやりとり — 2026-06-04 nishio ↔ kuboon」セクションに追記:
  1. `digitaldemocracy2030/slack-logs` が空のままなのは「kuboon が Moai からの招待を expire させた」ため
  2. kuboon が `slack-logger-cli-action` を実装基盤候補として提示（Issue #177 の gsheet-slack-logger ベース案とは別系統）
  3. nishio が「dd2030-wiki に吸収」という第三の選択肢に傾いている — Issue #170/#177 の前提が変わりうる
- 関連: raw/documents/2026-06-09_archive-pipeline-design-note.md（nishio が並行整理中のデータ蓄積アーキ設計メモ。当時は仮名 `raw/b.txt`、後に rename）への参照を本文末に添えた

## [2026-06-09] filing-back | OSS Weekly Reporter 保全状況の再確認（変化なし）

- 問い: 「6/4 の調査から5日経った今、何か動いたか」
- 確認対象: `nishio/oss_weekly_reporter` data ブランチ最新コミット、PR digitaldemocracy2030/website#211、Issue #170/#173/#177、`digitaldemocracy2030/slack-logs` リポ
- 結論: **実質的な動きなし**。
  - data ブランチは cron 稼働中（最新 `2ee810e` 2026-06-03、次回 6/10 水）
  - PR #211 は OPEN のまま CI 上書き push のみ
  - Issue #170 は依然コメントゼロ（9ヶ月＋）、#173/#177 も未着手
  - `slack-logs` リポは 0 コミットのまま
  - 2026-05-13 nishio 提案の CC-BY化＋公式サイトリンクも形跡なし
- 副次的な発見: **Issue [digitaldemocracy2030/website#216](https://github.com/digitaldemocracy2030/website/issues/216)**（2026-05-29、shingo-ohki）「Slackに投稿された事例をもとにウェブサイト更新PRを作成する」が新規起票されている。`#1_事例紹介_全体` 投稿を AI で website PR 化する提案で、週次サマリパイプラインの代替ではないが「Slack→AI→PR」パターンの隣接フロー
- 更新: entities/oss-weekly-reporter.md に「## 状況確認 — 2026-06-09時点」サブセクションを追加し、5日間の差分テーブルと #216 を記録

## [2026-06-04 21:52] filing-back | OSS Weekly Reporter 移管状況の調査結果を反映

- 問い: 「OSS Weekly Reporter のパイプラインは結局 nishio 個人で動いているのか、dd2030 で動いているのか／移管はされたのか」
- 調査範囲: `nishio/oss_weekly_reporter` の main / data ブランチ、`digitaldemocracy2030/website` Issue #170、`digitaldemocracy2030/slack-logs` リポ、oss_weekly_reporter data ブランチ上の 2025-09 〜 2026-06 の週次 Slack 要約
- 結論: **未移管**。Slack取得・AI要約は今も nishio 個人リポで自動実行中。website への反映だけが2025-09に部分移管され、Issue #170 は9ヶ月OPEN放置。2026-05以降は「Slack→Discord 移行」「過去ログ CC-BY 公開」という別フレームに連結された
- 更新: entities/oss-weekly-reporter.md に「## 運用状況（2026-06-04時点）」セクションを追加
  - 移管の経緯（〜2025-08、2025-09-03、2025-09-10、2026-06-04現在）
  - 部品別の移管状況テーブル（Slack取得 / AI要約 / dd2030.org/history 反映）
  - 2026-05 のスコープ拡張（Discord 移行案、`digitaldemocracy2030/slack-logs` の5/19作成、CC-BY化提案）
  - 未解決の宿題リスト
- 一次出典:
  - oss_weekly_reporter `data/2026-05-06_to_2026-05-13/markdown/slack/all_summary.md` — nishio による CC-BY 化提案
  - oss_weekly_reporter `data/2026-05-20_to_2026-05-27/markdown/slack/all_summary.md` — Slack→Discord 移行案アナウンス
  - GitHub Issue digitaldemocracy2030/website#170 本文（kuboon・Shingo OHKI・nishio のスレッド引用込み）

## [2026-06-03] explainer | コミュニティと法人の関係 解説ページ作成

- 元情報: raw/documents/2026-06-03_oss-foundation-survey.md（OSS財団事例のリサーチと、コミュニティ／法人の並走関係についての対話）
- 方針: 設計提案ではなく、「コミュニティと法人が並走する」状況の解説に絞る（元の対話で明示された要望）
- 新規ページ: topics/community-and-legal-entity.md
  - 役割の違い（コミュニティ vs 法人）
  - OSS事例（Apache / Linux Foundation / Mozilla / Ethereum / OpenStreetMap / Decidim）の役割分担パターン
  - 「法人は代表者ではなく責任の受け皿」「コミュニティは法人の部門ではない」の整理
  - 政治的中立性の三層（党派中立／手続き中立／個人の自由）
- index.md — 「組織」「テーマ」セクションに新ページへのリンクを追加
## [2026-06-30] guide | 初見者向け読む順序ガイドを追加

- 新規ページ: [[topics/first-reader-guide|初めて読む人へ]]
  - 10分で全体像を知る導線（[[overview]] → [[index]]）
  - 30分で時系列を追う導線（[[時系列まとめ]] → [[初年度まとめ]]）
  - 根拠確認の導線（[[sources/index|ソースカタログ]] → [[Slackログアーカイブ]]）
  - コミュニティ、法人、アーカイブ設計、AIによるSlack参照の関心別入口
- 更新: `wiki/index.md`, `wiki/overview.md`, `wiki/sources/index.md`, `wiki/timeline/quarterly-summary.md`, `wiki/timeline/first-year.md` などから新ガイドへリンク
- `digitaldemocracy2030/slack-logs` をSlackチャットログ本体の正置き場として読む注意も、新ガイドに明記

## [2026-06-30] file back | Wiki保守運用のチェックポイントを追加

- 元情報: 「全体を見てやるべきこと」の優先1として、広いWiki改善差分を先に安定化し、`codex/stabilize-wiki-improvements` で検証・commit・draft PR化した作業
- 新規ページ: [[Wiki保守運用]]
- 保存した知見:
  - 大きなWiki改善後は、次の取り込みに進む前にブランチ化、検証、コミットまたはPR化して差分を安定させる
  - `.claude/settings.local.json` はローカル設定で token らしき値を含み得るため staging しない
  - `git add -A` ではなく、今回触ったパスだけを明示して stage する
- 更新: `wiki/index.md`, `AGENTS.md`, `CLAUDE.md`
