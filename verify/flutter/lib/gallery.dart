// KM1 の検証用ギャラリー / KM1 verification gallery
import 'package:flutter/material.dart';
import 'km1_theme.dart';
import 'km1_icons.dart';
import 'km1_icons_b.dart';
import 'km1_widgets.dart';

class Km1Gallery extends StatefulWidget {
  const Km1Gallery({super.key});
  @override
  State<Km1Gallery> createState() => _Km1GalleryState();
}

class _Km1GalleryState extends State<Km1Gallery> {
  bool chip = true;
  int page = 1;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('KM1 検証')),
      body: ListView(padding: const EdgeInsets.all(Km1Space.lg), children: [
        const Km1Breadcrumb(items: [Km1BreadcrumbItem('ホーム'), Km1BreadcrumbItem('予定')]),
        const SizedBox(height: Km1Space.lg),
        Wrap(spacing: Km1Space.sm, runSpacing: Km1Space.sm, children: [
          FilledButton(onPressed: () {}, child: const Text('予定を追加')),
          OutlinedButton(onPressed: () {}, child: const Text('キャンセル')),
          Km1FilterChip(label: '授業', selected: chip, onSelected: (v) => setState(() => chip = v)),
          const Km1Avatar(name: '山田'),
        ]),
        const SizedBox(height: Km1Space.lg),
        const Km1Progress(label: '取り込み中', value: 0.4),
        const SizedBox(height: Km1Space.lg),
        const Km1Skeleton(),
        const SizedBox(height: Km1Space.lg),
        Km1ListItem(title: '物理化学', description: '2 限 10:00〜11:40', leading: const Km1BIcon(Km1BIconName.school), onTap: () {}),
        Km1ListItem(title: '締め切り: レポート', description: '23:59', leading: const Km1BIcon(Km1BIconName.deadline, filled: true), onTap: () {}),
        const SizedBox(height: Km1Space.lg),
        const Km1CategoryLegend(entries: [
          Km1LegendEntry('授業', color: Km1Category.blue, pattern: Km1Pattern.solid),
          Km1LegendEntry('バイト', color: Km1Category.cyan, pattern: Km1Pattern.horizontal),
        ]),
        const SizedBox(height: Km1Space.lg),
        Km1Pagination(page: page, count: 5, onChanged: (p) => setState(() => page = p)),
        const SizedBox(height: Km1Space.lg),
        const Km1EmptyState(title: '今日の予定はありません', body: '明日は 9:00 から気象学（W5-201）です。'),
        const SizedBox(height: Km1Space.lg),
        const Km1IconSheet(),
      ]),
    );
  }
}

/// 全アイコン（B 案の通常と塗り、フォントの字形）/ every icon: B regular, B filled, font glyph
class Km1IconSheet extends StatelessWidget {
  const Km1IconSheet({super.key, this.size = 20});
  final double size;
  @override
  Widget build(BuildContext context) {
    return Wrap(spacing: 6, runSpacing: 6, children: [
      for (final n in Km1BIconName.values)
        SizedBox(
          width: size * 3 + 12,
          child: Row(mainAxisSize: MainAxisSize.min, children: [
            Km1BIcon(n, size: size),
            const SizedBox(width: 2),
            Km1BIcon(n, size: size, filled: true),
          ]),
        ),
      const Icon(Km1Icons.calendar, size: 20),
    ]);
  }
}
