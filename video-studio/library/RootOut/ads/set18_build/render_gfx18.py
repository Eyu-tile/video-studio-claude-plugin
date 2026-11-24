#!/usr/bin/env python3
"""Set 18 graphics (code, free): phone-browser web cards, hook box, chips, offer pill, 90-day seal, and full-frame
animated clips (split circle, freeze calendar, 14-night calendar, skin side cut, end card). Out: assets/graphics/."""
import math, subprocess, os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont
P = Path(os.environ.get("S18", "/home/user/video-studio-claude-plugin/video-studio/projects/rootout-set18"))
LIB = Path("/home/user/video-studio-claude-plugin/video-studio/library/RootOut")
G = P / "assets/graphics"; G.mkdir(parents=True, exist_ok=True)
W, H, FPS = 1080, 1920, 30
NAVY, BLUE, ICE, ORANGE, WHITE, INK = (11, 42, 91), (23, 99, 184), (238, 244, 250), (224, 78, 24), (255, 255, 255), (20, 24, 32)
F = lambda w, s: ImageFont.truetype(f"/usr/share/fonts/opentype/inter/Inter-{w}.otf", s)

def shadowed(img, r=34, blur=18, off=10, alpha=120):
    w, h = img.size; sh = Image.new("RGBA", (w + 80, h + 80), (0, 0, 0, 0))
    m = Image.new("L", (w, h), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, w - 1, h - 1), r, fill=alpha)
    sh.paste((0, 0, 0, alpha), (40, 40 + off), m); sh = sh.filter(ImageFilter.GaussianBlur(blur)); sh.alpha_composite(img, (40, 40)); return sh

def web_card(src, out, host, crop=None, width=860):
    shot = Image.open(src).convert("RGB")
    if crop: shot = shot.crop(crop)
    PAD, BAR, R = 20, 104, 38; s = (width - 2 * PAD) / shot.width
    shot = shot.resize((width - 2 * PAD, int(shot.height * s)), Image.LANCZOS); h = BAR + shot.height + PAD
    body = Image.new("RGBA", (width, h), WHITE + (255,)); d = ImageDraw.Draw(body)
    d.rectangle((0, 0, width, BAR), fill=(242, 242, 246)); d.rounded_rectangle((PAD, 20, width - PAD, BAR - 18), 24, fill=(226, 226, 232))
    f = F("Medium", 34); tw = d.textlength(host, font=f); x = (width - tw) / 2 + 16; lx, ly = x - 38, 34
    d.rounded_rectangle((lx, ly + 13, lx + 22, ly + 33), 3, fill=(90, 90, 98)); d.arc((lx + 3, ly, lx + 19, ly + 22), 180, 360, fill=(90, 90, 98), width=3)
    d.text((x, 31), host, font=f, fill=(40, 40, 48)); body.paste(shot, (PAD, BAR))
    m = Image.new("L", body.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, width - 1, h - 1), R, fill=255)
    card = Image.new("RGBA", body.size, (0, 0, 0, 0)); card.paste(body, (0, 0), m); shadowed(card, R).save(out)

def pill(text, out, bg=ORANGE, fg=WHITE, size=64, weight="ExtraBold", padx=44, pady=26, r=None, strike=False):
    f = F(weight, size); tw = int(ImageDraw.Draw(Image.new("RGB", (1, 1))).textlength(text, font=f))
    w, h = tw + 2 * padx, size + 2 * pady; img = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    d.rounded_rectangle((0, 0, w - 1, h - 1), r if r is not None else h // 2, fill=bg)
    d.text((padx, pady - size * 0.12), text, font=f, fill=fg)
    if strike: d.line((padx - 8, h // 2 + 2, w - padx + 8, h // 2 + 2), fill=ORANGE, width=9)
    shadowed(img, h // 2, 14, 6, 90).save(out)

def hook_box(text, out):  # top-centre hook box, swipe style (two-tone: white text on orange)
    pill(text, out, ORANGE, WHITE, 68, "ExtraBold", 46, 28, r=22)

def seal(out):
    S = 360; img = Image.new("RGBA", (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    d.ellipse((10, 10, S - 10, S - 10), fill=NAVY); d.ellipse((28, 28, S - 28, S - 28), outline=WHITE, width=5)
    for i in range(36):
        a = i / 36 * 2 * math.pi; r1, r2 = S / 2 - 12, S / 2 - 2
        d.line((S / 2 + r1 * math.cos(a), S / 2 + r1 * math.sin(a), S / 2 + r2 * math.cos(a), S / 2 + r2 * math.sin(a)), fill=ICE, width=4)
    for txt, y, f in (("90", 92, F("Black", 128)), ("DAY", 222, F("ExtraBold", 44)), ("MONEY BACK", 268, F("Bold", 30))):
        tw = d.textlength(txt, font=f); d.text(((S - tw) / 2, y - (20 if txt == "90" else 0)), txt, font=f, fill=WHITE)
    shadowed(img, S // 2, 16, 8, 100).save(out)

def plants(out):
    names = [("Lemon", (246, 196, 40)), ("Tea tree", (200, 228, 236)), ("Pokeweed", (106, 54, 140)), ("White cedar", (86, 150, 70))]
    f = F("Bold", 44); w, h = 900, 120; img = Image.new("RGBA", (w, h * 2 + 20), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    for i, (n, c) in enumerate(names):
        x, y = (i % 2) * (w // 2 + 10), (i // 2) * (h + 20); d.rounded_rectangle((x, y, x + w // 2 - 10, y + h), 60, fill=WHITE + (240,))
        cx, cy = x + 62, y + h // 2; d.ellipse((cx - 30, cy - 22, cx + 30, cy + 38), fill=c); d.polygon([(cx - 26, cy - 4), (cx + 26, cy - 4), (cx, cy - 48)], fill=c)
        d.text((x + 112, y + 32), n, font=f, fill=NAVY)
    shadowed(img, 60, 14, 6, 80).save(out)

def gauge_frames(out_dir, n=36):
    out_dir.mkdir(exist_ok=True)
    for k in range(n):
        p = min(1, k / (n * 0.8)); img = Image.new("RGBA", (300, 820), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
        d.rounded_rectangle((90, 20, 210, 700), 60, fill=WHITE + (230,), outline=NAVY, width=6)
        top = 700 - 6 - int(p * 660)
        if top < 640: d.rounded_rectangle((102, max(32, top), 198, 688), 50, fill=BLUE)
        for i in range(1, 8): yy = 700 - i * 85; d.line((70, yy, 90, yy), fill=NAVY, width=5)
        t = f"{max(1, round(p * 8))}x"; f = F("Black", 92); tw = d.textlength(t, font=f); d.text(((300 - tw) / 2, 712), t, font=f, fill=WHITE, stroke_width=6, stroke_fill=NAVY)
        img.save(out_dir / f"g{k:03d}.png")

def anim(name, dur, draw):
    """Render a full-frame 1080x1920 animation: draw(d, img, t) per frame -> mp4."""
    out = G / f"{name}.mp4"; n = int(dur * FPS)
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", str(out)], stdin=subprocess.PIPE)
    for i in range(n):
        img = Image.new("RGB", (W, H), ICE); d = ImageDraw.Draw(img); draw(d, img, i / FPS); p.stdin.write(img.tobytes())
    p.stdin.close(); p.wait()

ease = lambda x: 1 - (1 - max(0, min(1, x))) ** 3
def centered(d, y, txt, f, fill=NAVY):
    tw = d.textlength(txt, font=f); d.text(((W - tw) / 2, y), txt, font=f, fill=fill)

def split_circle(d, img, t):  # "Half don't."
    cx, cy, r = W // 2, 860, 330; fade = ease((t - 0.35) / 0.8)
    d.pieslice((cx - r, cy - r, cx + r, cy + r), 90, 270, fill=tuple(int(a + (b - a) * fade) for a, b in zip(BLUE, ICE)), outline=NAVY, width=8)
    d.pieslice((cx - r, cy - r, cx + r, cy + r), -90, 90, fill=ORANGE, outline=NAVY, width=8)
    d.line((cx, cy - r, cx, cy + r), fill=NAVY, width=8)
    f = F("ExtraBold", 54); d.text((cx - r - 10, cy + r + 50), "gone in a year", font=f, fill=tuple(int(a + (b - a) * fade * 0.7) for a, b in zip(NAVY, ICE)))
    d.text((cx + 40, cy + r + 50), "still there", font=f, fill=ORANGE)
    centered(d, 300, "Half of kids' warts", F("Black", 78))

def freeze_cal(d, img, t):  # three Thursdays marked "freeze", pen circles the third
    x0, y0, cw, ch = 90, 520, 128, 150; d.rounded_rectangle((60, 330, W - 60, 1420), 40, fill=WHITE, outline=(210, 216, 224), width=4)
    centered(d, 380, "MARCH", F("Black", 70)); days = "SMTWTFS"
    for i, c in enumerate(days): d.text((x0 + i * cw + 46, y0 - 70), c, font=F("Bold", 40), fill=(120, 128, 140))
    for wk in range(5):
        for dy in range(7):
            x, y = x0 + dy * cw, y0 + wk * ch; day = wk * 7 + dy + 1
            if day > 31: continue
            d.rectangle((x, y, x + cw - 8, y + ch - 8), outline=(225, 230, 236), width=2)
            d.text((x + 10, y + 8), str(day), font=F("Medium", 32), fill=(140, 146, 156))
            if dy == 4 and wk in (0, 2, 3):
                k = (0, 2, 3).index(wk)
                if t > 0.15 + k * 0.3: d.text((x + 8, y + 70), "freeze", font=F("ExtraBold", 30), fill=ORANGE)
                if wk == 3 and t > 1.2:
                    a = ease((t - 1.2) / 0.5) * 360; d.arc((x - 14, y - 10, x + cw + 6, y + ch + 2), -90, -90 + a, fill=ORANGE, width=8)

def nights_cal(d, img, t):  # 14 crayon ticks fill
    d.rounded_rectangle((90, 420, W - 90, 1380), 40, fill=WHITE, outline=(210, 216, 224), width=4)
    centered(d, 470, "NIGHTS", F("Black", 70))
    for i in range(14):
        x, y = 160 + (i % 7) * 115, 640 + (i // 7) * 260; d.rounded_rectangle((x, y, x + 95, y + 200), 14, outline=(200, 206, 214), width=4)
        d.text((x + 28, y + 12), str(i + 1), font=F("Bold", 38), fill=(140, 146, 156))
        if t > 0.1 + i * 0.13:
            d.line((x + 18, y + 80, x + 78, y + 180), fill=BLUE, width=14); d.line((x + 78, y + 80, x + 18, y + 180), fill=BLUE, width=14)

def side_cut(d, img, t):  # hard top over a long white root; a new bump pushes up
    d.rectangle((0, 0, W, 520), fill=(220, 232, 244)); d.rectangle((0, 520, W, 760), fill=(214, 196, 160))   # hard top
    for i in range(0, W, 46): d.line((i, 520 + (i * 37 % 60), i + 30, 760 - (i * 13 % 50)), fill=(190, 170, 132), width=3)
    d.rectangle((0, 760, W, H), fill=(244, 196, 190))
    cx = W // 2; grow = ease((t - 0.6) / 1.4)
    d.line((cx, 540, cx - 20, 900, cx - 30, 1150, cx + 20, 1500, cx - 10, 1760), fill=WHITE, width=36, joint="curve")
    for a, b in ((-120, 1300), (110, 1420), (-80, 1600)): d.line((cx, b - 120, cx + a, b), fill=WHITE, width=16)
    bh = int(30 + 110 * grow); d.ellipse((cx - 130, 530 - bh, cx + 130, 530 + 70), fill=(150, 150, 146))
    for k in range(7): d.ellipse((cx - 70 + k * 22, 500 - bh // 2 + (k % 3) * 14, cx - 60 + k * 22, 510 - bh // 2 + (k % 3) * 14), fill=(40, 40, 40))
    f = F("ExtraBold", 50); d.text((70, 600), "hard top", font=f, fill=NAVY); d.text((cx + 70, 1240), "root", font=f, fill=NAVY)

DUO = Image.open(LIB / "brand/images/pdp/A12-duo-transparent.png").convert("RGBA")
def end_card(d, img, t):
    d.rectangle((0, 0, W, H), fill=ICE); centered(d, 250, "Not the top.", F("Black", 96)); centered(d, 365, "The root.", F("Black", 96), ORANGE)
    bw = 720; b = DUO.resize((bw, int(DUO.height * bw / DUO.width))); y = 560 + int(12 * math.sin(t * 2.2)); img.paste(b, ((W - bw) // 2, y), b)
    # snapped vs whole dandelion icon
    for x, whole in ((130, False), (950, True)):   # snapped (left) vs whole with root (right)
        d.line((x - 70, 1150, x + 70, 1150), fill=(140, 110, 70), width=8)
        d.line((x, 1150, x, 1000), fill=(80, 140, 60), width=12); d.ellipse((x - 55, 930, x + 55, 1040), fill=(246, 196, 40))
        if whole:
            d.line((x, 1150, x - 12, 1260, x + 10, 1340), fill=(250, 246, 236), width=16); d.line((x - 4, 1220, x - 40, 1270), fill=(250, 246, 236), width=8)
        else:
            d.line((x, 1150, x, 1165), fill=(80, 140, 60), width=12)
    centered(d, 1440, "Get 2, the 3rd is on us", F("ExtraBold", 58)); centered(d, 1550, "90-day money back", F("Bold", 48), BLUE)
    pr = 1 + 0.04 * math.sin(t * 5); bw2, bh2 = int(480 * pr), int(120 * pr); x0, y0 = (W - bw2) // 2, 1680
    d.rounded_rectangle((x0, y0, x0 + bw2, y0 + bh2), bh2 // 2, fill=ORANGE); f = F("ExtraBold", 60); tw = d.textlength("Shop now", font=f)
    d.text(((W - tw) / 2, y0 + (bh2 - 60) / 2 - 8), "Shop now", font=f, fill=WHITE)

if __name__ == "__main__":
    WEB = P / "assets/web"
    web_card(WEB / "w1_study_family.png", G / "w1_card.png", "pubmed.ncbi.nlm.nih.gov", crop=(0, 820, 1030, 1400))
    web_card(WEB / "w2_study_half.png", G / "w2_card.png", "pubmed.ncbi.nlm.nih.gov", crop=(0, 900, 1030, 1400))
    web_card(WEB / "w3_aad_goaway.png", G / "w3_card.png", "aad.org", crop=(0, 780, 1030, 1330))
    web_card(WEB / "w4_aad_repeat.png", G / "w4_card.png", "aad.org", crop=(0, 860, 1030, 1330))
    hook_box("The doctor said leave it.", G / "hook_h1.png")
    for n, t in (("week1", "Week 1"), ("week3", "Week 3"), ("week6", "Week 6"), ("x2", "2× as likely"), ("kids4", "Kids' formula · 4+"),
                 ("plus14", "+14 nights"), ("offer", "Get 2, the 3rd is on us")):
        pill(t, G / f"chip_{n}.png", NAVY if n != "offer" else ORANGE, WHITE, 58)
    for n, t in (("noacid", "acid"), ("nofreeze", "freezing"), ("noblister", "blister")):
        pill(t, G / f"chip_{n}.png", WHITE, NAVY, 58, strike=True)
    seal(G / "seal90.png"); plants(G / "plants.png"); gauge_frames(G / "gauge")
    anim("c_split", 2.4, split_circle); anim("c_freezecal", 2.0, freeze_cal); anim("c_nights", 2.6, nights_cal)
    anim("c_sidecut", 3.6, side_cut); anim("c_end", 3.2, end_card)
    print("ok", sorted(p.name for p in G.iterdir()))
