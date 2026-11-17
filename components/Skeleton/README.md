読み込み中に、これから出る内容のおおよその形を灰色で見せる。
*Grey placeholders showing the shape of content while it loads.*

## 使い方 / Usage
- 一覧やカードの形が決まっていて、1〜10 秒で出るときに使う。形が決まっていないなら `Spinner`、10 秒以上なら `Progress`（工程と時間の見込み）。
  *Use when the layout is known and loading takes 1–10 seconds; otherwise `Spinner`, or `Progress` for 10s or more.*
- 形は `text`（行）、`list`（丸 + 行）、`card`（画像 + 行）。実際の内容と同じ大きさにして、出たときに画面が跳ねないようにする。
  *Shapes: `text`, `list`, `card`. Match the real content's size so nothing jumps when it arrives.*
- 読み上げには「読み込み中」とだけ伝わり、灰色の形そのものは読まれない。`prefers-reduced-motion` では光る動きを止める。
  *Screen readers hear only "読み込み中"; the shimmer stops under reduced motion.*

## 利用側が渡すもの / You provide
`shape`、必要なら `lines`・`label`。
