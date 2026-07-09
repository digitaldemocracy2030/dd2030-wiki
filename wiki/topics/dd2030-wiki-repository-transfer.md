---
title: dd2030-wiki の dd2030 org 移行
aliases: [dd2030-wiki の dd2030 org 移管, dd2030-wiki の dd2030 org 移行, dd2030-wiki org移管, dd2030-wiki org移行, dd2030-wiki repository transfer]
tags: [dd2030, tooling, wiki, github, operations]
sources:
  - digitaldemocracy2030/slack-logs/mirror/slack/C08N2NU6D0S.jsonl.gz
  - digitaldemocracy2030/slack-logs/mirror/sync.json
  - "GitHub API: nishio/dd2030-wiki, digitaldemocracy2030/dd2030-wiki (2026-07-09確認)"
created: 2026-07-09
updated: 2026-07-09
---

# dd2030-wiki の dd2030 org 移行

`nishio/dd2030-wiki` として運用してきたこの Wiki を、`digitaldemocracy2030` organization 配下の新しい正規リポジトリへ移す作業メモ。2026-07-09時点では、移行はまだ実行していない。

## 結論

GitHub の repository transfer は使わない。既存の公開URL `https://nishio.github.io/dd2030-wiki/` を消すと、すでにリンクしている人にリンク切れを起こす可能性があるため。

推奨方針は次の二段階移行。

1. `digitaldemocracy2030/dd2030-wiki` を新規作成し、現在の Wiki をコピーして新サイト `https://digitaldemocracy2030.github.io/dd2030-wiki/` を公開する。
2. 新サイトの動作確認後、旧 `nishio/dd2030-wiki` は残したまま、旧サイトを「移動しました」アナウンス付きの案内ページにする。

深いページへの旧リンクも考慮するなら、旧サイトにはトップページだけでなく `404.html` も置き、同じパスの新URLへ案内または自動転送できるようにする。より丁寧にする場合は、しばらく旧コンテンツを読み取り専用で残し、全ページに移動告知を出す。

## 背景

2026-07-03から2026-07-04にかけて、Slack の `2_コミュニティ運営` で、公開 Wiki（`nishio.github.io/dd2030-wiki`）を dd2030 のリポジトリと AI で運用したい、という相談があった。

相談の目的は、[[OSS Weekly Reporter]] の代替的な活動把握先、また新規参加者向けガイドブックからのリンク先として、この Wiki を継続的に使える状態にすることだった。返信では、リポジトリを dd2030 側へ移せば Devin などの AI エージェントがメンテナンスしやすくなりそう、という見立てが共有され、来週半ばごろに作業する方向になった。

出典は `digitaldemocracy2030/slack-logs/mirror/slack/C08N2NU6D0S.jsonl.gz`。`mirror/` は上書きされる現状ミラーなので、長期的な根拠として残す必要がある場合は、後日 `raw/slack/C08N2NU6D0S/2026-07.jsonl.gz` の月次 canonical でも確認する。

## 2026-07-09時点の確認

| 項目 | 状態 |
|---|---|
| 現在のリポジトリ | `nishio/dd2030-wiki` |
| 新しい正規リポジトリ候補 | `digitaldemocracy2030/dd2030-wiki` |
| 新リポジトリ名 | 2026-07-09時点では未作成 |
| 現在の公開URL | `https://nishio.github.io/dd2030-wiki/` |
| 新しい公開URL | `https://digitaldemocracy2030.github.io/dd2030-wiki/` |
| 旧公開URLの扱い | 残して「移動しました」告知にする |
| GitHub Pages | GitHub Actions workflow で `public/` を deploy |
| Quartz設定 | `quartz.config.ts` の `baseUrl` が `nishio.github.io/dd2030-wiki` |
| 認証ユーザー | `nishio` が現リポジトリ admin かつ `digitaldemocracy2030` org admin |

## 移行で変わるもの

- GitHub リポジトリの正規URLは `https://github.com/digitaldemocracy2030/dd2030-wiki` になる。
- GitHub Pages の正規URLは `https://digitaldemocracy2030.github.io/dd2030-wiki/` になる。
- 旧URL `https://nishio.github.io/dd2030-wiki/` は消さず、移動告知ページとして残す。
- 新リポジトリ側では `quartz.config.ts` の `baseUrl`、README、Wiki内の自己参照リンクを更新する必要がある。
- ローカル clone の `origin` は、移行後に `https://github.com/digitaldemocracy2030/dd2030-wiki.git` へ更新する。旧リポジトリは `nishio` など別名 remote として残す。
- Devin など、dd2030 org 側の AI エージェントがリポジトリを扱いやすくなる。

この移行は Wiki 本体の正規運用場所を変える作業であり、[[Slackログアーカイブ]] の生ログ置き場を変える作業ではない。Slack チャットログ本体は引き続き `digitaldemocracy2030/slack-logs` を参照する。

## 作業前チェック

- `main` が `origin/main` と一致し、作業ツリーが clean であることを確認する。
- 未pushのブランチ、未mergeの PR、GitHub Actions の失敗がないか確認する。
- `.claude/settings.local.json` のようなローカル設定や secret らしき値を stage しない。
- `digitaldemocracy2030/dd2030-wiki` がまだ存在しないことを確認する。
- 旧URLから新URLへの案内方法を決める。最低限、旧トップページと `404.html` に移動告知を置く。
- Devin / GitHub App / Actions secrets / Pages 設定が、新リポジトリでも必要な権限を持つか確認する。

## 推奨手順

1. `main` を最新化し、必要なら直前の変更を commit / push する。
2. `digitaldemocracy2030/dd2030-wiki` を新規作成する。repository transfer は使わない。
3. 現在の `main` を新リポジトリへ push する。

```bash
gh repo create digitaldemocracy2030/dd2030-wiki --public
git remote add dd2030 https://github.com/digitaldemocracy2030/dd2030-wiki.git
git push dd2030 main
git push dd2030 --tags
```

4. ローカル clone の remote を、新リポジトリを正規 `origin`、旧リポジトリを `nishio` として整理する。

```bash
git remote rename origin nishio
git remote rename dd2030 origin
git fetch origin
```

5. 新リポジトリ側で `quartz.config.ts` の `baseUrl` を `digitaldemocracy2030.github.io/dd2030-wiki` に変更する。
6. README と Wiki 内の自己参照リンクを更新する。

```bash
rg "nishio.github.io/dd2030-wiki|github.com/nishio/dd2030-wiki|nishio/dd2030-wiki"
```

`nishio/oss_weekly_reporter` は補助アーカイブとして意図的に参照しているため、単純置換しない。

7. 新リポジトリの GitHub Pages Source が GitHub Actions になっていることを確認する。
8. build とリンク検査を通す。

```bash
pnpm build && pnpm check:pages-links
```

9. `https://digitaldemocracy2030.github.io/dd2030-wiki/` で公開確認する。
10. 旧 `nishio/dd2030-wiki` を、移動告知サイトに変更する。
11. 必要なら Slack の元スレッドへ、新URL・旧URLの案内・編集方法を共有する。

## 旧サイトの告知仕様

旧サイトは削除せず、少なくとも次を満たす。

- トップページに「移動しました」と新URLを明示する。
- `404.html` にも同じ告知を置き、古い深いURLへ来た人を新サイトへ案内する。
- 自動転送する場合でも、数秒待ってから移動するか、明示リンクを必ず置く。
- 既存の深いリンクをできるだけ守るなら、旧サイトの各ページを同じパスの新URLへ転送する redirect page に置き換える。
- より安全な暫定策として、旧サイトの既存コンテンツをしばらく残し、全ページ上部に移動告知を出す方法もある。

## 新リポジトリ側で更新するページ

- [[index]] — 外部アーカイブ参照ガイドへの GitHub URL を新リポジトリへ更新する。
- [[Wiki保守運用]] — 移行後の commit / PR / AIメンテナンス手順を必要に応じて追記する。
- [[Slackログアーカイブ]] — `archive_index.md` へのリンクが `nishio/dd2030-wiki` を指している箇所を更新する。
- [[AI から Slack ログを参照するパターン]] — 同上。
- `README.md` — 公開サイトURLと clone 先の説明を更新する。
- `quartz.config.ts` — GitHub Pages project site の base URL を更新する。

## 未決事項

- 旧サイトを「告知だけ」にするか、「旧コンテンツを残してバナーを出す」期間を置くか。
- 深いページへの旧リンクを、`404.html` だけで案内するか、全ページ redirect を生成するか。
- GitHub Pages の新リポジトリ初回デプロイで、Pages 設定の再有効化が必要か。
- Devin に渡す標準作業手順を、[[Wiki保守運用]] に統合するか、このページを移行作業専用ページとして残すか。
- 新規参加者向けガイドブックからリンクする正式URLをいつ切り替えるか。

## 関連ページ

- [[Wiki保守運用]] — Wiki更新時の検証と commit hygiene
- [[Slackログアーカイブ]] — Slackチャットログ本体の参照先
- [[OSS Weekly Reporter]] — 活動把握・週次レポート生成の移行文脈
- [[AI から Slack ログを参照するパターン]] — AI が Slack / Wiki を読む運用パターン
