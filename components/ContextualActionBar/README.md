選んだ対象にだけ効く操作をまとめたバー。選んでいる間だけ件数と操作が出る。`List`・`ImageGrid`・`Table` で共通（`Table` の一括操作もこの部品で描く）。選択の状態は `useSelection` で持てる。
*A bar of actions that apply only to the selection; the count and actions appear while something is selected. Shared by `List`, `ImageGrid` and `Table` (Table's bulk actions now render through it). `useSelection` holds the state.*

## 使う条件 / When to use

- 複数の対象を選んで、まとめて移動・削除・ダウンロードするとき。
  *Acting on several selected items at once.*
- 使わない: いつも使う操作 → `Toolbar`。1 件だけに効く操作 → その行の補助操作か、開いた先の画面。
  *Not for always-available actions (`Toolbar`) or single-item actions (row action or detail view).*

## 動き / Behavior

- 0 件: 操作は出さず、件数の読み上げ欄（`role="status"`）だけ残す。1 件以上: 「3 件を選択中（全 12 件）」、操作、必要なら「すべて選択」、「選択を解除」。
  *At 0 only the live count region remains; otherwise the count, actions, optional "select all" and "clear".*
- 「選択を解除」のあと、フォーカスはバーに残る（消えたボタンと一緒にフォーカスが失われない。WCAG 2.4.3）。
  *After "clear", focus stays on the bar instead of being lost.*
- 取り消せない操作（削除）は `danger: true`。押したら `Dialog` で「3 件を削除しますか」と件数と対象を示して確認する。元に戻せる操作（移動・アーカイブ）は確認せず、`Toast` の「元に戻す」で取り消せるようにする。
  *Irreversible actions use `danger` and confirm in a Dialog with the count; reversible ones skip confirmation and offer Undo in a Toast.*
- 選択はページ移動・並べ替え・絞り込みのあとも保つ。絞り込みで見えなくなった選択がある場合は「3 件を選択中（うち 1 件は非表示）」のように利用側で伝える。画面の幅が変わっても選択は消さない。
  *Keep the selection across paging, sorting and filtering; tell users when some selected items are filtered out; resizing never clears it.*

## キーボード・読み上げ / Keyboard and screen readers

件数は `role="status"` で読み上げる。操作は普通のボタンが並ぶ `role="group"`（名前「選択した項目の操作」）。`toolbar` の役割は使わない（矢印キーの移動を持たないため）。
*The count is announced; actions sit in a named `role="group"` of ordinary buttons (no `toolbar` role, since there's no arrow-key navigation).*

## 見た目・トークン / Look and tokens

`brand-tint` の背景（枠は付けない。面と件数の文字で足りる。D34）、`radius-md`、文字は `body-1-strong`。操作の高さは `--control-height`（PC 32px・タッチ 44px）。`sticky` で一覧の上に留める。
*`brand-tint` fill (no border; the tint and the count are enough, D34), `radius-md`, `body-1-strong`; controls follow `--control-height`; `sticky` pins it above the list.*

## 幅 / Responsive

操作は折り返す。スマホで操作が 3 つを超えるときは、よく使う 2 つを残して残りを `Menu`（「その他の操作」）に入れる。主な操作をすべて隠さない。
*Actions wrap; on phones with more than three, keep two and move the rest into a "More" `Menu`; never hide all of them.*

## API

```jsx
const s = useSelection();
<ContextualActionBar count={s.count} total={items.length} onSelectAll={() => s.selectAll(ids)} onClear={s.clear}
  actions={[{ label: '移動', onClick: move }, { label: '削除', danger: true, onClick: confirmDelete }]} />
<List selectable selected={s.selected} onSelectionChange={s.set}>…</List>
```

`ContextualActionBar`: `count`、`actions`（`{label, onClick, icon?, danger?}`）、`onClear`、`total`・`onSelectAll`、`label`、`sticky`。`useSelection(initial?)`: `selected`・`count`・`isSelected`・`toggle`・`set`・`clear`・`selectAll`。
Flutter: `Km1ContextualActionBar`（`count`・`total`・`actions`（`Km1BulkAction`）・`onClear`・`onSelectAll`）。

## してはいけないこと / Don't

- 選んでいないのに操作を並べたままにする。 *Show selection actions with nothing selected.*
- 操作をアイコンだけにする。 *Use icon-only actions.*
- 削除をいきなり実行する。 *Delete without confirmation.*

## テスト / Tests

件数の表示と `role="status"`、選択行の表示、チェックの名前、選択の追加、すべて選択、解除で操作が消える、解除後のフォーカス（8 項目、320〜1366px・ダークで合格）。`Table` の一括操作は同じ部品で描くようにしたあと、axe の回帰検査で確認。
*8 checks pass; Table's bulk bar re-tested via axe regression after the refactor.*

**理由 / Why:** 選んだものだけに効く操作を出したい。選んでいる間だけ出て、件数で何に効くか分かる。
*Actions that apply only to the selection: shown only while selecting, with a count saying what they affect.*
