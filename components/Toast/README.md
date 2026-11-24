操作の結果や時刻の通知を、画面の下に一時的に出すお知らせ。
*A temporary notice at the bottom of the screen for results and reminders.*

## 使い方 / Usage
- 中身はアイコン + 1 行の文言 + 操作 1 つまで（「元に戻す」「開く」）。長い説明や複数の操作は `Alert` か `Dialog` にする。
  *Icon, one line, at most one action. Longer text or several actions belong in `Alert` or `Dialog`.*
- `duration`（ミリ秒）を渡したときだけ自動で消える。操作付きは 10000 以上にするか、自動で消さない。×で必ず閉じられるよう `onClose` を渡す。
  *Auto-dismisses only when `duration` (ms) is set; with an action use 10000 or more, or none. Pass `onClose` so × always works.*
- エラーなど読み落とせない内容には使わない。画面に残る `Alert` を使う。
  *Not for errors that must not be missed: use a persistent `Alert`.*
- 読み上げには控えめなお知らせ（`role="status"`）として伝わる。フォーカスは奪わない。
  *Announced politely (`role="status"`); it does not take focus.*
- 位置は画面下の中央に固定、重なり順は `layer-message`。同時に出すのは 1 つ。トーストがフォーカス中の要素を隠さないよう、画面の下端にトーストの高さ分の余白を空けておく（WCAG 2.2 の 2.4.11）。
  *Fixed at bottom center on `layer-message`; show one at a time. Keep bottom padding equal to the toast height so it never hides the focused element (WCAG 2.2 2.4.11).*

## 利用側が渡すもの / You provide
`open`、文言、`onClose`、必要なら `status`（`info`・`success`・`warning`・`danger`）・`action`（`{label, onClick}`）・`duration`。

**理由 / Why:** 操作の結果を、作業を止めずに知らせる。画面の下に一時的に出し、元に戻すを添えられる。
*Report a result without stopping work: appears briefly at the bottom and can offer Undo.*
