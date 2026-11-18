// アイコンのファイルが km1_theme.dart・km1_icons.dart だけで組み込めるか（km1_widgets.dart を読み込まない）
// The icon files build and render with only km1_theme.dart and km1_icons.dart (no km1_widgets.dart).
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:km1_verify/km1_theme.dart';
import 'package:km1_verify/km1_icons.dart';
import 'package:km1_verify/km1_icons_b.dart';

Widget sheet({ThemeData? theme}) => MaterialApp(
      theme: theme,
      home: Scaffold(
        body: SingleChildScrollView(
          child: Wrap(children: [
            for (final s in [16.0, 20.0, 24.0, 32.0])
              for (final n in Km1BIconName.values) ...[
                Km1BIcon(n, size: s),
                Km1BIcon(n, size: s, filled: true),
                Km1BIcon(n, size: s, inherit: true),
                Km1BIcon(n, size: s, color: Colors.red),
              ],
            const Icon(Km1Icons.calendar),
          ]),
        ),
      ),
    );

void main() {
  testWidgets('全アイコン・ライト / all icons, light theme', (t) async {
    await t.pumpWidget(sheet(theme: Km1Theme.light()));
    expect(t.takeException(), isNull);
    expect(find.byType(Km1BIcon), findsNWidgets(Km1BIconName.values.length * 16));
  });
  testWidgets('全アイコン・ダーク / all icons, dark theme', (t) async {
    await t.pumpWidget(sheet(theme: Km1Theme.dark()));
    expect(t.takeException(), isNull);
  });
  testWidgets('KM1 のテーマがなくても出る / works without the KM1 theme', (t) async {
    await t.pumpWidget(sheet());
    expect(t.takeException(), isNull);
  });
  testWidgets('名前を付けると読み上げに出る / semanticLabel is exposed', (t) async {
    await t.pumpWidget(MaterialApp(theme: Km1Theme.light(), home: const Km1BIcon(Km1BIconName.deadline, semanticLabel: '締め切り')));
    expect(find.bySemanticsLabel('締め切り'), findsOneWidget);
  });
}
