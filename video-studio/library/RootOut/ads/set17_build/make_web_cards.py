#!/usr/bin/env python3
"""Real web pages (raw/web/*.png, phone 430 px @2.5x, phrase highlighted) -> cropped phone-browser cards for 1080x1920 overlay."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont
P = Path(__file__).resolve().parent.parent
W = 820; PAD = 18; BAR = 96; R = 36
FB = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"
CARDS = {  # name: (host, crop y0, y1 in source px)
 "w_pubmed_result": ("pubmed.ncbi.nlm.nih.gov", 140, 1900),
 "w_wiki_pain": ("en.wikipedia.org", 250, 1045),
 "w_aad_spread": ("aad.org", 790, 1675),
 "w_aad_freeze": ("aad.org", 330, 1060),
}
def card(src, out, host, y0, y1):
    shot = Image.open(src).convert("RGB"); shot = shot.crop((0, y0, shot.width, min(y1, shot.height)))
    s = (W - 2 * PAD) / shot.width; shot = shot.resize((W - 2 * PAD, int(shot.height * s)), Image.LANCZOS)
    H = BAR + shot.height + PAD
    c = Image.new("RGBA", (W, H), (0, 0, 0, 0)); m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, W - 1, H - 1), R, fill=255)
    body = Image.new("RGB", (W, H), (255, 255, 255)); d = ImageDraw.Draw(body)
    d.rectangle((0, 0, W, BAR), fill=(242, 242, 246)); d.rounded_rectangle((PAD, 18, W - PAD, BAR - 16), 22, fill=(226, 226, 232))
    f = ImageFont.truetype(FB, 30); tw = d.textlength(host, font=f); x = (W - tw) / 2 + 14; lx, ly = x - 34, 31
    d.rounded_rectangle((lx, ly + 12, lx + 20, ly + 30), 3, fill=(90, 90, 98)); d.arc((lx + 3, ly, lx + 17, ly + 20), 180, 360, fill=(90, 90, 98), width=3)
    d.text((x, 28), host, font=f, fill=(40, 40, 48)); body.paste(shot, (PAD, BAR)); c.paste(body, (0, 0), m)
    sh = Image.new("RGBA", (W + 80, H + 80), (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((40, 50, W + 40, H + 50), R, fill=(0, 0, 0, 120))
    sh = sh.filter(ImageFilter.GaussianBlur(18)); sh.paste(c, (40, 40), c); sh.save(out); print(out.name, sh.size)
for n, (h, a, b) in CARDS.items(): card(P / f"raw/web/{n}.png", P / f"assets/graphics/{n}_card.png", h, a, b)
