#!/usr/bin/env python3
"""RootOut Set 1 motion graphics, rendered frame by frame with PIL -> ffmpeg (720x1280, 30 fps).
Brand: navy #0B2A5B, blue #1763B8, ice #EEF4FA, CTA orange #E04E18, Newsreader + Inter. No text inside the skin cut."""
import math, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

P = Path(__file__).resolve().parent.parent
OUT = P / "work" / "gfx"; OUT.mkdir(parents=True, exist_ok=True)
W, H, FPS = 720, 1280, 30
NAVY, BLUE, ICE, ORANGE = (11, 42, 91), (23, 99, 184), (238, 244, 250), (224, 78, 24)
SERIF = str(P / "assets/fonts/Newsreader-SemiBold.ttf")
INTER_B = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
INTER_M = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"
DUO = Image.open(P / "assets/graphics/bottle_cutout_hf.png").convert("RGBA")  # bottle cut out in Higgsfield

def ease(t): t = max(0.0, min(1.0, t)); return t * t * (3 - 2 * t)
def lerp(a, b, t): return a + (b - a) * t
def mix(c1, c2, t): return tuple(int(lerp(a, b, t)) for a, b in zip(c1, c2))
def font(path, size): return ImageFont.truetype(path, size)

def write(name, frames_fn, seconds):
    n = int(round(seconds * FPS)); path = OUT / f"{name}.mp4"
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                          "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "16", str(path)],
                         stdin=subprocess.PIPE)
    for i in range(n):
        p.stdin.write(frames_fn(i / FPS, i).convert("RGB").tobytes())
    p.stdin.close(); p.wait(); print("wrote", path.name, seconds, "s")

# ---------- skin side cut ----------
BX0, BX1, TOP, HARD, BOT = 110, 610, 470, 600, 1060      # block left/right, surface y, hard-layer bottom, block bottom
CX = 360                                                # wart / root centre

def skin_base(soft=0.0, frost=0.0, root_break=0.0, door=0.0):
    im = Image.new("RGB", (W, H), ICE); d = ImageDraw.Draw(im)
    # soft shadow under block
    sh = Image.new("L", (W, H), 0); ImageDraw.Draw(sh).rounded_rectangle((BX0 + 10, TOP + 30, BX1 + 10, BOT + 30), 40, fill=90)
    im.paste((180, 195, 215), mask=sh.filter(ImageFilter.GaussianBlur(25)))
    # lower living skin, vertical gradient
    for y in range(HARD, BOT):
        t = (y - HARD) / (BOT - HARD)
        d.line((BX0, y, BX1, y), fill=mix((244, 170, 160), (226, 120, 118), t))
    # hard top layer (pale, cracked); softens toward a warmer, smoother tone
    hard_col = mix((236, 214, 160), (246, 196, 150), soft)
    d.rectangle((BX0, TOP, BX1, HARD), fill=hard_col)
    for k in range(7):  # strata lines
        y = TOP + 14 + k * 17
        d.line((BX0, y, BX1, y + (4 if k % 2 else -3)), fill=mix((214, 186, 128), hard_col, soft), width=2)
    if frost > 0:  # frost whitens only the hard top
        fr = Image.new("L", (W, H), 0); ImageDraw.Draw(fr).rectangle((BX0, TOP - 30, BX1, HARD), fill=int(205 * frost))
        im.paste((250, 252, 255), mask=fr.filter(ImageFilter.GaussianBlur(6)))
        d = ImageDraw.Draw(im)
    # root: tapering channel from the wart down into the living skin
    rb = root_break
    pts_l, pts_r = [], []
    for k in range(41):
        t = k / 40; y = lerp(TOP + 10, BOT - 90, t); wdt = lerp(70, 8, t ** 0.8) * (1 - 0.15 * math.sin(t * 9))
        sway = 10 * math.sin(t * 5)
        pts_l.append((CX - wdt / 2 + sway, y)); pts_r.append((CX + wdt / 2 + sway, y))
    root_col = mix((176, 62, 70), (210, 150, 140), rb)
    if rb < 0.98:
        poly = pts_l + pts_r[::-1]
        if rb > 0:  # break into fragments that fade
            for seg in range(6):
                a, b = seg * 7, seg * 7 + 6
                frag = pts_l[a:b + 1] + pts_r[a:b + 1][::-1]
                off = (seg - 2.5) * 14 * rb
                frag = [(x + off, y + 10 * rb * seg) for x, y in frag]
                lay = Image.new("L", (W, H), 0); ImageDraw.Draw(lay).polygon(frag, fill=int(255 * (1 - rb)))
                im.paste(root_col, mask=lay)
        else:
            d.polygon(poly, fill=root_col)
    d = ImageDraw.Draw(im)
    # the wart bump on top: grey, rough, black dots
    if rb < 0.98:
        bump = int(255 * (1 - rb))
        lay = Image.new("L", (W, H), 0); ImageDraw.Draw(lay).ellipse((CX - 70, TOP - 42, CX + 70, TOP + 28), fill=bump)
        im.paste(mix((150, 140, 128), (205, 190, 170), rb), mask=lay)
        d = ImageDraw.Draw(im)
        for dx, dy in ((-30, -14), (-6, -24), (20, -12), (40, -20), (-46, -2), (8, -2)):
            d.ellipse((CX + dx - 4, TOP + dy - 4, CX + dx + 4, TOP + dy + 4), fill=mix((35, 30, 30), (205, 190, 170), rb))
    else:  # smooth skin surface where the wart was
        d.arc((CX - 80, TOP - 10, CX + 80, TOP + 20), 200, 340, fill=(220, 190, 150), width=3)
    if door > 0:  # a little door in the hard top, swinging open
        dx0, dx1, dy0, dy1 = CX - 30, CX + 30, TOP + 20, HARD - 10
        d.rectangle((dx0, dy0, dx1, dy1), fill=(120, 70, 50))
        wd = (dx1 - dx0) * (1 - 0.8 * door)
        d.rectangle((dx0, dy0, dx0 + wd, dy1), fill=mix(hard_col, (255, 236, 200), 0.4), outline=(200, 160, 110), width=2)
    # rounded mask for the whole block
    m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).rounded_rectangle((BX0, TOP - 60, BX1, BOT), 36, fill=255)
    bg = Image.new("RGB", (W, H), ICE); bg.paste(im, mask=m)
    # put shadow back (outside block)
    return bg

def drop(img, x, y, r, col, alpha=255, shine=True):
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.ellipse((x - r, y - r * 1.1, x + r, y + r * 0.9), fill=col + (alpha,), outline=(255, 255, 255, int(alpha * 0.7)), width=2)
    d.polygon([(x - r * 0.7, y - r * 0.5), (x, y - r * 2.1), (x + r * 0.7, y - r * 0.5)], fill=col + (alpha,))
    if shine: d.ellipse((x - r * 0.45, y - r * 0.6, x - r * 0.05, y - r * 0.15), fill=(255, 255, 255, int(alpha * 0.8)))
    img.paste(lay, (0, 0), lay)

LEMON, TEA, POKE, CEDAR = (247, 214, 58), (214, 236, 232), (92, 160, 70), (36, 128, 92)

def frost_scene(t, i):  # 2.6 s: a frost puff whitens only the top
    f = ease((t - 0.5) / 1.0)
    im = skin_base(frost=f)
    d = ImageDraw.Draw(im)
    if 0.3 < t < 2.0:  # vapour puff from above
        a = ease((t - 0.3) / 0.4) * (1 - ease((t - 1.4) / 0.6))
        lay = Image.new("L", (W, H), 0); dd = ImageDraw.Draw(lay)
        for k in range(9):
            dd.ellipse((CX - 140 + k * 30, TOP - 190 + (k % 3) * 25, CX - 60 + k * 30, TOP - 100 + (k % 3) * 25), fill=int(170 * a))
        im.paste((255, 255, 255), mask=lay.filter(ImageFilter.GaussianBlur(14)))
    return im

def team_a(t, i):  # 7 s: drops land, lemon opens a door, tea tree carries the greens down
    land = [0.2, 0.55, 0.9, 1.25]; xs = [CX - 150, CX - 50, CX + 50, CX + 150]; cols = [LEMON, TEA, POKE, CEDAR]
    soft = ease((t - 2.2) / 1.5); door = ease((t - 3.0) / 1.0)
    im = skin_base(soft=soft, door=door)
    for k in range(4):
        tl = ease((t - land[k]) / 0.5)
        if tl <= 0: continue
        x, y = xs[k], lerp(TOP - 330, TOP - 70, tl)
        if k == 0:  # lemon soaks into the hard top
            s = ease((t - 2.2) / 1.2); x = lerp(x, CX, ease((t - 2.0) / 0.6)); y = lerp(y, TOP - 30, s)
            drop(im, x, y, 26 * (1 - 0.7 * s), cols[k], int(255 * (1 - s)))
        else:
            mv = ease((t - 4.2) / 2.6)  # tea tree slides down through the door carrying the two greens
            gx = lerp(x, CX + (k - 2) * 26, ease((t - 4.0) / 0.5))
            gy = lerp(y, HARD + 230, mv) if k == 1 else lerp(y, HARD + 200 - (k - 2) * 50, mv)
            if k > 1: gy = lerp(y, HARD + 200 - (k - 2) * 50, mv); gx = gx if mv < 0.05 else lerp(gx, CX + (k - 2.5) * 30, mv)
            drop(im, gx, gy, 24 if k == 1 else 18, cols[k], 235)
    return im

def team_b(t, i):  # 4.5 s: greens reach the root, it cracks and breaks apart; a clear dot closes over the top
    rb = ease((t - 0.6) / 2.0)
    im = skin_base(soft=1.0, root_break=rb, door=1.0 - ease((t - 2.8) / 0.8))
    for k, col in enumerate((POKE, CEDAR)):
        y = lerp(HARD + 160, BOT - 220 + k * 40, ease(t / 1.0))
        drop(im, CX - 20 + k * 40, y, 18, col, int(235 * (1 - ease((t - 2.0) / 0.8))))
    dt = ease((t - 3.1) / 0.9)
    if dt > 0:  # clear dot closing over the top
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        r = 110; y = lerp(TOP - 260, TOP - 18, dt)
        d.ellipse((CX - r, y - 34, CX + r, y + 34), fill=(255, 255, 255, 110), outline=(255, 255, 255, 230), width=3)
        im.paste(lay, (0, 0), lay)
    return im

def clock_scene(t, i):  # 3 s: sealed dot + small clock 9 pm -> 5 am in the corner
    im = skin_base(soft=1.0, door=0.0)
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.ellipse((CX - 110, TOP - 52, CX + 110, TOP + 16), fill=(255, 255, 255, 110), outline=(255, 255, 255, 230), width=3)
    # warm glow seeping down = keeps soaking
    g = Image.new("L", (W, H), 0); ImageDraw.Draw(g).ellipse((CX - 90, TOP, CX + 90, lerp(TOP + 60, HARD + 220, ease(t / 3))), fill=120)
    im.paste((255, 190, 90), mask=g.filter(ImageFilter.GaussianBlur(30)))
    im.paste(lay, (0, 0), lay)
    d = ImageDraw.Draw(im); cx, cy, r = 600, 220, 62
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(255, 255, 255), outline=NAVY, width=5)
    hours = lerp(21, 29, ease(t / 2.8)); ha = (hours % 12) / 12 * 2 * math.pi; ma = (hours % 1) * 2 * math.pi
    d.line((cx, cy, cx + 30 * math.sin(ha), cy - 30 * math.cos(ha)), fill=NAVY, width=7)
    d.line((cx, cy, cx + 48 * math.sin(ma), cy - 48 * math.cos(ma)), fill=BLUE, width=4)
    d.ellipse((cx - 6, cy - 6, cx + 6, cy + 6), fill=ORANGE)
    return im

# ---------- product cards (real packaging) ----------
def warm_bg():
    im = Image.new("RGB", (W, H)); d = ImageDraw.Draw(im)
    for y in range(H):
        d.line((0, y, W, y), fill=mix((250, 236, 222), (236, 214, 196), y / H))
    return im

def place_duo(im, cx, bottom, height, alpha=1.0):
    s = height / DUO.height; d = DUO.resize((int(DUO.width * s), int(height)), Image.LANCZOS)
    if alpha < 1: d.putalpha(d.getchannel("A").point(lambda v: int(v * alpha)))
    sh = Image.new("L", (W, H), 0); ImageDraw.Draw(sh).ellipse((cx - d.width * 0.55, bottom - 18, cx + d.width * 0.55, bottom + 22), fill=int(110 * alpha))
    im.paste((150, 120, 100), mask=sh.filter(ImageFilter.GaussianBlur(14)))
    im.paste(d, (int(cx - d.width / 2), int(bottom - d.height)), d)

def offer_scene(t, i):  # 8.5 s: three real bottle+box sets slide onto a warm shelf, the third arrives last
    im = warm_bg(); d = ImageDraw.Draw(im)
    d.rectangle((0, 900, W, 935), fill=(214, 188, 166)); d.rectangle((0, 935, W, 960), fill=(190, 162, 140))
    for k, (cx, t0) in enumerate(((200, 0.2), (360, 0.9), (520, 3.2))):
        a = ease((t - t0) / 0.9)
        if a <= 0: continue
        x = lerp(cx + (380 if k == 2 else 0), cx, a)
        place_duo(im, x, 905, 420, alpha=1.0 if k == 2 else a)
    return im

def end_card(t, i):  # 2.5 s
    im = warm_bg(); d = ImageDraw.Draw(im)
    place_duo(im, 360, 860, 560)
    a = ease(t / 0.5)
    f1 = font(SERIF, 64); txt = "Not the top. The root."
    w1 = d.textlength(txt, font=f1); d.text(((W - w1) / 2, 150), txt, font=f1, fill=mix((250, 236, 222), NAVY, a))
    # snapped vs whole dandelion icon
    for side, whole in ((-1, False), (1, True)):
        x0 = 360 + side * 120; yb = 1000
        d.ellipse((x0 - 22, yb - 120, x0 + 22, yb - 76), fill=(247, 214, 58))
        if whole:
            d.line((x0, yb - 78, x0, yb), fill=(90, 140, 60), width=5); d.line((x0, yb, x0, yb + 70), fill=(235, 228, 210), width=7)
            for k in range(4): d.line((x0, yb + 20 + k * 12, x0 + (-1) ** k * 16, yb + 34 + k * 12), fill=(235, 228, 210), width=3)
        else:
            d.line((x0, yb - 78, x0, yb - 20), fill=(90, 140, 60), width=5); d.line((x0 - 10, yb - 18, x0 + 10, yb - 24), fill=(120, 90, 60), width=4)
            d.line((x0, yb, x0, yb + 70), fill=(176, 62, 70), width=7)
        d.line((x0 - 60, yb, x0 + 60, yb), fill=(160, 130, 100), width=4)
    f2 = font(INTER_B, 40); pill = "Buy 2, get 1 free"; pw = d.textlength(pill, font=f2)
    d.rounded_rectangle(((W - pw) / 2 - 30, 1110, (W + pw) / 2 + 30, 1178), 34, fill=ORANGE)
    d.text(((W - pw) / 2, 1120), pill, font=f2, fill=(255, 255, 255))
    f3 = font(INTER_M, 22); s = "AI illustration."; d.text(((W - d.textlength(s, font=f3)) / 2, 1215), s, font=f3, fill=(120, 110, 100))
    return im

def stakes_scene(t, i):  # 4 s: left phone calendar "Wart freeze 3:15" deleted by a swipe; right the real product under lamp light
    im = Image.new("RGB", (W, H), (30, 26, 24)); d = ImageDraw.Draw(im)
    # left half: phone screen
    d.rounded_rectangle((24, 260, 344, 1020), 36, fill=(250, 250, 252))
    fb = font(INTER_B, 30); fm = font(INTER_M, 24)
    d.text((54, 300), "Thursday", font=fb, fill=(30, 30, 40)); d.text((54, 342), "November 27", font=fm, fill=(120, 120, 130))
    sw = ease((t - 1.2) / 0.8); gone = ease((t - 2.1) / 0.5)
    if gone < 1:
        x = lerp(54, -260, sw)
        if sw > 0.2: d.rounded_rectangle((54, 520, 314, 640), 18, fill=ORANGE); d.text((210, 563), "Delete", font=fm, fill=(255, 255, 255))
        d.rounded_rectangle((x, 520, x + 260, 640), 18, fill=(232, 238, 248))
        d.rectangle((x, 520, x + 8, 640), fill=BLUE)
        d.text((x + 24, 540), "Wart freeze", font=fb, fill=(30, 30, 40)); d.text((x + 24, 586), "3:15 PM", font=fm, fill=(90, 90, 100))
    if 0.8 < t < 2.3:  # thumb touch
        tx = lerp(250, 80, ease((t - 1.2) / 0.8)); d.ellipse((tx - 34, 546, tx + 34, 614), fill=(205, 170, 150))
    # right half: warm lamp glow + the real product
    glow = Image.new("L", (W, H), 0); ImageDraw.Draw(glow).ellipse((380, 300, 760, 900), fill=160)
    im.paste((255, 196, 120), mask=glow.filter(ImageFilter.GaussianBlur(60)))
    place_duo(im, 540, 900, 420)
    dl = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(dl).ellipse((600, 930, 680, 965), fill=(255, 255, 255, 120), outline=(255, 255, 255, 220), width=2); im.paste(dl, (0, 0), dl)
    d = ImageDraw.Draw(im); d.line((360, 0, 360, H), fill=(20, 18, 16), width=6)
    return im

if __name__ == "__main__":
    want = sys.argv[1:] or ["frost", "team_a", "team_b", "clock", "stakes", "offer", "end"]
    jobs = {"frost": ("g11_frost", frost_scene, 2.6), "team_a": ("g12a_team", team_a, 7.0), "team_b": ("g12b_team", team_b, 4.5),
            "clock": ("g19_clock", clock_scene, 3.0), "stakes": ("g26_stakes", stakes_scene, 4.8),
            "offer": ("g27_offer", offer_scene, 9.2), "end": ("g28_end", end_card, 2.5)}
    for k in want: write(*jobs[k])
