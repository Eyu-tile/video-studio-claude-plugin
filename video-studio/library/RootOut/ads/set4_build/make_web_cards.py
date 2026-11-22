#!/usr/bin/env python3
"""Real web screenshots (raw/web, captured by the b-roll pass) cropped to the exact sentence and framed as a phone
browser card with the source address. Quotes and URLs: WEB_SOURCES.md. No logos, text unchanged."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont
P = Path("/home/user/video-studio-claude-plugin/video-studio/projects/rootout-set4")
W = 860; PAD = 18; BAR = 92; R = 34
FB = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"
CARDS = {  # name: (screenshot, crop box, host shown in the address bar)
    "w_tape": ("duct_aafp_little_evidence", (0, 70, 860, 258), "aafp.org"),
    "w_acid": ("acid_nhs_3_months_irritate", (0, 84, 860, 300), "nhs.uk"),
    "w_freeze": ("cryo_aafp_repeat_2_3_weeks", (0, 34, 860, 116), "aafp.org"),
    "w_cryo": ("comeback_cc_reappear", (0, 84, 860, 470), "my.clevelandclinic.org"),
}
def card(src, box, host, out):
    shot = Image.open(src).convert("RGB").crop(box); s = (W - 2 * PAD) / shot.width
    shot = shot.resize((W - 2 * PAD, int(shot.height * s)), Image.LANCZOS)
    H = BAR + shot.height + PAD
    c = Image.new("RGBA", (W, H), (0, 0, 0, 0)); m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, W - 1, H - 1), R, fill=255)
    body = Image.new("RGB", (W, H), (255, 255, 255)); d = ImageDraw.Draw(body)
    d.rectangle((0, 0, W, BAR), fill=(242, 242, 246)); d.rounded_rectangle((PAD, 18, W - PAD, BAR - 16), 22, fill=(226, 226, 232))
    f = ImageFont.truetype(FB, 30); tw = d.textlength(host, font=f); x = (W - tw) / 2 + 14; lx, ly = x - 34, 30
    d.rounded_rectangle((lx, ly + 12, lx + 20, ly + 30), 3, fill=(90, 90, 98)); d.arc((lx + 3, ly, lx + 17, ly + 20), 180, 360, fill=(90, 90, 98), width=3)
    d.text((x, 27), host, font=f, fill=(40, 40, 48)); body.paste(shot, (PAD, BAR)); c.paste(body, (0, 0), m)
    sh = Image.new("RGBA", (W + 80, H + 80), (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((40, 50, W + 40, H + 50), R, fill=(0, 0, 0, 120))
    sh = sh.filter(ImageFilter.GaussianBlur(18)); sh.paste(c, (40, 40), c); sh.save(out); print(out.name, sh.size)
if __name__ == "__main__":
    (P / "assets/graphics").mkdir(parents=True, exist_ok=True)
    for n, (src, box, host) in CARDS.items(): card(P / "raw/web" / f"{src}.png", box, host, P / "assets/graphics" / f"{n}_card.png")
