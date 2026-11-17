# KM1 部品カタログ / Component catalog

各部品の説明は部品フォルダの `README.md`、動く見本は `preview.html`（`gen/render_previews.py` で単独のページにできる）。下の画像は `gen/shoot_previews.js` で撮ったライトテーマの見本。PDF 版は `dist/KM1_部品カタログ.pdf`。
*Each folder has a README and a live `preview.html`; images below are light-theme screenshots. PDF: `dist/KM1_部品カタログ.pdf`.*

### [Accordion](Accordion/)

見出しを押して、中身を開いたり閉じたりする一覧。よくある質問、設定のまとまり、長い説明の折りたたみに使う。

![Accordion の見本 / Accordion preview](Accordion/preview.png)

### [Alert](Alert/)

状態をユーザーに知らせるバナー。色に加えて、アイコンと「情報」「成功」「注意」「エラー」の文言を必ず併記する。

![Alert の見本 / Alert preview](Alert/preview.png)

### [AppIcon](AppIcon/)

KM1 のアプリアイコンとファビコン（KM1-ICO-001 §6）。紺（`brand`）の正方形に白の「KM1」と表紙のしるし。`icons/km1_appicon.py` が 

![AppIcon の見本 / AppIcon preview](AppIcon/preview.png)

### [Avatar](Avatar/)

人や場所を、写真か頭文字で小さく示す丸。

![Avatar の見本 / Avatar preview](Avatar/preview.png)

### [Badge](Badge/)

状態や件数を示す小さなラベル。丸型（`radius-circular`）。

![Badge の見本 / Badge preview](Badge/preview.png)

### [BottomSheet](BottomSheet/)

狭い画面で、今の画面を保ったまま、補助の情報や選択肢を下から出す。モーダル（`modal`、既定）と持続型（`persistent`）がある。M1 の Bottom sheets 

![BottomSheet の見本 / BottomSheet preview](BottomSheet/preview.png)

### [Breadcrumb](Breadcrumb/)

今いる画面が、全体のどこにあるかを示す道しるべ。3 階層以上ある画面で使う。

![Breadcrumb の見本 / Breadcrumb preview](Breadcrumb/preview.png)

### [Button](Button/)

操作を実行するボタン。1 画面にプライマリ（`appearance="primary"`）は 1 つだけ。

![Button の見本 / Button preview](Button/preview.png)

### [Calendar](Calendar/)

月の表から日付を 1 つ選ぶ。予定のある日に印を付けられる。

![Calendar の見本 / Calendar preview](Calendar/preview.png)

### [Card](Card/)

関連する情報をまとめる面。`surface` 上に `shadow-2`、`radius-lg`、内側は `container-card-padding-regular`（= `s

![Card の見本 / Card preview](Card/preview.png)

### [CategoryPattern](CategoryPattern/)

分類を**色 × 模様**で区別するための部品。`cat-*` の 18 色に 8 つの模様（塗り・横線・縦線・斜線・格子・斜め格子・点・市松）を組み合わせ、144 通りにする。色

![CategoryPattern の見本 / CategoryPattern preview](CategoryPattern/preview.png)

### [Checkbox](Checkbox/)

複数選択や同意のためのチェックボックス。ラベルは必ず付け、ラベルをクリックしても切り替わる。

![Checkbox の見本 / Checkbox preview](Checkbox/preview.png)

### [Chip](Chip/)

押して切り替える小さな絞り込みボタン。一覧のフィルターや、複数選べる分類に使う。

![Chip の見本 / Chip preview](Chip/preview.png)

### [Combobox](Combobox/)

入力して候補を絞り込み、1 つを選ぶ欄。選択肢が多い（6 件以上）ときに使う。

![Combobox の見本 / Combobox preview](Combobox/preview.png)

### [CompareBottomSheet](CompareBottomSheet/)

M1（初代 Material Design）の原型を寸法から再描画したもの（左）と、KM1 に合わせた案（右）の比較。左は公式の画像ではなく、出典の寸法をもとに KM1 が描いた参

![CompareBottomSheet の見本 / CompareBottomSheet preview](CompareBottomSheet/preview.png)

### [CompareExpansion](CompareExpansion/)

M1（初代 Material Design）の原型を寸法から再描画したもの（左）と、KM1 に合わせた案（右）の比較。左は公式の画像ではなく、出典の寸法をもとに KM1 が描いた参

![CompareExpansion の見本 / CompareExpansion preview](CompareExpansion/preview.png)

### [CompareFAB](CompareFAB/)

M1（初代 Material Design）の原型を寸法から再描画したもの（左）と、KM1 に合わせた案（右）の比較。左は公式の画像ではなく、出典の寸法をもとに KM1 が描いた参

![CompareFAB の見本 / CompareFAB preview](CompareFAB/preview.png)

### [CompareGrid](CompareGrid/)

M1（初代 Material Design）の原型を寸法から再描画したもの（左）と、KM1 に合わせた案（右）の比較。左は公式の画像ではなく、出典の寸法をもとに KM1 が描いた参

![CompareGrid の見本 / CompareGrid preview](CompareGrid/preview.png)

### [CompareList](CompareList/)

M1（初代 Material Design）の原型を寸法から再描画したもの（左）と、KM1 に合わせた案（右）の比較。左は公式の画像ではなく、出典の寸法をもとに KM1 が描いた参

![CompareList の見本 / CompareList preview](CompareList/preview.png)

### [CompareSelection](CompareSelection/)

M1（初代 Material Design）の原型を寸法から再描画したもの（左）と、KM1 に合わせた案（右）の比較。左は公式の画像ではなく、出典の寸法をもとに KM1 が描いた参

![CompareSelection の見本 / CompareSelection preview](CompareSelection/preview.png)

### [CompareStepper](CompareStepper/)

M1（初代 Material Design）の原型を寸法から再描画したもの（左）と、KM1 に合わせた案（右）の比較。左は公式の画像ではなく、出典の寸法をもとに KM1 が描いた参

![CompareStepper の見本 / CompareStepper preview](CompareStepper/preview.png)

### [ConditionalField](ConditionalField/)

前の答えによって必要になる欄を、その答えのすぐ下に出す。

![ConditionalField の見本 / ConditionalField preview](ConditionalField/preview.png)

### [ContextualActionBar](ContextualActionBar/)

選んだ対象にだけ効く操作をまとめたバー。選んでいる間だけ件数と操作が出る。`List`・`ImageGrid`・`Table` で共通（`Table` の一括操作もこの部品で描く）

![ContextualActionBar の見本 / ContextualActionBar preview](ContextualActionBar/preview.png)

### [Cover](Cover/)



![Cover の見本 / Cover preview](Cover/preview.png)

### [Density](Density/)

Card・Table・SortableList の 3 つの密度（compact・regular・spacious）を同じ画面で比べる見本。決まりは「トークン › 密度」（`tok

![Density の見本 / Density preview](Density/preview.png)

### [Dialog](Dialog/)

確認や短い入力のために、画面の上に重ねて出す。元の操作を止めてでも判断してほしいときだけ使う。

![Dialog の見本 / Dialog preview](Dialog/preview.png)

### [Drawer](Drawer/)

画面の端から出る大きめのパネル。絞り込みの条件、詳細、少し長い設定に使う。

![Drawer の見本 / Drawer preview](Drawer/preview.png)

### [EmptyState](EmptyState/)

まだ何も無い場所に出す案内。何が入る場所かと、最初の一歩を伝える。

![EmptyState の見本 / EmptyState preview](EmptyState/preview.png)

### [ErrorSummary](ErrorSummary/)

送信して誤りがあったとき、フォームの上に件数と誤りの一覧を出す。各行は該当の欄へのリンク。

![ErrorSummary の見本 / ErrorSummary preview](ErrorSummary/preview.png)

### [ExpansionEditor](ExpansionEditor/)

一覧の中の 1 項目を、その場で開いて直す。閉じているときは項目名と今の値、開くと入力欄と「キャンセル」「保存」。M1 の Expansion panels の「軽い編集」を取り込

![ExpansionEditor の見本 / ExpansionEditor preview](ExpansionEditor/preview.png)

### [FileUpload](FileUpload/)

ファイルを選ぶ、またはドラッグして渡す欄。

![FileUpload の見本 / FileUpload preview](FileUpload/preview.png)

### [FormGrid](FormGrid/)

関係の強い短い欄を、広い画面でだけ 2 列に並べる。基本は 1 列。

![FormGrid の見本 / FormGrid preview](FormGrid/preview.png)

### [FormGroup](FormGroup/)

フォームの中の 1 つのまとまりに見出しを付ける。間隔は「欄の間 < グループの間」になるよう決めてあり、枠や背景は付けない。全体の決まりは「画面の組み立て › フォーム」。

![FormGroup の見本 / FormGroup preview](FormGroup/preview.png)

### [Icon](Icon/)

KM1 のアイコン（KM1-ICO-001）。KM1 の名前で引く 1 つのセットで、通常表示（線と淡い面）も選択・強調の塗りの形（Filled）も KM1 B 案で KM1 が描

![Icon の見本 / Icon preview](Icon/preview.png)

### [IconTrial](IconTrial/)

KM1 B 案（調整版）の導入前と導入後の比較（KM1-ICO-001 §8）。試験導入した 6 種（検索・予定・フォルダ・削除・警告・通知）で見比べる。いまは全アイコンの通常表示

![IconTrial の見本 / IconTrial preview](IconTrial/preview.png)

### [ImageGrid](ImageGrid/)

写真やファイルのように、見た目で見分けるものを格子に並べる。タイル全体が主操作、選択のチェックは別の押し場所。M1 の Grid lists を KM1 に合わせたもの。

![ImageGrid の見本 / ImageGrid preview](ImageGrid/preview.png)

### [Input](Input/)

1 行のテキスト入力。ラベルは常に表示し、プレースホルダをラベル代わりにしない。

![Input の見本 / Input preview](Input/preview.png)

### [Link](Link/)

文中・文末のテキストリンク。常に下線を付け、色だけでリンクと分からせない。

![Link の見本 / Link preview](Link/preview.png)

### [List](List/)

同じ種類のものを縦に並べ、ざっと見て 1 つを選ぶ一覧。`List`・`ListItem`・`ListSection`（小見出しつきのまとまり）・`ListSectionHeade

![List の見本 / List preview](List/preview.png)

### [Menu](Menu/)

ボタンを押すと開く操作の一覧。場所を取らずに、頻度の低い操作をまとめる。

![Menu の見本 / Menu preview](Menu/preview.png)

### [Nav](Nav/)

画面を切り替えるメインのナビゲーション。狭い画面では下部のタブ、広い画面ではサイドバーになる。

![Nav の見本 / Nav preview](Nav/preview.png)

### [Pagination](Pagination/)

長い一覧をページに分けたときの、ページの移動。

![Pagination の見本 / Pagination preview](Pagination/preview.png)

### [Popover](Popover/)

ボタンの近くに出る、小さな作業用のパネル。表示の設定、短い補足、2〜3 項目の入力に使う。

![Popover の見本 / Popover preview](Popover/preview.png)

### [Progress](Progress/)

進み具合や量を横棒で示す。処理の進行、達成度、ゲームのゲージに使う。

![Progress の見本 / Progress preview](Progress/preview.png)

### [RadioGroup](RadioGroup/)

選択肢が 5 件以下で、1 つだけを選ぶとき。`fieldset` と `legend` でグループの名前を付け、矢印キーで移動できる（標準のラジオボタン）。

![RadioGroup の見本 / RadioGroup preview](RadioGroup/preview.png)

### [ScreenAddEvent](ScreenAddEvent/)

一覧と「予定を追加」ボタン、ドロワーの中のフォーム（エラーの一覧つき）、追加のお知らせ（Toast）を組み合わせた画面の例。

![ScreenAddEvent の見本 / ScreenAddEvent preview](ScreenAddEvent/preview.png)

### [ScreenListEdit](ScreenListEdit/)

一覧・詳細・編集の組み合わせの例: 左の一覧で選び、右でその場の編集（ExpansionEditor）、まとめて削除は確認（Dialog）と「元に戻す」（Toast）。

![ScreenListEdit の見本 / ScreenListEdit preview](ScreenListEdit/preview.png)

### [ScreenOffline](ScreenOffline/)

通信が切れたときの画面の例: 警告（Alert）、時点の表示、未送信の件数、つながったら自動で送ってお知らせ（Toast）。

![ScreenOffline の見本 / ScreenOffline preview](ScreenOffline/preview.png)

### [SearchBox](SearchBox/)

一覧や画面の中を探すための検索欄。

![SearchBox の見本 / SearchBox preview](SearchBox/preview.png)

### [Select](Select/)

選択肢が 6 件以上のときに 1 つを選ぶ。ブラウザ標準の `<select>` を使うので、キーボードとスクリーンリーダーの操作は標準のまま動く。

![Select の見本 / Select preview](Select/preview.png)

### [SelectionGuide](SelectionGuide/)

部品の選び方の早見図。「何をしたいか」から部品を選ぶ。文章版は「KM1 × M1」（`m1.md`）の「用途選択フロー」。

![SelectionGuide の見本 / SelectionGuide preview](SelectionGuide/preview.png)

### [Skeleton](Skeleton/)

読み込み中に、これから出る内容のおおよその形を灰色で見せる。

![Skeleton の見本 / Skeleton preview](Skeleton/preview.png)

### [Slider](Slider/)

範囲の中から、だいたいの値を選ぶつまみ。音量、通知の何分前、表示の密度など。

![Slider の見本 / Slider preview](Slider/preview.png)

### [SortableList](SortableList/)

順番を入れ替えられる一覧。優先順位、表示の順番、手順の並べ替えに使う。

![SortableList の見本 / SortableList preview](SortableList/preview.png)

### [SpinButton](SpinButton/)

数を入れる欄。手で入力でき、−・＋や矢印キーで 1 つずつ増減できる。

![SpinButton の見本 / SpinButton preview](SpinButton/preview.png)

### [Spinner](Spinner/)

短い待ち時間を示す回転する輪。ボタンの横や一覧の読み込み中に使う。

![Spinner の見本 / Spinner preview](Spinner/preview.png)

### [StepFlow](StepFlow/)

順序のある複数の工程を、利用者が入力しながら進める。工程の一覧（完了・現在・エラー・未完了）、今の工程の見出しと中身、「戻る」「次へ」。M1 の Steppers を KM1 に合

![StepFlow の見本 / StepFlow preview](StepFlow/preview.png)

### [Switch](Switch/)

その場で効く設定のオン・オフ。押すとすぐ反映される。送信ボタンが要る設定には `Checkbox` を使う。

![Switch の見本 / Switch preview](Switch/preview.png)

### [Table](Table/)

行と列でデータを見比べる表。

![Table の見本 / Table preview](Table/preview.png)

### [Tabs](Tabs/)

同じ階層の内容を切り替える。タブの並びは 2〜6 個まで。ページ遷移にはリンクを使う。

![Tabs の見本 / Tabs preview](Tabs/preview.png)

### [TagPicker](TagPicker/)

候補から複数を選ぶ欄。選んだものはタグとして並び、1 つずつ外せる。

![TagPicker の見本 / TagPicker preview](TagPicker/preview.png)

### [Textarea](Textarea/)

複数行の文章を入力する欄。メモ、説明、貼り付けた文章の取り込みに使う。

![Textarea の見本 / Textarea preview](Textarea/preview.png)

### [TimeGrid](TimeGrid/)

1 日または 1 週間の予定を、時刻の縦軸に並べる予定表。

![TimeGrid の見本 / TimeGrid preview](TimeGrid/preview.png)

### [Timetable](Timetable/)

曜日 × 時限の時間割。授業やシフトのように、毎週同じ枠に入る予定を見せる。

![Timetable の見本 / Timetable preview](Timetable/preview.png)

### [Toast](Toast/)

操作の結果や時刻の通知を、画面の下に一時的に出すお知らせ。

![Toast の見本 / Toast preview](Toast/preview.png)

### [Toolbar](Toolbar/)

一覧や編集画面の上に、よく使う操作を横に並べる帯。

![Toolbar の見本 / Toolbar preview](Toolbar/preview.png)

### [Tooltip](Tooltip/)

部品にマウスを乗せるかフォーカスしたときに出る、短い補足。

![Tooltip の見本 / Tooltip preview](Tooltip/preview.png)
