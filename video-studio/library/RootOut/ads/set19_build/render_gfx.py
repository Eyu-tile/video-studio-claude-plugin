#!/usr/bin/env python3
"""RootOut Set 19 code graphics (PIL -> ffmpeg), 1080x1920, 30 fps.
Brand: navy #0B2A5B, blue #1763B8, ice #EEF4FA, CTA orange #E04E18, Newsreader + Inter.
Outputs to work/gfx/: g_study (real PubMed screenshot, phone browser card), g_house (study card), g_receipt,
g_end (end card), and RGBA overlay frame folders: o_gauge (8x depth gauge + † footnote), o_calendar ("2 weeks + 14 nights")."""
import math, subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

P = Path(__file__).resolve().parent.parent
LIB = P.parents[1] / "library/RootOut"
OUT = P / "work" / "gfx"; OUT.mkdir(parents=True, exist_ok=True)
W, H, FPS = 1080, 1920, 30
NAVY, BLUE, ICE, ORANGE, WHITE = (11, 42, 91), (23, 99, 184), (238, 244, 250), (224, 78, 24), (255, 255, 255)
SERIF = str(P / "assets/fonts/Newsreader.ttf")
IB = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
IM = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"
ISB = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"


def F(path, size, wght=None):
    f = ImageFont.truetype(path, size)
    if wght and path == SERIF:
        try: f.set_variation_by_name('Bold' if wght >= 650 else 'SemiBold')
        except Exception as e: print('font var', e)
    return f


def ease(t): t = max(0.0, min(1.0, t)); return t * t * (3 - 2 * t)
def lerp(a, b, t): return a + (b - a) * t


def write(name, fn, seconds):
    n = int(round(seconds * FPS)); path = OUT / f"{name}.mp4"
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                          "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "16", str(path)], stdin=subprocess.PIPE)
    for i in range(n): p.stdin.write(fn(i / FPS).convert("RGB").tobytes())
    p.stdin.close(); p.wait(); print("wrote", path.name, seconds)


def write_rgba(name, fn, seconds):
    d = OUT / name; d.mkdir(exist_ok=True)
    for i in range(int(round(seconds * FPS))): fn(i / FPS).save(d / f"{i:04d}.png")
    print("wrote", d.name, seconds)


# bottle cutout from the transparent duo render (left half = bottle)
DUO = Image.open(LIB / "brand/images/pdp/A12-duo-transparent.png").convert("RGBA")
BOTTLE = DUO.crop((90, 150, 700, 1280)); BOTTLE = BOTTLE.crop(BOTTLE.getbbox())


def shadowed(base, im, xy, blur=28, alpha=90):
    sh = Image.new("RGBA", base.size, (0, 0, 0, 0))
    m = im.split()[3].point(lambda v: alpha if v > 10 else 0)
    sh.paste((10, 25, 50, 255), (xy[0] + 14, xy[1] + 26), m)
    base.alpha_composite(sh.filter(ImageFilter.GaussianBlur(blur)))
    base.alpha_composite(im, xy)


# ---------------- g_study: the real PubMed page in a phone browser frame ----------------
SHOT = Image.open(P / "assets/web/pubmed_full.png").convert("RGB")   # 1170 wide, iPhone 13 @3x
# crop off the NIH / PubMed header (no government logo): start at the article title
SHOT = SHOT.crop((0, 700, 1170, 4650))


def g_study(t):
    bg = Image.new("RGBA", (W, H), (226, 232, 240, 255))
    # phone browser card
    cw, ch = 960, 1640; cx, cy = (W - cw) // 2, 150
    card = Image.new("RGBA", (cw, ch), WHITE + (255,)); d = ImageDraw.Draw(card)
    d.rectangle((0, 0, cw, 110), fill=(245, 246, 248))
    d.rounded_rectangle((30, 26, cw - 30, 86), 30, fill=(230, 232, 236))
    d.text((70, 38), "pubmed.ncbi.nlm.nih.gov/19438464", font=F(IM, 30), fill=(70, 75, 85))
    page_w = cw; scale = page_w / SHOT.width
    page = SHOT.resize((page_w, int(SHOT.height * scale)))
    # scroll: hold on title, glide to Methods (1465 kids), then Results (not related / family member)
    keys = [(0.0, 0), (0.7, 0), (1.9, 700), (2.9, 700), (4.3, 1450), (8.5, 1450)]
    y = 0
    for (t0, y0), (t1, y1) in zip(keys, keys[1:]):
        if t0 <= t <= t1: y = lerp(y0, y1, ease((t - t0) / (t1 - t0 + 1e-6))); break
    else: y = keys[-1][1]
    card.paste(page.crop((0, int(y), page_w, int(y) + ch - 110)), (0, 110))
    mask = Image.new("L", (cw, ch), 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, cw, ch), 44, fill=255)
    card.putalpha(mask)
    shadowed(bg, card, (cx, cy + int(30 * (1 - ease(t / 0.5)))))
    d = ImageDraw.Draw(bg)
    d.text((W // 2, 1840), "van Haalen et al., Br J Dermatol 2009 · real study page", font=F(IM, 30), fill=(90, 100, 115), anchor="mm")
    return bg


def g_study_pool(t):
    """close-up of the real Results sentence: 'swimming pool visits were not related to the presence of warts'"""
    bg = Image.new("RGBA", (W, H), (226, 232, 240, 255))
    cw = 1000; scale = 0.95; chh = 560
    page = SHOT.resize((int(SHOT.width * scale), int(SHOT.height * scale)))
    y0 = int(2770 * scale)  # 'environmental factors ... swimming pool visits were not related'
    y0 = int(lerp(y0 + 40, y0, ease(t / 3.0)))
    crop = page.crop((int(40 * scale), y0, int(40 * scale) + cw, y0 + chh))
    card = Image.new("RGBA", (cw, chh), WHITE + (255,)); card.paste(crop, (0, 0))
    m = Image.new("L", (cw, chh), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, cw, chh), 40, fill=255); card.putalpha(m)
    z = 1.0 + 0.06 * ease(t / 4.0); card = card.resize((int(cw * z), int(chh * z)))
    shadowed(bg, card, ((W - card.width) // 2, 560))
    d = ImageDraw.Draw(bg)
    d.text((W // 2, 1560), "pubmed.ncbi.nlm.nih.gov/19438464", font=F(IM, 32), fill=(90, 100, 115), anchor="mm")
    return bg


# ---------------- g_house: one foot icon spreading to two more ----------------
def foot_icon(d, x, y, s, col):
    d.ellipse((x - 34 * s, y - 60 * s, x + 34 * s, y + 70 * s), fill=col)
    for k, (dx, dy, r) in enumerate([(-30, -86, 13), (-8, -98, 12), (14, -96, 11), (32, -86, 10), (44, -70, 9)]):
        d.ellipse((x + dx * s - r * s, y + dy * s - r * s, x + dx * s + r * s, y + dy * s + r * s), fill=col)


def g_house(t):
    im = Image.new("RGBA", (W, H), ICE + (255,)); d = ImageDraw.Draw(im)
    # house outline
    hx, hy, hw, hh = 190, 560, 700, 620
    d.polygon([(hx - 40, hy), (hx + hw // 2, hy - 300), (hx + hw + 40, hy)], fill=NAVY)
    d.rounded_rectangle((hx, hy, hx + hw, hy + hh), 18, fill=WHITE, outline=NAVY, width=10)
    feet = [(hx + 170, hy + 360, (224, 78, 24)), (hx + 350, hy + 360, BLUE), (hx + 530, hy + 360, BLUE)]
    for k, (x, y, col) in enumerate(feet):
        a = 1.0 if k == 0 else ease((t - 0.6 - 0.55 * k) / 0.5)
        if a <= 0: continue
        s = 1.0 * (0.6 + 0.4 * a)
        foot_icon(d, x, y, s, col if k == 0 else tuple(int(lerp(255, c, a)) for c in col))
    d.text((W // 2, 1340), "about 2x", font=F(SERIF, 150, 700), fill=NAVY, anchor="mm")
    d.text((W // 2, 1460), "more likely when a family member has warts", font=F(ISB, 40), fill=NAVY, anchor="mm")
    d.text((W // 2, 1700), "van Haalen 2009 · British Journal of Dermatology · 1,465 schoolkids", font=F(IM, 32), fill=(80, 92, 110), anchor="mm")
    return im


# ---------------- g_receipt ----------------
def g_receipt(t):
    im = Image.new("RGBA", (W, H), (60, 64, 70, 255)); d = ImageDraw.Draw(im)
    # car dashboard-ish backdrop gradient
    for y in range(H): d.line((0, y, W, y), fill=(int(lerp(40, 85, y / H)), int(lerp(42, 80, y / H)), int(lerp(48, 78, y / H))))
    rw, rh = 640, 1100; r = Image.new("RGBA", (rw, rh), (252, 250, 244, 255)); rd = ImageDraw.Draw(r)
    mono = F(IM, 34); big = F(IB, 64)
    lines = ["FAMILY PEDIATRICS", "Visit summary", "", "Office visit       $180.00", "Cryotherapy        $70.00", "",
             "-----------------------------", "TOTAL              $250.00", "", "PAID - CARD", "Thank you"]
    yy = 70
    for ln in lines:
        rd.text((50, yy), ln, font=mono if "TOTAL" not in ln else F(IB, 40), fill=(40, 40, 40)); yy += 70
    rd.text((rw // 2, rh - 150), "$250", font=big, fill=(200, 40, 30), anchor="mm")
    for x in range(0, rw, 24): rd.polygon([(x, rh), (x + 12, rh - 16), (x + 24, rh)], fill=(60, 64, 70, 0))
    rot = r.rotate(-4 + 2 * math.sin(t * 1.5), expand=True, resample=Image.BICUBIC)
    y0 = int(lerp(H, 380, ease(t / 0.45)))
    shadowed(im, rot, ((W - rot.width) // 2, y0))
    return im


# ---------------- g_end ----------------
def dandelion_icon(d, x, y, whole, s=1.0, col=NAVY):
    # flower head + stem; whole=True draws the long white root under a soil line
    d.line((x - 90 * s, y, x + 90 * s, y), fill=(120, 90, 60), width=int(6 * s))
    d.line((x, y, x, y - 120 * s), fill=(70, 130, 60), width=int(8 * s))
    for k in range(12):
        a = k / 12 * 2 * math.pi
        d.ellipse((x + 34 * s * math.cos(a) - 14 * s, y - 150 * s + 34 * s * math.sin(a) - 14 * s,
                   x + 34 * s * math.cos(a) + 14 * s, y - 150 * s + 34 * s * math.sin(a) + 14 * s), fill=(244, 196, 40))
    d.ellipse((x - 18 * s, y - 168 * s, x + 18 * s, y - 132 * s), fill=(230, 160, 20))
    if whole:
        d.line((x, y, x + 6 * s, y + 150 * s), fill=(245, 240, 225), width=int(12 * s))
        d.line((x + 6 * s, y + 150 * s, x - 4 * s, y + 210 * s), fill=(245, 240, 225), width=int(6 * s))
    else:
        d.line((x, y + 4 * s, x + 6 * s, y + 150 * s), fill=(200, 190, 170), width=int(12 * s))
        d.line((x - 30 * s, y - 60 * s, x + 30 * s, y - 90 * s), fill=(224, 78, 24), width=int(7 * s))  # snap mark


def g_end(t):
    im = Image.new("RGBA", (W, H), (250, 246, 240, 255)); d = ImageDraw.Draw(im)
    d.text((W // 2, 250), "Check every foot", font=F(SERIF, 104, 700), fill=NAVY, anchor="mm")
    d.text((W // 2, 370), "tonight.", font=F(SERIF, 104, 700), fill=NAVY, anchor="mm")
    pack = Image.open(LIB / "brand/images/pdp/A08-tier-90-nights-3-pack.jpg").convert("RGBA")
    z = 1.0 + 0.04 * ease(t / 3.5); sz = int(880 * z)
    pk = pack.resize((sz, sz)); m = Image.new("L", pk.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, sz, sz), 48, fill=255)
    pk.putalpha(m); a = ease(t / 0.4)
    shadowed(im, pk, ((W - sz) // 2, int(lerp(560, 470, a))))
    d = ImageDraw.Draw(im)
    dandelion_icon(d, 140, 1500, False, 0.75); dandelion_icon(d, 940, 1500, True, 0.75)
    pill = (220, 1460, 860, 1580)
    pulse = 1 + 0.03 * math.sin(t * 6)
    cxp, cyp = (pill[0] + pill[2]) / 2, (pill[1] + pill[3]) / 2
    pw, ph = (pill[2] - pill[0]) * pulse / 2, (pill[3] - pill[1]) * pulse / 2
    d.rounded_rectangle((cxp - pw, cyp - ph, cxp + pw, cyp + ph), 60, fill=ORANGE)
    d.text((cxp, cyp), "Buy 2, get 1 free", font=F(IB, 54), fill=WHITE, anchor="mm")
    d.text((W // 2, 1660), "90-day money-back", font=F(ISB, 46), fill=NAVY, anchor="mm")
    foot = ("*Benefit claims. Homeopathic claims are based on traditional homeopathic practice,\n"
            "not accepted medical evidence, and are not FDA evaluated. Results vary.")
    d.multiline_text((W // 2, 1820), foot, font=F(IM, 22), fill=(110, 115, 125), anchor="mm", align="center")
    return im


# ---------------- overlays (RGBA) ----------------
def o_gauge(t):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    x0, y0, y1 = 930, 520, 1380
    d.rounded_rectangle((x0 - 30, y0 - 10, x0 + 30, y1 + 10), 30, fill=(255, 255, 255, 200), outline=NAVY + (255,), width=5)
    f = ease((t - 0.3) / 2.2); yy = lerp(y1, y0 + 20, f)
    d.rounded_rectangle((x0 - 20, yy, x0 + 20, y1), 20, fill=BLUE + (255,))
    d.rounded_rectangle((x0 - 20, y1 - 60, x0 + 20, y1), 20, fill=(210, 210, 210, 255))  # cream stays on top
    d.text((x0, y0 - 60), "8x", font=F(IB, 64), fill=NAVY + (255,), anchor="mm", stroke_width=4, stroke_fill=WHITE + (255,))
    d.rounded_rectangle((40, 1790, W - 40, 1880), 20, fill=(0, 0, 0, 120))
    d.text((W // 2, 1835), "†Based on our manufacturer's absorption testing against a regular cream.", font=F(IM, 28),
           fill=WHITE + (255,), anchor="mm")
    return im


def o_calendar(t):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    a = ease((t - 0.4) / 0.6)
    if a > 0:
        box = (130, 1300, 950, 1480)
        d.rounded_rectangle(box, 90, fill=(255, 255, 255, int(235 * a)))
        d.text(((box[0] + box[2]) / 2, (box[1] + box[3]) / 2), "2 weeks + 14 nights", font=F(IB, 70),
               fill=ORANGE + (int(255 * a),), anchor="mm")
        # hand-drawn circle
        n = int(60 * ease((t - 0.8) / 0.9))
        pts = [(540 + 470 * math.cos(2 * math.pi * k / 60 - 1.2) + 6 * math.sin(k), 1390 + 130 * math.sin(2 * math.pi * k / 60 - 1.2)) for k in range(n)]
        if len(pts) > 1: d.line(pts, fill=ORANGE + (255,), width=10)
    return im


if __name__ == "__main__":
    import sys
    todo = sys.argv[1:] or ["g_study", "g_study_pool", "g_house", "g_receipt", "g_end", "o_gauge", "o_calendar"]
    for name in todo:
        fn = globals()[name]; sec = {"g_study": 8.5, "g_house": 4.5, "g_receipt": 2.8, "g_end": 3.5, "g_study_pool": 4.0, "o_gauge": 5.0, "o_calendar": 5.5}[name]
        (write_rgba if name.startswith("o_") else write)(name, fn, sec)
