画面を切り替えるメインのナビゲーション。狭い画面では下部のタブ、広い画面ではサイドバーになる。
*Primary navigation between screens: bottom tabs on narrow screens, a sidebar on wide ones.*

## 使い方 / Usage
- `orientation` は既定の `auto` で、1024px 未満は下部のタブ、以上はサイドバーに切り替わる。`horizontal`・`vertical` で固定もできる。置き場所（画面下に固定するなど）は利用側のレイアウトで決める。
  *`orientation` defaults to `auto`: bottom tabs below 1024px, sidebar from 1024px. `horizontal` and `vertical` pin it. Placement (e.g. fixing it to the bottom) is the consumer's layout.*
- 項目はアイコン（24px）+ 文言。下部のタブは 5 個まで（画面幅の都合）。サイドバーは原則 5 個で、6 個以上なら見出しで分類する。文言は名詞で 4 文字程度まで。
  *Each item is a 24px icon plus a label; bottom tabs hold five at most (width limit); the sidebar holds five by default and groups six or more under headings; short noun labels.*
- 選択中は、塗りのアイコン（`iconSelected`）・淡い紺の面（`brand-tint`）・文字の太さの 3 つで示す。線は足さない（合図を重ねすぎない。D25）。`icon` に Regular、`iconSelected` に Filled の KM1 のアイコン（`Icon`、24px）を渡す。
  *Selection shows as a filled icon (`iconSelected`), the brand tint and bold text; no indicator bar (D25). Pass a Regular KM1 icon as `icon` and the Filled one as `iconSelected` (`Icon`, 24px).*
- 読み上げには `nav` と `aria-current="page"` で伝わる。`label` でナビゲーションの名前を付ける。
  *Exposed as `nav` with `aria-current="page"`; name it with `label`.*
- 画面の中での切り替え（同じ画面の表示の切り替え）は `Tabs` を使う。
  *For switching views within one screen, use `Tabs`.*

## 利用側が渡すもの / You provide
`label`、`items`（`{value, label, icon, iconSelected?, href?}`）、`value`、`onChange`、必要なら `orientation`。

**理由 / Why:** 画面を切り替える。いつも同じ場所。狭い画面は下のタブ、広い画面は横のサイドバー。
*Switch screens: always in the same place; bottom tabs on narrow screens, a sidebar on wide ones.*
