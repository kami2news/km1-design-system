import json,re
import os as _os
_H=_os.path.dirname(_os.path.abspath(__file__))
P=_os.environ.get('KM1_PROJECT') or (_os.path.join(_H,'..','project') if _os.path.exists(_os.path.join(_H,'..','project','tokens.json')) else _os.path.join(_H,'..'))
P=_os.path.normpath(P)+'/'
t=json.load(open(P+'tokens.json'))
C={x['name']:x['value'] for x in t['color']['tokens']}
def res(n,th):
    v=C[n]; v=v if isinstance(v,str) else v.get(th,v['light'])
    m=re.fullmatch(r'\{(.+)\}',v); return res(m.group(1),th) if m else v.upper()
def camel(n):
    p=n.split('-'); return p[0]+''.join(w.capitalize() for w in p[1:])
def pascal(n): return ''.join(w.capitalize() for w in n.split('-'))
px=lambda s:float(str(s).replace('px',''))
sem=[n for n in C if not re.match(r'(gray|brand|blue|red|green|orange)-\d+$',n) and not n.startswith('cat-')]
cats=[n for n in C if n.startswith('cat-')]
SP={x['name']:px(x['value']) for x in t['spacing']['tokens']}
RA={x['name']:px(x['value']) for x in t['radius']['tokens']}
STY=[s for g in t['type']['groups'] for s in g['styles']]
HEAD_JA='KM1 — tokens.json から自動生成。直接編集しない。 / Generated from tokens.json; do not edit by hand.'
def h6(x): return x.lstrip('#').upper()
# ---------------- WinUI 3 ----------------
HC={'surface':'SystemColorWindowColor','ink':'SystemColorWindowTextColor','brand':'SystemColorHighlightColor','on-brand':'SystemColorHighlightTextColor',
    'ink-disabled':'SystemColorGrayTextColor','brand-ink':'SystemColorHotlightColor','focus-ring':'SystemColorWindowTextColor'}
def hc(n):
    if n in HC: return HC[n]
    if n.startswith('surface') or n.endswith('-tint'): return 'SystemColorWindowColor'
    if n.startswith('brand'): return 'SystemColorHighlightColor'
    return 'SystemColorWindowTextColor'
x=[f'<!-- {HEAD_JA} -->',
'<!-- 使い方 / Usage: App.xaml の Application.Resources の MergedDictionaries に入れる。',
'     <ResourceDictionary Source="KM1.xaml" /> を XamlControlsResources の後に置く。',
'     Merge after XamlControlsResources in App.xaml. -->',
'<ResourceDictionary',
'    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"',
'    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">','',
'  <!-- アクセント色: WinUI はライトで Dark1〜3、ダークで Light1〜3 を使う。',
'       Accent ramp: WinUI reads Dark1-3 in light theme and Light1-3 in dark theme. -->',
f'  <Color x:Key="SystemAccentColor">#FF{h6(res("brand-600","light"))}</Color>',
f'  <Color x:Key="SystemAccentColorDark1">#FF{h6(res("brand","light"))}</Color>',
f'  <Color x:Key="SystemAccentColorDark2">#FF{h6(res("brand-ink","light"))}</Color>',
f'  <Color x:Key="SystemAccentColorDark3">#FF{h6(res("brand-800","light"))}</Color>',
f'  <Color x:Key="SystemAccentColorLight1">#FF{h6(res("brand-400","light"))}</Color>',
f'  <Color x:Key="SystemAccentColorLight2">#FF{h6(res("brand","dark"))}</Color>',
f'  <Color x:Key="SystemAccentColorLight3">#FF{h6(res("brand-ink","dark"))}</Color>','',
'  <!-- 角丸 / Corner radius -->',
f'  <CornerRadius x:Key="ControlCornerRadius">{int(RA["radius-md"])}</CornerRadius>',
f'  <CornerRadius x:Key="OverlayCornerRadius">{int(RA["radius-lg"])}</CornerRadius>','',
'  <!-- 書体: 日本語は Yu Gothic UI（Windows 標準）。Noto Sans JP を同梱するならここを差し替える。',
'       Typeface: Yu Gothic UI for Japanese; replace if Noto Sans JP is bundled. -->',
'  <FontFamily x:Key="ContentControlThemeFontFamily">Segoe UI Variable Text, Yu Gothic UI, Segoe UI</FontFamily>','',
'  <ResourceDictionary.ThemeDictionaries>']
for key,th in (('Light','light'),('Default','dark')):
    x.append(f'    <ResourceDictionary x:Key="{key}">')
    if th=='dark':
        x.append('      <!-- KM1 のダークはブランドの塗りに白い文字。WinUI 既定の黒い文字を上書きする。')
        x.append('           KM1 dark uses light text on the brand fill; override WinUI\'s default black. -->')
        x.append(f'      <SolidColorBrush x:Key="TextOnAccentFillColorPrimaryBrush" Color="#FF{h6(res("on-brand","dark"))}" />')
        x.append(f'      <SolidColorBrush x:Key="TextOnAccentFillColorSecondaryBrush" Color="#FF{h6(res("on-brand","dark"))}" Opacity="0.85" />')
        x.append(f'      <SolidColorBrush x:Key="TextOnAccentFillColorSelectedTextBrush" Color="#FF{h6(res("on-brand","dark"))}" />')
        x.append('      <!-- 主ボタンの塗りと背景の差が小さいので、Web 版と同じく brand-stroke で縁取る。')
        x.append('           The fill is close to the background in dark, so outline primary buttons with brand-stroke as on the web. -->')
        for kk in ('AccentButtonBorderBrush','AccentButtonBorderBrushPointerOver','AccentButtonBorderBrushPressed'):
            x.append(f'      <SolidColorBrush x:Key="{kk}" Color="#FF{h6(res("brand-stroke","dark"))}" />')
    for n in sem:
        x.append(f'      <SolidColorBrush x:Key="KM1{pascal(n)}Brush" Color="#FF{h6(res(n,th))}" />')
    x.append('    </ResourceDictionary>')
x.append('    <!-- ハイコントラストではシステムの色に従う / High contrast follows system colors -->')
x.append('    <ResourceDictionary x:Key="HighContrast">')
for n in sem:
    x.append(f'      <SolidColorBrush x:Key="KM1{pascal(n)}Brush" Color="{{ThemeResource {hc(n)}}}" />')
x.append('    </ResourceDictionary>')
x.append('  </ResourceDictionary.ThemeDictionaries>')
x.append('')
x.append('  <!-- 分類色（帯と淡い塗りだけ）/ Category colors (bars and tints only) -->')
for n in cats: x.append(f'  <Color x:Key="KM1{pascal(n)}Color">#FF{h6(res(n,"light"))}</Color>')
x.append('')
x.append('  <!-- 余白 / Spacing (epx) -->')
for n,v in SP.items(): x.append(f'  <x:Double x:Key="KM1{pascal(n)}">{v:g}</x:Double>')
x.append('  <!-- 用途別の余白（KM1-TOK-001。値は基本トークンと同じ）/ Role spacing aliases -->')
for e in t['spacingRole']['tokens']: x.append(f'  <x:Double x:Key="KM1{pascal(e["name"])}">{px(e["value"]):g}</x:Double>  <!-- = KM1{pascal(e["ref"])} -->')
x.append('  <!-- 操作領域（Windows、KM1-TOK-001-D）/ Hit area on Windows -->')
_w=[e for e in t['platformTarget']['tokens'] if e['name']=='control-target-windows'][0]
x.append(f'  <x:Double x:Key="KM1ControlTarget">{px(_w["value"]):g}</x:Double>  <!-- = control-target-windows -->')
x.append('</ResourceDictionary>')
open(P+'KM1.xaml','w').write('\n'.join(x)+'\n')
# ---------------- Jetpack Compose ----------------
def col(hx): return f'Color(0xFF{h6(hx)})'
k=[f'// {HEAD_JA}','//',
'// 使い方 / Usage:','//   setContent { Km1Theme { ... } }','//   色は Km1.colors.ink のように意味づけトークンで取る。 / Use semantic tokens: Km1.colors.ink',
'//   動的な色（dynamicColorScheme）は使わない。KM1 のブランド色が消えるため。 / Do not use dynamic color.',
'//   アイコンは com.microsoft.design:fluent-system-icons（Maven Central）。Material Icons は使わない。',
'//   Icons: com.microsoft.design:fluent-system-icons (Maven Central); not Material Icons.',
'//   操作領域は Material 3 の既定の 48dp（Android の推奨）をそのまま使う。 / Keep Material 3\'s default 48dp touch targets.',
'','package km1.theme','',
'import androidx.compose.foundation.BorderStroke',
'import androidx.compose.foundation.isSystemInDarkTheme',
'import androidx.compose.foundation.layout.RowScope',
'import androidx.compose.foundation.shape.RoundedCornerShape',
'import androidx.compose.material3.Button',
'import androidx.compose.material3.MaterialTheme',
'import androidx.compose.material3.Shapes',
'import androidx.compose.material3.Typography',
'import androidx.compose.material3.darkColorScheme',
'import androidx.compose.material3.lightColorScheme',
'import androidx.compose.runtime.Composable',
'import androidx.compose.runtime.CompositionLocalProvider',
'import androidx.compose.runtime.Immutable',
'import androidx.compose.runtime.ReadOnlyComposable',
'import androidx.compose.runtime.staticCompositionLocalOf',
'import androidx.compose.ui.Modifier',
'import androidx.compose.ui.graphics.Color',
'import androidx.compose.ui.text.TextStyle',
'import androidx.compose.ui.text.font.FontWeight',
'import androidx.compose.ui.unit.dp',
'import androidx.compose.ui.unit.sp','',
'/** 意味づけの色 / Semantic colors */','@Immutable','data class Km1Colors(']
k+= [f'    val {camel(n)}: Color,' for n in sem]+[')','']
for th in ('light','dark'):
    k.append(f'val Km1{th.capitalize()}Colors = Km1Colors(')
    k+= [f'    {camel(n)} = {col(res(n,th))},' for n in sem]
    k.append(')'); k.append('')
k.append('/** 分類色（帯と淡い塗りだけ。文字には使わない）/ Category colors: bars and tints only */')
k.append('object Km1Category {')
k+= [f'    val {camel(n[4:])} = {col(res(n,"light"))}' for n in cats]
k.append('    val all = listOf('+', '.join(camel(n[4:]) for n in cats)+')')
k.append('    /** 淡い塗り（ライト 14%、ダーク 32%）/ Tint fill */')
k.append('    fun tint(c: Color, dark: Boolean): Color = c.copy(alpha = if (dark) 0.32f else 0.14f)')
k.append('}'); k.append('')
k.append('object Km1Space {'); k+= [f'    val {camel(n.replace("space-","",1))} = {v:g}.dp' for n,v in SP.items()]; k.append('}'); k.append('')
k.append('/** 用途別の余白（KM1-TOK-001）。Km1Space を指す / Role spacing aliases */')
k.append('object Km1SpaceRole {'); k+=[f'    val {camel(e["name"])} = '+('Km1Space.'+camel(e["ref"].replace("space-","",1)) if e["ref"].startswith("space-") else f'{px(e["value"]):g}.dp') for e in t['spacingRole']['tokens']]; k.append('}'); k.append('')
_a=[e for e in t['platformTarget']['tokens'] if e['name']=='control-target-android'][0]
k.append('/** 操作領域（Android 48dp、KM1-TOK-001-D）/ Hit area on Android */')
k.append(f'object Km1PlatformTarget {{ val android = {px(_a["value"]):g}.dp }}'); k.append('')
k.append('object Km1Radius {'); k+= [f'    val {camel(n.replace("radius-","",1))} = {v:g}.dp' for n,v in RA.items()]; k.append('}'); k.append('')
k.append('/** 文字スタイル（端末の書体。日本語は Noto Sans CJK）/ Text styles on the system font */')
k.append('object Km1Text {')
for s in STY:
    k.append(f'    val {camel(s["name"])} = TextStyle(fontSize = {px(s["fontSize"]):g}.sp, lineHeight = {px(s["lineHeight"]):g}.sp, fontWeight = FontWeight.W{s["fontWeight"]})')
k.append('}'); k.append('')
k.append('private val LocalKm1Colors = staticCompositionLocalOf { Km1LightColors }')
k.append('')
k.append('object Km1 {')
k.append('    val colors: Km1Colors')
k.append('        @Composable @ReadOnlyComposable get() = LocalKm1Colors.current')
k.append('}'); k.append('')
def scheme(th):
    f='darkColorScheme' if th=='dark' else 'lightColorScheme'
    m=[('primary','brand'),('onPrimary','on-brand'),('secondary','brand-ink'),('onSecondary','surface'),('error','danger'),('onError','on-brand'),
       ('background','surface'),('onBackground','ink'),('surface','surface'),('onSurface','ink'),('surfaceVariant','surface-muted'),('onSurfaceVariant','ink-secondary'),
       ('outline','stroke-strong'),('outlineVariant','stroke')]
    return f'private val Km1{th.capitalize()}Scheme = {f}(\n'+''.join(f'    {a} = {col(res(b,th))},\n' for a,b in m)+')\n'
k.append(scheme('light')); k.append(scheme('dark'))
k.append('''private val Km1Typography = Typography(
    displayLarge = Km1Text.display,
    headlineLarge = Km1Text.largeTitle,
    headlineMedium = Km1Text.title,
    headlineSmall = Km1Text.title,
    titleLarge = Km1Text.subtitle1,
    titleMedium = Km1Text.subtitle1,
    titleSmall = Km1Text.subtitle2,
    bodyLarge = Km1Text.body2,
    bodyMedium = Km1Text.body1,
    bodySmall = Km1Text.caption1,
    labelLarge = Km1Text.body1Strong,
    labelMedium = Km1Text.caption1,
    labelSmall = Km1Text.caption1,
)

private val Km1Shapes = Shapes(
    extraSmall = RoundedCornerShape(Km1Radius.sm),
    small = RoundedCornerShape(Km1Radius.md),
    medium = RoundedCornerShape(Km1Radius.lg),
    large = RoundedCornerShape(Km1Radius.xl),
    extraLarge = RoundedCornerShape(Km1Radius.xl),
)

/** KM1 のテーマ / KM1 theme */
@Composable
fun Km1Theme(darkTheme: Boolean = isSystemInDarkTheme(), content: @Composable () -> Unit) {
    val colors = if (darkTheme) Km1DarkColors else Km1LightColors
    CompositionLocalProvider(LocalKm1Colors provides colors) {
        MaterialTheme(
            colorScheme = if (darkTheme) Km1DarkScheme else Km1LightScheme,
            typography = Km1Typography,
            shapes = Km1Shapes,
            content = content,
        )
    }
}

/**
 * 主ボタン。ダークでは塗りと背景の差が小さいので、ほかの環境と同じく brand-stroke で縁取る。
 * Primary button outlined with brand-stroke, as on the web, Flutter and Windows.
 */
@Composable
fun Km1PrimaryButton(
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
    enabled: Boolean = true,
    content: @Composable RowScope.() -> Unit,
) {
    Button(
        onClick = onClick,
        modifier = modifier,
        enabled = enabled,
        shape = RoundedCornerShape(Km1Radius.md),
        border = if (enabled) BorderStroke(1.dp, Km1.colors.brandStroke) else null,
        content = content,
    )
}''')
open(P+'Km1Theme.kt','w').write('\n'.join(k)+'\n')
# ---------------- SwiftUI ----------------
def u(hx): return '0x'+h6(hx)
sw=[f'// {HEAD_JA}','//',
'// 使い方 / Usage: Text("予定").font(Km1Text.body1).foregroundStyle(Km1Color.ink)',
'//   色はライト・ダークで自動で切り替わる（iOS・iPadOS・macOS）。 / Colors switch with light and dark automatically.',
'//   書体は Noto Sans JP を同梱していればそれを、無ければシステムの書体（ヒラギノ角ゴ）を使い、どちらも Dynamic Type で拡大する。',
'//   Uses bundled Noto Sans JP if present, otherwise the system font; both scale with Dynamic Type.',
'//   アイコンは FluentIcons（Swift Package Manager か CocoaPods）。SF Symbols に置き換えない。 / Icons: FluentIcons, not SF Symbols.',
'//   操作領域は 44pt（Apple HIG）。 / Hit areas are 44pt (Apple HIG).',
'','import SwiftUI','#if canImport(UIKit)','import UIKit','#elseif canImport(AppKit)','import AppKit','#endif','',
'private func km1Dynamic(_ light: UInt32, _ dark: UInt32) -> Color {',
'    func comps(_ v: UInt32) -> (CGFloat, CGFloat, CGFloat) {',
'        (CGFloat((v >> 16) & 0xFF) / 255, CGFloat((v >> 8) & 0xFF) / 255, CGFloat(v & 0xFF) / 255)',
'    }',
'    let l = comps(light), d = comps(dark)',
'    #if canImport(UIKit)',
'    return Color(uiColor: UIColor { trait in',
'        let c = trait.userInterfaceStyle == .dark ? d : l',
'        return UIColor(red: c.0, green: c.1, blue: c.2, alpha: 1)',
'    })',
'    #elseif canImport(AppKit)',
'    return Color(nsColor: NSColor(name: nil) { appearance in',
'        let isDark = appearance.bestMatch(from: [.aqua, .darkAqua]) == .darkAqua',
'        let c = isDark ? d : l',
'        return NSColor(srgbRed: c.0, green: c.1, blue: c.2, alpha: 1)',
'    })',
'    #else',
'    return Color(red: Double(l.0), green: Double(l.1), blue: Double(l.2))',
'    #endif',
'}','',
'/// 意味づけの色 / Semantic colors','public enum Km1Color {']
sw+=[f'    public static let {camel(n)} = km1Dynamic({u(res(n,"light"))}, {u(res(n,"dark"))})' for n in sem]
sw.append('}'); sw.append('')
sw.append('/// 分類色（帯と淡い塗りだけ。文字には使わない）/ Category colors: bars and tints only')
sw.append('public enum Km1Category {')
sw+=[f'    public static let {camel(n[4:])} = km1Dynamic({u(res(n,"light"))}, {u(res(n,"dark"))})' for n in cats]
sw.append('    /// 淡い塗り（ライト 14%、ダーク 32%）/ Tint fill')
sw.append('    public static func tint(_ c: Color, dark: Bool) -> Color { c.opacity(dark ? 0.32 : 0.14) }')
sw.append('}'); sw.append('')
sw.append('public enum Km1Space {'); sw+=[f'    public static let {camel(n.replace("space-","",1))}: CGFloat = {v:g}' for n,v in SP.items()]
sw.append('    /// 操作領域（Apple HIG の 44pt）/ Hit area (Apple HIG 44pt)')
_i=[e for e in t['platformTarget']['tokens'] if e['name']=='control-target-ios'][0]
sw.append(f'    public static let hitTarget: CGFloat = {px(_i["value"]):g}  // = control-target-ios'); sw.append('}'); sw.append('')
sw.append('/// 用途別の余白（KM1-TOK-001）。Km1Space を指す / Role spacing aliases')
sw.append('public enum Km1SpaceRole {'); sw+=[f'    public static let {camel(e["name"])}: CGFloat = '+('Km1Space.'+camel(e["ref"].replace("space-","",1)) if e["ref"].startswith("space-") else f'{px(e["value"]):g}') for e in t['spacingRole']['tokens']]; sw.append('}'); sw.append('')
sw.append('public enum Km1Radius {'); sw+=[f'    public static let {camel(n.replace("radius-","",1))}: CGFloat = {v:g}' for n,v in RA.items()]; sw.append('}'); sw.append('')
REL={'display':'.largeTitle','large-title':'.largeTitle','title':'.title','subtitle-1':'.headline','subtitle-2':'.subheadline','body-2':'.body','body-1':'.body','body-1-strong':'.body','caption-1':'.caption','body-1-para':'.body'}
W={400:'.regular',500:'.medium',600:'.semibold',700:'.bold'}
sw.append('/// 文字スタイル。Dynamic Type に合わせて拡大する / Text styles that scale with Dynamic Type')
sw.append('public enum Km1Text {')
sw.append('    /// 同梱するときの書体名 / Bundled font name')
sw.append('    public static var familyName = "Noto Sans JP"')
for s in STY:
    rel=REL.get(s['name'],'.body')
    sw.append(f'    public static var {camel(s["name"])}: Font {{ .custom(familyName, size: {px(s["fontSize"]):g}, relativeTo: {rel}).weight({W.get(int(s["fontWeight"]),".regular")}) }}')
sw.append('}')
sw.append('''
/// 主ボタンの見た目。高さ 44pt、brand の塗り、brand-stroke の縁取り（ほかの環境とそろえる）
/// Primary button: 44pt high, brand fill, brand-stroke outline (matches other platforms)
public struct Km1PrimaryButtonStyle: ButtonStyle {
    @Environment(\\.isEnabled) private var isEnabled
    public init() {}
    public func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .font(Km1Text.body1Strong)
            .foregroundStyle(isEnabled ? Km1Color.onBrand : Km1Color.inkDisabled)
            .padding(.horizontal, Km1Space.md)
            .frame(minHeight: Km1Space.hitTarget)
            .background(
                RoundedRectangle(cornerRadius: Km1Radius.md)
                    .fill(isEnabled ? (configuration.isPressed ? Km1Color.brandPressed : Km1Color.brand) : Km1Color.surfaceMuted)
            )
            .overlay(
                RoundedRectangle(cornerRadius: Km1Radius.md)
                    .strokeBorder(isEnabled ? Km1Color.brandStroke : Km1Color.stroke, lineWidth: 1)
            )
            .contentShape(Rectangle())
    }
}''')
open(P+'KM1Theme.swift','w').write('\n'.join(sw)+'\n')
print('ok',len(sem),len(cats))
