// KM1 — tokens.json から自動生成。直接編集しない。 / Generated from tokens.json; do not edit by hand.
//
// 使い方 / Usage:
//   setContent { Km1Theme { ... } }
//   色は Km1.colors.ink のように意味づけトークンで取る。 / Use semantic tokens: Km1.colors.ink
//   動的な色（dynamicColorScheme）は使わない。KM1 のブランド色が消えるため。 / Do not use dynamic color.
//   アイコンは com.microsoft.design:fluent-system-icons（Maven Central）。Material Icons は使わない。
//   Icons: com.microsoft.design:fluent-system-icons (Maven Central); not Material Icons.
//   操作領域は Material 3 の既定の 48dp（Android の推奨）をそのまま使う。 / Keep Material 3's default 48dp touch targets.

package km1.theme

import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.foundation.layout.RowScope
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Shapes
import androidx.compose.material3.Typography
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.runtime.CompositionLocalProvider
import androidx.compose.runtime.Immutable
import androidx.compose.runtime.ReadOnlyComposable
import androidx.compose.runtime.staticCompositionLocalOf
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

/** 意味づけの色 / Semantic colors */
@Immutable
data class Km1Colors(
    val brandDarkTint: Color,
    val blueDarkTint: Color,
    val redDarkTint: Color,
    val greenDarkTint: Color,
    val orangeDarkTint: Color,
    val surface: Color,
    val surfaceSubtle: Color,
    val surfaceMuted: Color,
    val surfaceSunken: Color,
    val surfaceHover: Color,
    val surfacePressed: Color,
    val ink: Color,
    val inkSecondary: Color,
    val inkTertiary: Color,
    val inkDisabled: Color,
    val stroke: Color,
    val strokeSubtle: Color,
    val strokeStrong: Color,
    val iconInk: Color,
    val iconTintStart: Color,
    val iconTintEnd: Color,
    val brand: Color,
    val brandHover: Color,
    val brandPressed: Color,
    val onBrand: Color,
    val brandInk: Color,
    val brandTint: Color,
    val brandStroke: Color,
    val focusRing: Color,
    val infoInk: Color,
    val infoTint: Color,
    val danger: Color,
    val dangerInk: Color,
    val dangerTint: Color,
    val successInk: Color,
    val successTint: Color,
    val warningInk: Color,
    val warningTint: Color,
)

val Km1LightColors = Km1Colors(
    brandDarkTint = Color(0xFF333543),
    blueDarkTint = Color(0xFF253341),
    redDarkTint = Color(0xFF3E2E2F),
    greenDarkTint = Color(0xFF273627),
    orangeDarkTint = Color(0xFF42342B),
    surface = Color(0xFFFFFFFF),
    surfaceSubtle = Color(0xFFFAFAFA),
    surfaceMuted = Color(0xFFF5F5F5),
    surfaceSunken = Color(0xFFF0F0F0),
    surfaceHover = Color(0xFFF5F5F5),
    surfacePressed = Color(0xFFE0E0E0),
    ink = Color(0xFF242424),
    inkSecondary = Color(0xFF616161),
    inkTertiary = Color(0xFF616161),
    inkDisabled = Color(0xFFBDBDBD),
    stroke = Color(0xFFD1D1D1),
    strokeSubtle = Color(0xFFE0E0E0),
    strokeStrong = Color(0xFF616161),
    iconInk = Color(0xFF657283),
    iconTintStart = Color(0xFFF6F8FB),
    iconTintEnd = Color(0xFFD3DCE7),
    brand = Color(0xFF10218B),
    brandHover = Color(0xFF0C1A6E),
    brandPressed = Color(0xFF081257),
    onBrand = Color(0xFFFFFFFF),
    brandInk = Color(0xFF10218B),
    brandTint = Color(0xFFECEFFC),
    brandStroke = Color(0xFF10218B),
    focusRing = Color(0xFF000000),
    infoInk = Color(0xFF0F6CBD),
    infoTint = Color(0xFFEBF3FC),
    danger = Color(0xFFB10E1C),
    dangerInk = Color(0xFFB10E1C),
    dangerTint = Color(0xFFFDF3F4),
    successInk = Color(0xFF107C10),
    successTint = Color(0xFFF1FAF1),
    warningInk = Color(0xFFBC4B09),
    warningTint = Color(0xFFFFF9F5),
)

val Km1DarkColors = Km1Colors(
    brandDarkTint = Color(0xFF333543),
    blueDarkTint = Color(0xFF253341),
    redDarkTint = Color(0xFF3E2E2F),
    greenDarkTint = Color(0xFF273627),
    orangeDarkTint = Color(0xFF42342B),
    surface = Color(0xFF292929),
    surfaceSubtle = Color(0xFF1F1F1F),
    surfaceMuted = Color(0xFF141414),
    surfaceSunken = Color(0xFF0A0A0A),
    surfaceHover = Color(0xFF383838),
    surfacePressed = Color(0xFF1F1F1F),
    ink = Color(0xFFFFFFFF),
    inkSecondary = Color(0xFFADADAD),
    inkTertiary = Color(0xFFADADAD),
    inkDisabled = Color(0xFF5C5C5C),
    stroke = Color(0xFF666666),
    strokeSubtle = Color(0xFF525252),
    strokeStrong = Color(0xFFD6D6D6),
    iconInk = Color(0xFF9AA7B8),
    iconTintStart = Color(0xFF3B4452),
    iconTintEnd = Color(0xFF2A313B),
    brand = Color(0xFF3A4FD1),
    brandHover = Color(0xFF4A5FE0),
    brandPressed = Color(0xFF2C3FB8),
    onBrand = Color(0xFFFFFFFF),
    brandInk = Color(0xFF99A6FF),
    brandTint = Color(0xFF333543),
    brandStroke = Color(0xFF7A8CF5),
    focusRing = Color(0xFFFFFFFF),
    infoInk = Color(0xFF479EF5),
    infoTint = Color(0xFF253341),
    danger = Color(0xFFC50F1F),
    dangerInk = Color(0xFFE37D80),
    dangerTint = Color(0xFF3E2E2F),
    successInk = Color(0xFF54B054),
    successTint = Color(0xFF273627),
    warningInk = Color(0xFFFAA06B),
    warningTint = Color(0xFF42342B),
)

/** 分類色（帯と淡い塗りだけ。文字には使わない）/ Category colors: bars and tints only */
object Km1Category {
    val blue = Color(0xFF0F6CBD)
    val cornflower = Color(0xFF4F6BED)
    val cyan = Color(0xFF0099BC)
    val teal = Color(0xFF038387)
    val seafoam = Color(0xFF00B294)
    val green = Color(0xFF13A10E)
    val lime = Color(0xFF8BBF26)
    val marigold = Color(0xFFEAA300)
    val pumpkin = Color(0xFFF7630C)
    val darkOrange = Color(0xFFCA5010)
    val red = Color(0xFFD13438)
    val cranberry = Color(0xFFC50F1F)
    val pink = Color(0xFFE43BA6)
    val berry = Color(0xFFC239B3)
    val purple = Color(0xFF8764B8)
    val grape = Color(0xFF5C2E91)
    val brown = Color(0xFF8E562E)
    val gray = Color(0xFF7A7574)
    val all = listOf(blue, cornflower, cyan, teal, seafoam, green, lime, marigold, pumpkin, darkOrange, red, cranberry, pink, berry, purple, grape, brown, gray)
    /** 淡い塗り（ライト 14%、ダーク 32%）/ Tint fill */
    fun tint(c: Color, dark: Boolean): Color = c.copy(alpha = if (dark) 0.32f else 0.14f)
}

object Km1Space {
    val none = 0.dp
    val xxs = 2.dp
    val xs = 4.dp
    val smNudge = 6.dp
    val sm = 8.dp
    val mdNudge = 10.dp
    val md = 12.dp
    val lg = 16.dp
    val xl = 20.dp
    val xxl = 24.dp
    val xxxl = 32.dp
    val targetCompact = 32.dp
    val target = 44.dp
}

/** 用途別の余白（KM1-TOK-001）。Km1Space を指す / Role spacing aliases */
object Km1SpaceRole {
    val layoutSectionGap = Km1Space.xxl
    val layoutRegionGap = Km1Space.xxxl
    val containerCardPaddingCompact = Km1Space.md
    val containerCardPaddingRegular = Km1Space.lg
    val containerCardPaddingSpacious = Km1Space.xxl
    val collectionItemGapCompact = Km1Space.xs
    val collectionItemGapRegular = Km1Space.sm
    val collectionItemGapSpacious = Km1Space.lg
}

/** 操作領域（Android 48dp、KM1-TOK-001-D）/ Hit area on Android */
object Km1PlatformTarget { val android = 48.dp }

object Km1Radius {
    val none = 0.dp
    val sm = 2.dp
    val md = 4.dp
    val lg = 6.dp
    val xl = 8.dp
    val xxl = 12.dp
    val circular = 9999.dp
}

/** 文字スタイル（端末の書体。日本語は Noto Sans CJK）/ Text styles on the system font */
object Km1Text {
    val display = TextStyle(fontSize = 68.sp, lineHeight = 84.sp, fontWeight = FontWeight.W600)
    val largeTitle = TextStyle(fontSize = 40.sp, lineHeight = 52.sp, fontWeight = FontWeight.W600)
    val title = TextStyle(fontSize = 28.sp, lineHeight = 36.sp, fontWeight = FontWeight.W600)
    val subtitle1 = TextStyle(fontSize = 20.sp, lineHeight = 28.sp, fontWeight = FontWeight.W600)
    val subtitle2 = TextStyle(fontSize = 16.sp, lineHeight = 24.sp, fontWeight = FontWeight.W600)
    val body2 = TextStyle(fontSize = 16.sp, lineHeight = 26.sp, fontWeight = FontWeight.W400)
    val body1 = TextStyle(fontSize = 14.sp, lineHeight = 20.sp, fontWeight = FontWeight.W400)
    val body1Para = TextStyle(fontSize = 14.sp, lineHeight = 24.sp, fontWeight = FontWeight.W400)
    val body1Strong = TextStyle(fontSize = 14.sp, lineHeight = 20.sp, fontWeight = FontWeight.W600)
    val caption1 = TextStyle(fontSize = 12.sp, lineHeight = 18.sp, fontWeight = FontWeight.W400)
}

private val LocalKm1Colors = staticCompositionLocalOf { Km1LightColors }

object Km1 {
    val colors: Km1Colors
        @Composable @ReadOnlyComposable get() = LocalKm1Colors.current
}

private val Km1LightScheme = lightColorScheme(
    primary = Color(0xFF10218B),
    onPrimary = Color(0xFFFFFFFF),
    secondary = Color(0xFF10218B),
    onSecondary = Color(0xFFFFFFFF),
    error = Color(0xFFB10E1C),
    onError = Color(0xFFFFFFFF),
    background = Color(0xFFFFFFFF),
    onBackground = Color(0xFF242424),
    surface = Color(0xFFFFFFFF),
    onSurface = Color(0xFF242424),
    surfaceVariant = Color(0xFFF5F5F5),
    onSurfaceVariant = Color(0xFF616161),
    outline = Color(0xFF616161),
    outlineVariant = Color(0xFFD1D1D1),
)

private val Km1DarkScheme = darkColorScheme(
    primary = Color(0xFF3A4FD1),
    onPrimary = Color(0xFFFFFFFF),
    secondary = Color(0xFF99A6FF),
    onSecondary = Color(0xFF292929),
    error = Color(0xFFC50F1F),
    onError = Color(0xFFFFFFFF),
    background = Color(0xFF292929),
    onBackground = Color(0xFFFFFFFF),
    surface = Color(0xFF292929),
    onSurface = Color(0xFFFFFFFF),
    surfaceVariant = Color(0xFF141414),
    onSurfaceVariant = Color(0xFFADADAD),
    outline = Color(0xFFD6D6D6),
    outlineVariant = Color(0xFF666666),
)

private val Km1Typography = Typography(
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
}
