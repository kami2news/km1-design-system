# プラットフォーム / Platforms

KM1 は、1 つの見た目を全端末で同じに保つのではなく、**色・文字・言葉・部品の役割は共通、操作の作法は各プラットフォームに合わせる**。使う人は、自分の端末でいつもしている操作をそのまま期待するため。
*KM1 keeps color, type, wording and component roles shared, and follows each platform's interaction conventions, because people expect the moves they already know.*

| 対象 / Target | 実装 / Implementation | 状態 / Status |
|---|---|---|
| Web（HTML） | `components/bundle.js`（React）、`components/bundle.css`、`tokens.css`（React なしの単体 HTML でも可） | 見本のある部品 50（公開 60）。自動検査・キーボード・320px・強制カラーを headless Chrome で確認済み。**安定（パイロット）**。実際のブラウザ 4 種と読み上げソフトでの確認は未実施（verification W2・N1） |
| Flutter（Android・iOS・iPadOS・Windows・macOS・Web） | `km1_theme.dart`（テーマ）と `km1_widgets.dart`（KM1 専用の 30 部品）。ほかは Flutter 標準の部品にテーマを当てる | **パイロット**。CI で `flutter analyze` と `flutter test`（ギャラリーの組み立て）を push のたびに実施（2026-11-18 から）。実機でのビルドと表示は未実施（verification F3） |
| Windows ネイティブ（WinUI 3） | `KM1.xaml`（ResourceDictionary）。WinUI 3 の部品はもともと KM1 の土台と同じ形なので、アクセント色・角丸・書体と KM1 の色のブラシを当てるだけでよい | **実験的（experimental）**。生成済み。XML として正しいこと、上書きするキーが WinUI のソース（2026-11-12 時点）に実在すること、Windows の背景での読みやすさを確認。**ビルドは未実施** |
| Android ネイティブ（Jetpack Compose） | `Km1Theme.kt`（`Km1Theme`、`Km1.colors`、`Km1PrimaryButton`） | **実験的（experimental）**。生成済み。文法と、使った関数・引数が androidx のソース（2026-11-12 時点）に実在することを確認。**ビルドは未実施** |
| iOS・iPadOS・macOS ネイティブ（SwiftUI） | `KM1Theme.swift`（`Km1Color`、`Km1Text`、`Km1PrimaryButtonStyle`） | **実験的（experimental）**。生成済み。文法のみ確認（SwiftUI はソースが非公開で照合できない）。**ビルドは未実施** |

**状態の意味:** 安定（パイロット）＝自動検査に合格し、試しに製品で使ってよい。パイロット＝自動検査はあるが実機の確認がまだ。実験的＝ビルドしたことがなく、製品では使わない。実機の確認（`verification.md`）が済んだら 1 段上げる。
*Status: stable (pilot) = passes automated checks, fine for trial use; pilot = automated checks but no device run; experimental = never built, not for products. Promote after the device checks in `verification.md`.*

部品ごとの Web・Flutter・ネイティブの対応と不足は `coverage.md`（KM1-COV-001）。ネイティブはテーマだけで部品はない。
*Per-component coverage across Web, Flutter and native, with gaps: `coverage.md`. Native ships themes only, no components.*

## Web で使う / Web

React で使うときは `tokens.css`・`components/bundle.css`・`components/bundle.js` を読み込み、`window.Fluent2` の部品を使う（名前の `Fluent2` と、クラスの頭の `f2-` は、土台にした時期の名残で、互換のためそのままにしている）。各部品の使い方は `components/<Name>/README.md`。
*With React, load `tokens.css`, `bundle.css` and `bundle.js` and use the parts in `window.Fluent2` (the `Fluent2` name and `f2-` class prefix remain for compatibility). Each part's guide is `components/<Name>/README.md`.*

未収録: 予定表（`TimeGrid`）の中で予定をドラッグして動かす操作、自由入力でタグを作る操作。どちらも、編集画面と選択肢の追加で代わりができる。Flutter 版は、`km1_theme.dart`（テーマ）と `km1_widgets.dart`（KM1 専用の 30 部品）。ほかは Flutter 標準の部品にテーマを当てる（対応表は「プラットフォーム」）。
*Not included: dragging events inside `TimeGrid` and creating free-text tags; the editor and option lists cover both. Flutter uses `km1_theme.dart` plus `km1_widgets.dart` (30 KM1 widgets); see Platforms for the mapping.*

### React を使わない単体の HTML / Single HTML file without React

1. `tokens.css`（`tokens.json` から自動生成した CSS 変数）と `components/bundle.css`（部品のクラス）を、`<style>` に貼る。`bundle.css` の最初の `@import` 行は、オフラインで使うなら外す（書体は端末の標準書体に落ちる）。
2. `<html lang="ja">` を付ける。ダークは `<html data-theme="dark">` で固定でき、付けなければ OS の設定に従う。
3. 部品は `bundle.css` のクラスをそのまま使う（例: `<button class="f2-btn f2-btn--primary">保存</button>`）。クラス名と構造は、各部品の `README.md` と `bundle.js` を見る。React は要らない。
4. 値を変えるときは `tokens.json` を直して `tokens.css` を作り直す。`tokens.css` は手で編集しない。
5. **書体の約束（KM1-TYP-002）:** `bundle.css` の先頭にある土台の 2 行（`html{font-family:var(--font-sans)}` と、`button`・`input`・`select`・`textarea` の `font:inherit`）を消さない。`tokens.css` だけを使うときは、同じ 2 行を自分で書く。これがないと、素の文字やフォーム部品がブラウザ既定の書体（明朝など）になる。
*1. Paste `tokens.css` (CSS variables generated from `tokens.json`) and `components/bundle.css` (component classes) into `<style>`. Drop the first `@import` line of `bundle.css` for offline use (fonts fall back to system fonts). 2. Set `<html lang="ja">`. Dark can be pinned with `data-theme="dark"`; otherwise it follows the OS. 3. Use the `bundle.css` classes directly, e.g. `<button class="f2-btn f2-btn--primary">`; see each component README and `bundle.js` for structure. No React needed. 4. To change values, edit `tokens.json` and regenerate `tokens.css`; never hand-edit it. 5. Keep the two base rules at the top of `bundle.css` (`html{font-family:var(--font-sans)}` and `font:inherit` on form controls); add them yourself if you use `tokens.css` alone, or plain text and form controls fall back to the browser's default (often serif) font.*

**スマホ / Mobile:** タッチ操作の端末（`pointer: coarse`）では、入力欄と選択欄の文字を 16px にする。iPhone の Safari は、16px 未満の欄にフォーカスすると画面を拡大するため。
*On touch devices (`pointer: coarse`) input and select text is 16px, because iPhone Safari zooms the page when a field under 16px is focused.*

## Flutter で使う / Flutter

`tokens.json` から生成した `km1_theme.dart` を使う（`ThemeData` と `ThemeExtension`）。ほかのデザインを再現する既存パッケージ（`fluent_ui` など）は使わない。Material は部品の土台として使うだけで、色・形・大きさはテーマで上書きする。
*Use `km1_theme.dart`, generated from `tokens.json` (`ThemeData` + `ThemeExtension`). Packages that recreate other design systems (such as `fluent_ui`) are not used. Material is only the widget base; colour, shape and size are overridden by the theme.*

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

### 注意 / Notes
- 無効ボタンは Flutter では `onPressed: null` が標準だが、KM1 は「無効にせず理由を示す」方針（押せないボタンは理由を伝えられない）なので、なるべく有効のまま押したときに理由を出す。
- 入力欄は、Web 版の「下辺だけ強調」を `InputDecorationTheme` だけでは再現できないので、テーマでは四辺同じ枠にしてある。同じ見た目にしたいときは、スケジュール確認アプリのように専用の入力部品を作る。
- `Icons.*` は使わない。KM1 のアイコンは `Km1BIcon(Km1BIconName.…)` で出す（`Km1Icons.*` のフォントは Filled 用）。
- `NoSplash` にしているので、押した状態は色の変化（`surface-pressed`）だけで示す。
*Prefer leaving buttons enabled and explaining on press, per KM1's no-disable rule. Use `Km1BIcon(Km1BIconName.…)` (the `Km1Icons.*` font is for Filled), never `Icons.*`. Press feedback is a color change only (no ripple).*

## ネイティブで使う / Native setup

どのファイルも `tokens.json` から自動で作る（`gen/native.py`）。色を直すときは `tokens.json` だけを直し、作り直す。
*Every file is generated from `tokens.json`; edit only the tokens and regenerate.*

### Windows（WinUI 3）— `KM1.xaml`
1. `App.xaml` の `Application.Resources` で、`XamlControlsResources` の後に `<ResourceDictionary Source="KM1.xaml" />` を入れる。
2. ボタンやスイッチなど標準の部品は、そのまま KM1 の紺になる（`SystemAccentColor` 系を上書きしているため）。
3. 自分で色を塗るときは `{ThemeResource KM1InkBrush}` のように KM1 のブラシを使う。ライト・ダーク・ハイコントラストで自動で切り替わる。ハイコントラストではすべてシステムの色に従う。
4. WinUI のダークは「明るいアクセントの上に黒い文字」が標準だが、KM1 の紺の上では読みにくい（3.22:1）ため、アクセントの上の文字を白（6.52:1）に、主ボタンの縁を `brand-stroke`（背景と 4.5:1 以上）にしてある。
5. アイコンは KM1 のアイコンの SVG（`icons/build/svg`）。KM1 にない操作だけ Segoe Fluent Icons（Windows 標準）を使い、KM1 のアイコンに足す候補として記録する。
*Merge `KM1.xaml` after `XamlControlsResources`; standard controls pick up the accent; use `KM1*Brush` for custom drawing; high contrast follows system colors; dark text-on-accent and primary-button borders are overridden for contrast.*

### Android（Jetpack Compose）— `Km1Theme.kt`
1. `setContent { Km1Theme { ... } }` で包む。色は `Km1.colors.ink`、文字は `Km1Text.body1`、余白は `Km1Space.md`。
2. 動的な色（Material You の `dynamicColorScheme`）は使わない。KM1 の紺が端末の壁紙の色に置き換わってしまうため。
3. 主ボタンは `Km1PrimaryButton`（ダークで縁取りが付く）。操作領域は Material 3 の既定の 48dp のまま。
4. アイコンは KM1 のアイコンの SVG（`icons/build/svg`）を Vector Asset として取り込む。Material Icons は使わない。
5. 書体は端末の書体（日本語は Noto Sans CJK）。
*Wrap in `Km1Theme`; no dynamic color; `Km1PrimaryButton` for primaries; keep 48dp; import KM1 icon SVGs as vector assets.*

### iOS・iPadOS・macOS（SwiftUI）— `KM1Theme.swift`
1. ファイルをプロジェクトに入れる。色は `Km1Color.ink`、文字は `Km1Text.body1`、余白は `Km1Space.md`。ライト・ダークは自動で切り替わる。
2. 文字は Dynamic Type に合わせて拡大する。Noto Sans JP を同梱しないときは、システムの書体（ヒラギノ角ゴ）になる。
3. 主ボタンは `.buttonStyle(Km1PrimaryButtonStyle())`（高さ 44pt、縁取りつき）。
4. アイコンは KM1 のアイコンの SVG を Asset Catalog に入れて使う（「Preserve Vector Data」をオン、描画は Template）。SF Symbols に置き換えない。
*Add the file; colors, Dynamic Type text, `Km1PrimaryButtonStyle` (44pt, outlined); icons from the KM1 SVG set.*

### OS ごとの確認 / Per-OS checks
| OS | 読み上げ | 文字の拡大 | 確かめる道具 |
|---|---|---|---|
| Windows | ナレーター（Ctrl + Win + Enter） | 設定 > アクセシビリティ > 文字のサイズ | Accessibility Insights for Windows |
| Android | TalkBack | 設定 > ユーザー補助 > フォントサイズ（最大） | Accessibility Scanner |
| iOS・iPadOS | VoiceOver | 設定 > アクセシビリティ > さらに大きな文字 | Xcode の Accessibility Inspector |
| macOS | VoiceOver（Cmd + F5） | — | Accessibility Inspector |
| Web | NVDA（Windows）・VoiceOver | ブラウザの 200% 拡大 | axe DevTools |

## 部品の高さ / Control height

各社の推奨に合わせて端末ごとに切り替える。値は Flutter では `Km1Theme.targetFor()`、Web では CSS の `--control-height` が自動で決める。
*Switches per platform, following each vendor's guidance: `Km1Theme.targetFor()` in Flutter, `--control-height` on the web.*

値はトークン `control-target-*`（`tokens.json` の `platformTarget`）から生成する。Flutter は `Km1PlatformTarget`、Compose は `Km1PlatformTarget.android`、SwiftUI は `Km1Space.hitTarget`、WinUI は `KM1ControlTarget`。用途別の余白は各 OS で `Km1SpaceRole`（WinUI は `KM1LayoutSectionGap` などの Double）。密度は余白だけを変え、この値を下回らない（「基礎」）。
*Values come from `control-target-*` tokens; generated as `Km1PlatformTarget` (Flutter, Compose), `Km1Space.hitTarget` (SwiftUI), `KM1ControlTarget` (WinUI). Role spacing is `Km1SpaceRole`. Density never goes below these.*

| 端末 / Platform | 標準の高さ / Default | small ボタン | 根拠 / Source |
|---|---|---|---|
| Android | 48dp | 48dp | Android の推奨は、操作できる要素ごとに 48 × 48dp 以上 |
| iOS・iPadOS | 44pt | 44pt | Apple HIG の 44 × 44pt |
| Windows・macOS（マウス中心） | 32px | 24px | マウスで押し外さない大きさ。WCAG 2.2 AA（24px）を満たす |
| Windows（タブレット姿勢・タッチ中心） | 44px | 44px | Windows のタッチ向けの推奨 44 × 44 epx。Flutter では `Km1Theme.light(touch: true)` |
| Web・タッチ（`pointer: coarse`） | 44px | 44px | WCAG 2.2 AAA（2.5.5） |
| Web・マウス | 32px | 24px | 同上。WCAG 2.2 AA |

- Web は Android の端末で見ても 44px（WCAG の値）。Android の 48dp は、Flutter で作った Android アプリにだけ使う。
  *The web stays at 44px even on Android phones; 48dp applies to Flutter apps on Android only.*
- iPad は Magic Keyboard やトラックパッドが付いていてもタッチ中心として扱い、44pt のまま。
  *iPad stays at 44pt even with a trackpad.*

## プラットフォームごとの作法 / Conventions per platform

### Android
- **戻る**: 端からのスワイプとシステムの「戻る」で 1 つ前に戻る。アプリの中に独自の「戻る」ボタンだけを置いて、システムの戻るを無効にしない。最初の画面で戻るとアプリを閉じる。
  ***Back**: system back and edge swipe go one step back; never disable it in favor of a custom button.*
- **画面の端まで描く（edge-to-edge）**: 状態バーとナビゲーションバーの下まで背景を伸ばし、操作部品は `SafeArea` の内側に置く。
  ***Edge-to-edge**: backgrounds extend under the system bars; controls stay inside `SafeArea`.*
- **読み上げ**: TalkBack。部品の名前は `Semantics(label:)`、アイコンだけのボタンは `tooltip` で付ける。
  ***Screen reader**: TalkBack; name controls with `Semantics(label:)` and `tooltip`.*
- **確かめ方**: Accessibility Scanner で操作領域とコントラストを見る。
  ***Check** with Accessibility Scanner.*

### iOS・iPadOS
- **戻る**: 画面の左端からの右スワイプで戻る（`km1_theme.dart` で iOS は Cupertino の画面遷移にしてある）。上部バーの左に「戻る」ボタンを置く。
  ***Back**: swipe from the left edge (Cupertino transitions are set in `km1_theme.dart`); a back button sits at the top left.*
- **安全領域**: ノッチ・Dynamic Island・ホームインジケーターの領域に操作部品を置かない（`SafeArea`）。下部のタブはホームインジケーターの上に置く。
  ***Safe areas**: keep controls clear of the notch, Dynamic Island and home indicator.*
- **iPad**: 幅 1024px 以上では、KM1 の決まりどおりサイドバーを常時表示する。ダイアログの代わりにポップオーバーを使う場面がある（メニューなど、指した場所から出るもの）。画面分割（Split View）で幅が狭くなったら、スマホの組み立てに戻る。幅で判断し、端末の種類で判断しない。
  ***iPad**: persistent sidebar from 1024px; popovers for menus; in Split View fall back to the phone layout. Decide by width, never by device type.*
- **読み上げ**: VoiceOver。**文字の大きさ**: 「さらに大きな文字」まで崩れないこと。
  ***VoiceOver**; layouts must survive the largest Dynamic Type sizes.*

### Windows
- **キーボードが主**: すべての操作を Tab・矢印・Enter・Esc でできるようにし、よく使う操作にはショートカット（Ctrl + N で新規など）を付けて `Tooltip` に書く。
  ***Keyboard-first**: everything works by keyboard; common actions get shortcuts shown in tooltips.*
- **右クリック**: 一覧の項目には右クリックで `Menu` と同じ操作を出す（同じ操作が「⋯」からもできること）。
  ***Right-click** on list items opens the same actions as the "⋯" menu.*
- **ウィンドウの大きさ**: 最小 320px 幅まで崩れないこと。最大化と画面の半分のスナップを想定する。
  ***Window size**: works down to 320px wide; expect maximize and half-screen snap.*
- **読み上げ**: ナレーター。**高コントラスト**: KM1 の強制カラー対応（Web）がそのまま効く。
  ***Narrator**; KM1's forced-colors support covers high contrast on the web.*

### Web
- **ブラウザの戻る**: 画面の切り替えは URL を変え、ブラウザの戻る・進むで行き来できるようにする。ダイアログやドロワーはブラウザの戻るで閉じられるとよい。
  ***Browser back**: screen changes update the URL; dialogs and drawers may close on browser back.*
- **スマホのブラウザ**: 入力欄の文字は 16px（iOS の自動拡大を防ぐ。KM1 の CSS が自動で行う）。
  ***Mobile browsers**: 16px field text (prevents iOS zoom; automatic in KM1's CSS).*

## 共通 / Shared on every platform

- **文字の拡大**: OS の文字サイズ設定を止めない（Flutter で `textScaler` を固定しない、Web で `px` 固定の `font-size` を `html` に付けない）。200% でも操作できること。
  ***Text scaling**: never block the OS setting; everything works at 200%.*
- **書体**: Flutter は `Noto Sans JP` を同梱（`google_fonts` か assets）し、同梱しないときは端末の書体（iOS はヒラギノ角ゴ、Windows は Yu Gothic UI、Android は Noto Sans CJK）に任せる。`km1_theme.dart` の `fontFamilyFallback` にこの順で入っている。
  ***Typeface**: bundle Noto Sans JP in Flutter, or fall back to the system font (Hiragino Sans, Yu Gothic UI, Noto Sans CJK) as listed in `fontFamilyFallback`.*
- **アイコン**: すべての端末で KM1 のアイコン（Web は `Icon`、Flutter は `Km1Icons`、ネイティブは `icons/build/svg` の SVG を素材として取り込む）。iOS だけ SF Symbols に替える、ということはしない（見た目の言葉をそろえるため）。
  ***Icons**: KM1 icons everywhere (Web `Icon`, Flutter `Km1Icons`, native apps import the SVGs); no SF Symbols swap on iOS.*
- **動き**: OS の「視差効果を減らす」「アニメーションを削除」に従う（Flutter は `MediaQuery.disableAnimations`、Web は `prefers-reduced-motion`）。
  ***Motion**: honor the OS reduce-motion setting.*

## Flutter での部品の対応 / Web components in Flutter

**Flutter の版 / Flutter version:** GitHub の CI で、最新の安定版（2026-11-18 時点で 3.50）を使って `flutter analyze` と `flutter test` を流す。Flutter 3.47 から `package:flutter/material.dart` が非推奨になり、`material_ui` パッケージへの移行が始まっている。KM1 はまだ `material.dart` を使っていて、CI ではこの非推奨の「情報」だけは落とさない。移行は今後の課題。
*CI runs `flutter analyze` and `flutter test` on the latest stable (3.50 as of 2026-11-18). `material.dart` is deprecated since 3.47 in favour of the `material_ui` package; KM1 still uses it, CI tolerates that info, and the migration is pending.*

| KM1（Web） | Flutter | テーマで当たるか / Themed |
|---|---|---|
| Button | `FilledButton`（primary）、`OutlinedButton`（secondary）、`TextButton`（subtle） | ◯ |
| Input・Textarea | `TextField`（`maxLines` で複数行） | ◯ |
| SearchBox | `TextField` + 先頭に検索アイコン（`SearchBar` は Material の見た目なので使わない） | ◯ |
| Select | `DropdownMenu` | △ 形は Material 寄り |
| Combobox | `Autocomplete` | △ |
| Checkbox・RadioGroup・Switch | `CheckboxListTile`・`RadioListTile`・`SwitchListTile` | ◯ |
| Slider | `Slider` | △ 色のみ |
| SpinButton | `TextField`（`keyboardType: number`）+ `IconButton` 2 つ | ◯ |
| Tabs | `TabBar` | ◯ |
| Nav | 狭い画面 `NavigationBar`、広い画面 `NavigationRail` / `Drawer` | △ 色のみ |
| Dialog・Drawer | `showDialog` + `AlertDialog`、`Drawer` / `endDrawer` | ◯ |
| Menu | `MenuAnchor` | △ |
| Toolbar | `Row` に `IconButton`・`TextButton` を並べ、`Semantics(container: true, label:)` で名前を付ける。狭い画面の「⋯」は `MenuAnchor` | △ |
| Popover | `MenuAnchor` の中に操作を置くか、`showDialog`（小さめ） | △ |
| TagPicker | `Km1TagPicker` | ◎ KM1 専用 |
| SortableList | `Km1SortableList`（ドラッグ + 上下ボタン + 読み上げ） | ◎ KM1 専用 |
| FormGroup・FormActions | `Km1FormGroup`・`Km1FormActions`（全体の器は `Km1Form`。`AutovalidateMode.onUnfocus` で離れたら確かめる） | ◎ KM1 専用 |
| FormGrid | `Km1FormGrid`（`Km1FullSpan` で全幅） | ◎ KM1 専用 |
| ConditionalField | `Km1ConditionalField`（出たときに読み上げ） | ◎ KM1 専用 |
| ErrorSummary | `Km1ErrorSummary`（`Km1FormError` に欄の `FocusNode` を渡す） | ◎ KM1 専用 |
| List・ListSection | `Km1ListItem`・`Km1ListSectionHeader`（固定は `SliverPersistentHeader(pinned: true)`） | ◎ KM1 専用 |
| ContextualActionBar | `Km1ContextualActionBar` | ◎ KM1 専用 |
| ExpansionEditor | `Km1ExpansionEditor` | ◎ KM1 専用 |
| StepFlow | `Km1StepFlow`（Flutter 標準の `Stepper` は Material の見た目なので使わない） | ◎ KM1 専用 |
| BottomSheet | `showKm1BottomSheet`（スマホは `showModalBottomSheet`、640 以上は `Dialog`） | ◯ |
| ImageGrid | `Km1ImageGrid` | ◎ KM1 専用 |
| Table の行選択・一括操作 | `Km1Table` の `rowId`・`selected`・`onSelectionChanged`・`bulkActions` | ◎ KM1 専用 |
| Toast | `SnackBar` | ◯ |
| Progress・Spinner | `LinearProgressIndicator`・`CircularProgressIndicator` + 文言 | △ 工程と時間の表示は自分で組む |
| Accordion | `ExpansionTile` | △ |
| Tooltip | `Tooltip` | △ |
| Card・Badge・Avatar | `Card`、`Badge`、`CircleAvatar` | ◯ / △ |
| Table・Calendar・Timetable・TimeGrid・Breadcrumb・Pagination・Skeleton・EmptyState・Chip・Avatar | `km1_widgets.dart` の `Km1Table`・`Km1Calendar`・`Km1Timetable`・`Km1TimeGrid`・`Km1Breadcrumb`・`Km1Pagination`・`Km1Skeleton`・`Km1EmptyState`・`Km1FilterChip`・`Km1Avatar` | ◎ KM1 専用 |
| FileUpload | `Km1FileList`（一覧と「ファイルを選ぶ」ボタン）。ファイルを選ぶ処理は `file_picker` などをアプリ側で使う | ◎ KM1 専用 |
| Progress（工程と時間の見込み） | `Km1Progress`（`steps`・`remaining`・`elapsed`・`onCancel`） | ◎ KM1 専用 |

△ は、テーマで色と形は合うが、細部（開き方、余白）が Material の作法のまま残るもの。
*△ means color and shape follow the theme but details keep Material behavior.*

## 出典 / Sources

「参考文献」（`references.md`）の 4 節。

端末ごとの作法（戻る、安全領域、iPad の分割表示など）は各社の公式資料の一般的な決まりを KM1 の言葉でまとめたもので、細部は実機で確かめていない。
*Per-platform conventions summarize each vendor's general guidance in KM1's words; details are not verified on devices.*
