// 部品のギャラリーを、スマホと PC の幅、ライトとダークで組み立てて、例外や はみ出しがないかを見る。
// アイコンの一覧は、承認済みの画像（test/goldens/）と比べる。違えば失敗する（回帰の検査）。
// 画像を作り直すのは、GitHub の「goldens」ワークフローを手で動かしたときだけ（verification.md 6 章）。
// Builds the gallery at phone and desktop widths in light and dark; icon sheets are compared against approved goldens.
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:km1_verify/km1_theme.dart';
import 'package:km1_verify/gallery.dart';

Future<void> run(WidgetTester t, Size size, ThemeData theme) async {
  t.view.physicalSize = size;
  t.view.devicePixelRatio = 1;
  addTearDown(t.view.reset);
  await t.pumpWidget(MaterialApp(theme: theme, home: const Km1Gallery()));
  await t.pump();
  await t.pump(const Duration(milliseconds: 600)); // 読み込み中の動きは止まらないので、時間を決めて進める / animations loop, so advance a fixed time
  expect(t.takeException(), isNull);
}

void main() {
  // テストでは pubspec の書体が自動では読み込まれず、字形のアイコン（塗りと Km1Icons）が四角（豆腐）になる。
  // ここで KM1Icons を読み込む / Widget tests don't load pubspec fonts; load KM1Icons so glyph icons aren't tofu
  setUpAll(() async {
    final loader = FontLoader('KM1Icons')..addFont(rootBundle.load('fonts/KM1Icons.ttf'));
    await loader.load();
  });
  for (final dark in [false, true]) {
    final theme = dark ? Km1Theme.dark() : Km1Theme.light();
    final tag = dark ? 'dark' : 'light';
    testWidgets('スマホ幅 390・$tag', (t) => run(t, const Size(390, 844), theme));
    testWidgets('PC 幅 1280・$tag', (t) => run(t, const Size(1280, 800), theme));
    for (final s in [16.0, 20.0, 24.0]) {
      testWidgets('アイコンの一覧の画像 ${s.toInt()}px・$tag', tags: ['golden'], (t) async {
        t.view.physicalSize = const Size(1100, 760);
        t.view.devicePixelRatio = 1;
        addTearDown(t.view.reset);
        await t.pumpWidget(MaterialApp(
          debugShowCheckedModeBanner: false,
          theme: theme,
          home: Scaffold(body: Padding(padding: const EdgeInsets.all(12), child: RepaintBoundary(key: const ValueKey('sheet'), child: Km1IconSheet(size: s)))),
        ));
        await expectLater(find.byKey(const ValueKey('sheet')), matchesGoldenFile('goldens/icons_${s.toInt()}_$tag.png'));
      });
    }
  }
}
