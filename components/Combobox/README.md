入力して候補を絞り込み、1 つを選ぶ欄。選択肢が多い（6 件以上）ときに使う。
*Type to filter, then pick one. For six or more options.*

## 使い方 / Usage
- 選択肢が 5 件以下なら `RadioGroup`、6〜15 件で探す必要がなければ `Select`、それ以上か名前で探したいときに `Combobox`。
  *Five or fewer: `RadioGroup`; 6–15 without searching: `Select`; more, or when people search by name: `Combobox`.*
- 入力すると、文字を含む候補だけが残る。候補の件数は読み上げにも伝わる。一致しないときは「一致する候補がありません」。
  *Typing keeps matching options; the count is announced; no match shows a message.*
- 決まった選択肢から選ぶ部品で、自由入力の値は受け付けない。選ばずに離れたら、元の値に戻る。
  *Only listed values are accepted; leaving without choosing restores the previous value.*
- キーボード: ↓で開く・次へ、↑で前へ、Home・End、Enter で決定、Esc で閉じる（2 回目で入力を消す）。W3C APG の Combobox（リスト型）に合わせた。
  *Keyboard per W3C APG list combobox: Down opens/moves, Up, Home/End, Enter selects, Esc closes (twice clears).*

## 利用側が渡すもの / You provide
`label`、`options`（`{value, label, disabled?}`）、`value`、`onChange`、必要なら `placeholder`・`hint`・`error`・`required`・`emptyText`。
