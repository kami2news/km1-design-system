順番を入れ替えられる一覧。優先順位、表示の順番、手順の並べ替えに使う。
*A list whose order can be changed: priorities, display order, steps.*

## 使い方 / Usage
- 並べ替えの方法を 3 つ用意し、どれでも同じことができるようにする。
  *Three equivalent ways to reorder:*
  1. マウス・指で、左のつまみをドラッグする。 / *drag the handle;*
  2. 右の「↑」「↓」ボタンを押す（ドラッグができない人のため。WCAG 2.2 の 2.5.7）。 / *press the up/down buttons (WCAG 2.2 2.5.7 single-pointer alternative);*
  3. キーボードで、つまみにフォーカスして Space で持ち上げ、↑↓で動かし、Space で置く。Esc で取り消す（持ち上げる前の位置に戻り、そのことが読み上げられる）。フォーカスが外れたときは、その位置に置いたことにする。 / *keyboard: Space on the handle to lift, arrows to move, Space to drop, Esc to cancel and restore the original position (announced). Losing focus drops the item where it is.*
- 動かすたびに「（名前）を 3 番目に移動しました（全 5 件）」と読み上げる。
  *Each move is announced with the new position.*
- 並べ替えた結果はすぐ反映し、保存ボタンを別に要求しない。取り消せるように、必要なら `Toast` に「元に戻す」を付ける。
  *Changes apply immediately; offer "元に戻す" in a `Toast` if needed.*
- 予定表（`TimeGrid`）の中での予定の移動は、この部品の対象外。予定の時刻は編集画面で変える。
  *Moving events inside `TimeGrid` is out of scope; change times in the editor.*

## 密度 / Density

`density="compact"`・`"regular"`（既定、今までと同じ）・`"spacious"`。項目の間は `collection-item-gap-*` の半分（2・4・8px。項目に枠があるため半分にする）。つまみと上下のボタンの大きさは変わらない。Flutter は `Km1SortableList(density: Km1Density.compact)`。
*Item gap is half of `collection-item-gap-*` (2/4/8px, halved because items are bordered); grip and move buttons keep their size. Flutter: `Km1SortableList(density:)`.*

## 利用側が渡すもの / You provide
`label`、`items`（`{id, label, sub?}`）、`onChange`（並べ替えた配列）、必要なら `id`。

**理由 / Why:** 順番を自分で決めたい。つかむ場所と、キーボードでの上下移動の両方を用意する。
*Set the order yourself: both a grab handle and keyboard up/down.*
