選択肢が 6 件以上のときに 1 つを選ぶ。ブラウザ標準の `<select>` を使うので、キーボードとスクリーンリーダーの操作は標準のまま動く。
*Choose one from many options (roughly five or more). Uses the native `<select>`, so keyboard and screen-reader behavior is standard.*

利用側が渡すもの: `label`、`options`（`{value, label}` の配列）、`value` または `defaultValue`、`onChange`。
*Consumer provides: `label`, `options`, `value` or `defaultValue`, `onChange`.*

- 高さはスマホ 44px・PC 32px。ラベルは必ず付ける。エラーは文言で示し（`error`）、色だけにしない。
  *44px on touch, 32px on PC. Always label. Errors are shown in words (`error`), never color alone.*
- 選択肢が 5 件以下なら `RadioGroup` を使う（すべてが見えるほうが選びやすい）。多すぎると特にスマホで使いにくいので、先に質問を絞って選択肢を減らせないか考える。
  *With five or fewer options use `RadioGroup` (all visible, easier to choose). Too many options hurt on mobile, so first see whether an earlier question can narrow them.*
- タッチ操作の端末では文字を 16px にする（iPhone の Safari の自動拡大を避けるため）。
  *On touch devices text is 16px to avoid iPhone Safari auto-zoom.*
- 補足（`hint`）はラベルと選択欄の間、エラー（`error`）は選択欄の下に左寄せで置く。展開したリストは OS 標準のまま使う。
  *`hint` sits between the label and the select; `error` below, left-aligned. The opened list stays the OS default.*

**理由 / Why:** 6 件以上から 1 つ選ぶ。ブラウザ標準を使い、キーボードと読み上げの操作をそのまま生かす。
*Pick one of six or more: the native control keeps keyboard and screen-reader behaviour.*
