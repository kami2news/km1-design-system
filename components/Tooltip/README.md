部品にマウスを乗せるかフォーカスしたときに出る、短い補足。
*A short hint shown when a control is hovered or focused.*

## 使い方 / Usage
- アイコンだけのボタンの名前や、短い補足に使う（1 行、20 文字程度まで）。操作に必要な情報はツールチップに入れず、画面に出す。
  *For naming icon-only buttons or brief hints (one line). Information needed to act belongs on the page, not in a tooltip.*
- スマホではマウスを乗せられないので、ツールチップに頼らない。アイコンだけのボタンには必ず `aria-label` も付ける。
  *Touch has no hover: never depend on a tooltip, and always give icon-only buttons an `aria-label`.*
- フォーカスではすぐ、マウスでは 0.3 秒後に出る。Esc で消せる。吹き出しの上にマウスを移しても消えない（WCAG 2.2 の 1.4.13）。
  *Appears at once on focus, after 0.3s on hover; Esc dismisses; it stays while the pointer is over it (WCAG 2.2 1.4.13).*
- 中に入れる部品は 1 つだけ。補足は `aria-describedby` で読み上げに伝わる。ボタンやリンクなどフォーカスできる部品に付ける。
  *Wrap exactly one child; the hint is exposed via `aria-describedby`. Attach it to focusable controls.*

## 利用側が渡すもの / You provide
`content`（補足の文言）、中の部品 1 つ、必要なら `position`（`top`・`bottom`）・`align`（`center`・`start`・`end`。画面の端に近いときは端にそろえる）・`delay`。
