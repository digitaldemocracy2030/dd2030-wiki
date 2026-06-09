---
title: OSS Weekly Reporter
aliases: [OSS Weekly Reporter, oss_weekly_reporter, 週次レポーター]
tags: [dd2030, project, tooling, archive]
sources:
  - oss_weekly_reporter/README.md
  - oss_weekly_reporter/data/2025-04-02_to_2025-04-09/raw/slack/2_新しいプロジェクトの種.json
  - raw/slack/2026-06-04_oss-weekly-reporter-handoff.md
created: 2026-05-11
updated: 2026-06-09
---

# OSS Weekly Reporter

## 概要

**OSS Weekly Reporter** は、OSSプロジェクトの週次活動報告を省力化するための西尾製ツール。Slack ログと GitHub の Issue/PR を抽出し、LLM に渡す Markdown 形式に変換して、「今週何が起きたか」のレポートを半自動で生成する。

リポジトリ: [`nishio/oss_weekly_reporter`](https://github.com/nishio/oss_weekly_reporter)

dd2030 においては、これが**[[初年度まとめ|過去1年間のSlackログとGitHub活動データの一次アーカイブ]]**になっており、[[overview|dd2030 wiki]] 自体の基盤データ源として機能している。詳細な参照手順は [archive_index.md](https://github.com/nishio/dd2030-wiki/blob/main/archive_index.md) を参照。

## 由来 — `2_新しいプロジェクトの種` から生まれた

2025年4月初旬、`2_新しいプロジェクトの種` チャンネルで生まれたプロジェクト。前身は kuboon 氏の [`gsheet-slack-logger`](https://github.com/kuboon/gsheet-slack-logger)（Slack ログを Google Spreadsheet に保存する Bot）。

西尾の整理（出典: `oss_weekly_reporter/data/2025-04-02_to_2025-04-09/raw/slack/2_新しいプロジェクトの種.json`）:

> オリジナルの実装は「Slackからの抽出」と「Google Spreadsheetへのアップロード」がセットになっていた。これはログを保存するという目的には合理的。… 毎週の更新レポートをLLMで作りたいという目的に使おうと思った時、Google Spreadsheetを経由するのは無駄に複雑では？となった。それはそう、目的が変わったから適切な構成も変わる。

すなわち、**「ログ保全」と「週次レポート生成」を分離**し、後者を `oss_weekly_reporter` として切り出した。kuboon オリジナルは月次バッチでログ保存を継続、こちらは週次でレポート生成と JSON アーカイブを担当する、という分業構造になっている。

## 構成

```
Slack API → slack_to_json.py → raw/slack/<channel>.json
GitHub API → github_report.py → raw/github/<repo>.json
              ↓
         json_to_markdown.py → markdown/
              ↓
         call_openai_api.py（LLM） → ai_reports/
```

主要スクリプト:

| スクリプト | 役割 |
|------------|------|
| `slack_to_json.py` | チャンネルごとに JSON で抽出。日付範囲フォルダを作成 |
| `github_report.py` | リポジトリの Issue/PR を JSON 抽出（オプションで Markdown も） |
| `json_to_markdown.py` | LLM 入力用の Markdown に変換 |
| `call_openai_api.py` | OpenAI o1 を呼んで週次サマリを生成 |
| `json_to_gsheet.py` | （旧用途） Google Spreadsheet への保存 |

データは GitHub の `data` ブランチに `YYYY-MM-DD_to_YYYY-MM-DD/` 形式で push される。2026年5月時点で67週分・117MB。

## どのチャンネル・リポジトリを追跡しているか

`config.yaml` で設定する。**全公開チャンネルではなく、購読リスト方式**。

時期によって追跡対象が変わってきた経緯があり、初期のチャンネル（例: `2_学生のためのデジタル民主主義`）が後期には取得対象から外れていたり、後から追加されたチャンネル（例: `2_開発_cartographer` は2025-10から）があったりする。**67週通算で 80+ 個のチャンネル名が登場**するが、各週の取得対象は10〜20チャンネル程度。

追跡対象に入っていなかったチャンネルの議論は、このアーカイブには残らない。これは dd2030 wiki の構築上の重要な制約となる（→ [[初年度まとめ]] 末尾「含まれていない可能性があるもの」セクション）。

## dd2030 wiki におけるメタ循環構造

dd2030 wiki は次のような依存関係を持つ:

```
dd2030 Slack ──→ oss_weekly_reporter ──→ aiレポート/Markdown/生JSON
                                              ↓
                                         dd2030 wiki（このリポジトリ）
                                              ↑
                                        OSS Weekly Reporter の解説
                                        （このページ）
```

- アーカイブ自体は dd2030-wiki リポジトリには取り込まない（プライバシー・サイズ）
- 検索ベースで参照する（[scripts/search-archive.py](https://github.com/nishio/dd2030-wiki/blob/main/scripts/search-archive.py)）
- このアーカイブを生んだプロジェクト自体が dd2030 の中で `2_新しいプロジェクトの種` から立ち上がったもの

## 運用状況（2026-06-04時点）

**パイプラインは今も `nishio/oss_weekly_reporter` で毎週水曜JST 12:00に自動実行されている**（直近は2026-06-03週まで `data` ブランチ更新を確認）。dd2030 組織への完全移管は**未完了**。

### 移管の経緯

- **〜2025-08**: nishio個人のリポ・Slackトークン・OpenAIキーで週次CI実行。OpenAIキーの問題により2025年8月時点でAI要約生成が3週連続失敗（出典: 2_広報_pr スレッド 2025-08-21）
- **2025-09-03**: PR [digitaldemocracy2030/website#166](https://github.com/digitaldemocracy2030/website/pull/166)（Shingo OHKI）が merge され、`dd2030.org/history` 更新処理が website 側に移管。OpenAIキーは Shingo OHKI が広聴AIデモ用に発行した個人キーを流用
- **2025-09-10**: nishio が「dd2030側に移ったと思って `extract-logs.yml` を停止」→ Slack取得APIキーが未移管のため履歴更新が止まる → 手動再起動。同日 Issue [digitaldemocracy2030/website#170](https://github.com/digitaldemocracy2030/website/issues/170)「毎週のプロジェクトの活動状況の更新処理を移管する」が起票
- **2026-06-04現在**: Issue #170 は **OPEN のまま9ヶ月放置**。Slackログ取得・AI要約は引き続き nishio 個人リポで自動実行中

### 部品別の移管状況

| 部品 | 動作場所 | APIキー所有 | 状態 |
|---|---|---|---|
| Slackログ取得 (`extract-logs.yml`) | `nishio/oss_weekly_reporter` | nishio個人（Slack） | 未移管 |
| AI要約 (`weekly-report.yml`) | `nishio/oss_weekly_reporter` | nishio個人（OpenAI） | 未移管 |
| `dd2030.org/history` 反映 | `digitaldemocracy2030/website` | Shingo OHKI 発行キー | 部分移管済み（`nishio/oss_weekly_reporter` の `data` ブランチに依存） |

### 2026-05 のスコープ拡張

「dd2030側で動かす」という当初の論点は、2026-05以降に2つの大きな動きに連結された:

1. **Slack→Discord 移行案**（モアイ／小野、2026-05-23 #0_全体お知らせ にてアナウンス、フィードバック期間 〜5/30）  
   理由: Slack無料プランで過去メッセージが非表示化、有料プランは月額高額。  
   過去ログ受け皿として **`digitaldemocracy2030/slack-logs` リポが2026-05-19に作成**（2026-06-04時点で空、workflows 未設定）。FAQ: [dd2030.org/discord-migration/](https://dd2030.org/discord-migration/)

2. **過去ログのCC-BY公開化**（nishio提案、2026-05-13週の全体定例）  
   「OSS Weekly Reporter で初期から公開チャンネルログをGitHubに蓄積してきたことが、組織内で忘れられていた」と問題提起。「公式サイトから明示的にリンクし、CC-BYライセンスにしたい」「1週間の猶予期間後に着手」と発言（出典: 2026-05-06_to_2026-05-13 週 ai_reports/slack.md）

→ つまり、「nishio個人 → dd2030/website への移管」というフレームは、「Slack卒業＋過去ログを `digitaldemocracy2030/slack-logs` に CC-BY アーカイブ」という形に再構成されつつある。

### 未解決の宿題

- Issue #170 の処理方針（クローズするか／本気で移管するか）
- Slack API キーを dd2030 組織キーに置き換える経路（Slack 無料プランの「アプリ追加上限」が当時の障壁）
- `digitaldemocracy2030/slack-logs` の中身（2026-06-04 時点で空、後述）
- 2026-05-13 の nishio 提案「CC-BY化と公式サイトからのリンク貼り」の進捗（**slack-logs のライセンスは 2026-06-10 確定済**: データ CC BY 4.0 / コード MIT。公式サイトリンクは未）

## website 側の詰まりと slack-logs リポの実態（2026-06-04時点）

### `digitaldemocracy2030/website` weekly-summary.yml の動作

`digitaldemocracy2030/website/.github/workflows/weekly-summary.yml`（6.7KB）は毎週水曜 12:30 JST に cron 実行される。設計は:

```
nishio/oss_weekly_reporter の data ブランチを checkout
  → 最新の data ディレクトリを取得
  → week<N> ブランチを作って draft PR を起こす     ← 自動はここまで
  → 人が ready 化 → review → merge                ← 手動
  → dd2030.org/history に反映
```

つまり「PR を draft で作るところまで」だけ自動で、ready→merge は人手という前提。

### 詰まり: Week51 以降の PR が滞留中

直近の merged 履歴:

| Week | 期間 | merge日 | 担当 |
|---|---|---|---|
| Week47 | 2026-02-11週 | 2026-03-13 | shingo-ohki / shota_ono |
| Week48 | 2026-03-18週 | 2026-03-26 | 同上 |
| Week49 | 2026-03-25週 | 2026-04-01 | 同上 |
| Week50 | 2026-04-15週 | 2026-04-17 | 同上 |
| Week51〜 | 2026-04-22週〜 | **未merge** | — |

**PR [digitaldemocracy2030/website#211](https://github.com/digitaldemocracy2030/website/pull/211) "Week51 Summary Update" は 2026-04-22 に自動作成され、OPEN のまま**（updatedAt が 2026-06-03 になっているのは CI が毎週同ブランチに上書き push し続けているため）。**dd2030.org/history が Week50 で停止している直接の原因はこの PR キューの滞留**。

### 関連する OPEN な Issue

| Issue | 起票日 | 内容と現状 |
|---|---|---|
| [#173](https://github.com/digitaldemocracy2030/website/issues/173) 毎週のプロジェクトの活動状況の更新処理が適切に動いていない | 2025-11-15 | 「処理は毎週動いているが week27 と同じブランチに上書きされる」という既知バグ。**shingo-ohki と moai-redcap が「draft PR ではなく自動マージにしてしまう」で合意済み・未実装**。2025-11-19 に shingo-ohki が手動で過去分を最新まで追いつかせた、と報告 |
| [#177](https://github.com/digitaldemocracy2030/website/issues/177) 今後の「プロジェクトの歴史」の更新を可能な限り自動化する | 2025-11-16 | **kuboon が 2025-12-15 に脱nishio依存の設計を提示**: GitHub は public なので token 不要、Slack は `kuboon/gsheet-slack-logger` を改造して json 出力、OpenAI はプロンプト流用、というプラン。着手されていない |
| [#168](https://github.com/digitaldemocracy2030/website/issues/168) weekly-summary.yml のリファクタリング | 2025-09-03 | PR #166 マージ時のレビュー指摘の積み残し |
| [#170](https://github.com/digitaldemocracy2030/website/issues/170) 毎週のプロジェクトの活動状況の更新処理を移管する | 2025-09-10 | 前述。9ヶ月 OPEN |

### `digitaldemocracy2030/slack-logs` の実態

5/23 の Discord 移行アナウンスで「**すでに**専用リポジトリを作成し、過去ログを本格的に抽出してアーカイブとして保存する作業を**開始しています**」と書かれていたが、2026-06-04 時点の実態:

| 項目 | 値 |
|---|---|
| 作成日時 | 2026-05-19 01:42 UTC（JST 10:42） |
| description | なし |
| disk usage | **0 KB** |
| ブランチ | **0** |
| コミット | **0** |
| Issues / PRs | **0** |
| visibility | public |

→ **リポ枠の確保だけ**で、中身の作業は始まっていない。アナウンスは実態より先行している。

### 全体構造（2026-06-04時点）

```
nishio/oss_weekly_reporter（cron稼働中、6/3週まで）
        ↓ data ブランチ
digitaldemocracy2030/website weekly-summary.yml（cron稼働中）
        ↓ draft PR
   PR #211 (Week51) ←ここで詰まる、5週分滞留
        ↓（人がやらない）
   dd2030.org/history（Week50で表示停止）

digitaldemocracy2030/slack-logs ←空（0コミット、placeholder）
```

### 観察

- パイプライン自体は cron で生きているが、**「draft PR を人が ready→merge する」という人手プロセスのボトルネックで詰まっている**
- Issue #173 で「いっそ自動マージに」という結論はほぼ取れていた（shingo-ohki + moai-redcap）が、その後実装されていない
- Issue #177 で kuboon が完全な脱nishio依存設計を提案しているが、着手されていない
- 2026-05 以降の Discord 移行と CC-BY 化の動きが、これらの未解決 Issue 群の優先順位を曖昧にしている可能性

## 状況確認 — 2026-06-09時点

2026-06-04 のスナップショットから5日後の再点検。**実質的な動きはなし**。

| 項目 | 2026-06-04 → 2026-06-09 の変化 |
|---|---|
| `nishio/oss_weekly_reporter` data ブランチ | 稼働継続。最新コミット `2ee810e` 2026-06-03（次は 6/10 水のcron） |
| PR [#211](https://github.com/digitaldemocracy2030/website/pull/211) Week51 | OPEN のまま、CI上書き push のみ（merge されず、5週分滞留継続） |
| Issue [#170](https://github.com/digitaldemocracy2030/website/issues/170) 移管 | OPEN・コメントゼロ。2025-09-10 以降動きなし（9ヶ月＋） |
| Issue [#173](https://github.com/digitaldemocracy2030/website/issues/173) 自動マージ化 | 未着手 |
| Issue [#177](https://github.com/digitaldemocracy2030/website/issues/177) kuboon設計 | 未着手 |
| `digitaldemocracy2030/slack-logs` | 0 コミットの空リポのまま |
| CC-BY化＋公式リンク（nishio 2026-05-13 提案） | GitHub上に形跡なし |

Discord 移行 FB期間（〜2026-05-30）直後の週だが、それを受けたアクションは GitHub 側に現れていない。「ボトルネックは技術ではなく人手プロセス（draft PR の ready→merge）」という診断が再確認された形。

### 隣接領域の新規 Issue（保全パイプラインとは別件）

- **Issue [#216](https://github.com/digitaldemocracy2030/website/issues/216)**（2026-05-29、shingo-ohki）「Slackに投稿された事例をもとにウェブサイト更新PRを作成する」  
  `#1_事例紹介_全体` チャンネル投稿を AI で website 更新 PR 化する提案。週次サマリ系パイプラインとは別レイヤだが、「Slack→AI→website PR」という共通パターンを持つ新しいフロー。`weekly-summary.yml` の置き換え/拡張ではない。

## Slack上のやりとり — 2026-06-04 nishio ↔ kuboon

出典: [raw/slack/2026-06-04_oss-weekly-reporter-handoff.md](https://github.com/nishio/dd2030-wiki/blob/main/raw/slack/2026-06-04_oss-weekly-reporter-handoff.md)

5週分の draft PR 滞留と空のままの `slack-logs` リポを背景に、nishio が「Slackログを入れる仕組みは僕が作ればいいのか」と kuboon に問いかけたところ、次の3点が明らかになった。

### 1. `digitaldemocracy2030/slack-logs` が空である直接の理由

> @モアイ（小野）コミュマネ さんからリポジトリ招待もらったのにちょっと忙しくしてる間に expire してしまった。。。 — kuboon

つまり「誰も着手していない」のではなく、**着手予定だった kuboon が招待を取りこぼしてアクセス権を失った**状態。5/23 アナウンスの「すでに作業を開始している」は、Moai 側の認識としては kuboon を招待した時点での見込みだった可能性が高い。

### 2. kuboon が提示した実装基盤候補: `slack-logger-cli-action`

リポジトリ: [`kuboon/slack-logger-cli-action`](https://github.com/kuboon/slack-logger-cli-action)

Issue [#177](https://github.com/digitaldemocracy2030/website/issues/177) で kuboon が「`kuboon/gsheet-slack-logger` を改造して json 出力」と書いていたのとは別系統の、GitHub Actions 向け CLI として既にある実装。「コピーしてもいいしフルスクラッチでもいい」「スレッドのログをたどるのはちょっとしたノウハウ」と添えている。脱-nishio-依存の実装は、新規開発ではなくこの既存資産の移植で済む可能性が高い。

### 3. nishio 側のスタンス変化: 「dd2030-wiki に吸収」

> OSS Weekly Reporterが現状どうなってるのか調べてみたんですけど、(僕はてっきりdd2030で動いていると思い込んでいたのだけど) 今も僕のリポジトリで動いてるのを使ってるんですね
> ここら辺もどうするか考えたい。dd2030-wikiに吸収するので良いかもなという気持ち — nishio 2026-06-04

これまでの暗黙の前提は「`digitaldemocracy2030/website` または `digitaldemocracy2030/slack-logs` に移管する」だったが、nishio は **dd2030-wiki リポジトリ（このリポ）自身に吸収する**第三の選択肢を口にしている。Issue [#170](https://github.com/digitaldemocracy2030/website/issues/170) / [#177](https://github.com/digitaldemocracy2030/website/issues/177) の前提が変わりうる。

なお nishio はこのスレッドと並行して、データ蓄積構成（code repo / data repo 分離、workflow 配置、JSONL gz レイアウト、60日 inactivity 等）に関する設計メモを別途整理している（[raw/documents/2026-06-09_archive-pipeline-design-note.md](https://github.com/nishio/dd2030-wiki/blob/main/raw/documents/2026-06-09_archive-pipeline-design-note.md)）。この設計を dd2030 文脈で読み解いた整理は [[アーカイブパイプライン設計]] にある。

## 方針確定 — 2026-06-09 nishio との対話で

[[アーカイブパイプライン設計]] の paper exercise を経て、次の方針で固まった。

- **保全用 data repo は `digitaldemocracy2030/slack-logs` で確定**。dd2030-wiki は report システム（Quartz 公開ビルド）なので生 Slack ログの一次保管先には向かない、という整理。「dd2030-wiki に吸収」案は撤回。
- **collector は `kuboon/slack-logger-cli-action` を fork なしで `uses:` 導入**。commit step（rename + gzip + users snapshot + 失敗通知）を workflow 側で足す方針。
- **保全（slack-logs 月次）と週次レポート生成（`nishio/oss_weekly_reporter` 週次）は当面分離して併走**。後者の脱-nishio-依存化はフェーズ2。
- Issue [#170](https://github.com/digitaldemocracy2030/website/issues/170) / [#177](https://github.com/digitaldemocracy2030/website/issues/177) の前提が変わる: 「website 側に移管」ではなく「保全は slack-logs に分離・生成は当面 nishio 個人 repo 継続」。

詳細な paper exercise（何ができて何を足す必要があるか、fork 検討の発火条件）は [[アーカイブパイプライン設計]]「paper exercise」節を参照。

## 実装完了 — 2026-06-09

[`digitaldemocracy2030/slack-logs`](https://github.com/digitaldemocracy2030/slack-logs) を bootstrap し、過去16ヶ月分（2025-01〜2026-04）を埋め戻し完了。

| 項目 | 値 |
|---|---|
| 対象 channel 数 | 58（public ch を autoJoin） |
| 保存形式 | `raw/slack/<channel_id>/<YYYY>-<MM>.jsonl.gz` |
| users snapshot | `state/users-<YYYY>-<MM>.json` |
| 月次 cron | 毎月1日 09:11 JST（次回 2026-07-01 が 2026-05 分を取得） |
| 失敗時 | Issue を自動起票（labels: `slack-backup` `failure`） |
| SLACK_TOKEN | nishio が `oss_weekly_reporter` で使っている既存 bot token を流用（フェーズ1）|
| 全 16ヶ月の run 結果 | すべて success |
| repo サイズ | 773 KB（推奨 1GB に対し余裕）|

途中で発見・修正したバグ:

- GitHub Actions の `concurrency: cancel-in-progress: false` は **新しい pending が来ると古い pending を cancel** する仕様。15件並列 dispatch すると最初と最後だけ実行されて残りは cancel される。→ sequential dispatch（外部スクリプトで完了待ち）に変更。
- `git push` の race condition: 連続 dispatch で2つ目以降が `[rejected]`。→ workflow の commit step に `git pull --rebase` retry ループを追加（commit [39a299e](https://github.com/digitaldemocracy2030/slack-logs/commit/39a299e)）。

フェーズ2の残作業:

- ~~CC-BY ライセンスでの公開化（nishio 2026-05-13 提案の実行）~~ → **2026-06-10 確定**（slack-logs リポにデュアルライセンス: データ CC BY 4.0 / コード MIT）
- 公式サイト（dd2030.org）から slack-logs リポへのリンク貼り
- 過去ログ（nishio/oss_weekly_reporter の `data` ブランチ 67週分 117MB）の CC BY 4.0 での再公開経路

（bot token の所有移管は当面 nishio 個人 token を流用する方針で対応不要、と整理）

## 関連ページ

- [archive_index.md](https://github.com/nishio/dd2030-wiki/blob/main/archive_index.md) — アーカイブの参照ガイド
- [[初年度まとめ]] — このアーカイブから構築した時系列まとめ
- [[overview]] — プロジェクト全体の概要
- [[コミュニティ運営]] — Discord 移行検討の文脈
