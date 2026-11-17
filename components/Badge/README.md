状態や件数を示す小さなラベル。丸型（`radius-circular`）。
*A small label for status or counts, pill-shaped (`radius-circular`).*

利用側が渡すもの: `children`（短い文言）。`appearance` は `brand`、`subtle`、`success` / `warning` / `danger`、`outline`。
*Consumer provides: `children` (short text). `appearance`: `brand`, `subtle`, `success` / `warning` / `danger`, `outline`.*

- 状態は必ず文言で伝える（「完了」「期限切れ」）。色だけに頼らない。
  *Always state status in words ("Done", "Overdue"); never rely on color alone.*
- 状態系の淡い背景には枠線を付け、文字は `ink`。
  *Tinted status badges carry a border and use `ink` text.*
