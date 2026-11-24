# KM1 部品カタログ / Component catalog

見本 68 件を 16 のグループに分けて載せる。各部品の説明は部品フォルダの `README.md`、動く見本は `preview.html`。画像は `gen/shoot_previews.js` で撮ったもの（左がライト、右がダーク）。PDF 版は `dist/KM1_部品カタログ.pdf`。
*68 previews in 16 groups. Each folder has a README and a live `preview.html`; light on the left, dark on the right. PDF: `dist/KM1_部品カタログ.pdf`.*

## 目次 / Contents

- **表紙 / Cover**: [Cover](#cover)
- **操作 / Actions**: [Button](#button)・[Chip](#chip)・[Menu](#menu)・[Toolbar](#toolbar)
- **入力 / Forms**: [Checkbox](#checkbox)・[Combobox](#combobox)・[ConditionalField](#conditionalfield)・[ErrorSummary](#errorsummary)・[FileUpload](#fileupload)・[FormGrid](#formgrid)・[FormGroup](#formgroup)・[Input](#input)・[RadioGroup](#radiogroup)・[SearchBox](#searchbox)・[Select](#select)・[Slider](#slider)・[SpinButton](#spinbutton)・[Switch](#switch)・[TagPicker](#tagpicker)・[Textarea](#textarea)
- **一覧と選択 / Lists and selection**: [BottomSheet](#bottomsheet)・[ContextualActionBar](#contextualactionbar)・[ExpansionEditor](#expansioneditor)・[ImageGrid](#imagegrid)・[List](#list)・[StepFlow](#stepflow)
- **データ / Data**: [Avatar](#avatar)・[CategoryPattern](#categorypattern)・[SortableList](#sortablelist)・[Table](#table)
- **日付と時間 / Date and time**: [Calendar](#calendar)・[TimeGrid](#timegrid)・[Timetable](#timetable)
- **ナビゲーション / Navigation**: [Breadcrumb](#breadcrumb)・[Link](#link)・[Nav](#nav)・[Pagination](#pagination)・[Tabs](#tabs)
- **入れ物 / Containers**: [Accordion](#accordion)
- **面 / Surfaces**: [Card](#card)
- **重ねて出すもの / Overlays**: [Dialog](#dialog)・[Drawer](#drawer)・[Popover](#popover)・[Tooltip](#tooltip)
- **知らせ / Feedback**: [EmptyState](#emptystate)・[Progress](#progress)・[Skeleton](#skeleton)・[Spinner](#spinner)・[Toast](#toast)
- **状態 / Status**: [Alert](#alert)・[Badge](#badge)
- **アイコン / Icons**: [AppIcon](#appicon)・[Icon](#icon)・[IconTrial](#icontrial)
- **密度 / Density**: [Density](#density)
- **画面の例 / Screen patterns**: [ScreenAddEvent](#screenaddevent)・[ScreenListEdit](#screenlistedit)・[ScreenOffline](#screenoffline)・[ScreenToday](#screentoday)
- **M1 比較 / M1 comparison**: [CompareBottomSheet](#comparebottomsheet)・[CompareExpansion](#compareexpansion)・[CompareFAB](#comparefab)・[CompareGrid](#comparegrid)・[CompareList](#comparelist)・[CompareSelection](#compareselection)・[CompareStepper](#comparestepper)・[SelectionGuide](#selectionguide)

## 表紙 / Cover

### Cover

 → [Cover/](Cover/)

<table><tr><td valign="top"><img src="Cover/preview.png" alt="Cover の見本（ライト）/ Cover preview, light" width="420"></td><td valign="top"><img src="Cover/preview-dark.png" alt="Cover の見本（ダーク）/ Cover preview, dark" width="420"></td></tr></table>


## 操作 / Actions

### Button

操作を実行するボタン。1 画面にプライマリ（`appearance="primary"`）は 1 つだけ。 → [Button/](Button/)

<table><tr><td valign="top"><img src="Button/preview.png" alt="Button の見本（ライト）/ Button preview, light" width="420"></td><td valign="top"><img src="Button/preview-dark.png" alt="Button の見本（ダーク）/ Button preview, dark" width="420"></td></tr></table>

### Chip

押して切り替える小さな絞り込みボタン。一覧のフィルターや、複数選べる分類に使う。 → [Chip/](Chip/)

<table><tr><td valign="top"><img src="Chip/preview.png" alt="Chip の見本（ライト）/ Chip preview, light" width="420"></td><td valign="top"><img src="Chip/preview-dark.png" alt="Chip の見本（ダーク）/ Chip preview, dark" width="420"></td></tr></table>

### Menu

ボタンを押すと開く操作の一覧。場所を取らずに、頻度の低い操作をまとめる。 → [Menu/](Menu/)

<table><tr><td valign="top"><img src="Menu/preview.png" alt="Menu の見本（ライト）/ Menu preview, light" width="420"></td><td valign="top"><img src="Menu/preview-dark.png" alt="Menu の見本（ダーク）/ Menu preview, dark" width="420"></td></tr></table>

### Toolbar

一覧や編集画面の上に、よく使う操作を横に並べる帯。 → [Toolbar/](Toolbar/)

<table><tr><td valign="top"><img src="Toolbar/preview.png" alt="Toolbar の見本（ライト）/ Toolbar preview, light" width="420"></td><td valign="top"><img src="Toolbar/preview-dark.png" alt="Toolbar の見本（ダーク）/ Toolbar preview, dark" width="420"></td></tr></table>


## 入力 / Forms

### Checkbox

複数選択や同意のためのチェックボックス。ラベルは必ず付け、ラベルをクリックしても切り替わる。 → [Checkbox/](Checkbox/)

<table><tr><td valign="top"><img src="Checkbox/preview.png" alt="Checkbox の見本（ライト）/ Checkbox preview, light" width="420"></td><td valign="top"><img src="Checkbox/preview-dark.png" alt="Checkbox の見本（ダーク）/ Checkbox preview, dark" width="420"></td></tr></table>

### Combobox

入力して候補を絞り込み、1 つを選ぶ欄。選択肢が多い（6 件以上）ときに使う。 → [Combobox/](Combobox/)

<table><tr><td valign="top"><img src="Combobox/preview.png" alt="Combobox の見本（ライト）/ Combobox preview, light" width="420"></td><td valign="top"><img src="Combobox/preview-dark.png" alt="Combobox の見本（ダーク）/ Combobox preview, dark" width="420"></td></tr></table>

### ConditionalField

前の答えによって必要になる欄を、その答えのすぐ下に出す。 → [ConditionalField/](ConditionalField/)

<table><tr><td valign="top"><img src="ConditionalField/preview.png" alt="ConditionalField の見本（ライト）/ ConditionalField preview, light" width="420"></td><td valign="top"><img src="ConditionalField/preview-dark.png" alt="ConditionalField の見本（ダーク）/ ConditionalField preview, dark" width="420"></td></tr></table>

### ErrorSummary

送信して誤りがあったとき、フォームの上に件数と誤りの一覧を出す。各行は該当の欄へのリンク。 → [ErrorSummary/](ErrorSummary/)

<table><tr><td valign="top"><img src="ErrorSummary/preview.png" alt="ErrorSummary の見本（ライト）/ ErrorSummary preview, light" width="420"></td><td valign="top"><img src="ErrorSummary/preview-dark.png" alt="ErrorSummary の見本（ダーク）/ ErrorSummary preview, dark" width="420"></td></tr></table>

### FileUpload

ファイルを選ぶ、またはドラッグして渡す欄。 → [FileUpload/](FileUpload/)

<table><tr><td valign="top"><img src="FileUpload/preview.png" alt="FileUpload の見本（ライト）/ FileUpload preview, light" width="420"></td><td valign="top"><img src="FileUpload/preview-dark.png" alt="FileUpload の見本（ダーク）/ FileUpload preview, dark" width="420"></td></tr></table>

### FormGrid

関係の強い短い欄を、広い画面でだけ 2 列に並べる。基本は 1 列。 → [FormGrid/](FormGrid/)

<table><tr><td valign="top"><img src="FormGrid/preview.png" alt="FormGrid の見本（ライト）/ FormGrid preview, light" width="420"></td><td valign="top"><img src="FormGrid/preview-dark.png" alt="FormGrid の見本（ダーク）/ FormGrid preview, dark" width="420"></td></tr></table>

### FormGroup

フォームの中の 1 つのまとまりに見出しを付ける。間隔は「欄の間 < グループの間」になるよう決めてあり、枠や背景は付けない。全体の決まりは「画面の組み立て › フォーム」。 → [FormGroup/](FormGroup/)

<table><tr><td valign="top"><img src="FormGroup/preview.png" alt="FormGroup の見本（ライト）/ FormGroup preview, light" width="420"></td><td valign="top"><img src="FormGroup/preview-dark.png" alt="FormGroup の見本（ダーク）/ FormGroup preview, dark" width="420"></td></tr></table>

### Input

1 行のテキスト入力。ラベルは常に表示し、プレースホルダをラベル代わりにしない。 → [Input/](Input/)

<table><tr><td valign="top"><img src="Input/preview.png" alt="Input の見本（ライト）/ Input preview, light" width="420"></td><td valign="top"><img src="Input/preview-dark.png" alt="Input の見本（ダーク）/ Input preview, dark" width="420"></td></tr></table>

### RadioGroup

選択肢が 5 件以下で、1 つだけを選ぶとき。`fieldset` と `legend` でグループの名前を付け、矢印キーで移動できる（標準のラジオボタン）。 → [RadioGroup/](RadioGroup/)

<table><tr><td valign="top"><img src="RadioGroup/preview.png" alt="RadioGroup の見本（ライト）/ RadioGroup preview, light" width="420"></td><td valign="top"><img src="RadioGroup/preview-dark.png" alt="RadioGroup の見本（ダーク）/ RadioGroup preview, dark" width="420"></td></tr></table>

### SearchBox

一覧や画面の中を探すための検索欄。 → [SearchBox/](SearchBox/)

<table><tr><td valign="top"><img src="SearchBox/preview.png" alt="SearchBox の見本（ライト）/ SearchBox preview, light" width="420"></td><td valign="top"><img src="SearchBox/preview-dark.png" alt="SearchBox の見本（ダーク）/ SearchBox preview, dark" width="420"></td></tr></table>

### Select

選択肢が 6 件以上のときに 1 つを選ぶ。ブラウザ標準の `<select>` を使うので、キーボードとスクリーンリーダーの操作は標準のまま動く。 → [Select/](Select/)

<table><tr><td valign="top"><img src="Select/preview.png" alt="Select の見本（ライト）/ Select preview, light" width="420"></td><td valign="top"><img src="Select/preview-dark.png" alt="Select の見本（ダーク）/ Select preview, dark" width="420"></td></tr></table>

### Slider

範囲の中から、だいたいの値を選ぶつまみ。音量、通知の何分前、表示の密度など。 → [Slider/](Slider/)

<table><tr><td valign="top"><img src="Slider/preview.png" alt="Slider の見本（ライト）/ Slider preview, light" width="420"></td><td valign="top"><img src="Slider/preview-dark.png" alt="Slider の見本（ダーク）/ Slider preview, dark" width="420"></td></tr></table>

### SpinButton

数を入れる欄。手で入力でき、−・＋や矢印キーで 1 つずつ増減できる。 → [SpinButton/](SpinButton/)

<table><tr><td valign="top"><img src="SpinButton/preview.png" alt="SpinButton の見本（ライト）/ SpinButton preview, light" width="420"></td><td valign="top"><img src="SpinButton/preview-dark.png" alt="SpinButton の見本（ダーク）/ SpinButton preview, dark" width="420"></td></tr></table>

### Switch

その場で効く設定のオン・オフ。押すとすぐ反映される。送信ボタンが要る設定には `Checkbox` を使う。 → [Switch/](Switch/)

<table><tr><td valign="top"><img src="Switch/preview.png" alt="Switch の見本（ライト）/ Switch preview, light" width="420"></td><td valign="top"><img src="Switch/preview-dark.png" alt="Switch の見本（ダーク）/ Switch preview, dark" width="420"></td></tr></table>

### TagPicker

候補から複数を選ぶ欄。選んだものはタグとして並び、1 つずつ外せる。 → [TagPicker/](TagPicker/)

<table><tr><td valign="top"><img src="TagPicker/preview.png" alt="TagPicker の見本（ライト）/ TagPicker preview, light" width="420"></td><td valign="top"><img src="TagPicker/preview-dark.png" alt="TagPicker の見本（ダーク）/ TagPicker preview, dark" width="420"></td></tr></table>

### Textarea

複数行の文章を入力する欄。メモ、説明、貼り付けた文章の取り込みに使う。 → [Textarea/](Textarea/)

<table><tr><td valign="top"><img src="Textarea/preview.png" alt="Textarea の見本（ライト）/ Textarea preview, light" width="420"></td><td valign="top"><img src="Textarea/preview-dark.png" alt="Textarea の見本（ダーク）/ Textarea preview, dark" width="420"></td></tr></table>


## 一覧と選択 / Lists and selection

### BottomSheet

狭い画面で、今の画面を保ったまま、補助の情報や選択肢を下から出す。モーダル（`modal`、既定）と持続型（`persistent`）がある。M1 の Bottom sheets を KM1 に合わせたもの。 → [BottomSheet/](BottomSheet/)

<table><tr><td valign="top"><img src="BottomSheet/preview.png" alt="BottomSheet の見本（ライト）/ BottomSheet preview, light" width="420"></td><td valign="top"><img src="BottomSheet/preview-dark.png" alt="BottomSheet の見本（ダーク）/ BottomSheet preview, dark" width="420"></td></tr></table>

### ContextualActionBar

選んだ対象にだけ効く操作をまとめたバー。選んでいる間だけ件数と操作が出る。`List`・`ImageGrid`・`Table` で共通（`Table` の一括操作もこの部品で描く）。選択の状態は `useSelection` で持てる。 → [ContextualActionBar/](ContextualActionBar/)

<table><tr><td valign="top"><img src="ContextualActionBar/preview.png" alt="ContextualActionBar の見本（ライト）/ ContextualActionBar preview, light" width="420"></td><td valign="top"><img src="ContextualActionBar/preview-dark.png" alt="ContextualActionBar の見本（ダーク）/ ContextualActionBar preview, dark" width="420"></td></tr></table>

### ExpansionEditor

一覧の中の 1 項目を、その場で開いて直す。閉じているときは項目名と今の値、開くと入力欄と「キャンセル」「保存」。M1 の Expansion panels の「軽い編集」を取り込んだもの。閲覧だけの開閉は `Accordion`。 → [ExpansionEditor/](ExpansionEditor/)

<table><tr><td valign="top"><img src="ExpansionEditor/preview.png" alt="ExpansionEditor の見本（ライト）/ ExpansionEditor preview, light" width="420"></td><td valign="top"><img src="ExpansionEditor/preview-dark.png" alt="ExpansionEditor の見本（ダーク）/ ExpansionEditor preview, dark" width="420"></td></tr></table>

### ImageGrid

写真やファイルのように、見た目で見分けるものを格子に並べる。タイル全体が主操作、選択のチェックは別の押し場所。M1 の Grid lists を KM1 に合わせたもの。 → [ImageGrid/](ImageGrid/)

<table><tr><td valign="top"><img src="ImageGrid/preview.png" alt="ImageGrid の見本（ライト）/ ImageGrid preview, light" width="420"></td><td valign="top"><img src="ImageGrid/preview-dark.png" alt="ImageGrid の見本（ダーク）/ ImageGrid preview, dark" width="420"></td></tr></table>

### List

同じ種類のものを縦に並べ、ざっと見て 1 つを選ぶ一覧。`List`・`ListItem`・`ListSection`（小見出しつきのまとまり）・`ListSectionHeader`（小見出しだけ）からなる。M1 の Lists・Lists: Controls・Subheaders の考え方を、KM1 の見た目で実装したもの（KM1-M1-001）。 → [List/](List/)

<table><tr><td valign="top"><img src="List/preview.png" alt="List の見本（ライト）/ List preview, light" width="420"></td><td valign="top"><img src="List/preview-dark.png" alt="List の見本（ダーク）/ List preview, dark" width="420"></td></tr></table>

### StepFlow

順序のある複数の工程を、利用者が入力しながら進める。工程の一覧（完了・現在・エラー・未完了）、今の工程の見出しと中身、「戻る」「次へ」。M1 の Steppers を KM1 に合わせたもの。システムの処理を待つ工程は `Progress`（`steps`）。 → [StepFlow/](StepFlow/)

<table><tr><td valign="top"><img src="StepFlow/preview.png" alt="StepFlow の見本（ライト）/ StepFlow preview, light" width="420"></td><td valign="top"><img src="StepFlow/preview-dark.png" alt="StepFlow の見本（ダーク）/ StepFlow preview, dark" width="420"></td></tr></table>


## データ / Data

### Avatar

人や場所を、写真か頭文字で小さく示す丸。 → [Avatar/](Avatar/)

<table><tr><td valign="top"><img src="Avatar/preview.png" alt="Avatar の見本（ライト）/ Avatar preview, light" width="420"></td><td valign="top"><img src="Avatar/preview-dark.png" alt="Avatar の見本（ダーク）/ Avatar preview, dark" width="420"></td></tr></table>

### CategoryPattern

分類を**色 × 模様**で区別するための部品。`cat-*` の 18 色に 8 つの模様（塗り・横線・縦線・斜線・格子・斜め格子・点・市松）を組み合わせ、144 通りにする。色が見分けにくい人や白黒の印刷でも、模様で区別できる（WCAG 1.4.1）。 → [CategoryPattern/](CategoryPattern/)

<table><tr><td valign="top"><img src="CategoryPattern/preview.png" alt="CategoryPattern の見本（ライト）/ CategoryPattern preview, light" width="420"></td><td valign="top"><img src="CategoryPattern/preview-dark.png" alt="CategoryPattern の見本（ダーク）/ CategoryPattern preview, dark" width="420"></td></tr></table>

### SortableList

順番を入れ替えられる一覧。優先順位、表示の順番、手順の並べ替えに使う。 → [SortableList/](SortableList/)

<table><tr><td valign="top"><img src="SortableList/preview.png" alt="SortableList の見本（ライト）/ SortableList preview, light" width="420"></td><td valign="top"><img src="SortableList/preview-dark.png" alt="SortableList の見本（ダーク）/ SortableList preview, dark" width="420"></td></tr></table>

### Table

行と列でデータを見比べる表。 → [Table/](Table/)

<table><tr><td valign="top"><img src="Table/preview.png" alt="Table の見本（ライト）/ Table preview, light" width="420"></td><td valign="top"><img src="Table/preview-dark.png" alt="Table の見本（ダーク）/ Table preview, dark" width="420"></td></tr></table>


## 日付と時間 / Date and time

### Calendar

月の表から日付を 1 つ選ぶ。予定のある日に印を付けられる。 → [Calendar/](Calendar/)

<table><tr><td valign="top"><img src="Calendar/preview.png" alt="Calendar の見本（ライト）/ Calendar preview, light" width="420"></td><td valign="top"><img src="Calendar/preview-dark.png" alt="Calendar の見本（ダーク）/ Calendar preview, dark" width="420"></td></tr></table>

### TimeGrid

1 日または 1 週間の予定を、時刻の縦軸に並べる予定表。 → [TimeGrid/](TimeGrid/)

<table><tr><td valign="top"><img src="TimeGrid/preview.png" alt="TimeGrid の見本（ライト）/ TimeGrid preview, light" width="420"></td><td valign="top"><img src="TimeGrid/preview-dark.png" alt="TimeGrid の見本（ダーク）/ TimeGrid preview, dark" width="420"></td></tr></table>

### Timetable

曜日 × 時限の時間割。授業やシフトのように、毎週同じ枠に入る予定を見せる。 → [Timetable/](Timetable/)

<table><tr><td valign="top"><img src="Timetable/preview.png" alt="Timetable の見本（ライト）/ Timetable preview, light" width="420"></td><td valign="top"><img src="Timetable/preview-dark.png" alt="Timetable の見本（ダーク）/ Timetable preview, dark" width="420"></td></tr></table>


## ナビゲーション / Navigation

### Breadcrumb

今いる画面が、全体のどこにあるかを示す道しるべ。3 階層以上ある画面で使う。 → [Breadcrumb/](Breadcrumb/)

<table><tr><td valign="top"><img src="Breadcrumb/preview.png" alt="Breadcrumb の見本（ライト）/ Breadcrumb preview, light" width="420"></td><td valign="top"><img src="Breadcrumb/preview-dark.png" alt="Breadcrumb の見本（ダーク）/ Breadcrumb preview, dark" width="420"></td></tr></table>

### Link

文中・文末のテキストリンク。常に下線を付け、色だけでリンクと分からせない。 → [Link/](Link/)

<table><tr><td valign="top"><img src="Link/preview.png" alt="Link の見本（ライト）/ Link preview, light" width="420"></td><td valign="top"><img src="Link/preview-dark.png" alt="Link の見本（ダーク）/ Link preview, dark" width="420"></td></tr></table>

### Nav

画面を切り替えるメインのナビゲーション。狭い画面では下部のタブ、広い画面ではサイドバーになる。 → [Nav/](Nav/)

<table><tr><td valign="top"><img src="Nav/preview.png" alt="Nav の見本（ライト）/ Nav preview, light" width="420"></td><td valign="top"><img src="Nav/preview-dark.png" alt="Nav の見本（ダーク）/ Nav preview, dark" width="420"></td></tr></table>

### Pagination

長い一覧をページに分けたときの、ページの移動。 → [Pagination/](Pagination/)

<table><tr><td valign="top"><img src="Pagination/preview.png" alt="Pagination の見本（ライト）/ Pagination preview, light" width="420"></td><td valign="top"><img src="Pagination/preview-dark.png" alt="Pagination の見本（ダーク）/ Pagination preview, dark" width="420"></td></tr></table>

### Tabs

同じ階層の内容を切り替える。タブの並びは 2〜6 個まで。ページ遷移にはリンクを使う。 → [Tabs/](Tabs/)

<table><tr><td valign="top"><img src="Tabs/preview.png" alt="Tabs の見本（ライト）/ Tabs preview, light" width="420"></td><td valign="top"><img src="Tabs/preview-dark.png" alt="Tabs の見本（ダーク）/ Tabs preview, dark" width="420"></td></tr></table>


## 入れ物 / Containers

### Accordion

見出しを押して、中身を開いたり閉じたりする一覧。よくある質問、設定のまとまり、長い説明の折りたたみに使う。 → [Accordion/](Accordion/)

<table><tr><td valign="top"><img src="Accordion/preview.png" alt="Accordion の見本（ライト）/ Accordion preview, light" width="420"></td><td valign="top"><img src="Accordion/preview-dark.png" alt="Accordion の見本（ダーク）/ Accordion preview, dark" width="420"></td></tr></table>


## 面 / Surfaces

### Card

関連する情報をまとめる面。`surface` 上に `stroke` の 1px の縁、`radius-lg`、内側は `container-card-padding-regular`（= `space-lg`）。影は付けない。 → [Card/](Card/)

<table><tr><td valign="top"><img src="Card/preview.png" alt="Card の見本（ライト）/ Card preview, light" width="420"></td><td valign="top"><img src="Card/preview-dark.png" alt="Card の見本（ダーク）/ Card preview, dark" width="420"></td></tr></table>


## 重ねて出すもの / Overlays

### Dialog

確認や短い入力のために、画面の上に重ねて出す。元の操作を止めてでも判断してほしいときだけ使う。 → [Dialog/](Dialog/)

<table><tr><td valign="top"><img src="Dialog/preview.png" alt="Dialog の見本（ライト）/ Dialog preview, light" width="420"></td><td valign="top"><img src="Dialog/preview-dark.png" alt="Dialog の見本（ダーク）/ Dialog preview, dark" width="420"></td></tr></table>

### Drawer

画面の端から出る大きめのパネル。絞り込みの条件、詳細、少し長い設定に使う。 → [Drawer/](Drawer/)

<table><tr><td valign="top"><img src="Drawer/preview.png" alt="Drawer の見本（ライト）/ Drawer preview, light" width="420"></td><td valign="top"><img src="Drawer/preview-dark.png" alt="Drawer の見本（ダーク）/ Drawer preview, dark" width="420"></td></tr></table>

### Popover

ボタンの近くに出る、小さな作業用のパネル。表示の設定、短い補足、2〜3 項目の入力に使う。 → [Popover/](Popover/)

<table><tr><td valign="top"><img src="Popover/preview.png" alt="Popover の見本（ライト）/ Popover preview, light" width="420"></td><td valign="top"><img src="Popover/preview-dark.png" alt="Popover の見本（ダーク）/ Popover preview, dark" width="420"></td></tr></table>

### Tooltip

部品にマウスを乗せるかフォーカスしたときに出る、短い補足。 → [Tooltip/](Tooltip/)

<table><tr><td valign="top"><img src="Tooltip/preview.png" alt="Tooltip の見本（ライト）/ Tooltip preview, light" width="420"></td><td valign="top"><img src="Tooltip/preview-dark.png" alt="Tooltip の見本（ダーク）/ Tooltip preview, dark" width="420"></td></tr></table>


## 知らせ / Feedback

### EmptyState

まだ何も無い場所に出す案内。何が入る場所かと、最初の一歩を伝える。中身が入るはずの場所に、左寄せの文で置く。 → [EmptyState/](EmptyState/)

<table><tr><td valign="top"><img src="EmptyState/preview.png" alt="EmptyState の見本（ライト）/ EmptyState preview, light" width="420"></td><td valign="top"><img src="EmptyState/preview-dark.png" alt="EmptyState の見本（ダーク）/ EmptyState preview, dark" width="420"></td></tr></table>

### Progress

進み具合や量を横棒で示す。処理の進行、達成度、ゲームのゲージに使う。 → [Progress/](Progress/)

<table><tr><td valign="top"><img src="Progress/preview.png" alt="Progress の見本（ライト）/ Progress preview, light" width="420"></td><td valign="top"><img src="Progress/preview-dark.png" alt="Progress の見本（ダーク）/ Progress preview, dark" width="420"></td></tr></table>

### Skeleton

読み込み中に、これから出る内容のおおよその形を灰色で見せる。 → [Skeleton/](Skeleton/)

<table><tr><td valign="top"><img src="Skeleton/preview.png" alt="Skeleton の見本（ライト）/ Skeleton preview, light" width="420"></td><td valign="top"><img src="Skeleton/preview-dark.png" alt="Skeleton の見本（ダーク）/ Skeleton preview, dark" width="420"></td></tr></table>

### Spinner

短い待ち時間を示す回転する輪。ボタンの横や一覧の読み込み中に使う。 → [Spinner/](Spinner/)

<table><tr><td valign="top"><img src="Spinner/preview.png" alt="Spinner の見本（ライト）/ Spinner preview, light" width="420"></td><td valign="top"><img src="Spinner/preview-dark.png" alt="Spinner の見本（ダーク）/ Spinner preview, dark" width="420"></td></tr></table>

### Toast

操作の結果や時刻の通知を、画面の下に一時的に出すお知らせ。 → [Toast/](Toast/)

<table><tr><td valign="top"><img src="Toast/preview.png" alt="Toast の見本（ライト）/ Toast preview, light" width="420"></td><td valign="top"><img src="Toast/preview-dark.png" alt="Toast の見本（ダーク）/ Toast preview, dark" width="420"></td></tr></table>


## 状態 / Status

### Alert

状態をユーザーに知らせるバナー。色に加えて、アイコンと「情報」「成功」「注意」「エラー」の文言を必ず併記する。 → [Alert/](Alert/)

<table><tr><td valign="top"><img src="Alert/preview.png" alt="Alert の見本（ライト）/ Alert preview, light" width="420"></td><td valign="top"><img src="Alert/preview-dark.png" alt="Alert の見本（ダーク）/ Alert preview, dark" width="420"></td></tr></table>

### Badge

状態や件数を示す小さなラベル。丸型（`radius-circular`）。 → [Badge/](Badge/)

<table><tr><td valign="top"><img src="Badge/preview.png" alt="Badge の見本（ライト）/ Badge preview, light" width="420"></td><td valign="top"><img src="Badge/preview-dark.png" alt="Badge の見本（ダーク）/ Badge preview, dark" width="420"></td></tr></table>


## アイコン / Icons

### AppIcon

KM1 のアプリアイコンとファビコン（KM1-ICO-001 §6）。紺（`brand`）の正方形に白の「KM1」と表紙のしるし。`icons/km1_appicon.py` が 1 枚の元の絵から Web・Android・iOS・Windows の大きさを全部書き出す。 → [AppIcon/](AppIcon/)

<table><tr><td valign="top"><img src="AppIcon/preview.png" alt="AppIcon の見本（ライト）/ AppIcon preview, light" width="420"></td><td valign="top"><img src="AppIcon/preview-dark.png" alt="AppIcon の見本（ダーク）/ AppIcon preview, dark" width="420"></td></tr></table>

### Icon

KM1 のアイコン（KM1-ICO-001）。KM1 の名前で引く 1 つのセットで、通常表示（線と淡い面）も選択・強調の塗りの形（Filled）も KM1 B 案で KM1 が描いた形（もとにした絵は Fluent System Icons、Microsoft、MIT）。描き方と一覧は本編「アイコン」の章。 → [Icon/](Icon/)

<table><tr><td valign="top"><img src="Icon/preview.png" alt="Icon の見本（ライト）/ Icon preview, light" width="420"></td><td valign="top"><img src="Icon/preview-dark.png" alt="Icon の見本（ダーク）/ Icon preview, dark" width="420"></td></tr></table>

### IconTrial

KM1 B 案（調整版）の導入前と導入後の比較（KM1-ICO-001 §8）。試験導入した 6 種（検索・予定・フォルダ・削除・警告・通知）で見比べる。いまは全アイコンの通常表示が B 案。通常の `Icon` の呼び出し（`h(Icon,{name:'calendar'})`）でそのまま出る。 → [IconTrial/](IconTrial/)

<table><tr><td valign="top"><img src="IconTrial/preview.png" alt="IconTrial の見本（ライト）/ IconTrial preview, light" width="420"></td><td valign="top"><img src="IconTrial/preview-dark.png" alt="IconTrial の見本（ダーク）/ IconTrial preview, dark" width="420"></td></tr></table>


## 密度 / Density

### Density

Card・Table・SortableList の 3 つの密度（compact・regular・spacious）を同じ画面で比べる見本。決まりは「トークン › 密度」（`tokens.md`）。 → [Density/](Density/)

<table><tr><td valign="top"><img src="Density/preview.png" alt="Density の見本（ライト）/ Density preview, light" width="420"></td><td valign="top"><img src="Density/preview-dark.png" alt="Density の見本（ダーク）/ Density preview, dark" width="420"></td></tr></table>


## 画面の例 / Screen patterns

### ScreenAddEvent

一覧と「予定を追加」ボタン、ドロワーの中のフォーム（エラーの一覧つき）、追加のお知らせ（Toast）を組み合わせた画面の例。 → [ScreenAddEvent/](ScreenAddEvent/)

<table><tr><td valign="top"><img src="ScreenAddEvent/preview.png" alt="ScreenAddEvent の見本（ライト）/ ScreenAddEvent preview, light" width="420"></td><td valign="top"><img src="ScreenAddEvent/preview-dark.png" alt="ScreenAddEvent の見本（ダーク）/ ScreenAddEvent preview, dark" width="420"></td></tr></table>

### ScreenListEdit

一覧・詳細・編集の組み合わせの例: 左の一覧で選び、右でその場の編集（ExpansionEditor）、まとめて削除は確認（Dialog）と「元に戻す」（Toast）。 → [ScreenListEdit/](ScreenListEdit/)

<table><tr><td valign="top"><img src="ScreenListEdit/preview.png" alt="ScreenListEdit の見本（ライト）/ ScreenListEdit preview, light" width="420"></td><td valign="top"><img src="ScreenListEdit/preview-dark.png" alt="ScreenListEdit の見本（ダーク）/ ScreenListEdit preview, dark" width="420"></td></tr></table>

### ScreenOffline

通信が切れたときの画面の例: 警告（Alert）、時点の表示、未送信の件数、つながったら自動で送ってお知らせ（Toast）。 → [ScreenOffline/](ScreenOffline/)

<table><tr><td valign="top"><img src="ScreenOffline/preview.png" alt="ScreenOffline の見本（ライト）/ ScreenOffline preview, light" width="420"></td><td valign="top"><img src="ScreenOffline/preview-dark.png" alt="ScreenOffline の見本（ダーク）/ ScreenOffline preview, dark" width="420"></td></tr></table>

### ScreenToday

スケジュール確認アプリの「今日」の画面の例。「画面の組み立て › わかりやすさ」の順番で、部品からではなく、開いた人が最初に知りたいことから作った。 → [ScreenToday/](ScreenToday/)

<table><tr><td valign="top"><img src="ScreenToday/preview.png" alt="ScreenToday の見本（ライト）/ ScreenToday preview, light" width="420"></td><td valign="top"><img src="ScreenToday/preview-dark.png" alt="ScreenToday の見本（ダーク）/ ScreenToday preview, dark" width="420"></td></tr></table>


## M1 比較 / M1 comparison

### CompareBottomSheet

M1（初代 Material Design）の原型を寸法から再描画したもの（左）と、KM1 に合わせた案（右）の比較。左は公式の画像ではなく、出典の寸法をもとに KM1 が描いた参考の再現。判断の理由は「KM1 × M1」（`m1.md`）。 → [CompareBottomSheet/](CompareBottomSheet/)

<table><tr><td valign="top"><img src="CompareBottomSheet/preview.png" alt="CompareBottomSheet の見本（ライト）/ CompareBottomSheet preview, light" width="420"></td><td valign="top"><img src="CompareBottomSheet/preview-dark.png" alt="CompareBottomSheet の見本（ダーク）/ CompareBottomSheet preview, dark" width="420"></td></tr></table>

### CompareExpansion

M1（初代 Material Design）の原型を寸法から再描画したもの（左）と、KM1 に合わせた案（右）の比較。左は公式の画像ではなく、出典の寸法をもとに KM1 が描いた参考の再現。判断の理由は「KM1 × M1」（`m1.md`）。 → [CompareExpansion/](CompareExpansion/)

<table><tr><td valign="top"><img src="CompareExpansion/preview.png" alt="CompareExpansion の見本（ライト）/ CompareExpansion preview, light" width="420"></td><td valign="top"><img src="CompareExpansion/preview-dark.png" alt="CompareExpansion の見本（ダーク）/ CompareExpansion preview, dark" width="420"></td></tr></table>

### CompareFAB

M1（初代 Material Design）の原型を寸法から再描画したもの（左）と、KM1 に合わせた案（右）の比較。左は公式の画像ではなく、出典の寸法をもとに KM1 が描いた参考の再現。判断の理由は「KM1 × M1」（`m1.md`）。 → [CompareFAB/](CompareFAB/)

<table><tr><td valign="top"><img src="CompareFAB/preview.png" alt="CompareFAB の見本（ライト）/ CompareFAB preview, light" width="420"></td><td valign="top"><img src="CompareFAB/preview-dark.png" alt="CompareFAB の見本（ダーク）/ CompareFAB preview, dark" width="420"></td></tr></table>

### CompareGrid

M1（初代 Material Design）の原型を寸法から再描画したもの（左）と、KM1 に合わせた案（右）の比較。左は公式の画像ではなく、出典の寸法をもとに KM1 が描いた参考の再現。判断の理由は「KM1 × M1」（`m1.md`）。 → [CompareGrid/](CompareGrid/)

<table><tr><td valign="top"><img src="CompareGrid/preview.png" alt="CompareGrid の見本（ライト）/ CompareGrid preview, light" width="420"></td><td valign="top"><img src="CompareGrid/preview-dark.png" alt="CompareGrid の見本（ダーク）/ CompareGrid preview, dark" width="420"></td></tr></table>

### CompareList

M1（初代 Material Design）の原型を寸法から再描画したもの（左）と、KM1 に合わせた案（右）の比較。左は公式の画像ではなく、出典の寸法をもとに KM1 が描いた参考の再現。判断の理由は「KM1 × M1」（`m1.md`）。 → [CompareList/](CompareList/)

<table><tr><td valign="top"><img src="CompareList/preview.png" alt="CompareList の見本（ライト）/ CompareList preview, light" width="420"></td><td valign="top"><img src="CompareList/preview-dark.png" alt="CompareList の見本（ダーク）/ CompareList preview, dark" width="420"></td></tr></table>

### CompareSelection

M1（初代 Material Design）の原型を寸法から再描画したもの（左）と、KM1 に合わせた案（右）の比較。左は公式の画像ではなく、出典の寸法をもとに KM1 が描いた参考の再現。判断の理由は「KM1 × M1」（`m1.md`）。 → [CompareSelection/](CompareSelection/)

<table><tr><td valign="top"><img src="CompareSelection/preview.png" alt="CompareSelection の見本（ライト）/ CompareSelection preview, light" width="420"></td><td valign="top"><img src="CompareSelection/preview-dark.png" alt="CompareSelection の見本（ダーク）/ CompareSelection preview, dark" width="420"></td></tr></table>

### CompareStepper

M1（初代 Material Design）の原型を寸法から再描画したもの（左）と、KM1 に合わせた案（右）の比較。左は公式の画像ではなく、出典の寸法をもとに KM1 が描いた参考の再現。判断の理由は「KM1 × M1」（`m1.md`）。 → [CompareStepper/](CompareStepper/)

<table><tr><td valign="top"><img src="CompareStepper/preview.png" alt="CompareStepper の見本（ライト）/ CompareStepper preview, light" width="420"></td><td valign="top"><img src="CompareStepper/preview-dark.png" alt="CompareStepper の見本（ダーク）/ CompareStepper preview, dark" width="420"></td></tr></table>

### SelectionGuide

部品の選び方の早見図。「何をしたいか」から部品を選ぶ。文章版は「KM1 × M1」（`m1.md`）の「用途選択フロー」。 → [SelectionGuide/](SelectionGuide/)

<table><tr><td valign="top"><img src="SelectionGuide/preview.png" alt="SelectionGuide の見本（ライト）/ SelectionGuide preview, light" width="420"></td><td valign="top"><img src="SelectionGuide/preview-dark.png" alt="SelectionGuide の見本（ダーク）/ SelectionGuide preview, dark" width="420"></td></tr></table>
