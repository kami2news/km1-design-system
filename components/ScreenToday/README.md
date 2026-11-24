スケジュール確認アプリの「今日」の画面の例。「画面の組み立て › わかりやすさ」の順番で、部品からではなく、開いた人が最初に知りたいことから作った。
*The "Today" screen of the schedule app, built in the order of Patterns › Understandability: from what the reader needs first, not from the parts.*

**理由 / Why:** 今日の画面を開く人が最初に知りたいのは「次はいつ、どこで、何か」なので、次の予定を時刻の大きな数字で主役にした。残りは主役から遠い順に「このあと」「締め切り」と下げ、まとまりの間を `space-xxl` あけて、縁ではなく余白で分けた。
*People open Today to learn what is next, when and where, so the next event's time is the focal point. The rest steps down by distance from it, separated by `space-xxl` rather than borders.*

## 組み立て / Composition
- 見出し行: 「今日」と、何時の時点の内容か（`ink-secondary`）。主ボタンは「予定を追加」の 1 つだけ、右に置く。
  *Heading row with the as-of time; one primary button, on the right.*
- 主役: 次の予定。時刻は 32px の太字で桁をそろえ（`tabular-nums`）、名前は 20px、場所と残り時間は 14px の `ink-secondary`。
  *Focal point: the next event; 32px bold tabular time, 20px name, 14px secondary place and time left.*
- このあと・締め切り: 左に時刻か日付を右ぞろえで置き、名前、右端に補足。行の区切りは `stroke-subtle` の細い線だけ。
  *Later and deadlines: right-aligned times or dates in the left column, the name, a note at the end; rows split by thin `stroke-subtle` lines only.*
- 1 日以内の締め切りは「あと 1 日」の文言を `danger-ink` の太字にする。色だけでなく、残りの日数を言葉で書く。
  *A deadline within a day sets "あと 1 日" in bold `danger-ink`; the words carry it, not just the colour.*
- 読み上げ: 各まとまりは `section` と見出し（`h3`）、行は本物のリスト、時刻は `time` 要素。
  *Each group is a `section` with an `h3`; rows are real lists; times use `time`.*

## やらないこと / Don't
- 次の予定・このあと・締め切りを同じ大きさのカードに並べない（どれが大事か分からなくなる）。
  *Don't lay the three groups out as equal cards.*
- 終わった予定を「このあと」に混ぜない。
  *Don't mix finished events into "Later".*
