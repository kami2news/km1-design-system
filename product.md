# プロダクトデザイン / Product design

「どう見せるか」の前に「何を、誰の、どの場面のために作るか」を決める手順。ここで決めたことが、画面の組み立て → 部品 → トークンの順に下りていく。対象はアプリやツールなどの画面のある製品で、形のある製品（筐体や素材）は扱わない。
*How to decide what to build, for whom and for which situation, before deciding how it looks. Decisions made here flow down into patterns, components and tokens. Scope: products with screens (apps, tools); physical products are not covered.*

| 層 / Layer | 決めること / Decides | KM1 の場所 / Where |
|---|---|---|
| プロダクト / Product | 誰の何を解決するか、何を作らないか / whose problem, what not to build | このページ / this page |
| 画面の組み立て / Patterns | 画面の分け方、移動、状態 / screens, navigation, states | 画面の組み立て / Patterns |
| 部品 / Components | 個々の操作 / individual controls | Components |
| トークン / Tokens | 色・大きさ・動き / color, size, motion | Tokens |

進め方は、人間中心設計の国際規格 ISO 9241-210:2019 の 4 つの活動（使う場面を理解する → 要求を決める → 形にする → 確かめる）の順にしている。一度で終わらせず、確かめた結果で前の段に戻る。
*The order follows the four activities of ISO 9241-210:2019 (understand the context of use → specify requirements → produce solutions → evaluate). It is a loop: evaluation sends you back.*

## 1. 使う場面を書く / Context of use

次の 5 つを、それぞれ 1 文で書く。書けない項目が残っているうちは、画面を作り始めない。
*Write one sentence for each of these five. Do not start on screens while any is blank.*

1. **誰が / Who**: 年齢や職業ではなく、状況で書く（「授業とバイトを掛け持ちしている学生」）。
2. **いつ・どこで / When and where**: 「朝、家を出る前に」「電車の中で片手で」。
3. **どの端末で / On what**: スマホか PC か、両方ならどちらが主か。部品の高さ（44px・32px）と画面幅の決まりがここで決まる。
4. **何を済ませたいか / The job**: 「今日どこに何時に行けばよいかを 10 秒で知りたい」。機能の名前ではなく、済んだ状態で書く。
5. **今はどうしているか / Today's workaround**: 「LINE とメールと時間割アプリを順に見ている」。これより楽にならないなら作る意味がない。

*Describe people by situation, not demographics; describe the job as a finished state, not a feature; the current workaround is the bar to beat.*

## 2. 要求を決める / Requirements

- 要求は「〜のとき、〜したい。なぜなら〜」の形で書く。
  *Write each requirement as "When …, I want to …, because …".*
- 全部を 3 つに分ける: **必ず**（これが無いと「済ませたいこと」が済まない）、**あとで**、**やらない**。「やらない」を必ず 1 つ以上書く。
  *Sort into **must** (the job fails without it), **later** and **won't**. Always write at least one "won't".*
- 「必ず」には、数えられる確かめ方を付ける: 「起動から今日の予定が見えるまで 2 タップ以内」「予定の追加が 30 秒以内」。数えられない要求（「使いやすい」）は要求にしない。
  *Each "must" gets a countable check ("today's schedule within 2 taps of launch"). Uncountable wishes ("easy to use") are not requirements.*
- 「必ず」は 5 個まで。6 個目が出たら、どれかを「あとで」に落とす。
  *Five "musts" at most; a sixth pushes one down to "later".*

### 迷ったときの優先順位 / When requirements conflict

上にあるものを優先する。 / Higher wins.

1. **失わせない / No loss**: 入力したものが消えない。取り消せる。取り消せない操作は確認する。
2. **誰でも使える / Usable by everyone**: KM1 のアクセシビリティの決まり（コントラスト、操作領域、キーボード、色だけに頼らない）を満たす。
3. **迷わせない / No guessing**: 次に何をすればよいかが、画面を見て分かる。
4. **速い / Fast**: 手数と待ち時間が少ない。
5. **見た目 / Looks**: 上の 4 つを満たした上で整える。

## 3. 形にする / Design

KM1 の決まりは 2 種類ある。**必須**は例外を作らない。**原則**は既定の答えで、理由を書けば外してよい。
*KM1 has two kinds of rules. **Musts** have no exceptions. **Defaults** are the standard answer and may be broken with a written reason.*

| 区分 / Kind | 決まり / Rules | 外してよいとき / When it may be broken |
|---|---|---|
| 必須 / Must | 入力を失わせない、取り消せない操作の確認、アクセシビリティ（コントラスト・操作領域・キーボード・色だけに頼らない）、10 秒以上の待ちで工程と時間の見込みを出す | 外さない / never |
| 原則 / Default | 1 画面 = 1 目的 | 比べながら決める画面（2 つの予定の比較など）、慣れた人が毎日使う作業画面 |
| 原則 / Default | プライマリボタンは 1 画面に 1 つ | 同じ重さの作業が並ぶ一覧の各行（行ごとの「承認」など）。そのときは画面全体のプライマリを作らない |
| 原則 / Default | 行き先は 5 個まで | 業務用で利用者が慣れている場合。6 個目以降はサイドバーで分類して見出しを付ける |
| 原則 / Default | 一覧を押したらまずプレビュー | 直すことが主な一覧（「画面の組み立て」参照） |

外したときは、プロダクトメモの「確かめた記録」に、どの原則をなぜ外したかを 1 行書く。
*When you break a default, record which and why in the product memo.*

- **主な流れを 1 本、先に決める。** 「済ませたいこと」を済ませるまでの手順を 5 ステップ以内で書き、その流れに出てくる画面から作る。設定やアカウントの画面は後回しにする。
  ***Design one main flow first:** five steps or fewer from start to "job done", and build the screens on that flow before settings or account screens.*
- **1 画面 = 1 目的（原則）。** 画面ごとに「この画面で済むこと」を 1 文で書く。2 つ書きたくなったら、まず画面を分けられないか考える。プライマリボタンも原則 1 画面に 1 つ。外してよい場面は上の表のとおり。
  ***One screen, one purpose (default).** If a screen needs two sentences, first try splitting it; one primary button per screen by default. Exceptions are in the table above.*
- **言葉の一覧を作る。** 扱う「もの」（予定、締め切り、タスクなど）と操作（追加、取り込み、完了など）の呼び名を表にして、画面・通知・エラーで同じ言葉を使う。
  ***Keep a vocabulary list** of the things (event, deadline, task) and actions (add, import, complete), and use the same words in screens, notifications and errors.*
- **行き先は 5 個まで（原則）。** 主な行き先を 5 個以内にまとめて `Nav` に載せる。収まらないときは、まずプロダクトの範囲が広すぎないかを見直す。業務用などの例外は上の表のとおり。
  ***Five destinations (default)** in `Nav`; if more are needed, first check whether the scope is too wide. Exceptions are in the table above.*
- **状態を先に全部書く。** 画面ごとに、次の 6 つの状態でどう見えるかを決めてから作る。
  ***List every state first.** Decide how each screen looks in these six states before building.*

| 状態 / State | 見せるもの / Show | 部品 / Component |
|---|---|---|
| まだ何も無い / Empty | 何が入る場所か + 最初の一歩のボタン / what belongs here + first action | `EmptyState` |
| 読み込み中 / Loading | 何を待っているか。10 秒以上なら工程と時間の見込みを必ず（残り時間、実績の幅、または経過時間と理由） / what is loading; steps and a time estimate if 10s or more | 10 秒未満は `Spinner`、以上は `Progress`（`steps` と `remaining` か `elapsed`） |
| うまくいった / Success | 結果 + 取り消し / result + undo | `Toast`（「元に戻す」つき） |
| 入力の誤り / Input error | どこが、どう直せばよいか / where and how to fix | `Input` などの `error` |
| 失敗・つながらない / Failure, offline | 何が起きたか + もう一度試す。入力は消さない / what happened + retry; keep input | `Alert`（`danger`）+ ボタン |
| 多すぎる / Too much | 絞り込みか分割 / filter or split | `Chip`、`Pagination`、`Table` の並べ替え |

## 4. 確かめる / Evaluate

作ったら、次の順に確かめる。飛ばさない。 / Check in this order, skipping none.

1. **自分で主な流れを通す。** スマホの幅と PC の幅、ライトとダーク、キーボードだけ、の 3 通りで、最初から最後まで。
   ***Walk the main flow yourself** at phone and PC widths, in light and dark, and with the keyboard only.*
2. **「必ず」の確かめ方を数える。** 2 で書いた数（タップ数、秒数）を実際に数える。届かなければ 3 に戻る。
   ***Count the checks** written in step 2; if they fail, go back to step 3.*
3. **10 項目で点検する。** 下の表（Jakob Nielsen の 10 のユーザビリティ原則を、KM1 の部品に当てはめたもの）。
   ***Inspect against ten points** (Jakob Nielsen's ten usability heuristics, mapped to KM1).*
4. **1 人に試してもらう。** 説明せずに「〜を済ませてください」とだけ伝え、止まった場所と口にした言葉を書き留める。直すのは、止まった場所から。
   ***Watch one person try it** with only the goal stated, no explanation; note where they stop and what they say, and fix those places first.*

| # | 点検すること / Check | KM1 での答え / In KM1 |
|---|---|---|
| 1 | 今どうなっているかが見える / status is visible | `Spinner`・`Progress`・`Toast`、選択中の表示 |
| 2 | 利用者の言葉で書いてある / speaks the user's language | 言葉の一覧、日付と時刻の書き方 |
| 3 | 途中で引き返せる・元に戻せる / exit and undo | `Dialog` の「キャンセル」、`Toast` の「元に戻す」 |
| 4 | 同じものは同じ見た目と言葉 / consistent | 部品とトークンを使う。独自の色や大きさを足さない |
| 5 | 間違えにくい / prevents errors | 取り消せない操作の確認、選択肢で入れさせる（`Select`・`RadioGroup`・`Calendar`） |
| 6 | 覚えさせない / recognition, not recall | 選択肢を見せる、プレビューカード、入力例をヒントに書く |
| 7 | 慣れた人は速くできる / shortcuts for experts | キーボード操作、`Menu`、貼り付けでの取り込み |
| 8 | 余計なものが無い / nothing extra | 1 画面 = 1 目的、プライマリは 1 つ（どちらも原則） |
| 9 | エラーから立ち直れる / recover from errors | エラーは「どこが・どう直すか」を文言で。入力は消さない |
| 10 | 助けがその場にある / help in place | ヒント（ラベルと欄の間）、`Tooltip`、`EmptyState` の説明 |

## 5. 出す前の確認 / Before release

- [ ] 「必ず」の確かめ方が全部通っている。 / Every "must" check passes.
- [ ] 全画面で 6 つの状態を見た。 / Every screen seen in all six states.
- [ ] スマホの幅（360px）と PC の幅で崩れない。 / No breakage at 360px and at PC width.
- [ ] ライトとダークの両方で読める。 / Readable in light and dark.
- [ ] キーボードだけで主な流れを最後まで通せる。 / Main flow completes with the keyboard only.
- [ ] 取り消せない操作にはすべて確認がある。 / Every irreversible action confirms.
- [ ] 10 秒以上かかる処理はすべて、工程と時間の見込み（残り時間、実績の幅、または経過時間と見積もれない理由）を出している。根拠のない残り時間は出していない。 / Every wait of 10s or more shows steps and a time estimate (time left, a past range, or elapsed time with the reason); no invented time left.
- [ ] KM1 に無い色・大きさ・部品を足していない。足したなら下の「KM1 に戻す」を行う。 / No colors, sizes or components outside KM1, or they are fed back as below.

## 6. KM1 に戻す / Feeding back into KM1

- アプリを作る中で KM1 に無い工夫が必要になったら、まずアプリ側で作り、うまくいったものを KM1 に書き戻す（トークン、部品、または「画面の組み立て」）。
  *When an app needs something KM1 lacks, build it in the app first, then write what worked back into KM1 (a token, a component, or a pattern).*
- 2 つ目のアプリでも同じ工夫が要ったら、それは KM1 に入れる合図。1 回きりのものは入れない。
  *Needing the same thing in a second app is the signal to add it; one-offs stay out.*
- KM1 の決まりを破る必要が出たら、破る前に決まりのほうを直す。アプリごとの例外を作らない。
  *If a rule must be broken, change the rule first; no per-app exceptions.*
- 使って分かった不足は、`adoption.md` の導入の記録に穴（A1〜）として積み、「2 つ目のアプリでも起きたら KM1 に入れる」の合図を記録から読む。
  *Gaps found in use go into the adoption ledger (`adoption.md`, A1…); the second-app signal is read from that ledger.*

## 記入用の型 / Template

```md
# （プロダクト名）のプロダクトメモ

## 使う場面
- 誰が:
- いつ・どこで:
- どの端末で（主）:
- 何を済ませたいか:
- 今はどうしているか:

## 要求
| 要求（〜のとき、〜したい。なぜなら〜） | 区分（必ず・あとで・やらない） | 確かめ方（数えられる形） |
|---|---|---|

## 主な流れ（5 ステップ以内）
1.

## 言葉の一覧
| 呼び名 | 意味 | 使わない言い方 |
|---|---|---|

## 行き先（原則 5 個まで）と、各画面で済むこと
| 画面 | この画面で済むこと（1 文） |
|---|---|

## 確かめた記録
| 日付 | 何を確かめたか | 結果 | 直すこと |
|---|---|---|---|
```

## 記入例: スケジュール確認アプリ / Worked example

「確かめ方」の数字は仮の目安で、まだ測っていない。 / The check figures are provisional and not yet measured.

- **誰が**: 授業とバイトを掛け持ちしている学生。
- **何を済ませたいか**: バイトのシフト・授業の時間割・締め切りを、1 か所で確認したい。
- **主な流れ**: 開く → 今日の予定が見える → 必要なら今週に切り替える。

| 要求 | 区分 | 確かめ方（仮） |
|---|---|---|
| 開いたとき、今日と今週の予定をすぐ見たい | 必ず | 起動から 0 タップで今日、1 タップで今週 |
| 締め切りとタスクを予定と同じ場所で見たい | 必ず | 今日の画面に締め切りが旗のアイコン + 時刻で出る |
| メールなどの文章を貼り付けて予定に反映したい | 必ず | 貼り付けから保存まで 3 操作以内 |
| 予定をアプリ内で手入力したい | 必ず | 追加が 30 秒以内 |
| ログインしなくても使いたい | 必ず | 初回起動からログイン無しで追加できる |
| 毎週の予定を、その回だけ・それ以降で変えたい | あとで | — |
| メールを自動で読み取って予定にする | やらない（アプリの外で別に行う） | — |

## 出典 / Sources

「参考文献」（`references.md`）の 3 節。

「迷ったときの優先順位」「5 個まで」「6 つの状態」「KM1 に戻す」は KM1 独自の決まり。
*The priority order, the limits of five, the six states and the feedback rules are KM1's own.*
