#!/usr/bin/env python3
"""Set 20 code-made graphics (1080x1920, 30 fps, always moving: no held frames).
Brand: navy #0B2A5B, blue #1763B8, ice #EEF4FA, orange #E04E18; Newsreader + Inter. No disclaimer text (house rule L1).
Outputs to assets/graphics/: checklist_{0..3}.png overlays, gauge_8x.png, offer.png, and mp4s:
sidecut_root, sidecut_arrows, sidecut_break, calendar, bg_soft, endcard."""
import math, subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

P = Path(__file__).resolve().parent.parent; OUT = P / "assets/graphics"; OUT.mkdir(parents=True, exist_ok=True)
W, H, FPS = 1080, 1920, 30
NAVY, BLUE, ICE, ORANGE, WHITE = (11, 42, 91), (23, 99, 184), (238, 244, 250), (224, 78, 24), (255, 255, 255)
NEWS = str(Path.home() / ".fonts/Newsreader-SemiBold.ttf"); INTER = "/usr/share/fonts/opentype/inter/Inter-{}.otf"
F = lambda p, s: ImageFont.truetype(p, s)
ease = lambda x: 0.5 - 0.5 * math.cos(math.pi * max(0, min(1, x)))


def video(name, dur, draw):
    n = int(dur * FPS)
    p = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                          "-i", "-", "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", str(OUT / f"{name}.mp4")],
                         stdin=subprocess.PIPE)
    for i in range(n):
        p.stdin.write(draw(i / FPS, i / max(1, n - 1)).convert("RGB").tobytes())
    p.stdin.close(); p.wait(); print(name, dur)


def bg(t):
    """Soft ice background with a slowly drifting light blob (never static)."""
    im = Image.new("RGB", (W, H), ICE); d = ImageDraw.Draw(im)
    cx, cy = 540 + 160 * math.sin(t * 0.5), 760 + 120 * math.cos(t * 0.4)
    for r in range(900, 0, -60):
        a = int(18 * (1 - r / 900)); d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(ICE[0] - a, ICE[1] - a // 2, ICE[2]))
    return im


def heel(t, k, mode):
    """Side cut of a heel: soft skin layers, thick hard yellow top with black dots, white root going down.
    mode: root | arrows | break. k = 0..1 progress."""
    im = bg(t); d = ImageDraw.Draw(im)
    z = 1 + 0.06 * k  # slow push-in
    def S(x, y): return (540 + (x - 540) * z, 980 + (y - 980) * z)
    def R(x0, y0, x1, y1): return (*S(x0, y0), *S(x1, y1))
    d.rounded_rectangle(R(110, 760, 970, 1560), 60, fill=(244, 196, 186))           # soft skin block
    for i, y in enumerate((1000, 1180, 1360)):
        d.line((*S(140, y), *S(940, y)), fill=(232, 176, 166), width=4)
    d.rounded_rectangle(R(110, 640, 970, 820), 50, fill=(236, 214, 150))           # hard top
    for i in range(9):
        x = 200 + i * 85 + 18 * math.sin(i * 2.1); d.line((*S(x, 650), *S(x + 30, 700)), fill=(214, 190, 120), width=5)
    root_alpha = 1.0
    if mode == "break": root_alpha = max(0, 1 - ease((k - 0.35) / 0.6))
    # wart core under the top + root
    col = tuple(int(c * root_alpha + s * (1 - root_alpha)) for c, s in zip((250, 248, 240), (244, 196, 186)))
    d.ellipse(R(470, 690, 610, 830), fill=(225, 210, 175))
    pts = []
    for j in range(40):
        y = 820 + j * 17; x = 540 + 26 * math.sin(j / 5 + t * 0.6)
        pts.append(S(x, y))
    if root_alpha > 0.02:
        if mode == "break" and k > 0.35:
            for j in range(0, 39, 3):  # cracked segments drifting apart
                off = 30 * ease((k - 0.35) / 0.6) * (1 if j % 2 else -1)
                a, b = pts[j], pts[min(39, j + 2)]
                d.line((a[0] + off, a[1], b[0] + off, b[1]), fill=col, width=int(26 * z))
        else:
            d.line(pts, fill=col, width=int(26 * z), joint="curve")
    for (x, y) in ((515, 720), (548, 745), (575, 712), (530, 770), (565, 778)):  # black dots
        d.ellipse(R(x - 7, y - 7, x + 7, y + 7), fill=(40, 28, 24))
    lab = F(INTER.format("SemiBold"), 40)
    if mode in ("root", "arrows"):
        a = ease(k / 0.4)
        d.text(S(150, 560), "hard skin", font=lab, fill=NAVY)
        d.text(S(250, 1420), "the root", font=lab, fill=NAVY)
    if mode == "arrows":
        for (y0, y1, x, c, kk) in ((380, 640, 780, ORANGE, ease(k / 0.4)), (1150, 1500, 760, BLUE, ease((k - 0.35) / 0.4))):
            if kk <= 0: continue
            yy = y0 + (y1 - y0) * kk; d.line((*S(x, y0), *S(x, yy)), fill=c, width=14)
            tip = S(x, yy); d.polygon([(tip[0] - 26, tip[1] - 30), (tip[0] + 26, tip[1] - 30), (tip[0], tip[1] + 8)], fill=c)
    if mode == "break":
        for i, c in enumerate(((46, 125, 50), (85, 139, 47))):  # pokeweed + white cedar drops
            y = 560 + 700 * ease(min(1, k / 0.55)); x = 520 + i * 50
            d.ellipse(R(x - 20, y - 28, x + 20, y + 28), fill=c)
    return im


def checklist(n):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    items = ["Tiny black dots", "Sore when squeezed", "Lines go around"]
    f = F(INTER.format("SemiBold"), 44); x0, y0 = 120, 170
    d.rounded_rectangle((x0 - 30, y0 - 30, W - x0 + 30, y0 + 3 * 86 + 10), 34, fill=(255, 255, 255, 236))
    for i, s in enumerate(items):
        y = y0 + i * 86; done = i < n
        d.rounded_rectangle((x0, y, x0 + 54, y + 54), 12, outline=NAVY, width=5, fill=(ORANGE if done else WHITE))
        if done: d.line((x0 + 12, y + 28, x0 + 24, y + 42, x0 + 44, y + 12), fill=WHITE, width=8)
        d.text((x0 + 84, y + 2), s, font=f, fill=NAVY if done or i == n else (120, 135, 160))
    im.save(OUT / f"checklist_{n}.png")


def gauge():
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    x, y0, y1 = 930, 420, 1340
    d.rounded_rectangle((x - 40, y0, x + 40, y1), 40, fill=(255, 255, 255, 220), outline=NAVY, width=5)
    d.rounded_rectangle((x - 28, y0 + 14, x + 28, y1 - 14), 28, fill=BLUE)
    d.rounded_rectangle((W - 440, y1 + 30, W - 40, y1 + 130), 30, fill=(255, 255, 255, 240))
    d.text((W - 405, y1 + 46), "up to 8x deeper", font=F(INTER.format("Bold"), 40), fill=NAVY)
    im.save(OUT / "gauge_8x.png")


def offer():
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    f1, f2 = F(NEWS, 76), F(INTER.format("SemiBold"), 44)
    t1, t2 = "Grab 2, get a 3rd free", "90-day money-back"
    w1 = d.textlength(t1, font=f1); d.rounded_rectangle(((W - w1) / 2 - 50, 1260, (W + w1) / 2 + 50, 1380), 60, fill=ORANGE)
    d.text(((W - w1) / 2, 1272), t1, font=f1, fill=WHITE)
    w2 = d.textlength(t2, font=f2); d.rounded_rectangle(((W - w2) / 2 - 36, 1410, (W + w2) / 2 + 36, 1490), 40, fill=(255, 255, 255, 240))
    d.text(((W - w2) / 2, 1422), t2, font=f2, fill=NAVY)
    im.save(OUT / "offer.png")


def calendar(t, k):
    im = bg(t); d = ImageDraw.Draw(im)
    x0, y0, cw = 120, 560, 120
    d.rounded_rectangle((x0 - 40, y0 - 170, x0 + 7 * cw + 40, y0 + 4 * cw + 60), 30, fill=WHITE)
    d.text((x0, y0 - 140), "Bedtime nights", font=F(NEWS, 64), fill=NAVY)
    fn = F(INTER.format("Medium"), 34)
    for i in range(28):
        cx, cy = x0 + (i % 7) * cw, y0 + (i // 7) * cw
        d.rectangle((cx, cy, cx + cw, cy + cw), outline=(200, 210, 225), width=2)
        d.text((cx + 10, cy + 6), str(i + 1), font=fn, fill=(110, 125, 150))
        on = k * 30 > i + 1
        if on and i < 14:
            d.line((cx + 30, cy + 66, cx + 52, cy + 92, cx + 94, cy + 40), fill=NAVY, width=9)
        if on and i >= 14:
            d.ellipse((cx + 22, cy + 26, cx + 100, cy + 104), outline=ORANGE, width=8)
    f = F(INTER.format("Bold"), 48)
    if k > 0.5: d.text((x0, y0 + 4 * cw + 90), "about 2 weeks", font=f, fill=NAVY)
    if k > 0.9: d.text((x0 + 470, y0 + 4 * cw + 90), "+ 14 nights", font=f, fill=ORANGE)
    return im


def endcard(t, k):
    im = bg(t); d = ImageDraw.Draw(im)
    b = Image.open(P.parents[2] / "video-studio/library/RootOut/brand/images/pdp/A12-duo-transparent.png").convert("RGBA") \
        if (P.parents[2] / "video-studio/library/RootOut/brand/images/pdp/A12-duo-transparent.png").exists() else None
    if b is None:
        b = Image.open(Path("/home/user/video-studio-claude-plugin/video-studio/library/RootOut/brand/images/pdp/A12-duo-transparent.png")).convert("RGBA")
    s = 760 / b.width; b = b.resize((760, int(b.height * s)), Image.LANCZOS)
    y = 560 - 14 * math.sin(t * 1.6); im.paste(b, ((W - b.width) // 2, int(y)), b)
    f1 = F(NEWS, 92); t1 = "Check for the black dots."
    for i, line in enumerate(("Check for the", "black dots.")):
        w = d.textlength(line, font=f1); d.text(((W - w) / 2, 200 + i * 104), line, font=f1, fill=NAVY)
    f2 = F(INTER.format("SemiBold"), 44)
    for i, s2 in enumerate(("Grab 2, get a 3rd free", "90-day money-back")):
        w = d.textlength(s2, font=f2); d.text(((W - w) / 2, 1340 + i * 64), s2, font=f2, fill=NAVY)
    pulse = 1 + 0.05 * math.sin(t * 5); bw, bh = 420 * pulse, 120 * pulse
    d.rounded_rectangle(((W - bw) / 2, 1520 - bh / 2 + 60, (W + bw) / 2, 1520 + bh / 2 + 60), 60, fill=ORANGE)
    f3 = F(INTER.format("Bold"), 52); w = d.textlength("Shop now", font=f3); d.text(((W - w) / 2, 1550), "Shop now", font=f3, fill=WHITE)
    # heel icon with three black dots
    d.ellipse((120, 1080, 300, 1300), fill=(244, 206, 190)); [d.ellipse((190 + dx - 9, 1170 + dy - 9, 190 + dx + 9, 1170 + dy + 9), fill=(40, 28, 24)) for dx, dy in ((0, 0), (26, 14), (8, 32))]
    return im


if __name__ == "__main__":
    for n in range(4): checklist(n)
    gauge(); offer()
    video("sidecut_root", 3.0, lambda t, k: heel(t, k, "root"))
    video("sidecut_arrows", 3.5, lambda t, k: heel(t, k, "arrows"))
    video("sidecut_break", 6.0, lambda t, k: heel(t, k, "break"))
    video("calendar", 6.0, calendar)
    video("bg_soft", 7.0, lambda t, k: bg(t))
    video("endcard", 4.0, endcard)
