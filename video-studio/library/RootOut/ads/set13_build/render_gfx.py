#!/usr/bin/env python3
"""Set 13 overlay graphics (PIL, 1080x1920 canvas). Writes RGBA PNGs to work/gfx/.
Cards sit in the upper half so the speaker stays on camera (brief: no voice-over over B-roll)."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps
P = Path(__file__).resolve().parent.parent
G = P / "work/gfx"; G.mkdir(parents=True, exist_ok=True)
FR = P / "raw/gen/frames"; WEB = P / "raw/web"; LIB = P.parents[1] / "library/RootOut/brand/images/pdp"
INTER = "/usr/share/fonts/opentype/inter/Inter-%s.otf"
NEWS = str(P / "assets/fonts/Newsreader_wght_600.ttf"); NEWSI = str(P / "assets/fonts/Newsreader_ital_wght_1_600.ttf")
NAVY, BLUE, ICE, ORANGE, PEACH, SLATE = (11, 42, 91), (23, 99, 184), (238, 244, 250), (224, 78, 24), (255, 237, 227), (74, 85, 104)
W, H = 1080, 1920

def font(w, s): return ImageFont.truetype(INTER % w, s)
def canvas(): return Image.new("RGBA", (W, H), (0, 0, 0, 0))
def shadow(img, r=22, off=10, a=110):
    pad = r * 3; s = Image.new("RGBA", (img.width + 2 * pad, img.height + 2 * pad), (0, 0, 0, 0))
    m = img.split()[3].point(lambda v: a if v > 0 else 0)
    s.paste((0, 0, 0, 255), (pad, pad + off), m); s = s.filter(ImageFilter.GaussianBlur(r)); s.alpha_composite(img, (pad, pad)); return s
def rounded(img, r):
    m = Image.new("L", img.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, img.width - 1, img.height - 1), r, fill=255)
    o = img.convert("RGBA"); o.putalpha(m); return o
def place(card, cx, cy, name):
    c = canvas(); s = shadow(card); c.alpha_composite(s, (int(cx - s.width / 2), int(cy - s.height / 2))); c.save(G / name); print(name)

def text_box(lines, size=58, weight="ExtraBold", fg=(20, 20, 24), bg=(255, 255, 255), padx=30, pady=16, r=18):
    """Swipe-style white caption box (Amoils #003 look)."""
    f = font(weight, size); d0 = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    ws = [d0.textlength(l, font=f) for l in lines]; lh = int(size * 1.18)
    img = Image.new("RGBA", (int(max(ws) + 2 * padx), lh * len(lines) + 2 * pady), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    d.rounded_rectangle((0, 0, img.width - 1, img.height - 1), r, fill=bg + (255,))
    for i, l in enumerate(lines): d.text(((img.width - ws[i]) / 2, pady + i * lh - size * 0.06), l, font=f, fill=fg)
    return img

# 1. hook titles (on-screen text from the brief; H2/H3 mirror its style)
for name, lines in {"t_h1": ["Flaked right off.", "No tears."], "t_h2": ["Scared of anything", "touching it."],
                    "t_h3": ["She made the sign", "herself."]}.items():
    place(text_box(lines, 64), W / 2, 330, name + ".png")

# 2. phone gallery: 4 photos of the same finger, swiped on "Dry, then dark, then it flaked off. Smooth skin"
def gallery(i, src):
    cw, ch = 760, 1080; card = Image.new("RGBA", (cw, ch), (255, 255, 255, 255)); d = ImageDraw.Draw(card)
    d.text((34, 28), "‹  Photos", font=font("SemiBold", 34), fill=BLUE)
    t = f"{i} of 4"; f = font("SemiBold", 32); d.text((cw - 34 - d.textlength(t, font=f), 30), t, font=f, fill=SLATE)
    ph = ImageOps.fit(Image.open(src).convert("RGB"), (cw, 900), Image.LANCZOS, centering=(0.45, 0.55)); card.paste(ph, (0, 92))
    for k in range(4):
        x = cw / 2 - 45 + k * 30; d.ellipse((x, 1022, x + 14, 1036), fill=(NAVY if k == i - 1 else (200, 206, 214)))
    lab = text_box(["AI illustration"], 24, "SemiBold", (255, 255, 255), (0, 0, 0), 14, 6, 10); lab.putalpha(lab.split()[3].point(lambda v: int(v * .7)))
    card.alpha_composite(lab, (cw - lab.width - 18, 92 + 900 - lab.height - 18))
    return rounded(card, 44)
stages = [FR / f"S{k}.png" for k in (1, 2, 3, 4)]
for i, s in enumerate(stages, 1):
    if s.exists():
        g = gallery(i, s); g = g.resize((int(g.width * 0.66), int(g.height * 0.66)), Image.LANCZOS)
        place(g, 790, 760, f"gal_{i}.png")

# 3. real web screenshots framed as a phone-browser card (exact quote highlighted in the capture itself)
def web_card(src, host, w=820, crop=None):
    shot = Image.open(src).convert("RGB")
    if crop: shot = shot.crop(crop)
    pad, bar = 20, 96; s = (w - 2 * pad) / shot.width; shot = shot.resize((w - 2 * pad, int(shot.height * s)), Image.LANCZOS)
    card = Image.new("RGBA", (w, bar + shot.height + pad), (255, 255, 255, 255)); d = ImageDraw.Draw(card)
    d.rectangle((0, 0, w, bar), fill=(242, 242, 246)); d.rounded_rectangle((pad, 18, w - pad, bar - 16), 24, fill=(226, 226, 232))
    f = font("Medium", 32); tw = d.textlength(host, font=f); x = (w - tw) / 2 + 14; lx = x - 36
    d.rounded_rectangle((lx, 42, lx + 20, 60), 3, fill=(90, 90, 98)); d.arc((lx + 3, 30, lx + 17, 50), 180, 360, fill=(90, 90, 98), width=3)
    d.text((x, 28), host, font=f, fill=(40, 40, 48)); card.paste(shot, (pad, bar)); return rounded(card, 36)
for name, host in {"w_freeze": None, "w_comeback": None, "w_kids4": "trywillomd.com", "w_offer": "trywillomd.com"}.items():
    src = WEB / f"cards/{name}.png"
    if src.exists():
        meta = (WEB / f"cards/{name}.host").read_text().strip() if (WEB / f"cards/{name}.host").exists() else host
        wd = 640 if name == "w_offer" else 820
        place(web_card(src, meta, wd), W / 2, 600 if name == "w_offer" else 560, name + "_card.png")

# 4. plant chips (real CC photos): one per named plant, stacked down the right side
def chip(src, label):
    d0 = 210; ph = ImageOps.fit(Image.open(src).convert("RGB"), (d0, d0), Image.LANCZOS)
    m = Image.new("L", (d0, d0), 0); ImageDraw.Draw(m).ellipse((0, 0, d0 - 1, d0 - 1), fill=255)
    f = font("Bold", 38); tw = int(ImageDraw.Draw(Image.new("RGB", (1, 1))).textlength(label, font=f))
    img = Image.new("RGBA", (max(d0 + 16, tw + 48), d0 + 80), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    cx = (img.width - d0) // 2; d.ellipse((cx - 8, -0, cx + d0 + 8, d0 + 8), fill=(255, 255, 255, 255))
    img.paste(ph, (cx, 4), m)
    d.rounded_rectangle(((img.width - tw) / 2 - 22, d0 + 18, (img.width + tw) / 2 + 22, d0 + 74), 28, fill=NAVY + (255,))
    d.text(((img.width - tw) / 2, d0 + 22), label, font=f, fill=(255, 255, 255)); return img
for k, (key, label) in enumerate((("lemon", "Lemon"), ("teatree", "Tea tree"), ("pokeweed", "Pokeweed"), ("cedar", "White cedar"))):
    src = WEB / f"plants/pick_{key}.jpg"
    if src.exists():
        c = canvas(); s = shadow(chip(src, label), 14, 6, 90); cx = 135 + k * 270
        c.alpha_composite(s, (int(cx - s.width / 2), 1010)); c.save(G / f"plant_{key}.png"); print("plant", key)

# 5. footnotes (CLAIMS.md: † travels with "8x deeper", * with the plants breaking the wart down)
def foot(txt, name, y=1795, size=26):
    f = font("Medium", size); d0 = ImageDraw.Draw(Image.new("RGB", (1, 1))); words, lines, cur = txt.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d0.textlength(t, font=f) > 960: lines.append(cur); cur = w_
        else: cur = t
    lines.append(cur); c = canvas(); d = ImageDraw.Draw(c)
    for i, l in enumerate(lines):
        tw = d.textlength(l, font=f); x = (W - tw) / 2; yy = y + i * (size + 6)
        d.text((x, yy), l, font=f, fill=(255, 255, 255, 235), stroke_width=3, stroke_fill=(0, 0, 0, 150))
    c.save(G / name); print(name)
foot("†Up to 8x deeper: based on our manufacturer's absorption testing against a regular cream.", "fn_dagger.png")
foot("*Benefit claims. Homeopathic claims are based on traditional homeopathic practice, not accepted medical evidence, and are not FDA evaluated. Results vary.", "fn_star.png", 1760)

# 6. "8x" depth chip beside the side cut
def pill(txt, bg, fg=(255, 255, 255), size=46, weight="ExtraBold"):
    return text_box([txt], size, weight, fg, bg, 34, 14, 40)
place(pill("up to 8x deeper†", BLUE), W / 2, 1000, "p_8x.png")
place(pill("+14 nights after it looks gone", PEACH, NAVY, 42, "Bold"), W / 2, 330, "p_rootrule.png")
place(pill("Buy 2, get 1 free  ·  90-day money-back", ORANGE, size=40), W / 2, 330, "p_offer.png")
place(pill("Kids' formula · ages 4+", NAVY, size=42), W / 2, 330, "p_kids.png")
for i, t in enumerate(("1  File", "2  Brush", "3  Cover"), 1): place(pill(t, BLUE, size=48), W / 2, 300, f"p_step{i}.png")

# 7. end card (full frame): split dandelion + bottle, brand palette
def end_card():
    c = Image.new("RGBA", (W, H), ICE + (255,)); d = ImageDraw.Draw(c)
    for y in range(H):  # soft vertical gradient ice -> white
        k = y / H; d.line((0, y, W, y), fill=(int(238 + 17 * k), int(244 + 11 * k), int(250 + 5 * k), 255))
    fN = ImageFont.truetype(NEWS, 112); fNi = ImageFont.truetype(NEWSI, 112)
    for i, (t, f) in enumerate((("Not the top.", fN), ("The root.", fNi))):
        tw = d.textlength(t, font=f); d.text(((W - tw) / 2, 210 + i * 128), t, font=f, fill=NAVY)
    # dandelion icon pair: snapped (left) vs whole with root (right)
    def dand(x0, whole):
        g, soil = (78, 140, 60), (150, 110, 70)
        d.line((x0, 980, x0 + 140, 980), fill=soil, width=6)
        top = 760 if whole else 960
        if whole:
            d.line((x0 + 70, 980, x0 + 70, 770), fill=g, width=8)
            for k in range(14): import math; a = k / 14 * 2 * math.pi; d.line((x0 + 70, 760, x0 + 70 + 38 * math.cos(a), 760 + 38 * math.sin(a)), fill=(250, 200, 30), width=7)
            d.ellipse((x0 + 54, 744, x0 + 86, 776), fill=(245, 180, 20))
            d.line((x0 + 70, 980, x0 + 66, 1150), fill=(235, 228, 205), width=10); d.line((x0 + 66, 1080, x0 + 40, 1130), fill=(235, 228, 205), width=5)
        else:
            d.line((x0 + 70, 980, x0 + 70, 955), fill=g, width=8)
            d.line((x0 + 70, 980, x0 + 66, 1150), fill=(235, 228, 205), width=10); d.line((x0 + 66, 1080, x0 + 92, 1125), fill=(235, 228, 205), width=5)
            d.text((x0 + 18, 1170), "freezing", font=font("SemiBold", 30), fill=SLATE)
        return top
    dand(120, False); dand(820, True); d.text((828, 1170), "RootOut", font=font("Bold", 30), fill=NAVY)
    b = Image.open(LIB / "A12-duo-transparent.png").convert("RGBA"); b.thumbnail((560, 620), Image.LANCZOS)
    c.alpha_composite(shadow(b, 26, 18, 70), (int((W - b.width) / 2) - 78, 560))
    btn = pill("Buy 2, get 1 free", ORANGE, size=54); c.alpha_composite(shadow(btn), (int((W - btn.width) / 2) - 66, 1290))
    f = font("SemiBold", 34); t = "90-day money-back  ·  trywillomd.com"; d.text(((W - d.textlength(t, font=f)) / 2, 1470), t, font=f, fill=NAVY)
    f = font("Medium", 26); t = "AI illustration."; d.text(((W - d.textlength(t, font=f)) / 2, 1840), t, font=f, fill=SLATE)
    c.convert("RGB").save(G / "endcard.png"); print("endcard.png")
end_card()

# 8. real photo card (dandelion with its whole taproot, Wikimedia Commons CC) for "from the root"
def photo_card(src, name, w=600, credit=""):
    im = Image.open(src).convert("RGB"); s = w / im.width; im = im.resize((w, int(im.height * s)), Image.LANCZOS)
    if im.height > 1000: im = im.crop((0, (im.height - 1000) // 2, w, (im.height - 1000) // 2 + 1000))
    card = Image.new("RGBA", (w + 24, im.height + 24 + (40 if credit else 0)), (255, 255, 255, 255)); card.paste(im, (12, 12))
    if credit: ImageDraw.Draw(card).text((16, im.height + 22), credit, font=font("Medium", 20), fill=SLATE)
    c = canvas(); s_ = shadow(rounded(card, 28)); c.alpha_composite(s_, (int(W / 2 - s_.width / 2), 120)); c.save(G / name); print(name)
rp = WEB / "dandelion/commons_dandelion_plant_with_root_zimmerling.jpg"
if rp.exists(): photo_card(rp, "photo_root.png", 520, "Photo: Wikimedia Commons")

cp = WEB / "freezing/commons_wart_cryotherapy_toe_swab.jpg"
if cp.exists(): photo_card(cp, "photo_cryo.png", 640, "Cryotherapy on a wart · Photo: Wikimedia Commons")

# 9. v2 hook: bigger two-tone title + before/after proof pop (swipe #003 does its before/after at 2-4 s)
def hook_title(l1, l2, name):
    a = text_box([l1], 76, "ExtraBold", (20, 20, 24), (255, 255, 255), 34, 16, 22)
    b = text_box([l2], 76, "ExtraBold", (255, 255, 255), ORANGE, 34, 16, 22)
    img = Image.new("RGBA", (max(a.width, b.width), a.height + b.height + 10), (0, 0, 0, 0))
    img.alpha_composite(a, ((img.width - a.width) // 2, 0)); img.alpha_composite(b, ((img.width - b.width) // 2, a.height + 10))
    img = img.rotate(-2, resample=Image.BICUBIC, expand=True); place(img, W / 2, 270, name)
hook_title("Flaked right off.", "No tears.", "t_h1.png")
hook_title("Scared of anything", "touching it.", "t_h2.png")
hook_title("She made the sign", "herself.", "t_h3.png")

def before_after():
    pw, ph = 420, 540; card = Image.new("RGBA", (2 * pw + 60, ph + 110), (255, 255, 255, 255)); d = ImageDraw.Draw(card)
    for k, (src, lab) in enumerate(((FR / "S1.png", "Before"), (FR / "S4.png", "2 weeks later"))):
        im = Image.open(src).convert("RGB"); sw, sh = im.size; cw_ = sw * 0.42; ch_ = cw_ * ph / pw
        im = im.crop((int(sw * .55 - cw_ / 2), int(sh * .53 - ch_ / 2), int(sw * .55 + cw_ / 2), int(sh * .53 + ch_ / 2))).resize((pw, ph), Image.LANCZOS); x = 20 + k * (pw + 20)
        card.paste(rounded(im, 22), (x, 20), rounded(im, 22))
        f = font("Bold", 36); tw = d.textlength(lab, font=f)
        d.rounded_rectangle((x + (pw - tw) / 2 - 20, ph + 36, x + (pw + tw) / 2 + 20, ph + 92), 28, fill=(NAVY if k == 0 else (21, 128, 61)))
        d.text((x + (pw - tw) / 2, ph + 41), lab, font=f, fill=(255, 255, 255))
    # arrow between
    cx, cy = card.width // 2, 20 + ph // 2
    d.ellipse((cx - 38, cy - 38, cx + 38, cy + 38), fill=ORANGE); d.polygon([(cx - 12, cy - 18), (cx + 18, cy), (cx - 12, cy + 18)], fill=(255, 255, 255))
    lab = text_box(["AI illustration"], 22, "SemiBold", (255, 255, 255), (0, 0, 0), 12, 5, 8); card.alpha_composite(lab, (card.width - lab.width - 30, ph - lab.height + 6))
    place(rounded(card, 34), W / 2, 820, "ba.png")
before_after()
