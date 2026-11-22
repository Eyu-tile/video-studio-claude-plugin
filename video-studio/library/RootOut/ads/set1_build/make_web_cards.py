#!/usr/bin/env python3
"""Frame real web screenshots (raw/web/*.png) as a phone-browser card with the source address, for overlay on 1080x1920."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont
P = Path(__file__).resolve().parent.parent
W = 700; PAD = 18; BAR = 92; R = 34
FB = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"
def card(src, out, host="aad.org"):
    shot = Image.open(src).convert("RGB"); s = (W - 2 * PAD) / shot.width
    shot = shot.resize((W - 2 * PAD, int(shot.height * s)), Image.LANCZOS)
    H = BAR + shot.height + PAD
    c = Image.new("RGBA", (W, H), (0, 0, 0, 0)); m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, W - 1, H - 1), R, fill=255)
    body = Image.new("RGB", (W, H), (255, 255, 255)); d = ImageDraw.Draw(body)
    d.rectangle((0, 0, W, BAR), fill=(242, 242, 246))
    d.rounded_rectangle((PAD, 18, W - PAD, BAR - 16), 22, fill=(226, 226, 232))
    f = ImageFont.truetype(FB, 30); tw = d.textlength(host, font=f); x = (W - tw) / 2 + 14
    lx, ly = x - 34, 30  # lock icon
    d.rounded_rectangle((lx, ly + 12, lx + 20, ly + 30), 3, fill=(90, 90, 98)); d.arc((lx + 3, ly, lx + 17, ly + 20), 180, 360, fill=(90, 90, 98), width=3)
    d.text((x, 27), host, font=f, fill=(40, 40, 48))
    body.paste(shot, (PAD, BAR))
    c.paste(body, (0, 0), m)
    sh = Image.new("RGBA", (W + 80, H + 80), (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((40, 50, W + 40, H + 50), R, fill=(0, 0, 0, 120))
    sh = sh.filter(ImageFilter.GaussianBlur(18)); sh.paste(c, (40, 40), c); sh.save(out); print(out.name, sh.size)
for n in ("w1_acid", "w2_freeze", "w3_repeat"):
    card(P / f"raw/web/{n}.png", P / f"assets/graphics/{n}_card.png")
