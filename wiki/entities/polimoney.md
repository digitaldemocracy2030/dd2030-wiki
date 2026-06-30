---
title: Polimoney
aliases: [Polimoney]
tags: [dd2030, product, polimoney]
sources:
  - raw/minutes/polimoney.txt
  - raw/minutes/weekly-general-meeting.txt
  - raw/history/week25_20250903/polimoney.md
  - raw/history/week26_20250910/polimoney.md
created: 2026-04-18
updated: 2026-06-30
---

# Polimoney

## 概要

**Polimoney（ポリマネー）** は、政治資金収支報告書をAI（Gemini）でOCR解析し、政治資金の流れを可視化するツール。「政治資金の問題がなくなる2030年」を目指すdd2030のプロダクトの1つ。

ブランド名は2025年8月にコミュニティ投票で「Polimoney」に決定。

## ビジョン

政治資金がどんな目的で使われているかを見える化し、政治団体・政治家がどのような方向を目指しているかを伝えるコミュニケーションチャネルとなること。

## 3ペルソナ（2025年5月確定）

- **ライト**（政治関心低め）: 見る・シェア・いいね
- **ミドル**（インフルエンサー・応援者・会計担当）: 比較・議論
- **ヘビー**（会計士・議員）: ダッシュボードカスタム・ダウンロード・API

## 主要機能

### 政治資金の可視化（polimoney.dd2030.org）
- 政治資金収支報告書のPDF→Gemini OCR→JSON→可視化パイプライン
- サンキー図等による支出の可視化
- シェアボタン・OGP対応

### 選挙運動費用収支報告書
- 政治資金収支報告書（政治団体・年次）とは別に、個人単位の選挙ごとの報告書に対応
- 2025年8月に和歌山県議・岩永さんとの接触で重要性が判明
- Excel→JSON化を実施（和歌山・東京データ）
- [[topics/political-funds-and-campaign-expenses|政治資金収支報告書と選挙運動費用収支報告書]] の違いが、データ構造・公開範囲・Ledger設計の前提になった

### Ledger（会計ソフト）
- 政治家が自分で収支入力できる専用ソフト
- 複式簿記の仕訳入力、年度締め、団体・選挙台帳
- 仕訳承認時にHub（公開サイト）へ自動同期
- SaaS方式: Supabase Cloud + Deno Deploy + Stripe
- 2026年3月末時点で仕訳承認時のHub自動同期や領収書ダウンロードなどの骨格ができ、2026年4月にはUI/UX、政治家・政治団体の承認画面、岩永さんの選挙運動費用データ公開準備が継続していた

## 技術スタック

| 項目 | 技術 |
|------|------|
| OCR | Google Gemini AI |
| バックエンド | Python（FastAPI）※Go→Pythonに変更（2025年10月） |
| フロントエンド | Deno Deploy |
| DB | Supabase Cloud（PostgreSQL + RLS） |
| 認証 | Supabase Auth ※Auth0から変更（2026年1月） |
| インフラ | Azure Container Apps |
| 会計ソフト | Flutter（Windowsデスクトップアプリ） |
| リポジトリ | `polimoney`（フロント）+ `polimoney_hub`（バックエンド統合）+ `polimoney_ledger`（会計） |

## チームメンバー

| 名前 | 役割 |
|------|------|
| モアイ（小野翔太） | 開発マネジメント・Ledger実装・全体設計 |
| shimizu（清水） | バックエンド（FastAPI）・Azure・OCR・選挙運動費用JSON化 |
| tagusa（田草） | フロントエンド（サンキー図・URL設計） |
| 衣笠千絵子 | マーケ・記事作成・インタビュー |
| みたらし | PO・渉外連携窓口 |
| 足立さん | PO・公認会計士 |
| 中村さん | 会計ソフト要件定義・顧問的役割 |
| 太田さん | 渉外担当（2025年9月〜） |

## ロードマップ（2025年7月確定）

1. STEP1（〜9/15）: シェア・公認バッジ
2. STEP2（〜12/15）: 専用会計ソフト開発
3. STEP3（〜3/15）: Polimoneyから寄付可能に
4. STEP4（〜6/15）: 複数政治団体合算表示
5. STEP5（〜9/15）: 人と人の比較機能
6. STEP6（〜12/15）: データDL・API公開

## チームみらいとの関係

2025年8月にMTGで棲み分けを確認:
- **チームみらい**: 「支出と収入をタイムリーに公開」優先。既存クラウド会計API利用
- **DD2030 Polimoney**: 「会計ソフトで収支報告書を作る」優先。専用ソフト開発

競合ではなく協働が基本姿勢。専門知の提供・具体的会計データ例を共有する関係。

## 利用事例

- **出井亮輔（いでいさん、自民党）**: 最初の活用事例（2025年4月）
- **岩永さん（和歌山県議）**: 選挙運動費用収支報告書のパイロットユーザー
- **[[events/2026-01-09-burikaigi-polimoney|ぶり会議2026]]**: haruki shimizu氏が登壇し、Polimoneyをエンジニア向けに紹介（2026年1月9日）

## もっと詳しく

- [[sources/polimoney-minutes|Polimoney 議事録]] — 開発定例・ロードマップのWiki内ソース要約
- [[sources/weekly-general-meeting|週次全体定例 議事録]] — 全体定例側の進捗共有
- [Polimoney GitHubリポジトリ](https://github.com/digitaldemocracy2030/polimoney) — ソースコード
- [Polimoney 公開サイト](https://polimoney.dd2030.org/) — 実際の政治資金可視化ページ
- [Polimoney 議事録（Google Docs）](https://docs.google.com/document/d/19Kn6ekK3twMVcVaSyUgptvmfzrXEJezA6GXTbPXjm9M) — 定例会の議事録

## 関連ページ

- [[overview]] — プロジェクト全体の概要
- [[topics/political-funds-and-campaign-expenses|政治資金収支報告書と選挙運動費用収支報告書]] — Polimoneyで扱う2種類の書類の違い
- [[events/2025-04-12-1day-meetup|1Day Meetup（2025-04-12）]] — 初期にPolimoneyが共有されたイベント
- [[events/2025-05-25-meetup-2|デジタル民主主義2030 MEETUP #2]] — Polimoneyの設計思想の着地点が扱われたイベント
- [[events/2025-07-18-meetup-3|デジタル民主主義2030 MEETUP #3]] — 各プロダクト紹介の一部として接続するイベント
- [[events/2026-01-09-burikaigi-polimoney|ぶり会議2026 Polimoney登壇]] — Polimoneyを外部のエンジニア向け文脈へ説明したイベント
- [[sources/history-week43-20260114|週次History week43（2026-01-14）]] — Polimoneyの外向け発信強化を確認できる個別週ソース
- [[sources/history-week50-20260415|週次History week50（2026-04-15）]] — データ整備完了とUI/UX改善論点を確認できる個別週ソース
- [[時系列まとめ]] — 四半期ごとの活動記録
- [[初年度まとめ]] — 立ち上がりから1年の詳細な時系列
- [[主要メンバー]] — プロジェクトの主要な人物
- [[コミュニティと法人の関係]] — OSSコミュニティと法人の役割分担
