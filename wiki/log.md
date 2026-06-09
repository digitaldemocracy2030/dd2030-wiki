---
title: Wiki作業ログ
tags: [dd2030, log]
created: 2026-04-18
updated: 2026-06-09 (slack-logs 方針確定)
---

# Wiki 作業ログ

取り込み・更新・メンテナンスの記録。

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
