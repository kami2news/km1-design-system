# グラフとデータの見せ方 / Charts and data

KM1-VIZ-001。状態は**提案**（試行前）。グラフの部品はまだなく、どのライブラリで描いても（Web は SVG・D3 など、Flutter は `CustomPainter`、PDF・Office の図も）、この章の規則に従う。数値のうち「暫定」と書いたものは、実際のグラフで試して確かめるまで仮の値。
*KM1-VIZ-001. Status: **proposal** (not yet trialled). There is no chart component yet; whatever draws the chart (SVG/D3, Flutter `CustomPainter`, figures in PDF and Office) follows these rules. Values marked provisional are placeholders until tried on real charts.*

色・模様は既存の決まり（「画面の組み立て › 分類色」の色 × 模様 KM1-COL-001）をそのまま使う。新しい色やトークンは足さない。
*Color and pattern reuse the existing rules (Patterns › Category colors, KM1-COL-001). No new colors or tokens.*

## 1. 必須の規則 / Musts

| # | 規則 / Rule | 確かめ方 / Check |
|---|---|---|
| M1 | **色だけで系列を区別しない。** 棒・面は模様（8 種、間隔 8px、線 3px）で、折れ線は線の種類（実線・破線・点線・一点鎖線）と点の形（丸・四角・三角・ひし形）で区別する | グレースケールにして見分けられる |
| M2 | **系列の名前を文字で読めるようにする。** 系列が 2 つ以上なら、凡例（`CategoryLegend`）か、線の端の直接ラベルを必ず付ける | 名前を読める場所がある |
| M3 | **表を付ける。** すべてのグラフに、同じ数値の表（`Table`）を「表で見る」の切り替えか、グラフの下の `Accordion` で付ける。グラフ本体は `role="img"` と、要約の `aria-label`（「過去 14 日の降水量。最大は 11/10 の 24 mm」）を持つ | 読み上げで要約が読まれ、表で全部の値に届く |
| M4 | **文字は 12px 以上。** 目盛・凡例・注記は `ink-secondary` 以上の濃さ（白地で 4.5:1）。数値は `tabular-nums` | 最小の文字を測る |
| M5 | **棒と面は 0 から始める。** 折れ線は 0 から始めなくてよいが、始めていないことをグラフの中に書く（例「縦軸は 40 から」） | 縦軸の起点 |
| M6 | **マークと背景の比を 3:1 にそろえる。** 分類色だけでは `surface` との比が 3:1 に満たないものがある（「分類色」）。棒・面・点には 1px の `stroke-strong` の縁を付け、縁で 3:1 を満たす。線は 2px 以上で、3:1 に満たない色の線は、点の形と直接ラベルで補う | 縁と背景の比を計算する |
| M7 | **操作できるグラフはキーボードでも使える。** 値を出す動き（ホバー）は、フォーカスでも出る。データ点・棒の押せる範囲は、PC で 24px、タッチで 44px（見た目は変えず、押せる範囲だけ広げる）。隣と重ねない | Tab とタッチで全部の点に届く |
| M8 | **ライトとダークの両方で読める。** 強制カラーでは、模様と縁を `CanvasText` で描く | 両テーマと強制カラーで確認 |

## 2. 原則 / Defaults

理由を書けば外してよい（`product.md` の原則と同じ扱い）。
*May be broken with a written reason, as with the defaults in `product.md`.*

### 2.1 形の選び方 / Which form

| 見せたいこと / To show | 使う形 / Form |
|---|---|
| 項目どうしの大小の比較 | 棒グラフ。項目名が長い・多いときは横棒 |
| 時間の変化 | 折れ線グラフ。点が少なければ点を打つ |
| 内訳 | 100% の積み上げ棒、または表 |
| 分布 | ヒストグラム |
| 2 つの量の関係 | 散布図 |
| 正確な値 | 表（グラフにしない） |

使わない: 円グラフ・ドーナツ・レーダー（角度や面積は比べにくい）、3D、影、グラデーションの塗り、異なる単位を 1 枚に重ねる二重軸（別の小さなグラフに分ける）。
*Not used: pie, donut, radar, 3D, shadows, gradient fills, dual axes (split into small multiples).*

### 2.2 軸・目盛・線 / Axes, ticks and lines

- 目盛線は横方向だけ、`stroke-subtle` の 1px、6 本まで。軸線は `stroke`。
  *Horizontal gridlines only, `stroke-subtle` 1px, at most six; axis lines use `stroke`.*
- 目盛は区切りのよい値（0・10・20 など）。数値の桁区切りと小数の桁数をそろえ、単位は軸のタイトルか数値の後ろに書く。
  *Round ticks; consistent separators and decimals; units in the axis title or after the value.*
- 折れ線は 2px、点は 8px（暫定）。線の種類の間隔は破線 6px・2px、点線 1.5px・3px、一点鎖線 8px・3px・1.5px・3px（暫定）。
  *Lines 2px, markers 8px, dash patterns as listed (provisional).*

### 2.3 凡例・ラベル・値 / Legend, labels and values

- 折れ線は、線の右端に系列名を直接書くのを優先する。置けないときは凡例を上か右に置く。
  *Prefer direct labels at line ends; otherwise a legend above or to the right.*
- 棒は、項目が 12 個以内なら端に値を書く。
  *Show values at bar ends when there are 12 items or fewer.*
- 系列は 1 つのグラフに 6 つまで（暫定）。それを超えるときは、絞り込みか、小さなグラフを並べる。
  *At most six series per chart (provisional); beyond that filter or use small multiples.*
- 同じ分類は、どのグラフでも同じ色 × 模様にする。割り当ては `categoryStyle(i)`（Flutter は `km1CategoryStyleAt(i)`）の順。
  *The same category keeps the same color × pattern in every chart; assign with `categoryStyle(i)`.*

### 2.4 題名と注記 / Titles and notes

- 題名は「何を、いつ、単位」を 1 文で（例「降水量（mm）、2026/11/01〜11/14」）。見出しの段は飛ばさない。
  *Title says what, when and the unit in one sentence; keep heading order.*
- 日付は「日付と時刻の書き方」に従う。
  *Dates follow "Dates and times".*

### 2.5 大きさ・状態 / Size and states

- 高さは PC で 240px 以上、スマホで 200px 以上（暫定）。幅 320px で横にはみ出さない。はみ出すなら、表と同じく枠の中で横にスクロールする。
  *Height 240px on PC and 200px on phones (provisional); no horizontal overflow at 320px — scroll inside the frame like tables.*
- 空・読み込み中・失敗は `EmptyState`・`Skeleton`・`Alert` で出し、グラフの形を保つ（6 つの状態は `product.md`）。10 秒以上かかる集計は、待ち時間の規則に従う。
  *Empty, loading and failure use `EmptyState`, `Skeleton` and `Alert`; waits of 10 seconds or more follow the waiting rules.*

### 2.6 印刷・PDF・Office / Print, PDF and Office

- 白黒で印刷しても系列を区別できること（M1 を印刷で確かめる）。PDF の図は `<figure role="group">` に代替テキストと説明を付ける（`documents.md`）。
  *Series must stay distinguishable in grayscale print; PDF figures follow `documents.md`.*
- 見本や図の大きさは KM1 で決めた寸法に準拠させる。
  *Sizes follow KM1's defined dimensions.*

## 3. 連続量の色の段階 / Sequential color scales

ヒートマップのような、量を色の濃さで表す図は**使わない**。KM1 には連続量のための色の段階がまだなく、`cat-*` は分類のための色で、濃さの順序を表せないため。必要になったら `proposals.md` の P5 から進める。
*Heatmap-style charts are not used: KM1 has no sequential color scale and `cat-*` colors are categorical. Start from P5 in `proposals.md` if one is needed.*

## 4. 実装 / Implementation

| 対象 | 使うもの |
|---|---|
| Web | SVG。凡例は `CategoryLegend`、模様は `f2-pat--lg`（間隔 8px、線 3px）、表は `Table` |
| Flutter | `CustomPainter` と `Km1PatternPainter(pitch: 8)`、凡例は `Km1CategoryLegend` |
| PDF・Office | 図は画像にして、代替テキストを付ける。色 × 模様は同じ |

グラフ専用の部品（`Chart`）は `proposals.md` の P3。
*A dedicated `Chart` component is P3 in `proposals.md`.*

## 5. 点検 / Checklist

- [ ] グレースケールで全系列を見分けられる（M1）
- [ ] 系列名を文字で読める（M2）
- [ ] 要約の `aria-label` があり、表で全部の値に届く（M3）
- [ ] いちばん小さい文字が 12px 以上、文字は白地で 4.5:1 以上（M4）
- [ ] 棒・面の起点が 0、または起点を明記している（M5）
- [ ] 縁と背景の比が 3:1 以上（M6）
- [ ] キーボードとタッチで全部の点に届く（M7）
- [ ] ライト・ダーク・強制カラーで読める（M8）
- [ ] 320px で横にはみ出さない
- [ ] 同じ分類が全グラフで同じ色 × 模様
