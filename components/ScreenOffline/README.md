通信が切れたときの画面の例: 警告（Alert）、時点の表示、未送信の件数、つながったら自動で送ってお知らせ（Toast）。
*A screen pattern combining several components; also used for the scenario checks in README.*

**理由 / Why:** 通信が切れたときにいちばん大事なのは「何が送れていないか」なので、未送信の予定を件数つきで一番上に出す。送れた内容は、何時の時点のものかを添えてその下に置く。
*Offline, what matters most is what has not been sent, so pending events lead with their count; the synced list follows with its as-of time.*

**見本の始まり / Initial state:** 見本は、この画面の主役であるオフラインの状態（未送信 1 件）から始まる。実際のアプリでは `navigator.onLine` に従う（D40）。
*The example starts offline with one unsent event, the state it exists to show; real apps follow `navigator.onLine`.*
