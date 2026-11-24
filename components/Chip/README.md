押して切り替える小さな絞り込みボタン。一覧のフィルターや、複数選べる分類に使う。角は `radius-md`（4px）。
*A small toggle for filtering lists or picking several categories, with `radius-md` (4px) corners.*

**理由 / Why:** 押せるものは角丸、押せない印は丸、と形で分ける（D19）。Chip はボタンと同じ角丸にし、丸い Badge と見間違えないようにする。
*Pressable things have rounded corners and non-pressable marks are round (D19); Chip shares the button's corners so it is never mistaken for a round Badge.*

## 使い方 / Usage
- 選択中は、チェックのアイコン・枠の色・文字の太さの 3 つで示す（色だけにしない）。読み上げには `aria-pressed` で伝わる。
  *Selected shows a check icon, edge color and bold text (never color alone), and is exposed via `aria-pressed`.*
- 文言は名詞で短く（「授業」「バイト」）。1 つだけ選ぶ切り替えは `Tabs` か `RadioGroup` を使う。
  *Short noun labels. For choosing exactly one, use `Tabs` or `RadioGroup`.*
- 見た目の高さは 32px。スマホでは見た目はそのままで、押せる範囲だけ上下に広げて 44px にしてある。縦に並べるときは 12px 以上あける。
  *Visual height is 32px; on touch the pressable area extends to 44px without changing the look. Leave 12px or more between stacked rows.*
- 状態を表すだけで押せないものは `Badge` を使う。
  *For non-interactive status, use `Badge`.*

## 利用側が渡すもの / You provide
`selected`、`onClick`、文言。
