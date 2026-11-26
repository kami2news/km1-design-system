# 仕様案 / Proposals

KM1-PRP-001。KM1 にまだない部品・トークンの仕様案。どれも状態は**提案**で、実装も検証もしていない。決める手順と期限は「運用の決まり」（`governance.md`）。使う条件は、`adoption.md` の台帳に、不足として書いてから進める。
*KM1-PRP-001. Specs for parts and tokens KM1 does not have yet. All are **proposals**: nothing is implemented or verified. Decision steps and deadlines are in `governance.md`; start from a gap logged in `adoption.md`.*

| # | 対象 | 状態 | 判断の番号 |
|---|---|---|---|
| P1 | 日付範囲 `DateRange` | 提案 | D11 |
| P2 | ツリー `Tree` | 提案 | D11 |
| P3 | グラフ `Chart` | 提案 | D11（規則は `dataviz.md`） |
| P4 | 動きのトークンの `duration`・`easing` | 提案 | D12（D6 の代案） |
| P5 | 連続量の色の段階 | 提案 | D11 |

## P1. 日付範囲 / DateRange

**目的:** 開始日と終了日の組を選ぶ（予定の繰り返しの範囲、グラフの期間、レポートの期間）。
**使い分け:** 日付 1 つは `Input`（`type="date"`）か `Calendar`。期間は `DateRange`。離れた複数の日は対象外。
**既存との重複:** `Input` の日付と `Calendar` で、日付の 1 つずつは選べる。足りないのは、2 つを 1 組として検証し、読み上げ、カレンダー上で範囲を見せる部分。

**仕様案 / Spec**
- 既定は `FormGrid columns={2}` に「開始日」「終了日」の `Input`（日付）を並べる形。ここまでは既存の部品だけで作れる。
- 任意で、`Calendar` による範囲の選択を足す。広い画面は `Popover`、640px 未満は `BottomSheet`。1 回目の選択が開始、2 回目が終了。
- 検証: 終了が開始より前なら、エラーは「終了日は開始日（11/12）以降にしてください。」。入力した値は自動で直さず、消さない（フォームの規則）。
- 上限: `maxDays` を指定したときは「最大 31 日までです。」のように件数を書く。
- 近道（任意）: 「今日」「今週」「今月」を `Chip` で最大 4 つ。
- 読み上げ: 選ぶたびに `role="status"` で「開始日 11/12（木）。終了日を選んでください」「期間 11/12（木）〜11/15（日）、4 日間」と伝える。
- キーボード: `Calendar` の既存のキー。Enter で確定、Esc で閉じて、開いたボタンへフォーカスを戻す。
- 表記: 「11/12（木）〜11/15（日）」（日付と時刻の書き方）。
- Flutter: `showDateRangePicker` は Material の見た目なので使わない。`Km1Calendar` をもとに `Km1DateRange` を作る。
- 見た目（端点と間の日の塗り）: 試行のとき、見本を並べて決める（色だけに頼らず、端点に形か文字の印を付ける）。

**未決:** 期間の端点の塗り方、`Chip` の近道の既定、Flutter の部品の作り。
**検証:** 利用シナリオに S4「期間を選ぶ」を足す（キーボードのみ・読み上げ・320px）。

## P2. ツリー / Tree

**目的:** 3 段以上の階層（分類、フォルダ、組織）を、開閉しながら選ぶ。
**使い分け:** 2 段までなら `Accordion` か `ListSection` で足りるので、ツリーは 3 段以上に限る。画面の移動には `Nav` を使い、ツリーにしない。

**仕様案 / Spec** — 振る舞いは W3C ARIA Authoring Practices Guide の Tree View に合わせる。
- 役割: 入れ物は `role="tree"`、項目は `role="treeitem"`、開閉は `aria-expanded`、深さは `aria-level`、選択は `aria-selected`。子の入れ物は `role="group"`。
- キー: 上下で移動、右で開く（開いていれば最初の子へ）、左で閉じる（閉じていれば親へ）、Home・End で先頭・末尾、Enter で選ぶ、文字入力で頭文字へ移動。
- 大きさ: 1 行の高さは PC 32px・タッチ 44px（`--control-height`）。段ごとの字下げは `space-xl`（20px）。開閉の印は KM1 のアイコン（向きの違う 2 つ）で、色だけに頼らない。
- 複数選択: チェックを付ける形は、`Checkbox` の「一部だけ選択」の状態が KM1 にあるかを先に確かめる（未確認）。
- 数の上限: 1 画面で開いた項目は 500 行まで（大量のデータの規則）。
- 空・読み込み中: `EmptyState`・`Skeleton`。子を読み込む間は、その項目に `Spinner` と「読み込み中」。
- Flutter: Material の `ExpansionTile` を重ねず、`Km1Tree` を作る（読み上げは `Semantics` の階層）。

**未決:** 複数選択の「一部だけ選択」、字下げの線を引くか、読み込みの出し方。
**検証:** キーボード操作の一式、読み上げ（NVDA・VoiceOver・TalkBack）、500 行の反応の時間。

## P3. グラフ / Chart

**目的:** `dataviz.md` の規則を守った棒・折れ線を、1 つの部品で出す。
**既存との重複:** 模様の塗り（`CategoryMark`・`f2-pat--lg`・`Km1PatternPainter`）と凡例（`CategoryLegend`）はある。足りないのは、軸・目盛・点・直接ラベル・表の切り替えを一式で持つ部分。

**仕様案 / Spec**
- 引数: `type`（`bar`・`line`）、`series`（名前・値の配列・`categoryStyle` の番号）、`x`（項目名）、`unit`（単位）、`summary`（要約。**必須**。`aria-label` になる）、`table`（既定は表を付ける）。
- 出力: Web は SVG（`role="img"`）と、同じ値の `Table`。Flutter は `CustomPainter` と `Semantics`。
- 規則の適用: `dataviz.md` の M1〜M8 を部品が自動で満たす。`summary` がなければ描かずに、開発時にエラーを出す。
- 状態: 空・読み込み中・失敗は部品の中で出し分ける。

**未決:** 折れ線の数値のラベルの出し方、凡例の位置の自動切り替え、トークン化する数値（点の大きさ・破線）。
**検証:** `dataviz.md` の点検に加えて、軸の目盛の自動計算が区切りのよい値になるか。

## P4. 動きのトークン / Motion tokens (D6 の代案)

**背景:** D6 は「動きのトークンを `tokens.json` に入れる」で、保存の形式が動きの族を読まないため保留だった（2026-11-26 に D12 へ統合して閉じた）。保存の形式は、名前が `motion` の族を特別に扱わないが、ほかの名前の `{tokens:[…]}` は族として読み、単一の値（`150ms` や `cubic-bezier(…)` など）を保てる。族の名前を `duration` と `easing` にすれば、障害は解ける可能性がある。
*Background: D6 was held because the storage format has no motion family. It does read other `{tokens:[…]}` families with single CSS values, so naming them `duration` and `easing` may work. To be confirmed by trying it.*

**仕様案 / Spec**
1. `tokens.json` に族 `duration`（`duration-faster`・`duration-fast`・`duration-normal`）と族 `easing`（`curve-easy-ease`・`curve-decelerate`・`curve-accelerate`）を足す。名前は今の CSS 変数と同じにする。値は `components/bundle.css` の今の変数からそのまま写す（新しい値は作らない）。
2. 族の数の上限は 12。`tokens.json` の今の族の数を先に数える（未確認）。
3. ページが `tokens.css` を作ったら、`bundle.css` の同じ変数の宣言を外して、出どころを `tokens.json` の 1 つにする。
4. Flutter の `Km1Motion` と、WinUI・Compose・SwiftUI の生成（`gen/km1_dart.py`・`gen/native.py`）が、新しい族を読むようにする。
5. `gen/tokens_check.py` に、値の一致と `bundle.css` に宣言が残っていないことの検査を足す。
6. 全部の見本を、変更の前後で画素ごとに比べる（動きは止める）。壊す変更ではない。

**未決:** 族の数の上限、ページがこの族を表示するか（試すまで分からない）。
**検証:** 手順 1 を試した直後に、ページがトークンを表示するか、`tokens.css` に変数が出るかを見る。

## P5. 連続量の色の段階 / Sequential color scale

**目的:** ヒートマップや密度の図のために、量の大小を濃さで表す色の段階を持つ。
**今の扱い:** 使わない（`dataviz.md` 3 章）。
**作るときの条件（要件）:**
- 一方向に濃くなる。明るさが単調に変わり、グレースケールでも順序が分かる。
- ライト・ダーク両方で、最も薄い段が背景と区別でき、最も濃い段の上の文字が 4.5:1 になる。
- 色覚の違いで順序が崩れない。段の数は 5〜7（暫定）。
- ブランド色（`brand`）は使わない。操作の色と混ざるため。
- 値は `tokens.json` に新しい族として足す（P4 と同じ上限に注意）。

**未決:** 何色を土台にするか、段の数、分岐する（正負の）段が要るか。
**検証:** グレースケールの順序、両テーマの比、色覚のシミュレーション。
