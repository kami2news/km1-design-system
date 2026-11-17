複数行の文章を入力する欄。メモ、説明、貼り付けた文章の取り込みに使う。
*A multi-line text field for notes, descriptions and pasted text.*

## 使い方 / Usage
- ラベルは必ず付ける。ヒントはラベルと欄の間、エラーは欄の下に出る（`Input` と同じ）。
  *Always label. The hint sits between label and field, the error below (same as `Input`).*
- `maxLength` を渡すと「12 / 200」の文字数を右下に出す。入力は止めず、超えたら「◯ 文字超えています」と文言で知らせる。
  *`maxLength` shows a "12 / 200" counter. Typing is never blocked; going over is reported in words.*
- 高さは `rows`（既定 4 行）。利用者が縦に伸ばせる。1 行で済む入力は `Input` を使う。
  *Height comes from `rows` (default 4) and is user-resizable vertically. Use `Input` for single-line values.*
- 文字はスマホで 16px、PC で 14px。
  *Text is 16px on touch, 14px on PC.*

## 利用側が渡すもの / You provide
`label`、必要なら `hint`・`error`・`maxLength`・`rows`・`required`、値は `value` + `onChange` か `defaultValue`。
