import json,re
import os as _os
_H=_os.path.dirname(_os.path.abspath(__file__))
P=_os.environ.get('KM1_PROJECT') or (_os.path.join(_H,'..','project') if _os.path.exists(_os.path.join(_H,'..','project','tokens.json')) else _os.path.join(_H,'..'))
P=_os.path.normpath(P)+'/'
t=json.load(open(P+'tokens.json'))
C={x['name']:x['value'] for x in t['color']['tokens']}
def resolve(n,th):
    v=C[n]; v=v if isinstance(v,str) else v.get(th,v['light'])
    m=re.fullmatch(r'\{(.+)\}',v)
    return resolve(m.group(1),th) if m else v
def camel(n):
    p=n.split('-'); return p[0]+''.join(w.capitalize() for w in p[1:])
def hexc(h):
    h=h.lstrip('#')
    if len(h)==3: h=''.join(c*2 for c in h)
    return 'Color(0xFF'+h.upper()+')'
sem=[n for n in C if not re.match(r'(gray|brand|blue|red|green|orange)-\d+$',n) and not n.startswith('cat-')]
cats=[n for n in C if n.startswith('cat-')]
px=lambda s:float(str(s).replace('px','') or 0)
o='''// KM1 km1_theme.dart — tokens.json から自動生成。直接編集しない。
// Generated from tokens.json; do not edit by hand.
//
// 使い方 / Usage:
//   MaterialApp(theme: Km1Theme.light(), darkTheme: Km1Theme.dark(), themeMode: ThemeMode.system, ...)
//   色は Theme.of(context).extension<Km1Colors>()! 経由で意味づけトークンを使う。
//   Use semantic tokens via Theme.of(context).extension<Km1Colors>()!.
//
// アイコンは KM1 のアイコン（km1_icons.dart の Km1Icons と KM1Icons.ttf）を使い、Icons.*（Material）は使わない。
// Use KM1 icons (Km1Icons in km1_icons.dart + KM1Icons.ttf); do not use Icons.* (Material).
// Material は土台として使うだけで、見た目は下のテーマで上書きする。
// Material is only the base widget layer; the look is overridden below.

import 'package:flutter/foundation.dart' show defaultTargetPlatform;
import 'package:flutter/material.dart';
// Flutter 3.50 から material.dart が Cupertino の画面切り替えを含まないため、直接読む / Flutter 3.50+ no longer re-exports it from material.dart
import 'package:flutter/cupertino.dart' show CupertinoPageTransitionsBuilder;

'''
# colors
o+='@immutable\nclass Km1Colors extends ThemeExtension<Km1Colors> {\n  const Km1Colors({\n'
o+=''.join(f'    required this.{camel(n)},\n' for n in sem)+'  });\n\n'
o+=''.join(f'  final Color {camel(n)};\n' for n in sem)
for th in('light','dark'):
    o+=f'\n  static const Km1Colors {th} = Km1Colors(\n'+''.join(f'    {camel(n)}: {hexc(resolve(n,th))},\n' for n in sem)+'  );\n'
o+='\n  @override\n  Km1Colors copyWith({\n'+''.join(f'    Color? {camel(n)},\n' for n in sem)+'  }) =>\n      Km1Colors(\n'+''.join(f'        {camel(n)}: {camel(n)} ?? this.{camel(n)},\n' for n in sem)+'      );\n'
o+='\n  @override\n  Km1Colors lerp(ThemeExtension<Km1Colors>? other, double t) {\n    if (other is! Km1Colors) return this;\n    return Km1Colors(\n'+''.join(f'      {camel(n)}: Color.lerp({camel(n)}, other.{camel(n)}, t)!,\n' for n in sem)+'    );\n  }\n}\n\n'
# spacing/radius
o+='abstract final class Km1Space {\n'+''.join(f'  static const double {camel(x["name"][6:] or "none") if False else camel(x["name"].replace("space-","",1))} = {px(x["value"])};\n' for x in t['spacing']['tokens'])+'}\n\n'

# 用途別エイリアス（KM1-TOK-001）: 基本トークンを指す / role aliases point to base tokens
def _rk(ref):
    return 'Km1Space.'+camel(ref.replace('space-','',1)) if ref.startswith('space-') else 'Km1Size.'+camel(ref)
o+='/// 用途別の余白（KM1-TOK-001）。新しい値ではなく Km1Space を指す。/ Role spacing aliases pointing to Km1Space.\n'
o+='abstract final class Km1SpaceRole {\n'+''.join(f'  static const double {camel(x["name"])} = {_rk(x["ref"])};\n' for x in t['spacingRole']['tokens'])+'}\n\n'
o+="""/// 密度（KM1-TOK-001-C）。Card・Table・SortableList だけに使う。操作領域は変えない。
/// Density for Card, Table and SortableList only; never changes hit areas.
enum Km1Density {
  compact,
  regular,
  spacious;

  /// コンテナ（Card）の内側の余白 / Container (Card) padding
  double get containerPadding => switch (this) {
        Km1Density.compact => Km1SpaceRole.containerCardPaddingCompact,
        Km1Density.regular => Km1SpaceRole.containerCardPaddingRegular,
        Km1Density.spacious => Km1SpaceRole.containerCardPaddingSpacious,
      };

  /// 集合部品の項目の間 / Gap between collection items
  double get itemGap => switch (this) {
        Km1Density.compact => Km1SpaceRole.collectionItemGapCompact,
        Km1Density.regular => Km1SpaceRole.collectionItemGapRegular,
        Km1Density.spacious => Km1SpaceRole.collectionItemGapSpacious,
      };

  /// 表の行の最小の高さ。compact は中身に合わせる（操作部品のある行は、その部品の高さが残る）。
  /// Minimum table row height; compact follows content (rows with controls keep the control's height).
  double rowMinHeight(double target) => switch (this) {
        Km1Density.compact => 0,
        Km1Density.regular => target,
        Km1Density.spacious => target + Km1Space.sm,
      };
}

"""
o+='abstract final class Km1Radius {\n'
for x in t['radius']['tokens']:
    n=camel(x['name'].replace('radius-','',1)); v=px(x['value'])
    o+=f'  static const double {n} = {v};\n'
o+='}\n\n'
# shadows
def sh(s):
    out=[]
    for part in re.findall(r'(-?\d+)(?:px)?\s+(-?\d+)(?:px)?\s+(\d+)(?:px)?(?:\s+(-?\d+)(?:px)?)?\s+rgba\(0,0,0,([\d.]+)\)',s):
        dx,dy,b,_,a=part
        out.append(f'BoxShadow(color: Color.fromRGBO(0, 0, 0, {a}), offset: Offset({float(dx)}, {float(dy)}), blurRadius: {float(b)})')
    return out
o+='abstract final class Km1Shadow {\n'
for x in t['shadow']['tokens']:
    n=camel(x['name']); l=sh(x['value'])
    assert l,x
    o+=f'  static const List<BoxShadow> {n} = [\n'+''.join(f'    {i},\n' for i in l)+'  ];\n'
o+='}\n\n'
# text
fs={}
o+='abstract final class Km1Text {\n  static const String fontFamily = \'Noto Sans JP\';\n  static const List<String> fontFamilyFallback = [\'Hiragino Sans\', \'Yu Gothic UI\', \'Meiryo UI\', \'Noto Sans CJK JP\', \'Segoe UI\'];\n'
for g in t['type']['groups']:
    for s in g['styles']:
        n=camel(s['name']); size=px(s['fontSize']); lh=px(s['lineHeight'])
        o+=f'  static const TextStyle {n} = TextStyle(\n    fontFamily: fontFamily,\n    fontFamilyFallback: fontFamilyFallback,\n    fontSize: {size},\n    height: {lh}/{size},\n    fontWeight: FontWeight.w{s["fontWeight"]},\n  );\n'
o+='}\n\n'

S={x['name']:x['value'] for x in t['size']['tokens']}
o+='/// アイコン・線・幅 / Icon sizes, stroke widths, widths\nabstract final class Km1Size {\n'+''.join(f'  static const double {camel(n)} = {px(v)};\n' for n,v in S.items() if not n.startswith('breakpoint'))+'}\n\n'
o+='/// 画面幅の区切り（Fluent 2 の size class）/ Breakpoints (Fluent 2 size classes)\nabstract final class Km1Breakpoint {\n'+''.join(f'  static const double {camel(n.replace("breakpoint-",""))} = {px(v)};\n' for n,v in S.items() if n.startswith('breakpoint'))
o+="""
  /// 編集をダイアログで開く幅か / Wide enough to edit in a dialog
  static bool useDialog(BuildContext context) => MediaQuery.sizeOf(context).width >= lg;

  /// サイドバーを常時表示する幅か / Wide enough for a persistent sidebar
  static bool useSidebar(BuildContext context) => MediaQuery.sizeOf(context).width >= xl;
}

/// 動き / Motion（Fluent 2 の duration・curve）
abstract final class Km1Motion {
  /// hover・pressed の色の変化 / Hover and pressed color changes
  static const Duration faster = Duration(milliseconds: 100);

  /// スイッチ・下線・チェックの切り替え / Switch, underline, check toggles
  static const Duration fast = Duration(milliseconds: 150);

  /// ダイアログ・ポップオーバー・画面の出入り / Dialog, popover and screen transitions
  static const Duration normal = Duration(milliseconds: 200);

  static const Curve easyEase = Cubic(0.33, 0, 0.67, 1);

  /// 現れるとき / Entering
  static const Curve decelerate = Cubic(0, 0, 0, 1);

  /// 消えるとき / Exiting
  static const Curve accelerate = Cubic(1, 0, 1, 1);

  /// 出入りで動かしてよい距離の上限 / Max travel for enter and exit
  static const double maxShift = 8;
}

/// 分類色 / Category colors — 帯と淡い塗りだけに使い、文字には使わない。
abstract final class Km1Category {
"""
o+=''.join(f'  static const Color {camel(n[4:])} = {hexc(resolve(n,"light"))};\n' for n in cats)
o+='  static const List<Color> all = ['+', '.join(camel(n[4:]) for n in cats)+'];\n'
o+="""
  /// 淡い塗り（ライト 14%、ダーク 32%）/ Tint fill (14% light, 32% dark)
  static Color tint(Color c, Brightness b) => c.withValues(alpha: b == Brightness.dark ? 0.32 : 0.14);
}

/// 暗幕 / Scrim
const Color kKm1Scrim = Color(0x66000000);

"""
o+='/// OS ごとの操作領域の最小値（KM1-TOK-001-D）。名前と意味は共通、値は OS ごと。/ Minimum hit area per OS.\n'
o+='abstract final class Km1PlatformTarget {\n'+''.join(f'  static const double {camel(x["name"].replace("control-target-","",1))} = {_rk(x["ref"])};\n' for x in t['platformTarget']['tokens'])+'}\n\n'
o+='''/// 操作領域 / Hit areas (WCAG 2.2 2.5.5 AAA = 44, 2.5.8 AA = 24)
const double kKm1Target = Km1Space.target;
const double kKm1TargetCompact = Km1Space.targetCompact;

abstract final class Km1Theme {
  /// 端末ごとの部品の高さ / Control height per platform
  /// Android 48dp（Android の推奨）、iOS・iPadOS 44pt（Apple HIG）、
  /// Windows・macOS・Linux 32px（Fluent Compact、マウス中心）。
  /// Android 48dp, iOS/iPadOS 44pt, desktop 32px (Fluent Compact, pointer-first).
  static double targetFor(TargetPlatform p) {
    switch (p) {
      case TargetPlatform.android:
      case TargetPlatform.fuchsia:
        return Km1PlatformTarget.android;
      case TargetPlatform.iOS:
        return Km1PlatformTarget.ios;
      case TargetPlatform.macOS:
        return Km1PlatformTarget.macos;
      default:
        return Km1PlatformTarget.windows;
    }
  }

  /// タッチ操作が主な端末か（iOS・Android）。Web でも端末の OS で決まる。
  /// Whether touch is the main input (iOS, Android); on the web it follows the device OS.
  static bool get isTouch =>
      defaultTargetPlatform == TargetPlatform.iOS || defaultTargetPlatform == TargetPlatform.android;

  /// [touch] を省くと端末から決める。[touch] が true なら少なくとも 44（Windows のタブレット姿勢など）。
  /// Omit [touch] to decide from the platform; touch: true forces at least 44 (e.g. Windows tablet posture).
  static ThemeData light({bool? touch}) => _build(Km1Colors.light, Brightness.light, touch);
  static ThemeData dark({bool? touch}) => _build(Km1Colors.dark, Brightness.dark, touch);

  static ThemeData _build(Km1Colors c, Brightness b, bool? touchOverride) {
    final platform = defaultTargetPlatform;
    final bool touch = touchOverride ?? isTouch;
    final double platformTarget = targetFor(platform);
    final double target = touch ? (platformTarget < kKm1Target ? kKm1Target : platformTarget) : platformTarget;
    final double fieldSize = touch ? 16 : 14;
    final tapSize = touch ? MaterialTapTargetSize.padded : MaterialTapTargetSize.shrinkWrap;
    final scheme = ColorScheme(
      brightness: b,
      primary: c.brand,
      onPrimary: c.onBrand,
      secondary: c.brandInk,
      onSecondary: c.surface,
      error: c.danger,
      onError: c.onBrand,
      surface: c.surface,
      onSurface: c.ink,
      outline: c.strokeStrong,
      outlineVariant: c.stroke,
    );
    final minTarget = Size(target, target);
    final shape = RoundedRectangleBorder(borderRadius: BorderRadius.circular(Km1Radius.md));
    final focusSide = BorderSide(color: c.focusRing, width: 2);

    OutlineInputBorder border(Color color, [double w = 1]) => OutlineInputBorder(
          borderRadius: BorderRadius.circular(Km1Radius.md),
          borderSide: BorderSide(color: color, width: w),
        );

    return ThemeData(
      useMaterial3: true,
      brightness: b,
      colorScheme: scheme,
      scaffoldBackgroundColor: c.surface,
      canvasColor: c.surface,
      fontFamily: Km1Text.fontFamily,
      fontFamilyFallback: Km1Text.fontFamilyFallback,
      // 画面の切り替え: iOS・macOS は端からのスワイプで戻れる Cupertino の動き、ほかは Flutter の既定。
      // Page transitions: Cupertino (edge-swipe back) on iOS and macOS; Flutter defaults elsewhere.
      pageTransitionsTheme: const PageTransitionsTheme(builders: {
        TargetPlatform.iOS: CupertinoPageTransitionsBuilder(),
        TargetPlatform.macOS: CupertinoPageTransitionsBuilder(),
      }),
      // Material のスプラッシュは使わず、状態は色の変化で示す。 / No ink splash; states are shown by color.
      splashFactory: NoSplash.splashFactory,
      highlightColor: Colors.transparent,
      textTheme: TextTheme(
        displayLarge: Km1Text.display.copyWith(color: c.ink),
        headlineLarge: Km1Text.largeTitle.copyWith(color: c.ink),
        headlineMedium: Km1Text.title.copyWith(color: c.ink),
        headlineSmall: Km1Text.title.copyWith(color: c.ink),
        titleLarge: Km1Text.subtitle1.copyWith(color: c.ink),
        titleMedium: Km1Text.subtitle1.copyWith(color: c.ink),
        titleSmall: Km1Text.subtitle2.copyWith(color: c.ink),
        // 入力中の文字は bodyLarge。スマホ 16px、PC 14px。 / Field text: 16px on touch, 14px on PC.
        bodyLarge: (touch ? Km1Text.body2 : Km1Text.body1).copyWith(color: c.ink),
        bodyMedium: Km1Text.body1.copyWith(color: c.ink),
        bodySmall: Km1Text.caption1.copyWith(color: c.inkSecondary),
        labelLarge: Km1Text.body1Strong.copyWith(color: c.ink),
        labelMedium: Km1Text.caption1.copyWith(color: c.inkSecondary),
        labelSmall: Km1Text.caption1.copyWith(color: c.inkSecondary),
      ),
      extensions: [c],
      dividerTheme: DividerThemeData(color: c.strokeSubtle, thickness: 1, space: 1),
      materialTapTargetSize: tapSize,
      visualDensity: VisualDensity.standard,
      focusColor: c.focusRing,
      hoverColor: c.surfaceHover,

      // ボタン / Buttons — 主 = 塗り、副 = 枠、三次 = 文字のみ。画面に主は 1 つ。
      filledButtonTheme: FilledButtonThemeData(
        style: ButtonStyle(
          minimumSize: WidgetStatePropertyAll(minTarget),
          padding: const WidgetStatePropertyAll(EdgeInsets.symmetric(horizontal: Km1Space.md)),
          shape: WidgetStatePropertyAll(shape),
          textStyle: const WidgetStatePropertyAll(Km1Text.body1Strong),
          foregroundColor: WidgetStateProperty.resolveWith((s) => s.contains(WidgetState.disabled) ? c.inkDisabled : c.onBrand),
          backgroundColor: WidgetStateProperty.resolveWith((s) {
            if (s.contains(WidgetState.disabled)) return c.surfaceMuted;
            if (s.contains(WidgetState.pressed)) return c.brandPressed;
            if (s.contains(WidgetState.hovered)) return c.brandHover;
            return c.brand;
          }),
          side: WidgetStateProperty.resolveWith((s) {
            if (s.contains(WidgetState.focused)) return focusSide;
            if (s.contains(WidgetState.disabled)) return BorderSide(color: c.stroke);
            return BorderSide(color: c.brandStroke);
          }),
          elevation: const WidgetStatePropertyAll(0),
        ),
      ),
      outlinedButtonTheme: OutlinedButtonThemeData(
        style: ButtonStyle(
          minimumSize: WidgetStatePropertyAll(minTarget),
          padding: const WidgetStatePropertyAll(EdgeInsets.symmetric(horizontal: Km1Space.md)),
          shape: WidgetStatePropertyAll(shape),
          textStyle: const WidgetStatePropertyAll(Km1Text.body1Strong),
          foregroundColor: WidgetStateProperty.resolveWith((s) => s.contains(WidgetState.disabled) ? c.inkDisabled : c.ink),
          backgroundColor: WidgetStateProperty.resolveWith((s) {
            if (s.contains(WidgetState.disabled)) return c.surface;
            if (s.contains(WidgetState.pressed)) return c.surfacePressed;
            if (s.contains(WidgetState.hovered)) return c.surfaceHover;
            return c.surface;
          }),
          side: WidgetStateProperty.resolveWith((s) {
            if (s.contains(WidgetState.focused)) return focusSide;
            return BorderSide(color: s.contains(WidgetState.disabled) ? c.stroke : c.strokeStrong);
          }),
        ),
      ),
      textButtonTheme: TextButtonThemeData(
        style: ButtonStyle(
          minimumSize: WidgetStatePropertyAll(minTarget),
          padding: const WidgetStatePropertyAll(EdgeInsets.symmetric(horizontal: Km1Space.md)),
          shape: WidgetStatePropertyAll(shape),
          textStyle: const WidgetStatePropertyAll(Km1Text.body1Strong),
          foregroundColor: WidgetStateProperty.resolveWith((s) => s.contains(WidgetState.disabled) ? c.inkDisabled : c.ink),
          backgroundColor: WidgetStateProperty.resolveWith((s) {
            if (s.contains(WidgetState.pressed)) return c.surfacePressed;
            if (s.contains(WidgetState.hovered)) return c.surfaceHover;
            return Colors.transparent;
          }),
          side: WidgetStateProperty.resolveWith((s) => s.contains(WidgetState.focused) ? focusSide : BorderSide.none),
        ),
      ),
      // ナビの選択中は、淡い紺の面・太字・塗りのアイコン（Web と同じ。線は足さない。D25・D33）
      // Nav selection: brand tint, bold label, filled icon (same as Web; no bar)
      navigationBarTheme: NavigationBarThemeData(
        backgroundColor: c.surface,
        surfaceTintColor: Colors.transparent,
        elevation: 0,
        height: 64,
        indicatorColor: c.brandTint,
        indicatorShape: const RoundedRectangleBorder(borderRadius: BorderRadius.all(Radius.circular(Km1Radius.md))),
        labelTextStyle: WidgetStateProperty.resolveWith((s) => s.contains(WidgetState.selected)
            ? Km1Text.caption1.copyWith(color: c.brandInk, fontWeight: FontWeight.w600)
            : Km1Text.caption1.copyWith(color: c.inkSecondary)),
        iconTheme: WidgetStateProperty.resolveWith((s) =>
            IconThemeData(size: Km1Size.iconLg, color: s.contains(WidgetState.selected) ? c.brandInk : c.inkSecondary)),
      ),
      navigationRailTheme: NavigationRailThemeData(
        backgroundColor: c.surface,
        elevation: 0,
        indicatorColor: c.brandTint,
        indicatorShape: const RoundedRectangleBorder(borderRadius: BorderRadius.all(Radius.circular(Km1Radius.md))),
        selectedIconTheme: IconThemeData(size: Km1Size.iconLg, color: c.brandInk),
        unselectedIconTheme: IconThemeData(size: Km1Size.iconLg, color: c.inkSecondary),
        selectedLabelTextStyle: Km1Text.caption1.copyWith(color: c.brandInk, fontWeight: FontWeight.w600),
        unselectedLabelTextStyle: Km1Text.caption1.copyWith(color: c.inkSecondary),
      ),
      iconButtonTheme: IconButtonThemeData(
        style: ButtonStyle(
          minimumSize: WidgetStatePropertyAll(minTarget),
          fixedSize: WidgetStatePropertyAll(minTarget),
          shape: WidgetStatePropertyAll(shape),
          foregroundColor: WidgetStateProperty.resolveWith((s) => s.contains(WidgetState.disabled) ? c.inkDisabled : c.ink),
          backgroundColor: WidgetStateProperty.resolveWith((s) {
            if (s.contains(WidgetState.pressed)) return c.surfacePressed;
            if (s.contains(WidgetState.hovered)) return c.surfaceHover;
            return Colors.transparent;
          }),
          side: WidgetStateProperty.resolveWith((s) => s.contains(WidgetState.focused) ? focusSide : BorderSide.none),
        ),
      ),

      // 入力欄 / Inputs — 文字はスマホ 16px、PC 14px。ヒントは上、エラーは下。
      inputDecorationTheme: InputDecorationTheme(
        isDense: false,
        filled: true,
        fillColor: c.surface,
        contentPadding: const EdgeInsets.symmetric(horizontal: Km1Space.mdNudge, vertical: Km1Space.mdNudge),
        constraints: BoxConstraints(minHeight: target),
        hintStyle: TextStyle(fontSize: fieldSize, height: (fieldSize + 8) / fieldSize, color: c.inkTertiary),
        labelStyle: Km1Text.body1.copyWith(color: c.inkSecondary),
        floatingLabelBehavior: FloatingLabelBehavior.never,
        helperStyle: Km1Text.caption1.copyWith(color: c.inkSecondary),
        errorStyle: Km1Text.caption1.copyWith(color: c.dangerInk),
        border: border(c.strokeStrong),
        enabledBorder: border(c.strokeStrong),
        focusedBorder: border(c.focusRing, 2),
        errorBorder: border(c.danger),
        focusedErrorBorder: border(c.danger, 2),
        disabledBorder: border(c.stroke),
      ),
      textSelectionTheme: TextSelectionThemeData(cursorColor: c.brandInk, selectionColor: c.brandTint),

      // 選択系 / Selection controls — 選択の縁は brandStroke。
      checkboxTheme: CheckboxThemeData(
        materialTapTargetSize: tapSize,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(Km1Radius.sm)),
        side: WidgetStateBorderSide.resolveWith((s) => BorderSide(
              color: s.contains(WidgetState.disabled) ? c.stroke : (s.contains(WidgetState.selected) ? c.brandStroke : c.strokeStrong),
              width: 1,
            )),
        fillColor: WidgetStateProperty.resolveWith((s) {
          if (s.contains(WidgetState.disabled)) return c.surfaceMuted;
          return s.contains(WidgetState.selected) ? c.brand : Colors.transparent;
        }),
        checkColor: WidgetStatePropertyAll(c.onBrand),
      ),
      radioTheme: RadioThemeData(
        materialTapTargetSize: tapSize,
        fillColor: WidgetStateProperty.resolveWith((s) {
          if (s.contains(WidgetState.disabled)) return c.inkDisabled;
          return s.contains(WidgetState.selected) ? c.brandStroke : c.strokeStrong;
        }),
      ),
      switchTheme: SwitchThemeData(
        materialTapTargetSize: tapSize,
        thumbColor: WidgetStateProperty.resolveWith((s) {
          if (s.contains(WidgetState.disabled)) return c.inkDisabled;
          return s.contains(WidgetState.selected) ? c.onBrand : c.inkSecondary;
        }),
        trackColor: WidgetStateProperty.resolveWith((s) {
          if (s.contains(WidgetState.disabled)) return c.surfaceMuted;
          return s.contains(WidgetState.selected) ? c.brand : c.surfaceMuted;
        }),
        trackOutlineColor: WidgetStateProperty.resolveWith((s) {
          if (s.contains(WidgetState.disabled)) return c.stroke;
          return s.contains(WidgetState.selected) ? c.brandStroke : c.strokeStrong;
        }),
      ),

      // タブ / Tabs
      tabBarTheme: TabBarThemeData(
        labelColor: c.ink,
        unselectedLabelColor: c.inkSecondary,
        labelStyle: Km1Text.body1Strong,
        unselectedLabelStyle: Km1Text.body1,
        indicatorColor: c.brandStroke,
        dividerColor: c.strokeSubtle,
        indicatorSize: TabBarIndicatorSize.label,
        overlayColor: WidgetStateProperty.resolveWith((s) =>
            s.contains(WidgetState.pressed) ? c.surfacePressed : (s.contains(WidgetState.hovered) ? c.surfaceHover : null)),
      ),

      // カード・ダイアログ / Cards & dialogs
      cardTheme: CardThemeData(
        color: c.surface,
        surfaceTintColor: Colors.transparent,
        elevation: 0,
        margin: EdgeInsets.zero,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(Km1Radius.lg),
          side: BorderSide(color: c.stroke),
        ),
      ),
      dialogTheme: DialogThemeData(
        backgroundColor: c.surface,
        surfaceTintColor: Colors.transparent,
        elevation: 0,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(Km1Radius.xl),
          side: BorderSide(color: c.stroke),
        ),
        titleTextStyle: Km1Text.subtitle1.copyWith(color: c.ink),
        contentTextStyle: Km1Text.body1Para.copyWith(color: c.ink),
        actionsPadding: const EdgeInsets.all(Km1Space.xxl),
      ),
      snackBarTheme: SnackBarThemeData(
        backgroundColor: c.surfaceSunken,
        contentTextStyle: Km1Text.body1Para.copyWith(color: c.ink),
        // 操作（元に戻す）は紺の文字だけにせず、枠のボタンと同じ見た目（Web と同じ。D32）
        // The action is outlined like a secondary button, not bare navy text (same as Web)
        actionTextColor: c.ink,
        actionBackgroundColor: c.surface,
        actionOverflowThreshold: 0.25,
        behavior: SnackBarBehavior.floating,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(Km1Radius.lg),
          side: BorderSide(color: c.stroke),
        ),
      ),
      listTileTheme: ListTileThemeData(
        minTileHeight: target,
        textColor: c.ink,
        iconColor: c.ink,
      ),
    );
  }
}
'''
open(P+'km1_theme.dart','w').write(o)
print(len(o.splitlines()),'lines; semantic',len(sem))
