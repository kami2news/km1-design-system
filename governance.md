# 運用の決まり / Governance

KM1 に何を入れ、何を入れないかを決める手続きと、変更・互換性・出典の扱い。判断を変えるときも、ここの手続きに従う。
*How KM1 decides what goes in, and how changes, compatibility and sources are handled—including reversing a decision.*

## 1. 判断の状態 / Decision states

| 状態 / State | 意味 / Meaning | 次に進む条件 / To move on |
|---|---|---|
| 提案 / Proposed | 案があるだけ | 目的・使う条件・既存との重複を書く |
| 保留 / On hold | 判断の材料が足りない | 足りない材料（比較・利用テスト・技術の制約）を書き、そろったら再検討 |
| 試行 / Trial | 条件つきで一部の画面だけに使う | 期間と、比べる指標を決める。終わったら採用か不採用 |
| 採用 / Adopted | 標準。部品・トークン・規則になっている | 変えるときは 3 章の手続き |
| 不採用 / Rejected | 理由を書いて入れない | 前提が変わったら「提案」から出し直す |
| 廃止予定 / Deprecated | まだ使えるが、次の版で外す | 代わりを書き、1 つの版のあいだは残す |

## 2. 判断の記録 / Decision log

| # | 対象 / Subject | 状態 | 日付 | 理由・条件 / Reason | 出典の章 |
|---|---|---|---|---|---|
| D1 | FAB（浮いた丸いボタン） | 不採用（2026-11-13 に再確認） | 2026-11-12 以前 | 内容と重なる・読む順と位置がずれる・アイコンだけでは意味が伝わらない。採るなら、今の配置と比べる利用テストを先にする | KM1 × M1 |
| D2 | Ripple（波紋） | 不採用 | 2026-11-12 以前 | 動かしてよいのは色・影・不透明度と 8px までの移動だけ。押した時は色の変化で伝える | 画面の組み立て › 動き |
| D3 | Carbon の Fluid スタイル・フォームの密度の切り替え | 不採用 | 2026-11-13 | 複雑なフォームに向かない。高さは入力方法で決まる | 画面の組み立て › フォーム |
| D4 | Card・Table・SortableList の密度 | 採用 | 2026-11-13 | コレクションとコンテナに限って余白だけを変える | トークン |
| D5 | ページ内のボタンの位置（Carbon の主ボタン左） | 不採用 | 2026-11-13 | KM1 の他の画面と揃える（PC は主ボタン右） | 画面の組み立て › フォーム |
| D6 | 動きのトークンを `tokens.json` に入れる | 閉じた（D12 に統合。確認日を過ぎたので 6 章の既定どおり、2026-11-24） | 2026-11-13 | 保存の形式が動きの族を読まない。生成スクリプトの中に持つ案を検討。代案は D12（2026-11-15） | KM1 × M1 |
| D7 | Dialog・Drawer のボタンの並び（CSS で見た目だけ逆にする） | 廃止（直した） | 2026-11-13 | DOM の順＝見た目の順に統一。スマホでは DOM の順ごと入れ替える | 変更履歴 |
| D8 | 仮想スクロール（大量の行） | 提案 | 2026-11-13 | 2,000 行を超えると選択の反応が遅れる。当面は 500 行まで＋ページ送り | 検証 |
| D9 | 密度の spacious を Spectrum 2 と同じ「1 段上」にそろえるか | 採用（今の値の 2 段上を続ける。確認日を過ぎたので 6 章の既定どおり、2026-11-24） | 2026-11-13 | 今は依頼の値（2 段上）。変えたくなったら提案から出し直す | トークン |
| D10 | 書体（Noto Sans JP）の自前配信 | 提案 | 2026-11-15 | 外部配信に頼らず、オフライン・社内網でも同じ字形にする。ライセンス（OFL 1.1）と配信量の確認が先 | トークン 7 章 |
| D11 | 不足領域の仕様案（期間入力・ツリー・グラフ・連続色） | 提案 | 2026-11-15 | 部品にする前に、仕様だけ先に決める。使う画面が出てから試行へ | 仕様案 |
| D12 | 動きのトークンを `duration`・`easing` の族として `tokens.json` に入れる（D6 の代案） | 提案 | 2026-11-15 | 保存の形式は単一の値の族を読める。族の数（12 まで）の確認と試行が先 | 仕様案 P4 |
| D13 | メインカラー `#10218B` の扱い | 採用 | 2026-11-18 | EPSON の青を参考にして KM1 が選んだ色として書く。「EPSON ブルー」と断定せず、EPSON の指定色としても扱わない。原典の確認は要らない | デザイン原則 |
| D15 | KM1 の軸: 前提はアクセシビリティ、軸は見やすい・わかりやすい・理由を言える。優先はアクセシビリティ → 見やすい → わかりやすい → 個性。土台（Fluent 2 など）と味付け（KM1 の個性）の 2 層 | 採用 | 2026-11-24 | AI が作ったような平均的な見た目を避け、何を大切にするかで判断できるようにする | デザイン原則 |
| D16 | Card の影をやめ、`stroke` の縁だけにする | 採用 | 2026-11-24 | カードは浮いていない。影は浮く部品（7 章の一覧）だけ。Flutter はもともと縁だけ | 部品 › Card |
| D17 | Alert の色の縁と色の文字をやめ、色は面だけにする | 採用 | 2026-11-24 | 状態はアイコンと言葉の 2 つで伝わる。同じことを 4 回言わない | 部品 › Alert |
| D18 | EmptyState を左寄せにし、アイコンを既定で外す | 採用 | 2026-11-24 | 中身が入るはずの場所で、同じ左の線から読ませる。真ん中の大きなアイコンは何も伝えない | 部品 › EmptyState |
| D19 | 形で押せるかを分ける: 押せるもの（ボタン・Chip）は角丸 `radius-md`、押せない印（Badge）と人（Avatar）は丸 | 採用 | 2026-11-24 | Badge と Chip が同じ丸で見分けにくかった。形で押せるかが分かれば、色や説明に頼らずに済む | 部品 › Chip・Badge・Avatar |
| D20 | 部品は、いま使う画面がなくても保管する（理由が言えれば外さない） | 採用 | 2026-11-24 | 部品が少ないと、必要になったときに作業が詰まる。使う画面がないことは、外す理由にしない | 運用 |
| D21 | 判断の記録と早見図（M1 との比較 7 個・IconTrial・Density・SelectionGuide）は消さずに保管し、部品の一覧とは別の「記録と早見図 / Records and guides」の群にまとめる。部品の数には数えない | 採用 | 2026-11-24 | 部品ではないものが部品に混ざると、部品の数と使い分けが分かりにくくなる。判断の根拠なので消さない | 運用 |
| D22 | 文字の大きさを 7 つ（12・14・16・20・28・40・68 px）に減らし、見出しを `title`・`subtitle-1`・`subtitle-2` の 3 段にする。`title-1`・`title-2`・`title-3`・`caption-2`（10 px）はなくす | 採用 | 2026-11-24 | 28・24・20 px のように段が近いと、大きさで上下が分からず、使い分けの理由も言えない。10 px は漢字の字形がつぶれ、部品でも使われていなかった | トークン・全部品 |
| D23 | 2 行以上になりうる文の行の高さを 1.5 倍以上にする（`body-1-para` 14/24 を新設、`body-2` 16/26、`caption-1` 12/18）。折り返す説明文は 1 行 40em まで | 採用 | 2026-11-24 | 行が詰まると次の行を追いにくい（WCAG 1.4.12 の考え方、デジタル庁 DADS は本文 150% 以上）。広い画面で行が長いと、次の行の始まりを探しにくい | トークン・全部品 |
| D24 | 文字の濃さを `ink` と `ink-secondary` の 2 段にし、`ink-secondary` を #424242 → #616161（ダーク #ADADAD）にする。`ink-tertiary` は同じ値の別名として残す。紺の文字色だけで選択や強調を示さない | 採用 | 2026-11-24 | #242424 と #424242 の比は 1.54 で、主と従の区別がつかなかった。#616161 は白地で 6.19:1 と読める濃さを保つ。紺は白地で 13.0:1 と黒に近い | トークン・全部品・Office |
| D25 | 状態の合図は 2〜3 つまでにする。ナビの選択中は、淡い紺の面・太字・塗りのアイコンで示し、上と左の線はやめる | 採用 | 2026-11-24 | 同じことを 4 つの合図で重ねると、画面がうるさくなり、何が大事か分からなくなる（AI の作る画面に多い「全部盛り」）。色以外の合図（太字・アイコンの形）が残っていれば足りる | Nav |
| D26 | 取り消せない操作の確認ボタンは `danger`（赤の文字）にし、`primary` にしない。見出しに対象の名前を入れる | 採用 | 2026-11-24 | 紺の `primary` は「こちらを選んでほしい」という合図。消す操作を勧める形にしない。何が消えるかは名前で分かるようにする | Dialog・Button |
| D27 | 入力例はプレースホルダに入れず `hint` に「例：」で書く。数字と単位・助数詞の間は半角あける（「第 8 回」「3 件」） | 採用 | 2026-11-24 | プレースホルダは入力を始めると消え、薄い文字は入力済みに見える。数字の書き方がそろわないのは「ムラ」 | Input・見本の文言 |
| D28 | ボタンを 4 種類（`primary`・`secondary`・`subtle`・`danger`）にまとめる。`outline` は `secondary`、`transparent` は `subtle` に読み替える。「キャンセル」は `secondary` | 採用 | 2026-11-25 | `secondary` と `outline` は面の色だけ、`subtle` と `transparent` は文字の色だけが違い、使い分けの理由が言えなかった。紺の文字のキャンセルは、やめる操作をいちばん目立たせてしまう | Button・Dialog・Flutter |
| D29 | 全部品の README に「理由 / Why」の行を書いた。これからは行がないと `reasoncheck.py` が FAIL にする | 採用 | 2026-11-25 | 理由を言えない形を増やさないため。なぜなぜのリストから写した | 運用 |
| D30 | 同じ値を 1 つの画面に 2 回並べない（見出しの下の要約と、その下の表など） | 採用 | 2026-11-25 | 同じことを 2 回読ませるのは「無駄」。どちらが正か迷わせる | 画面の例 |
| D31 | 一覧では「開く」と「まとめて選ぶ」を同時に出さない。まとめて選ぶのは「まとめて選ぶ」で入るモードにし、そのあいだ行は押すと選ぶ | 採用 | 2026-11-26 | 行の左にチェック、行の本体に開く操作があると、押した場所で結果が変わり、どちらも「選ぶ」と呼ばれて取り違える。今開いている行と、チェックした行の印（左の紺の線）も重なっていた | List・ScreenListEdit・Flutter |
| D32 | 枠なしのボタン（`subtle`）には必ずアイコンを付ける | 採用 | 2026-11-26 | 枠も塗りもない太字だけでは、見出しやラベルと見分けがつかず、押せると分からない | Button・部品の中のボタン |
| D33 | Flutter のナビ（`NavigationBar`・`NavigationRail`）も、選択中を淡い紺の面・太字・塗りのアイコンで示す | 採用 | 2026-11-26 | Material の既定（楕円の印・別の色）のままで、Web と見た目がずれていた（D25 にそろえる） | Flutter |
| D34 | 選択中の操作バーは淡い紺の面と件数の文字で示し、紺の枠をやめる | 採用 | 2026-11-26 | 面と枠の 2 つで同じ「選択中」を言っていた（D25 の重ねすぎ）。強制カラーでは枠で示す | ContextualActionBar・Flutter |
| D35 | ダークの淡い面（brand・info・danger・success・warning の tint）を、暗い面に色を 16% 混ぜた彩度の低い色にする | 採用 | 2026-11-26 | 前のダークの tint は濃く鮮やかで（#3B0509 など）、明るい画面の淡い面と釣り合わず、お知らせが 4 色のかたまりに見えた。新しい色でも、文字・状態の文字色・補足の灰はすべて 4.5:1 以上 | トークン |
| D36 | 並んだ領域の見出しは同じ段にする（一覧の見出しと詳しい内容の見出し） | 採用 | 2026-11-26 | 同じ h2 なのに 16 px と 20 px で、詳しい側が上の段に見えた。段の大きさは見出しの順位と一致させる | 画面の例 |
| D14 | KM1 本体のライセンス | 採用 | 2026-11-18 | MIT License。著作権表示は `LICENSE` に書き、名前はそこにだけ出す。PDF と Office には個人名を書かず、ライセンスの一文（notices 2.6）だけ載せる | 第三者表記 |

## 3. 判断を変える手続き / Changing a decision

1. **提案を書く:** 何を・なぜ変えるか、前の判断の理由のどれが変わったか。導入の記録（`adoption.md`）の穴 A1〜 から起こすときは、その番号を書く。
   *Write what changes and which earlier reason no longer holds.*
2. **影響を調べる:** 使っている部品と画面（`gen/tokens_check.py` の影響の表、`inventory.json`）、各 OS への影響。
   *Map the impact with the impact table and inventory.*
3. **比べる:** 今の形と新しい形を同じ画面で並べる見本を作る。操作に関わるものは利用テストか、少なくとも利用シナリオ（「検証」）で確かめる。
   *Compare side by side; for interaction changes, test with users or at least the scenarios.*
4. **決める:** 持ち主が決める。決めたら 2 章に記録し、変更履歴に書く。
   *The owner decides; record it here and in the changelog.*
5. **移す:** 互換性の規則（4 章）に従って、廃止予定の期間をおく。
   *Migrate per the compatibility rules.*

## 4. 互換性 / Compatibility

- **壊さない変更（いつでも可）:** 部品に任意の属性を足す、トークンを足す、文書を直す、見た目の不具合を直す。
  *Non-breaking: optional props, new tokens, doc fixes, visual bug fixes.*
- **壊す変更（廃止予定を経る）:** 属性やトークンの名前を変える・消す、既定の見た目を変える、DOM の構造を変えて利用側の CSS が効かなくなる。1 つの版で「廃止予定」と書き、次の版で外す。
  *Breaking changes (renaming/removing props or tokens, changing defaults or DOM) go through one edition as deprecated.*
- **確かめ方:** 既定の見た目は、全部の見本を変更の前後で画素ごとに比べる（動きは止める）。操作は利用シナリオと部品ごとの検査を流す。
  *Verify with before/after pixel comparison of all previews (animations frozen) plus scenario and component checks.*
- **版の名前:** `KM1 YYYY-MM-DD`（その日の最後の公開）。変更履歴の見出しと同じ。
  *Editions are named by date, matching changelog headings.*
- **版のタグとリリース:** 公開するたびに Git のタグ `km1-YYYY-MM-DD` を付け、PDF の表紙の版とソースのコミットを結ぶ。タグは付け直さない（使う側が固定した版が変わってしまうため）。同じ日にもう一度公開するときは `km1-YYYY-MM-DD.2` とする。タグごとに GitHub の Release を作り、`dist/` の配布物（PDF・ひな形・アイコンと模様の zip・DTCG のトークン）を添付し、変更履歴のその日の節を本文にする。手順は `CONTRIBUTING.md`。
  *Tag every publish `km1-YYYY-MM-DD` (never move a tag; use `.2` for a second publish that day) and create a GitHub Release with the `dist/` files and that day's changelog. Steps in `CONTRIBUTING.md`.*

## 5. 出典の扱い / Sources

| 出典 / Source | 状態 / Status | 扱い / How it is used |
|---|---|---|
| Fluent 2・Fluent System Icons | 確認済み（公式サイト・リポジトリ） | 基盤 |
| デジタル庁デザインシステム・WCAG 2.2・W3C APG | 確認済み | 規則の根拠 |
| Carbon・M1・Spectrum 2 | 確認済み（2026-11-13 に公式ページを参照） | 考え方だけを取り込む。見た目は取り込まない |
| EPSON の考え方 | 公開されている説明を参照 | デザイン原則の柱の 1 つ |
| メインカラー `#10218B` | 参考にした色（2026-11-18 に決定） | EPSON の青を参考にして KM1 が選んだ色として使う。EPSON の指定色とは書かず、原典の確認も要らない |
| Science Tokyo（ISCT） | 公開されている説明を参照 | デザイン原則の 3 つの柱の 1 つ（考え方の読み取り。ガイドラインの転記ではない） |

- 出典を足すときは、参照した日付と URL を本文の出典の欄に書く。原典を見ていないものは「未確認」と書き、根拠として使わない。
  *Record date and URL; mark unseen originals as unverified and don't rely on them.*

## 6. 保留と提案の期限 / Deadlines (KM1-GOV-002)

開いている判断（提案・保留・試行）には、次の確認日と「決まらないときの既定」を置く。放っておいても、既定の側に倒れるだけで、壊れない。確認は `gen/govcheck.py` で流す。日付は仮置きで、持ち主が変えてよい。
*Every open decision (proposed, on hold, trial) has a next review date and a default if nothing is decided. Dates are provisional; the owner may change them. Run `gen/govcheck.py`.*

| 判断 | 状態 | 次の確認日 | 担当 | 決まらないときの既定 | 決める条件 |
|---|---|---|---|---|---|
| D12 | 提案 | 2026-11-30 | 持ち主 | `bundle.css` に持ったままにする | 族の数が 12 以内で、1 画面で試して問題がない |
| D10 | 提案 | 2026-12-06 | 持ち主 | Google Fonts のままにする | OFL の表記と配信量が確認でき、検査 `fontcheck` が通る |
| D11 | 提案 | 2026-12-13 | 持ち主 | 仕様案のままにする | 使う画面が 1 つ出る |
| D8 | 提案 | 2026-12-15 | 持ち主 | 500 行の規則を続ける | 導入の記録で 300 行超の画面が 2 つ出る |

## 7. 理由の確認 / Reason review

「デザイン原則」の軸 3「理由を言える」の手続き。部品・画面を足すとき、変えるときに必ず通す。
*The procedure for axis 3. Required whenever a part or screen is added or changed.*

1. **理由を一文で書く:** 部品の `README.md` の最初の段落のあとに「**理由 / Why:**」の行を置き、なぜこの形かを一文で書く。書けない形は置かない。
   *Write a one-sentence "Why" line in the part's README; if you can't, the form goes.*
2. **問いに答える:** 次の問いに全部「はい」と答えられること。
   *Answer yes to every question:*
   - これを消したら、誰かが困るか（部品は、いま使う画面がなくても、いつか困るなら残す。D20）。 / *Would anyone miss it, now or later? (D20)*
   - 既定値を、理由なくそのまま使っていないか。 / *No default kept without a reason?*
   - 同じことを 3 つ以上の手段で言っていないか（状態はアイコンと言葉の 2 つ、色は 1 か所）。 / *No message said three ways or more?*
   - 見本の文言は本物の内容か。 / *Is the sample copy real content?*
   - 優先の順番（アクセシビリティ → 見やすい → わかりやすい → 個性）に反していないか。 / *Does it respect the order of priority?*
3. **型を疑う:** 次の形は、AI が作る平均的な画面に多く、理由なく置かれやすい。使うときは理由の行にその理由を書く。
   *These forms are common in averaged, AI-made screens; using one needs its own reason:*
   - 真ん中に大きなアイコン・見出し・説明・ボタンを積んだ空の状態 / *the centred big-icon empty state*
   - 同じ大きさ・同じ重さのカードの並び / *rows of equal-weight cards*
   - 浮いていない面への影、縁と影の両方 / *shadows on parts that don't float; border plus shadow*
   - 色の面・色の縁・色の文字・アイコンを全部重ねた知らせ / *alerts with tint, coloured border, coloured text and icon all at once*
   - 部品や見本を説明する文言（「クリックできるカード」） / *copy that describes the part itself*
4. **機械の確認:** `python3 gen/reasoncheck.py`。浮いていない部品の影と見本の文言は FAIL、理由の行がない部品は件数を WARN で出す。人の確認の代わりにはならない。
   *`gen/reasoncheck.py` fails shadows on non-floating parts and self-describing sample copy, and counts parts without a Why line. It does not replace the human review.*
