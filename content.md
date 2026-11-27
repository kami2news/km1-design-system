# 言葉 / Writing

画面・文書・スライドに出る言葉の決まり。言葉も部品と同じく「わかりやすい」の軸に従い、本物の物と操作の名前で、短く書く。
*Rules for the words on screens, documents and slides. Words follow the "easy to understand" axis like components do: real names of things and actions, kept short.*

## 1. 文と口調 / Sentences and tone

- 敬体（です・ます）を基本とし、UI ラベル・見出し・ボタンは体言止めか動詞の終止形。感嘆符、絵文字、キャラクター口調は使わない。
  *Use polite Japanese for sentences; labels, headings and buttons are nouns or dictionary-form verbs. No exclamation marks, emoji or character voices.*
- 1 つの文は短く（目安 40 字まで）、1 つのことだけを言う。
  *Keep sentences short (about 40 characters), one idea each.*
- 専門の言葉は、使う人の言葉に置き換える。
  *Replace jargon with the user's words.*
- 英字は文頭のみ大文字（sentence case）。例: 「Add new item」。
  *English uses sentence case: "Add new item".*

## 2. 本物の名前で書く / Real names

- 物と操作は本物の名前と数で書く（「予定 3 件」ではなく「授業 2 コマ、バイト 1 回」が分かるなら、そう書く）。見本や試作でも、部品や見本を説明する文（「クリックできるカード」）は書かない。
  *Name real things and real counts; even in samples, never write copy that describes the part itself.*
- 部品や見本そのものを説明する文（「クリックできるカード」「ここに説明が入ります」）は、見本や試作でも書かない。理由を言えない文言の代表で、AI が作った画面に見える原因になる。
  *Never write copy that describes the part itself, even in samples: it has no reason and is a hallmark of AI-made screens.*
- 入力の例は入力欄の中（プレースホルダ）に書かず、欄の説明（`hint`）に「例：」として書く。プレースホルダは入力を始めると消え、薄い文字は入力済みの値に見える。
  *Put examples in the field hint ("例：…"), not the placeholder.*

## 3. ボタンと操作の言葉 / Buttons and actions

- 文言は簡潔で、動詞から始める。ボタンは「保存」「キャンセル」「追加」のように 2〜4 文字の動詞。「OK」「はい」だけのラベルは避ける。
  *Keep copy short and lead with a verb. Use short verbs such as Save, Cancel, Add; avoid bare "OK" or "Yes".*
- 実行しない側の言葉を使い分ける: 何も変えずに引き返すのは「キャンセル」、読むだけの画面を消すのは「閉じる」、前の画面に移るのは「戻る」、済んだ操作を無かったことにするのは「元に戻す」。「やめる」「中止」「取り消し」は使わない（何をやめるのかが文脈で変わるため）。操作そのものが予約などの取り消しのときは、実行する側を「予約を取り消す」のように対象つきで書き、実行しない側は「戻る」にする。
  *Words for not proceeding: "キャンセル" backs out with no change, "閉じる" dismisses a read-only view, "戻る" goes to the previous screen, "元に戻す" undoes a finished action. "やめる", "中止" and "取り消し" are not used, since what they stop depends on context. When the action itself cancels something (a booking), name the object on the confirming side ("予約を取り消す") and use "戻る" for the other.*
- 取り消せない操作の確認は、見出しに対象の名前を入れる（「『環境化学 第 8 回』を削除しますか？」）。本文で何が消えるかを 1 文で書く。
  *Irreversible confirmations name the object in the title and say what will be lost in one sentence.*
- 同じ操作に違う言葉を使わない。どの画面でも同じ言葉にする。
  *One action, one word, on every screen.*

## 4. 状態とエラー / States and errors

- エラーは「何が起きたか＋どうすればよいか」を 1 文で。
  *Errors say what happened and what to do, in one sentence.*
- 状態は色だけで伝えず、必ず文言かアイコンを添える。
  *Never convey state by color alone; add a label or icon.*
- 空の状態は、何が無いかと、本物の次の一歩を書く（「授業はまだありません。時間割から追加します」）。
  *Empty states say what is missing and give the real next step.*

## 5. 数字と単位 / Numbers and units

- 数値と単位・助数詞の間は半角あける（「3 件」「第 8 回」「40 分」「12 px」）。ただし「%」と、ファイル名・型番の中の数字はそのまま。
  *A half-width space between a number and its unit or counter; not before "%" or inside file names and model numbers.*
- 数とその前の言葉の間では改行させない（「レポート 3」の間は改行しない空白にする）。
  *No line break between a number and the word it belongs to (use a non-breaking space).*
- 数字は等幅の数字（`font-variant-numeric: tabular-nums`）で桁をそろえる。表の数値は右寄せ。
  *Tabular figures; right-align numbers in tables.*
- 主役の数字は大きく太くし、単位は小さく `ink-secondary` にする。
  *A focal number is large and bold; its unit smaller in `ink-secondary`.*

## 6. 日付と時刻 / Dates and times

- 日付は「11/12（木）」、年が要るときは「2026/11/12（木）」。曜日は丸括弧で 1 文字。
- 時刻は 24 時間制で「9:00」。時の先頭に 0 を付けない。範囲は「9:00〜9:50」。
- 終日は「終日」と書く。0:00 ちょうどの締め切りは、前日の終日として見せる。
- 相対表現（「今日」「明日」）は日付と併記する: 「今日 11/12（木）」。
*Dates as "11/12（木）" (add the year as "2026/11/12（木）" when needed); 24-hour times without a leading zero ("9:00"); ranges with "〜"; "終日" for all-day; a 0:00 deadline is shown as all-day on the previous day; relative words go with the date.*

## 7. 検査 / Checks

`gen/reasoncheck.py` が見本の文言を調べる: 部品を説明する文、入力例をプレースホルダに入れたもの、数と助数詞の間があいていないもの、削除を `primary` にしたボタン。
*`gen/reasoncheck.py` checks preview copy: self-describing text, examples in placeholders, digits stuck to counters, and delete as primary.*
