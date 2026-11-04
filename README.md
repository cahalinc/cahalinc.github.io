# カハール株式会社 公式サイト

静的サイト（手順RAG / Experiment OS / BioSpatial OS / Auto Lab Loop）。
各ページは自社製品・公開アプリへの紐づけを前提にしています。

## 主なページ

- `index.html` — トップ（技術層 → 製品 → 受託）
- `products.html` — 製品一覧（#protocol / #experiment / #biospatial / #autolab）
- `services.html` — 受託開発（自社スタック延長のバイオインフォ / フィジカルAI）
- `about.html` — 会社概要
- `message.html` — 代表挨拶
- `contact.html` — お問い合わせ
- `history.html` — 会社変遷（フッターから）
- `blog.html` — 調査メモ（フッターから）
- `members.html` — `message.html` へのリダイレクト
- `tech.html` — products.html へのリダイレクト
- `tools/studio.html` — SNS Content Studio（biolab_UI marketing 資産）

## 調査メモ

`blog/` 配下は、次のリポジトリで読んだ内容・整理した内容をサイト向けに書き直したものです。

| 記事 | 元リポジトリ |
|------|-------------|
| 実験自動化 4分類 / Auto Lab Loop / 手順 RAG | `biology_resarch` |
| Experiment OS | `biolab_UI` |
| BioSpatial OS | `biospatial` |

他社論文の転載や、他社成果の自社実績化はしません。出典がある場合は各記事内に書きます。

## ローカル確認

```bash
python3 -m http.server 8765
```

## 技術資産の参照元

- `biology_resarch` — 手順 RAG / Autolab 公開面
- `biolab_UI` — Experiment OS
- `biospatial` — BioSpatial OS

## プロジェクトページ

会社本体はこのリポジトリ。Autolab Loop のビジョン・公開導線は別ホストのプロジェクトページです。

- [Autolab Loop プロジェクトページ](https://biolablooper.github.io/) — ソース: [`biolablooper/biolablooper.github.io`](https://github.com/biolablooper/biolablooper.github.io)
