---
title: Civic AI（6-Pack of Care）
aliases: [Civic AI, シビックAI, 6-Pack of Care, 6pack.care, Kami, ケアの6原則]
tags: [dd2030, concept, plurality, care, audrey-tang]
sources:
  - https://mutimoumai.hatenablog.com/entry/2026/08/16/043931
  - https://www.lesswrong.com/posts/anoK4akwe8PKjtzkL/plurality-and-6pack-care
  - https://audreyt.org/dd
created: 2026-08-18
updated: 2026-08-18
---

# Civic AI（6-Pack of Care）

**Civic AI** は、[[オードリー・タン]]（Audrey Tang）とキャロライン・エマー（Caroline Emmer、オックスフォード大学AI倫理研究所リサーチディレクター）による研究プロジェクト。「単一の巨大なAIで社会を統治する」のではなく、**コミュニティごとにローカルなAIを運用・管理する**という設計思想を中核に置く。このローカルAIを **Kami**（knowledge artefact management intelligence）と呼ぶ。

初めての人向けに言い換えると、「一つの正解AIをみんなに配る」のではなく、「それぞれのコミュニティが、自分たちのケアの基準に沿って小さなAIを育て、期限が来たら手放す」という考え方。dd2030が取り組む[[ブロードリスニング]]が「声をどう集めて可視化するか」を扱うのに対し、Civic AIは「集めた声をどう意思決定に接続し、結果を話し手へ返し、その健全さをどう測るか」という**関係の設計**に重心がある。

## 思想的背景

- **Plurality（多元性）**: 「社会的差異を超えた協力のための技術」。関係の健全性を重視する立場。[[オードリー・タン]]と[[グレン・ワイル]]らが体系化した考え方で、dd2030の活動全体の底流にある。
- **ケアの倫理（ジョーン・トロント）**: ケアを「私たちがこの世界で可能なかぎり良く生きられるよう、世界を維持し、継続させ、修復するために行うあらゆる活動」と定義する。Civic AIはこのケア概念を6つの原則に分解している。

## 6-Pack of Care（ケアの6原則）

各原則には測定指標が対応する。特徴は「**最大化が目的ではなく、コミュニティが定めた閾値を超えていれば十分**」とする点。

1. **Attentiveness（注意深さ）** — 困っている人のニーズを把握する
2. **Responsibility（責任）** — 検証・異議申し立てが可能な約束を形成する
3. **Competence（有能さ）** — シャドーモード → カナリアリリース → 一般展開という段階的な実行
4. **Responsiveness（応答性）** — ケアが実際に届いたか確認し、届いていなければ修復を試みる
5. **Solidarity（連帯）** — 複数のKami間でwin-winを構築する
6. **Symbiosis（共生）** — Kamiが永続的な権力にならないよう時間制限を設ける

「ケアは、一人ひとりの内側ではなく、私たちの『あいだ』で測る」という主題は、[[events/2026-08-02-digital-democracy-summit|デジタル民主主義サミット2026]]の閉会スピーチ「ループを、閉じる」で示された、声が意思決定へ接続され結果が話し手へ返る**循環**の考え方と接続する。

## 実践面

- `civic.ai` のサイト上の指示に従ってセットアップできる。
- Kamiは**プロンプトベースで自然言語で構築**されるため、使用するモデルやプロンプト内容によってKamiの性質が変わる。

## dd2030との関係

Civic AI自体はdd2030のプロダクトではなく、[[オードリー・タン]]らの海外研究プロジェクト。ただし、[[events/2026-08-02-digital-democracy-summit|デジタル民主主義サミット2026]]の閉会でタンが提示した「閉じたループ」の議論と地続きであり、dd2030が扱う[[ブロードリスニング]]・[[熟議民主主義]]の「声の循環」を、AIガバナンスの原則として言語化したものと読める。

## 参照

- [[sources/civic-ai-6pack-of-care-blog|Civic AI「6-Pack of Care」解説ブログ]] — このページの主な出典（コミュニティメンバーによる外部ブログ）
- [オードリー・タン「Plurality & 6pack.care」（LessWrong）](https://www.lesswrong.com/posts/anoK4akwe8PKjtzkL/plurality-and-6pack-care)
