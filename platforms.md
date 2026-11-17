# プラットフォーム / Platforms

KM1 は、1 つの見た目を全端末で同じに保つのではなく、**色・文字・言葉・部品の役割は共通、操作の作法は各プラットフォームに合わせる**。Fluent 2 が「各プラットフォームで馴染みのある操作を尊重する」としているのと同じ考え方。
*KM1 keeps color, type, wording and component roles shared, and follows each platform's interaction conventions, as Fluent 2 does.*

| 対象 / Target | 実装 / Implementation | 状態 / Status |
|---|---|---|
| Web（HTML） | `components/bundle.js`（React）、`components/bundle.css`、`tokens.css`（React なしの単体 HTML でも可） | 見本のある部品 50（公開 60）。自動検査・キーボード・320px・強制カラーを確認済み |
| Flutter（Android・iOS・iPadOS・Windows・macOS・Web） | `km1_theme.dart`（テーマ）と `km1_widgets.dart`（KM1 専用の 30 部品）。ほかは Flutter 標準の部品にテーマを当てる | 文法と、使っているクラス・引数が Flutter の安定版（2026-11-09 時点）に実在するかを照合済み。**型の確認とコンパイルは未実施** |
| Windows ネイティブ（WinUI 3） | `KM1.xaml`（ResourceDictionary）。WinUI 3 は Fluent 2 そのものなので、アクセント色・角丸・書体と KM1 の色のブラシを当てる | 生成済み。XML として正しいこと、上書きするキーが WinUI のソース（2026-11-12 時点）に実在すること、Windows の背景での読みやすさを確認。**ビルドは未実施** |
| Android ネイティブ（Jetpack Compose） | `Km1Theme.kt`（`Km1Theme`、`Km1.colors`、`Km1PrimaryButton`） | 生成済み。文法と、使った関数・引数が androidx のソース（2026-11-12 時点）に実在することを確認。**ビルドは未実施** |
| iOS・iPadOS・macOS ネイティブ（SwiftUI） | `KM1Theme.swift`（`Km1Color`、`Km1Text`、`Km1PrimaryButtonStyle`） | 生成済み。文法のみ確認（SwiftUI はソースが非公開で照合できない）。**ビルドは未実施** |

部品ごとの Web・Flutter・ネイティブの対応と不足は `coverage.md`（KM1-COV-001）。ネイティブはテーマだけで部品はない。
*Per-component coverage across Web, Flutter and native, with gaps: `coverage.md`. Native ships themes only, no components.*

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
4. アイコンは `implementation 'com.microsoft.design:fluent-system-icons:1.1.345@aar'`（Maven Central）。Material Icons は使わない。
5. 書体は端末の書体（日本語は Noto Sans CJK）。
*Wrap in `Km1Theme`; no dynamic color; `Km1PrimaryButton` for primaries; keep 48dp; Fluent icons from Maven Central.*

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

値はトークン `control-target-*`（`tokens.json` の `platformTarget`）から生成する。Flutter は `Km1PlatformTarget`、Compose は `Km1PlatformTarget.android`、SwiftUI は `Km1Space.hitTarget`、WinUI は `KM1ControlTarget`。用途別の余白は各 OS で `Km1SpaceRole`（WinUI は `KM1LayoutSectionGap` などの Double）。密度は余白だけを変え、この値を下回らない（「トークン」）。
*Values come from `control-target-*` tokens; generated as `Km1PlatformTarget` (Flutter, Compose), `Km1Space.hitTarget` (SwiftUI), `KM1ControlTarget` (WinUI). Role spacing is `Km1SpaceRole`. Density never goes below these.*

| 端末 / Platform | 標準の高さ / Default | small ボタン | 根拠 / Source |
|---|---|---|---|
| Android | 48dp | 48dp | Android の推奨は、操作できる要素ごとに 48 × 48dp 以上 |
| iOS・iPadOS | 44pt | 44pt | Apple HIG の 44 × 44pt |
| Windows・macOS（マウス中心） | 32px | 24px | Fluent Compact（32 × 32 epx）、WCAG 2.2 AA（24px） |
| Windows（タブレット姿勢・タッチ中心） | 44px | 44px | Windows のタッチ向けの推奨 44 × 44 epx。Flutter では `Km1Theme.light(touch: true)` |
| Web・タッチ（`pointer: coarse`） | 44px | 44px | WCAG 2.2 AAA（2.5.5） |
| Web・マウス | 32px | 24px | Fluent Compact、WCAG 2.2 AA |

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
- Android Developers, "Make apps more accessible": https://developer.android.com/guide/topics/ui/accessibility/apps
- Apple, Human Interface Guidelines（44 × 44pt）: https://developer.apple.com/design/human-interface-guidelines/
- Microsoft Learn, "Guidelines for touch targets" と "Touch interactions"（Windows）: https://learn.microsoft.com/windows/apps/design/input/guidelines-for-targeting
- 端末ごとの作法（戻る、安全領域、iPad の分割表示など）は各社の公式資料の一般的な決まりを KM1 の言葉でまとめたもので、細部は実機で確かめていない。
  *Per-platform conventions summarize each vendor's general guidance in KM1's words; details are not verified on devices.*
