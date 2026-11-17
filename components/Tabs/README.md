同じ階層の内容を切り替える。タブの並びは 2〜6 個まで。ページ遷移にはリンクを使う。
*Switch between peer content. Two to six tabs. Use links for page navigation.*

利用側が渡すもの: `items`（`{value, label, content}`）、`label`（タブ一覧の名前）、`defaultValue` または `value`、`onChange`。
*Consumer provides: `items`, `label`, `defaultValue` or `value`, `onChange`.*

- 左右の矢印キーで移動し、Home と End で先頭と末尾へ。Tab キーは選択中のタブにだけ止まる（W3C APG の方式）。選ぶとすぐ内容が切り替わる。
  *Left/Right move between tabs, Home/End jump to ends; Tab stops only on the selected tab (W3C APG). Selecting shows the panel immediately.*
- 選択中は文字の濃さと下線の両方で示す。高さはスマホ 44px・PC 32px。
  *Selected is shown by text weight and an underline. 44px on touch, 32px on PC.*
