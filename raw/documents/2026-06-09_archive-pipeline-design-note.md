結論から言うと、**GitHub ActionsでSlack/ScrapboxログをGitHub上に溜めるなら、コード用repoとデータ用repoを分け、workflowはできればデータ用repo側に置く**のがよいです。`main`に直接ログをcommitする構成は手軽ですが、データ更新commitがソースコードの履歴に混ざる。`data` branch案は一見よいものの、最新コードと最新データを同時に扱うときにrebase/merge運用が重くなる、という西尾さんのメモの観察は妥当です。

## 推奨構成

構成としてはこうです。

```text
collector-code repo   optional
  └─ collector scripts / tests / README

data repo
  ├─ .github/workflows/collect.yml
  ├─ state/
  │   ├─ slack.json
  │   └─ scrapbox.json
  ├─ raw/
  │   ├─ slack/<workspace>/<channel>/<yyyy>/<mm>/<dd>.jsonl.gz
  │   └─ scrapbox/<project>/snapshots/<yyyy-mm-dd>.json.gz
  ├─ normalized/
  │   ├─ slack/messages/<yyyy>/<mm>/<dd>.jsonl.gz
  │   └─ scrapbox/pages/<project>/<page_id>.json
  └─ derived/
      └─ markdown / index / reports
```

ポイントは、**rawをまず保存し、加工結果は後で作れるものとして分離する**ことです。SlackもScrapboxもAPI仕様やレスポンス形式が変わりうるので、正規化済みデータだけを残すと、後で変換ロジックを直したいときに元に戻れません。

## なぜworkflowはデータrepo側がよいか

GitHubの`GITHUB_TOKEN`は、workflowが存在するrepoに権限が限定されます。別repoへpushするなら、GitHub Appのinstallation tokenかPATをsecretに入れる必要があります。GitHub公式ドキュメントも、`GITHUB_TOKEN`で足りない権限が必要な場合はGitHub App tokenまたはPATを使う、と説明しています。([GitHub Docs][1]) ([GitHub Docs][2])

さらに、public repoのscheduled workflowは、そのrepoに60日間activityがないと自動無効化されます。これはGitHub公式ドキュメントにも明記されています。([GitHub Docs][3]) 西尾さんのメモでも、`from_scrapbox`側のworkflowが`disabled_inactivity`になり、更新先repoではなく「workflowが置かれているrepo」のactivity不足が問題になった、という事例が書かれています。

したがって、次のどちらかがよいです。

```text
案A: data repoにworkflowを置く
  data repo自身に定期commitが入る
  codeとdataが疎結合になる
  GITHUB_TOKENだけで同一repoへpushできる

案B: code repoにworkflowを置き、data repoへpushする
  collector codeの管理は自然
  ただしGitHub App token/PATが必要
  code repo側の60日inactivity対策が必要
```

長期運用なら、**案Aを基本**にした方が事故が少ないです。collector codeが育ってきたら、collectorを別repoに置いて、data repoのworkflowからそのコードをcheckoutする構成にできます。

## Slack側の考察

Slackログ取得は、技術的には`conversations.history`と`conversations.replies`を使うのが基本です。`conversations.history`は指定conversationのmessage eventsの一部を返し、cursor pagination、`oldest`、`latest`、`limit`で範囲取得できます。token種別によって読めるconversation範囲が変わります。([Slack Developer Docs][4]) スレッドは`conversations.replies`で取得し、`channel`と親messageの`ts`が必須です。([Slack Developer Docs][5])

ただしSlackはここが設計上の制約になります。SlackのWeb API rate limitは「methodごと、workspaceごと、分単位」で評価され、429時は`Retry-After`ヘッダに従う必要があります。([Slack Developer Docs][6]) さらに2025年5月29日以降、Marketplace外で商用配布される新規・新規インストールの非Marketplaceアプリでは、`conversations.history`と`conversations.replies`が1分1リクエスト、最大15件に制限されます。一方、Marketplace appとinternal customer-built appはTier 3扱いです。([Slack Developer Docs][7]) ([Slack Developer Docs][8])

西尾さん自身の用途が「自分または所属組織の内部用アプリ」なら、商用配布アプリの制限とは分けて考えられます。ただし、SlackのDeveloper Policyは、Dataの収集・保存・利用には適切な同意が必要で、LLM trainingへの利用は禁止、Dataの保存には暗号化などの注意が求められる、としています。([Slack Developer Docs][9]) API Termsでも、外部組織向けアプリではAPI Dataの利用・処理・保存を機能に必要な最小限に制限することが求められています。([Slack][10])

つまりSlackについては、技術より先に次を決めるべきです。

```text
取る範囲:
  public channelだけか
  private channelも含むか
  DMは取らないのか
  botが参加しているchannelだけか

保存する粒度:
  message本文を保存するか
  URL・ts・user_id・channel_idだけ保存するか
  添付ファイル本文まで追うか

利用目的:
  個人の検索用
  週次レポート生成
  公開アーカイブ
  LLM/RAG用の検索index
```

実装上は、**Slackは差分取得・冪等保存が必須**です。GitHub Actionsのscheduleは高負荷時に遅延またはdropされる可能性があり、最短間隔は5分です。現在のGitHub Actionsではtimezone指定もできますが、正確な時刻起動を前提にせず、`oldest = 前回成功watermark - overlap`のように少し重複して取得し、`channel_id + ts`で重複排除する方が安全です。([GitHub Docs][11])

## Scrapbox/Cosense側の考察

Scrapbox/Cosenseは、Slackよりもログ取得しやすい一方で、APIの安定性に注意が必要です。CosenseヘルプのAPIページは、APIを「あくまで内部API」であり予告なく変更されると明記しています。ページ一覧、ページデータ、ページ本文を取得する内部APIはあります。([Cosense][12])

バックアップ用途なら、Cosenseのexport機能を使うのが素直です。公式ヘルプは、Project SettingsのPage DataからExport Pagesでき、metadataを含めると行の作成・編集日時を保存できる、と説明しています。([Cosense][13]) コミュニティ側の記述では、`/api/page-data/export/:projectname.json`に`metadata=true`を付けると、行ごとの作成日時・更新日時などを含むexportが得られるとされています。これは自動化には便利ですが、公式安定APIではない点は残ります。([Cosense][14])

Scrapboxは2段階がよいです。

```text
毎日:
  project全体のmetadata付きexportをsnapshot保存

数分〜数時間ごと:
  /api/pages/:projectName?sort=updated
  で更新ページ候補を取り、
  changed pageだけ個別取得
```

全量snapshotは復元性のため、差分取得は日常の検索・分析の鮮度のためです。private projectの場合は認証情報をActions Secretに置くことになりますが、Cookie方式は漏洩時の影響が大きいので、公開repoのActionsでは特に避けるか、private repo＋最小権限＋secret漏洩対策を前提にした方がよいです。

## GitHubを保存先にする利点と限界

GitHubに溜める利点は、履歴・差分・レビュー・Actions・Pages・検索・clone可能性が一体化していることです。個人の外部脳や週次レポート生成には相性がよいです。

一方で、Gitは大きなログデータベースではありません。GitHubは通常repoのファイルについて50MiB超で警告、100MiB超をblockし、repoは理想的には1GB未満、5GB未満を強く推奨しています。大きなSQLファイルや巨大データの共有にはGit以外の手段を推奨しています。([GitHub Docs][15]) Actions artifact/logはデフォルト90日で削除されるので、長期保存先ではなく一時成果物向けです。([GitHub Docs][16])

大きなバイナリや圧縮アーカイブを置くならReleaseも選択肢です。GitHub Releasesは1 releaseあたり最大1000 assets、各fileは2GiB未満という制約です。([GitHub Docs][17]) ただし、西尾さんのメモにもある通り、releaseに置く構成はGit commit保存より運用が複雑になります。

## 保存形式

おすすめはJSONL gzip/zstdです。

```text
raw/slack/T123/C456/2026/06/09.jsonl.gz
raw/slack/T123/C456/threads/1482960137.003543.json.gz
raw/scrapbox/nishio/snapshots/2026-06-09.json.gz
normalized/slack/messages/2026/06/09.jsonl.gz
normalized/scrapbox/pages/<page_id>.json
state/slack.json
state/scrapbox.json
```

Slack messageのキーはこうします。

```json
{
  "source": "slack",
  "workspace_id": "T...",
  "channel_id": "C...",
  "ts": "1717891234.000100",
  "thread_ts": "1717891234.000100",
  "user": "U...",
  "text": "...",
  "raw": { "...": "..." },
  "fetched_at": "2026-06-09T06:00:00Z"
}
```

Scrapbox pageはこうします。

```json
{
  "source": "scrapbox",
  "project": "nishio",
  "page_id": "...",
  "title": "...",
  "created": 1710000000,
  "updated": 1718000000,
  "lines": [],
  "raw": { "...": "..." },
  "fetched_at": "2026-06-09T06:00:00Z"
}
```

`raw`を残す理由は、後から「この正規化は間違っていた」と気づいたときに再処理できるからです。

## commit戦略

毎回全ファイルを書き換えるとGit履歴が肥大化します。方針は次がよいです。

```text
Slack:
  日付別append
  1日1ファイルまたはchannelごと1日1ファイル
  同じtsは追記前に除去

Scrapbox:
  snapshotは日次・週次
  個別pageは上書き
  大きな全量exportは圧縮して別ディレクトリ

commit:
  変更があるときだけcommit
  commit messageは機械可読にする
  例: collect slack 2026-06-09T06:00Z channels=12 messages=183
```

Actions側は`concurrency`を使って二重起動を避けます。scheduleの遅延や手動実行が重なったときに、同じファイルへ同時pushして衝突するのを防ぐためです。

```yaml
concurrency:
  group: collect-logs
  cancel-in-progress: false
```

## 失敗モードと対策

一番危ないのは、「取得したつもりでwatermarkだけ進む」ことです。対策は、**保存commitが成功してからstateを進める**ことです。Slackなら、`latest=run_started_at`まで取得し、保存とcommitが成功したら`last_successful_latest`を更新する。失敗したら次回同じ範囲を再取得し、`channel_id + ts`で重複排除します。

次に危ないのは、Slackのrate limitです。429を受けたら`Retry-After`に従う。大量の過去ログを初回取得する場合は、通常の定期workflowではなく、手動`workflow_dispatch`で対象channel・期間を分割して走らせる方がよいです。Slackのrate limitはmethod/workspace単位なので、channelを増やしても無制限には速くなりません。([Slack Developer Docs][6])

三つ目は、secret漏洩です。Slack token、Scrapbox private project用Cookie、GitHub App private key/PATはすべてActions Secretsに入れる。public repoでpull request由来のworkflowにsecretを渡さない。保存先data repoがpublicなら、raw Slack本文を置く設計はかなり慎重に扱うべきです。

## 判断

この用途では、GitHubは「小〜中規模のテキストログを、透明な履歴付きで蓄積する場所」としては有用です。しかし「Slack全履歴の恒久アーカイブ」「添付ファイル込みの巨大バックアップ」「組織横断の検索基盤」まで行くと、GitHub repoだけでは無理が出ます。

私なら最初はこうします。

```text
1. data repoをprivateで作る
2. workflowはdata repo側に置く
3. Slackは対象public channelを少数に限定
4. Scrapboxは日次export + 更新ページ差分
5. raw jsonl.gzとstateだけcommit
6. derived markdown/reportは別workflowで生成
7. 30日ほど運用してrepo増加量を見る
8. 増え方が大きければsnapshotをReleaseか外部object storageへ逃がす
```

この構成なら、西尾さんのメモにある「main汚染」「data branch運用の重さ」「code/data分離時の60日inactivity」をかなり避けられます。

[1]: https://docs.github.com/en/actions/concepts/security/github_token "GITHUB_TOKEN - GitHub Docs"
[2]: https://docs.github.com/actions/reference/authentication-in-a-workflow "Use GITHUB_TOKEN for authentication in workflows - GitHub Docs"
[3]: https://docs.github.com/actions/managing-workflow-runs/disabling-and-enabling-a-workflow "Disabling and enabling a workflow - GitHub Docs"
[4]: https://docs.slack.dev/reference/methods/conversations.history "conversations.history method | Slack Developer Docs"
[5]: https://docs.slack.dev/reference/methods/conversations.replies "conversations.replies method | Slack Developer Docs"
[6]: https://docs.slack.dev/apis/web-api/rate-limits "Rate limits | Slack Developer Docs"
[7]: https://docs.slack.dev/changelog/2025/05/29/rate-limit-changes-for-non-marketplace-apps "Rate limit changes for non-Marketplace apps | Slack Developer Docs"
[8]: https://docs.slack.dev/ja-jp/2025-05-terms-rate-limit-update-and-faq "非 Marketplace アプリのレート制限の変更 | Slack Developer Docs"
[9]: https://docs.slack.dev/developer-policy "Slack App Developer Policy | Slack Developer Docs"
[10]: https://slack.com/terms-of-service/api "Slack API Terms of Service | Legal | Slack"
[11]: https://docs.github.com/actions/using-workflows/events-that-trigger-workflows "Events that trigger workflows - GitHub Docs"
[12]: https://scrapbox.io/help-jp/API "API - Cosense ヘルプ"
[13]: https://scrapbox.io/help/Importing_and_exporting_data "Importing and exporting data - Cosense Help"
[14]: https://scrapbox.io/scrapboxlab/api%2Fpage-data%2Fexport%2F%3Aprojectname.json "api/page-data/export/:projectname.json - Cosense研究会"
[15]: https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github "About large files on GitHub - GitHub Docs"
[16]: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository "Managing GitHub Actions settings for a repository - GitHub Docs"
[17]: https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases "About releases - GitHub Docs"
