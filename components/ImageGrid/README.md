写真やファイルのように、見た目で見分けるものを格子に並べる。タイル全体が主操作、選択のチェックは別の押し場所。M1 の Grid lists を KM1 に合わせたもの。
*A grid for items told apart by appearance (photos, files). The tile is the primary action; the selection checkbox is a separate target. Adapts M1 Grid lists.*

## 使う条件 / When to use

- 画像が主な手がかりになる同じ種類のもの（観測写真、アルバム、ファイルの縮小画像）。
  *Same-kind items where the image is the main cue.*
- 使わない: 文字や数を読み比べる → `List`・`Table`。長さや形がまちまち → `Card`。横に流れるカルーセル（M1 も横スクロールを勧めていない）。
  *Not for text/number comparison (`List`, `Table`), mixed content (`Card`), or horizontal carousels.*

## 動き / Behavior

- 縦にだけスクロール。列の数は幅で決まる（タイルの最小幅 `minTileWidth`、既定 160px）。左上から右へ、上から下へ並ぶ。
  *Vertical scroll only; column count follows width (`minTileWidth`, 160px default); order runs left-to-right, top-to-bottom.*
- 画像は `loading="lazy"`。読み込めないとき・画像がないときは、アイコンと「画像を表示できません」「画像なし」を出し、代替テキストは読み上げに残す（M1 も代わりの画像を求めている）。
  *Lazy-loaded; failures and missing images show an icon and text, keeping the alt text for screen readers.*
- 選択: チェックはタイルの左上、44px（タッチ）・32px（PC）の押し場所。選んだタイルは `brand` の 2px の枠とチェック。選択の操作は `ContextualActionBar`。タイルごとのスワイプ操作は作らない（M1 も認めていない）。
  *Checkbox top-left with a full-size target; selected tiles get a 2px brand border and a check; actions go in ContextualActionBar; no per-tile swipe.*

## キーボード・読み上げ / Keyboard and screen readers

`ul role="list"`（名前は `label`）。タイルは button（名前は画像の代替テキストと題名）、チェックはその隣（入れ子でない）。Tab の順はチェック → タイル。矢印キーの 2 次元移動は持たない（大量に並ぶ場合は今後の課題）。
*`ul role="list"`; each tile is a button named by alt text and caption; the checkbox sits beside it; Tab goes checkbox → tile; no 2D arrow keys yet.*

## 見た目・トークン / Look and tokens

題名は画像の下に置く（M1 のように画像の上の半透明の帯に重ねない。写真によって文字のコントラストが下がるため）。すき間 `space-sm`、枠 `stroke-subtle`、`radius-md`、比率 `aspectRatio`（既定 4:3）。
*Captions go below the image, not over it, to keep contrast; `space-sm` gaps, `stroke-subtle`, `radius-md`, `aspectRatio` (4:3 default).*

## API

```jsx
<ImageGrid label="観測写真" items={[{ id: 1, src, alt: '湖と山の写真', caption: '観測地点 A', meta: '11/03' }]}
  selectable selected={s.selected} onSelectionChange={s.set} onOpen={open} />
```

`items`（`{id, src, alt, caption?, meta?}`）、`label`、`onOpen`、`selectable`・`selected`・`onSelectionChange`、`minTileWidth`、`aspectRatio`。
Flutter: `Km1ImageGrid`（`items`（`Km1ImageItem`）・`onOpen`・`selectable`・`selected`・`onSelectionChanged`・`minTileWidth`・`aspectRatio`）。

## してはいけないこと / Don't

- 代替テキストを空にする（飾りではない）。 *Leave alt text empty.*
- 題名を画像の上に重ねる。 *Overlay captions on photos.*
- 文字が主役のデータを格子にする。 *Use a grid for text-led data.*

## テスト / Tests

枚数、代替テキスト、遅延読み込み、読み込み失敗の表示、チェックが入れ子でない、選択の表示、選択がバーに反映、列数、横スクロールなし（9 項目、320〜1366px・ダークで合格）。
*9 checks pass at 320–1366px and dark.*
