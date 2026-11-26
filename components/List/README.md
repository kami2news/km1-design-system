同じ種類のものを縦に並べ、ざっと見て 1 つを選ぶ一覧。`List`・`ListItem`・`ListSection`（小見出しつきのまとまり）・`ListSectionHeader`（小見出しだけ）からなる。M1 の Lists・Lists: Controls・Subheaders の考え方を、KM1 の見た目で実装したもの（KM1-M1-001）。
*A vertical list of same-kind items to scan and pick from: `List`, `ListItem`, `ListSection` (a titled group) and `ListSectionHeader` (heading only). Implements the ideas of M1 Lists, List controls and Subheaders in KM1's look (KM1-M1-001).*

## 使う条件 / When to use

- 同じ種類のもの（予定、ファイル、連絡先）を縦に見て、1 つを開く・選ぶとき。1 行の文字は 3 行まで（題名 + 説明 2 行）。
  *Same-kind items to scan and open; at most three lines per row.*
- 使わない: 列で比べる → `Table`。画像で見分ける → `ImageGrid`。種類も長さもまちまち・説明が 3 行を超える → `Card`。画面の移動 → `Nav`。
  *Not for column comparison (`Table`), image-led items (`ImageGrid`), mixed or long content (`Card`), or app navigation (`Nav`).*

## 行の組み立て / Row anatomy

| 場所 / Slot | 中身 / Content | 押し場所 / Target |
|---|---|---|
| 主操作 / primary | `leading`（アイコン 20px）・`title`・`description`・`meta` | 行の大半。`onClick` で button、`href` で a / most of the row |
| 右端 / end | `trailing`（補助操作。ピン留め・展開など）/ secondary action | 別 / separate |

- 主操作と補助操作は入れ子にしない（ボタンの中にボタンを置かない）。補助操作は同じ一覧の中で位置と意味をそろえる。各行に同じ「共有」を並べるような重複は避ける（M1 Lists）。
  *Never nest the targets. Keep the trailing action consistent; avoid repeating the same action (e.g. Share) on every row.*
- 主操作が画面の移動なら、右端に矢印アイコンを足さない（M1 Lists: Controls）。
  *If the primary action navigates, don't add an arrow icon.*
- 「開く」と「まとめて選ぶ」を同じ行に同時に出さない。ふだんの行は押すと開く。まとめて操作するときだけ、一覧の見出しの横の「まとめて選ぶ」（`subtle` ＋アイコン）で選ぶモードに入る。選ぶモードでは `selectable` を渡し、行全体が 1 つのチェックボックスになって、押すと選ぶ（`onClick` は使わない）。「選び終える」で抜けて選択を消す（D31）。
  *Never offer "open" and "select" on the same row at once. Rows open by default; a "まとめて選ぶ" button next to the list heading enters selection mode, where `selectable` makes the whole row one checkbox that selects on tap (`onClick` is ignored). "選び終える" leaves and clears.*

## 状態 / States

通常、ホバー（`surface-hover`）、押下（`surface-pressed`）、フォーカス（2px の `focus-ring`）、選択（`brand-tint` の背景 + 左の 3px `brand` の線 + チェック。色だけに頼らない）、無効（`aria-disabled`）。強制カラーでは選択を `Highlight` の枠で示す。
*Default, hover, pressed, focus ring, selected (tint + 3px brand bar + checkbox, never color alone), disabled. Forced colors outline selection with `Highlight`.*

## キーボード・読み上げ / Keyboard and screen readers

- Tab で主操作 → 補助操作の順に進む（DOM の順。選ぶモードでは行のチェックボックスだけ）。矢印キーの移動は持たない（一覧は「ウィジェット」ではなく、普通のリンクとボタンの並び）。
  *Tab goes primary → trailing in DOM order (selection mode: the row checkbox only); no arrow-key roving (a list of links and buttons, not a composite widget).*
- `ul role="list"` と `li`。`ListSection` は小見出しを本物の見出し（既定 `h3`、`headingLevel` で変更）にして、中の `ul` に `aria-labelledby` で名前を付ける。件数は「3 件」と見出しの中に書く。
  *`ul role="list"`; `ListSection` uses a real heading (h3 by default) and names its inner list with it; the count is in the heading.*
- 選ぶモードのチェックボックスは、行全体（題名と説明）がそのままラベルになる。
  *In selection mode the whole row (title and description) labels the checkbox.*

## 長い一覧と固定見出し / Long lists and sticky headings

- `sticky` は、長い一覧で今どのまとまりを見ているか分からなくなるときだけ使う（M1 Subheaders の「上に留まる見出し」）。短い一覧では使わない。
  *Use `sticky` only when users lose track of the current group in a long list.*
- 固定見出しの下にフォーカスが隠れないよう、スクロールする入れ物に `scroll-padding-top` を入れる（WCAG 2.4.11）。`maxHeight` を渡すと `List` 自身が入れ物になり、自動で入る。ページ全体でスクロールするときは `html{scroll-padding-top:…}` を利用側で足す。
  *Keep focus from hiding under sticky headings with `scroll-padding-top` (WCAG 2.4.11). `maxHeight` makes the list its own scroller and sets it; for page scrolling, add it to `html`.*

## 幅 / Responsive

どの幅でも 1 列。行の高さは PC 32px・タッチ 44px 以上（M1 の 48・56・72・88dp ではなく KM1 の規則）。`meta` は折り返さず、題名と説明は折り返す。320px で横スクロールしない。
*Single column at all widths; rows are at least 32px (PC) / 44px (touch). Titles wrap, meta doesn't. No horizontal scroll at 320px.*

## トークン / Tokens

`space-lg`（左右）・`space-md`（アイコンと文字）・`space-sm`（上下）、`stroke-subtle`（区切り線、`dividers={false}` で消す）、`ink`・`ink-secondary`、`brand-tint`・`brand`、`body-1`（題名）・`caption-1`（説明・時刻）。
*`space-lg`/`space-md`/`space-sm`, `stroke-subtle` dividers, `ink`/`ink-secondary`, `brand-tint`/`brand`, `body-1` and `caption-1`.*

## API

```jsx
<List label="今週の予定" maxHeight={440} selectable selected={ids} onSelectionChange={setIds}>
  <ListSection title="11月14日（土）" count={2} sticky>
    <ListItem id="a" leading={<CalendarIcon/>} title="環境化学 第8回" description="W9-324" meta="10:45"
      onClick={open} trailing={<PinButton/>} />
  </ListSection>
</List>
```

`List`: `label`、`selectable`・`selected`・`onSelectionChange`、`dividers`、`maxHeight`。`ListItem`: `id`、`title`、`description`、`meta`、`leading`、`trailing`、`onClick` か `href`、`current`、`disabled`、`selectLabel`。`ListSection`: `title`、`count`、`note`、`sticky`、`headingLevel`。

Flutter: `Km1ListItem`（`title`・`description`・`meta`・`leading`・`trailing`・`onTap`・`selectable`・`selected`・`onSelectedChanged`）と `Km1ListSectionHeader`（`title`・`count`）。固定見出しは `SliverPersistentHeader(pinned: true)` に入れる。

## してはいけないこと / Don't

- 1 行に意味の分からないアイコンの操作を並べる。 *Line up unexplained icon actions in a row.*
- 行の中にボタンを入れ子にする。 *Nest buttons inside the row button.*
- 行を左右にスワイプしないと使えない操作を作る（スワイプは補助。必ずボタンを用意する。WCAG 2.5.1）。 *Make swipe the only way to reach an action.*
- すべての項目をカードにする。 *Turn every item into a card.*

## テスト / Tests

行数、見出しが h3 で件数つき、まとまりの名前、主操作と補助操作が入れ子でない、ピンの `aria-pressed`、`scroll-padding-top`、固定見出し（7 項目、320・360・1366px・ダーク 1024px で合格）。axe 違反 0。
*7 scripted checks pass at 320/360/1366px and dark at 1024px; axe: 0 violations.*

**理由 / Why:** 同じ種類のものから 1 つ選ぶ。縦 1 列で、ざっと上から読める。比べるなら Table に回す。
*Pick one of many similar things: one column read top to bottom; comparisons go to Table.*
