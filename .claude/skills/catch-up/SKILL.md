---
name: catch-up
description: dd2030 の最近の動き（Slack・議事録 Google Docs・GitHub）を一括で取得して Wiki 未反映分を見つけ、必要なら Wiki に反映する。「最近の動きを見て」「Slack 見てる？」「議事録に差分ある？」「最新状況にして」「キャッチアップして」などで使う。
---

# catch-up — 最近の動きを取得して Wiki に反映する

## 1. 取得（機械的な部分はスクリプトに任せる）

```bash
python3 scripts/catch-up.py            # wiki/log.md の最新エントリ日から今日まで
python3 scripts/catch-up.py --since 2026-10-26
python3 scripts/catch-up.py --days 7 --no-github
```

1〜2分かかる。出力は `work/catch-up/<今日>/report.md`（git 管理外）に保存され、標準出力にも出る。長いときはファイルを読む。

やってくれること:
- `work/slack-logs` を pull し、mirror の直近メッセージをチャンネル別・人名解決済みで一覧（GitHub bot チャンネルと本文なしは除外。`--include-bots` で含める）
- 議事録 Google Docs 6本（CLAUDE.md の表と同じ ID）を再取得し、**バイト単位で**現行 `raw/minutes/*.txt` と比較。変更があれば `raw/minutes/` を上書きし、新しく足された冒頭部分（新しい回）を抜粋。`--no-apply-minutes` で上書きを止められる
- 主要 8 リポジトリのリリース・コミット数・merged PR・新規 Issue
- Slack で共有された URL が wiki/ に既出か（✓/✗）と、wiki/log.md の直近エントリ

## 2. 読んで、未反映を判定する

report.md を上から読み、次の順で「Wiki に入れるべきか」を決める。

- **入れる**: リリース、方針決定、公開物（記事・ページ・データセット）、戦略会議のまとめ、プロジェクトの現況説明、新しい論点の議論、外部との協働
- **入れない**: 私的な雑談、自己紹介、会議リマインダー、外部イベントの単なる告知、bot 通知。Slack の私的発言は wiki に持ち込まない（CLAUDE.md）
- URL が ✓ でも内容が薄いことはある。✗ の URL は、それを共有した発言ごと取り込み候補になる
- 議事録に「変更あり」が出たら、抜粋された冒頭部分（新しい回）を読む。冒頭に追記がなく本文編集だけの場合は `diff` で確認: `diff work/catch-up/<日付>/minutes/<name>.txt` と比べるのは git 上の旧版 `git show HEAD:raw/minutes/<name>.txt`
- 議事録の回が長い（提言書本文などが貼られている）ときは、回の単位でサブエージェントに分けて読ませてよい。ファイルの担当を重ねない

## 3. 反映する

- 更新先の目安: プロダクトの動き → `wiki/entities/<project>.md` の「開発の歩み」末尾、議事録 → `wiki/sources/<minutes>.md` と関連 entity、会議 → `wiki/events/YYYY-MM-DD-*.md`、横断的な議論 → `wiki/topics/`、月の出来事 → `wiki/timeline/quarterly-summary.md`
- 新ページを作ったら `wiki/index.md` に登録。触ったページは `updated:` を今日にする
- 出典は `sources:` と本文に書く（Slack は `digitaldemocracy2030/slack-logs` の `mirror/slack/<channel_id>.jsonl.gz`、議事録は `raw/minutes/<name>.txt`）
- `wiki/log.md` の先頭に `## [YYYY-MM-DD] ingest | 要約` を追加し、取り込んだもの・**取り込まない判断をしたもの**・未読で残したものを書く。次回の `--since` の起点になる
- 差分が何もなければ、その旨をユーザーに伝えるだけでよい。log.md に「差分なし」を書く必要はない

## 4. 検証してコミット

```bash
pnpm build && pnpm check:pages-links
```

- 赤リンクが出たら概念ページを作るかリンクを外す（既存の赤リンクが拾われることもある）
- stage は触ったパスだけ明示（`git add -A` 禁止、`.claude/settings.local.json` は stage しない）。Slack/GitHub 由来の編集なので staged diff に secret らしき文字列がないか確認
- コミットメッセージは `docs: ...`、末尾に `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`
- この wiki は PR を作らず main に直接 push してよい（2026-10-31 に nishio が指示）。他のリポジトリには適用しない

## 5. ユーザーへの報告

日本語で、「何が新しく分かったか」「Wiki のどこを更新したか」「取り込まなかったもの・未読のもの」の3点。差分なしの議事録は表にして一行で済ませる。
