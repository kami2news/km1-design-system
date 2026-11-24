状態や件数を示す小さなラベル。丸型（`radius-circular`）。
*A small label for status or counts, pill-shaped (`radius-circular`).*

**理由 / Why:** 押せない印なので丸にし、角丸の押せる部品（ボタン・Chip）と形で見分けられるようにする（D19）。小さいので、状態は色だけでなく文字で書く。
*It cannot be pressed, so it is round, telling it apart by shape from pressable parts with rounded corners (D19). Being small, it states the status in words, not colour alone.*

利用側が渡すもの: `children`（短い文言）。`appearance` は `brand`、`subtle`、`success` / `warning` / `danger`、`outline`。
*Consumer provides: `children` (short text). `appearance`: `brand`, `subtle`, `success` / `warning` / `danger`, `outline`.*

- 状態は必ず文言で伝える（「完了」「期限切れ」）。色だけに頼らない。
  *Always state status in words ("Done", "Overdue"); never rely on color alone.*
- 状態系の淡い背景には枠線を付け、文字は `ink`。
  *Tinted status badges carry a border and use `ink` text.*
