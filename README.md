# KM1 デザインシステム / KM1 Design System

KM1 は、自分が作る道具（アプリ・Web・スライド・PDF）の見た目と使い勝手をそろえるための標準である。目的は使いやすさを上げること。適当に作るとひと目で AI が作ったと分かる画面になり、使う人の嫌悪感につながるので、形の 1 つ 1 つに理由を持たせる。
*KM1 keeps the look and usability of its author's tools (apps, web, slides, PDFs) consistent. Its purpose is usability: careless design reads at a glance as AI-made and puts people off, so every form carries a reason.*

**位置づけ / Status:** KM1 は個人の標準で、特定の企業・団体の承認を受けたものではない。ライセンスは MIT（`LICENSE`）。第三者の素材の扱いは「表記とライセンス」（`notices.md`）。
*A personal standard, not endorsed by any company or organization. MIT-licensed (`LICENSE`); third-party terms in `notices.md`.*

説明は日本語を主、英語を従とする。数値と単位の間は半角あける。
*Japanese first, English second; a half-width space between a number and its unit.*

## KM1 の軸 / The axes

**前提はアクセシビリティ。軸は「見やすい」「わかりやすい」「理由を言える」の 3 つ。** 迷ったら、アクセシビリティ → 見やすい → わかりやすい → 個性 の順で決める。KM1 は 2 層でできていて、土台は確立した規則に従って個性を抑え、その上の味付けの層で KM1 らしさを出す。詳しくは「原則」（`principles.md`）。
*Accessibility is the premise; the axes are easy to see, easy to understand, and every form has a reason. Decide in the order accessibility → legibility → understandability → personality. A base layer follows established rules; a flavor layer carries KM1's character. See Principles.*

## 読む順 / How to read

KM1 は上から順に「何を作るか → 画面 → 部品 → 値」の 4 層でできている。新しい製品は「プロダクトデザイン」の型を埋めてから下へ進む。
*Four layers, top down: what to build → screens → components → values. Start a new product from the Product design template and work down.*

| 章 / Chapter | ファイル / File | 中身 / Contents |
|---|---|---|
| 原則 / Principles | `principles.md` | 目的・前提・3 つの軸・優先の順番・土台と味付け・従う規格 |
| プロダクトデザイン / Product design | `product.md` | 使う場面 → 要求 → 形 → 確かめる、の進め方と記入用の型 |
| 画面の組み立て / Patterns | `patterns.md` | わかりやすさ・画面幅・移動・画面の型・フォーム・状態・待ち時間・動き |
| 部品 / Components | `components/README.md` | 部品のカタログ（各部品の `README.md` に使い方と理由、見本の画像つき）。PDF は別冊「部品カタログ」 |
| 言葉 / Writing | `content.md` | 文言・敬体・実行しない側の言葉・数字と日付の書き方 |
| 基礎 / Foundations | `tokens.md` | 色・文字・余白・角丸・影・線・状態・密度・操作領域・書体 |
| アイコン / Icons | `icons.md` | KM1 のアイコンの中身・使い方・描き方、ロゴと表示バッジ |
| プラットフォーム / Platforms | `platforms.md` | Web・Flutter・WinUI 3・Compose・SwiftUI での使い方と端末ごとの作法 |
| グラフ / Charts | `dataviz.md` | グラフとデータの見せ方（提案） |
| PDF / PDF documents | `documents.md` | 画面のない文書の規定（KM1-DOC-001） |
| Word と PowerPoint | `office.md` | 文書（KM1-DOC-002）とスライド（KM1-DOC-003）の規定 |
| 運用 / Governance | `governance.md` | 判断の記録・変え方・互換性・期限・理由の確認 |
| 検証 / Verification | `verification.md` | 自動の検査の流し方と記録、実機・読み上げの手順 |
| 対応表 / Coverage | `coverage.md` | 部品ごとの Web・Flutter・ネイティブの対応 |
| 適用記録 / Adoption | `adoption.md` | 製品への適用と、足りなかったものの台帳 |
| 仕様案 / Proposals | `proposals.md` | まだ採用していない部品と値の案 |
| 表記とライセンス / Notices | `notices.md` | KM1 と第三者の素材のライセンス、外に配るときの文言 |
| 記録 / Records | `m1.md`・`changelog.md` | 過去の統合仕様と変更履歴 |
| 変更の進め方 / Contributing | `CONTRIBUTING.md` | 変更・公開（Release）の手順 |

## すぐ使う / Quick start

- **Web（React）:** `tokens.css` と `components/bundle.css`・`components/bundle.js` を読み込む。見本のある部品 50 個（公開している部品は全部で 60 個）と、フォームの状態をまとめる `useForm`、選択の状態をまとめる `useSelection` を `window.Fluent2` に収録。
  *50 components with previews (60 exported in total) plus the `useForm` and `useSelection` hooks live in `window.Fluent2`.*
- **React を使わない単体の HTML:** `tokens.css` と `bundle.css` のクラスだけで組める。手順は「プラットフォーム」の「Web」。
  *Plain HTML works with `tokens.css` and the `bundle.css` classes; see Platforms › Web.*
- **Flutter:** `km1_theme.dart`（テーマ）と `km1_widgets.dart`（KM1 専用の部品）を入れ、`MaterialApp(theme: Km1Theme.light(), darkTheme: Km1Theme.dark())`。詳しくは「プラットフォーム」の「Flutter」。
  *Add `km1_theme.dart` and `km1_widgets.dart`; details in Platforms › Flutter.*
- **WinUI 3・Jetpack Compose・SwiftUI:** `KM1.xaml`・`Km1Theme.kt`・`KM1Theme.swift`（テーマだけ。実験的）。
  *Themes only, experimental.*
- **Word・PowerPoint・PDF:** `dist/` のひな形（`KM1_文書.dotx`・`KM1_スライド.potx`）と、`office/`・`pdf/` の道具。
  *Templates in `dist/`, tools in `office/` and `pdf/`.*
- **値を変える:** `tokens.json` が正本。直したら `gen/` の道具で生成物を作り直し、`bash gen/check_all.sh` で全部の検査を流す（「検証」）。
  *`tokens.json` is the source of truth; regenerate and run `bash gen/check_all.sh` (see Verification).*

## ファイル / Files

| 場所 / Path | 内容 / Contents |
|---|---|
| `tokens.json` / `tokens.css` | トークン（正本は JSON、CSS は生成物） |
| `dist/tokens/` | W3C Design Tokens（DTCG）形式のトークン。ライトとダークで 1 ファイルずつ（生成物） |
| `components/` | Web の部品（各部品の `README.md` と `preview.html`、`bundle.css`・`bundle.js`・`index.d.ts`）と部品カタログ `components/README.md` |
| `km1_theme.dart` / `km1_widgets.dart` | Flutter のテーマと KM1 専用部品 |
| `KM1.xaml` / `Km1Theme.kt` / `KM1Theme.swift` | WinUI 3・Jetpack Compose・SwiftUI のテーマ |
| `icons/` | アイコンの元データ・生成物・フォント（`km1-icons.json`、`sprite-20.svg`、`km1_icons.dart`、`km1_icons_b.dart`、`KM1Icons.ttf`）と一覧の図 `icon-list.svg` |
| `assets/tokens/` | トークンの見本の図（「基礎」に掲載） |
| `brand/`・`dist/logo/` | ロゴと表示バッジの生成の道具と、SVG・PNG |
| `dist/` | 配布物: デザイン標準と部品カタログの PDF、`KM1_icons.zip`、Word・PowerPoint のひな形と見本、表示バッジの PowerPoint、グラフの模様 |
| `office/` | Word・PowerPoint のひな形を作る道具と検査 |
| `pdf/` | PDF のひな形・印刷用 CSS・仕上げと検査の道具 |
| `gen/` | 生成と検査の道具（`check_all.sh` が入口） |
| `verify/` | Windows 実機用の検証セット |
| `*.md` | 本編の文書（上の「読む順」） |

**ライセンス / License:** KM1 は MIT License（`LICENSE`）。アイコンを配るときは、もとにした絵のライセンス `LICENSE-Fluent.txt` も一緒に付ける（「表記とライセンス」）。
*KM1 is MIT-licensed (`LICENSE`). Ship `LICENSE-Fluent.txt` with the icons (see Notices).*
