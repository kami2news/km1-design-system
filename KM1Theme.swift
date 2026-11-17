// KM1 — tokens.json から自動生成。直接編集しない。 / Generated from tokens.json; do not edit by hand.
//
// 使い方 / Usage: Text("予定").font(Km1Text.body1).foregroundStyle(Km1Color.ink)
//   色はライト・ダークで自動で切り替わる（iOS・iPadOS・macOS）。 / Colors switch with light and dark automatically.
//   書体は Noto Sans JP を同梱していればそれを、無ければシステムの書体（ヒラギノ角ゴ）を使い、どちらも Dynamic Type で拡大する。
//   Uses bundled Noto Sans JP if present, otherwise the system font; both scale with Dynamic Type.
//   アイコンは FluentIcons（Swift Package Manager か CocoaPods）。SF Symbols に置き換えない。 / Icons: FluentIcons, not SF Symbols.
//   操作領域は 44pt（Apple HIG）。 / Hit areas are 44pt (Apple HIG).

import SwiftUI
#if canImport(UIKit)
import UIKit
#elseif canImport(AppKit)
import AppKit
#endif

private func km1Dynamic(_ light: UInt32, _ dark: UInt32) -> Color {
    func comps(_ v: UInt32) -> (CGFloat, CGFloat, CGFloat) {
        (CGFloat((v >> 16) & 0xFF) / 255, CGFloat((v >> 8) & 0xFF) / 255, CGFloat(v & 0xFF) / 255)
    }
    let l = comps(light), d = comps(dark)
    #if canImport(UIKit)
    return Color(uiColor: UIColor { trait in
        let c = trait.userInterfaceStyle == .dark ? d : l
        return UIColor(red: c.0, green: c.1, blue: c.2, alpha: 1)
    })
    #elseif canImport(AppKit)
    return Color(nsColor: NSColor(name: nil) { appearance in
        let isDark = appearance.bestMatch(from: [.aqua, .darkAqua]) == .darkAqua
        let c = isDark ? d : l
        return NSColor(srgbRed: c.0, green: c.1, blue: c.2, alpha: 1)
    })
    #else
    return Color(red: Double(l.0), green: Double(l.1), blue: Double(l.2))
    #endif
}

/// 意味づけの色 / Semantic colors
public enum Km1Color {
    public static let surface = km1Dynamic(0xFFFFFF, 0x292929)
    public static let surfaceSubtle = km1Dynamic(0xFAFAFA, 0x1F1F1F)
    public static let surfaceMuted = km1Dynamic(0xF5F5F5, 0x141414)
    public static let surfaceSunken = km1Dynamic(0xF0F0F0, 0x0A0A0A)
    public static let surfaceHover = km1Dynamic(0xF5F5F5, 0x383838)
    public static let surfacePressed = km1Dynamic(0xE0E0E0, 0x1F1F1F)
    public static let ink = km1Dynamic(0x242424, 0xFFFFFF)
    public static let inkSecondary = km1Dynamic(0x424242, 0xD6D6D6)
    public static let inkTertiary = km1Dynamic(0x616161, 0xADADAD)
    public static let inkDisabled = km1Dynamic(0xBDBDBD, 0x5C5C5C)
    public static let stroke = km1Dynamic(0xD1D1D1, 0x666666)
    public static let strokeSubtle = km1Dynamic(0xE0E0E0, 0x525252)
    public static let strokeStrong = km1Dynamic(0x616161, 0xD6D6D6)
    public static let iconInk = km1Dynamic(0x657283, 0x9AA7B8)
    public static let iconTintStart = km1Dynamic(0xF6F8FB, 0x3B4452)
    public static let iconTintEnd = km1Dynamic(0xD3DCE7, 0x2A313B)
    public static let brand = km1Dynamic(0x10218B, 0x3A4FD1)
    public static let brandHover = km1Dynamic(0x0C1A6E, 0x4A5FE0)
    public static let brandPressed = km1Dynamic(0x081257, 0x2C3FB8)
    public static let onBrand = km1Dynamic(0xFFFFFF, 0xFFFFFF)
    public static let brandInk = km1Dynamic(0x10218B, 0x99A6FF)
    public static let brandTint = km1Dynamic(0xECEFFC, 0x0D1238)
    public static let brandStroke = km1Dynamic(0x10218B, 0x7A8CF5)
    public static let focusRing = km1Dynamic(0x000000, 0xFFFFFF)
    public static let infoInk = km1Dynamic(0x0F6CBD, 0x479EF5)
    public static let infoTint = km1Dynamic(0xEBF3FC, 0x082338)
    public static let danger = km1Dynamic(0xB10E1C, 0xC50F1F)
    public static let dangerInk = km1Dynamic(0xB10E1C, 0xE37D80)
    public static let dangerTint = km1Dynamic(0xFDF3F4, 0x3B0509)
    public static let successInk = km1Dynamic(0x107C10, 0x54B054)
    public static let successTint = km1Dynamic(0xF1FAF1, 0x052505)
    public static let warningInk = km1Dynamic(0xBC4B09, 0xFAA06B)
    public static let warningTint = km1Dynamic(0xFFF9F5, 0x411200)
}

/// 分類色（帯と淡い塗りだけ。文字には使わない）/ Category colors: bars and tints only
public enum Km1Category {
    public static let blue = km1Dynamic(0x0F6CBD, 0x0F6CBD)
    public static let cornflower = km1Dynamic(0x4F6BED, 0x4F6BED)
    public static let cyan = km1Dynamic(0x0099BC, 0x0099BC)
    public static let teal = km1Dynamic(0x038387, 0x038387)
    public static let seafoam = km1Dynamic(0x00B294, 0x00B294)
    public static let green = km1Dynamic(0x13A10E, 0x13A10E)
    public static let lime = km1Dynamic(0x8BBF26, 0x8BBF26)
    public static let marigold = km1Dynamic(0xEAA300, 0xEAA300)
    public static let pumpkin = km1Dynamic(0xF7630C, 0xF7630C)
    public static let darkOrange = km1Dynamic(0xCA5010, 0xCA5010)
    public static let red = km1Dynamic(0xD13438, 0xD13438)
    public static let cranberry = km1Dynamic(0xC50F1F, 0xC50F1F)
    public static let pink = km1Dynamic(0xE43BA6, 0xE43BA6)
    public static let berry = km1Dynamic(0xC239B3, 0xC239B3)
    public static let purple = km1Dynamic(0x8764B8, 0x8764B8)
    public static let grape = km1Dynamic(0x5C2E91, 0x5C2E91)
    public static let brown = km1Dynamic(0x8E562E, 0x8E562E)
    public static let gray = km1Dynamic(0x7A7574, 0x7A7574)
    /// 淡い塗り（ライト 14%、ダーク 32%）/ Tint fill
    public static func tint(_ c: Color, dark: Bool) -> Color { c.opacity(dark ? 0.32 : 0.14) }
}

public enum Km1Space {
    public static let none: CGFloat = 0
    public static let xxs: CGFloat = 2
    public static let xs: CGFloat = 4
    public static let smNudge: CGFloat = 6
    public static let sm: CGFloat = 8
    public static let mdNudge: CGFloat = 10
    public static let md: CGFloat = 12
    public static let lg: CGFloat = 16
    public static let xl: CGFloat = 20
    public static let xxl: CGFloat = 24
    public static let xxxl: CGFloat = 32
    public static let targetCompact: CGFloat = 32
    public static let target: CGFloat = 44
    /// 操作領域（Apple HIG の 44pt）/ Hit area (Apple HIG 44pt)
    public static let hitTarget: CGFloat = 44  // = control-target-ios
}

/// 用途別の余白（KM1-TOK-001）。Km1Space を指す / Role spacing aliases
public enum Km1SpaceRole {
    public static let layoutSectionGap: CGFloat = Km1Space.xxl
    public static let layoutRegionGap: CGFloat = Km1Space.xxxl
    public static let containerCardPaddingCompact: CGFloat = Km1Space.md
    public static let containerCardPaddingRegular: CGFloat = Km1Space.lg
    public static let containerCardPaddingSpacious: CGFloat = Km1Space.xxl
    public static let collectionItemGapCompact: CGFloat = Km1Space.xs
    public static let collectionItemGapRegular: CGFloat = Km1Space.sm
    public static let collectionItemGapSpacious: CGFloat = Km1Space.lg
}

public enum Km1Radius {
    public static let none: CGFloat = 0
    public static let sm: CGFloat = 2
    public static let md: CGFloat = 4
    public static let lg: CGFloat = 6
    public static let xl: CGFloat = 8
    public static let xxl: CGFloat = 12
    public static let circular: CGFloat = 9999
}

/// 文字スタイル。Dynamic Type に合わせて拡大する / Text styles that scale with Dynamic Type
public enum Km1Text {
    /// 同梱するときの書体名 / Bundled font name
    public static var familyName = "Noto Sans JP"
    public static var display: Font { .custom(familyName, size: 68, relativeTo: .largeTitle).weight(.semibold) }
    public static var largeTitle: Font { .custom(familyName, size: 40, relativeTo: .largeTitle).weight(.semibold) }
    public static var title1: Font { .custom(familyName, size: 32, relativeTo: .title).weight(.semibold) }
    public static var title2: Font { .custom(familyName, size: 28, relativeTo: .title2).weight(.semibold) }
    public static var title3: Font { .custom(familyName, size: 24, relativeTo: .title3).weight(.semibold) }
    public static var subtitle1: Font { .custom(familyName, size: 20, relativeTo: .headline).weight(.semibold) }
    public static var subtitle2: Font { .custom(familyName, size: 16, relativeTo: .subheadline).weight(.semibold) }
    public static var body2: Font { .custom(familyName, size: 16, relativeTo: .body).weight(.regular) }
    public static var body1: Font { .custom(familyName, size: 14, relativeTo: .body).weight(.regular) }
    public static var body1Strong: Font { .custom(familyName, size: 14, relativeTo: .body).weight(.semibold) }
    public static var caption1: Font { .custom(familyName, size: 12, relativeTo: .caption).weight(.regular) }
    public static var caption2: Font { .custom(familyName, size: 10, relativeTo: .caption2).weight(.regular) }
}

/// 主ボタンの見た目。高さ 44pt、brand の塗り、brand-stroke の縁取り（ほかの環境とそろえる）
/// Primary button: 44pt high, brand fill, brand-stroke outline (matches other platforms)
public struct Km1PrimaryButtonStyle: ButtonStyle {
    @Environment(\.isEnabled) private var isEnabled
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
}
