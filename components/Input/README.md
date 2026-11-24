1 行のテキスト入力。ラベルは常に表示し、プレースホルダをラベル代わりにしない。
*A single-line text field. Always show a label; never use the placeholder as the label.*

利用側が渡すもの: `label`、`value` または `defaultValue`、`onChange`。必須項目は `required`（見える「※必須」は読み上げず、`required` 属性で伝える）。補足は `hint`、エラーは `error`（原因と対処を文言で）。
*Consumer provides: `label`, `value` or `defaultValue`, `onChange`. Use `required` for required fields (the visible "※必須" is hidden from screen readers; the attribute conveys it). Use `hint` for help and `error` for errors (state cause and fix in words).*

- 補足（`hint`）はラベルと入力欄の間、エラー（`error`）は入力欄の下に左寄せで置く（デジタル庁デザインシステム）。
  *`hint` sits between the label and the field; `error` sits below the field, left-aligned (Digital Agency DS).*
- 入力例はプレースホルダに入れず、`hint` に「例：」として書く。プレースホルダは入力を始めると消え、薄い文字は入力済みの値と見分けにくい（D27）。
  *Put examples in `hint` ("例：…"), not in the placeholder: it disappears on typing and its pale text looks like a filled value.*

- タッチ操作の端末では文字を 16px にする（iPhone の Safari で、フォーカスしても画面が拡大されないようにするため）。
  *On touch devices text is 16px so iPhone Safari does not zoom on focus.*
- 下罫線は `stroke-strong`、フォーカス時は `brand-stroke` の 2px に変わる。
  *The underline is `stroke-strong` and becomes a 2px `brand-stroke` on focus.*
- エラー時は `aria-invalid` と説明文が自動で結び付く。
  *On error, `aria-invalid` and the message are linked automatically.*
- やらないこと: 枠の色だけで状態を示す。
  *Don't: show state by border color alone.*
- 日付と時刻は `type="date"`・`type="time"`・`type="datetime-local"` で、端末の標準の選択画面を使う（スマホで速く、読み上げにも対応している）。月の表から選ばせたいときや予定の印を見せたいときは `Calendar` を使う。
  *Dates and times use `type="date"`, `type="time"` or `type="datetime-local"` with the device's native picker (fast on phones, screen-reader ready). Use `Calendar` when people should pick from a month grid or see event marks.*
