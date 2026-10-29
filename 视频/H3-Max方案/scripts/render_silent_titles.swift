import AppKit
import Foundation

let destination = CommandLine.arguments[1]
try FileManager.default.createDirectory(atPath: destination, withIntermediateDirectories: true)
let w = 854, h = 480

func text(_ value: String, x: CGFloat, top: CGFloat, width: CGFloat, height: CGFloat, size: CGFloat, color: NSColor = .white, center: Bool = false) {
    let paragraph = NSMutableParagraphStyle()
    paragraph.alignment = center ? .center : .left
    let font = NSFont(name: "Arial Unicode MS", size: size) ?? NSFont.systemFont(ofSize: size)
    (value as NSString).draw(in: NSRect(x: x, y: CGFloat(h)-top-height, width: width, height: height), withAttributes: [.font: font, .foregroundColor: color, .paragraphStyle: paragraph])
}

func render(_ filename: String, _ draw: () -> Void) throws {
    let bitmap = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: w, pixelsHigh: h, bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true, isPlanar: false, colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0)!
    NSGraphicsContext.saveGraphicsState()
    NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: bitmap)
    NSColor.clear.setFill()
    NSRect(x: 0, y: 0, width: w, height: h).fill(using: .copy)
    draw()
    NSGraphicsContext.restoreGraphicsState()
    try bitmap.representation(using: .png, properties: [:])!.write(to: URL(fileURLWithPath: destination + "/" + filename))
}

func label(_ filename: String, _ top: String, _ bottom: String) throws {
    try render(filename) {
        NSColor(calibratedRed: 0.025, green: 0.055, blue: 0.095, alpha: 0.78).setFill()
        NSRect(x: 22, y: 386, width: 300, height: 72).fill()
        NSColor(calibratedRed: 0.4, green: 0.75, blue: 0.95, alpha: 1).setFill()
        NSRect(x: 22, y: 386, width: 3, height: 72).fill()
        text(top, x: 37, top: 30, width: 270, height: 22, size: 14, color: NSColor(calibratedWhite: 0.8, alpha: 1))
        text(bottom, x: 37, top: 55, width: 270, height: 29, size: 21)
    }
}

try render("title.png") {
    NSColor(calibratedWhite: 0, alpha: 0.45).setFill()
    NSRect(x: 272, y: 390, width: 310, height: 65).fill()
    text("去 看 一 眼", x: 272, top: 30, width: 310, height: 48, size: 34, center: true)
}
try label("jupiter.png", "航程记录", "木星引力辅助")
try label("kuiper.png", "稍后 · 柯伊伯带", "采样区")
try label("period.png", "历史观测数据", "自转周期 15.92 小时")
try label("later.png", "采样窗口", "十六分钟后")
try label("sealed.png", "样本状态", "封装完成 · 返航准备")
try render("credits.png") {
    NSColor(calibratedRed: 0.018, green: 0.032, blue: 0.055, alpha: 1).setFill()
    NSRect(x: 0, y: 0, width: w, height: h).fill()
    text("去看一眼", x: 40, top: 70, width: 774, height: 52, size: 36, center: true)
    text("2026年合肥市蜀山区创客微剧场", x: 30, top: 148, width: 794, height: 35, size: 23, center: true)
    text("合肥市湖东小学三（2）班、三（6）班", x: 30, top: 203, width: 794, height: 35, size: 22, center: true)
    text("张铭轩  ·  张楚珺  ·  汤兴昊  ·  赵以清  ·  王一初", x: 20, top: 270, width: 814, height: 32, size: 20, center: true)
    text("AI生成影像  ·  480P无台词预览", x: 30, top: 380, width: 794, height: 25, size: 14, color: NSColor(calibratedWhite: 0.66, alpha: 1), center: true)
}
