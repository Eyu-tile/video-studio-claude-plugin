#!/usr/bin/env python3
"""Set 16 code-made graphics (1080x1920, 30 fps, always moving). Brand: navy #0B2A5B, blue #1763B8, ice #EEF4FA,
orange #E04E18; Newsreader + Inter. No disclaimer text (house rule L1).
Outputs to projects/rootout-set16/assets/graphics/: depth_sink.mp4 (thin oil sinks vs cream blob stays, 8x gauge fills),
depth_carry.mp4 (gauge full, label), endcard.mp4 (bottle + snapped-vs-whole dandelion icon), hook_h1/h2/h3.png."""
import math, subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

WS = Path("/home/user/video-studio-claude-plugin/video-studio")
OUT = WS / "projects/rootout-set16/assets/graphics"; OUT.mkdir(parents=True, exist_ok=True)
DUO = WS / "library/RootOut/brand/images/pdp/A12-duo-transparent.png"
W, H, FPS = 1080, 1920, 30
NAVY, BLUE, ICE, ORANGE, WHITE = (11, 42, 91), (23, 99, 184), (238, 244, 250), (224, 78, 24), (255, 255, 255)
NEWS = str(Path.home() / ".fonts/Newsreader-SemiBold.ttf"); INTER = "/usr/share/fonts/opentype/inter/Inter-{}.otf"
F = lambda p, s: ImageFont.truetype(p, s)
ease = lambda x: 0.5 - 0.5 * math.cos(math.pi * max(0, min(1, x)))
SKIN = [(246, 222, 160), (240, 205, 140), (232, 186, 160), (226, 150, 150), (214, 124, 128), (200, 104, 110)]


def video(name, dur, draw):
    n = int(dur * FPS)
    p = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                          "-i", "-", "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", str(OUT / f"{name}.mp4")], stdin=subprocess.PIPE)
    for i in range(n):
        p.stdin.write(draw(i / FPS, i / max(1, n - 1)).convert("RGB").tobytes())
    p.stdin.close(); p.wait(); print(name, dur)


def bg(t):
    im = Image.new("RGB", (W, H), ICE); d = ImageDraw.Draw(im)
    cx, cy = 540 + 160 * math.sin(t * 0.5), 760 + 120 * math.cos(t * 0.4)
    for r in range(900, 0, -60):
        a = int(18 * (1 - r / 900)); d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(ICE[0] - a, ICE[1] - a // 2, ICE[2]))
    return im


def layers(d, x0, x1, y0, y1):
    h = (y1 - y0) / len(SKIN)
    for i, c in enumerate(SKIN):
        d.rectangle((x0, y0 + i * h, x1, y0 + (i + 1) * h), fill=c)
    for i in range(1, 4):  # hard-top crack lines
        yy = y0 + i * h / 4; d.line((x0, yy, x1, yy), fill=(214, 182, 118), width=3)


def depth(t, k, phase):
    """Left: thick white cream blob sits on top. Right: a clear oil drop sinks down the layers. Gauge fills to 8x."""
    im = bg(t); d = ImageDraw.Draw(im)
    y0, y1 = 620, 1460
    layers(d, 90, 520, y0, y1); layers(d, 560, 990, y0, y1)
    d.line((540, y0 - 40, 540, y1 + 20), fill=(190, 200, 215), width=4)
    fb = F(INTER.format("Bold"), 46)
    for x, s in ((305, "regular cream"), (775, "thin oil")):
        w = d.textlength(s, font=fb); d.text((x - w / 2, y0 - 120), s, font=fb, fill=NAVY)
    wob = 6 * math.sin(t * 3)
    d.ellipse((215 + wob, y0 - 70, 395 - wob, y0 + 30), fill=WHITE, outline=(205, 210, 220), width=4)  # cream stays on top
    sink = ease(k * 1.2) if phase == "sink" else 1.0
    yy = y0 - 40 + sink * (y1 - y0 - 40)
    for j in range(14):  # soaked trail
        ty = y0 + (yy - y0) * j / 14; d.ellipse((760 - 10, ty - 10, 790 + 10, ty + 10), fill=(250, 200, 70))
    d.ellipse((745, yy - 34, 805, yy + 34), fill=(255, 214, 90), outline=(214, 160, 40), width=4)
    gx, g0, g1 = 1030, y0, y1
    d.rounded_rectangle((gx - 26, g0, gx + 26, g1), 26, fill=WHITE, outline=NAVY, width=4)
    fill = min(g1 - 40, g1 - (g1 - g0 - 12) * sink)
    d.rounded_rectangle((gx - 16, fill, gx + 16, g1 - 8), 16, fill=BLUE)
    if phase == "label" or sink > 0.95:
        fl = F(NEWS, 92); s = "up to 8x deeper"; w = d.textlength(s, font=fl)
        d.rounded_rectangle(((W - w) / 2 - 40, 1560, (W + w) / 2 + 40, 1690), 50, fill=WHITE)
        d.text(((W - w) / 2, 1572), s, font=fl, fill=NAVY)
    z = 1 + 0.05 * k
    big = im.resize((int(W * z), int(H * z)), Image.LANCZOS); ox, oy = (big.width - W) // 2, (big.height - H) // 2
    return big.crop((ox, oy, ox + W, oy + H))


def dandelion_icon(d, cx, cy, s, whole):
    d.line((cx, cy, cx, cy + 90 * s), fill=(70, 140, 60), width=int(8 * s))
    if whole:
        d.ellipse((cx - 34 * s, cy - 34 * s, cx + 34 * s, cy + 34 * s), fill=(250, 200, 40))
        pts = [(cx, cy + 90 * s), (cx - 8 * s, cy + 170 * s), (cx + 6 * s, cy + 240 * s), (cx - 4 * s, cy + 300 * s)]
        d.line(pts, fill=(245, 240, 225), width=int(10 * s), joint="curve")
    else:
        d.line((cx - 20 * s, cy + 2 * s, cx + 20 * s, cy - 6 * s), fill=(120, 90, 60), width=int(5 * s))
    d.line((cx - 80 * s, cy + 90 * s, cx + 80 * s, cy + 90 * s), fill=(160, 120, 80), width=int(6 * s))


def endcard(t, k):
    im = bg(t); d = ImageDraw.Draw(im)
    b = Image.open(DUO).convert("RGBA"); s = 700 / b.width; b = b.resize((700, int(b.height * s)), Image.LANCZOS)
    y = 600 - 14 * math.sin(t * 1.6); im.paste(b, ((W - b.width) // 2, int(y)), b)
    f1 = F(NEWS, 104)
    for i, line in enumerate(("Not the top.", "The root.")):
        w = d.textlength(line, font=f1); d.text(((W - w) / 2, 210 + i * 116), line, font=f1, fill=NAVY)
    dandelion_icon(d, 170, 1160, 0.9, False); dandelion_icon(d, 910, 1160, 0.9, True)
    pulse = 1 + 0.04 * math.sin(t * 5); bw, bh = 640 * pulse, 130 * pulse
    d.rounded_rectangle(((W - bw) / 2, 1560 - bh / 2, (W + bw) / 2, 1560 + bh / 2), 65, fill=ORANGE)
    f3 = F(INTER.format("Bold"), 56); s3 = "Buy 2, get 1 free"; w = d.textlength(s3, font=f3); d.text(((W - w) / 2, 1526), s3, font=f3, fill=WHITE)
    return im


def hook(name, lines):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im); f = F(INTER.format("ExtraBold"), 70)
    y = 250
    for line in lines:
        w = d.textlength(line, font=f)
        d.rounded_rectangle(((W - w) / 2 - 30, y - 12, (W + w) / 2 + 30, y + 92), 22, fill=WHITE)
        d.text(((W - w) / 2, y), line, font=f, fill=(20, 20, 20)); y += 112
    im.save(OUT / f"{name}.png")


if __name__ == "__main__":
    hook("hook_h1", ["Months. And it kept", "getting bigger."])
    hook("hook_h2", ["Getting bigger", "by the day."])
    hook("hook_h3", ["I thought it was", "a splinter."])
    video("depth_sink", 3.0, lambda t, k: depth(t, k, "sink"))
    video("depth_label", 2.8, lambda t, k: depth(t + 3, k, "label"))
    video("endcard", 3.2, endcard)
