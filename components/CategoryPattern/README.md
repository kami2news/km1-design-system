分類を**色 × 模様**で区別するための部品。`cat-*` の 18 色に 8 つの模様（塗り・横線・縦線・斜線・格子・斜め格子・点・市松）を組み合わせ、144 通りにする。色が見分けにくい人や白黒の印刷でも、模様で区別できる（WCAG 1.4.1）。
*Distinguish categories by **color × pattern**: 18 `cat-*` colors and 8 patterns (solid, horizontal, vertical, diagonal, grid, crosshatch, dots, checker) give 144 combinations that stay distinct for color-blind readers and in grayscale print (WCAG 1.4.1).*

利用側が渡すもの: `CategoryMark` は `color`（`cat-*` の名前）・`pattern`・`size`（`sm` 16px／`md` 20px）・`label`（しるしだけで意味を持つときだけ）。`CategoryLegend` は `items`（`label`・`color`・`pattern`）と `label`（凡例の名前）。`categoryStyle(i)` は i 番目の分類の既定の色と模様を返す。`Timetable` と `TimeGrid` の項目にも `pattern` を渡せる（題名の前にしるしが出る）。
*Consumer provides: `CategoryMark` takes `color`, `pattern`, `size` (`sm` 16px / `md` 20px) and `label` (only when the mark stands alone). `CategoryLegend` takes `items` and `label`. `categoryStyle(i)` returns the default color and pattern for the i-th category. `Timetable` and `TimeGrid` items accept `pattern` too.*

## 使い方 / Usage

- 模様は**文字の下に描かない**。使うのは、分類のしるし（16px・20px）、凡例、グラフの棒や面の塗り（模様の間隔 8px）だけ。予定のブロックなど文字が載る面は、これまでどおり淡い塗りと 4px の帯で、模様はしるしで添える。
  *Never draw patterns under text: only in marks (16/20px), legends and chart fills (8px pitch). Text surfaces keep the tint and 4px bar, with the pattern shown by a mark.*
- 利用者が選ばないときは `categoryStyle(i)` の順に割り当てる。隣り合う分類で色の明るさと模様が両方変わる順になっている（青→マリーゴールド→ティール→パンプキン…、模様は 8 つを順に）。18 と 8 の組み合わせで 72 個目まで重ならない。
  *Without a user choice, assign in `categoryStyle(i)` order: neighbours differ in lightness and pattern; no repeats for the first 72.*
- 1 つの画面に出す分類は 12 個までを目安にする。それより多いと、色と模様があっても凡例との照らし合わせがつらくなる。
  *Aim for at most 12 categories on one screen.*
- しるしには必ず分類名の文字を添える（凡例・詳細・読み上げ）。しるしの横に名前があるときは `label` を付けない（同じことを 2 度読ませない）。
  *Always pair marks with the category name; omit `label` when the name is next to the mark.*
- 「仮の予定」は、ブロック全体の 135° の斜線で表す（状態の描き分け）。分類の模様の「斜線」は向きが逆（右下がり）で、しるしの中だけに出るので混ざらない。
  *Tentative events keep the full-block 135° hatch (a state); the category diagonal runs the other way and only inside marks.*
- しるしの枠は `stroke-strong`（背景と 3:1 以上）。ハイコントラスト（forced colors）では色を捨てて `CanvasText` の模様だけで描く。印刷では背景を印刷させる。
  *Mark borders use `stroke-strong`; in forced colors the pattern is drawn in `CanvasText`; print forces background printing.*

## 他の環境 / Other platforms

- Flutter: `Km1Pattern`、`Km1CategoryMark`、`Km1CategoryLegend`、`Km1Category.styleAt(i)`。
- PowerPoint・Word・Excel: 図形とグラフの系列の「塗りつぶし › パターン」で、塗り＝塗りつぶし（単色）、横線＝`dkHorz`（横線: 太）、縦線＝`dkVert`（縦線: 太）、斜線＝`wdDnDiag`（右下がり対角線: 太）、格子＝`smGrid`（格子: 小）、斜め格子＝`diagCross`（斜め格子）、点＝`dotGrid`（点線: 格子）、市松＝`lgCheck`（市松模様: 大）。前景色に分類の色、背景色に白を選ぶ。
  *Office: use Format › Fill › Pattern with the presets above, foreground = category color, background = white.*
