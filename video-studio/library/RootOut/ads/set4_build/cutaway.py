#!/usr/bin/env python3
"""Set 4 animated foot cut-away (the green-screen background), drawn in code, RootOut palette.
A scene = {"name", "dur", "chip", "pins": {...}, events...}; times are seconds from scene start.
Usage: cutaway.py scenes.json [name ...]   -> work/cutaway/<name>.mp4 (1080x1920, 30 fps, silent)
       cutaway.py --still out.png            -> the empty cut-away (for Seedance clay-drop start frames)"""
import json, math, random, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

P = Path("/home/user/video-studio-claude-plugin/video-studio/projects/rootout-set4")
W, H, FPS = 1080, 1920, 30
NAVY, BLUE, ICE, MIST, SLATE, ORANGE, WHITE = "#0B2A5B", "#1763B8", "#EEF4FA", "#D9E2EC", "#4A5568", "#E04E18", "#FFFFFF"
SERIF = str(P / "assets/fonts/Newsreader.ttf")
INTER_B, INTER_X = "/usr/share/fonts/opentype/inter/Inter-Bold.otf", "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"

def font(path, size, var=None):
    f = ImageFont.truetype(path, size)
    if var: f.set_variation_by_name(var)
    return f

# ---- geometry (the mom covers y > ~1050 in the middle when she is keyed in) ----
PX0, PY0, PX1, PY1 = 48, 190, 1032, 1060          # cut-away panel
SURF, HARD_B, ROOT_END = 360, 590, 1000           # surface line, bottom of hard band, root tip depth
WX = 520                                           # wart centre x
RX0, RX1 = 950, 990                                # depth ruler x range
SLOTS = {1: SURF - 6, 2: SURF + 70, 3: HARD_B - 14, 4: ROOT_END - 8}
PIN_X = {1: 452, 2: 520, 3: 590, 4: 640}
PIN_COL = {1: ("#9AA3AD", "#5E6670"), 2: (BLUE, NAVY), 3: (WHITE, NAVY), 4: ("#F2B632", "#9A6A00")}

def ease(x):  # ease-out back for drops
    x = max(0.0, min(1.0, x)); c = 1.4
    return 1 + (c + 1) * (x - 1) ** 3 + c * (x - 1) ** 2

def smooth(x):
    x = max(0.0, min(1.0, x)); return x * x * (3 - 2 * x)

def root_pts(sway=0.0):
    pts = []
    for i in range(41):
        u = i / 40; y = HARD_B - 10 + u * (ROOT_END - HARD_B + 10)
        x = WX + 60 * u ** 1.6 + 14 * math.sin(u * 7 + sway) * u
        pts.append((x, y, 30 * (1 - u) ** 0.8 + 3))
    return pts

def base_layer():
    """Background + panel + skin layers + root + ruler: everything that never moves."""
    rnd = random.Random(7)
    im = Image.new("RGB", (W, H), ICE); d = ImageDraw.Draw(im)
    for y in range(H):  # soft vertical gradient
        k = y / H; c = tuple(int(a + (b - a) * k) for a, b in zip((238, 244, 250), (214, 226, 238)))
        d.line([(0, y), (W, y)], fill=c)
    panel = Image.new("RGB", (PX1 - PX0, PY1 - PY0), "#FFFFFF"); pd = ImageDraw.Draw(panel)
    ox, oy = PX0, PY0
    # air above the skin
    pd.rectangle((0, 0, panel.width, SURF - oy), fill="#F7FAFD")
    # soft pink skin with faint cells
    for y in range(HARD_B - oy, panel.height):
        k = (y - (HARD_B - oy)) / (panel.height - (HARD_B - oy))
        c = tuple(int(a + (b - a) * k) for a, b in zip((247, 205, 200), (236, 170, 168)))
        pd.line([(0, y), (panel.width, y)], fill=c)
    for _ in range(140):
        x, y = rnd.uniform(0, panel.width), rnd.uniform(HARD_B - oy + 10, panel.height)
        r = rnd.uniform(10, 26); pd.ellipse((x - r, y - r * 0.7, x + r, y + r * 0.7), outline=(228, 160, 158), width=2)
    # hard band: pale cracked ground
    for y in range(SURF - oy, HARD_B - oy):
        k = (y - (SURF - oy)) / (HARD_B - SURF)
        c = tuple(int(a + (b - a) * k) for a, b in zip((238, 224, 190), (222, 200, 160)))
        pd.line([(0, y), (panel.width, y)], fill=c)
    for _ in range(26):  # crack network
        x = rnd.uniform(0, panel.width); y = SURF - oy + 4; pts = [(x, y)]
        for _ in range(rnd.randint(3, 6)):
            x += rnd.uniform(-38, 38); y += rnd.uniform(20, 55)
            if y > HARD_B - oy - 4: break
            pts.append((x, y))
        pd.line(pts, fill=(176, 150, 110), width=rnd.choice([2, 3, 4]), joint="curve")
    for _ in range(400):  # grain
        x, y = rnd.uniform(0, panel.width), rnd.uniform(SURF - oy, HARD_B - oy)
        pd.point((x, y), fill=(200, 178, 140))
    # dividing lines
    pd.line([(0, SURF - oy), (panel.width, SURF - oy)], fill=(190, 166, 122), width=4)
    pd.line([(0, HARD_B - oy), (panel.width, HARD_B - oy)], fill=(214, 150, 140), width=3)
    mask = Image.new("L", panel.size, 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, panel.width - 1, panel.height - 1), 44, fill=255)
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((PX0 + 6, PY0 + 18, PX1 + 6, PY1 + 18), 44, fill=(11, 42, 91, 60))
    im.paste(Image.alpha_composite(Image.new("RGBA", (W, H), (0, 0, 0, 0)), sh.filter(ImageFilter.GaussianBlur(20))).convert("RGB"), (0, 0), sh.filter(ImageFilter.GaussianBlur(20)))
    im.paste(panel, (ox, oy), mask)
    d = ImageDraw.Draw(im)
    # layer labels (small, left)
    fl = font(INTER_B, 26)
    d.text((PX0 + 28, SURF + 18), "HARD SKIN", font=fl, fill=(150, 124, 84))
    d.text((PX0 + 28, HARD_B + 18), "SOFT SKIN", font=fl, fill=(190, 110, 110))
    # depth ruler
    d.rounded_rectangle((RX0, SURF - 20, RX1, ROOT_END + 20), 20, fill="#FFFFFF", outline=MIST, width=3)
    for k in range(0, 17):
        y = SURF + k * (ROOT_END - SURF) / 16; L = 18 if k % 4 == 0 else 9
        d.line([(RX0 + 4, y), (RX0 + 4 + L, y)], fill=SLATE, width=2)
    return im

def draw_root(d, alpha=1.0, glow=0.0):
    if alpha <= 0: return
    pts = root_pts()
    col = tuple(int(255 * alpha + c * (1 - alpha)) for c in (240, 190, 185))
    for (x0, y0, r0), (x1, y1, r1) in zip(pts, pts[1:]):
        if glow > 0:
            d.line([(x0, y0), (x1, y1)], fill=(255, 170, 120), width=int(2 * r0 + 18 * glow))
        d.line([(x0, y0), (x1, y1)], fill=col, width=int(2 * r0))
        d.ellipse((x1 - r1, y1 - r1, x1 + r1, y1 + r1), fill=col)
    if alpha > 0.5:
        for u, s in ((0.35, -1), (0.55, 1), (0.72, -1)):  # rootlets
            x, y, r = pts[int(u * 40)]
            d.line([(x, y), (x + s * 46, y + 40)], fill=col, width=5)

def draw_bump(d, cx, scale=1.0, h=1.0, dots=1.0):
    if h <= 0.02 or scale <= 0: return
    w = 92 * scale; rnd = random.Random(int(cx))
    # body in the hard band: a grey wedge tapering down toward the root
    depth = (HARD_B - SURF) * (0.95 if scale >= 0.99 else 0.55) * scale
    body = [(cx - w * 0.95, SURF)]
    for k in range(1, 9):
        u = k / 8; body.append((cx - w * 0.95 * (1 - u) ** 0.8 - 12 * u + rnd.uniform(-5, 5), SURF + depth * u))
    for k in range(8, -1, -1):
        u = k / 8; body.append((cx + w * 0.95 * (1 - u) ** 0.8 + 12 * u + rnd.uniform(-5, 5), SURF + depth * u))
    d.polygon(body, fill=(158, 156, 152), outline=(112, 110, 108))
    # rough cauliflower top above the surface
    for k in range(9):
        u = (k / 8) * 2 - 1; bx = cx + u * w * 0.82; r = (34 - 10 * abs(u)) * scale
        by = SURF - (40 * (1 - u * u) + 6) * scale * h
        d.ellipse((bx - r, by - r * h, bx + r, by + r), fill=(150, 149, 146), outline=(108, 106, 104), width=3)
    d.rectangle((cx - w * 0.92, SURF - 8 * scale, cx + w * 0.92, SURF + 4), fill=(158, 156, 152))
    for _ in range(int(9 * scale)):  # black dots (and rough texture)
        x = cx + rnd.uniform(-w * 0.65, w * 0.65); y = SURF - rnd.uniform(4, 40 * scale * h)
        r = rnd.uniform(4, 7) * scale; v = int(30 + (1 - dots) * 120)
        d.ellipse((x - r, y - r, x + r, y + r), fill=(v, v, v))

def draw_pin(im, i, tip_y, alpha=1.0, dx=0.0, rot=0.0):
    if alpha <= 0: return
    head, edge = PIN_COL[i]; L = 150
    lay = Image.new("RGBA", (120, L + 70), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.line([(60, 56), (60, L + 60)], fill=(80, 84, 92, 255), width=7)
    d.ellipse((18, 10, 102, 94), fill=head, outline=edge, width=6)
    d.ellipse((38, 26, 58, 46), fill=(255, 255, 255, 170))
    if rot: lay = lay.rotate(rot, resample=Image.BICUBIC, center=(60, L + 60))
    if alpha < 1: lay.putalpha(lay.getchannel("A").point(lambda a: int(a * alpha)))
    im.paste(lay, (int(PIN_X[i] - 60 + dx), int(tip_y - (L + 60))), lay)

def draw_tomb(d, t, x=260):
    if t <= 0: return
    s = ease(t / 0.45); y = SURF
    h = 200 * s; w = 150
    d.rounded_rectangle((x - w / 2, y - h, x + w / 2, y + 10), 60, fill=(168, 172, 178), outline=(110, 114, 122), width=5)
    if s > 0.6:
        f = font(INTER_X, 34); d.text((x, y - h + 70), "R.I.P.", font=f, fill=(70, 74, 82), anchor="mm")
        f2 = font(INTER_X, 30); d.text((x, y - h + 112), "WART", font=f2, fill=(70, 74, 82), anchor="mm")
        cx, cy = x + 30, y - h - 4  # daisy on top
        for k in range(8):
            a = k * math.pi / 4; d.ellipse((cx + 18 * math.cos(a) - 10, cy + 18 * math.sin(a) - 10, cx + 18 * math.cos(a) + 10, cy + 18 * math.sin(a) + 10), fill=WHITE, outline=MIST)
        d.ellipse((cx - 10, cy - 10, cx + 10, cy + 10), fill="#F2B632")

def chip(d, text, a=1.0):
    if not text or a <= 0: return
    f = font(INTER_X, 46); tw = d.textlength(text, font=f)
    x0, y0 = PX0 + 4, PY0 - 120
    d.rounded_rectangle((x0, y0, x0 + tw + 64, y0 + 86), 43, fill=NAVY)
    d.text((x0 + 32, y0 + 43), text, font=f, fill=WHITE, anchor="lm")

def frame(sc, t, base):
    im = base.copy(); d = ImageDraw.Draw(im)
    g = lambda k, default=None: sc.get(k, default)
    # slots on the ruler
    for i, y in SLOTS.items():
        on = 0.0
        if g("slots_glow") is not None: on = smooth((t - g("slots_glow")) / 0.4)
        if i == 4 and g("blink_slot4") is not None and t > g("blink_slot4"):
            on = 0.35 + 0.65 * (0.5 + 0.5 * math.cos((t - g("blink_slot4")) * 9))
        filled = any(p.get("slot", k) == i for k, p in g("pins", {}).items() if pin_state(p, t)[1] > 0.99 and pin_state(p, t)[2] > 0.5)
        r = 17; c = PIN_COL[i][0] if filled else (WHITE if on < 0.5 else "#CFE0F5")
        if on > 0 and not filled:
            d.ellipse((RX0 + 20 - r - 10 * on, y - r - 10 * on, RX0 + 20 + r + 10 * on, y + r + 10 * on), fill=(23, 99, 184, int(60 * on)))
        d.ellipse((RX0 + 20 - r, y - r, RX0 + 20 + r, y + r), fill=c, outline=BLUE, width=4)
        d.text((RX0 + 20, y), str(i), font=font(INTER_X, 20), fill=NAVY, anchor="mm")
    # 8x fill on the ruler
    if g("fill8x"):
        a, b = g("fill8x"); u = smooth((t - a) / max(b - a, 0.01))
        if u > 0:
            y1 = SURF + u * (ROOT_END - SURF)
            d.rounded_rectangle((RX0 + 30, SURF, RX1 - 4, y1), 6, fill="#F2B632")
            if u > 0.9: d.text((RX0 - 16, ROOT_END + 46), "8x†", font=font(INTER_X, 40), fill=NAVY, anchor="mm")
    smooth_u = smooth((t - g("smooth_at")) / 1.2) if g("smooth_at") is not None else 0.0
    glow = 0.0
    if g("root_glow"): glow = 0.5 + 0.5 * math.sin((t - g("root_glow")) * 5) if t > g("root_glow") else 0.0
    draw_root(d, 1 - smooth_u, glow)
    # extra roots under each pin for the reveal ("the same long white root, untouched")
    # bumps
    h = 1.0
    if g("regrow"):
        a, b = g("regrow")  # flatten at a, pushes back up at b
        h = 1 - 0.85 * smooth((t - a) / 0.6) + 0.85 * smooth((t - b) / 0.8)
    dots = 1.0
    if g("dots_fade") is not None: dots = 1 - smooth((t - g("dots_fade")) / 0.6)
    if g("regrow"): dots = max(dots, smooth((t - g("regrow")[1]) / 0.8))
    draw_bump(d, WX, 1.0 * (1 - smooth_u), h, dots)
    if g("bumps3_at") is not None:
        s = ease((t - g("bumps3_at")) / 0.5) * (1 - smooth_u)
        if s > 0: draw_bump(d, 330, 0.62 * s); draw_bump(d, 760, 0.55 * s)
    if g("bumps3"):  # already three (later beats)
        draw_bump(d, 330, 0.62 * (1 - smooth_u)); draw_bump(d, 760, 0.55 * (1 - smooth_u))
    if smooth_u > 0:  # smooth skin line over where bumps were
        d.line([(PX0 + 20, SURF), (PX1 - 20, SURF)], fill=(190, 166, 122), width=4)
    # tape blanket
    if g("tape_at") is not None and t > g("tape_at"):
        u = ease((t - g("tape_at")) / 0.5)
        y = SURF - 70 + (1 - u) * -200
        d.polygon([(WX - 110, y + 28), (WX + 110, y + 18), (WX + 118, y + 52), (WX - 104, y + 62)], fill=(150, 154, 160), outline=(110, 114, 120))
        for k in range(6): d.line([(WX - 90 + k * 36, y + 26), (WX - 86 + k * 36, y + 58)], fill=(132, 136, 142), width=3)
    if g("tomb_at") is not None: draw_tomb(d, t - g("tomb_at"), g("tomb_x", 260))
    # cream blob stuck on top
    if g("cream_at") is not None and t > g("cream_at"):
        u = ease((t - g("cream_at")) / 0.4); cx = 300
        d.ellipse((cx - 70 * u, SURF - 50 * u, cx + 70 * u, SURF + 6), fill=WHITE, outline=MIST, width=3)
        d.ellipse((cx - 24 * u, SURF - 68 * u, cx + 30 * u, SURF - 20 * u), fill=WHITE, outline=MIST, width=3)
    # pins
    for k, p in g("pins", {}).items():
        y, a, landed, dx, rot = pin_state(p, t)
        if a > 0: draw_pin(im, int(k), y, a, dx, rot)
    d = ImageDraw.Draw(im)
    # clock
    if g("clock"):
        a, b = g("clock"); u = smooth((t - a) / max(b - a, .01))
        if t > a - 0.3:
            mins = 21 * 60 + u * 8 * 60; hh = int(mins // 60) % 24; mm = int(mins % 60)
            lab = f"{(hh - 1) % 12 + 1}:{mm:02d} {'PM' if hh >= 12 else 'AM'}"
            cx, cy = PX0 + 120, PY0 + 90
            d.ellipse((cx - 64, cy - 64, cx + 64, cy + 64), fill=WHITE, outline=NAVY, width=6)
            ang = (mins % 720) / 720 * 2 * math.pi; ang2 = (mins % 60) / 60 * 2 * math.pi
            d.line([(cx, cy), (cx + 30 * math.sin(ang), cy - 30 * math.cos(ang))], fill=NAVY, width=7)
            d.line([(cx, cy), (cx + 48 * math.sin(ang2), cy - 48 * math.cos(ang2))], fill=BLUE, width=4)
            d.text((cx + 90, cy), lab, font=font(INTER_X, 44), fill=NAVY, anchor="lm")
    if g("board"): draw_board(im, sc, t)
    ca = 1.0
    if g("chip_in") is not None: ca = smooth((t - g("chip_in")) / 0.25)
    chip(d, g("chip"), ca)
    # push-in zoom (into the cut-away before the dandelion)
    if g("zoom"):
        a, b, s = g("zoom"); u = smooth((t - a) / max(b - a, .01))
        if u > 0:
            z = 1 + (s - 1) * u; cx, cy = WX, (SURF + HARD_B) / 2
            cw, chh = W / z, H / z
            im = im.crop((int(cx - cw / 2), int(cy - chh * 0.4), int(cx + cw / 2), int(cy + chh * 0.6))).resize((W, H), Image.BICUBIC)
    return im

RANKS = {1: ("Duct tape", "sits on top"), 2: ("Acid pads", "just inside"), 3: ("Freezing", "bottom of the hard skin"), 4: ("RootOut", "the root")}
def draw_board(im, sc, t):
    """Ranking board under the cut-away (full-screen shots without the mom)."""
    d = ImageDraw.Draw(im); y0 = 1130
    ks = sorted(int(k) for k, p in sc.get("pins", {}).items() if pin_state(p, t)[1] > 0 or p.get("present"))
    if sc.get("board_all"): ks = [1, 2, 3, 4]
    f1, f2 = font(INTER_X, 46), font(INTER_B, 34)
    for row, i in enumerate([1, 2, 3, 4]):
        y = y0 + row * 170; on = i in ks
        d.rounded_rectangle((PX0, y, PX1, y + 146), 34, fill=WHITE if on else "#F3F6FA", outline=MIST, width=3)
        head, edge = PIN_COL[i]
        d.ellipse((PX0 + 30, y + 41, PX0 + 94, y + 105), fill=head if on else "#E3E8EF", outline=edge if on else MIST, width=5)
        d.text((PX0 + 62, y + 73), str(i), font=font(INTER_X, 30), fill=NAVY if on else "#A0AAB8", anchor="mm")
        name, depth = RANKS[i]
        d.text((PX0 + 124, y + 50), name, font=f1, fill=NAVY if on else "#A0AAB8", anchor="lm")
        d.text((PX0 + 124, y + 104), depth if on else "", font=f2, fill=(224, 78, 24) if i == 4 else (90, 100, 120), anchor="lm")
        if i == 4 and on:
            d.text((PX1 - 40, y + 73), "✓", font=font("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60), fill="#15803D", anchor="rm")

def pin_state(p, t):
    """-> (tip_y, alpha, landed 0..1, dx, rot) for a pin {"slot", "drop_at" | "present", "flick_at"}"""
    slot = p.get("slot"); ty = SLOTS[slot]
    if p.get("present"): y, a, landed = ty, 1.0, 1.0
    elif p.get("drop_at") is not None:
        u = (t - p["drop_at"]) / p.get("drop_dur", 0.55)
        if u <= 0: return (0, 0, 0, 0, 0)
        y = -60 + (ty + 60) * ease(u); a = min(1.0, u * 4); landed = 1.0 if u >= 1 else 0.0
    else: return (0, 0, 0, 0, 0)
    dx = rot = 0.0
    if p.get("flick_at") is not None and t > p["flick_at"]:
        v = (t - p["flick_at"]) / 0.5
        dx = 900 * v * v + 200 * v; y -= 500 * v - 300 * v * v; rot = -140 * v; a = max(0.0, 1 - v)
    return (y, a, landed, dx, rot)

def render(sc, out):
    base = base_layer(); n = int(round(sc["dur"] * FPS))
    out.parent.mkdir(parents=True, exist_ok=True)
    ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                           "-c:v", "libx264", "-preset", "medium", "-crf", "16", "-pix_fmt", "yuv420p", str(out)], stdin=subprocess.PIPE)
    for k in range(n): ff.stdin.write(frame(sc, k / FPS, base).tobytes())
    ff.stdin.close(); ff.wait(); print(out.name, f"{sc['dur']:.2f}s")

if __name__ == "__main__":
    if sys.argv[1] == "--still":
        frame({"pins": {}}, 0, base_layer()).save(sys.argv[2]); sys.exit()
    scenes = json.loads(Path(sys.argv[1]).read_text())
    want = set(sys.argv[2:])
    for sc in scenes:
        if not want or sc["name"] in want: render(sc, P / "work/cutaway" / f"{sc['name']}.mp4")
