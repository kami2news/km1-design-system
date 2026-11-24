// KM1 km1_widgets.dart — Flutter 標準に近いものが無い KM1 の部品。
// KM1 components that have no close Flutter equivalent.
//
// 前提 / Requires: Flutter 3.27 以降、km1_theme.dart、km1_icons_b.dart、km1_icons.dart と pubspec に KM1Icons.ttf（fonts の family: KM1Icons）。
// Flutter 3.27+, km1_theme.dart, km1_icons_b.dart, km1_icons.dart, and KM1Icons.ttf declared in pubspec (family KM1Icons).
//
// 部品 / Widgets:
//   Km1EmptyState, Km1Progress, Km1Skeleton, Km1FilterChip, Km1Breadcrumb,
//   Km1Pagination, Km1Table, Km1Calendar, Km1Timetable, Km1FileList, Km1Avatar, Km1TimeGrid,
//   Km1TagPicker, Km1SortableList,
//   Km1Form, Km1FormGroup, Km1FormGrid, Km1FullSpan, Km1ConditionalField, Km1ErrorSummary, Km1FormActions,
//   Km1ListItem, Km1ListSectionHeader, Km1ContextualActionBar, Km1ExpansionEditor, Km1StepFlow,
//   showKm1BottomSheet, Km1ImageGrid, Km1CategoryMark, Km1CategoryLegend
//
// Km1TimeGrid は親で高さを決めて使う（SizedBox や Expanded の中）。
// Km1TimeGrid needs a bounded height from its parent (SizedBox, Expanded).
//
// どの部品も、色は Km1Colors、文字は Km1Text、高さは Km1Theme.targetFor() に従う。
// Every widget takes colors from Km1Colors, text from Km1Text and height from Km1Theme.targetFor().

import 'package:flutter/foundation.dart' show defaultTargetPlatform;
import 'package:flutter/material.dart';
import 'package:flutter/semantics.dart';
import 'package:flutter/services.dart';
import 'km1_icons.dart';
import 'km1_icons_b.dart';

import 'km1_theme.dart';

/// テーマから KM1 の色と高さを取る / KM1 colors and control height from the theme
extension Km1Context on BuildContext {
  Km1Colors get km1 => Theme.of(this).extension<Km1Colors>() ?? Km1Colors.light;

  /// 端末ごとの部品の高さ / Control height for this platform
  double get km1Target => Km1Theme.targetFor(defaultTargetPlatform);

  bool get km1ReduceMotion => MediaQuery.disableAnimationsOf(this);
}

// ---------------------------------------------------------------------------
// EmptyState — まだ何も無い場所の案内 / Guidance for an empty place
// ---------------------------------------------------------------------------

class Km1EmptyState extends StatelessWidget {
  const Km1EmptyState({
    super.key,
    required this.title,
    this.body,
    this.icon,
    this.bIcon,
    this.action,
  });

  /// 何が無いかを事実で書く（「今日の予定はありません」）/ State what is missing
  final String title;

  /// 次に何があるか・どうすれば入るかを本物の内容で（「明日は 9:00 から気象学です」）/ The real next step
  final String? body;

  /// アイコンは既定で付けない。見出しがなく文だけでは何の場所か分かりにくいときだけ 32px を 1 つ
  /// No icon by default; one 32px icon only when the words alone leave the place unclear.
  final IconData? icon;
  final Km1BIconName? bIcon;

  /// 最初の一歩になる操作を 1 つだけ / Exactly one first-step action
  final Widget? action;

  // 理由: 一覧が入るはずの位置で、一覧と同じ左の線から読ませる。真ん中に大きなアイコンを置く型は使わない
  // Why: read from the same left edge as the list it replaces; the centred big-icon template is not used.
  @override
  Widget build(BuildContext context) {
    final c = context.km1;
    final mark = icon != null
        ? Icon(icon, size: Km1Size.iconXl, color: c.inkSecondary)
        : (bIcon != null ? Km1BIcon(bIcon!, size: Km1Size.iconXl) : null);
    return Align(
      alignment: AlignmentDirectional.topStart,
      child: ConstrainedBox(
        constraints: const BoxConstraints(maxWidth: 560),
        child: Padding(
          padding: const EdgeInsets.symmetric(vertical: Km1Space.lg),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              if (mark != null) ...[ExcludeSemantics(child: mark), const SizedBox(height: Km1Space.sm)],
              Semantics(
                header: true,
                child: Text(title, style: Km1Text.subtitle1.copyWith(color: c.ink)),
              ),
              if (body != null) ...[
                const SizedBox(height: Km1Space.xs),
                Text(body!, style: Km1Text.body1.copyWith(color: c.ink)),
              ],
              if (action != null) ...[
                const SizedBox(height: Km1Space.md),
                action!,
              ],
            ],
          ),
        ),
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// Progress — 10 秒以上の処理は工程と時間の見込みを必ず出す
// Work of 10s or more always shows steps and a time estimate
// ---------------------------------------------------------------------------

/// 「残り約 30 秒」などに丸める / Rounds time left the KM1 way
String km1FormatRemaining(Duration d) {
  final sec = d.inSeconds;
  if (sec <= 0) return '残りわずか';
  final s5 = ((sec + 4) ~/ 5) * 5;
  if (s5 < 60) return '残り約 $s5 秒';
  final m = (sec + 59) ~/ 60;
  if (m < 60) return '残り約 $m 分';
  return '残り約 ${(sec / 3600).toStringAsFixed(1)} 時間';
}

/// 「1 分 20 秒経過」/ Elapsed time
String km1FormatElapsed(Duration d) {
  final m = d.inMinutes;
  final s = d.inSeconds % 60;
  if (m == 0) return '$s 秒経過';
  if (s == 0) return '$m 分経過';
  return '$m 分 $s 秒経過';
}

class Km1Progress extends StatelessWidget {
  const Km1Progress({
    super.key,
    required this.label,
    this.value,
    this.steps,
    this.step = 0,
    this.remaining,
    this.estimating = false,
    this.elapsed,
    this.valueText,
    this.overdue = false,
    this.onCancel,
  });

  final String label;

  /// 0.0〜1.0。null で終わりの分からない表示 / 0–1; null for indeterminate
  final double? value;

  /// 工程の名前（3〜7 個、利用者の言葉で）/ Step names, in the user's words
  final List<String>? steps;
  final int step;

  /// 見積もれるときの残り時間 / Time left when it can be estimated
  final Duration? remaining;

  /// 出し始めで、まだ残り時間を計算できない / Still estimating
  final bool estimating;

  /// 見積もれないときの経過時間（理由は valueText に）/ Elapsed time when it cannot be estimated
  final Duration? elapsed;
  final String? valueText;

  /// 見込みを超えた / Past the estimate
  final bool overdue;
  final VoidCallback? onCancel;

  String _summary() {
    final parts = <String>[];
    final s = steps;
    if (s != null && s.isNotEmpty) parts.add('工程 ${step.clamp(0, s.length - 1) + 1} / ${s.length}');
    if (valueText != null) {
      parts.add(valueText!);
    } else if (value != null) {
      parts.add('${(value!.clamp(0.0, 1.0) * 100).round()}%');
    }
    if (overdue) {
      parts.add('予定より時間がかかっています');
    } else if (estimating) {
      parts.add('残り時間を計算中');
    } else if (remaining != null) {
      parts.add(km1FormatRemaining(remaining!));
    } else if (elapsed != null) {
      parts.add(km1FormatElapsed(elapsed!));
    }
    return parts.isEmpty ? '処理中' : parts.join('・');
  }

  @override
  Widget build(BuildContext context) {
    final c = context.km1;
    final summary = _summary();
    final s = steps;
    final current = s == null || s.isEmpty ? -1 : step.clamp(0, s.length - 1);
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      mainAxisSize: MainAxisSize.min,
      children: [
        Text(label, style: Km1Text.body1Strong.copyWith(color: c.ink)),
        Text(summary, style: Km1Text.body1.copyWith(color: c.inkSecondary, fontFeatures: const [FontFeature.tabularFigures()])),
        const SizedBox(height: Km1Space.xs),
        Semantics(
          label: label,
          value: summary,
          child: ExcludeSemantics(
            child: Container(
              height: 8,
              decoration: BoxDecoration(
                border: Border.all(color: c.strokeStrong),
                borderRadius: BorderRadius.circular(Km1Radius.circular),
              ),
              clipBehavior: Clip.antiAlias,
              child: LinearProgressIndicator(
                value: value?.clamp(0.0, 1.0),
                minHeight: 8,
                backgroundColor: c.surface,
                color: c.brandStroke,
              ),
            ),
          ),
        ),
        if (s != null && s.isNotEmpty) ...[
          const SizedBox(height: Km1Space.xs),
          for (var i = 0; i < s.length; i++)
            _Km1Step(label: s[i], state: i < current ? _StepState.done : (i == current ? _StepState.current : _StepState.todo)),
          // 工程が変わったことを読み上げる / Announce step changes
          Semantics(liveRegion: true, child: ExcludeSemantics(child: SizedBox(height: 0, child: Text(s[current])))),
        ],
        if (onCancel != null) ...[
          const SizedBox(height: Km1Space.sm),
          Align(alignment: Alignment.centerLeft, child: OutlinedButton(onPressed: onCancel, child: const Text('キャンセル'))),
        ],
      ],
    );
  }
}

enum _StepState { done, current, todo }

class _Km1Step extends StatelessWidget {
  const _Km1Step({required this.label, required this.state});
  final String label;
  final _StepState state;

  @override
  Widget build(BuildContext context) {
    final c = context.km1;
    final suffix = switch (state) { _StepState.done => '（完了）', _StepState.current => '（実行中）', _StepState.todo => '（未着手）' };
    return Semantics(
      label: '$label$suffix',
      child: ExcludeSemantics(
        child: Padding(
          padding: const EdgeInsets.symmetric(vertical: 2),
          child: Row(children: [
            Container(
              width: 16,
              height: 16,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: state == _StepState.done ? c.brand : Colors.transparent,
                border: Border.all(
                  color: state == _StepState.todo ? c.strokeStrong : c.brandStroke,
                  width: state == _StepState.current ? 2 : 1,
                ),
              ),
              child: state == _StepState.done ? Km1BIcon(Km1BIconName.check, size: 12, color: c.onBrand) : null,
            ),
            const SizedBox(width: Km1Space.sm),
            Expanded(
              child: Text(label,
                  style: (state == _StepState.current ? Km1Text.body1Strong : Km1Text.body1)
                      .copyWith(color: state == _StepState.todo ? c.inkSecondary : c.ink)),
            ),
          ]),
        ),
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// Skeleton — 1〜10 秒の読み込み中の仮表示 / Placeholder for 1–10s loads
// ---------------------------------------------------------------------------

enum Km1SkeletonShape { text, list, card }

class Km1Skeleton extends StatefulWidget {
  const Km1Skeleton({super.key, this.shape = Km1SkeletonShape.text, this.lines = 3, this.label = '読み込み中'});
  final Km1SkeletonShape shape;
  final int lines;
  final String label;

  @override
  State<Km1Skeleton> createState() => _Km1SkeletonState();
}

class _Km1SkeletonState extends State<Km1Skeleton> with SingleTickerProviderStateMixin {
  late final AnimationController _ctl = AnimationController(vsync: this, duration: const Duration(milliseconds: 1600));

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    if (context.km1ReduceMotion) {
      _ctl.stop();
    } else if (!_ctl.isAnimating) {
      _ctl.repeat();
    }
  }

  @override
  void dispose() {
    _ctl.dispose();
    super.dispose();
  }

  Widget _bar(Km1Colors c, {double widthFactor = 1, double height = 12, BoxShape shape = BoxShape.rectangle}) {
    return FractionallySizedBox(
      alignment: Alignment.centerLeft,
      widthFactor: widthFactor,
      child: AnimatedBuilder(
        animation: _ctl,
        builder: (context, _) {
          final t = _ctl.value;
          return Container(
            height: height,
            decoration: BoxDecoration(
              shape: shape,
              borderRadius: shape == BoxShape.circle ? null : BorderRadius.circular(Km1Radius.sm),
              gradient: LinearGradient(
                begin: Alignment(-1 + t * 3 - 1, 0),
                end: Alignment(t * 3 - 1, 0),
                colors: [c.surfacePressed, c.surfaceHover, c.surfacePressed],
              ),
            ),
          );
        },
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final c = context.km1;
    final List<Widget> children;
    switch (widget.shape) {
      case Km1SkeletonShape.card:
        children = [_bar(c, height: 120), const SizedBox(height: Km1Space.sm), _bar(c, widthFactor: .6), const SizedBox(height: Km1Space.sm), _bar(c, widthFactor: .9)];
      case Km1SkeletonShape.list:
        children = [
          for (var i = 0; i < widget.lines; i++)
            Padding(
              padding: const EdgeInsets.only(bottom: Km1Space.sm),
              child: Row(children: [
                SizedBox(width: 32, height: 32, child: _bar(c, height: 32, shape: BoxShape.circle)),
                const SizedBox(width: Km1Space.md),
                Expanded(child: _bar(c, widthFactor: (80 - (i * 12) % 40) / 100)),
              ]),
            ),
        ];
      case Km1SkeletonShape.text:
        children = [
          for (var i = 0; i < widget.lines; i++)
            Padding(padding: const EdgeInsets.only(bottom: Km1Space.sm), child: _bar(c, widthFactor: i == widget.lines - 1 ? .6 : 1)),
        ];
    }
    return Semantics(
      label: widget.label,
      liveRegion: true,
      child: ExcludeSemantics(child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, mainAxisSize: MainAxisSize.min, children: children)),
    );
  }
}

// ---------------------------------------------------------------------------
// FilterChip — 押して切り替える絞り込み / Toggle filter chip
// ---------------------------------------------------------------------------

class Km1FilterChip extends StatelessWidget {
  const Km1FilterChip({super.key, required this.label, required this.selected, required this.onSelected});
  final String label;
  final bool selected;
  final ValueChanged<bool> onSelected;

  @override
  Widget build(BuildContext context) {
    final c = context.km1;
    // 見た目は 32px、押せる範囲は端末の高さまで広げる / 32px look, platform-height hit area
    final hit = context.km1Target < 32 ? 32.0 : context.km1Target;
    return Semantics(
      button: true,
      toggled: selected,
      label: label,
      child: ExcludeSemantics(
        child: InkWell(
          onTap: () => onSelected(!selected),
          borderRadius: BorderRadius.circular(Km1Radius.circular),
          child: ConstrainedBox(
            constraints: BoxConstraints(minHeight: hit),
            child: Center(
              widthFactor: 1,
              child: AnimatedContainer(
                duration: context.km1ReduceMotion ? Duration.zero : Km1Motion.faster,
                height: 32,
                padding: const EdgeInsets.symmetric(horizontal: Km1Space.md),
                decoration: BoxDecoration(
                  color: selected ? c.brandTint : c.surface,
                  border: Border.all(color: selected ? c.brandStroke : c.strokeStrong),
                  borderRadius: BorderRadius.circular(Km1Radius.circular),
                ),
                child: Row(mainAxisSize: MainAxisSize.min, children: [
                  if (selected) ...[
                    Km1BIcon(Km1BIconName.check, size: Km1Size.iconSm, color: c.brandInk),
                    const SizedBox(width: Km1Space.xs),
                  ],
                  Text(label, style: (selected ? Km1Text.body1Strong : Km1Text.body1).copyWith(color: selected ? c.brandInk : c.ink)),
                ]),
              ),
            ),
          ),
        ),
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// Breadcrumb — 3 階層以上の画面の道しるべ / Path for three or more levels
// ---------------------------------------------------------------------------

class Km1BreadcrumbItem {
  const Km1BreadcrumbItem(this.label, {this.onTap});
  final String label;
  final VoidCallback? onTap;
}

class Km1Breadcrumb extends StatelessWidget {
  const Km1Breadcrumb({super.key, required this.items});
  final List<Km1BreadcrumbItem> items;

  @override
  Widget build(BuildContext context) {
    final c = context.km1;
    final narrow = MediaQuery.sizeOf(context).width < Km1Breakpoint.md;
    final shown = <int>[];
    for (var i = 0; i < items.length; i++) {
      final middle = i > 0 && i < items.length - 2;
      if (!(narrow && middle)) shown.add(i);
    }
    final children = <Widget>[];
    for (var k = 0; k < shown.length; k++) {
      final i = shown[k];
      final it = items[i];
      final last = i == items.length - 1;
      if (k > 0) {
        if (shown[k] - shown[k - 1] > 1) {
          children.add(ExcludeSemantics(child: Text('…', style: Km1Text.body1.copyWith(color: c.inkSecondary))));
        }
        children.add(ExcludeSemantics(child: Km1BIcon(Km1BIconName.chevronRight, size: Km1Size.iconSm, color: c.inkSecondary)));
      }
      children.add(last
          ? Semantics(
              label: '${it.label}（現在のページ）',
              child: ExcludeSemantics(
                child: Padding(
                  padding: const EdgeInsets.symmetric(horizontal: Km1Space.xs),
                  child: Text(it.label, style: Km1Text.body1Strong.copyWith(color: c.ink)),
                ),
              ),
            )
          : TextButton(
              onPressed: it.onTap,
              style: TextButton.styleFrom(foregroundColor: c.inkSecondary, padding: const EdgeInsets.symmetric(horizontal: Km1Space.xs)),
              child: Text(it.label, style: const TextStyle(decoration: TextDecoration.underline)),
            ));
    }
    return Semantics(
      container: true,
      label: 'パンくずリスト',
      child: Wrap(crossAxisAlignment: WrapCrossAlignment.center, spacing: Km1Space.xxs, children: children),
    );
  }
}

// ---------------------------------------------------------------------------
// Pagination — 長い一覧のページ送り / Paging for long lists
// ---------------------------------------------------------------------------

class Km1Pagination extends StatelessWidget {
  const Km1Pagination({super.key, required this.page, required this.count, required this.onChanged});

  /// 1 始まり / 1-based
  final int page;
  final int count;
  final ValueChanged<int> onChanged;

  List<int?> _pages(int cur, int n) {
    if (n <= 7) return [for (var i = 1; i <= n; i++) i];
    final lo = (cur - 1).clamp(2, n - 1);
    final hi = (cur + 1).clamp(2, n - 1);
    return [1, if (lo > 2) null, for (var i = lo; i <= hi; i++) i, if (hi < n - 1) null, n];
  }

  @override
  Widget build(BuildContext context) {
    final c = context.km1;
    final n = count < 1 ? 1 : count;
    final cur = page.clamp(1, n);
    final narrow = MediaQuery.sizeOf(context).width < Km1Breakpoint.md;
    final t = context.km1Target;
    Widget arrow(IconData icon, String tip, int to, bool enabled) => IconButton(
          tooltip: tip,
          onPressed: enabled ? () => onChanged(to) : null,
          icon: Icon(icon, size: Km1Size.iconSm),
        );
    return Semantics(
      container: true,
      label: 'ページ送り',
      child: Row(mainAxisSize: MainAxisSize.min, children: [
        arrow(Km1Icons.chevronLeft16, '前のページ', cur - 1, cur > 1),
        if (narrow)
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: Km1Space.sm),
            child: Text('$cur / $n', style: Km1Text.body1.copyWith(color: c.ink, fontFeatures: const [FontFeature.tabularFigures()])),
          )
        else
          for (final p in _pages(cur, n))
            if (p == null)
              ExcludeSemantics(child: SizedBox(width: Km1Space.lg, child: Text('…', textAlign: TextAlign.center, style: Km1Text.body1.copyWith(color: c.inkSecondary))))
            else
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 2),
                child: Semantics(
                  selected: p == cur,
                  button: true,
                  label: p == cur ? '$p ページ（現在）' : '$p ページ',
                  child: ExcludeSemantics(
                    child: SizedBox(
                      height: t,
                      child: TextButton(
                        onPressed: p == cur ? () {} : () => onChanged(p),
                        style: TextButton.styleFrom(
                          minimumSize: Size(t, t),
                          padding: const EdgeInsets.symmetric(horizontal: Km1Space.xs),
                          backgroundColor: p == cur ? c.brandTint : null,
                          foregroundColor: p == cur ? c.brandInk : c.ink,
                          side: p == cur ? BorderSide(color: c.brandStroke) : BorderSide.none,
                          textStyle: p == cur ? Km1Text.body1Strong : Km1Text.body1,
                        ),
                        child: Text('$p'),
                      ),
                    ),
                  ),
                ),
              ),
        arrow(Km1Icons.chevronRight16, '次のページ', cur + 1, cur < n),
      ]),
    );
  }
}

// ---------------------------------------------------------------------------
// Table — 並べ替えできる表 / Sortable table
// ---------------------------------------------------------------------------

class Km1Column<T> {
  const Km1Column({required this.label, required this.cell, this.numeric = false, this.sortable = false, this.flex = 1});
  final String label;
  final Widget Function(T row) cell;

  /// 数値の列は右寄せ / Numeric columns align right
  final bool numeric;
  final bool sortable;
  final int flex;
}

class Km1Table<T> extends StatelessWidget {
  const Km1Table({
    super.key,
    required this.caption,
    required this.columns,
    required this.rows,
    this.sortColumn,
    this.ascending = true,
    this.onSort,
    this.empty = 'データがありません',
    this.minWidth = 480,
    this.rowId,
    this.rowName,
    this.selected,
    this.onSelectionChanged,
    this.bulkActions = const [],
    this.density = Km1Density.regular,
  });

  /// 表の名前（必須）/ Table name (required)
  final String caption;
  final List<Km1Column<T>> columns;
  final List<T> rows;
  final int? sortColumn;
  final bool ascending;

  /// 並べ替えそのものは利用側で行う / Sorting itself is done by the caller
  final void Function(int column, bool ascending)? onSort;
  final String empty;

  /// これより狭いと横スクロール / Scrolls horizontally below this width
  final double minWidth;

  /// 行選択: 行の ID と読み上げ名、選んだ ID の集合、変更の通知、一括操作
  /// Row selection: row id and name, the selected set, change callback, bulk actions
  final Object Function(T row)? rowId;
  final String Function(T row)? rowName;
  final Set<Object>? selected;
  final ValueChanged<Set<Object>>? onSelectionChanged;
  final List<Km1BulkAction> bulkActions;

  /// 密度（既定 regular）。行の上下の余白と高さだけが変わる。選択のチェックと並べ替えのボタンは端末の操作領域を保つ。
  /// Density (default regular): only row padding and height change; checkboxes and sort buttons keep the platform hit area.
  final Km1Density density;

  bool get _selectable => rowId != null && selected != null && onSelectionChanged != null;

  @override
  Widget build(BuildContext context) {
    final c = context.km1;
    final h = context.km1Target;
    final sel = selected ?? const <Object>{};
    final ids = _selectable ? rows.map(rowId!).toList() : const <Object>[];
    final nSel = ids.where(sel.contains).length;
    final all = rows.isNotEmpty && nSel == rows.length;
    Widget checkCell({required bool? value, required String label, required VoidCallback onTap}) => ConstrainedBox(
          // どの密度でも、選択のチェックは端末の操作領域の高さを保つ / The checkbox keeps the platform hit area at every density
          constraints: BoxConstraints.tightFor(width: h < 44 ? 44 : h).copyWith(minHeight: h),
          child: Semantics(
            label: label,
            checked: value == true,
            mixed: value == null,
            child: ExcludeSemantics(child: Checkbox(value: value, tristate: value == null, onChanged: (_) => onTap())),
          ),
        );
    Widget cellBox(Widget child, Km1Column<T> col, {bool header = false}) => Expanded(
          flex: col.flex,
          child: Container(
            constraints: BoxConstraints(minHeight: header ? h : density.rowMinHeight(h)),
            alignment: col.numeric ? Alignment.centerRight : Alignment.centerLeft,
            padding: EdgeInsets.symmetric(horizontal: Km1Space.md, vertical: density.itemGap / 2),
            child: DefaultTextStyle.merge(
              style: (header ? Km1Text.body1Strong.copyWith(color: c.inkSecondary) : Km1Text.body1.copyWith(color: c.ink))
                  .copyWith(fontFeatures: col.numeric ? const [FontFeature.tabularFigures()] : null),
              child: child,
            ),
          ),
        );
    final header = Row(children: [
      if (_selectable)
        checkCell(
          value: all ? true : (nSel > 0 ? null : false),
          label: 'すべて選択',
          onTap: () => onSelectionChanged!(all ? <Object>{} : ids.toSet()),
        ),
      for (var i = 0; i < columns.length; i++)
        cellBox(
          columns[i].sortable && onSort != null
              ? Semantics(
                  label: '${columns[i].label}、${sortColumn == i ? (ascending ? '昇順で並べ替え済み' : '降順で並べ替え済み') : '並べ替えできます'}',
                  button: true,
                  child: ExcludeSemantics(
                    child: TextButton.icon(
                      onPressed: () => onSort!(i, sortColumn == i ? !ascending : true),
                      style: TextButton.styleFrom(foregroundColor: sortColumn == i ? c.ink : c.inkSecondary, padding: const EdgeInsets.symmetric(horizontal: Km1Space.xs)),
                      iconAlignment: IconAlignment.end,
                      icon: Icon(
                        sortColumn != i
                            ? Km1Icons.sort16
                            : (ascending ? Km1Icons.sortUp16 : Km1Icons.sortDown16),
                        size: Km1Size.iconSm,
                      ),
                      label: Text(columns[i].label),
                    ),
                  ),
                )
              : Semantics(header: true, child: Text(columns[i].label)),
          columns[i],
          header: true,
        ),
    ]);
    final body = rows.isEmpty
        ? Container(
            constraints: BoxConstraints(minHeight: h),
            alignment: Alignment.center,
            child: Text(empty, style: Km1Text.body1.copyWith(color: c.inkSecondary)),
          )
        : Column(children: [
            for (var r = 0; r < rows.length; r++)
              Container(
                decoration: BoxDecoration(border: r == rows.length - 1 ? null : Border(bottom: BorderSide(color: c.strokeSubtle))),
                color: _selectable && sel.contains(rowId!(rows[r])) ? c.brandTint : null,
                child: Row(children: [
                  if (_selectable)
                    checkCell(
                      value: sel.contains(rowId!(rows[r])),
                      label: '${rowName == null ? '${r + 1} 行目' : rowName!(rows[r])} を選択',
                      onTap: () {
                        final id = rowId!(rows[r]);
                        final n = Set<Object>.of(sel);
                        if (!n.remove(id)) n.add(id);
                        onSelectionChanged!(n);
                      },
                    ),
                  for (final col in columns) cellBox(col.cell(rows[r]), col),
                ]),
              ),
          ]);
    final bulkBar = !_selectable || nSel == 0
        ? null
        : Container(
            margin: const EdgeInsets.only(bottom: Km1Space.xs),
            padding: const EdgeInsets.symmetric(horizontal: Km1Space.sm, vertical: Km1Space.xs),
            decoration: BoxDecoration(color: c.brandTint, border: Border.all(color: c.brandStroke), borderRadius: BorderRadius.circular(Km1Radius.md)),
            child: Wrap(spacing: Km1Space.xs, runSpacing: Km1Space.xs, crossAxisAlignment: WrapCrossAlignment.center, children: [
              Semantics(liveRegion: true, child: Text('$nSel 件を選択中', style: Km1Text.body1Strong.copyWith(color: c.ink))),
              for (final a in bulkActions)
                OutlinedButton(
                  onPressed: () => a.onPressed(sel.where(ids.contains).toSet()),
                  style: a.danger ? OutlinedButton.styleFrom(foregroundColor: c.dangerInk) : null,
                  child: Text(a.label),
                ),
              TextButton(onPressed: () => onSelectionChanged!(<Object>{}), child: const Text('選択を解除')),
            ]),
          );
    return Semantics(
      container: true,
      label: caption,
      child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, mainAxisSize: MainAxisSize.min, children: [
        if (bulkBar != null) bulkBar,
        Container(
        decoration: BoxDecoration(border: Border.all(color: c.stroke), borderRadius: BorderRadius.circular(Km1Radius.md)),
        clipBehavior: Clip.antiAlias,
        child: LayoutBuilder(builder: (context, box) {
          final w = box.maxWidth < minWidth ? minWidth : box.maxWidth;
          final table = SizedBox(
            width: w,
            child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
              Padding(
                padding: const EdgeInsets.fromLTRB(Km1Space.md, Km1Space.md, Km1Space.md, Km1Space.xs),
                child: Semantics(header: true, child: Text(caption, style: Km1Text.body1Strong.copyWith(color: c.ink))),
              ),
              Container(decoration: BoxDecoration(border: Border(bottom: BorderSide(color: c.strokeStrong))), child: header),
              body,
            ]),
          );
          return box.maxWidth < minWidth ? SingleChildScrollView(scrollDirection: Axis.horizontal, child: table) : table;
        }),
      ),
      ]),
    );
  }
}

/// 一括操作 / Bulk action for selected rows
class Km1BulkAction {
  const Km1BulkAction({required this.label, required this.onPressed, this.danger = false});
  final String label;

  /// 選んだ行の ID が渡る。取り消せない操作は件数つきで確認する / Confirm irreversible actions with the count
  final void Function(Set<Object> ids) onPressed;
  final bool danger;
}

// ---------------------------------------------------------------------------
// Calendar — 月の表から日付を 1 つ選ぶ / Pick one date from a month grid
// ---------------------------------------------------------------------------

const List<String> _km1Weekdays = ['日', '月', '火', '水', '木', '金', '土'];

DateTime _day(DateTime d) => DateTime(d.year, d.month, d.day);

class Km1Calendar extends StatefulWidget {
  const Km1Calendar({
    super.key,
    this.value,
    required this.onChanged,
    this.marks = const {},
    this.firstDate,
    this.lastDate,
    this.weekStart = DateTime.sunday,
    this.today,
    this.label,
  });

  final DateTime? value;
  final ValueChanged<DateTime> onChanged;

  /// 日付ごとの予定の件数（時刻は無視）/ Event counts per day (time ignored)
  final Map<DateTime, int> marks;
  final DateTime? firstDate;
  final DateTime? lastDate;

  /// DateTime.sunday か DateTime.monday / Sunday or Monday
  final int weekStart;
  final DateTime? today;
  final String? label;

  @override
  State<Km1Calendar> createState() => _Km1CalendarState();
}

class _Km1CalendarState extends State<Km1Calendar> {
  late DateTime _focus = _day(widget.value ?? widget.today ?? DateTime.now());
  final Map<DateTime, FocusNode> _nodes = {};
  bool _moveFocus = false;

  @override
  void dispose() {
    for (final n in _nodes.values) {
      n.dispose();
    }
    super.dispose();
  }

  FocusNode _node(DateTime d) => _nodes.putIfAbsent(d, () => FocusNode());

  bool _out(DateTime d) =>
      (widget.firstDate != null && d.isBefore(_day(widget.firstDate!))) || (widget.lastDate != null && d.isAfter(_day(widget.lastDate!)));

  void _go(DateTime d, {bool focus = true}) {
    if (_out(d)) return;
    setState(() {
      _focus = d;
      _moveFocus = focus;
    });
  }

  DateTime _shiftMonth(int n) {
    final first = DateTime(_focus.year, _focus.month + n, 1);
    final last = DateTime(first.year, first.month + 1, 0).day;
    return DateTime(first.year, first.month, _focus.day > last ? last : _focus.day);
  }

  KeyEventResult _onKey(FocusNode node, KeyEvent e) {
    if (e is! KeyDownEvent && e is! KeyRepeatEvent) return KeyEventResult.ignored;
    final k = e.logicalKey;
    final dow = (_focus.weekday % 7 - widget.weekStart % 7 + 7) % 7;
    DateTime? to;
    if (k == LogicalKeyboardKey.arrowLeft) to = _focus.subtract(const Duration(days: 1));
    if (k == LogicalKeyboardKey.arrowRight) to = _focus.add(const Duration(days: 1));
    if (k == LogicalKeyboardKey.arrowUp) to = _focus.subtract(const Duration(days: 7));
    if (k == LogicalKeyboardKey.arrowDown) to = _focus.add(const Duration(days: 7));
    if (k == LogicalKeyboardKey.home) to = _focus.subtract(Duration(days: dow));
    if (k == LogicalKeyboardKey.end) to = _focus.add(Duration(days: 6 - dow));
    if (k == LogicalKeyboardKey.pageUp) to = _shiftMonth(-1);
    if (k == LogicalKeyboardKey.pageDown) to = _shiftMonth(1);
    if ((k == LogicalKeyboardKey.enter || k == LogicalKeyboardKey.space) && !_out(_focus)) {
      widget.onChanged(_focus);
      return KeyEventResult.handled;
    }
    if (to == null) return KeyEventResult.ignored;
    _go(_day(to));
    return KeyEventResult.handled;
  }

  @override
  Widget build(BuildContext context) {
    final c = context.km1;
    final t = context.km1Target;
    final today = _day(widget.today ?? DateTime.now());
    final sel = widget.value == null ? null : _day(widget.value!);
    final marks = {for (final e in widget.marks.entries) _day(e.key): e.value};
    final first = DateTime(_focus.year, _focus.month, 1);
    final lead = (first.weekday % 7 - widget.weekStart % 7 + 7) % 7;
    final days = DateTime(_focus.year, _focus.month + 1, 0).day;
    final cells = <DateTime?>[for (var i = 0; i < lead; i++) null, for (var d = 1; d <= days; d++) DateTime(_focus.year, _focus.month, d)];
    while (cells.length % 7 != 0) {
      cells.add(null);
    }
    if (_moveFocus) {
      _moveFocus = false;
      WidgetsBinding.instance.addPostFrameCallback((_) {
        if (mounted) _node(_focus).requestFocus();
      });
    }
    final title = '${_focus.year}年${_focus.month}月';
    return Column(mainAxisSize: MainAxisSize.min, children: [
      Row(mainAxisSize: MainAxisSize.min, children: [
        IconButton(tooltip: '前の月', onPressed: () => _go(_shiftMonth(-1), focus: false), icon: const Km1BIcon(Km1BIconName.chevronLeft, size: Km1Size.iconSm, inherit: true)),
        SizedBox(
          width: t * 5,
          child: Semantics(
            liveRegion: true,
            header: true,
            child: Text(title, textAlign: TextAlign.center, style: Km1Text.subtitle2.copyWith(color: c.ink)),
          ),
        ),
        IconButton(tooltip: '次の月', onPressed: () => _go(_shiftMonth(1), focus: false), icon: const Km1BIcon(Km1BIconName.chevronRight, size: Km1Size.iconSm, inherit: true)),
      ]),
      ExcludeSemantics(
        child: Row(mainAxisSize: MainAxisSize.min, children: [
          for (var i = 0; i < 7; i++)
            SizedBox(
              width: t,
              height: 32,
              child: Center(child: Text(_km1Weekdays[(i + widget.weekStart) % 7], style: Km1Text.caption1.copyWith(color: c.inkSecondary))),
            ),
        ]),
      ),
      Focus(
        skipTraversal: true,
        onKeyEvent: _onKey,
        child: Semantics(
          label: '${widget.label == null ? '' : '${widget.label} '}$title',
          container: true,
          child: Column(mainAxisSize: MainAxisSize.min, children: [
            for (var w = 0; w < cells.length; w += 7)
              Row(mainAxisSize: MainAxisSize.min, children: [
                for (final d in cells.sublist(w, w + 7))
                  SizedBox(width: t, height: t, child: d == null ? null : _dayCell(c, d, d == today, d == sel, d == _focus, marks[d] ?? 0)),
              ]),
          ]),
        ),
      ),
    ]);
  }

  Widget _dayCell(Km1Colors c, DateTime d, bool isToday, bool isSel, bool isFocus, int mark) {
    final dis = _out(d);
    final label = '${d.month}月${d.day}日（${_km1Weekdays[d.weekday % 7]}）${isToday ? ' 今日' : ''}${mark > 0 ? ' 予定 $mark 件' : ''}';
    return Semantics(
      button: true,
      selected: isSel,
      enabled: !dis,
      label: label,
      child: ExcludeSemantics(
        child: Focus(
          focusNode: _node(d),
          canRequestFocus: !dis,
          skipTraversal: !isFocus,
          child: Builder(builder: (context) {
            final focused = Focus.of(context).hasPrimaryFocus;
            return GestureDetector(
              behavior: HitTestBehavior.opaque,
              onTap: dis
                  ? null
                  : () {
                      _go(d, focus: false);
                      widget.onChanged(d);
                    },
              child: Center(
                child: Container(
                  width: 32,
                  height: 32,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    color: isSel ? c.brand : Colors.transparent,
                    border: Border.all(
                      color: focused ? c.focusRing : (isSel || isToday ? c.brandStroke : Colors.transparent),
                      width: focused ? 2 : 1,
                    ),
                  ),
                  child: Stack(alignment: Alignment.center, children: [
                    Text('${d.day}',
                        style: (isSel || isToday ? Km1Text.body1Strong : Km1Text.body1)
                            .copyWith(color: dis ? c.inkDisabled : (isSel ? c.onBrand : c.ink), fontFeatures: const [FontFeature.tabularFigures()])),
                    if (mark > 0)
                      Positioned(
                        bottom: 3,
                        child: Container(width: 4, height: 4, decoration: BoxDecoration(shape: BoxShape.circle, color: isSel ? c.onBrand : c.ink)),
                      ),
                  ]),
                ),
              ),
            );
          }),
        ),
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// Timetable — 曜日 × 時限の時間割 / Weekday-by-period timetable
// ---------------------------------------------------------------------------

class Km1Period {
  const Km1Period(this.label, {this.time});
  final String label;
  final String? time;
}

class Km1Slot {
  const Km1Slot({required this.day, required this.period, required this.title, this.sub, this.color = Km1Category.blue, this.pattern});

  /// 0 始まりの列と行 / Zero-based column and row
  final int day;
  final int period;
  final String title;
  final String? sub;

  /// 分類色（Km1Category）。帯と淡い塗りだけに使う / Category color: bar and tint only
  final Color color;

  /// 分類の模様。渡すと題名の前にしるしが出る / Category pattern; shows a mark before the title
  final Km1Pattern? pattern;
}

class Km1Timetable extends StatelessWidget {
  const Km1Timetable({
    super.key,
    required this.caption,
    required this.periods,
    required this.slots,
    this.days = const ['月', '火', '水', '木', '金'],
    this.today,
    this.onSelect,
    this.minWidth = 560,
  });

  final String caption;
  final List<Km1Period> periods;
  final List<Km1Slot> slots;
  final List<String> days;

  /// 今日の列（0 始まり）/ Today's column, zero-based
  final int? today;

  /// 渡すとコマが押せる。押したらプレビューを出す / Makes slots pressable; open a preview
  final ValueChanged<Km1Slot>? onSelect;
  final double minWidth;

  @override
  Widget build(BuildContext context) {
    final c = context.km1;
    final b = Theme.of(context).brightness;
    final map = {for (final s in slots) '${s.day}-${s.period}': s};
    final border = BorderSide(color: c.strokeSubtle);
    TableRow headRow() => TableRow(
          decoration: BoxDecoration(border: Border(bottom: BorderSide(color: c.strokeStrong))),
          children: [
            const SizedBox(height: 32),
            for (var i = 0; i < days.length; i++)
              Semantics(
                header: true,
                label: i == today ? '${days[i]}（今日）' : days[i],
                child: ExcludeSemantics(
                  child: Container(
                    height: 32,
                    alignment: Alignment.center,
                    decoration: i == today ? BoxDecoration(border: Border(bottom: BorderSide(color: c.brandStroke, width: 2))) : null,
                    child: Text(days[i], style: Km1Text.body1Strong.copyWith(color: i == today ? c.brandInk : c.inkSecondary)),
                  ),
                ),
              ),
          ],
        );
    Widget slot(Km1Slot s) {
      final box = Container(
        constraints: const BoxConstraints(minHeight: 48),
        padding: const EdgeInsets.fromLTRB(Km1Space.sm, Km1Space.xs, Km1Space.sm, Km1Space.xs),
        decoration: BoxDecoration(
          color: Km1Category.tint(s.color, b),
          borderRadius: BorderRadius.circular(Km1Radius.md),
          border: Border(left: BorderSide(color: s.color, width: Km1Size.strokeAccent)),
        ),
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, mainAxisSize: MainAxisSize.min, children: [
          Row(mainAxisSize: MainAxisSize.min, children: [
            if (s.pattern != null) ...[Km1CategoryMark(color: s.color, pattern: s.pattern!), const SizedBox(width: Km1Space.xs)],
            Flexible(child: Text(s.title, style: Km1Text.body1Strong.copyWith(color: c.ink))),
          ]),
          if (s.sub != null) Text(s.sub!, style: Km1Text.caption1.copyWith(color: c.inkSecondary)),
        ]),
      );
      final label = '${days[s.day]}曜 ${periods[s.period].label} ${s.title}${s.sub == null ? '' : '、${s.sub}'}';
      if (onSelect == null) return Semantics(label: label, child: ExcludeSemantics(child: box));
      return Semantics(
        button: true,
        label: label,
        child: ExcludeSemantics(
          child: InkWell(onTap: () => onSelect!(s), borderRadius: BorderRadius.circular(Km1Radius.md), child: box),
        ),
      );
    }

    final table = Table(
      columnWidths: {0: const FixedColumnWidth(104), for (var i = 1; i <= days.length; i++) i: const FlexColumnWidth()},
      border: TableBorder(horizontalInside: border, verticalInside: border),
      defaultVerticalAlignment: TableCellVerticalAlignment.top,
      children: [
        headRow(),
        for (var p = 0; p < periods.length; p++)
          TableRow(children: [
            Padding(
              padding: const EdgeInsets.all(Km1Space.xs),
              child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Text(periods[p].label, style: Km1Text.body1Strong.copyWith(color: c.ink)),
                if (periods[p].time != null) Text(periods[p].time!, style: Km1Text.caption1.copyWith(color: c.inkSecondary)),
              ]),
            ),
            for (var d = 0; d < days.length; d++)
              Container(
                constraints: const BoxConstraints(minHeight: 56),
                padding: const EdgeInsets.all(Km1Space.xs),
                child: map['$d-$p'] == null ? Semantics(label: '空き', child: const SizedBox.shrink()) : slot(map['$d-$p']!),
              ),
          ]),
      ],
    );
    return Semantics(
      container: true,
      label: caption,
      child: Container(
        decoration: BoxDecoration(border: Border.all(color: c.stroke), borderRadius: BorderRadius.circular(Km1Radius.md)),
        clipBehavior: Clip.antiAlias,
        child: LayoutBuilder(builder: (context, box) {
          final w = box.maxWidth < minWidth ? minWidth : box.maxWidth;
          final content = SizedBox(
            width: w,
            child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
              Padding(
                padding: const EdgeInsets.all(Km1Space.md),
                child: Semantics(header: true, child: Text(caption, style: Km1Text.body1Strong.copyWith(color: c.ink))),
              ),
              table,
            ]),
          );
          return box.maxWidth < minWidth ? SingleChildScrollView(scrollDirection: Axis.horizontal, child: content) : content;
        }),
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// FileList — 選んだファイルの一覧と「ファイルを選ぶ」ボタン
// Chosen files plus a pick button. Picking itself is the app's job
// (e.g. the file_picker package), so KM1 has no plugin dependency.
// ---------------------------------------------------------------------------

class Km1File {
  const Km1File(this.name, this.size);
  final String name;

  /// バイト数 / Bytes
  final int size;
}

String km1FormatSize(int b) {
  if (b < 1024) return '$b B';
  if (b < 1024 * 1024) return '${(b / 1024).toStringAsFixed(1)} KB';
  return '${(b / 1024 / 1024).toStringAsFixed(1)} MB';
}

class Km1FileList extends StatelessWidget {
  const Km1FileList({
    super.key,
    required this.label,
    required this.files,
    required this.onPick,
    required this.onRemove,
    this.hint,
    this.error,
    this.required = false,
  });

  final String label;
  final List<Km1File> files;

  /// ファイルを選ぶ処理（file_picker など）/ Opens the picker (file_picker etc.)
  final VoidCallback onPick;
  final ValueChanged<int> onRemove;

  /// 受け付ける形式と大きさを書く（「PDF・画像、10 MB まで」）/ Accepted formats and size
  final String? hint;
  final String? error;
  final bool required;

  @override
  Widget build(BuildContext context) {
    final c = context.km1;
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, mainAxisSize: MainAxisSize.min, children: [
      Text.rich(TextSpan(children: [
        TextSpan(text: label),
        if (required) TextSpan(text: ' ※必須', style: TextStyle(color: c.dangerInk)),
      ]), style: Km1Text.body1Strong.copyWith(color: c.ink)),
      if (hint != null) Text(hint!, style: Km1Text.caption1.copyWith(color: c.inkTertiary)),
      const SizedBox(height: Km1Space.xs),
      Container(
        padding: const EdgeInsets.all(Km1Space.lg),
        decoration: BoxDecoration(
          border: Border.all(color: error != null ? c.dangerInk : c.strokeStrong),
          borderRadius: BorderRadius.circular(Km1Radius.md),
        ),
        child: Row(mainAxisAlignment: MainAxisAlignment.center, children: [
          ExcludeSemantics(child: Km1BIcon(Km1BIconName.upload, size: Km1Size.iconMd, color: c.inkSecondary)),
          const SizedBox(width: Km1Space.sm),
          OutlinedButton(onPressed: onPick, child: Text('ファイルを選ぶ', semanticsLabel: '$label、ファイルを選ぶ')),
        ]),
      ),
      for (var i = 0; i < files.length; i++)
        Padding(
          padding: const EdgeInsets.only(top: Km1Space.xs),
          child: Container(
            padding: const EdgeInsets.only(left: Km1Space.sm),
            decoration: BoxDecoration(border: Border.all(color: c.stroke), borderRadius: BorderRadius.circular(Km1Radius.md)),
            child: Row(children: [
              ExcludeSemantics(child: Km1BIcon(Km1BIconName.document, size: Km1Size.iconMd, color: c.inkSecondary)),
              const SizedBox(width: Km1Space.sm),
              Expanded(child: Text(files[i].name, style: Km1Text.body1.copyWith(color: c.ink))),
              Text(km1FormatSize(files[i].size), style: Km1Text.body1.copyWith(color: c.inkSecondary)),
              IconButton(tooltip: '${files[i].name} を外す', onPressed: () => onRemove(i), icon: const Km1BIcon(Km1BIconName.dismiss, size: Km1Size.iconSm, inherit: true)),
            ]),
          ),
        ),
      if (error != null)
        Padding(
          padding: const EdgeInsets.only(top: Km1Space.xxs),
          child: Text(error!, style: Km1Text.caption1.copyWith(color: c.dangerInk)),
        ),
    ]);
  }
}

// ---------------------------------------------------------------------------
// Avatar — 人や場所を頭文字で示す / Initials for a person or place
// ---------------------------------------------------------------------------

enum Km1AvatarSize { sm, md, lg }

class Km1Avatar extends StatelessWidget {
  const Km1Avatar({super.key, required this.name, this.size = Km1AvatarSize.md, this.color, this.image, this.decorative = false});
  final String name;
  final Km1AvatarSize size;

  /// 省くと名前から Km1Category の色を決める / Defaults to a category color from the name
  final Color? color;
  final ImageProvider? image;

  /// すぐ横に名前があるときは true（二重に読ませない）/ true when the name is already next to it
  final bool decorative;

  String get _initials {
    final n = name.trim();
    if (n.isEmpty) return '';
    final ascii = n.codeUnitAt(0) < 128;
    if (!ascii) return n.replaceAll(RegExp(r'\s'), '').substring(0, 1);
    return n.split(RegExp(r'\s+')).where((w) => w.isNotEmpty).map((w) => w[0]).take(2).join().toUpperCase();
  }

  @override
  Widget build(BuildContext context) {
    final c = context.km1;
    final b = Theme.of(context).brightness;
    var hash = 0;
    for (final u in name.codeUnits) {
      hash = (hash * 31 + u) % 997;
    }
    final base = color ?? Km1Category.all[hash % Km1Category.all.length];
    final px = switch (size) { Km1AvatarSize.sm => 24.0, Km1AvatarSize.md => 32.0, Km1AvatarSize.lg => 48.0 };
    final font = switch (size) { Km1AvatarSize.sm => 10.0, Km1AvatarSize.md => 12.0, Km1AvatarSize.lg => 16.0 };
    final avatar = Container(
      width: px,
      height: px,
      alignment: Alignment.center,
      decoration: BoxDecoration(
        shape: BoxShape.circle,
        color: Km1Category.tint(base, b),
        border: Border.all(color: base.withValues(alpha: .5)),
        image: image == null ? null : DecorationImage(image: image!, fit: BoxFit.cover),
      ),
      child: image == null ? Text(_initials, style: TextStyle(fontSize: font, fontWeight: FontWeight.w600, color: c.ink)) : null,
    );
    if (decorative) return ExcludeSemantics(child: avatar);
    return Semantics(label: name, image: true, child: ExcludeSemantics(child: avatar));
  }
}

// ---------------------------------------------------------------------------
// TimeGrid — 1 日・1 週間の予定表 / Day or week schedule on a time axis
// ---------------------------------------------------------------------------

class Km1TimeGridEvent {
  const Km1TimeGridEvent({
    required this.day,
    required this.title,
    this.start,
    this.end,
    this.sub,
    this.color = Km1Category.blue,
    this.pattern,
    this.allDay = false,
    this.deadline = false,
    this.tentative = false,
  });

  /// days の位置（0 始まり）/ Index into days
  final int day;
  final String title;

  /// 0:00 からの分 / Minutes from 0:00
  final int? start;
  final int? end;
  final String? sub;
  final Color color;

  /// 分類の模様 / Category pattern
  final Km1Pattern? pattern;

  /// 0:00 ちょうどの締め切りは前日の終日として渡す / A 0:00 deadline is all-day on the previous day
  final bool allDay;

  /// 時刻つきの締め切り（start だけ）/ Timed deadline (start only)
  final bool deadline;
  final bool tentative;
}

String _km1Hm(int m) => '${m ~/ 60}:${(m % 60).toString().padLeft(2, '0')}';

class Km1TimeGrid extends StatelessWidget {
  const Km1TimeGrid({
    super.key,
    required this.label,
    required this.days,
    required this.events,
    this.startHour = 8,
    this.endHour = 22,
    this.hourHeight,
    this.now,
    this.onSelect,
  });

  final String label;

  /// 見出し（「11/12（木）」）/ Day labels
  final List<String> days;
  final List<Km1TimeGridEvent> events;
  final int startHour;
  final int endHour;

  /// 省くとスマホ 64・PC 56 / Defaults to 64 on touch, 56 on PC
  final double? hourHeight;

  /// 現在時刻の線を出す列と時刻 / Column and time for the current-time line
  final ({int day, int minute})? now;

  /// 短い予定は文字が切れるので、押したらプレビューを出す / Open a preview: short events truncate
  final ValueChanged<Km1TimeGridEvent>? onSelect;

  String _semantic(Km1TimeGridEvent e) {
    // 見えている文字の順（題名・時刻・補足）のあとに日付（WCAG 2.5.3）/ visible text in order, then the day
    final timed = !e.deadline && !e.allDay;
    final vis = '${e.title}${timed ? ' ${_km1Hm(e.start ?? 0)}〜${_km1Hm(e.end ?? 0)}' : ''}${e.sub == null ? '' : ' ${e.sub}'}';
    final tail = e.allDay ? ' 終日' : (e.deadline ? ' ${_km1Hm(e.start ?? 0)} 締め切り' : '');
    return '$vis、${days[e.day]}$tail';
  }

  Widget _event(BuildContext context, Km1TimeGridEvent e, {bool compact = false}) {
    final c = context.km1;
    final b = Theme.of(context).brightness;
    final barColor = e.deadline ? c.warningInk : e.color;
    final fill = e.deadline ? c.warningTint : Km1Category.tint(e.color, b);
    final content = Container(
      padding: EdgeInsets.fromLTRB(Km1Space.sm, compact ? 0 : 2, Km1Space.xs, compact ? 0 : 2),
      decoration: BoxDecoration(
        color: fill,
        borderRadius: BorderRadius.circular(Km1Radius.sm),
        border: Border(left: BorderSide(color: barColor, width: Km1Size.strokeAccent)),
      ),
      foregroundDecoration: e.tentative ? _Km1Hatch(e.color.withValues(alpha: .4)) : null,
      clipBehavior: Clip.hardEdge,
      child: compact || e.deadline || e.allDay
          ? Row(children: [
              if (e.deadline) ...[Icon(Km1Icons.flag16Filled, size: Km1Size.iconSm, color: c.warningInk), const SizedBox(width: Km1Space.xs)],
              Expanded(child: Text(e.title, maxLines: 1, overflow: TextOverflow.ellipsis, style: Km1Text.caption1.copyWith(color: c.ink, fontWeight: FontWeight.w600))),
            ])
          : Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Row(children: [
                if (e.pattern != null) ...[Km1CategoryMark(color: e.color, pattern: e.pattern!), const SizedBox(width: Km1Space.xs)],
                Expanded(child: Text(e.title, maxLines: 1, overflow: TextOverflow.ellipsis, style: Km1Text.caption1.copyWith(color: c.ink, fontWeight: FontWeight.w600))),
              ]),
              Text('${_km1Hm(e.start ?? 0)}〜${_km1Hm(e.end ?? 0)}', maxLines: 1, overflow: TextOverflow.clip, style: Km1Text.caption1.copyWith(color: c.inkSecondary)),
              if (e.sub != null) Text(e.sub!, maxLines: 1, overflow: TextOverflow.ellipsis, style: Km1Text.caption1.copyWith(color: c.inkSecondary)),
            ]),
    );
    final label = _semantic(e);
    if (onSelect == null) return Semantics(label: label, child: ExcludeSemantics(child: content));
    return Semantics(
      button: true,
      label: label,
      child: ExcludeSemantics(child: InkWell(onTap: () => onSelect!(e), borderRadius: BorderRadius.circular(Km1Radius.sm), child: content)),
    );
  }

  @override
  Widget build(BuildContext context) {
    final c = context.km1;
    final hh = hourHeight ?? (Km1Theme.isTouch ? 64.0 : 56.0);
    final ppm = hh / 60;
    final s0 = startHour * 60, e0 = endHour * 60;
    const hoursWidth = 56.0;
    final allDay = events.where((e) => e.allDay).toList();
    final total = (endHour - startHour) * hh;

    Widget dayColumn(int d) {
      final timed = events.where((e) => e.day == d && !e.allDay && !e.deadline && e.start != null && e.end != null).toList()
        ..sort((a, b) => a.start!.compareTo(b.start!) != 0 ? a.start!.compareTo(b.start!) : b.end!.compareTo(a.end!));
      // 重なる予定を横に並べる / Lay out overlapping events side by side
      final col = <Km1TimeGridEvent, int>{};
      final cols = <Km1TimeGridEvent, int>{};
      var cluster = <Km1TimeGridEvent>[];
      var clusterEnd = -1;
      void flush() {
        final ends = <int>[];
        for (final e in cluster) {
          var i = 0;
          while (i < ends.length && ends[i] > e.start!) {
            i++;
          }
          if (i == ends.length) {
            ends.add(e.end!);
          } else {
            ends[i] = e.end!;
          }
          col[e] = i;
        }
        for (final e in cluster) {
          cols[e] = ends.length;
        }
        cluster = [];
      }

      for (final e in timed) {
        if (cluster.isNotEmpty && e.start! >= clusterEnd) flush();
        cluster.add(e);
        if (e.end! > clusterEnd) clusterEnd = e.end!;
      }
      if (cluster.isNotEmpty) flush();
      final deadlines = events.where((e) => e.day == d && e.deadline && e.start != null && e.start! >= s0 && e.start! < e0).toList();
      final isToday = now != null && now!.day == d;
      return Semantics(
        container: true,
        label: isToday ? '${days[d]}（今日）' : days[d],
        child: LayoutBuilder(builder: (context, box) {
          final w = box.maxWidth;
          return SizedBox(
            height: total,
            child: Stack(clipBehavior: Clip.none, children: [
              for (final e in timed)
                if (e.end! > s0 && e.start! < e0)
                  Positioned(
                    top: (e.start!.clamp(s0, e0) - s0) * ppm,
                    height: ((e.end!.clamp(s0, e0) - e.start!.clamp(s0, e0)) * ppm).clamp(20.0, total),
                    left: w / cols[e]! * col[e]! + 2,
                    width: w / cols[e]! - 4,
                    child: _event(context, e),
                  ),
              for (final e in deadlines)
                Positioned(top: (e.start! - s0) * ppm - 12, height: 24, left: 2, right: 2, child: _event(context, e, compact: true)),
              if (isToday && now!.minute >= s0 && now!.minute <= e0)
                Positioned(
                  top: (now!.minute - s0) * ppm - 1,
                  left: 0,
                  right: 0,
                  child: Semantics(
                    label: '現在 ${_km1Hm(now!.minute)}',
                    child: ExcludeSemantics(child: Container(height: 2, color: c.dangerInk)),
                  ),
                ),
            ]),
          );
        }),
      );
    }

    final grid = Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      // 見出し / Day headings
      ExcludeSemantics(
        child: Container(
          decoration: BoxDecoration(border: Border(bottom: BorderSide(color: c.strokeStrong))),
          child: Row(children: [
            const SizedBox(width: hoursWidth),
            for (var d = 0; d < days.length; d++)
              Expanded(
                child: Container(
                  height: 36,
                  alignment: Alignment.center,
                  decoration: now?.day == d ? BoxDecoration(border: Border(bottom: BorderSide(color: c.brandStroke, width: 2))) : null,
                  child: Text(days[d], style: Km1Text.body1Strong.copyWith(color: now?.day == d ? c.brandInk : c.inkSecondary)),
                ),
              ),
          ]),
        ),
      ),
      // 終日 / All-day row
      if (allDay.isNotEmpty)
        Container(
          decoration: BoxDecoration(border: Border(bottom: BorderSide(color: c.strokeStrong))),
          child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
            SizedBox(
              width: hoursWidth,
              child: Padding(
                padding: const EdgeInsets.all(Km1Space.xs),
                child: ExcludeSemantics(child: Text('終日', textAlign: TextAlign.right, style: Km1Text.caption1.copyWith(color: c.inkSecondary))),
              ),
            ),
            for (var d = 0; d < days.length; d++)
              Expanded(
                child: Padding(
                  padding: const EdgeInsets.all(2),
                  child: Column(children: [
                    for (final e in allDay.where((e) => e.day == d))
                      Padding(padding: const EdgeInsets.only(bottom: 2), child: SizedBox(height: 24, child: _event(context, e, compact: true))),
                  ]),
                ),
              ),
          ]),
        ),
      // 時刻の軸 / Time axis
      Expanded(
        child: SingleChildScrollView(
          child: SizedBox(
            height: total,
            child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
              SizedBox(
                width: hoursWidth,
                child: ExcludeSemantics(
                  child: Stack(children: [
                    for (var hr = startHour; hr < endHour; hr++)
                      Positioned(
                        top: (hr - startHour) * hh + (hr == startHour ? 0 : -8),
                        right: Km1Space.xs,
                        child: Text('$hr:00', style: Km1Text.caption1.copyWith(color: c.inkSecondary)),
                      ),
                  ]),
                ),
              ),
              for (var d = 0; d < days.length; d++)
                Expanded(
                  child: CustomPaint(
                    painter: _Km1HourLines(hh: hh, line: c.strokeSubtle),
                    child: dayColumn(d),
                  ),
                ),
            ]),
          ),
        ),
      ),
    ]);

    return Semantics(
      container: true,
      label: label,
      child: Container(
        decoration: BoxDecoration(border: Border.all(color: c.stroke), borderRadius: BorderRadius.circular(Km1Radius.md)),
        clipBehavior: Clip.antiAlias,
        child: LayoutBuilder(builder: (context, box) {
          final minW = hoursWidth + days.length * 96.0;
          if (days.length == 1 || box.maxWidth >= minW) return grid;
          return SingleChildScrollView(scrollDirection: Axis.horizontal, child: SizedBox(width: minW, height: box.maxHeight, child: grid));
        }),
      ),
    );
  }
}

/// 30 分ごとの横線と左の縦線 / Half-hour lines and the left border
class _Km1HourLines extends CustomPainter {
  _Km1HourLines({required this.hh, required this.line});
  final double hh;
  final Color line;

  @override
  void paint(Canvas canvas, Size size) {
    final p = Paint()
      ..color = line
      ..strokeWidth = 1;
    for (var y = 0.0; y <= size.height; y += hh / 2) {
      canvas.drawLine(Offset(0, y), Offset(size.width, y), p);
    }
    canvas.drawLine(Offset.zero, Offset(0, size.height), p);
  }

  @override
  bool shouldRepaint(_Km1HourLines old) => old.hh != hh || old.line != line;
}

/// 仮の予定の斜線 / Hatching for tentative events
class _Km1Hatch extends Decoration {
  const _Km1Hatch(this.color);
  final Color color;

  @override
  BoxPainter createBoxPainter([VoidCallback? onChanged]) => _Km1HatchPainter(color);
}

class _Km1HatchPainter extends BoxPainter {
  _Km1HatchPainter(this.color);
  final Color color;

  @override
  void paint(Canvas canvas, Offset offset, ImageConfiguration configuration) {
    final size = configuration.size;
    if (size == null) return;
    final rect = offset & size;
    final p = Paint()
      ..color = color
      ..strokeWidth = 2;
    canvas.save();
    canvas.clipRect(rect);
    for (var x = -size.height; x < size.width; x += 8) {
      canvas.drawLine(Offset(rect.left + x, rect.bottom), Offset(rect.left + x + size.height, rect.top), p);
    }
    canvas.restore();
  }
}

/// 読み上げで知らせる（新旧の Flutter で動く書き方）/ Announce to screen readers on old and new Flutter
void _km1Announce(BuildContext context, String message) {
  // ignore: deprecated_member_use
  SemanticsService.announce(message, Directionality.of(context));
}

// ---------------------------------------------------------------------------
// TagPicker — 候補から複数を選ぶ / Pick several options as tags
// ---------------------------------------------------------------------------

class Km1Option {
  const Km1Option(this.value, this.label);
  final String value;
  final String label;
}

class Km1TagPicker extends StatefulWidget {
  const Km1TagPicker({
    super.key,
    required this.label,
    required this.options,
    required this.value,
    required this.onChanged,
    this.hint,
    this.error,
    this.max,
    this.placeholder,
  });

  final String label;
  final List<Km1Option> options;

  /// 選んだ value の一覧 / Selected values
  final List<String> value;
  final ValueChanged<List<String>> onChanged;
  final String? hint;
  final String? error;

  /// 上限。超えたら止めずに知らせる / Limit; exceeding it is announced
  final int? max;
  final String? placeholder;

  @override
  State<Km1TagPicker> createState() => _Km1TagPickerState();
}

class _Km1TagPickerState extends State<Km1TagPicker> {
  TextEditingController? _text;
  FocusNode? _focus;
  String? _notice;

  String _label(String v) {
    for (final o in widget.options) {
      if (o.value == v) return o.label;
    }
    return v;
  }

  void _add(Km1Option o) {
    if (widget.max != null && widget.value.length >= widget.max!) {
      setState(() => _notice = '選べるのは ${widget.max} 個までです');
      _km1Announce(context, _notice!);
      return;
    }
    widget.onChanged([...widget.value, o.value]);
    _km1Announce(context, '${o.label} を追加しました');
    _text?.clear();
    setState(() => _notice = null);
    _focus?.requestFocus();
  }

  void _remove(String v) {
    widget.onChanged(widget.value.where((x) => x != v).toList());
    _km1Announce(context, '${_label(v)} を外しました');
    _focus?.requestFocus();
  }

  @override
  Widget build(BuildContext context) {
    final c = context.km1;
    final t = context.km1Target;
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, mainAxisSize: MainAxisSize.min, children: [
      Text(widget.label, style: Km1Text.body1Strong.copyWith(color: c.ink)),
      if (widget.hint != null) Text(widget.hint!, style: Km1Text.caption1.copyWith(color: c.inkTertiary)),
      const SizedBox(height: Km1Space.xs),
      if (widget.value.isNotEmpty)
        Padding(
          padding: const EdgeInsets.only(bottom: Km1Space.xs),
          child: Wrap(spacing: Km1Space.xs, runSpacing: Km1Space.xs, children: [
            for (final v in widget.value)
              Container(
                padding: const EdgeInsets.only(left: Km1Space.sm),
                decoration: BoxDecoration(color: c.surfaceSunken, border: Border.all(color: c.strokeStrong), borderRadius: BorderRadius.circular(Km1Radius.md)),
                child: Row(mainAxisSize: MainAxisSize.min, children: [
                  Text(_label(v), style: Km1Text.body1.copyWith(color: c.ink)),
                  IconButton(
                    tooltip: '${_label(v)} を外す',
                    constraints: BoxConstraints(minWidth: t, minHeight: t),
                    onPressed: () => _remove(v),
                    icon: const Km1BIcon(Km1BIconName.dismiss, size: Km1Size.iconSm, inherit: true),
                  ),
                ]),
              ),
          ]),
        ),
      Autocomplete<Km1Option>(
        displayStringForOption: (o) => o.label,
        optionsBuilder: (v) {
          final q = v.text.toLowerCase();
          return widget.options.where((o) => !widget.value.contains(o.value) && (q.isEmpty || o.label.toLowerCase().contains(q)));
        },
        onSelected: _add,
        fieldViewBuilder: (context, controller, focusNode, onSubmitted) {
          _text = controller;
          _focus = focusNode;
          return TextField(
            controller: controller,
            focusNode: focusNode,
            onSubmitted: (_) => onSubmitted(),
            style: Theme.of(context).textTheme.bodyLarge,
            decoration: InputDecoration(
              hintText: widget.placeholder,
              errorText: widget.error ?? _notice,
              prefixIcon: const Km1BIcon(Km1BIconName.tag, size: Km1Size.iconMd, inherit: true),
            ),
          );
        },
      ),
    ]);
  }
}

// ---------------------------------------------------------------------------
// SortableList — 順番を入れ替えられる一覧
// Reorderable list: drag handle, up/down buttons (WCAG 2.5.7), announcements
// ---------------------------------------------------------------------------

class Km1SortItem {
  const Km1SortItem({required this.id, required this.label, this.sub});
  final String id;
  final String label;
  final String? sub;
}

class Km1SortableList extends StatelessWidget {
  const Km1SortableList({super.key, required this.label, required this.items, required this.onChanged, this.density = Km1Density.regular});
  final String label;
  final List<Km1SortItem> items;
  final ValueChanged<List<Km1SortItem>> onChanged;

  /// 密度（既定 regular）。項目の間だけが変わる。つまみと上下のボタンは操作領域を保つ。
  /// Density (default regular): only the gap between items changes; grip and move buttons keep their hit area.
  final Km1Density density;

  void _move(BuildContext context, int from, int to) {
    if (to < 0 || to >= items.length || from == to) return;
    final n = [...items];
    final x = n.removeAt(from);
    n.insert(to, x);
    onChanged(n);
    _km1Announce(context, '${x.label} を ${to + 1} 番目に移動しました（全 ${items.length} 件）');
  }

  @override
  Widget build(BuildContext context) {
    final c = context.km1;
    return Semantics(
      container: true,
      label: label,
      child: ReorderableListView.builder(
        shrinkWrap: true,
        physics: const NeverScrollableScrollPhysics(),
        buildDefaultDragHandles: false,
        itemCount: items.length,
        // 新しい Flutter では onReorderItem が後継。3.27 でも動くよう onReorder を使う。
        // onReorderItem replaces this on newer Flutter; onReorder keeps 3.27 working.
        // ignore: deprecated_member_use
        onReorder: (from, to) => _move(context, from, to > from ? to - 1 : to),
        itemBuilder: (context, i) {
          final it = items[i];
          return Padding(
            key: ValueKey(it.id),
            padding: EdgeInsets.only(bottom: density.itemGap / 2),
            child: Container(
              decoration: BoxDecoration(color: c.surface, border: Border.all(color: c.stroke), borderRadius: BorderRadius.circular(Km1Radius.md)),
              child: Row(children: [
                ReorderableDragStartListener(
                  index: i,
                  child: Semantics(
                    label: '${it.label}（${i + 1} / ${items.length}）、ドラッグで並べ替え',
                    child: ExcludeSemantics(
                      child: SizedBox(
                        width: context.km1Target,
                        height: context.km1Target,
                        child: Km1BIcon(Km1BIconName.drag, size: Km1Size.iconMd, color: c.inkSecondary),
                      ),
                    ),
                  ),
                ),
                Expanded(
                  child: Padding(
                    padding: const EdgeInsets.symmetric(vertical: Km1Space.xs),
                    child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                      Text(it.label, style: Km1Text.body1.copyWith(color: c.ink)),
                      if (it.sub != null) Text(it.sub!, style: Km1Text.caption1.copyWith(color: c.inkSecondary)),
                    ]),
                  ),
                ),
                IconButton(
                  tooltip: '${it.label} を上へ',
                  onPressed: i == 0 ? null : () => _move(context, i, i - 1),
                  icon: const Km1BIcon(Km1BIconName.arrowUp, size: Km1Size.iconSm, inherit: true),
                ),
                IconButton(
                  tooltip: '${it.label} を下へ',
                  onPressed: i == items.length - 1 ? null : () => _move(context, i, i + 1),
                  icon: const Km1BIcon(Km1BIconName.arrowDown, size: Km1Size.iconSm, inherit: true),
                ),
              ]),
            ),
          );
        },
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// Forms（KM1-PAT-001）— フォームの並べ方 / Form layout
// 欄の確かめ方: Form(autovalidateMode: AutovalidateMode.onUnfocus) で「離れたら確かめる」。
// 送信時は formKey.currentState!.validate()。隠れた欄はツリーから外すので検証されない。
// Validation: Form(autovalidateMode: AutovalidateMode.onUnfocus) validates on blur;
// call formKey.currentState!.validate() on submit. Hidden fields leave the tree, so they are not validated.
// 入力値は TextEditingController を親で持てば、欄を隠しても残る。
// Keep TextEditingControllers in the parent so values survive while a field is hidden.
// ---------------------------------------------------------------------------

/// ページのフォームか、ダイアログ・ドロワーの中か / Page form or contained (dialog, drawer)
enum Km1FormDensity { page, contained }

double _km1FieldGap(Km1FormDensity d) => d == Km1FormDensity.page ? Km1Space.xxl : Km1Space.lg;
double _km1GroupGap(Km1FormDensity d) => d == Km1FormDensity.page ? Km1Space.xxxl + Km1Space.lg : Km1Space.xxxl;

/// フォーム全体の器。最大 720px・左寄せ、グループの間を広く取る。
/// Form shell: max 720px, left-aligned, wide gaps between groups.
class Km1Form extends StatelessWidget {
  const Km1Form({super.key, required this.children, this.density = Km1FormDensity.page, this.formKey});

  final List<Widget> children;
  final Km1FormDensity density;
  final GlobalKey<FormState>? formKey;

  @override
  Widget build(BuildContext context) {
    final gap = _km1GroupGap(density);
    final body = <Widget>[];
    for (var i = 0; i < children.length; i++) {
      if (i > 0) body.add(SizedBox(height: gap));
      body.add(children[i]);
    }
    return Align(
      alignment: AlignmentDirectional.topStart,
      child: ConstrainedBox(
        constraints: BoxConstraints(maxWidth: density == Km1FormDensity.page ? 720 : double.infinity),
        child: Form(
          key: formKey,
          autovalidateMode: AutovalidateMode.onUnfocus,
          child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, mainAxisSize: MainAxisSize.min, children: body),
        ),
      ),
    );
  }
}

/// 見出し付きのまとまり。枠や背景は付けない。
/// A titled cluster with no border or background.
class Km1FormGroup extends StatelessWidget {
  const Km1FormGroup({super.key, required this.title, this.description, required this.children, this.density = Km1FormDensity.page});

  final String title;
  final String? description;
  final List<Widget> children;
  final Km1FormDensity density;

  @override
  Widget build(BuildContext context) {
    final c = context.km1;
    final gap = _km1FieldGap(density);
    final body = <Widget>[];
    for (var i = 0; i < children.length; i++) {
      if (i > 0) body.add(SizedBox(height: gap));
      body.add(children[i]);
    }
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      mainAxisSize: MainAxisSize.min,
      children: [
        Semantics(header: true, child: Text(title, style: Km1Text.subtitle2.copyWith(color: c.ink))),
        if (description != null) ...[
          const SizedBox(height: Km1Space.xs),
          Text(description!, style: Km1Text.body1.copyWith(color: c.inkSecondary)),
        ],
        const SizedBox(height: Km1Space.md),
        ...body,
      ],
    );
  }
}

/// FormGrid の中で行の全幅を使う子 / A child that spans the whole row in Km1FormGrid
class Km1FullSpan extends StatelessWidget {
  const Km1FullSpan({super.key, required this.child});

  final Widget child;

  @override
  Widget build(BuildContext context) => child;
}

/// 短い欄の組を、画面 1024px 以上かつ幅 560px 以上のときだけ 2 列にする。子の順に左→右、上→下。
/// Two columns only when the screen is ≥1024px and the form is ≥560px wide; children flow left→right, top→bottom.
class Km1FormGrid extends StatelessWidget {
  const Km1FormGrid({super.key, required this.children, this.columns = 1, this.density = Km1FormDensity.page});

  final List<Widget> children;
  final int columns;
  final Km1FormDensity density;

  @override
  Widget build(BuildContext context) {
    final vGap = _km1FieldGap(density);
    final screen = MediaQuery.sizeOf(context).width;
    return LayoutBuilder(builder: (context, box) {
      final two = columns == 2 && screen >= 1024 && box.maxWidth >= 560;
      final rows = <Widget>[];
      var i = 0;
      while (i < children.length) {
        final a = children[i];
        final canPair = two && a is! Km1FullSpan && i + 1 < children.length && children[i + 1] is! Km1FullSpan;
        if (rows.isNotEmpty) rows.add(SizedBox(height: vGap));
        if (canPair) {
          rows.add(Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Expanded(child: a),
            const SizedBox(width: Km1Space.lg),
            Expanded(child: children[i + 1]),
          ]));
          i += 2;
        } else {
          rows.add(a);
          i += 1;
        }
      }
      return Column(crossAxisAlignment: CrossAxisAlignment.stretch, mainAxisSize: MainAxisSize.min, children: rows);
    });
  }
}

/// 前の答えで必要になる欄。出てもフォーカスは動かさず、読み上げで知らせる。
/// Fields revealed by an earlier answer; focus stays put and the change is announced.
class Km1ConditionalField extends StatefulWidget {
  const Km1ConditionalField({super.key, required this.show, required this.child, this.announce = '入力項目が追加されました', this.announceHide});

  final bool show;
  final Widget child;
  final String announce;
  final String? announceHide;

  @override
  State<Km1ConditionalField> createState() => _Km1ConditionalFieldState();
}

class _Km1ConditionalFieldState extends State<Km1ConditionalField> {
  @override
  void didUpdateWidget(covariant Km1ConditionalField oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.show == widget.show) return;
    final msg = widget.show ? widget.announce : widget.announceHide;
    if (msg != null && msg.isNotEmpty) _km1Announce(context, msg);
  }

  @override
  Widget build(BuildContext context) {
    if (!widget.show) return const SizedBox.shrink();
    final c = context.km1;
    final hc = MediaQuery.highContrastOf(context);
    return Container(
      padding: const EdgeInsetsDirectional.only(start: Km1Space.lg),
      decoration: BoxDecoration(border: BorderDirectional(start: BorderSide(color: hc ? c.ink : c.strokeSubtle, width: 2))),
      child: widget.child,
    );
  }
}

/// エラー一覧の 1 行 / One line of the error summary
class Km1FormError {
  const Km1FormError({required this.label, required this.message, required this.focusNode});

  final String label;
  final String message;

  /// 該当の欄の FocusNode / FocusNode of the field
  final FocusNode focusNode;
}

/// 送信に失敗したとき、フォームの上に件数と一覧を出す。focusKey が変わるたびに一覧へフォーカスする。
/// Shown above the form after a failed submit; takes focus whenever focusKey changes.
class Km1ErrorSummary extends StatefulWidget {
  const Km1ErrorSummary({super.key, required this.errors, this.focusKey = 0, this.title = '入力内容を確認してください'});

  final List<Km1FormError> errors;
  final int focusKey;
  final String title;

  @override
  State<Km1ErrorSummary> createState() => _Km1ErrorSummaryState();
}

class _Km1ErrorSummaryState extends State<Km1ErrorSummary> {
  final FocusNode _node = FocusNode(debugLabel: 'Km1ErrorSummary');

  @override
  void didUpdateWidget(covariant Km1ErrorSummary oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.focusKey != widget.focusKey && widget.errors.isNotEmpty) {
      WidgetsBinding.instance.addPostFrameCallback((_) {
        if (!mounted) return;
        _node.requestFocus();
        Scrollable.ensureVisible(context, alignment: 0.1);
      });
    }
  }

  @override
  void dispose() {
    _node.dispose();
    super.dispose();
  }

  void _go(FocusNode n) {
    final ctx = n.context;
    if (ctx != null) Scrollable.ensureVisible(ctx, alignment: 0.3);
    n.requestFocus();
  }

  @override
  Widget build(BuildContext context) {
    if (widget.errors.isEmpty) return const SizedBox.shrink();
    final c = context.km1;
    final hc = MediaQuery.highContrastOf(context);
    final title = '${widget.title}（${widget.errors.length} 件）';
    return Focus(
      focusNode: _node,
      child: Semantics(
        container: true,
        label: title,
        child: Container(
          padding: const EdgeInsets.all(Km1Space.lg),
          decoration: BoxDecoration(
            color: c.dangerTint,
            borderRadius: BorderRadius.circular(Km1Radius.md),
            border: Border(
              left: BorderSide(color: hc ? c.ink : c.dangerInk, width: 4),
              top: BorderSide(color: hc ? c.ink : c.dangerInk),
              right: BorderSide(color: hc ? c.ink : c.dangerInk),
              bottom: BorderSide(color: hc ? c.ink : c.dangerInk),
            ),
          ),
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, mainAxisSize: MainAxisSize.min, children: [
            Semantics(
              header: true,
              child: Row(children: [
                Icon(Km1Icons.statusError16, size: Km1Size.iconSm, color: c.dangerInk),
                const SizedBox(width: Km1Space.xs),
                Flexible(child: Text(title, style: Km1Text.subtitle2.copyWith(color: c.ink))),
              ]),
            ),
            const SizedBox(height: Km1Space.sm),
            for (final e in widget.errors)
              Align(
                alignment: AlignmentDirectional.centerStart,
                child: TextButton(
                  onPressed: () => _go(e.focusNode),
                  style: TextButton.styleFrom(
                    foregroundColor: c.brandInk,
                    minimumSize: Size(0, context.km1Target),
                    padding: const EdgeInsets.symmetric(horizontal: Km1Space.xs),
                    alignment: AlignmentDirectional.centerStart,
                  ),
                  child: Text('${e.label}：${e.message}', style: Km1Text.body1.copyWith(decoration: TextDecoration.underline, color: c.brandInk)),
                ),
              ),
          ]),
        ),
      ),
    );
  }
}

/// 子は PC の並び（左から: キャンセル … 主ボタン）で渡す。幅 479px 以下は縦に積み、順を逆にして主ボタンを上に置く。
/// Pass children in PC order (Cancel … primary). At ≤479px they stack in reverse so the primary is on top.
class Km1FormActions extends StatelessWidget {
  const Km1FormActions({super.key, required this.children});

  final List<Widget> children;

  @override
  Widget build(BuildContext context) {
    final narrow = MediaQuery.sizeOf(context).width < 480;
    if (narrow) {
      final list = children.reversed.toList();
      return Column(crossAxisAlignment: CrossAxisAlignment.stretch, mainAxisSize: MainAxisSize.min, children: [
        for (var i = 0; i < list.length; i++) ...[if (i > 0) const SizedBox(height: Km1Space.sm), list[i]],
      ]);
    }
    return Wrap(alignment: WrapAlignment.end, spacing: Km1Space.sm, runSpacing: Km1Space.sm, children: children);
  }
}

// ---------------------------------------------------------------------------
// KM1 × M1（KM1-M1-001）— 一覧・選択・その場の編集・工程・下からのシート・画像の格子
// Lists, selection, inline editing, step flows, bottom sheets, image grids
// ---------------------------------------------------------------------------

/// 一覧の 1 行。主操作は行の大半、補助操作（trailing）は別の押し場所。選択できる一覧では左にチェック。
/// One list row: the primary action fills the row; trailing is a separate target; a checkbox on the left when selectable.
class Km1ListItem extends StatelessWidget {
  const Km1ListItem({
    super.key,
    required this.title,
    this.description,
    this.meta,
    this.leading,
    this.trailing,
    this.onTap,
    this.selectable = false,
    this.selected = false,
    this.onSelectedChanged,
  });

  final String title;
  final String? description;
  final String? meta;
  final Widget? leading;
  final Widget? trailing;
  final VoidCallback? onTap;
  final bool selectable;
  final bool selected;
  final ValueChanged<bool>? onSelectedChanged;

  @override
  Widget build(BuildContext context) {
    final c = context.km1;
    final primary = Semantics(
      button: onTap != null,
      selected: selectable ? selected : null,
      child: InkWell(
        onTap: onTap,
        child: ConstrainedBox(
          constraints: BoxConstraints(minHeight: context.km1Target),
          child: Padding(
            padding: const EdgeInsets.symmetric(horizontal: Km1Space.lg, vertical: Km1Space.smNudge),
            child: Row(children: [
              if (leading != null) ...[IconTheme(data: IconThemeData(color: c.inkSecondary, size: Km1Size.iconMd), child: leading!), const SizedBox(width: Km1Space.md)],
              Expanded(
                child: Column(crossAxisAlignment: CrossAxisAlignment.start, mainAxisSize: MainAxisSize.min, children: [
                  Text(title, style: Km1Text.body1.copyWith(color: c.ink)),
                  if (description != null) const SizedBox(height: Km1Space.xs),
                  if (description != null) Text(description!, style: Km1Text.caption1.copyWith(color: c.inkSecondary)),
                ]),
              ),
              if (meta != null) ...[const SizedBox(width: Km1Space.sm), Text(meta!, style: Km1Text.caption1.copyWith(color: c.inkSecondary))],
            ]),
          ),
        ),
      ),
    );
    return Container(
      decoration: BoxDecoration(
        color: selected ? c.brandTint : null,
        border: selected ? Border(left: BorderSide(color: c.brand, width: 3)) : null,
      ),
      child: Row(children: [
        if (selectable)
          SizedBox(
            width: context.km1Target,
            child: Checkbox(
              value: selected,
              onChanged: onSelectedChanged == null ? null : (v) => onSelectedChanged!(v ?? false),
              semanticLabel: '$title を選択',
            ),
          ),
        Expanded(child: primary),
        if (trailing != null) Padding(padding: const EdgeInsets.only(right: Km1Space.xs), child: trailing!),
      ]),
    );
  }
}

/// 一覧の小見出し（件数つき）。長い一覧で上に固定するときは SliverPersistentHeader(pinned: true) に入れる。
/// List subheader with a count; to pin it in long lists, place it in SliverPersistentHeader(pinned: true).
class Km1ListSectionHeader extends StatelessWidget {
  const Km1ListSectionHeader({super.key, required this.title, this.count});

  final String title;
  final int? count;

  @override
  Widget build(BuildContext context) {
    final c = context.km1;
    return Semantics(
      header: true,
      child: Container(
        color: c.surface,
        padding: const EdgeInsets.fromLTRB(Km1Space.lg, Km1Space.md, Km1Space.lg, Km1Space.xs),
        child: Row(crossAxisAlignment: CrossAxisAlignment.baseline, textBaseline: TextBaseline.alphabetic, children: [
          Text(title, style: Km1Text.body1Strong.copyWith(color: c.ink)),
          if (count != null) ...[const SizedBox(width: Km1Space.sm), Text('$count 件', style: Km1Text.caption1.copyWith(color: c.inkSecondary))],
        ]),
      ),
    );
  }
}

/// 選んだ対象にだけ効く操作。0 件のときは何も出さない。件数は読み上げに伝える。
/// Actions for the current selection; hidden at zero; the count is announced.
class Km1ContextualActionBar extends StatelessWidget {
  const Km1ContextualActionBar({super.key, required this.count, required this.actions, required this.onClear, this.total, this.onSelectAll});

  final int count;
  final int? total;
  final List<Km1BulkAction> actions;
  final VoidCallback onClear;
  final VoidCallback? onSelectAll;

  @override
  Widget build(BuildContext context) {
    final c = context.km1;
    if (count == 0) return Semantics(liveRegion: true, child: const SizedBox.shrink());
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: Km1Space.sm, vertical: Km1Space.xs),
      decoration: BoxDecoration(color: c.brandTint, border: Border.all(color: c.brandStroke), borderRadius: BorderRadius.circular(Km1Radius.md)),
      child: Wrap(spacing: Km1Space.xs, runSpacing: Km1Space.xs, crossAxisAlignment: WrapCrossAlignment.center, children: [
        Semantics(liveRegion: true, child: Text(total == null ? '$count 件を選択中' : '$count 件を選択中（全 $total 件）', style: Km1Text.body1Strong.copyWith(color: c.ink))),
        for (final a in actions)
          OutlinedButton(
            onPressed: () => a.onPressed(const <Object>{}),
            style: a.danger ? OutlinedButton.styleFrom(foregroundColor: c.dangerInk) : null,
            child: Text(a.label),
          ),
        if (onSelectAll != null && total != null && count < total!) TextButton(onPressed: onSelectAll, child: Text('すべて選択（$total 件）')),
        TextButton(onPressed: onClear, child: const Text('選択を解除')),
      ]),
    );
  }
}

/// その項目だけをその場で編集する。閉じているときは項目名と今の値。保存・キャンセル・保存中・失敗を持つ。
/// Edit one item in place: collapsed shows the name and current value; open shows the form with save/cancel, busy and error states.
class Km1ExpansionEditor extends StatefulWidget {
  const Km1ExpansionEditor({
    super.key,
    required this.title,
    required this.summary,
    required this.child,
    required this.onSave,
    this.onCancel,
    this.dirty = false,
    this.readOnlyReason,
  });

  final String title;
  final String summary;
  final Widget child;

  /// 成功で true。失敗は例外のメッセージを表示する / Return true on success; a thrown message is shown.
  final Future<bool> Function() onSave;
  final VoidCallback? onCancel;
  final bool dirty;
  final String? readOnlyReason;

  @override
  State<Km1ExpansionEditor> createState() => _Km1ExpansionEditorState();
}

class _Km1ExpansionEditorState extends State<Km1ExpansionEditor> {
  bool _open = false;
  bool _busy = false;
  String? _error;
  String? _note;
  final FocusNode _head = FocusNode(debugLabel: 'Km1ExpansionEditor');

  @override
  void dispose() {
    _head.dispose();
    super.dispose();
  }

  void _toggle() {
    if (_open && widget.dirty) {
      setState(() => _note = '変更が保存されていません。「保存」か「キャンセル」を押してください。');
      return;
    }
    setState(() {
      _open = !_open;
      _note = null;
      _error = null;
    });
  }

  Future<void> _save() async {
    if (_busy) return;
    setState(() {
      _busy = true;
      _error = null;
    });
    try {
      final ok = await widget.onSave();
      if (!mounted) return;
      setState(() {
        _busy = false;
        if (ok) _open = false;
      });
      if (ok) {
        _km1Announce(context, '${widget.title}を保存しました');
        _head.requestFocus();
      }
    } catch (e) {
      if (!mounted) return;
      setState(() {
        _busy = false;
        _error = e.toString();
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    final c = context.km1;
    final ro = widget.readOnlyReason != null;
    final head = ConstrainedBox(
      constraints: BoxConstraints(minHeight: context.km1Target),
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: Km1Space.lg, vertical: Km1Space.smNudge),
        child: Row(children: [
          Expanded(child: Text(widget.title, style: Km1Text.body1Strong.copyWith(color: c.ink))),
          Expanded(flex: 2, child: Text(ro ? '${widget.summary}\n${widget.readOnlyReason}' : widget.summary, style: Km1Text.body1.copyWith(color: c.inkSecondary))),
          if (!ro)
            ExcludeSemantics(
              child: _open
                  ? Km1BIcon(Km1BIconName.chevronUp, size: Km1Size.iconSm, color: c.brandInk)
                  : Row(mainAxisSize: MainAxisSize.min, children: [
                      Km1BIcon(Km1BIconName.edit, size: Km1Size.iconSm, color: c.brandInk),
                      const SizedBox(width: Km1Space.xs),
                      Text('編集', style: Km1Text.body1Strong.copyWith(color: c.brandInk)),
                    ]),
            ),
        ]),
      ),
    );
    return Container(
      margin: const EdgeInsets.only(bottom: Km1Space.sm),
      decoration: BoxDecoration(color: c.surface, border: Border.all(color: _open ? c.stroke : c.strokeSubtle), borderRadius: BorderRadius.circular(Km1Radius.md)),
      child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
        if (ro)
          head
        else
          Semantics(
            button: true,
            expanded: _open,
            child: InkWell(focusNode: _head, onTap: _toggle, borderRadius: BorderRadius.circular(Km1Radius.md), child: head),
          ),
        if (_open)
          Container(
            decoration: BoxDecoration(border: Border(top: BorderSide(color: c.strokeSubtle))),
            padding: const EdgeInsets.fromLTRB(Km1Space.lg, Km1Space.sm, Km1Space.lg, Km1Space.lg),
            child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
              widget.child,
              if (_error != null) ...[
                const SizedBox(height: Km1Space.lg),
                Semantics(
                  liveRegion: true,
                  child: Container(
                    padding: const EdgeInsets.symmetric(horizontal: Km1Space.md, vertical: Km1Space.sm),
                    decoration: BoxDecoration(color: c.dangerTint, borderRadius: BorderRadius.circular(Km1Radius.md)),
                    child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
                      Icon(Km1Icons.statusError16, size: Km1Size.iconSm, color: c.dangerInk),
                      const SizedBox(width: Km1Space.xs),
                      Expanded(child: Text(_error!, style: Km1Text.body1.copyWith(color: c.ink))),
                    ]),
                  ),
                ),
              ],
              if (_note != null) ...[const SizedBox(height: Km1Space.sm), Semantics(liveRegion: true, child: Text(_note!, style: Km1Text.body1.copyWith(color: c.warningInk)))],
              const SizedBox(height: Km1Space.lg),
              Km1FormActions(children: [
                OutlinedButton(
                  onPressed: () {
                    widget.onCancel?.call();
                    setState(() {
                      _open = false;
                      _note = null;
                    });
                    _head.requestFocus();
                  },
                  child: const Text('キャンセル'),
                ),
                FilledButton(onPressed: _busy ? null : _save, child: Text(_busy ? '保存中…' : '保存')),
              ]),
            ]),
          ),
      ]),
    );
  }
}

/// StepFlow の工程 / A step in Km1StepFlow
class Km1Step {
  const Km1Step({required this.id, required this.title, this.optional = false, this.editable = true});

  final String id;
  final String title;
  final bool optional;
  final bool editable;
}

/// 順序のある複数の工程を利用者が進める。工程の一覧（完了・現在・エラー・未完了）と、今の工程の見出し・中身・戻る/次へ。
/// A user-driven multi-step flow: the step list (done, current, error, to do), then the current step's heading, content and back/next.
class Km1StepFlow extends StatefulWidget {
  const Km1StepFlow({
    super.key,
    required this.steps,
    required this.active,
    required this.child,
    this.completed = const {},
    this.errors = const {},
    this.linear = true,
    this.onStepChange,
    this.onBack,
    this.onNext,
    this.onFinish,
    this.finishLabel = '完了',
  });

  final List<Km1Step> steps;
  final String active;
  final Widget child;
  final Set<String> completed;
  final Set<String> errors;
  final bool linear;
  final ValueChanged<String>? onStepChange;
  final VoidCallback? onBack;
  final VoidCallback? onNext;
  final VoidCallback? onFinish;
  final String finishLabel;

  @override
  State<Km1StepFlow> createState() => _Km1StepFlowState();
}

class _Km1StepFlowState extends State<Km1StepFlow> {
  final FocusNode _heading = FocusNode(debugLabel: 'Km1StepFlow heading');

  @override
  void didUpdateWidget(covariant Km1StepFlow oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.active != widget.active) {
      WidgetsBinding.instance.addPostFrameCallback((_) {
        if (mounted) _heading.requestFocus();
      });
    }
  }

  @override
  void dispose() {
    _heading.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final c = context.km1;
    final steps = widget.steps;
    final idx = steps.indexWhere((s) => s.id == widget.active).clamp(0, steps.length - 1);
    final last = idx == steps.length - 1;
    final wide = MediaQuery.sizeOf(context).width >= 640;
    Widget marker(int i, String state) {
      final isCur = state == 'current';
      return Container(
        width: 24,
        height: 24,
        alignment: Alignment.center,
        decoration: BoxDecoration(
          shape: BoxShape.circle,
          color: isCur ? c.brand : (state == 'error' ? c.dangerTint : c.surface),
          border: isCur || state == 'error' ? null : Border.all(color: state == 'done' ? c.brandInk : c.strokeStrong),
        ),
        child: state == 'error'
            ? Icon(Km1Icons.statusError16, size: Km1Size.iconSm, color: c.dangerInk)
            : state == 'done'
                ? Km1BIcon(Km1BIconName.check, size: Km1Size.iconSm, color: c.brandInk)
                : Text('${i + 1}', style: Km1Text.caption1.copyWith(color: isCur ? c.onBrand : c.inkSecondary, fontWeight: FontWeight.w600)),
      );
    }

    final items = <Widget>[];
    for (var i = 0; i < steps.length; i++) {
      final s = steps[i];
      final isCur = i == idx;
      final state = widget.errors.contains(s.id) ? 'error' : isCur ? 'current' : widget.completed.contains(s.id) ? 'done' : 'todo';
      final srState = {'error': 'エラーあり', 'current': '現在の手順', 'done': '完了', 'todo': '未完了'}[state]!;
      final canJump = !isCur && (widget.linear ? (state == 'done' && s.editable) : true);
      final row = ConstrainedBox(
        constraints: BoxConstraints(minHeight: context.km1Target),
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: Km1Space.sm, vertical: Km1Space.xs),
          child: Row(mainAxisSize: MainAxisSize.min, children: [
            ExcludeSemantics(child: marker(i, state)),
            const SizedBox(width: Km1Space.sm),
            Text(s.title, style: (isCur ? Km1Text.body1Strong : Km1Text.body1).copyWith(color: state == 'todo' ? c.inkSecondary : c.ink)),
            if (s.optional) ...[const SizedBox(width: Km1Space.xs), Text('任意', style: Km1Text.caption1.copyWith(color: c.inkSecondary))],
          ]),
        ),
      );
      items.add(Semantics(
        label: '${s.title}（${i + 1} / ${steps.length}、$srState）',
        button: canJump,
        excludeSemantics: true,
        child: canJump ? InkWell(onTap: () => widget.onStepChange?.call(s.id), borderRadius: BorderRadius.circular(Km1Radius.md), child: row) : row,
      ));
    }
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, mainAxisSize: MainAxisSize.min, children: [
      wide
          ? Wrap(crossAxisAlignment: WrapCrossAlignment.center, spacing: Km1Space.xs, children: [
              for (var i = 0; i < items.length; i++) ...[
                if (i > 0) SizedBox(width: Km1Space.xxl, child: Divider(color: c.stroke, height: 1)),
                items[i],
              ],
            ])
          : Column(crossAxisAlignment: CrossAxisAlignment.start, children: items),
      const SizedBox(height: Km1Space.xxl),
      Focus(
        focusNode: _heading,
        child: Semantics(
          header: true,
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text('手順 ${idx + 1} / ${steps.length}', style: Km1Text.caption1.copyWith(color: c.inkSecondary)),
            Text(steps[idx].title, style: Km1Text.subtitle1.copyWith(color: c.ink)),
          ]),
        ),
      ),
      const SizedBox(height: Km1Space.lg),
      widget.child,
      const SizedBox(height: Km1Space.xxl),
      Km1FormActions(children: [
        if (idx > 0) OutlinedButton(onPressed: widget.onBack, child: const Text('戻る')),
        FilledButton(onPressed: last ? widget.onFinish : widget.onNext, child: Text(last ? widget.finishLabel : '次へ')),
      ]),
    ]);
  }
}

/// 下から出すシート。スマホは下から、幅 640 以上は中央のダイアログ。引っ張る操作に頼らず「閉じる」を必ず置く。
/// Bottom sheet on phones, a centered dialog at 640+; always has a close button instead of relying on drag.
Future<T?> showKm1BottomSheet<T>({required BuildContext context, required String title, required WidgetBuilder builder, List<Widget>? actions}) {
  final wide = MediaQuery.sizeOf(context).width >= 640;
  Widget sheet(BuildContext ctx) {
    final c = ctx.km1;
    return SafeArea(
      top: false,
      child: Column(mainAxisSize: MainAxisSize.min, crossAxisAlignment: CrossAxisAlignment.stretch, children: [
        Padding(
          padding: const EdgeInsets.fromLTRB(Km1Space.lg, Km1Space.sm, Km1Space.sm, Km1Space.xs),
          child: Row(children: [
            Expanded(child: Semantics(header: true, child: Text(title, style: Km1Text.subtitle2.copyWith(color: c.ink)))),
            IconButton(tooltip: '閉じる', onPressed: () => Navigator.of(ctx).pop(), icon: const Km1BIcon(Km1BIconName.dismiss, size: Km1Size.iconSm, inherit: true)),
          ]),
        ),
        Divider(height: 1, color: c.strokeSubtle),
        Flexible(child: SingleChildScrollView(padding: const EdgeInsets.symmetric(horizontal: Km1Space.lg, vertical: Km1Space.sm), child: builder(ctx))),
        if (actions != null) ...[
          Divider(height: 1, color: c.strokeSubtle),
          Padding(padding: const EdgeInsets.all(Km1Space.md), child: Km1FormActions(children: actions)),
        ],
      ]),
    );
  }

  if (wide) {
    return showDialog<T>(context: context, builder: (ctx) => Dialog(child: ConstrainedBox(constraints: const BoxConstraints(maxWidth: 480, maxHeight: 640), child: sheet(ctx))));
  }
  return showModalBottomSheet<T>(
    context: context,
    isScrollControlled: true,
    useSafeArea: true,
    showDragHandle: false,
    shape: const RoundedRectangleBorder(borderRadius: BorderRadius.vertical(top: Radius.circular(Km1Radius.xl))),
    constraints: BoxConstraints(maxHeight: MediaQuery.sizeOf(context).height * 0.6),
    builder: sheet,
  );
}

/// 画像の格子の 1 枚 / One tile in Km1ImageGrid
class Km1ImageItem {
  const Km1ImageItem({required this.id, required this.image, required this.alt, this.caption, this.meta});

  final Object id;
  final ImageProvider image;
  final String alt;
  final String? caption;
  final String? meta;
}

/// 見た目で見分ける画像・ファイルの格子。タイル全体が主操作、選択のチェックは別の押し場所。縦にだけスクロール。
/// A grid of images: the tile is the primary action; the selection checkbox is a separate target; vertical scrolling only.
class Km1ImageGrid extends StatelessWidget {
  const Km1ImageGrid({super.key, required this.items, this.onOpen, this.selectable = false, this.selected = const {}, this.onSelectionChanged, this.minTileWidth = 160, this.aspectRatio = 4 / 3});

  final List<Km1ImageItem> items;
  final ValueChanged<Km1ImageItem>? onOpen;
  final bool selectable;
  final Set<Object> selected;
  final ValueChanged<Set<Object>>? onSelectionChanged;
  final double minTileWidth;
  final double aspectRatio;

  @override
  Widget build(BuildContext context) {
    final c = context.km1;
    return GridView.builder(
      shrinkWrap: true,
      physics: const NeverScrollableScrollPhysics(),
      gridDelegate: SliverGridDelegateWithMaxCrossAxisExtent(maxCrossAxisExtent: minTileWidth * 1.6, mainAxisSpacing: Km1Space.sm, crossAxisSpacing: Km1Space.sm, childAspectRatio: aspectRatio * 0.78),
      itemCount: items.length,
      itemBuilder: (context, i) {
        final it = items[i];
        final on = selected.contains(it.id);
        final tile = Container(
          decoration: BoxDecoration(
            color: c.surface,
            border: Border.all(color: on ? c.brand : c.strokeSubtle, width: on ? 2 : 1),
            borderRadius: BorderRadius.circular(Km1Radius.md),
          ),
          clipBehavior: Clip.antiAlias,
          child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
            Expanded(
              child: Image(
                image: it.image,
                fit: BoxFit.cover,
                semanticLabel: it.alt,
                errorBuilder: (context, error, stack) => Container(
                  color: c.surfaceSubtle,
                  alignment: Alignment.center,
                  child: Column(mainAxisSize: MainAxisSize.min, children: [
                    Km1BIcon(Km1BIconName.image, size: Km1Size.iconSm, color: c.inkSecondary),
                    Text('画像を表示できません', style: Km1Text.caption1.copyWith(color: c.inkSecondary)),
                  ]),
                ),
              ),
            ),
            if (it.caption != null || it.meta != null)
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: Km1Space.md, vertical: Km1Space.sm),
                child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                  if (it.caption != null) Text(it.caption!, style: Km1Text.body1.copyWith(color: c.ink)),
                  if (it.meta != null) Text(it.meta!, style: Km1Text.caption1.copyWith(color: c.inkSecondary)),
                ]),
              ),
          ]),
        );
        return Stack(children: [
          Positioned.fill(child: onOpen == null ? tile : InkWell(onTap: () => onOpen!(it), borderRadius: BorderRadius.circular(Km1Radius.md), child: tile)),
          if (selectable)
            Positioned(
              top: Km1Space.xs,
              left: Km1Space.xs,
              child: Container(
                width: context.km1Target,
                height: context.km1Target,
                decoration: BoxDecoration(color: c.surface, borderRadius: BorderRadius.circular(Km1Radius.md)),
                child: Checkbox(
                  value: on,
                  semanticLabel: '${it.caption ?? it.alt} を選択',
                  onChanged: (v) {
                    final next = {...selected};
                    if (v ?? false) {
                      next.add(it.id);
                    } else {
                      next.remove(it.id);
                    }
                    onSelectionChanged?.call(next);
                  },
                ),
              ),
            ),
        ]);
      },
    );
  }
}


// ---------------------------------------------------------------------------
// 分類の模様（KM1-COL-001）/ Category patterns
// 分類は「色 × 模様」で区別する。模様は文字の下に描かない: しるし・凡例・グラフの塗りだけ。
// Categories are color × pattern. Never under text: marks, legends and chart fills only.
// ---------------------------------------------------------------------------

enum Km1Pattern { solid, horizontal, vertical, diagonal, grid, crosshatch, dots, checker }

extension Km1PatternLabel on Km1Pattern {
  String get labelJa => const {
        Km1Pattern.solid: '塗り', Km1Pattern.horizontal: '横線', Km1Pattern.vertical: '縦線', Km1Pattern.diagonal: '斜線',
        Km1Pattern.grid: '格子', Km1Pattern.crosshatch: '斜め格子', Km1Pattern.dots: '点', Km1Pattern.checker: '市松',
      }[this]!;
}

/// 既定の割り当て順。隣どうしで明るさと模様が両方変わる（Web の categoryStyle と同じ）
/// Default order; matches the web categoryStyle()
const List<Color> km1CategoryOrder = [
  Km1Category.blue, Km1Category.marigold, Km1Category.teal, Km1Category.pumpkin, Km1Category.grape, Km1Category.lime,
  Km1Category.cranberry, Km1Category.cyan, Km1Category.brown, Km1Category.pink, Km1Category.green, Km1Category.berry,
  Km1Category.cornflower, Km1Category.darkOrange, Km1Category.purple, Km1Category.seafoam, Km1Category.red, Km1Category.gray,
];
({Color color, Km1Pattern pattern}) km1CategoryStyleAt(int i) =>
    (color: km1CategoryOrder[i % km1CategoryOrder.length], pattern: Km1Pattern.values[i % Km1Pattern.values.length]);

/// 模様を描く。pitch はしるしで 4、グラフの塗りで 8 / Paints a pattern; pitch 4 for marks, 8 for chart fills
class Km1PatternPainter extends CustomPainter {
  const Km1PatternPainter({required this.color, required this.pattern, required this.background, this.pitch = 4});
  final Color color;
  final Km1Pattern pattern;
  final Color background;
  final double pitch;

  @override
  void paint(Canvas canvas, Size size) {
    final r = Offset.zero & size;
    canvas.save();
    canvas.clipRect(r);
    canvas.drawRect(r, Paint()..color = background);
    final fill = Paint()..color = color;
    final w = pitch >= 8 ? 3.0 : 2.0;
    final line = Paint()
      ..color = color
      ..strokeWidth = w;
    final thin = Paint()
      ..color = color
      ..strokeWidth = 1;
    switch (pattern) {
      case Km1Pattern.solid:
        canvas.drawRect(r, fill);
      case Km1Pattern.horizontal:
        for (var y = 0.0; y < size.height; y += pitch) {
          canvas.drawRect(Rect.fromLTWH(0, y, size.width, w), fill);
        }
      case Km1Pattern.vertical:
        for (var x = 0.0; x < size.width; x += pitch) {
          canvas.drawRect(Rect.fromLTWH(x, 0, w, size.height), fill);
        }
      case Km1Pattern.diagonal: // 右下がり。仮の予定の右上がりの斜線と向きを変える / falls to the right, unlike the tentative hatch
        for (var x = -size.height; x < size.width; x += pitch * .75) {
          canvas.drawLine(Offset(x, 0), Offset(x + size.height, size.height), line..strokeWidth = w * .8);
        }
      case Km1Pattern.grid:
        for (var y = 0.0; y < size.height; y += pitch) {
          canvas.drawRect(Rect.fromLTWH(0, y, size.width, 1), fill);
        }
        for (var x = 0.0; x < size.width; x += pitch) {
          canvas.drawRect(Rect.fromLTWH(x, 0, 1, size.height), fill);
        }
      case Km1Pattern.crosshatch:
        for (var x = -size.height; x < size.width; x += pitch * .75) {
          canvas.drawLine(Offset(x, 0), Offset(x + size.height, size.height), thin);
          canvas.drawLine(Offset(x, size.height), Offset(x + size.height, 0), thin);
        }
      case Km1Pattern.dots:
        for (var y = pitch / 2; y < size.height; y += pitch) {
          for (var x = pitch / 2; x < size.width; x += pitch) {
            canvas.drawCircle(Offset(x, y), 1.1, fill);
          }
        }
      case Km1Pattern.checker:
        for (var y = 0.0, row = 0; y < size.height; y += pitch, row++) {
          for (var x = (row.isOdd ? pitch : 0.0); x < size.width; x += pitch * 2) {
            canvas.drawRect(Rect.fromLTWH(x, y, pitch, pitch), fill);
          }
        }
    }
    canvas.restore();
  }

  @override
  bool shouldRepaint(Km1PatternPainter old) => old.color != color || old.pattern != pattern || old.background != background || old.pitch != pitch;
}

/// 分類のしるし（16px か 20px）。横に分類名があるときは label を付けない
/// Category mark (16 or 20px). Omit label when the name sits next to it.
class Km1CategoryMark extends StatelessWidget {
  const Km1CategoryMark({super.key, required this.color, required this.pattern, this.size = Km1Size.iconSm, this.label});
  final Color color;
  final Km1Pattern pattern;
  final double size;
  final String? label;

  @override
  Widget build(BuildContext context) {
    final c = context.km1;
    final hc = MediaQuery.highContrastOf(context);
    final mark = Container(
      width: size,
      height: size,
      decoration: BoxDecoration(border: Border.all(color: hc ? c.ink : c.strokeStrong), borderRadius: BorderRadius.circular(Km1Radius.sm)),
      clipBehavior: Clip.antiAlias,
      child: CustomPaint(painter: Km1PatternPainter(color: hc ? c.ink : color, pattern: pattern, background: c.surface)),
    );
    if (label == null) return ExcludeSemantics(child: mark);
    return Semantics(label: '$label（${pattern.labelJa}）', image: true, child: ExcludeSemantics(child: mark));
  }
}

class Km1LegendEntry {
  const Km1LegendEntry(this.label, {this.color, this.pattern});
  final String label;
  final Color? color;
  final Km1Pattern? pattern;
}

/// 凡例。色と模様を省くと km1CategoryStyleAt の順で割り当てる / Legend; unset entries use km1CategoryStyleAt order
class Km1CategoryLegend extends StatelessWidget {
  const Km1CategoryLegend({super.key, required this.entries, this.vertical = false, this.label = '凡例'});
  final List<Km1LegendEntry> entries;
  final bool vertical;
  final String label;

  @override
  Widget build(BuildContext context) {
    final c = context.km1;
    final items = [
      for (var i = 0; i < entries.length; i++)
        Row(mainAxisSize: MainAxisSize.min, children: [
          Km1CategoryMark(color: entries[i].color ?? km1CategoryStyleAt(i).color, pattern: entries[i].pattern ?? km1CategoryStyleAt(i).pattern),
          const SizedBox(width: Km1Space.sm),
          Text(entries[i].label, style: Km1Text.body1.copyWith(color: c.ink)),
        ]),
    ];
    return Semantics(
      container: true,
      label: label,
      child: vertical
          ? Column(crossAxisAlignment: CrossAxisAlignment.start, children: [for (final w in items) Padding(padding: const EdgeInsets.only(bottom: Km1Space.xs), child: w)])
          : Wrap(spacing: Km1Space.lg, runSpacing: Km1Space.sm, children: items),
    );
  }
}
