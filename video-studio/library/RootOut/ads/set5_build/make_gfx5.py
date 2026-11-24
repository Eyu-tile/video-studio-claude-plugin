#!/usr/bin/env python3
"""Set 5 graphics (1080x1920). Writes to projects/rootout-set5/assets/graphics/:
- stamp_N{1,3,7,10,14}.png  crayon "NIGHT n" chapter stamps (overlay on the next shot, blurred-in; swipe device #2)
- redx.png                  red brush X for the grey "old fix" shots (swipe device #3/#4)
- gauge_8x.png              depth gauge for "up to 8x deeper" (no footnote mark on screen: house rule L1)
- c_night1.png, c_dots.png, c_repeat.png, c_tiers.png, c_guarantee.png   real web screenshots framed as phone cards
- calendar14.mp4            paper calendar: 14 crayon X's land, then "+14" is written
- endcard.mp4               "Try this before the freeze." + offer + bottle + snapped/whole dandelion icon
House rules: no 'AI illustration' / disclaimer text, no on-screen credits."""
import subprocess, math, random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

P = Path("/home/user/video-studio-claude-plugin/video-studio/projects/rootout-set5")
L = Path("/home/user/video-studio-claude-plugin/video-studio/library/RootOut")
WEB = L / "ads/set5_build/web"; OUT = P / "assets/graphics"; OUT.mkdir(parents=True, exist_ok=True)
W, H, FPS = 1080, 1920, 30
CRAYON = str(P / "assets/fonts/CaveatBrush-Regular.ttf"); NEWS = str(P / "assets/fonts/Newsreader.ttf")
INTER_B = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"; INTER_M = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"
NAVY, BLUE, ICE, ORANGE = (11, 42, 91), (23, 99, 184), (238, 244, 250), (224, 78, 24)
CRAY = (236, 112, 34)


def crayon_text(text, size, color=CRAY, rot=-4, seed=1):
    """Text that looks drawn with a wax crayon: rough edge + grain + slight wobble."""
    random.seed(seed)
    f = ImageFont.truetype(CRAYON, size); tmp = ImageDraw.Draw(Image.new("L", (1, 1)))
    x0, y0, x1, y1 = tmp.textbbox((0, 0), text, font=f); w, h = x1 - x0 + 80, y1 - y0 + 80
    m = Image.new("L", (w, h), 0); d = ImageDraw.Draw(m)
    for dx, dy in ((0, 0), (2, 1), (-1, 2), (1, -1)):  # several passes = waxy stroke
        d.text((40 - x0 + dx, 40 - y0 + dy), text, font=f, fill=200)
    grain = Image.effect_noise((w, h), 90).point(lambda v: 255 if v > 70 else 0)
    m = Image.composite(m, Image.new("L", (w, h), 0), grain).filter(ImageFilter.GaussianBlur(0.6))
    im = Image.new("RGBA", (w, h), color + (0,)); im.putalpha(m)
    return im.rotate(rot, expand=True, resample=Image.BICUBIC)


def stamps():
    for n in (1, 3, 7, 10, 14):
        im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        t = crayon_text(f"NIGHT {n}", 320, seed=n, rot=-5 + (n % 3) * 2)
        cx, cy = (W - t.width) // 2, 640 - t.height // 2
        a = t.split()[3].point(lambda v: 255 if v > 30 else 0)
        for blur, k, off in ((26, 0.75, 12), (8, 0.95, 5)):  # soft dark halo + tight dark edge so it reads on bright shots
            sh = a.filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(blur)).point(lambda v, k=k: int(v * k))
            im.alpha_composite(Image.merge("RGBA", (*Image.new("RGB", t.size, (25, 12, 4)).split(), sh)), (cx + off, cy + off))
        im.alpha_composite(t, (cx, cy)); im.save(OUT / f"stamp_N{n}.png")


def redx():
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    c, s = (W // 2, 760), 260
    for k in range(5):
        o = k * 3 - 6
        d.line((c[0] - s + o, c[1] - s, c[0] + s + o, c[1] + s), fill=(214, 32, 38, 235), width=58)
        d.line((c[0] + s + o, c[1] - s, c[0] - s + o, c[1] + s), fill=(214, 32, 38, 235), width=58)
    im.filter(ImageFilter.GaussianBlur(1.2)).save(OUT / "redx.png")


def gauge():
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    x, y0, y1, w = 900, 520, 1360, 70
    d.rounded_rectangle((x - 16, y0 - 90, x + w + 16, y1 + 24), 34, fill=(255, 255, 255, 215))
    d.rounded_rectangle((x, y0, x + w, y1), 26, fill=(220, 228, 238, 255))
    d.rounded_rectangle((x, y0 + 40, x + w, y1), 26, fill=BLUE + (255,))
    f = ImageFont.truetype(INTER_B, 54); d.text((x + w // 2, y0 - 50), "8x", font=f, fill=NAVY, anchor="mm")
    fs = ImageFont.truetype(INTER_M, 24)
    for i, lab in enumerate(("1x", "4x", "8x")):
        yy = y1 - 30 - i * (y1 - y0 - 80) / 2; d.line((x - 30, yy, x - 6, yy), fill=(255, 255, 255, 230), width=4)
        d.text((x - 38, yy), lab, font=fs, fill=(255, 255, 255, 240), anchor="rm", stroke_width=3, stroke_fill=(20, 30, 60))
    im.save(OUT / "gauge_8x.png")


def phone_card(name, src, box, host="trywillomd.com", hl=None, cursor=None, CW=760, out=None):
    shot = Image.open(WEB / src).convert("RGB").crop(box)
    if hl:  # yellow highlight on a region (in crop coordinates)
        o = Image.new("RGBA", shot.size, (0, 0, 0, 0)); ImageDraw.Draw(o).rounded_rectangle(hl, 18, outline=(255, 205, 0, 255), width=10)
        shot = Image.alpha_composite(shot.convert("RGBA"), o).convert("RGB")
    s = (CW - 36) / shot.width; shot = shot.resize((CW - 36, int(shot.height * s)), Image.LANCZOS)
    BAR = 96; Hc = BAR + shot.height + 18
    body = Image.new("RGB", (CW, Hc), "white"); d = ImageDraw.Draw(body)
    d.rectangle((0, 0, CW, BAR), fill=(242, 242, 246)); d.rounded_rectangle((18, 20, CW - 18, BAR - 18), 24, fill=(226, 226, 232))
    f = ImageFont.truetype(INTER_M, 30); d.text((CW // 2 + 12, BAR // 2), host, font=f, fill=(40, 40, 48), anchor="mm")
    lx = CW // 2 + 12 - d.textlength(host, font=f) / 2 - 34; d.rounded_rectangle((lx, 44, lx + 20, 62), 3, fill=(90, 90, 98)); d.arc((lx + 3, 32, lx + 17, 52), 180, 360, fill=(90, 90, 98), width=3)
    body.paste(shot, (18, BAR))
    if cursor:  # a tap ring + hand cursor in crop coords
        cx, cy = 18 + cursor[0] * s, BAR + cursor[1] * s
        d.ellipse((cx - 34, cy - 34, cx + 34, cy + 34), outline=(23, 99, 184), width=6)
        d.ellipse((cx - 10, cy - 10, cx + 10, cy + 10), fill=(23, 99, 184))
    m = Image.new("L", (CW, Hc), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, CW - 1, Hc - 1), 34, fill=255)
    card = Image.new("RGBA", (CW, Hc)); card.paste(body, (0, 0), m)
    sh = Image.new("RGBA", (CW + 90, Hc + 90), (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((45, 58, CW + 45, Hc + 58), 34, fill=(0, 0, 0, 130))
    sh = sh.filter(ImageFilter.GaussianBlur(20)); sh.alpha_composite(card, (45, 45)); sh.save(out or OUT / f"{name}.png")


def cards():
    phone_card("c_night1", "pdp_3_Night_1_Takes_Two_Minutes.png", (0, 540, 828, 1000))
    phone_card("c_dots", "aad_symptoms_2_plantar.png", (0, 570, 828, 795), host="aad.org")
    phone_card("c_repeat", "aad_treatment_3_Treatment_may_be_repeated.png", (0, 580, 828, 700), host="aad.org")
    # tiers: crop 190..1640; highlight the 90-night bundle (crop coords) and tap it
    phone_card("c_tiers", "pdp_tiers.png", (0, 700, 828, 1640), hl=(26, 440, 802, 780), cursor=(640, 550))
    phone_card("c_guarantee", "pdp_guarantee.png", (0, 240, 828, 600))


def pipe(name, dur, draw):
    p = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", str(OUT / f"{name}.mp4")], stdin=subprocess.PIPE)
    n = int(dur * FPS)
    for k in range(n): p.stdin.write(draw(k / FPS, k).convert("RGB").tobytes())
    p.stdin.close(); p.wait()


def paper_bg(seed=3):
    random.seed(seed)
    wall = Image.new("RGB", (W, H), (196, 160, 118)); n = Image.effect_noise((W, H), 18).convert("RGB")
    wall = Image.blend(wall, n, 0.06)
    # warm lamp falloff from top-left
    g = Image.radial_gradient("L").resize((W * 2, H * 2)).crop((0, 0, W, H)).point(lambda v: int(v * 0.75))
    wall = Image.composite(Image.new("RGB", (W, H), (60, 40, 25)), wall, g)
    return wall


def calendar14(dur=5.2):
    base = paper_bg(); d0 = ImageDraw.Draw(base)
    px, py, pw, ph = 110, 330, 860, 1080
    sheet = Image.new("RGB", (pw, ph), (247, 243, 232)); ds = ImageDraw.Draw(sheet)
    cols, rows = 7, 5; cw, chh = (pw - 60) / cols, (ph - 160) / rows; fN = ImageFont.truetype(INTER_M, 26)
    for r in range(rows + 1): ds.line((30, 130 + r * chh, pw - 30, 130 + r * chh), fill=(120, 120, 120), width=2)
    for c in range(cols + 1): ds.line((30 + c * cw, 130, 30 + c * cw, ph - 30), fill=(120, 120, 120), width=2)
    for i in range(31):
        r, c = divmod(i, 7)
        if r < rows: ds.text((40 + c * cw, 138 + r * chh), str(i + 1), font=fN, fill=(90, 90, 90))
    sheet = sheet.rotate(-1.2, expand=True, fillcolor=(0, 0, 0)); m = Image.new("L", sheet.size, 0)
    ImageDraw.Draw(m).polygon([(6, 18), (sheet.width - 18, 4), (sheet.width - 4, sheet.height - 18), (18, sheet.height - 4)], fill=255)
    base.paste(sheet, (px, py), m)
    for tx, ty in ((px + 40, py - 10), (px + pw - 120, py - 20), (px + 30, py + ph - 40), (px + pw - 110, py + ph - 30)):
        d0.rectangle((tx, ty, tx + 90, ty + 34), fill=(60, 110, 200))
    xs = [crayon_text("X", 150, seed=40 + i, rot=random.Random(i).randint(-14, 12)) for i in range(14)]
    plus = crayon_text("+14", 190, color=(30, 120, 60), seed=99, rot=-8)
    def draw(t, k):
        im = base.copy().convert("RGBA")
        nx = min(14, int(t / 0.17) + 1)
        for i in range(nx):
            r, c = divmod(i, 7); x = px + 30 + c * cw + cw / 2 - xs[i].width / 2; y = py + 130 + r * chh + chh / 2 - xs[i].height / 2
            im.alpha_composite(xs[i], (int(x), int(y)))
        if t > 3.0:
            a = min(1, (t - 3.0) / 0.5); pl = plus.copy(); pl.putalpha(pl.split()[3].point(lambda v: int(v * a)))
            im.alpha_composite(pl, (px + 30 + int(2 * cw), int(py + 130 + 2 * chh)))
        z = 1 + 0.03 * t / dur  # slow push-in (never a held frame)
        im = im.resize((int(W * z), int(H * z)), Image.BICUBIC); ox, oy = (im.width - W) // 2, (im.height - H) // 2
        return im.crop((ox, oy, ox + W, oy + H))
    pipe("calendar14", dur, draw)


def endcard(dur=3.2):
    bot = Image.open(L / "brand/images/pdp/A12-duo-transparent.png").convert("RGBA"); bot = bot.resize((560, int(bot.height * 560 / bot.width)))
    fH = ImageFont.truetype(NEWS, 92); fS = ImageFont.truetype(INTER_B, 46); fP = ImageFont.truetype(INTER_B, 44)
    def dand(d, x, y, whole):  # snapped-vs-whole dandelion icon
        d.rectangle((x - 170, y, x + 170, y + 190), fill=(214, 196, 170)); d.line((x - 170, y, x + 170, y), fill=(120, 90, 60), width=8)
        if whole:
            d.line((x, y + 4, x, y - 150), fill=(60, 120, 60), width=12); d.ellipse((x - 52, y - 250, x + 52, y - 146), fill=(250, 200, 40))
            for k in range(7): d.line((x, y + 4, x + (k - 3) * 18, y + 150 + (k % 2) * 30), fill=(250, 248, 238), width=8)
        else:
            d.line((x, y + 4, x, y - 30), fill=(60, 120, 60), width=12); d.line((x, y + 4, x + 2, y + 150), fill=(250, 248, 238), width=10)
            d.line((x + 40, y - 120, x + 110, y - 50), fill=(214, 32, 38), width=14); d.line((x + 110, y - 120, x + 40, y - 50), fill=(214, 32, 38), width=14)
    def draw(t, k):
        im = Image.new("RGBA", (W, H), ICE + (255,)); d = ImageDraw.Draw(im)
        e = 1 - (1 - min(1, t / 0.5)) ** 3
        d.text((W // 2, 330 + 40 * (1 - e)), "Try this before", font=fH, fill=NAVY, anchor="mm")
        d.text((W // 2, 440 + 40 * (1 - e)), "the freeze.", font=fH, fill=BLUE, anchor="mm")
        fy = 560 + 12 * math.sin(t * 2.4); im.alpha_composite(bot, ((W - bot.width) // 2, int(fy)))
        dand(d, 270, 1300, False); dand(d, 810, 1300, True)
        pulse = 1 + 0.04 * math.sin(t * 6)
        pw, ph = int(640 * pulse), int(110 * pulse); x0, y0 = (W - pw) // 2, 1650 - ph // 2
        d.rounded_rectangle((x0, y0, x0 + pw, y0 + ph), ph // 2, fill=ORANGE); d.text((W // 2, 1650), "Buy 2, get 1 free", font=fP, fill="white", anchor="mm")
        d.text((W // 2, 1770), "90-day money-back", font=fS, fill=NAVY, anchor="mm")
        return im
    pipe("endcard", dur, draw)


def glow():  # soft warm glow over the wart in the night-1 still (hook: "The wart isn't.")
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    cx, cy = int(W * 0.42), int(H * 0.40)
    for r in range(220, 0, -6): d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(255, 190, 90, int(70 * (1 - r / 220) ** 1.6)))
    im.filter(ImageFilter.GaussianBlur(14)).save(OUT / "glow.png")


if __name__ == "__main__":
    glow(); stamps(); redx(); gauge(); cards(); calendar14(); endcard(); print("graphics ->", OUT)
