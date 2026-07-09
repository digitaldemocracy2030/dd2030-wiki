---
title: Wiki保守運用
aliases: [Wiki保守運用, wiki-maintenance, Wiki運用チェックポイント]
tags: [dd2030, tooling, wiki, operations]
sources:
  - AGENTS.md
  - CLAUDE.md
  - PLAN.md
created: 2026-06-30
updated: 2026-07-09
---

# Wiki保守運用

dd2030 Wiki を継続更新する時の、作業開始と完了のチェックポイント。

## 大きな改善後は先に安定化する

ページ追加や横断修正が広がったら、次の改善に進む前にブランチ化し、検証して、コミットまたはPRへまとめる。未整理の大きな差分を抱えたまま新しいソース取り込みを始めると、根拠の混線とレビュー困難が起きる。

2026-06-30の初見導線・ソース網羅改善では、`codex/stabilize-wiki-improvements` で検証後にコミットし、draft PR #1へまとめた。以後も同程度の広い差分は、作業単位を切って安定化してから次に進む。

## コミット前の確認

- `raw/` と `content/` を触っていないか確認する。例外はユーザーが明示した場合のみ。
- `.claude/settings.local.json` はローカル設定で、token らしき値を含むことがあるため staging しない。
- `git add -A` ではなく、今回の file-back / wiki 更新で触ったパスだけを明示して stage する。
- Slack、GitHub、archive、workflow まわりを編集した時は、staged diff に secret らしき文字列が入っていないか追加確認する。

## 検証

Wiki本文、目次、リンク、検索スクリプトを触った場合は、少なくとも以下を実行する。

```bash
python3 scripts/lint-wiki.py
git diff --check
python3 -m py_compile scripts/search-archive.py
pnpm build && pnpm check:pages-links
```

`PLAN.md` だけの更新なら `pnpm build` は必須ではない。ただし `wiki/` の本文やリンクを触った場合は、Quartz build と Pages link check まで通してからコミットする。

## 次に見る観点

安定化後の優先作業は `PLAN.md` を見る。2026-06-30時点では、イベントページの追加よりも、根拠確認できるものを選び、古い予定表現を日付つきの記録へ直すことを優先する。

## 関連ページ

- [[index]] — Wiki全体の目次
- [[dd2030-wiki の dd2030 org 移行]] — Wiki本体をorg側へ移す時に旧URLを守る作業メモ
