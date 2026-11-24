選択肢が 5 件以下で、1 つだけを選ぶとき。`fieldset` と `legend` でグループの名前を付け、矢印キーで移動できる（標準のラジオボタン）。
*Pick exactly one of five or fewer options. A `fieldset` and `legend` name the group; arrow keys move between options (native radios).*

利用側が渡すもの: `legend`、`options`、`value` または `defaultValue`、`onChange`。
*Consumer provides: `legend`, `options`, `value` or `defaultValue`, `onChange`.*

- 1 行の高さはスマホ 44px・PC 32px。選択中は枠の太い丸で示し、色の違いだけに頼らない。
  *Rows are 44px on touch, 32px on PC. Selection is a thick ring, not just a color change.*
- 複数選べるときは `Checkbox` を使う。ラジオは選択を取り消せないので、任意の項目には「あてはまるものはない」のような選ばない選択肢を用意する（デジタル庁デザインシステム）。必須のときは `required` を付ける。
  *Use `Checkbox` when several can be chosen. A radio cannot be deselected, so give optional questions a "none of the above" option (Digital Agency DS). Set `required` when mandatory.*

**理由 / Why:** 5 件以下から 1 つ選ぶ。選択肢が全部見えるので、開かずに比べられる。
*Pick one of five or fewer: every option is visible, compared without opening anything.*
