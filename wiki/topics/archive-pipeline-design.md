---
title: アーカイブパイプライン設計
aliases: [アーカイブパイプライン設計, archive-pipeline-design, ログ蓄積アーキテクチャ]
tags: [dd2030, tooling, explainer, archive]
sources:
  - raw/documents/2026-06-09_archive-pipeline-design-note.md
  - raw/slack/2026-06-04_oss-weekly-reporter-handoff.md
  - digitaldemocracy2030/slack-logs/raw/slack/
created: 2026-06-09
updated: 2026-06-30 (slack-logs 実装後の現在状態を追記)
---

# アーカイブパイプライン設計 — Slack/Scrapbox ログを GitHub に溜めるときの選択

> dd2030 で「Slack 卒業＋過去ログ CC-BY アーカイブ」「OSS Weekly Reporter の脱-nishio-依存」を進めるとき、**どのリポにworkflowを置き、どの粒度で何を保存するか**で後々の運用コストが大きく変わる。

このページは、nishio が 2026-06 にまとめた設計メモ（[raw/documents/2026-06-09_archive-pipeline-design-note.md](https://github.com/nishio/dd2030-wiki/blob/main/raw/documents/2026-06-09_archive-pipeline-design-note.md)）を、dd2030 の文脈（[[OSS Weekly Reporter]] / Issue #170 / #173 / #177 / `digitaldemocracy2030/slack-logs`）に対応づけて整理したもの。具体的な未解決 Issue の状況は [[OSS Weekly Reporter]] を参照。

## 結論（要約）

**コード用 repo とデータ用 repo を分け、workflow はデータ用 repo 側に置く**のが基本。`main` に直接ログを commit する構成は手軽だがソース履歴にデータ更新 commit が混ざり、`data` branch 方式は最新コードと最新データを同時に扱うときに rebase/merge 運用が重くなる。

dd2030 ではこの方針に沿って、Slack チャットログの data repo を [`digitaldemocracy2030/slack-logs`](https://github.com/digitaldemocracy2030/slack-logs) に確定した。2026-06-30 現在は `raw/`（月次 canonical）と `mirror/`（直近14日の rolling snapshot）の二層で動いている。

## 現在の実装（2026-06-30）

```text
digitaldemocracy2030/slack-logs
├── .github/workflows/
│   ├── slack-backup.yml    # 月次 canonical。2ヶ月遅延で raw/ に保存
│   └── slack-mirror.yml    # 6時間ごとの rolling mirror
├── raw/slack/<channel_id>/<YYYY-MM>.jsonl.gz
├── mirror/slack/<channel_id>.jsonl.gz
├── mirror/sync.json
└── state/users-<YYYY-MM>.json
```

確認した `mirror/sync.json` は、`synced_at=2026-06-30T04:12:50Z`、58チャンネル、506メッセージ、14日 window を示している。これにより、保存用の canonical と AI の現状クエリ用 mirror が同じ data repo に集約された。

運用上の注意として、2026-06-30時点では `raw/slack/*/2025-01.jsonl.gz` 〜 `2026-02.jsonl.gz` は各チャンネルのメタデータのみで本文0件だった。2026-03・2026-04には本文が入っているため、設計としての二層構成は成立しているが、初年度の古い本文を調べる時は [[OSS Weekly Reporter]] の週次raw/markdownを補助的に使う。

## 推奨構成

```text
collector-code repo   (optional)
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

ポイントは **raw をまず保存し、加工結果は後で作れるものとして分離する**こと。Slack も Scrapbox も API 仕様が変わりうるので、正規化済みデータだけ残すと変換ロジックを直したいときに元に戻れない。

## なぜ workflow はデータ repo 側がよいか

- GitHub の `GITHUB_TOKEN` は workflow が存在する repo に権限が限定される。別 repo へ push するなら GitHub App installation token または PAT を secret に入れる必要がある。
- public repo の scheduled workflow は、その repo に **60日間 activity がないと自動無効化**される。collector code が安定して更新が止まると、code repo 側の workflow が止まる事故が起きうる（過去 `from_scrapbox` 側で `disabled_inactivity` 事例あり）。

```text
案A: data repo に workflow を置く
  data repo 自身に定期 commit が入る
  code と data が疎結合になる
  GITHUB_TOKEN だけで同一 repo へ push できる

案B: code repo に workflow を置き、data repo へ push する
  collector code の管理は自然
  ただし GitHub App token / PAT が必要
  code repo 側の 60日 inactivity 対策が必要
```

長期運用なら **案A を基本**にし、collector code が育ってきたら別 repo に置いて data repo の workflow から checkout する構成にできる。

## Slack 側の論点

技術的には `conversations.history`（チャンネルメッセージ）と `conversations.replies`（スレッド）を組み合わせる。スレッドは `channel` と親 message の `ts` が必須。

ただし以下の設計上の制約がある。

- **rate limit**: method × workspace × 分単位。429 時は `Retry-After` ヘッダに従う。
- **2025-05-29 以降の非 Marketplace アプリ制限**: Marketplace 外で商用配布される新規アプリでは `conversations.history` / `conversations.replies` が **1分1リクエスト・最大15件**。Marketplace app と internal customer-built app は Tier 3 扱い。dd2030 用途は「internal customer-built」に当たるので分けて考えられる。
- **Slack Developer Policy**: Data の収集・保存・利用には適切な同意が必要。LLM training への利用は禁止。Data 保存には暗号化等の注意。

技術より先に決めるべき意思決定:

```text
取る範囲:
  public channel だけか
  private channel も含むか
  DM は取らないのか
  bot が参加している channel だけか

保存する粒度:
  message 本文を保存するか
  URL・ts・user_id・channel_id だけ保存するか
  添付ファイル本文まで追うか

利用目的:
  個人の検索用
  週次レポート生成
  公開アーカイブ
  LLM/RAG 用の検索 index
```

実装上は **Slack は差分取得・冪等保存が必須**。GitHub Actions の schedule は遅延・drop されうるので、`oldest = 前回成功 watermark - overlap` で少し重複取得し、`channel_id + ts` で重複排除する。

## Scrapbox / Cosense 側の論点

Cosense ヘルプの API ページは「あくまで内部 API」「予告なく変更される」と明記している。バックアップ用途なら Project Settings → Page Data → Export Pages（metadata 付きで行ごとの作成・編集日時を保存）が素直。コミュニティ記述では `/api/page-data/export/:projectname.json?metadata=true` が同等。

2段階構成がよい:

```text
毎日:
  project 全体の metadata 付き export を snapshot 保存

数分〜数時間ごと:
  /api/pages/:projectName?sort=updated で更新ページ候補を取り
  changed page だけ個別取得
```

private project の場合の Cookie 認証は漏洩時の影響が大きい。public repo の Actions では特に避け、private repo＋最小権限＋secret 漏洩対策を前提に。

## GitHub を保存先にする利点と限界

利点: 履歴・差分・レビュー・Actions・Pages・検索・clone 可能性が一体化。

限界:
- file は **50MiB 超で警告、100MiB 超で block**。repo は理想 1GB 未満、強く推奨 5GB 未満。
- **Actions artifact / log はデフォルト 90日で削除**（長期保存先ではなく一時成果物向け）。
- 巨大バイナリは Release も選択肢（1 release あたり最大 1000 assets、各 2GiB 未満）だが、運用は Git commit より複雑。

→ 「小〜中規模のテキストログを透明な履歴付きで蓄積する場所」としては有用。「Slack 全履歴の恒久アーカイブ」「添付込みの巨大バックアップ」「組織横断の検索基盤」まで行くと GitHub repo だけでは無理が出る。

## 保存形式

JSONL gzip / zstd を推奨。

```text
raw/slack/T123/C456/2026/06/09.jsonl.gz
raw/slack/T123/C456/threads/1482960137.003543.json.gz
raw/scrapbox/nishio/snapshots/2026-06-09.json.gz
normalized/slack/messages/2026/06/09.jsonl.gz
normalized/scrapbox/pages/<page_id>.json
state/slack.json
state/scrapbox.json
```

Slack message の保存キー:

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

`raw` を残す理由: 後から正規化ロジックの誤りに気づいたとき再処理できる。

## commit 戦略

毎回全ファイル書き換えだと Git 履歴が肥大化する。

```text
Slack:
  日付別 append
  1日1ファイル or channel ごと 1日1ファイル
  同じ ts は追記前に除去

Scrapbox:
  snapshot は日次・週次
  個別 page は上書き
  大きな全量 export は圧縮して別ディレクトリ

commit:
  変更があるときだけ commit
  message は機械可読
  例: collect slack 2026-06-09T06:00Z channels=12 messages=183
```

Actions 側は `concurrency` で二重起動を回避:

```yaml
concurrency:
  group: collect-logs
  cancel-in-progress: false
```

## 失敗モードと対策

1. **取得したつもりで watermark だけ進む** → 保存 commit が成功してから state を進める。失敗したら次回同じ範囲を再取得し `channel_id + ts` で重複排除。
2. **Slack rate limit** → 429 は `Retry-After` に従う。大量過去ログの初回取得は通常の定期 workflow ではなく手動 `workflow_dispatch` で channel・期間を分割。rate limit は method/workspace 単位なので channel を増やしても無制限には速くならない。
3. **secret 漏洩** → Slack token、Scrapbox Cookie、GitHub App key / PAT は Actions Secrets。public repo で PR 由来の workflow に secret を渡さない。data repo が public なら raw Slack 本文を置く設計は慎重に。

## 段階的アプローチ

```text
1. data repo を private で作る
2. workflow は data repo 側に置く
3. Slack は対象 public channel を少数に限定
4. Scrapbox は日次 export + 更新ページ差分
5. raw jsonl.gz と state だけ commit
6. derived markdown / report は別 workflow で生成
7. 30日ほど運用して repo 増加量を見る
8. 増え方が大きければ snapshot を Release か外部 object storage へ逃がす
```

この構成なら「main 汚染」「data branch 運用の重さ」「code/data 分離時の60日 inactivity」をかなり避けられる。

## dd2030 文脈での当てはめ

この設計を dd2030 の現状（[[OSS Weekly Reporter]] 参照）に当てると次のようになる。

| 既存の状況 | この設計から導かれる読み |
|---|---|
| `nishio/oss_weekly_reporter` が code+data 同居（`main` にコード、`data` ブランチに週次データ） | 「data branch 方式は最新コードと最新データを同時に扱うとき重くなる」に該当。長期運用では code repo / data repo 分離が望ましい |
| `digitaldemocracy2030/website` 側に weekly-summary.yml を置き、`nishio/oss_weekly_reporter` の data ブランチを checkout している | code repo に workflow がある「案B」。website 側の inactivity と PAT/token 管理が論点。自動生成PRの人手確認・mergeボトルネック（PR #211 は2026-06-30再確認時もOPEN）はこれとは別の人手プロセス問題 |
| `digitaldemocracy2030/slack-logs` | この設計の data repo。2026-06-09 に workflow と過去分 backfill が入り、2026-06-30 現在は `raw/` と `mirror/` の二層で稼働 |
| kuboon が [`slack-logger-cli-action`](https://github.com/kuboon/slack-logger-cli-action) を実装基盤候補として提示 | collector code の側。data repo 側 workflow から `uses:` で呼ぶ案 A が自然 |
| nishio が「dd2030-wiki に吸収」案を口にしている | dd2030-wiki を data repo として使う = 案A 寄り。ただし wiki の公開ビルド（Quartz → GitHub Pages）と raw JSONL の同居は、repo サイズと公開範囲の設計を要する |
| Issue [#177](https://github.com/digitaldemocracy2030/website/issues/177) の kuboon プラン（GitHub は token 不要、Slack は gsheet-slack-logger 改造、OpenAI はプロンプト流用） | data repo を slack-logs にし workflow も slack-logs 側に置く案A の具体化。`slack-logger-cli-action` ベースに置き換えれば改造工数も減る |

## 方針確定（2026-06-09）

nishio との対話で次のように決めた。

- **data repo = `digitaldemocracy2030/slack-logs` で確定**。
  理由: dd2030-wiki は report システム（Quartz 公開ビルドが入る）なので、生 Slack ログの一次保管先には向かない。既に名前空間が確保されており、案A（data repo に workflow を置く）と整合する。
- **collector code = `kuboon/slack-logger-cli-action` を `uses:` でそのまま導入**（fork なし）。
- **保全（slack-logs）と週次レポート生成（`nishio/oss_weekly_reporter`）は分離して併走**。後者を slack-logs ベースに移し替えるのは保全が安定してからの第2フェーズ。

この方針は実装済み。以後は「Slack 生ログをどこに置くか」ではなく、「週次AIレポート生成や website history 更新をどこまで `slack-logs` ベースに寄せるか」が次の論点になる。

## paper exercise — slack-logger-cli-action をそのまま入れたら何が起きるか

`kuboon/slack-logger-cli-action` のソースを読んで動作を整理した結果。

### 最小 workflow（slack-logs に置く案）

```yaml
# .github/workflows/slack-backup.yml
name: slack-backup
on:
  schedule:
    - cron: '11 0 1 * *'   # 毎月1日 09:11 JST
  workflow_dispatch:
    inputs:
      year: { required: true }
      month: { required: true }
jobs:
  main:
    runs-on: ubuntu-latest
    permissions: { contents: write }
    steps:
      - uses: actions/checkout@v4
      - uses: kuboon/slack-logger-cli-action@main
        id: slack
        with:
          slackToken: ${{ secrets.SLACK_TOKEN }}
          timezone: 'Asia/Tokyo'
          year: ${{ inputs.year }}
          month: ${{ inputs.month }}
      - name: commit jsonl
        run: |
          mkdir -p raw/slack
          cp -r ${{ steps.slack.outputs.jsonl_dir }}/* raw/slack/
          git config user.name dd2030-bot
          git config user.email bot@dd2030.invalid
          git add raw/slack
          git diff --cached --quiet || git commit -m "slack backup $(date -u +%FT%TZ)"
          git push
```

Secrets は `SLACK_TOKEN` のみ（Google Sheets 系の input は optional なので不要）。
必要な Slack scope: `channels:history` `channels:read` `users:read` `channels:join`。

### この構成でカバーできるもの

| 設計メモの要件 | 充足 | 補足 |
|---|---|---|
| 案A（data repo に workflow） | ✅ | 完全一致 |
| 60日 inactivity 対策 | ✅ | 毎月コミットが入る |
| スレッド (`conversations.replies`) 取得 | ✅ | `fetchHistory` 内で reply_count>0 の親ごとに呼ぶ |
| 全 public channel 自動カバー | ✅ | `autoJoin: true` で `conversations.join` 自動実行 |
| 除外指定 | ✅ | `skipChannels` 入力（channel id を空白区切り） |
| 過去分埋め戻し | ✅ | `workflow_dispatch` + `year`/`month` で月単位 |

### 足りない / 設計メモの推奨と違う点

| 項目 | slack-logger-cli-action | 推奨 | dd2030 でどうするか |
|---|---|---|---|
| ファイル粒度 | `<channel_id>.jsonl` を毎回 truncate して 1ヶ月分書き出し | 日付別 append | commit step で `raw/slack/<channel_id>/<YYYY>-<MM>.jsonl` に rename して保存 |
| 圧縮 | なし | gzip / zstd | commit step に `gzip` を1行挟む |
| state 管理 | なし（year/month 引数決め打ち） | `state/slack.json` で watermark | 月単位パスで一意に決まるので state 不要 |
| rate limit 対応 | 429/Retry-After のリトライロジックが見えない | 必要 | bot を **internal customer-built** として登録すれば 2025-05-29 制限の対象外（要確認）。だめなら fork |
| users.list snapshot | 実行時の解決にしか使わない（jsonl は raw user_id のまま） | 退会者解決のため snapshot 必要 | commit step に `users.list` を `state/users-<YYYY>-<MM>.json` として保存するロジックを足す |
| private channel / DM | 非対応（`types: ["public_channel"]` 決め打ち） | — | CC-BY 公開化と整合的、これで OK |
| 失敗通知 | なし | 必要 | 失敗時に Slack 通知 or Issue 自動起票を workflow に足す（`weekly-summary.yml` の PR#211 滞留パターンを再演しない） |

### スレッド返信のラグ問題

README が明示している重要な前提:

> 「スレッド返信はその発言元の時刻でしか取得できない」
> 例: 9/30 投稿に対し 10/2 にスレッド返信 → 9月分を 10/1 に取得すると 10/2 の返信はどこにも残らない
> → デフォルト「実行日の2ヶ月前の1ヶ月分」を取る設計

dd2030 で考えると:
- **保全（slack-logs）**: 月次 + 2ヶ月遅延で問題なし。履歴消失防止が目的。
- **週次 AI レポート（oss_weekly_reporter）**: 即時性が要るので、現状の週次バッチを併走させる。スレッド完全性は二次的に slack-logs の月次バックフィルで補完される。

### 結論

**fork は不要**。`uses:` でそのまま導入して、commit step を足すだけで実用最小限が動く:

1. `cp` でファイルを `raw/slack/<channel_id>/<YYYY>-<MM>.jsonl` に rename
2. `gzip` で圧縮
3. `users.list` を `state/users-<YYYY>-<MM>.json` として一緒に commit
4. 失敗時に Issue 自動起票

将来 fork を検討する条件:
- 日付別 append + watermark に揃えたくなったとき
- 429 / Retry-After 対応をまじめにやる必要が出たとき
- private channel も取りたくなったとき

## 残った宿題

- [x] ~~`digitaldemocracy2030/slack-logs` の data repo 化~~ → 2026-06-09 実装済み
- [x] ~~現状クエリ用 mirror 層~~ → 2026-06-09 実装済み、2026-06-30 時点でも同期継続を確認
- [x] ~~**public か private か**~~ → **2026-06-10 確定**: public + デュアルライセンス（データ CC BY 4.0 / コード MIT）
- [ ] dd2030 Slack bot が **internal customer-built** として登録されているかの確認（rate limit の前提）
- [ ] **過去ログの移送**: nishio 個人 repo の `data` ブランチ 67週分（117MB）の CC-BY 再公開経路。slack-logs が動き始めてから別作業。
- [ ] 週次AIレポート生成・website history 更新を `slack-logs` ベースに寄せるかどうかの判断。2026-06-30時点で website PR #211 と Issue #170/#173/#177 はOPENのまま

## 関連ページ

- [[topics/first-reader-guide|初めて読む人へ]] — Wiki全体とアーカイブ関連ページへの入り方
- [[Slackログアーカイブ]] — 現在の `slack-logs` の読み方
- [[AI から Slack ログを参照するパターン]] — 保全用途と現状クエリ用途の使い分け
- [[OSS Weekly Reporter]] — 現状のパイプラインと滞留状況
- [[sources/archive-pipeline-design-note|アーカイブパイプライン設計メモ]] — このページの主要ソース要約
- [[sources/oss-weekly-reporter-handoff|OSS Weekly Reporter 移管Slackメモ]] — 移管経緯のSlackメモ要約
- [archive_index.md](https://github.com/nishio/dd2030-wiki/blob/main/archive_index.md) — 外部アーカイブ参照ガイド
- [[コミュニティ運営]] — Discord 移行の文脈
