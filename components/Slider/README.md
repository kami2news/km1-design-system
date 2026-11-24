範囲の中から、だいたいの値を選ぶつまみ。音量、通知の何分前、表示の密度など。
*A thumb for picking an approximate value in a range: volume, reminder lead time, density.*

**理由 / Why:** 音量や表示の大きさ、通知の何分前のように、正確な数より範囲の中のどのあたりかが大事な値は、つまみの位置で量が一目で分かる。正確な数が要るときは SpinButton を使う。
*For values where position in a range matters more than the exact number (volume, display size, minutes before a reminder), the thumb shows the amount at a glance; use SpinButton for exact numbers.*

## 使い方 / Usage
- 正確な数を入れてほしいときは `SpinButton` を使う。スライダーは「だいたい」で良い値だけ。
  *Use `SpinButton` for exact numbers; sliders are for approximate values.*
- ラベルの右に今の値を必ず出す（「15 分前」）。読み上げにも同じ文言が伝わるよう `valueText` で書き方を決める。
  *Always show the current value next to the label; `valueText` sets the wording, also used for screen readers.*
- 端の意味が分かりにくいときは `marks`（「控えめ」「多め」）で両端に言葉を置く。
  *Use `marks` to label the ends when they are not obvious.*
- 標準の `input type="range"` を使うので、矢印キー・Home・End・PageUp/PageDown がそのまま使える。つまみは 20px、押せる範囲は部品の高さ（スマホ 44px、PC 32px）。
  *Built on native `input type="range"`: arrows, Home/End, PageUp/PageDown work. The thumb is 20px; the hit area is the control height.*

## 利用側が渡すもの / You provide
`label`、`min`・`max`・`step`、`value` + `onChange`、必要なら `unit`・`valueText`・`marks`・`hint`。
