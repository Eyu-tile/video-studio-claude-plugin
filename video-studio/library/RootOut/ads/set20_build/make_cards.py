#!/usr/bin/env python3
"""Set 20 cards for overlay on 1080x1920: real web screenshots framed as a phone browser (raw/web/*.png),
the van Haalen 2009 citation card, the retyped 'black hole' comment card and two short quote cards.
Brand: navy #0B2A5B, blue #1763B8, ice #EEF4FA, CTA orange #E04E18; Newsreader headlines, Inter body."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

P = Path(__file__).resolve().parent.parent
OUT = P / "assets/graphics"; OUT.mkdir(parents=True, exist_ok=True)
INTER = "/usr/share/fonts/opentype/inter/Inter-{}.otf"
NEWS = str(Path.home() / ".fonts/Newsreader-SemiBold.ttf")
NEWS_I = str(Path.home() / ".fonts/Newsreader-400-italic.ttf")
NAVY, BLUE, ICE, ORANGE = (11, 42, 91), (23, 99, 184), (238, 244, 250), (224, 78, 24)
f = lambda path, size: ImageFont.truetype(path, size)


def shadowed(card, r=34, out=None):
    W, H = card.size
    sh = Image.new("RGBA", (W + 80, H + 80), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((40, 50, W + 40, H + 50), r, fill=(0, 0, 0, 120))
    sh = sh.filter(ImageFilter.GaussianBlur(18)); sh.paste(card, (40, 40), card)
    sh.save(out); print(out.name, sh.size)


def rounded(body, r=34):
    W, H = body.size
    m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, W - 1, H - 1), r, fill=255)
    c = Image.new("RGBA", (W, H), (0, 0, 0, 0)); c.paste(body, (0, 0), m); return c


def wrap(d, text, font, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= width: cur = t
        else: lines.append(cur); cur = w
    return lines + [cur]


def web_card(name, host, crop=(0, 1), W=700, PAD=18, BAR=92):
    shot = Image.open(P / f"raw/web/{name}.png").convert("RGB")
    shot = shot.crop((0, int(shot.height * crop[0]), shot.width, int(shot.height * crop[1]))); s = (W - 2 * PAD) / shot.width
    shot = shot.resize((W - 2 * PAD, int(shot.height * s)), Image.LANCZOS)
    H = BAR + shot.height + PAD
    body = Image.new("RGB", (W, H), (255, 255, 255)); d = ImageDraw.Draw(body)
    d.rectangle((0, 0, W, BAR), fill=(242, 242, 246))
    d.rounded_rectangle((PAD, 18, W - PAD, BAR - 16), 22, fill=(226, 226, 232))
    ft = f(INTER.format("Medium"), 30); tw = d.textlength(host, font=ft); x = (W - tw) / 2 + 14
    lx, ly = x - 34, 30
    d.rounded_rectangle((lx, ly + 12, lx + 20, ly + 30), 3, fill=(90, 90, 98))
    d.arc((lx + 3, ly, lx + 17, ly + 20), 180, 360, fill=(90, 90, 98), width=3)
    d.text((x, 27), host, font=ft, fill=(40, 40, 48)); body.paste(shot, (PAD, BAR))
    shadowed(rounded(body), out=OUT / f"{name}_card.png")


def study_card(W=860):
    H = 980; body = Image.new("RGB", (W, H), (255, 255, 255)); d = ImageDraw.Draw(body); x = 56; y = 52
    d.text((x, y), "BRITISH JOURNAL OF DERMATOLOGY · 2009", font=f(INTER.format("SemiBold"), 26), fill=BLUE); y += 58
    for ln in wrap(d, "Warts in primary schoolchildren: prevalence and relation with environmental factors", f(NEWS, 50), W - 2 * x):
        d.text((x, y), ln, font=f(NEWS, 50), fill=NAVY); y += 60
    y += 22; d.line((x, y, W - x, y), fill=(210, 222, 236), width=3); y += 34
    d.text((x, y), "1,465 children aged 4–12", font=f(INTER.format("Bold"), 40), fill=NAVY); y += 54
    d.text((x, y), "hands and feet examined at four Dutch primary schools", font=f(INTER.format("Regular"), 29), fill=(70, 80, 100)); y += 70
    quote = ("“An increased risk of the presence of warts was found in children with a family member "
             "with warts [odds ratio (OR) 1.9 …]”")
    qf = f(NEWS_I, 38); lines = wrap(d, quote, qf, W - 2 * x - 40)
    d.rounded_rectangle((x - 10, y - 14, W - x + 10, y + len(lines) * 50 + 20), 18, fill=ICE)
    d.rectangle((x - 10, y - 14, x - 2, y + len(lines) * 50 + 20), fill=BLUE)
    for ln in lines: d.text((x + 20, y), ln, font=qf, fill=NAVY); y += 50
    y += 60
    d.text((x, y), "2×", font=f(NEWS, 120), fill=ORANGE)
    d.text((x + 175, y + 30), "about twice as likely when", font=f(INTER.format("SemiBold"), 32), fill=NAVY)
    d.text((x + 175, y + 72), "someone at home has a wart", font=f(INTER.format("SemiBold"), 32), fill=NAVY); y += 170
    for ln in wrap(d, "van Haalen FM, Bruggink SC, Gussekloo J, Assendelft WJ, Eekhof JA. Br J Dermatol 2009;161(1):148–152. "
                      "PMID 19438464", f(INTER.format("Regular"), 22), W - 2 * x):
        d.text((x, y), ln, font=f(INTER.format("Regular"), 22), fill=(110, 118, 134)); y += 30
    body = body.crop((0, 0, W, y + 40)); shadowed(rounded(body), out=OUT / "c_study_card.png")


def heart(d, cx, cy, s, fill):
    d.ellipse((cx - s, cy - s * .7, cx, cy + s * .3), fill=fill); d.ellipse((cx, cy - s * .7, cx + s, cy + s * .3), fill=fill)
    d.polygon([(cx - s * .97, cy - s * .05), (cx + s * .97, cy - s * .05), (cx, cy + s * 1.05)], fill=fill)


def comment_card(W=860):
    """Retyped comment (KP20, 6,169 likes), no username or avatar photo: the script asks for plain type."""
    body = Image.new("RGB", (W, 300), (255, 255, 255)); d = ImageDraw.Draw(body); x = 40; y = 40
    d.ellipse((x, y, x + 76, y + 76), fill=(214, 220, 230))
    d.ellipse((x + 24, y + 14, x + 52, y + 42), fill=(245, 247, 250)); d.pieslice((x + 12, y + 44, x + 64, y + 96), 180, 360, fill=(245, 247, 250))
    tx = x + 100
    d.rounded_rectangle((tx, y + 6, tx + 170, y + 30), 12, fill=(228, 232, 238))  # name withheld
    d.text((tx + 186, y + 2), "· 2y", font=f(INTER.format("Regular"), 26), fill=(150, 156, 168))
    yy = y + 48; cf = f(INTER.format("Medium"), 38)
    for ln in wrap(d, "I was wondering why I had a ‘black hole’ in my foot", cf, W - tx - 130):
        d.text((tx, yy), ln, font=cf, fill=(22, 24, 30)); yy += 50
    d.text((tx, yy + 14), "Reply", font=f(INTER.format("SemiBold"), 26), fill=(150, 156, 168))
    heart(d, W - 70, y + 44, 22, (254, 44, 85))
    hf = f(INTER.format("SemiBold"), 26); t = "6,169"; d.text((W - 70 - d.textlength(t, font=hf) / 2, y + 80), t, font=hf, fill=(110, 116, 128))
    body = body.crop((0, 0, W, yy + 70)); shadowed(rounded(body, 30), r=30, out=OUT / "c_comment_card.png")


def quote_card(name, text, W=800):
    body = Image.new("RGB", (W, 400), ICE); d = ImageDraw.Draw(body); x = 54; y = 40
    d.text((x - 6, y - 30), "“", font=f(NEWS, 140), fill=BLUE); y += 70
    qf = f(NEWS, 54)
    for ln in wrap(d, text, qf, W - 2 * x): d.text((x, y), ln, font=qf, fill=NAVY); y += 64
    y += 18
    import math
    for i in range(5):
        cx, cy, R = x + 18 + i * 42, y + 18, 17
        pts = [(cx + (R if k % 2 == 0 else R * .45) * math.cos(math.radians(-90 + k * 36)),
                cy + (R if k % 2 == 0 else R * .45) * math.sin(math.radians(-90 + k * 36))) for k in range(10)]
        d.polygon(pts, fill=ORANGE)
    body = body.crop((0, 0, W, y + 64)); shadowed(rounded(body, 30), r=30, out=OUT / f"{name}.png")


if __name__ == "__main__":
    for n, h, c in (("w1_dots_nhs", "nhs.uk", (0, .63)), ("w2_pebbles_aad", "aad.org", (.2, .66)),
                    ("w3_nopick_aad", "aad.org", (0, .55)), ("w4_spread_aad", "aad.org", (.18, .58)),
                    ("w6_nhs_spread", "nhs.uk", (0, .55))):
        web_card(n, h, c)
    study_card(); comment_card()
    quote_card("q_flinch_card", "He didn't even flinch.")
    quote_card("q_dots_card", "The black dots were gone by week two. We still did the 14 nights.")
