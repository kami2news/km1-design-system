# 対応表 / Coverage

KM1-COV-001。どの部品が、どのプラットフォームで、どこまで使えるかの一覧。「実装」と「検証」は別に書く。作ってあっても、確かめ済みとは限らない。
*KM1-COV-001. Which component works where, and how far. Implementation and verification are written separately: built does not mean checked.*

## 1. 印の読み方 / Legend

| 印 | 意味 / Meaning |
|---|---|
| ◎ | KM1 専用の実装がある（Web は `bundle.js`、Flutter は `km1_widgets.dart`）/ A dedicated KM1 implementation |
| ◯ | 標準の部品に KM1 のテーマを当てると、KM1 の見た目と作法になる / A standard widget with the KM1 theme matches KM1 |
| △ | 色と形は合うが、細部に標準の作法が残る / Color and shape match; details keep the platform's behavior |
| — | 対応する部品がない / No part exists |
| 要確認 | `platforms.md` に対応の記載がない / No mapping is recorded in `platforms.md` |

## 2. プラットフォームごとの状態 / Status per platform

| 対象 / Target | 実装の単位 / Unit | 部品 / Parts | 検証（`verification.md` の番号）/ Verification |
|---|---|---|---|
| Web | `components/bundle.js`・`bundle.css` | 見本のある部品 50（公開 60） | headless Chrome の自動検査と利用シナリオは済み（W1）。実際のブラウザは未実施（W2） |
| Flutter | `km1_theme.dart`・`km1_widgets.dart` | KM1 専用の 31 部品と、テーマを当てた標準の部品 | 文法と API 名の照合のみ。解析・ビルド・実際の画面は未実施（F1） |
| WinUI 3 | `KM1.xaml` | 部品なし。標準のボタンやスイッチが KM1 の紺になる | 文法とキー名の照合のみ。ビルド未実施（N2） |
| Jetpack Compose | `Km1Theme.kt` | `Km1PrimaryButton` だけ | 文法と関数名の照合のみ。ビルド未実施（A1） |
| SwiftUI | `KM1Theme.swift` | `Km1PrimaryButtonStyle` だけ | 文法のみ。ビルド未実施（I1・M1） |

*Web: 50 with previews, 60 exported; Flutter: 31 KM1 widgets. The three native targets ship tokens (color, type, spacing, hit area) and icons, not components.*

ネイティブ 3 つ（WinUI 3・Compose・SwiftUI）の部品は、下の表の `Button` を除いてすべて「—」。色・文字・余白・操作領域のトークンとアイコンの SVG だけを渡している。
*Apart from `Button`, every part in the table below is "—" on the three native targets: they get tokens and SVG icons only.*

## 3. 部品ごとの対応 / Per component

「公開 60」のうち `ICONS`・`PATTERNS` はデータ、`FormItem` は `FormGroup` の内部の部品。部品の数として数えるときは、この内訳に気をつける。
*Of the 60 exports, `ICONS` and `PATTERNS` are data and `FormItem` is internal to `FormGroup`; keep that in mind when counting components.*

### 操作 / Actions

| 部品 / Component | Web | Flutter | 備考 / Note |
|---|---|---|---|
| `Button` | ◎ | ◯ `FilledButton`・`OutlinedButton`・`TextButton` | WinUI は標準のボタンが KM1 の紺になる。Compose・SwiftUI は主ボタンだけ |
| `Link` | ◎ | 要確認 | G1 |
| `Menu` | ◎ | △ `MenuAnchor` | |
| `Toolbar` | ◎ | △ `Row` に `Semantics` | |
| `Chip` | ◎ | ◎ `Km1FilterChip` | |

### 入力 / Forms

| 部品 / Component | Web | Flutter | 備考 / Note |
|---|---|---|---|
| `Input` | ◎ | △ `TextField` | 「下辺だけ強調」をテーマで再現できない（G2） |
| `Textarea` | ◎ | ◯ `TextField` | |
| `SearchBox` | ◎ | ◯ `TextField` と検索アイコン | `SearchBar` は使わない |
| `Select` | ◎ | △ `DropdownMenu` | 形が Material 寄り |
| `Combobox` | ◎ | △ `Autocomplete` | |
| `Checkbox` | ◎ | ◯ `CheckboxListTile` | |
| `RadioGroup` | ◎ | ◯ `RadioListTile` | |
| `Switch` | ◎ | ◯ `SwitchListTile` | |
| `Slider` | ◎ | △ `Slider` | 色のみ |
| `SpinButton` | ◎ | ◯ `TextField` と `IconButton` | |
| `TagPicker` | ◎ | ◎ `Km1TagPicker` | |
| `FileUpload` | ◎ | ◎ `Km1FileList` | 選ぶ処理はアプリ側 |

### フォームの組み立て / Form layout

| 部品 / Component | Web | Flutter | 備考 / Note |
|---|---|---|---|
| `FormGroup` | ◎ | ◎ `Km1FormGroup`・`Km1Form` | `Km1Form` は全体の器 |
| `FormActions` | ◎ | ◎ `Km1FormActions` | |
| `FormGrid` | ◎ | ◎ `Km1FormGrid`・`Km1FullSpan` | |
| `ConditionalField` | ◎ | ◎ `Km1ConditionalField` | |
| `ErrorSummary` | ◎ | ◎ `Km1ErrorSummary` | |
| `FormItem` | ◎ | — | Web の内部の部品 |

### 移動 / Navigation

| 部品 / Component | Web | Flutter | 備考 / Note |
|---|---|---|---|
| `Nav` | ◎ | △ `NavigationBar`・`NavigationRail` | 色のみ |
| `Tabs` | ◎ | ◯ `TabBar` | |
| `Breadcrumb` | ◎ | ◎ `Km1Breadcrumb` | |
| `Pagination` | ◎ | ◎ `Km1Pagination` | |

### お知らせ / Feedback

| 部品 / Component | Web | Flutter | 備考 / Note |
|---|---|---|---|
| `Alert` | ◎ | 要確認 | G1。「通信できないとき」「失敗」の型が使う |
| `Toast` | ◎ | ◯ `SnackBar` | |
| `Progress` | ◎ | ◎ `Km1Progress` | 工程と時間の見込みを出せる |
| `Spinner` | ◎ | △ `CircularProgressIndicator` | 文言は自分で付ける |
| `Skeleton` | ◎ | ◎ `Km1Skeleton` | |
| `EmptyState` | ◎ | ◎ `Km1EmptyState` | |
| `Badge` | ◎ | △ `Badge` | |

### 重ねる・まとめる / Overlays and containers

| 部品 / Component | Web | Flutter | 備考 / Note |
|---|---|---|---|
| `Dialog` | ◎ | ◯ `showDialog` と `AlertDialog` | |
| `Drawer` | ◎ | ◯ `Drawer` | |
| `BottomSheet` | ◎ | ◯ `showKm1BottomSheet` | 640 以上は `Dialog` |
| `Popover` | ◎ | △ `MenuAnchor` か小さい `showDialog` | |
| `Tooltip` | ◎ | △ `Tooltip` | |
| `Card` | ◎ | ◯ `Card` | |
| `Accordion` | ◎ | △ `ExpansionTile` | |

### データ・一覧と選択 / Data, lists and selection

| 部品 / Component | Web | Flutter | 備考 / Note |
|---|---|---|---|
| `Table` | ◎ | ◎ `Km1Table` | |
| `SortableList` | ◎ | ◎ `Km1SortableList` | |
| `Avatar` | ◎ | ◎ `Km1Avatar` | |
| `List` | ◎ | ◎ `Km1ListItem` | `ListView` と組み合わせる |
| `ListItem` | ◎ | ◎ `Km1ListItem` | |
| `ListSection` | ◎ | ◎ `Km1ListSectionHeader` | 固定は `SliverPersistentHeader` |
| `ListSectionHeader` | ◎ | ◎ `Km1ListSectionHeader` | |
| `ContextualActionBar` | ◎ | ◎ `Km1ContextualActionBar` | |
| `ExpansionEditor` | ◎ | ◎ `Km1ExpansionEditor`・`Km1ExpansionEditorGroup` | |
| `StepFlow` | ◎ | ◎ `Km1StepFlow` | `Stepper` は使わない |
| `ImageGrid` | ◎ | ◎ `Km1ImageGrid` | |

### 日付と時刻 / Date and time

| 部品 / Component | Web | Flutter | 備考 / Note |
|---|---|---|---|
| `Calendar` | ◎ | ◎ `Km1Calendar` | 期間の選択は未収録（P1） |
| `Timetable` | ◎ | ◎ `Km1Timetable` | |
| `TimeGrid` | ◎ | ◎ `Km1TimeGrid` | |

### 分類・アイコン・データ / Categories, icons and data

| 部品 / Component | Web | Flutter | 備考 / Note |
|---|---|---|---|
| `CategoryMark` | ◎ | ◎ `Km1CategoryMark` | |
| `CategoryLegend` | ◎ | ◎ `Km1CategoryLegend` | |
| `Icon` | ◎ | ◎（`Km1BIcon`・`Km1Icons`） | `Icons.*` は使わない |
| `ICONS` | データ | データ | アイコンの一覧 |
| `PATTERNS` | データ | データ | 分類の模様の一覧 |

## 4. 空欄と気づいた点 / Gaps

| # | 内容 / What | 状態 | 次の一手 / Next |
|---|---|---|---|
| G1 | Flutter の `Alert` と `Link` の対応が `platforms.md` にない。`Alert` は「通信できないとき」「失敗・つながらない」の型で使う | 未判断 | 対応を決めて `platforms.md` に書く。専用のウィジェットが要るなら提案にする |
| G2 | Flutter の `Input` は、Web の「下辺だけ強調」をテーマで再現できない。スケジュール確認アプリは専用の入力部品で補った | 未判断 | 2 つ目の製品（`kami2pos`）でも同じ部品が要るなら、KM1 の部品にする合図（`product.md` 6 章） |
| G3 | Flutter の △ の部品（`Select`・`Combobox`・`Menu`・`Nav`・`Slider`・`Spinner`・`Popover`・`Tooltip`・`Accordion`・`Toolbar`・`Badge`・`Input`）は、細部が Material の作法のまま | 未判断 | 製品で目立つ順に、△ を ◎ にするか決める |
| G4 | ネイティブ 3 つに部品がない（`Button` だけ） | 未判断 | 実際にネイティブで作る製品が決まってから、必要な部品から足す |
| G5 | Flutter・ネイティブは、実装はあっても検証が追いついていない（2 章） | 進行中 | `verification.md` の F1・N2・A1・I1 を実機で行う |

*G1: the Flutter mapping for `Alert` and `Link` is missing. G2: Flutter's `Input` cannot reproduce the underline emphasis; a second product needing the same part is the signal to add it (product.md ch. 6). G3: △ parts keep Material details. G4: native targets have no components beyond `Button`. G5: verification lags implementation.*

## 5. 進める順の案 / Suggested order (proposal)

持ち主が決める。部品の増強は急務という方針に沿って、効果の大きい順に並べた。
*The owner decides. Ordered by payoff, following the stated urgency of widening component coverage.*

1. G1 を埋める（Flutter の `Alert`・`Link`）。他の型が `Alert` を前提にしている。
2. 製品（`kami2pos`・スケジュール確認アプリ）で目立つ △ を ◎ にする（G2 の `Input`、`Select`、`Menu`、`Nav` の順に検討）。
3. Flutter の解析とビルド（F1）で、◎ の実装が動くことを確かめる。
4. 新しい部品の仕様案（`proposals.md`: 日付範囲・ツリー・グラフ）。
5. ネイティブの部品。作る製品が決まってから。

## 6. 更新の決まり / Keeping it current

- 部品を足す・名前を変える・Flutter のウィジェットを足すときは、この表に行を足す。
  *Add or rename a row whenever a component or Flutter widget is added or renamed.*
- 印を ◯・△ から ◎ に上げるのは、実装がそろったとき。下げるのは、検証で問題が見つかったとき。理由を変更履歴に書く。
  *Raise a mark to ◎ only when the implementation exists; lower it when a check finds a problem, and note why in the changelog.*
- `gen/sync_counts.py --check` が、部品と Flutter ウィジェットの名前がこの表に全部あるか、数の記述が合っているかを調べる。
  *`gen/sync_counts.py --check` verifies that every component and widget name appears here and that counts match.*
