# 原則 / Principles

KM1 は、自分が作る道具の見た目と使い勝手をそろえるための標準である。適当に作ると、ひと目で AI が作ったと分かるデザインになり、使う人の嫌悪感につながる。だから KM1 は、使いやすさ（ユーザビリティ）を上げることを目的にする。無駄とムラは誰の得にもならないので省き、広く使ってもらうために、色の見え方・視力・使う場面の違いにも合わせる。
*KM1 keeps the look and usability of its author's tools consistent. Careless design reads at a glance as AI-made and puts people off, so KM1 exists to raise usability: waste and inconsistency help no one and go, and to reach more people it fits differences in colour vision, eyesight and situation.*

## 1. 前提: 誰でも使える / Premise: usable by anyone

色の見え方、視力、年齢、読み上げやキーボードだけでの操作、明るい屋外のような使う場面に関わらず使えることを、すべての前提にする。案に迷ったら「どちらがより多くの人に使えるか」を問い、そちらを選んでから磨く。
*Accessibility is the premise of everything. When in doubt, ask which option more people can use, choose it, then refine it.*

すべての部品で守ること / Required of every component:
- 文字は背景に対して 4.5:1 以上、操作要素の境界・アイコン・フォーカスの枠は 3:1 以上。 / *4.5:1 text; 3:1 control borders, icons and focus ring.*
- 色だけで伝えない（お知らせはアイコンと文言、リンクは下線、チェックは記号、分類は模様）。 / *Never colour alone (icon + word, underline, tick mark, pattern).*
- キーボードだけで操作でき、フォーカスがいつも見える。 / *Keyboard operable with a visible focus.*
- 押せる大きさは、タッチで 44px、マウスで 32px（小さいものでも 24px）以上。 / *Targets: 44px touch, 32px mouse (24px minimum).*
- 見出しの順序を飛ばさない。表は見出しセル、リストは本物のリスト要素。 / *Keep heading order; header cells in tables, real list elements.*
- 画像には代替テキスト、飾りの画像は空の alt。リンクは行き先が分かる言葉にする（「こちら」にしない）。 / *Alt text (empty for decoration); link text names the destination.*
- 動きを減らす設定（`prefers-reduced-motion`）と強制カラー（`forced-colors`）に従う。 / *Honour reduced motion and forced colours.*
- 書体は `lang` で切り替える（日本語は Noto Sans JP、英語は Segoe UI → Hind）。 / *Switch typefaces by `lang`.*

## 2. 3 つの軸 / Three axes

### 2.1 見やすい / Easy to see

目で正しく読めること。文字の大きさと濃さ、コントラスト、行の高さ、数字・時刻・単位の組み方で誤読させない。
*Read correctly at a glance: size, weight, contrast, line height and the setting of numbers, times and units leave no room for misreading.*

- 文字の大きさは 7 つ（12・14・16・20・28・40・68px）。見出しは 3 段で、となりの段とは 1.25 倍以上はなす。 / *Seven sizes; three heading steps at least 1.25x apart.*
- 文字の濃さは `ink` と `ink-secondary` の 2 段だけ。 / *Two text weights only.*
- 2 行以上になりうる文の行の高さは 1.5 倍以上、1 行は 40 字（40em）まで。 / *Wrapping text gets 1.5x line height and at most 40em per line.*
- 数字は桁をそろえ（等幅の数字）、数値と単位の間は半角あける。数とその前後の言葉の間では改行しない。 / *Tabular figures; a space before units; no break between a number and its word.*

### 2.2 わかりやすい / Easy to understand

頭で迷わないこと。1 画面に主役を 1 つ置き、今どうなっていて次に何をすればよいかが分かるようにする。言葉は平易で具体的にし、同じものはいつも同じ場所に置く。決まりは「画面の組み立て」の「わかりやすさ」と「言葉」。
*No hesitation: one focal point per screen, the current state and the next step visible, plain and specific words, and the same thing always in the same place. Rules: Patterns › Understandability, and Writing.*

- 1 画面に `primary` のボタンは原則 1 つ。ボタンの言葉は動詞。 / *One primary per screen; verb labels.*
- 1 つの `Card` は 1 つの作業にし、その作業に必要な情報だけを載せる。 / *One card, one task.*
- 設定は多くの項目を細かく調整させず、求める結果（プリセット）から選ばせる。基本の設定は初期値として組み込む。 / *Let people pick a result (a preset) instead of tuning many settings; build basic settings in as defaults.*
- 同じ値を 1 つの画面に 2 回並べない。 / *Never show the same value twice on one screen.*
- 1 つの場所で「開く」と「選ぶ」のように、押して起きることを 2 つにしない。 / *One place, one outcome when pressed.*

### 2.3 理由を言える / Every form has a reason

部品も画面も、なぜこの形なのかを一文で言えるものだけを置く。既定値のまま置いた影、決まった型の当てはめ、自分の役割を説明する文言のように、理由を言えない形は置かない。無駄（要らない形）とムラ（同じものが場所によって違うこと）も、理由を言えない形として省く。これは見た目の軸ではなく、2.1 と 2.2 を守れているかを確かめる検査である。
*Keep only forms whose reason fits in one sentence. Defaults left as they are, templates applied by habit, copy that describes itself, waste and inconsistency have no reason and go. This is the check that 2.1 and 2.2 hold.*

- すべての部品の `README.md` に「理由 / Why」の行を書く。ない部品は検査で止まる。 / *Every component README has a Why line; missing ones fail the checks.*
- 同じ状態を示す合図（色・面・線・太さ・形）は 3 つまで。重ねすぎると何が大事か分からなくなる。 / *At most three cues per state.*
- 値は決まった段（文字・余白・角丸・線・色）の中からだけ選ぶ。段の外の値は、精度の監査（`gen/precision_audit.js`）で止まる。例外は理由を書いて監査の中に置く。 / *Values come only from the scales; off-scale values fail the precision audit, and exceptions carry a written reason.*
- 人の目での確かめ方は「運用」の「理由の確認」。 / *Human review: Governance › Reason review.*

## 3. 優先の順番 / Order of priority

**アクセシビリティ → 見やすい → わかりやすい → 個性。** 個性のためにコントラストや読みやすさを下げない。簡潔さと説明の多さがぶつかるときは、伝わる方（アクセシビリティ）を先に取り、そのうえで最小限に近づける。
*Accessibility, then legibility, then understandability, then personality. Never lower contrast or legibility for personality. When brevity and explanation conflict, take what communicates first, then trim.*

## 4. 土台と味付け / Base and flavor

KM1 は 2 層で作る。
*Two layers.*

- **土台:** 部品の振る舞い・状態・トークンの構造・値は、Fluent 2 から始めた。キーボードの操作、フォーカス、ラベルの位置のような振る舞いは、使う人がすでに知っている形にそろえ、個性を出さない。 / *Base: component behaviour, states, token structure and values started from Fluent 2. Behaviour people already know (keyboard, focus, label position) stays familiar and carries no personality.*
- **味付け:** その上に KM1 が自分で決める層で、個性を出してよい。ただし、寸法や値で書けて検査できる決まりにし、上の優先の順番に従う。測れない「ちょっとした工夫」は置かない。 / *Flavor: KM1's own layer, where personality may show, but only as measurable, checkable rules that follow the order of priority.*
- **ブランドの色は 1 色:** 中立の面に、メインカラーの紺 `#10218B`（`brand`）を 1 色だけ差す。グラデーション・ガラス効果・強い影は使わない。紺は黒に近いので、紺の文字色だけで選択や強調を示さない。 / *One brand colour: navy `#10218B` on neutral surfaces; no gradients, glass or heavy shadows; never mark selection with navy text alone.*
- **流行を追わない:** 改良は `tokens.json` と文書を更新して積み上げ、判断は「運用」に記録する。 / *No trends; improve by updating `tokens.json` and the docs, and log the decision.*

取り込まないもの / Not adopted: Google Material 風の表現（大きな丸み、FAB、tonal の面、Ripple）、ほかの組織の配色・ロゴ・形。
*Material-style expression (large radii, FAB, tonal surfaces, ripple), and other organizations' palettes, logos and shapes.*

## 5. 従う規格 / Standards KM1 follows

規則の根拠として使う、外の規格と研究。KM1 の決まりは、これを KM1 の部品に当てはめて書き直したもの。
*External standards and research used as the basis for rules, restated for KM1's components.*

| 規格 / Standard | 使っているところ / Used for |
|---|---|
| WCAG 2.2 | コントラスト、押せる大きさ（2.5.5・2.5.8）、リフロー（1.4.10）、文字の間隔（1.4.12）、フォーカス |
| W3C ARIA Authoring Practices Guide | Tabs・Dialog・Menu などのキーボード操作と役割 |
| ISO 9241-210:2019（人間中心設計） | 「プロダクトデザイン」の 4 つの活動の順番（本文は未読。公開の目次と解説から確認） |
| Jakob Nielsen の応答時間の 3 つの目安（0.1・1・10 秒） | 待ち時間の表示の区切り |
| Jakob Nielsen の 10 のユーザビリティ原則 | 作ったものを点検する 10 項目（KM1 の部品に当てはめて書き直した） |
| Android・Apple・Windows の公式の指針 | 端末ごとの操作領域（Android 48dp、iOS 44pt、Windows のタッチ 44epx）と作法（「プラットフォーム」） |

出典 / Sources: 「参考文献」（`references.md`）の 1〜4 節。
