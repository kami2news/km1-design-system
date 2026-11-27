その場で効く設定のオン・オフ。押すとすぐ反映される。送信ボタンが要る設定には `Checkbox` を使う。
*On/off for a setting that takes effect immediately. Use `Checkbox` for settings that need a submit button.*

利用側が渡すもの: `children`（設定名）、`checked` または `defaultChecked`、`onChange`。
*Consumer provides: `children` (setting name), `checked` or `defaultChecked`, `onChange`.*

- 状態は、つまみの位置と「オン／オフ」の文字の両方で示す（色だけにしない）。高さはスマホ 44px・PC 32px。
  *State is shown by knob position and the words "オン/オフ", never color alone. 44px on touch, 32px on PC.*
- `role="switch"` を付けた標準のチェックボックスなので、スペースキーで切り替わる。
  *A native checkbox with `role="switch"`; Space toggles it.*

**理由 / Why:** その場で効く設定を切り替える。押した瞬間に反映される操作だと形で分かる。送信が要る設定とは分ける。
*Toggle a setting that applies at once: the shape says it takes effect immediately, unlike settings that need submitting.*
