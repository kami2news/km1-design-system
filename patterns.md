# 画面の組み立て / Patterns

部品より大きい単位の決まり。スケジュール確認アプリ（Flutter）で実際に使っている組み立てを、KM1 のトークンに合わせて一般化した。出典のあるもの（Fluent 2 のブレークポイント・動き・重なり順、デジタル庁のボタン配置）以外は、KM1 独自のアレンジである。
*Rules above the component level, generalized from the layouts actually used in the schedule-check Flutter app and aligned to KM1 tokens. Apart from sourced items (Fluent 2 breakpoints, motion and layers; Digital Agency button placement) these are KM1's own arrangements.*

## わかりやすさ / Understandability

「デザイン原則」の軸 2「わかりやすい」を、画面の決まりにしたもの。画面は部品を並べて作るのではなく、その画面を開いた人が最初に知りたいことから上に向かって決める。
*Axis 2 of the principles, as screen rules. Build a screen from what its reader needs first, not by lining up parts.*

**作る順番 / Order of work**

1. その画面を開いた人が最初に知りたいことを 1 つ決める。それが主役になる。
2. 次にすることを 1 つ決める。それが主ボタンになる（1 画面に 1 つ）。
3. 残りの情報をまとまりに分け、主役から遠い順に下げていく。
4. 足りない部品があれば作る。部品から先に作らない。
*Pick the one thing the reader needs first (the focal point), then the one next step (the primary button), then group the rest by distance from the focal point. Build missing parts last.*

**主役 / Focal point**

- 主役は、画面の中でいちばん大きく、いちばん濃く出す。ほかのまとまりは同じ重さに並べない。全部が同じ大きさのカードの並びは、どれが大事か分からない。
  *The focal point is the largest and darkest thing on screen; do not give every group the same weight.*
- 数字・時刻が主役のときは、数字を大きく太くし、単位は小さく `ink-secondary` にして半角あける。
  *When a number or time is the focus, set it large and bold; the unit smaller in `ink-secondary`, after a space.*

**余白でまとまりを見せる / Group with space**

- まとまりの中は `space-xs`〜`space-md`、まとまりの間は `space-xxl` 以上あける。中より間を必ず広くする。
  *Inside a group `space-xs` to `space-md`; between groups `space-xxl` or more. Between is always wider than inside.*
- まとまりは、まず余白と見出しで示す。縁や面で囲むのは、余白だけでは境目が分からないときだけにする（となりに別の内容が並ぶ、押せる範囲を示すなど）。
  *Group with space and headings first; add borders or surfaces only when space alone cannot show the edge.*

**言葉 / Words**

- 画面の言葉は「内容の原則」に従い、本物の物と操作の名前で書く。見本や試作でも、部品や見本そのものを説明する文（「クリックできるカード」）は書かない。
  *Use real names of things and actions, even in samples; never copy that describes the part itself.*
- 1 つの文は短く（目安 40 字まで）、1 つの文で 1 つのことを言う。専門の言葉は、使う人の言葉に置き換える。
  *Short sentences (about 40 characters), one idea each; replace jargon with the user's words.*

**いつも同じ場所 / Same thing, same place**

- 主ボタン・戻る・閉じる・検索は、どの画面でも同じ位置に置く（PC は主ボタンを右、スマホは「フォーム › ボタン」）。同じ操作に違う言葉を使わない。
  *Primary, back, close and search sit in the same place on every screen; one action, one word.*

**空・読み込み中・エラー / Empty, loading and error**

- 空の状態は、中身が入るはずの場所に左寄せで出し、何が無いかと、本物の次の一歩を書く（`EmptyState`）。真ん中に大きなアイコンを置く型は使わない。
  *Empty states sit left-aligned where the content would be, with what is missing and the real next step; no centred big-icon template.*
- エラーは、何が起きたかと、どうすれば直るかを書く。読み込み中は、出てくる中身の形を先に見せる（`Skeleton`）。10 秒以上かかるなら工程と時間の見込みを出す（「待ち時間」）。
  *Errors say what happened and how to fix it; loading previews the shape of the content; 10s or more shows steps and time.*

**和文の改行 / Japanese line breaks**

- Web は文節で改行する（`word-break: auto-phrase`、行頭と行末の禁則は `line-break: strict`）。見出しは `text-wrap: balance` で行の長さをそろえ、本文は `text-wrap: pretty` で最後の行に 1〜2 字だけ残さない。KM1 の部品には `bundle.css` で入っている。対応していないブラウザでは文字の単位で折り返すので、行末に 1〜2 字だけ落ちる文は言葉を直す。Flutter には文節の改行がないので、同じく言葉で直す。
  *Web breaks Japanese at phrase boundaries (`word-break: auto-phrase`, `line-break: strict`), headings use `text-wrap: balance`, body `text-wrap: pretty`; built into `bundle.css`. Where unsupported (and in Flutter), fix stranded characters by rewording.*

## 画面幅 / Breakpoints

Fluent 2 の size class をそのまま使う。値は `breakpoint-*`（Flutter は `Km1Breakpoint`）。
*Fluent 2 size classes as-is: `breakpoint-*` (`Km1Breakpoint` in Flutter).*

| 幅 / Width | Fluent 2 | ナビゲーション / Navigation | 編集・詳細 / Editing | 余白 / Page margin |
|---|---|---|---|---|
| 〜639px | small・medium | 下部のタブ（5 個まで）/ bottom tabs (max 5) | 全画面のページ / full-screen page | `space-lg` 16px |
| 640〜1023px | large | 下部のタブ、または開閉するサイドバー / bottom tabs or collapsible sidebar | ダイアログ / dialog | `space-xxl` 24px |
| 1024〜1365px | x-large | 常時表示のサイドバー / persistent sidebar | ダイアログ / dialog | `space-xxl` 24px |
| 1366px〜 | xx-large 以上 | サイドバー + 内容 + 補助ペインの 3 ペインまで / up to three panes | ダイアログ / dialog | `space-xxxl` 32px |

- 読み物とフォームの 1 カラムは `content-width`（720px）まで。それより広い画面では中央に寄せず左に置き、余った幅は空ける。
  *A reading or form column stops at `content-width` (720px); on wider screens keep it left-aligned and leave the rest empty.*
- 段の間隔（ガター）は `space-lg`、ペインの区切りは `stroke-subtle` の 1px。
  *Gutters are `space-lg`; panes are separated by a 1px `stroke-subtle` line.*
- レイアウトの余白は用途の名前で指す: 見出しつきのセクションの間と部品どうしの間は `layout-section-gap`（24px）、サイドバーと本文のような大きな領域の間は `layout-region-gap`（32px）。部品の中の余白（カードの内側・項目の間）は部品側のトークンで、混ぜない（「トークン」の 2 章）。
  *Layout spacing uses role names: `layout-section-gap` (24px) between headed sections and components, `layout-region-gap` (32px) between large regions. Component-internal spacing uses component-side tokens (Tokens, chapter 2).*
- 密度（compact・regular・spacious）は Card・Table・SortableList だけ。画面の幅で自動に切り替えず、画面の目的か利用者の設定で決める（「トークン」の 3 章）。
  *Density applies only to Card, Table and SortableList, chosen by purpose or user setting, never by width alone.*

## ナビゲーション / Navigation

- 項目はアイコン（`icon-lg` 24px）+ 文言。アイコンは通常 Regular、選択中は Filled にして、色（`brand-ink`）だけに頼らず形でも示す。
  *Each item is an icon (`icon-lg`) plus a label. Regular normally, Filled when selected, so selection shows in shape as well as color (`brand-ink`).*
- 部品は `Nav`。下部のタブは 5 個まで（これは原則ではなく、狭い画面に 44px の項目を並べる都合の上限）。行き先が 6 個以上になる例外のプロダクトでは、使用頻度の低いものを「⋮」メニューかサイドバーに移す。
  *Bottom tabs: five at most (a layout limit of narrow screens, not a default). Products that need six or more destinations move rarer ones into a "⋮" menu or the sidebar.*
- 上部バーはライトでは `brand` の塗り + `on-brand` の文字。ダークでは `brand` を使わず `surface-sunken` + `ink` にする（暗い画面で大きな色面を作らない）。
  *The top bar is a `brand` fill with `on-brand` text in light; in dark it is `surface-sunken` with `ink`, never a large brand-colored area.*
- 主な追加操作（「予定を追加」など）は、広い画面ではサイドバー上部のプライマリボタン、狭い画面では見出し行の右のボタンに置く。Material の FAB（浮いた丸ボタン）は使わない。
  *The main create action sits as the primary button at the top of the sidebar on wide screens, or at the right of the heading row on narrow ones. No floating action button.*

## 画面の型 / Screen layouts

一覧・詳細・編集の組み合わせ方。見本は「画面の例」（ScreenAddEvent・ScreenListEdit・ScreenOffline）で、利用シナリオの検証にも使う（「検証」）。
*How list, detail and edit combine; see the "Screen patterns" cards, which also drive the scenario checks.*

| 型 / Layout | 使う場面 / When | 組み立て / Composition | スマホ（1023px 以下） |
|---|---|---|---|
| 一覧 → 追加 | 項目を足すのが主な作業 | 見出し行の右に主ボタン「〜を追加」、追加は `Drawer` の中のフォーム（`.f2-form--contained`）、追加の結果は `Toast` | 主ボタンは見出し行の右のまま。フォームは全画面に近い `Drawer` |
| 一覧・詳細（2 つ並べる）| 一覧から選んで中身を見る・直すことが多い | 左に `List`（今開いている行に印）、右に詳細。項目ごとの直しは `ExpansionEditor`。領域の間は `layout-region-gap` | 一覧と詳細を別の画面にし、詳細から「戻る」 |
| 一覧・まとめて操作 | 複数を選んで消す・移す | `List` か `Table` を選べる形にして、上に `ContextualActionBar`。取り消せない操作は件数つきの `Dialog`、元に戻せる操作は `Toast` の「元に戻す」 | 同じ |
| 通信できないとき | 手元の内容で作業を続けられる | 上に `Alert`（warning）、「〜時点の内容」、送れなかった項目に「未送信」、つながったら自動で送って `Toast` | 同じ |

- どの型でも、ダイアログ・ドロワー・シートを閉じたら、開いたボタンへフォーカスを戻す。
  *Always return focus to the opener when an overlay closes.*
- 1 画面に出す行は 500 行まで。それ以上はページ送りか絞り込み（「検証」の大量データ）。
  *At most 500 rows per screen; paginate or filter beyond that.*

## 密な画面 / Dense screens

- 部品の高さは端末で切り替わる: スマホは 44px、PC は 32px。密な画面だからといって、これより小さくしない（PC の small ボタン 24px が下限）。
  *Control height follows the device: 44px on phones, 32px on PC. Dense screens do not go smaller (the 24px small button on PC is the floor).*
- スマホで見た目を小さくしたい部品（チップ、小さなアイコンボタン）は、見た目だけ小さくして、押せる範囲を余白で 44px まで広げる。隣の操作領域と重ねない。
  *On phones, when a control must look small (chips, small icon buttons), shrink only the visual and extend the pressable area to 44px with padding; hit areas must not overlap.*
- 毎週同じ枠の予定は `Timetable`、日ごとの予定は `TimeGrid`（スマホは 1 日表示 + アジェンダの一覧）、日付を選ぶのは `Calendar`。時間のグリッドは 1 時間を 56px 以上にし、30 分の補助線は `stroke-subtle`。現在時刻の線は `danger-ink`（ダークでも背景と 3:1 以上になる）。
  *Time grids give one hour at least 56px; half-hour guides use `stroke-subtle`; the current-time line uses `danger-ink` (3:1 or more in dark too).*

## 分類色 / Category colors

利用者が分類（カレンダー、タグ、店舗など）に付ける色。`cat-*` の 18 色（Fluent の共有パレットから）で、ライトとダークで同じ値を使う。
*Colors that people assign to categories (calendars, tags, shops): 18 `cat-*` colors from the Fluent shared palette, same value in light and dark.*

- 使い方は 2 つだけ: 幅 `stroke-accent`（4px）の帯と、淡い塗り（ライト 14%、ダーク 32%）。文字は必ず `ink`。分類色を文字色やボタンの塗りにしない。
  *Two uses only: a `stroke-accent` (4px) bar and a tinted fill (14% light, 32% dark). Text stays `ink`; never use a category color for text or button fills.*
- CSS の例 / CSS: `border-left:var(--stroke-accent) solid var(--cat-teal); background:color-mix(in srgb, var(--cat-teal) var(--opacity-cat-tint-light), var(--surface));`
- Flutter: `Km1Category.teal`、`Km1Category.tint(color, brightness)`。
- 18 色のうち、`surface` との比が 3:1 に満たないものがある（ライト: seafoam・lime・marigold。ダーク: blue・red・cranberry・grape・brown）。各トークンの説明に比を書いてある。色だけで分類を区別させず、分類名を文字で確認できる場所（凡例、詳細、プレビュー）を必ず用意する。
  *Some fall below 3:1 against `surface` (light: seafoam, lime, marigold; dark: blue, red, cranberry, grape, brown); each token's note lists its ratios. Never rely on color alone: always provide a place (legend, detail, preview) where the category name is readable.*
- 既定で割り当てる色は、隣り合って使うもの同士で明るさが違う組にする。赤と緑の組は避け、青と橙の組を優先する（EPSON のカラーユニバーサルデザインの考え方）。
  *Defaults that sit side by side should differ in lightness; prefer blue/orange over red/green (Epson's color-universal-design thinking).*
- 色以外で伝える状態は、帯の描き方で分ける: 確定 = 塗り、仮 = 斜線、空き = 白抜き、別の場所 = 点線。
  *States beyond color use the bar's drawing: confirmed = solid, tentative = hatched, free = hollow, elsewhere = dashed.*
- **色 × 模様（KM1-COL-001）:** 分類は色だけでなく模様でも区別する。模様は 8 つ（塗り・横線・縦線・斜線・格子・斜め格子・点・市松）で、18 色と組み合わせて 144 通り。色の見分けにくい人にも、白黒の印刷やハイコントラスト表示でも区別が残る。
  *Color × pattern: 8 patterns (solid, horizontal, vertical, diagonal, grid, crosshatch, dots, checker) × 18 colors = 144 combinations that survive color-vision differences, grayscale print and forced colors.*
  - 模様は文字の下に描かない。使う場所は、分類のしるし（`CategoryMark`、16px か 20px）、凡例（`CategoryLegend`）、グラフの棒や面の塗り（模様の間隔 8px）だけ。予定のブロックのように文字が載る面は淡い塗りと帯のままにし、しるしを題名の前に置く（`Timetable`・`TimeGrid` の `pattern`）。
    *Never under text: only marks, legends and chart fills. Text surfaces keep tint and bar, with a mark before the title.*
  - 利用者が選ばないときは `categoryStyle(i)`（Flutter は `km1CategoryStyleAt(i)`）の順に割り当てる。隣り合う分類で明るさと模様が両方変わり、72 個目まで同じ組が出ない。1 画面の分類は 12 個までを目安にする。
    *Assign defaults with `categoryStyle(i)`; neighbours differ in lightness and pattern, no repeat before 72. Aim for 12 or fewer per screen.*
  - 状態の描き分けとは混ぜない: 仮の予定はブロック全体の右上がりの斜線、分類の「斜線」はしるしの中だけの右下がり。
    *Keep states separate: tentative = full-block rising hatch; the category diagonal falls and lives only in marks.*
  - しるしには分類名の文字を必ず添える（凡例か横の文字）。しるしの枠は `stroke-strong`。ハイコントラストでは模様を `CanvasText` で描く。
    *Always pair a mark with the category name; mark border `stroke-strong`; forced colors draw patterns in `CanvasText`.*

## 意味の色の使い分け / Status colors in practice

- `danger-ink`: エラー、取り消せない操作、現在時刻の線。
- `warning-ink`: 締め切り・期限が近いもの。エラーではないので赤にしない。
- `success-ink`: 完了。`info-ink`: 補足のお知らせ。
- どれも色だけで示さず、アイコンか文言を添える（締め切りは旗のアイコン + 時刻）。
*`danger-ink` for errors, irreversible actions and the current-time line; `warning-ink` for deadlines and things due soon (not red: they are not errors); `success-ink` for done; `info-ink` for notices. Always with an icon or words (a deadline = flag icon + time).*

## ダイアログとプレビュー / Dialogs and previews

- 幅は `dialog-width`（480px）、確認と小さな設定は `dialog-width-sm`（420px）。暗幕は黒の `opacity-scrim`（40%）。入力を伴う編集は、640px 未満では全画面のページにする。確認は狭い画面でもダイアログのまま。
  *Width `dialog-width` (480px), or `dialog-width-sm` (420px) for confirmations and small settings; scrim is black at `opacity-scrim` (40%). Editing with input becomes a full-screen page below 640px; confirmations stay dialogs.*
- ボタンは 2 つまで。右にプライマリ、左に「キャンセル」（デジタル庁の配置）。480px 未満では縦に積み、プライマリを上にする（`Dialog` に実装済み）。
  *Two buttons at most: primary right, cancel left (Digital Agency placement); below 480px they stack with the primary on top (built into `Dialog`).*
- 見ることが主な一覧（予定表など）では、項目を押したらいきなり編集画面を開かず、小さなプレビューカードを出す（上辺に分類色の 4px の帯、右上に編集・削除・閉じる）。直すことが主な一覧（タスクの整理、在庫の修正など）では、押したらそのまま編集してよい。
  *In lists people mainly read (schedules), pressing an item opens a small preview card first (4px category bar; edit, delete, close at top right). In lists people mainly edit (task triage, stock fixes), it may open the editor directly.*
- 削除などの取り消せない操作は、確認ダイアログで対象の名前を見出しに入れる（「『ゼミ』を削除しますか」）。
  *Irreversible actions confirm with the target's name in the title.*

## フォーム / Forms

KM1-PAT-001。IBM Carbon の「Forms」「Fluid styles」の考え方を参考にし、見た目は KM1 のトークンと部品のままにする。部品は `FormGroup`・`FormGrid`・`FormActions`・`ConditionalField`・`ErrorSummary` と、状態をまとめる `useForm`。
*KM1-PAT-001. Borrows the ideas of IBM Carbon's Forms and Fluid styles guidance while keeping KM1's own tokens and components. Parts: `FormGroup`, `FormGrid`, `FormActions`, `ConditionalField`, `ErrorSummary`, plus the `useForm` state hook.*

### 並べ方 / Layout

- 基本は 1 列。ラベルは欄の上に置く。1 列のほうが目の動きがまっすぐで、入力漏れが減る（Carbon）。
  *Default to one column with labels on top. A single column keeps the eye moving straight down and reduces skipped fields (Carbon).*
- 2 列にしてよいのは、画面幅が 1024px 以上で、しかもフォームの幅が 560px 以上あるときだけ。対象は「姓・名」「開始・終了」「郵便番号・都道府県」のような、関係が強く短い欄の組。`FormGrid columns={2}` がこの 2 つの条件（メディアクエリとコンテナクエリ）を両方見る。
  *Two columns only when the viewport is at least 1024px and the form itself is at least 560px wide, and only for short, closely related pairs (family/given name, start/end, postcode/prefecture). `FormGrid columns={2}` checks both conditions (media query and container query).*
- スマホ（1023px 以下）は必ず 1 列。ダイアログやドロワーの中のように狭い入れ物では、PC でも 1 列のまま。
  *Phones and tablets (≤1023px) are always one column; so are narrow containers such as dialogs and drawers, even on PC.*
- 住所・メール・メモのように長い欄は `span="full"` で全幅にする。
  *Long fields (address, email, notes) take the full width with `span="full"`.*
- 読む順・Tab の順・DOM の順を同じにする。CSS の `order` や `row-reverse` で見た目だけ並べ替えない（WCAG 1.3.2・2.4.3）。ボタンの並びをスマホで逆にするときは `FormActions` が DOM の順ごと入れ替える。
  *Reading order, Tab order and DOM order are the same. Never reorder visually with CSS `order` or `row-reverse` (WCAG 1.3.2, 2.4.3). When phones flip the button order, `FormActions` flips the DOM order too.*
- フォーム全体の幅は `content-width`（720px）まで、左寄せ。
  *The whole form stops at `content-width` (720px), left-aligned.*

### 間隔 / Spacing

既存のトークンだけを使う。新しい値は足さない。
*Existing tokens only; no new values.*

| 場所 / Where | ページのフォーム / Page form（`.f2-form`） | 入れ物の中 / Contained（`.f2-form--contained`: Dialog・Drawer） |
|---|---|---|
| 欄と欄 / Field to field | `space-xxl` 24px | `space-lg` 16px |
| グループとグループ / Group to group | `space-xxxl` + `space-lg` 48px | `space-xxxl` 32px |
| 見出しと最初の欄 / Heading to first field | `space-xs` + `space-sm` 12px | 同じ / same |
| 最後のグループとボタン / Last group to buttons | 48px（グループ間と同じ） | 32px |

- グループ間は必ず欄の間より広くする。これでまとまりが見え、枠や線を足さずに済む（Carbon は欄 32px・ボタン前 48px。KM1 は 4px/8px 刻みの既存トークンで近い比率にした）。
  *Group gaps are always larger than field gaps, which shows grouping without extra borders. (Carbon uses 32px between fields and 48px before buttons; KM1 keeps a similar ratio with its existing 4/8px tokens.)*

### グループ / Groups

- まとまりごとに `FormGroup` で見出しを付ける。見出しは `<section>` + `<h2>`（`headingLevel` で変更可）。
  *Give each cluster a heading with `FormGroup`: a `<section>` with an `<h2>` (change with `headingLevel`).*
- 「1 つの問い」に答える選択肢の集まり（ラジオ・チェックボックスの組、生年月日の 3 欄など）は `as="fieldset"` にして `legend` で問いを読ませる（W3C WAI Forms Tutorial）。
  *When the controls answer one question (a radio or checkbox set, a three-part date), use `as="fieldset"` so the `legend` is read as the question (W3C WAI Forms Tutorial).*
- グループごとにカードや枠で囲まない。区切りは見出しと間隔で示す。
  *Don't box each group in a card or border; headings and spacing separate them.*
- 長いフォームは段階に分ける。まず必須だけ見せ、詳しい設定は `Accordion`（「詳しい設定」）に入れるか、3 工程以上なら `StepFlow` で手順ごとの画面に分ける（処理を待つ工程の表示は `Progress steps`）。1 項目ずつ直す設定画面は `ExpansionEditor`。
  *Split long forms: show what's required first, put advanced settings in an `Accordion`, or use `StepFlow` for three or more steps (`Progress steps` is for waiting on system work). Settings edited one item at a time use `ExpansionEditor`.*

### 条件で出る欄 / Conditional fields

- 前の答えで必要になる欄は、最初は出さない。答えた直後に、その答えのすぐ下に出す（`ConditionalField`）。
  *Fields that depend on an earlier answer are hidden at first and appear right below that answer once it's given (`ConditionalField`).*
- 出たときにフォーカスを動かさない。代わりに `role="status"` で「〇〇の入力欄が追加されました」と読ませる。消えるときは通知しない（必要なら `announceHide`）。
  *Don't move focus when fields appear. Announce "a field for X was added" through `role="status"`; disappearing fields are silent unless `announceHide` is set.*
- 隠した欄は検証しない・送らない。`useForm` の `when` に条件を書くと、エラーも `payload()` も自動で外れる。
  *Hidden fields are neither validated nor submitted. Put the condition in `useForm`'s `when` and both errors and `payload()` skip it.*
- 隠しても入力値は消さない（答えを戻したら元の値が出る）。入力値が残ると困る場合（別の人の情報など）だけ `resetOnHide` に名前を書いて初期値に戻す。
  *Hiding keeps the value, so switching back restores it. Only list a field in `resetOnHide` when a stale value would be harmful (for example, someone else's details); it then returns to its initial value.*
- 出し入れの区別に左の線（`stroke-subtle` 2px）を使う。色だけに頼らず、位置（答えの直下）と字下げでも示す。
  *A 2px `stroke-subtle` rule on the left marks the dependent block; position (right below the answer) and indent carry the meaning too, not color alone.*

### 入力の確認とエラー / Validation and errors

- 確かめるのは「欄を離れたとき（blur）」と「送信したとき」。打っている途中には出さない。一度エラーが出た欄は、直している最中に毎回確かめ、正しくなった時点で消す（Carbon）。
  *Validate on blur and on submit, never while the user is still typing. Once a field has shown an error, re-check it on every change and clear the error as soon as it's fixed (Carbon).*
- メッセージは「何がだめか」と「どう直すか」を 1 文で。例: 「終了時刻は開始時刻（10:00）より後にしてください。」。「不正な値です」だけにしない。
  *One sentence saying what's wrong and how to fix it, e.g. "Set the end time after the start time (10:00)." Never just "Invalid value".*
- エラーの見た目は今の `Input`・`Select`・`Textarea`・`RadioGroup` のまま（赤い文・`aria-invalid`・`aria-describedby` で欄に結ぶ）。
  *Error styling stays as in the existing fields: red message text tied to the field with `aria-invalid` and `aria-describedby`.*
- 送信して誤りがあれば、フォームの上に `ErrorSummary` を出し、そこへフォーカスを移す。件数と、各欄へのリンクを並べる。リンクを押すとその欄へ移る（GOV.UK・デジタル庁）。
  *On a failed submit, show `ErrorSummary` above the form and move focus to it. It lists the count and a link per field; each link focuses its field (GOV.UK, Digital Agency).*
- 入力した値は、エラーでも送信失敗でも消さない。
  *Never clear what the user typed, whether validation or the submit fails.*
- 送信ボタンは押せないようにしない。押したら足りない所を教える（デジタル庁）。Carbon は短いフォームでの無効化を認めているが、理由が伝わらないため KM1 では採らない。送信中だけ `aria-disabled` と `Spinner` で二重送信を防ぐ。
  *Don't disable the submit button; let it explain what's missing (Digital Agency). Carbon allows disabling on short forms, but KM1 doesn't because the reason isn't communicated. Only while submitting, use `aria-disabled` plus a `Spinner` to block double submits.*
- 必須の印は今のまま、必須の欄に「※必須」を付ける（デジタル庁）。Carbon の「少ない方に印を付ける」は採らない。
  *Required fields keep the "※必須" marker (Digital Agency). Carbon's "mark whichever is fewer" isn't adopted.*

### ボタン / Buttons

- `Button` の既存の決まりに合わせる: PC は主ボタンを右、キャンセル・戻るを左。スマホ（479px 以下）は縦に積み、主ボタンを一番上。Carbon のページ内フォーム（主ボタン左）とは違うが、KM1 の他の画面と揃えることを優先する。
  *Follows the existing `Button` rule: on PC the primary is on the right with Cancel/Back on the left; on phones (≤479px) they stack with the primary on top. This differs from Carbon's in-page forms (primary on the left), but consistency with the rest of KM1 wins.*
- `FormActions` には PC の並び（左から右）で子を渡す。スマホでは DOM の順ごと逆になるので、Tab の順と見た目が一致する。
  *Pass children to `FormActions` in PC order (left to right); on phones it reverses the DOM order so Tab order still matches what you see.*

### 密度 / Density

- Carbon の Fluid スタイル（ラベルを欄の中に入れ、高さ 64px で隙間なく並べる）は採らない。Carbon 自身が、複雑なフォームや情報の多い画面には勧めていないため。
  *Carbon's Fluid style (labels inside fields, 64px tall, stacked flush) isn't adopted; Carbon itself advises against it for complex or dense forms.*
- 密度の切り替えも足さない。KM1 は入力方法で高さが決まる（タッチ 44px・PC 32px）ので、それで足りる。違いは「ページ」と「入れ物の中」の間隔（上の表）だけ。
  *No density switch either. KM1 already sizes controls by input method (44px touch, 32px PC); the only variant is page vs contained spacing (table above).*

### Flutter

- `Form(autovalidateMode: AutovalidateMode.onUnfocus)` が「欄を離れたら確かめる」に当たる。送信時は `formKey.currentState!.validate()`。
  *`Form(autovalidateMode: AutovalidateMode.onUnfocus)` gives validate-on-blur; call `formKey.currentState!.validate()` on submit.*
- 部品は `Km1FormGroup`・`Km1FormGrid`・`Km1ConditionalField`・`Km1ErrorSummary`・`Km1FormActions`（`km1_widgets.dart`）。
  *Widgets: `Km1FormGroup`, `Km1FormGrid`, `Km1ConditionalField`, `Km1ErrorSummary`, `Km1FormActions` (in `km1_widgets.dart`).*

出典 / Sources: [Carbon Forms](https://carbondesignsystem.com/patterns/forms-pattern/)・[Carbon Fluid styles](https://carbondesignsystem.com/patterns/fluid-styles/)・[W3C WAI Forms Tutorial: Grouping](https://www.w3.org/WAI/tutorials/forms/grouping/)・[GOV.UK Error summary](https://design-system.service.gov.uk/components/error-summary/)・[デジタル庁デザインシステム](https://design.digital.go.jp/)

## 通信できないとき / Offline

KM1-M1-001 で追加。M1 の Offline states を下敷きにし、同期と再試行は KM1 で足した。
*Added in KM1-M1-001, based on M1 Offline states; sync and retry are KM1 additions.*

- 一部の機能だけが通信なしで動くアプリでは、今つながっているかを画面に出す。通信が切れたら、画面の上に `Alert`（`warning`、アイコン cloud off）で「インターネットに接続されていません。保存した予定は見られます。」のように、使えることと使えないことを 1 文で書く。M1 も、通信がないときは使えることを添えるよう求めている。
  *When only some features work offline, show the connection state: a warning `Alert` stating what still works and what doesn't.*
- 何も読み込めないより、手元にあるものを出す（M1）。前回の内容を出すときは「11/13 10:20 時点の内容」と時刻を添える。
  *Show cached content rather than nothing, with its timestamp.*
- 通信が要る操作のボタンは押せるままにし、押したら理由を出す（KM1 のボタンを無効にしない規則）。送れなかった入力は消さずに端末に残し、「未送信 2 件」と件数を出す。
  *Keep buttons enabled and explain on press; keep unsent input and show its count.*
- つながり直したら自動で送り、`Toast` で「2 件を送信しました」。失敗したら `Alert` に「再試行」ボタン。自動の再試行は間隔を広げながら行い、10 秒以上かかるなら待ち時間の規則に従う。
  *Send automatically on reconnect and confirm in a Toast; on failure show Retry; back off automatic retries.*
- ダウンロードして通信なしで使える物には、言葉つきの印（「端末に保存済み」）と容量を出し、消して空きを作れるようにする（M1）。1 つのファイルのダウンロードにスイッチを使わない（M1）。
  *Mark offline-available items with words and size, allow deleting them; no switch for a single download.*

## 権限を求めるとき / Permissions

KM1-M1-001 で追加。M1 の Permissions を下敷きにした。
*Added in KM1-M1-001, based on M1 Permissions.*

- 権限（位置・通知・カメラなど）は、その機能を使う直前に求める。アプリの中心で、なくては動かない権限だけを最初に求める（M1）。
  *Ask right before the feature is used; ask up front only for critical, obvious permissions.*
- 理由が分かりにくい権限は、OS の確認を出す前に 1 文で説明する（「授業の 10 分前に知らせるため、通知を許可してください」）。説明の画面には「許可する」と「今はしない」を並べる。
  *Explain non-obvious permissions in one sentence before the OS prompt, with "Allow" and "Not now".*
- 必要な分だけ求める。利用者の操作そのものが許可になる場合（ファイルを選ぶなど）は、確認を出さない（M1）。
  *Ask only for what's needed; an explicit user action (picking a file) needs no prompt.*
- 断られたら、その機能の場所で、何ができないかと、どうすれば使えるかを書き、「設定を開く」ボタンを置く（M1）。何度も確認を出し直さない。
  *On denial, explain at the feature what's unavailable and offer "Open settings"; don't re-prompt repeatedly.*
- 権限がなくて中身を出せない画面は `EmptyState` で、理由と次の一手（「設定を開く」）を出す。
  *Use `EmptyState` with the reason and next step when a screen can't show content without permission.*

## お知らせ / Notifications

- 操作の結果や時刻の通知は、画面下の `Toast`（`surface-sunken`、`radius-lg`、`stroke` の枠）で出す。中身はアイコン + 1 行の文言 + 操作 1 つまで。
  *Results and reminders appear as a bottom toast (`surface-sunken`, `radius-lg`, `stroke` border): icon, one line, at most one action.*
- 操作を含むトーストは自動で消さないか、十分長く（10 秒以上）出す。×で閉じられるようにする。
  *A toast with an action either stays or shows for 10 seconds or more, and can be dismissed with ×.*
- 画面内に残す必要があるお知らせは `Alert` を使う。
  *Use `Alert` for notices that must stay on the page.*

## 日付と時刻の書き方 / Dates and times

- 日付は「11/12（木）」、年が要るときは「2026/11/12（木）」。曜日は丸括弧で 1 文字。
- 時刻は 24 時間制で「9:00」。時の先頭に 0 を付けない。範囲は「9:00〜9:50」。
- 終日は「終日」と書く。0:00 ちょうどの締め切りは、前日の終日として見せる。
- 相対表現（「今日」「明日」）は日付と併記する: 「今日 11/12（木）」。
*Dates as "11/12（木）" (add the year as "2026/11/12（木）" when needed); 24-hour times without a leading zero ("9:00"); ranges with "〜"; "終日" for all-day; a 0:00 deadline is shown as all-day on the previous day; relative words go with the date.*

## 待ち時間 / Waiting

待ち時間の長さと、出てくる中身の形が分かるかで、見せるものを変える。待ちの部品は 3 つで、この表のほかの場面には使わない。区切りは Jakob Nielsen の応答時間の 3 つの目安（0.1・1・10 秒）。
*What to show depends on the wait; the thresholds are Jakob Nielsen's three response-time limits (0.1, 1 and 10 seconds).*

| 見込み / Expected | 見せるもの / Show | 部品 / Component |
|---|---|---|
| 1 秒未満 / under 1s | 何も出さない（結果がそのまま出る） / nothing | — |
| 1〜10 秒・出てくる中身の形が分かる / 1–10s, layout known | 中身のおおよその形 / the shape of the content | `Skeleton` |
| 1〜10 秒・形が分からない（保存・送信など）/ 1–10s, no layout | 何を待っているか / what is being waited for | `Spinner`（「保存中」など） |
| **10 秒以上 / 10s or more** | **工程と時間の見込みを必ず出す** / **steps and a time estimate, always** | `Progress`（`steps`・`remaining`・`elapsed`） |

10 秒以上かかる処理の決まり / Rules for 10 seconds or more:

- **工程**: 利用者の言葉で 3〜7 個に分ける（「メールを読み込む」「予定を探す」「照らし合わせる」「保存する」）。内部の処理名（「API 呼び出し」）は書かない。
  ***Steps**: three to seven, in the user's words; no internal names.*
- **時間の見込み**: 根拠の強さに応じて、次の順で出せるものを出す。根拠のない数字は出さない。
  1. 計算できる（終わった量 ÷ 経過時間、過去の実測）→ 「残り約 30 秒」と「約」を付けて丸める。出し始めの数秒は「残り時間を計算中」。
  2. 過去の実績の幅だけ分かる → 「通常 1〜3 分」と幅で出し、経過時間（「1 分 20 秒経過」）を並べる。
  3. 相手次第で見積もれない（通信、外部のサービス） → 経過時間と、見積もれない理由（「外部のサービスの応答を待っています」）を出す。
  ***Time estimate**: show the strongest estimate you have, never an invented number. (1) Computable → "残り約 30 秒", rounded with "約" ("計算中" for the first seconds). (2) Only a past range → "通常 1〜3 分" plus elapsed time. (3) Depends on others (network, external service) → elapsed time and why it cannot be estimated.*
- **見積もりの出し方**: 過去の実測（同じ処理にかかった時間）か、終わった量と経過時間から計算する。進むたびに更新し、急に増やさない。
  ***Estimates** come from past measurements or work done ÷ time elapsed, update as work proceeds, and never jump up suddenly.*
- **見込みを超えたとき**: 0 秒のまま止めず、「予定より時間がかかっています」と出す。原因が分かるなら書く（「通信が遅くなっています」）。
  ***Past the estimate**: never sit at zero; say it is taking longer, with the cause if known.*
- **止められるなら止められるように**: 途中で止められる処理には「キャンセル」を付ける。止めたら、そこまでの結果を残すか捨てるかを文言で伝える。
  ***Allow stopping** where possible with "キャンセル", and say whether partial results are kept.*
- **ほかの操作を止めない**: 待っている間も、ほかの画面に移ったり入力したりできるようにする。画面を離れても続く処理は、終わったら `Toast` か通知で知らせる。
  ***Do not block** other work; if it continues off-screen, report completion with a `Toast` or notification.*
- **始める前に分かるなら先に言う**: 10 秒以上かかると分かっている操作は、ボタンの近くか確認ダイアログに「1 分ほどかかります」と書いておく。
  ***Say it up front** when a long wait is known, near the button or in the confirmation.*

## 動き / Motion

| 用途 / Use | 時間 / Duration | 曲線 / Curve |
|---|---|---|
| hover・pressed の色 / hover, pressed color | `--duration-faster` 100ms | `--curve-easy-ease` |
| スイッチ・下線・チェック / switch, underline, check | `--duration-fast` 150ms | `--curve-easy-ease` |
| ダイアログ・ポップオーバー・画面が現れる / entering | `--duration-normal` 200ms | `--curve-decelerate` |
| 消える / exiting | `--duration-fast` 150ms | `--curve-accelerate` |

- 動かしてよいのは色・影・不透明度と、8px までの移動だけ。拡大縮小、跳ねる動き、Material の波紋は使わない。
  *Animate only color, shadow, opacity and travel of up to 8px. No scaling, bounce or Material ripple.*
- 画面の出入りは「短いフェード + 下から 8px」。`prefers-reduced-motion`（Flutter は `MediaQuery.disableAnimations`）では動きを止める。
  *Screens enter with a short fade plus an 8px rise; stop under `prefers-reduced-motion` (`MediaQuery.disableAnimations` in Flutter).*
- 値は Fluent 2 の duration・curve トークン。CSS では `components/bundle.css` に変数がある。
  *Values are Fluent 2 duration and curve tokens; the CSS variables live in `components/bundle.css`.*

## 重なり順 / Layers

`layer-content`（1）→ `layer-overlay`（1000、暗幕とダイアログ）→ `layer-popup`（2000、メニュー・ツールチップ）→ `layer-message`（3000、トースト）。値は Fluent 2 の zIndex トークン。これ以外の z-index を作らない。
*Fluent 2 zIndex values; do not invent other z-index values.*
