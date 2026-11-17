数を入れる欄。手で入力でき、−・＋や矢印キーで 1 つずつ増減できる。
*A number field: type a value, or step it with −/+ or arrow keys.*

## 使い方 / Usage
- 単位は欄の右に `unit` で書く（「円」「分」「個」）。読み上げにも単位つきで伝わる。
  *Put the unit to the right with `unit`; it is read with the value.*
- `min`・`max` を超えた入力は、欄を離れたときに範囲内に直す。数字でない入力は直さず「数字で入力してください。」と出す。全角数字は半角として受け付ける。
  *Out-of-range values are clamped on blur; non-numbers show an error instead. Full-width digits are accepted.*
- キーボード: ↑↓で 1 つ、PageUp・PageDown で 10、Home・End で最小・最大（W3C APG の Spinbutton）。−・＋ボタンは Tab で止まらない（キーボードでは矢印で足りるため）。
  *Keyboard per W3C APG spinbutton: arrows step, PageUp/Down by 10, Home/End to min/max. −/+ are skipped by Tab.*
- スマホでは数字のキーボードが出る（`inputmode="decimal"`）。
  *Phones show a numeric keyboard.*

## 利用側が渡すもの / You provide
`label`、`value` + `onChange`、必要なら `min`・`max`・`step`・`unit`・`hint`・`error`。
