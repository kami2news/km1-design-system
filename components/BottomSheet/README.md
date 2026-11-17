狭い画面で、今の画面を保ったまま、補助の情報や選択肢を下から出す。モーダル（`modal`、既定）と持続型（`persistent`）がある。M1 の Bottom sheets を KM1 に合わせたもの。
*On narrow screens, shows extra info or choices from the bottom while keeping context. Modal (default) and persistent variants; adapts M1 Bottom sheets.*

## 使う条件 / When to use

- モーダル: スマホで、並び順・共有先・絞り込みのように、短い選択肢をその場で選ぶとき。利用者の操作でだけ開く（M1）。
  *Modal: short choices on phones (sort, share, filter); only opened by a user action.*
- 持続型: 地図の場所の詳しい情報や再生中の操作のように、画面と並べて見続けるもの。
  *Persistent: content that stays alongside the screen (place details on a map, playback).*
- 使わない: 長い入力や申し込み（別画面・`StepFlow`）、押した場所の近くに出すべき操作（PC では `Menu`・`Popover`）、取り消せない操作の確認（`Dialog`）。
  *Not for long forms, actions that belong next to the trigger on PC, or destructive confirmations.*

## 動き / Behavior

- モーダル: 画面の下から開き、背景を暗くして操作を止める（ネイティブの `dialog` の `showModal`）。高さは中身に合わせ、最大で画面の 60%。中身が長いときはシートの中でスクロール。
  *Opens from the bottom with a scrim, blocking the page (`dialog.showModal`); height fits content up to 60% of the screen; scrolls inside.*
- 閉じ方: ×、Esc、背景を押す、Android の戻る。開いたボタンへフォーカスが戻る。
  *Closes with ×, Esc, scrim tap or Android Back; focus returns to the opener.*
- 引っ張って広げる・閉じる操作には頼らない。必ず「全画面に広げる」と × を置く（WCAG 2.5.7 ドラッグ操作）。KM1 では引っ張る操作を実装していない。
  *No drag gestures are required or implemented: "全画面に広げる" and × buttons are always present (WCAG 2.5.7).*
- 640px 以上では、中央のダイアログとして開く（M1 も大きな画面では別の形を勧めている）。
  *At 640px and up it opens as a centered dialog, as M1 also recommends alternatives on large screens.*
- 持続型: `section` として画面の一部に置き、背景の操作を止めない。たたむ・開くボタン（`aria-expanded`）を持つ。
  *Persistent: a `section` in the layout that doesn't block the page, with a collapse button.*
- 端末の安全領域（`env(safe-area-inset-bottom)`）と、キーボードが出たときの高さ（`dvh`）に合わせる。下部のタブ（`Nav`）より上の重なり順（`layer-overlay`）に置く。
  *Respects safe areas and keyboard height (`dvh`), and sits above bottom navigation.*

## キーボード・読み上げ / Keyboard and screen readers

見出し（`h2`）で名前を付ける。モーダルの間、フォーカスは中に閉じ込められる（ネイティブの `dialog`）。最初のフォーカスは「全画面に広げる」か ×。
*Named by its `h2`; focus is trapped while modal (native dialog).*

## トークン / Tokens

上の角だけ `radius-xl`（8px）、`shadow-28`、`stroke`、背景の幕 `rgba(0,0,0,.4)`、出るときは `duration-normal` で 8px 上がる（動きを減らす設定では動かない）。
*`radius-xl` top corners, `shadow-28`, scrim, 8px rise over `duration-normal` (none with reduced motion).*

## API

```jsx
<BottomSheet open={open} onClose={() => setOpen(false)} title="並び順"
  actions={<><Button onClick={close}>キャンセル</Button><Button appearance="primary" onClick={apply}>適用</Button></>}>
  <RadioGroup legend="予定の並び順" … />
</BottomSheet>
<BottomSheet variant="persistent" title="選んだ場所：W9 棟">…</BottomSheet>
```

`open`、`onClose`、`title`、`children`、`actions`、`variant`（`modal`・`persistent`）、`expandable`、`defaultCollapsed`。
Flutter: `showKm1BottomSheet(context:, title:, builder:, actions:)`。スマホは `showModalBottomSheet`（`showDragHandle: false`、閉じるボタンつき、最大 60%）、640 以上は `Dialog`。

## してはいけないこと / Don't

- 開いたとたんに出す（利用者が押していないのに出す）。 *Open it without a user action.*
- メニューの代わりに、押した場所から遠いシートに操作を並べる（PC）。 *Use it on PC for actions that belong next to the trigger.*
- 閉じる手段を引っ張る操作だけにする。 *Make dragging the only way to close or expand.*

## テスト / Tests

モーダルで開く、名前、フォーカスが中へ、広げるボタン（狭い画面）、全画面、Esc で閉じる、開いたボタンへフォーカスが戻る、持続型は section、たためる（320・360px で 9 項目、1024・1366px で 8 項目合格）。
*All checks pass at 320/360px (9) and 1024/1366px (8).*
