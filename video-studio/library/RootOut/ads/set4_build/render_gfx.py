#!/usr/bin/env python3
"""Set 4 code graphics (free): fridge calendar (14 X + "+14"), offer card, end card, web-source cards.
render_gfx.py [calendar offer end webcards]  -> work/gfx/*.mp4 | assets/graphics/*.png"""
import math, random, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import numpy as np

P = Path("/home/user/video-studio-claude-plugin/video-studio/projects/rootout-set4")
LIB = Path("/home/user/video-studio-claude-plugin/video-studio/library/RootOut")
W, H, FPS = 1080, 1920, 30
NAVY, BLUE, ICE, MIST, ORANGE, WHITE = "#0B2A5B", "#1763B8", "#EEF4FA", "#D9E2EC", "#E04E18", "#FFFFFF"
SERIF = str(P / "assets/fonts/Newsreader.ttf")
INTER_B, INTER_X, INTER_M = (f"/usr/share/fonts/opentype/inter/Inter-{w}.otf" for w in ("Bold", "ExtraBold", "Medium"))
OUT = P / "work/gfx"; OUT.mkdir(parents=True, exist_ok=True)

def F(path, size, var=None):
    f = ImageFont.truetype(path, size)
    if var: f.set_variation_by_name(var)
    return f

def smooth(x): x = max(0.0, min(1.0, x)); return x * x * (3 - 2 * x)
def back(x): x = max(0.0, min(1.0, x)); c = 1.5; return 1 + (c + 1) * (x - 1) ** 3 + c * (x - 1) ** 2

def encode(frames, out, dur):
    ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                           "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", str(out)], stdin=subprocess.PIPE)
    for k in range(int(dur * FPS)): ff.stdin.write(frames(k / FPS).convert("RGB").tobytes())
    ff.stdin.close(); ff.wait(); print(out.name)

def bottle_cutout():
    """Flood-fill the white studio background from the image border (keeps the white label and cap)."""
    im = Image.open(LIB / "brand/images/pdp/A01-bottle-front-white.jpg").convert("RGB")
    a = np.asarray(im).astype(np.int16)
    near = (a.min(-1) > 236)  # near-white
    from collections import deque
    h, w = near.shape; bg = np.zeros((h, w), bool); q = deque()
    for x in range(w):
        for y in (0, h - 1):
            if near[y, x]: bg[y, x] = True; q.append((y, x))
    for y in range(h):
        for x in (0, w - 1):
            if near[y, x] and not bg[y, x]: bg[y, x] = True; q.append((y, x))
    while q:
        y, x = q.popleft()
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            yy, xx = y + dy, x + dx
            if 0 <= yy < h and 0 <= xx < w and near[yy, xx] and not bg[yy, xx]: bg[yy, xx] = True; q.append((yy, xx))
    m = Image.fromarray(((~bg) * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.0))
    rgba = im.convert("RGBA"); rgba.putalpha(m); bb = rgba.getbbox()
    rgba = rgba.crop(bb)
    # drop the soft floor shadow under the base (bottom rows that are mostly light grey)
    arr = np.asarray(rgba); keep = arr.shape[0]
    for yy in range(arr.shape[0] - 1, 0, -1):
        row = arr[yy]; solid = row[row[:, 3] > 200]
        if len(solid) and solid[:, :3].mean() < 200: keep = yy + 1; break
    return rgba.crop((0, 0, rgba.width, keep))

def bg_grad(top=(238, 244, 250), bot=(205, 220, 236)):
    g = Image.new("RGB", (W, H)); d = ImageDraw.Draw(g)
    for y in range(H):
        k = y / H; d.line([(0, y), (W, y)], fill=tuple(int(a + (b - a) * k) for a, b in zip(top, bot)))
    return g

def shadow_paste(base, im, x, y, blur=26, off=18, op=90):
    sh = Image.new("RGBA", base.size, (0, 0, 0, 0)); m = im.getchannel("A")
    sh.paste((11, 42, 91, op), (int(x), int(y + off)), m); sh = sh.filter(ImageFilter.GaussianBlur(blur))
    base.alpha_composite(sh); base.alpha_composite(im, (int(x), int(y)))

# ---------------- calendar ----------------
def calendar(dur=5.0):
    rnd = random.Random(4)
    paper = Image.new("RGBA", (900, 1060), (252, 250, 244, 255)); d = ImageDraw.Draw(paper)
    d.rectangle((0, 0, 900, 150), fill=(23, 99, 184, 255))
    d.text((450, 78), "DECEMBER", font=F(INTER_X, 72), fill=WHITE, anchor="mm")
    cw, ch, x0, y0 = 124, 150, 15, 190
    for i, dn in enumerate("SMTWTFS"): d.text((x0 + cw * i + cw / 2, y0 - 16), dn, font=F(INTER_B, 30), fill=(90, 100, 120), anchor="mm")
    cells = []
    for r in range(5):
        for c in range(7):
            n = r * 7 + c + 1
            if n > 31: continue
            bx, by = x0 + c * cw, y0 + 10 + r * ch
            d.rectangle((bx, by, bx + cw, by + ch), outline=(200, 205, 214), width=2)
            d.text((bx + 12, by + 8), str(n), font=F(INTER_M, 28), fill=(70, 80, 96))
            cells.append((bx, by))
    def fr(t):
        im = bg_grad((233, 228, 220), (210, 204, 196)).convert("RGBA")
        dd = ImageDraw.Draw(im)
        for k in range(0, H, 6): dd.line([(0, k), (W, k)], fill=(222, 217, 209, 255))  # fridge sheen lines
        pg = paper.copy(); pd = ImageDraw.Draw(pg)
        n = int(min(14, max(0, (t - 0.3) / 0.16)))
        for i in range(n):  # crayon X marks
            bx, by = cells[i]; j = rnd.Random(i) if False else random.Random(i)
            for a, b in (((bx + 22, by + 46), (bx + cw - 22, by + ch - 18)), ((bx + cw - 22, by + 46), (bx + 22, by + ch - 18))):
                pd.line([(a[0] + j.uniform(-4, 4), a[1]), (b[0] + j.uniform(-4, 4), b[1])], fill=(224, 78, 24, 255), width=11)
        if t > 2.9:  # "+14" in marker
            u = smooth((t - 2.9) / 0.5); bx, by = cells[14]
            f = F(INTER_X, 110); lay = Image.new("RGBA", (360, 160), (0, 0, 0, 0))
            ImageDraw.Draw(lay).text((10, 10), "+14", font=f, fill=(21, 128, 61, int(255 * u)))
            pg.alpha_composite(lay.rotate(-6, expand=True), (bx + 20, by + 10))
        rot = pg.rotate(1.5, expand=True, resample=Image.BICUBIC)
        z = 1 + 0.04 * t / dur; rw = int(rot.width * z * 1.0); rh = int(rot.height * z)
        rot = rot.resize((rw, rh), Image.BICUBIC)
        shadow_paste(im, rot, (W - rw) / 2, 380 - (z - 1) * 300)
        for mx in (W / 2 - 300, W / 2 + 300):  # magnets
            dd = ImageDraw.Draw(im); dd.ellipse((mx - 34, 360, mx + 34, 428), fill=(224, 78, 24, 255))
        return im
    encode(fr, OUT / "g_calendar.mp4", dur)

# ---------------- offer card ----------------
def offer(dur=4.6):
    b = bottle_cutout(); bh = 760; b = b.resize((int(b.width * bh / b.height), bh), Image.LANCZOS)
    def fr(t):
        im = bg_grad().convert("RGBA"); d = ImageDraw.Draw(im)
        d.text((W / 2, 250), "Three for the", font=F(SERIF, 104, "SemiBold"), fill=NAVY, anchor="mm")
        d.text((W / 2, 360), "price of two", font=F(SERIF, 104, "SemiBold"), fill=NAVY, anchor="mm")
        for i, dx in enumerate((-300, 0, 300)):
            u = back((t - 0.15 - 0.22 * i) / 0.5)
            if u <= 0: continue
            y = 1240 - bh - (1 - u) * 260; x = W / 2 + dx - b.width / 2
            bb = b.copy()
            if u < 1: bb.putalpha(bb.getchannel("A").point(lambda a: int(a * min(1, u * 1.5))))
            shadow_paste(im, bb, x, y)
            if i == 2 and t > 1.0:
                s = back((t - 1.0) / 0.45); r = 92 * s; cx, cy = x + b.width - 10, y + 40
                d = ImageDraw.Draw(im); d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=ORANGE)
                if s > 0.7: d.text((cx, cy), "FREE", font=F(INTER_X, int(46 * s)), fill=WHITE, anchor="mm")
        d = ImageDraw.Draw(im)
        if t > 1.5:
            u = smooth((t - 1.5) / 0.4); y = 1400 + (1 - u) * 60
            d.rounded_rectangle((150, y, 930, y + 120), 60, fill=NAVY)
            d.text((W / 2, y + 60), "Buy 2, get 1 free", font=F(INTER_X, 56), fill=WHITE, anchor="mm")
        if t > 1.9:
            u = smooth((t - 1.9) / 0.4); cx, cy, r = W / 2, 1680, 92 + 6 * math.sin(t * 5)
            d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=BLUE, width=8, fill=WHITE)
            d.text((cx, cy - 22), "90-DAY", font=F(INTER_X, 34), fill=NAVY, anchor="mm")
            d.text((cx, cy + 22), "money-back", font=F(INTER_B, 26), fill=NAVY, anchor="mm")
        return im
    encode(fr, OUT / "g_offer.mp4", dur)

# ---------------- end card ----------------
def dandelion_icon(snapped, s=1.0):
    im = Image.new("RGBA", (260, 520), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    gy = 250
    if snapped:
        d.rectangle((0, gy, 260, 520), fill=(214, 190, 150, 255)); d.line([(0, gy), (260, gy)], fill=(160, 132, 90, 255), width=5)
        d.line([(130, gy - 30), (130, gy)], fill=(96, 150, 60, 255), width=10)
        d.line([(118, gy - 34), (142, gy - 24)], fill=(96, 150, 60, 255), width=6)
        d.line([(130, gy), (136, 470)], fill=WHITE, width=16)  # root left in the ground
        d.text((130, 500), "", fill=NAVY)
    else:  # the whole plant lifted out, long white root and all
        d.rectangle((0, 440, 260, 520), fill=(214, 190, 150, 255))
        d.line([(0, 440), (260, 440)], fill=(160, 132, 90, 255), width=5)
        d.line([(130, 70), (130, 210)], fill=(96, 150, 60, 255), width=10)
        for k in range(12):
            a = k * math.pi / 6; d.ellipse((130 + 34 * math.cos(a) - 18, 70 + 34 * math.sin(a) - 18, 130 + 34 * math.cos(a) + 18, 70 + 34 * math.sin(a) + 18), fill=(250, 200, 40, 255))
        d.ellipse((110, 50, 150, 90), fill=(240, 170, 20, 255))
        d.polygon([(118, 210), (142, 210), (136, 410), (128, 418)], fill=(255, 255, 255, 255), outline=(200, 190, 170, 255))
        d.line([(132, 300), (100, 340)], fill=WHITE, width=5); d.line([(134, 350), (166, 384)], fill=WHITE, width=5)
    return im

def end(dur=3.2):
    b = bottle_cutout(); bh = 820; b = b.resize((int(b.width * bh / b.height), bh), Image.LANCZOS)
    ic1, ic2 = dandelion_icon(True), dandelion_icon(False)
    def fr(t):
        im = bg_grad().convert("RGBA"); d = ImageDraw.Draw(im)
        u = smooth(t / 0.5)
        d.text((W / 2, 230 - (1 - u) * 30), "Not the top.", font=F(SERIF, 118, "SemiBold"), fill=(11, 42, 91, int(255 * u)), anchor="mm")
        u2 = smooth((t - 0.35) / 0.5)
        d.text((W / 2, 370 - (1 - u2) * 30), "The root.", font=F(SERIF, 118, "SemiBoldItalic") if False else F(SERIF, 118, "SemiBold"), fill=(224, 78, 24, int(255 * u2)), anchor="mm")
        y = 1330 - bh + 8 * math.sin(t * 2.4); shadow_paste(im, b, W / 2 - b.width / 2, y)
        im.alpha_composite(ic1, (60, 780)); im.alpha_composite(ic2, (W - 320, 780))
        d = ImageDraw.Draw(im)
        d.text((190, 1330), "freezing", font=F(INTER_B, 34), fill=(110, 116, 130), anchor="mm")
        d.text((W - 190, 1330), "RootOut", font=F(INTER_B, 34), fill=NAVY, anchor="mm")
        if t > 0.8:
            u3 = smooth((t - 0.8) / 0.4); yy = 1450 + (1 - u3) * 40
            d.rounded_rectangle((120, yy, 960, yy + 124), 62, fill=ORANGE)
            d.text((W / 2, yy + 62), "Buy 2, get 1 free", font=F(INTER_X, 58), fill=WHITE, anchor="mm")
            d.text((W / 2, yy + 200), "90-day money-back", font=F(INTER_B, 44), fill=NAVY, anchor="mm")
        d.text((W / 2, 1860), "AI illustration.", font=F(INTER_M, 30), fill=(90, 100, 120), anchor="mm")
        return im
    encode(fr, OUT / "g_end.mp4", dur)


# ---------------- real CC stills as slow push-in clips (Ken Burns), 9:16 cover ----------------
STILLS = {  # name: (file in assets/images, focus x,y (0..1), zoom from, zoom to)
    "s_tape": ("wikimedia_61966358_duct-tape-20170827-jpg.jpg", (0.43, 0.8), 1.6, 1.8),
    "s_acid": ("wikimedia_6101020_plantar-wart-after-treatment-w.jpg", (0.5, 0.45), 1.0, 1.25),
    "s_freeze": ("wikimedia_47599599_wart-cryotherapy-jpg.jpg", (0.45, 0.5), 1.0, 1.18),
    "s_dand_root": ("wikimedia_174390580_dandelion-with-long-root-53644.jpg", (0.5, 0.55), 1.05, 1.2),
    "s_stem": ("openverse_29e9ba9b-0b36-44ed-95a2-_taraxacum-officinale-stem-sap-.jpg", (0.45, 0.6), 1.0, 1.2),
    "s_dand_back": ("wikimedia_70942321_dandelion-grown-in-old-sidewal.jpg", (0.45, 0.55), 1.0, 1.2),
    "s_dand_dry": ("wikimedia_39310783_2015-03-27-14-50-21-lone-dande.jpg", (0.5, 0.45), 1.0, 1.25),
}
def stills(dur=3.0):
    for name, (fn, (fx, fy), z0, z1) in STILLS.items():
        im = Image.open(P / "assets/images" / fn).convert("RGB")
        if name == "s_tape":  # blur the printed brand text inside the core
            bx = (int(im.width * 0.17), int(im.height * 0.27), int(im.width * 0.74), int(im.height * 0.64))
            im.paste(im.crop(bx).filter(ImageFilter.GaussianBlur(28)), bx[:2])
        s = max(W / im.width, H / im.height); base = im.resize((int(im.width * s) + 2, int(im.height * s) + 2), Image.LANCZOS)
        def fr(t, base=base, fx=fx, fy=fy, z0=z0, z1=z1):
            z = z0 + (z1 - z0) * smooth(t / dur); cw, ch = W / z, H / z
            cx = min(max(fx * base.width, cw / 2), base.width - cw / 2); cy = min(max(fy * base.height, ch / 2), base.height - ch / 2)
            return base.crop((int(cx - cw / 2), int(cy - ch / 2), int(cx + cw / 2), int(cy + ch / 2))).resize((W, H), Image.BICUBIC)
        encode(fr, OUT / f"{name}.mp4", dur)

if __name__ == "__main__":
    for job in sys.argv[1:] or ["calendar", "offer", "end"]:
        globals()[job]()
