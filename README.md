# KM1 デザインシステム / KM1 Design System

| 場所 / Path | 内容 / Contents |
|---|---|
| `dist/` | 配布物: デザイン標準と部品カタログの PDF、`KM1_icons.zip`、Word・PowerPoint のひな形と見本（.dotx/.docx/.potx/.pptx）。作り直しの順: `cd gen && npm i` → `node gen/shoot_previews.js <render_previews.py の出力> components` → `python3 gen/catalog_md.py` → `node gen/token_sheets.js` → `python3 icons/icon_sheet.py` → `python3 gen/build_pdf.py dist`（寸法と件数の検査を通してから 2 冊を作る）。Office は `office/`、アイコン一式は `icons/build_all.py` |
| `components/README.md` | 部品カタログ（グループ別、ライトとダークの見本の画像つき。`gen/catalog_md.py` で作る） |
| `assets/tokens/` | トークンの見本の図（色のライト・ダーク、文字、余白、角丸、影、大きさ。`gen/token_sheets.js` で作る。`tokens.md` に掲載） |
| `verify/` | Windows 実機用の検証セット（`make_kit.py` で本体の今のファイルから組み立て、`verify.ps1` で実行） |
| `icons/icon-list.svg` | アイコン一覧の図（`icons/icon_sheet.py` で作る。`icons.md` §4 に掲載） |
| `*.md` | 本編の文書（原則・画面の組み立て・プロダクトデザイン・プラットフォーム・トークン・アイコン・文書・運用・検証・変更履歴など） |
| `tokens.json` / `tokens.css` | トークン（正本は JSON、CSS は生成物） |
| `components/` | Web の部品（各部品の `README.md` と `preview.html`、`bundle.css`・`bundle.js`・`index.d.ts`） |
| `km1_theme.dart` / `km1_widgets.dart` | Flutter のテーマと KM1 専用部品 |
| `KM1.xaml` / `Km1Theme.kt` / `KM1Theme.swift` | WinUI 3・Jetpack Compose・SwiftUI のテーマ |
| `icons/` | アイコンの元データ・生成物・フォント（`km1-icons.json`、`sprite-20.svg`、`km1_icons.dart`、`km1_icons_b.dart`、`KM1Icons.ttf`） |
| `office/` | Word・PowerPoint のひな形を作る道具と検査 |
| `pdf/` | PDF のひな形・印刷用 CSS・仕上げと検査の道具 |
| `gen/` | 生成と検査の道具（トークン、Dart、ネイティブ、書体、数の同期、運用期限など） |

アイコンは KM1 B 案で、KM1 が描いたものです。もとにした絵は Fluent System Icons（Microsoft、MIT）です。ライセンスは `LICENSE-Fluent.txt`。
*The icons are KM1's B style, drawn by KM1, based on Fluent System Icons (Microsoft, MIT); see `LICENSE-Fluent.txt`.*

---

KM1 は Microsoft Fluent 2 の構造に、Science Tokyo と EPSON の考え方、デジタル庁デザインシステムの部品の使い方を重ねた標準デザインシステム。Google / Material 風の表現（大きな丸み、FAB、tonal 面）は使わない。判断の軸は「デザイン原則」セクションにある。
*KM1 layers the thinking of Science Tokyo and EPSON, and the Digital Agency design system's component usage, onto the Fluent 2 structure. Avoid Google / Material styling (large radii, FABs, tonal surfaces). The axes of judgment are in the Design principles section.*

説明は日本語を主、英語を従とする。値は公開されている Fluent 2 Web のトークンと、KM1 のメインカラー `#10218B`（EPSON の青を参考にして選んだ紺）を基にしている。アレンジを加えたら tokens.json と本文を更新する。
*Documentation is Japanese first, English second. Values come from the public Fluent 2 Web tokens and KM1's main color `#10218B`, a navy chosen with Epson's blue as a reference. When you adapt it, update tokens.json and this text.*

**位置づけ / Status:** KM1 は個人の標準で、Microsoft、Science Tokyo、Seiko Epson、デジタル庁とは無関係であり、承認・認証を受けたものではない。出典の表記と帰属は `notices.md`（KM1-LIC-001）。
*KM1 is a personal standard, not affiliated with or endorsed by Microsoft, Science Tokyo, Seiko Epson or the Digital Agency. Attribution wording is in `notices.md` (KM1-LIC-001).*


**このシステムの読み方 / How to read this system:** KM1 は 4 層でできている。上から、プロダクトデザイン（何を誰のために作るか）→ 画面の組み立て（画面の分け方・移動・状態）→ 部品 → トークン。新しいものを作るときは「プロダクトデザイン」のセクションの型を埋めてから、下の層に進む。
*KM1 has four layers, top down: product design (what to build and for whom) → patterns (screens, navigation, states) → components → tokens. Start a new product by filling in the template in the Product design section, then move down.*

**運用と検証 / Governance and verification:** 採用・不採用・保留の記録と判断を変える手続き、互換性の決まり、出典の確認の状態は「運用の決まり」（`governance.md`）。実機・読み上げ・各 OS の検証の手順と記録は「検証」（`verification.md`）。見た目の判断には、別冊「KM1 部品カタログ」（`KM1_部品カタログ.pdf`、横向き、等倍の見本と説明）を使う。本編 `KM1_デザイン標準.pdf` と 2 冊で 1 組で、同じ版のものを一緒に使う。
*Decision log, change procedure, compatibility and source status: Governance. Local verification procedures and log: Verification. For visual review use the companion "KM1 Component catalog" (`KM1_部品カタログ.pdf`, landscape, true-size previews); it pairs with the main `KM1_デザイン標準.pdf` as a two-volume set of the same edition.*

**PDF・印刷物 / PDFs and print:** 画面のない文書は「PDF の規定」（`documents.md`、KM1-DOC-001）に従う。ひな形・仕上げ・検査の道具は `pdf/` にある。
*Documents without a screen follow "PDF documents" (`documents.md`, KM1-DOC-001); template, finishing and checking tools are in `pdf/`.*

**Word・PowerPoint:** Word の文書は KM1-DOC-002、スライドは KM1-DOC-003（`office.md`）に従う。ひな形（`KM1_文書.dotx`・`KM1_スライド.potx`）を作る道具と検査 `officecheck.py` は `office/` にある。
*Word documents follow KM1-DOC-002 and slides KM1-DOC-003 (`office.md`); template generators and `officecheck.py` are in `office/`.*

**補遺 / Supplements:** 部品の対応表は `coverage.md`（KM1-COV-001）、出典と帰属は `notices.md`（KM1-LIC-001）、グラフは `dataviz.md`（KM1-VIZ-001、提案）、不足領域の仕様案は `proposals.md`（KM1-PRP-001）、導入の記録は `adoption.md`（KM1-ADO-001）。
*Component coverage: `coverage.md`; notices: `notices.md`; charts: `dataviz.md` (proposed); spec proposals: `proposals.md`; adoption log: `adoption.md`.*

## トークンの二層構造 / Two-layer tokens

色は「原色」（`gray-*`、`brand-*`、`blue-*`、`red-*`、`green-*`、`orange-*`）と「意味づけ」（`surface`、`ink`、`brand` など）の二層。UI と実装は意味づけトークンだけを参照し、原色を直接使わない。ライトとダークの違いは、意味づけトークンが指す原色の違いだけで表す。
*Color has two layers: primitives (`gray-*`, `brand-*`, `blue-*`, `red-*`, `green-*`, `orange-*`) and semantic tokens (`surface`, `ink`, `brand`, ...). UI and code reference semantic tokens only. Light and dark differ only in which primitive a semantic token points to.*

余白にも用途別のエイリアス（`layout-section-gap`、`container-card-padding-*`、`collection-item-gap-*`）と、OS ごとの操作領域（`control-target-*`）がある。Card・Table・SortableList は密度（compact・regular・spacious）を持つ。決まりと影響の範囲は「トークン」（`tokens.md`、KM1-TOK-001）。
*Spacing also has role aliases and per-OS hit-area tokens; Card, Table and SortableList support density. See "Tokens" (`tokens.md`, KM1-TOK-001).*

## 内容の原則 / Content fundamentals

- 文言は簡潔で、動詞から始める。ボタンは「保存」「キャンセル」「追加」のように 2〜4 文字の動詞。「OK」「はい」だけのラベルは避ける。
  *Keep copy short and lead with a verb. Use short verbs such as Save, Cancel, Add; avoid bare "OK" or "Yes".*
- 実行しない側の言葉を使い分ける: 何も変えずに引き返すのは「キャンセル」、読むだけの画面を消すのは「閉じる」、前の画面に移るのは「戻る」、済んだ操作を無かったことにするのは「元に戻す」。「やめる」「中止」「取り消し」は使わない（何をやめるのかが文脈で変わるため）。操作そのものが予約などの取り消しのときは、実行する側を「予約を取り消す」のように対象つきで書き、実行しない側は「戻る」にする。
  *Words for not proceeding: "キャンセル" backs out with no change, "閉じる" dismisses a read-only view, "戻る" goes to the previous screen, "元に戻す" undoes a finished action. "やめる", "中止" and "取り消し" are not used, since what they stop depends on context. When the action itself cancels something (a booking), name the object on the confirming side ("予約を取り消す") and use "戻る" for the other.*
- 敬体（です・ます）を基本とし、UI ラベル・見出し・ボタンは体言止めか動詞の終止形。感嘆符、絵文字、キャラクター口調は使わない。
  *Use polite Japanese for sentences; labels, headings and buttons are nouns or dictionary-form verbs. No exclamation marks, emoji or character voices.*
- 英字は文頭のみ大文字（sentence case）。例: 「Add new item」。
  *English uses sentence case: "Add new item".*
- エラーは「何が起きたか＋どうすればよいか」を 1 文で。
  *Errors say what happened and what to do, in one sentence.*
- 状態は色だけで伝えず、必ず文言かアイコンを添える。
  *Never convey state by color alone; add a label or icon.*

## 視覚の基礎 / Visual foundations

- **色 / Color**: 面は `surface` を基準に `surface-subtle` → `surface-muted` → `surface-sunken` と奥へ。文字は `ink`、`ink-secondary`、`ink-tertiary`。メインカラーは `#10218B`（EPSON の青を参考にした紺。`brand`＝塗り、`brand-stroke`＝縁・下線、`brand-ink`＝文字・リンク）で、1 画面でプライマリボタンは 1 つ。ブランド塗りの上は `on-brand`。情報は `info-*`、ステータスは `danger` / `success-ink` / `warning-ink` と各 `-tint`。
  *Surfaces step back from `surface` to `surface-sunken`. Text uses `ink`, `ink-secondary`, `ink-tertiary`. The main color is `#10218B`, a navy inspired by Epson's blue (`brand` fills, `brand-stroke` edges and underlines, `brand-ink` text and links); one primary button per screen; `on-brand` on brand fills. Info uses `info-*`; status uses `danger`, `success-ink`, `warning-ink` with `-tint` backgrounds.*
- **タイポグラフィ / Typography**: UI の標準は `body-1`（14/20）。ボタンは `body-1-strong`。階層は `title-1` → `title-3` → `subtitle-1` → `subtitle-2`。書体は `<html lang>` で切り替える。`ja` は Noto Sans JP（フォールバック Hiragino Sans / Yu Gothic UI / Meiryo UI）で、Body 以外には `"palt" 1` を付ける。`en` は Segoe UI Variable → Segoe UI → Hind。**書体はゴシック体だけ。華美なセリフ体・行書や筆文字・手書き風・明朝体は使わない**（`tokens.md` 7 章、KM1-TYP-001）。Noto Sans JP と Hind は Google Fonts から読み込む。日本語の画面に混ざる英数字（「PDF」「10:00」「Wi-Fi」）は Noto Sans JP のままにし、`lang` を変えない（字形がそろい、読み上げも日本語の流れで自然）。英語の文や固有名詞の英語表記が 1 文以上続くときだけ、その要素に `lang="en"` を付ける（読み上げが英語の発音になり、書体も Segoe UI に切り替わる）。数字は `font-variant-numeric: tabular-nums` で桁をそろえる。
  *UI default is `body-1` (14/20); buttons use `body-1-strong`. The typeface switches by `<html lang>`: `ja` uses Noto Sans JP (fallback Yu Gothic UI / Meiryo UI) with `"palt" 1` on non-body styles; `en` uses Segoe UI Variable → Segoe UI → Hind. Sans-serif only: no ornate serifs, brush or script faces, or Mincho (`tokens.md` §7, KM1-TYP-001). Noto Sans JP and Hind load from Google Fonts. Latin letters and digits inside Japanese UI ("PDF", "10:00") stay in Noto Sans JP with no `lang` change; only a full English sentence or English proper name gets `lang="en"` on its element (English pronunciation and Segoe UI). Digits use `tabular-nums`.*
- **余白 / Spacing**: 4px 刻み。基本は 8px の倍数（8・16・24・32）。8 の倍数でない値は、使う場所を決めて使う。
  - 6・10px（`space-sm-nudge`・`space-md-nudge`）: コンパクトなコントロールの内側だけ。
  - 12px（`space-md`）: コントロールの内側（ボタンの左右・アイコンと文字の間）、カードの中の小さなまとまりの間、compact 密度のコンテナの内側（`container-card-padding-compact`）。
  - 20px（`space-xl`）: 大きめのカードの内側。
  - 基本の値（`space-*`）は変えない。用途別の名前（「トークン」の章）から使うと、どの規則で使っているかが分かる。
  *4px step; mostly multiples of 8. Off-grid values have fixed uses: 6/10px only inside compact controls; 12px inside controls, between small groups in a card, and as compact-density container padding; 20px for larger card padding. Base values are unchanged.*
- **角丸 / Radius**: 標準は `radius-md`（4px）。カード・Alert・ポップオーバーは `radius-lg`、ダイアログは `radius-xl`。`radius-circular` はバッジ・アバター・スイッチだけ。
  *Default `radius-md`; cards, alerts, popovers `radius-lg`; dialogs `radius-xl`; `radius-circular` only for badges, avatars, switches.*
- **影 / Shadow**: 面の高さを示すときだけ。静止カード `shadow-2`、ホバー `shadow-4`、メニュー `shadow-8`、ポップオーバー `shadow-16`、ダイアログ `shadow-28`。ダークでは影より `stroke` で境界を示す。
  *Only to show elevation. In dark, show edges with `stroke` instead.*
- **境界線 / Borders**: 装飾は `stroke` / `stroke-subtle`、操作できる要素は `stroke-strong`。`stroke` は Fluent 原典値で surface 上 3:1 に満たないため、操作の識別には使わない。
  *Decorative borders use `stroke` / `stroke-subtle`; interactive elements use `stroke-strong`. `stroke` is the Fluent source value and falls below 3:1, so never use it alone to identify a control.*
- **フォーカス / Focus**: `focus-ring` の 2px 実線を要素の外側 1px に出す。全テーマ・全面で 3:1 以上。
  *A 2px solid `focus-ring`, offset 1px; 3:1 or more everywhere.*
- **状態 / States**: すべての操作部品に hover・pressed・focus・disabled を定義する。hover は `surface-hover` / `brand-hover`（入力欄・選択肢の枠は `ink-secondary`）、pressed は `surface-pressed` / `brand-pressed`、disabled は `ink-disabled` とカーソル `not-allowed`。無効の実装は部品で分ける: ボタンは `aria-disabled`（Tab で届き、押しても何も起きない。理由を読み上げられる）、入力欄・選択肢（Checkbox・Radio・Switch・Select）は HTML の `disabled` 属性（Tab で届かない）。どちらも近くに理由を書く。
  *Every interactive part defines hover, pressed, focus and disabled. Hover uses `surface-hover` / `brand-hover` (field and option borders use `ink-secondary`); pressed uses `surface-pressed` / `brand-pressed`; disabled uses `ink-disabled` and cursor `not-allowed`. Disabled is implemented per component: buttons use `aria-disabled` (reachable by Tab, inert, reason can be read); fields and options (Checkbox, Radio, Switch, Select) use the HTML `disabled` attribute (not reachable by Tab). Always explain the reason nearby.*
- **選択時の縁 / Selected edges**: チェック・ラジオ・スイッチ・タブの選択表示の縁と下線は、塗り（`brand`）ではなく `brand-stroke` を使う。ダークでも背景に対して 3:1 以上を保つため。
  *Edges and underlines that show selection (checkbox, radio, switch, tab) use `brand-stroke`, not the `brand` fill, so they keep 3:1 against the background in dark too.*
- **モーション / Motion**: 色の変化 100ms、切り替え 150ms、出入り 200ms（Fluent 2 の duration）。動かすのは色・影・不透明度と 8px までの移動だけ。`prefers-reduced-motion` では止める。表は「画面の組み立て」セクション。
  *Color changes 100ms, toggles 150ms, enter/exit 200ms (Fluent 2 durations); only color, shadow, opacity and up to 8px of travel; stopped under `prefers-reduced-motion`. See the Patterns section.*
- **線の太さ / Stroke width**: 境界線は `stroke-thin`（1px）、フォーカス・選択の下線は `stroke-thick`（2px）、分類色の帯は `stroke-accent`（4px）。入力欄は四辺 1px で下辺だけ `stroke-strong`、フォーカスで下辺が 2px の `brand-stroke` になる。
  *Borders `stroke-thin` (1px); focus and selected underlines `stroke-thick` (2px); category bars `stroke-accent` (4px). Fields have a 1px border whose bottom edge is `stroke-strong`, turning into a 2px `brand-stroke` on focus.*
- **分類色 / Category colors**: `cat-*` の 18 色は、利用者が付ける分類のためだけの色。帯と淡い塗りにだけ使う。使い方は「画面の組み立て」セクション。
  *The 18 `cat-*` colors are only for user-assigned categories, as bars and tinted fills. See the Patterns section.*
- **色 × 模様 / Color × pattern** (KM1-COL-001): 分類は 18 色 × 8 模様の 144 通りで区別する。模様は文字の下に描かず、しるし・凡例・グラフの塗りだけに使う（`CategoryMark`・`CategoryLegend`）。
  *Categories use 18 colors × 8 patterns; patterns appear only in marks, legends and chart fills.*
- **画面幅・重なり順 / Breakpoints and layers**: `breakpoint-*`（480・640・1024・1366px、Fluent 2 の size class）と `layer-*`（Fluent 2 の zIndex）。
  *`breakpoint-*` (Fluent 2 size classes) and `layer-*` (Fluent 2 zIndex).*

## アイコン / Iconography

アイコンは **KM1 のアイコン**（KM1-ICO-001、「アイコン」の章と `icons/`）を使う。KM1 の名前で引く 1 つのセットで、通常表示（線と淡い面、`icon-ink`）も選択・強調の塗りの形（Filled）も、Alert の状態の記号も、すべて KM1 B 案で KM1 が描いた（もとにした絵は Fluent System Icons、Microsoft、MIT。144 個）。標準は 20px Regular（`icon-md`）、選択中・強調は Filled、小さな場所は 16px（`icon-sm`）、ナビゲーションと上部バーは 24px（`icon-lg`）、空の状態（`EmptyState`）だけ 32px（`icon-xl`）。色は `currentColor`。描き方は「アイコン」§8。Web は `Icon`、Flutter は `Km1Icons` と `Km1BIcon`、Office は SVG・PNG の素材集。絵文字は装飾に使わない。
*Use **KM1 icons** (KM1-ICO-001; see the Icons chapter and `icons/`): one set addressed by KM1 names, Regular (strokes + soft tint, `icon-ink`), Filled and the Alert status symbols are all drawn by KM1 in the B style (based on Fluent System Icons, Microsoft, MIT; 144 icons). 20px Regular by default, Filled for selected or emphasized, 16px in small places, 24px in navigation and top bars, 32px only in EmptyState; color `currentColor`. Drawing rules: Icons §8. Web `Icon`, Flutter `Km1Icons` and `Km1BIcon`, Office SVG/PNG pack. No emoji as decoration.*

**分かりづらいアイコンを避ける規則（KM1 独自） / Rules against unclear icons (KM1's own)**
- KM1 のアイコンにないアイコン集（Material Icons など）は混ぜない。足りないときは KM1 のアイコンに足す（Fluent にあれば取り込み、なければ描く）。Flutter でも `Km1Icons` を使い、`Icons.*` は使わない。
- 操作のアイコンには文言を添える。アイコンだけにしてよいのは、閉じる・検索・戻るなど意味が定着したものだけで、その場合も `aria-label`（Flutter は `semanticLabel`）とツールチップを付ける。
- 1 つの意味に 1 つのアイコンを割り当て、画面が変わっても変えない。
- 意味が曖昧になるなら、アイコンをやめて文言だけにする。
*Do not mix in other icon sets such as Material Icons; add missing icons to the KM1 set (import from Fluent, or draw). In Flutter use `Km1Icons`, never `Icons.*`. Operation icons carry a text label; icon-only is allowed only for well-settled meanings (close, search, back) and then needs `aria-label` (`semanticLabel` in Flutter) and a tooltip. One meaning, one icon, on every screen. If the meaning is unclear, drop the icon and use words.*

**Flutter への適用 / Flutter**
専用の出典はなく、`tokens.json` から生成した `km1_theme.dart`を使う（`ThemeData` と `ThemeExtension`）。Fluent の見た目を再現する既存パッケージ（`fluent_ui`）は使わない。Material は部品の土台として使うだけで、色・形・大きさはテーマで上書きする。
*No dedicated source: use `km1_theme.dart`, generated from `tokens.json` (`ThemeData` + `ThemeExtension`). The `fluent_ui` package is not used. Material is only the widget base; color, shape and size are overridden by the theme.*

使い方 / Usage:
`km1_theme.dart`（テーマ）と `km1_widgets.dart`（表・カレンダー・時間割・予定表など KM1 専用の 30 部品）をアプリに入れる。アイコンは `icons/km1_icons_b.dart`（通常表示の B 案）・`icons/km1_icons.dart`（字形。B 案の 1 色の形と塗りの形）・`KM1Icons.ttf` を入れ、pubspec の `fonts` に `family: KM1Icons` で登録する（`fluentui_system_icons` は不要になった）。アイコンのファイルは `km1_theme.dart` だけに頼り、`km1_widgets.dart` がなくても組み込める。
*Icons: add `km1_icons_b.dart` (regular B style), `km1_icons.dart` (single-color B glyphs, incl. Filled) and `KM1Icons.ttf`; the icon files depend only on `km1_theme.dart`.*
`MaterialApp(theme: Km1Theme.light(), darkTheme: Km1Theme.dark(), themeMode: ThemeMode.system)`。色は `Theme.of(context).extension<Km1Colors>()!.ink` のように意味づけトークンで取る。Flutter 3.27 以降が必要（`CardThemeData` などを使うため）。
*Colors come from semantic tokens, e.g. `Theme.of(context).extension<Km1Colors>()!.ink`. Requires Flutter 3.27+ (uses `CardThemeData` etc.).*

| KM1 トークン / Token | Flutter |
|---|---|
| 色（意味づけ 30 個）/ Semantic colors | `Km1Colors`（`ThemeExtension`）。`ink`→`inkSecondary` のように camelCase |
| `brand` / `on-brand` / `danger` | `ColorScheme` の `primary` / `onPrimary` / `error` にも入れてある |
| `space-*` | `Km1Space.md` など（double） |
| `radius-*` | `Km1Radius.md` など（double） |
| `shadow-*` | `Km1Shadow.shadow4`（`List<BoxShadow>`） |
| タイプスタイル / Text styles | `Km1Text.body1`、`Km1Text.body1Strong` など。`TextTheme` にも割り当て済み |
| 部品の高さ / Control height | `Km1Theme.light()` が端末で決める（Android 48dp、iOS・iPadOS 44pt、Windows・macOS 32px）。`Km1Theme.light(touch: true)` で Windows のタブレット姿勢なども 44px 以上にできる。詳しくは「プラットフォーム」 |
| 入力欄の文字 / Field text | スマホは 16px、PC は 14px（`bodyLarge` と `hintStyle` をテーマが切り替える） |
| `focus-ring` | ボタンの `side`（2px）、入力欄の `focusedBorder` |
| `breakpoint-*` | `Km1Breakpoint.lg` など。`Km1Breakpoint.useDialog(context)`、`useSidebar(context)` |
| 動き / Motion | `Km1Motion.faster` / `fast` / `normal`、`Km1Motion.easyEase` / `decelerate` / `accelerate` |
| `cat-*` | `Km1Category.teal` など、`Km1Category.all`、淡い塗りは `Km1Category.tint(color, brightness)` |
| `icon-*`・`stroke-*`・`dialog-width` | `Km1Size.iconMd` など |
| `brand-stroke` | 選択時の縁（Checkbox / Radio / Switch / Tabs の下線） |

**注意 / Notes**
- 無効ボタンは Flutter では `onPressed: null` が標準だが、KM1 は「無効にせず理由を示す」方針（Digital Agency）なので、なるべく有効のまま押したときに理由を出す。
- 入力欄は、Web 版の「下辺だけ強調」を `InputDecorationTheme` だけでは再現できないので、テーマでは四辺同じ枠にしてある。同じ見た目にしたいときは、スケジュール確認アプリのように専用の入力部品を作る。
- `Icons.*` は使わない。KM1 のアイコンは `Km1BIcon(Km1BIconName.…)` で出す（`Km1Icons.*` のフォントは Filled 用）。
- `NoSplash` にしているので、押した状態は色の変化（`surface-pressed`）だけで示す。
*Prefer leaving buttons enabled and explaining on press, per KM1's no-disable rule. Use `Km1BIcon(Km1BIconName.…)` (the `Km1Icons.*` font is for Filled), never `Icons.*`. Press feedback is a color change only (no ripple).*

## コンポーネント / Components

見本のある部品 50 個（公開している部品は全部で 60 個）と、フォームの状態をまとめる `useForm`、選択の状態をまとめる `useSelection` を `window.Fluent2` に収録。各ガイドは `components/<Name>/README.md`。
*50 components with previews (60 exported in total) plus the `useForm` and `useSelection` hooks live in `window.Fluent2`; guides are in `components/<Name>/README.md`.*

| 用途 / Purpose | 部品 / Components |
|---|---|
| 操作 / Actions | `Button`、`Link`、`Menu`、`Toolbar`、`Chip` |
| 入力 / Forms | `Input`、`Textarea`、`SearchBox`、`Select`、`Combobox`、`Checkbox`、`RadioGroup`、`Switch`、`TagPicker`、`Slider`、`SpinButton`、`FileUpload` |
| フォームの組み立て / Form layout | `FormGroup`（と `FormActions`）、`FormGrid`、`ConditionalField`、`ErrorSummary`、`useForm`。決まりは「画面の組み立て › フォーム」 |
| 移動 / Navigation | `Nav`、`Tabs`、`Breadcrumb`、`Pagination` |
| お知らせ / Feedback | `Alert`、`Toast`、`Progress`、`Spinner`、`Skeleton`、`EmptyState`、`Badge` |
| 重ねる・まとめる / Overlays and containers | `Dialog`、`Drawer`、`Popover`、`Tooltip`、`Card`、`Accordion` |
| データ / Data | `Table`（行の選択と一括操作）、`SortableList`、`Avatar` |
| 画面の例 / Screen patterns | 見本だけ（部品ではない）: `ScreenAddEvent`（一覧 → 追加）、`ScreenListEdit`（一覧・詳細・編集）、`ScreenOffline`（通信できないとき）。型の決まりは「画面の組み立て › 画面の型」 |
| 一覧と選択（KM1-M1-001）/ Lists and selection | `List`（`ListItem`・`ListSection`・`ListSectionHeader`）、`ContextualActionBar`（`useSelection`）、`ExpansionEditor`、`StepFlow`、`BottomSheet`、`ImageGrid`。選び方は「KM1 × M1」 |
| 日付と時刻 / Date and time | `Calendar`、`Timetable`、`TimeGrid`、`Input`（`type="date"`・`"time"`） |

未収録: 予定表（`TimeGrid`）の中で予定をドラッグして動かす操作、自由入力でタグを作る操作。どちらも、編集画面と選択肢の追加で代わりができる。Flutter 版は、`km1_theme.dart`（テーマ）と `km1_widgets.dart`（KM1 専用の 30 部品）。ほかは Flutter 標準の部品にテーマを当てる（対応表は「プラットフォーム」）。
*Not included: dragging events inside `TimeGrid` and creating free-text tags; the editor and option lists cover both. Flutter uses `km1_theme.dart` plus `km1_widgets.dart` (30 KM1 widgets); see Platforms for the mapping.*

**部品の高さと操作領域 / Control height and hit area:** 端末の操作方法で切り替える（Flutter の Android は 48dp。全端末の表は「プラットフォーム」セクション）。タッチ操作（スマホ・タブレット、CSS の `pointer: coarse`）は 44px（`space-target`、WCAG 2.2 の AAA 2.5.5）。マウス操作（PC）は 32px（`space-target-compact`、Fluent 2 の medium、WCAG 2.2 の AA 2.5.8 を満たす）。ボタンの small は PC で 24px・スマホで 44px、large は PC で 40px・スマホで 48px。切り替えは `components/bundle.css` の `--control-height` が自動で行う。文中のリンクは対象外。
*Switches by input method. Touch (phones, tablets; CSS `pointer: coarse`): 44px (`space-target`, WCAG 2.2 AAA 2.5.5). Mouse (PC): 32px (`space-target-compact`, Fluent 2 medium, meets WCAG 2.2 AA 2.5.8). Small buttons are 24px on PC and 44px on touch; large are 40px and 48px. `--control-height` in `components/bundle.css` switches automatically. Inline links are exempt.*

## 確認していること / What has been checked

### 利用シナリオと見直し（2026-11-13）/ Scenarios and review fixes

| 点検 / Check | 方法 / Method | 結果 / Result |
|---|---|---|
| 利用シナリオ 3 つ / scenarios | 予定を追加する・一覧から選んで編集する・通信が切れて戻る、をスクリプトで最初から最後まで操作（360・1366px のライト、1024px のダーク） | 18 項目すべて合格 |
| ボタンの並び / action order | Dialog・Drawer・BottomSheet を 360px と 1366px で開き、DOM の順と見た目の順を比較 | どれも一致（以前は 360px で不一致） |
| 表の行の種類 / table rows | compact で、表示専用の行・リンクのある行・選べる行の高さを PC とタッチで測定 | 表示専用だけ 25px に詰まり、ほかは 32・44px を保つ |
| 大量のデータ / large data | List・Table に 500〜5,000 行（「検証」の 4 章） | 2,000 行を超えると選択の反応が 200ms を超える。1 画面 500 行までの規則を追加 |
| 部品の数 / counts | `gen/sync_counts.py --check`（`inventory.json` から数える） | 文書の記述がすべて一致 |
| 手元で行う検証 / local checks | 手順と記録欄を「検証」にまとめた | 実機・読み上げ・各 OS のビルドは未実施 |

### 書体の点検（KM1-TYP-001、2026-11-14）/ Typeface check

| 点検 / Check | 方法 / Method | 結果 / Result |
|---|---|---|
| ソースの書体の指定 / source declarations | `gen/fontcheck.py`（CSS・JS・Dart・Kotlin・Swift・XAML・HTML） | 使わない書体 0。等幅の並びにあった Courier New（タイプライター風のセリフ体）を外した |
| Office のテーマ / Office themes | `gen/fontcheck.py`・`office/officecheck.py` | ひな形と見本の 4 つで、言語ごとの補助の書体に残っていた Office 既定の明朝・セリフ体・手書き風（新細明體・Times New Roman・Angsana New・MV Boli など）をゴシック系に置き換え、FAIL 0 |
| PDF の埋め込み書体 / PDF fonts | `gen/fontcheck.py`（`pdffonts`） | 2 冊ともゴシック系と等幅だけ |
| 描かれた書体 / rendered fonts | `gen/fontcheck_render.js`（Chrome、見本 175 ページ（ライト・ダーク）、文字ごとに実際の書体） | セリフ体・明朝・手書き風 0。ただしこの環境に日本語の明朝体がないため、和文が明朝に落ちることはここでは見つけられない |
| 道具 / tools | 検査と生成の道具を `gen/` に置いた（`KM1_PROJECT` でフォルダを指定できる） | — |

### トークンと密度（KM1-TOK-001）の点検（2026-11-13）/ Token and density check

headless Chrome だけで実施。実機・読み上げソフト・各 OS のビルドは未確認。
*Headless Chrome only; devices, screen readers and native builds not yet checked.*

| 点検 / Check | 方法 / Method | 結果 / Result |
|---|---|---|
| トークンの解決 / resolution | `tokens_check.py` で値と参照先を照合。見本で Card の余白・表の行の余白・並べ替えの間を実測 | 14 個すべて一致。密度ごとに 12/2/2・16/4/4・24/8/8px |
| ライト・ダーク / themes | 見本「Density」を両テーマで axe と目視 | 違反 0 |
| 操作領域 / targets | 3 つの密度で、ボタン・チェック・つまみの大きさと選べる行の高さを PC とタッチで測定 | すべて PC 32px・タッチ 44px 以上 |
| キーボード / keyboard | Tab で届く 42 個のフォーカスの見え方と大きさ（PC・タッチ） | 問題なし |
| 文字の拡大 / text resize | 200% 拡大（683px 相当）、文字の間隔の上書き（WCAG 1.4.12）、両方、320px | はみ出し・切れなし（視覚的に隠した読み上げ用の文字を除く） |
| 意図しない変化 / regression | 既定（regular）で全 65 の見本を、変更前後で画素比較（PC とタッチ） | 同じ。差が出た 5 つは動きのある部品で、アニメーションを止めると同じ |
| 回帰の自動検査 / axe | 60 の見本 × ライト・ダーク（120 ページ） | 違反 0 |
| 生成物 / generated | Flutter（構文と API 名）、Kotlin・Swift（構文）、XAML（xmllint） | 問題なし（ビルドは未実施） |

### フォーム（KM1-PAT-001）の点検（2026-11-13）/ Forms check

headless Chrome だけで実施。実機・スクリーンリーダーは未確認。
*Headless Chrome only; real devices and screen readers not yet checked.*

| 点検 / Check | 方法 / Method | 結果 / Result |
|---|---|---|
| 動き方 26 項目 / behavior | 見本フォームをスクリプトで操作（離れたら確かめる、直すと消える、送信で一覧とフォーカス、リンクで欄へ、条件表示でフォーカスを奪わない、読み上げ文、隠れた欄は検証しない・送らない、値が残る、相関チェック、送信中の表示、横スクロールなし、DOM 順＝見た目の順）/ scripted | 320・360・640・1023・1024・1366px（ライト）、360・1366px（ダーク）ですべて合格 / all pass |
| 2 列の条件 / two-column rule | 画面 500・1023・1024・1366px、入れ物 420px | 2 列になるのは 1024px 以上かつ入れ物 560px 以上のときだけ / only ≥1024px and container ≥560px |
| 自動検査 / axe-core 4.10 | 新しい 4 部品、送信後・条件表示後の状態も含む。1366px と 360px / incl. after-submit and revealed states | 違反 0 / 0 violations |
| 既存部品の回帰 / regression | 全 45 プレビュー × ライト・ダーク（90 ページ）を axe で再検査 / all 45 previews re-run | 違反 0、はみ出し 0 / 0 violations, no overflow |
| フォーカス表示と押せる大きさ / focus and target | Tab で届く全要素、PC とタッチ / every tabbable, PC and touch | 問題なし / no issues |
| 強制カラー / forced colors | CSS に `CanvasText` の規則を追加 | 表示の確認は未実施 / rendering not verified |

### アクセシビリティ点検（2026-11-12）/ Accessibility check

当時の全 40 部品のプレビューを、ライトとダークの両方で点検した（2026-11-12 時点の記録、追加した部品も同じ方法で点検。追加分では、パンくずのリンクの幅、ファイル選択のフォーカス表示、予定表の締め切りの重なりと高さ、終日の行の読み上げ名、ポップオーバーの属性、タグ欄の押せる範囲を直した）。
*All 40 component previews were checked in light and dark with the same method; additions needed fixes (breadcrumb width, file picker focus, timeline deadline overlap and height, all-day row naming, popover attribute, tag field hit area).*

| 点検 / Check | 方法 / Method | 結果 / Result |
|---|---|---|
| WCAG 2.2 A・AA の自動検査 / automated | axe-core 4.10（WCAG 2.0〜2.2 の A・AA と推奨ルール）。メニュー・ダイアログ・ツールチップ・カレンダーは開いた状態でも実施 / incl. open states | 違反 0。判定保留 3 種は、背景色をツールが読めないもの（色は計算で合格済み）/ 0 violations |
| リフロー 1.4.10 / reflow | 320px 幅で横にはみ出す要素を数えた / overflow at 320px | 0（表と時間割は決まりどおり枠内で横スクロール）|
| 文字の間隔 1.4.12 / text spacing | 行間 1.5・字間 0.12em・語間 0.16em を強制 / forced spacing | 切れていた時間割のコマとナビの文字を、折り返しに直した / truncation fixed |
| フォーカス / focus | 操作できる全要素に順にフォーカスし、届くか・2px 以上の枠が出るかを確認 / every focusable element | 全部品で届き、枠が出る / all pass |
| 操作領域 2.5.8・2.5.5 / target size | PC は 24px 以上、タッチ表示は 44px 以上か / 24px PC, 44px touch | タッチ表示の small ボタンの幅が 37〜38px だったので、最小幅を高さと同じにした / fixed |
| 強制カラー / forced colors | Windows のハイコントラスト相当で表示 / high-contrast emulation | カレンダーの選択日・タブ・ページ送り・ナビの選択中が見分けにくかったので、強調色で示すように直した / fixed |

未確認 / Not checked: スクリーンリーダー（NVDA・VoiceOver・TalkBack）での実際の読み上げ、スマホ実機、ブラウザの 200% 拡大での実操作、Flutter 版。自動検査で見つかるのは問題の一部だけなので、読み上げの確認は人が行う必要がある。
*Screen readers (NVDA, VoiceOver, TalkBack), real phones, real 200% browser zoom and the Flutter side. Automated tools catch only part of the problems; screen-reader behavior still needs a human check.*

- 部品が使う色の組み合わせ（最初の 12 部品の 30 組と、追加した部品の 18 組、時間割の分類色の淡い塗りの上の文字 18 色分）を、ライトとダークの両方で計算し、文字 4.5:1 と枠・アイコン 3:1 を満たす（不合格 0）。分類色 `cat-*` はこの確認の対象外で、3:1 に満たない色がある（「画面の組み立て」に一覧）。この確認でダークの選択表示が 2.23:1 だったため、上の「選択時の縁」を決めた。
  *The color pairs used by components (30 for the first 12 components, 18 for the added ones, plus text on the timetable tint for all 18 category colors) were computed in light and dark: 4.5:1 for text, 3:1 for borders and icons (0 failures; the `cat-*` category colors are outside this check and some are below 3:1, as listed in Patterns). The check found selection marks at 2.23:1 in dark, which led to the "Selected edges" rule above.*
- Tabs の矢印キー・Home・End、Dialog の Esc、無効ボタンの Tab 到達、Alert の閉じるボタンの大きさ、Menu のキー操作（開く・移動・端で折り返し・Esc でボタンに戻る・外側クリックで閉じる）、Table の並べ替えと `aria-sort`、Toast の閉じる、Chip の `aria-pressed`、Nav の `aria-current`、Calendar のキー操作（矢印・Home・PageUp/PageDown・`min` で止まる）、Tooltip（フォーカスで出る・Esc で消える・マウスで出る）、Pagination の省略と端の動きは、ブラウザで動作を確認した。
  *Exercised in a browser: Tabs arrow/Home/End keys, Dialog Esc, Tab reach of disabled buttons, the Alert close button, Menu keys (open, move, wrap, Esc returns focus, outside click closes), Table sorting with `aria-sort`, Toast dismissal, Chip `aria-pressed`, Nav `aria-current`, Calendar keys (arrows, Home, PageUp/PageDown, stopping at `min`), Tooltip (focus shows, Esc hides, hover shows), Pagination truncation and end behavior.*
- ネイティブ用の `KM1.xaml`（WinUI 3）・`Km1Theme.kt`（Jetpack Compose）・`KM1Theme.swift`（SwiftUI）は、文法チェックを通した。WinUI と Compose は、使ったキー・関数・引数が公式のソース（2026-11-12 時点）に実在することも照合した。SwiftUI はソースが非公開のため照合していない。どれも**ビルドは未実施**。
  *Native files passed syntax checks; WinUI and Compose names were matched against official sources (SwiftUI is closed source). None has been built.*
- Flutter の `km1_theme.dart` と `km1_widgets.dart` は、(1) Dart の文法チェック（構文エラー 0）と、(2) 使っているクラス・名前付き引数・メンバー・アイコン名が Flutter の安定版（2026-11-09 時点）のソースと `fluentui_system_icons` 1.1.294 に実在するかの照合（問題 0）を通した。この照合は、わざと入れた間違い 6 件のうち 5 件を見つけ、列挙型の値の間違い 1 件は見逃した。**型の確認とコンパイル（`flutter analyze`）は、この環境では Flutter を入れられないため未実施。**
  *Flutter files passed (1) a Dart syntax check and (2) a check that every class, named argument, member and icon name exists in Flutter stable (2026-11-09) and fluentui_system_icons 1.1.294. The check caught 5 of 6 planted mistakes (missing a wrong enum value). **Type checking and compilation were not possible here.***
- 未確認: スクリーンリーダーでの読み上げ、実機のスマホ、Flutter での実際の見た目。
  *Not checked: screen-reader output, real mobile devices, and how it actually looks in Flutter.*

## React を使わない単体 HTML で使う / Using KM1 in a single HTML file

1. `tokens.css`（`tokens.json` から自動生成した CSS 変数）と `components/bundle.css`（部品のクラス）を、`<style>` に貼る。`bundle.css` の最初の `@import` 行は、オフラインで使うなら外す（書体は端末の標準書体に落ちる）。
2. `<html lang="ja">` を付ける。ダークは `<html data-theme="dark">` で固定でき、付けなければ OS の設定に従う。
3. 部品は `bundle.css` のクラスをそのまま使う（例: `<button class="f2-btn f2-btn--primary">保存</button>`）。クラス名と構造は、各部品の `README.md` と `bundle.js` を見る。React は要らない。
4. 値を変えるときは `tokens.json` を直して `tokens.css` を作り直す。`tokens.css` は手で編集しない。
*1. Paste `tokens.css` (CSS variables generated from `tokens.json`) and `components/bundle.css` (component classes) into `<style>`. Drop the first `@import` line of `bundle.css` for offline use (fonts fall back to system fonts). 2. Set `<html lang="ja">`. Dark can be pinned with `data-theme="dark"`; otherwise it follows the OS. 3. Use the `bundle.css` classes directly, e.g. `<button class="f2-btn f2-btn--primary">`; see each component README and `bundle.js` for structure. No React needed. 4. To change values, edit `tokens.json` and regenerate `tokens.css`; never hand-edit it.*

**スマホ / Mobile:** タッチ操作の端末（`pointer: coarse`）では、入力欄と選択欄の文字を 16px にする。iPhone の Safari は、16px 未満の欄にフォーカスすると画面を拡大するため。
*On touch devices (`pointer: coarse`) input and select text is 16px, because iPhone Safari zooms the page when a field under 16px is focused.*
