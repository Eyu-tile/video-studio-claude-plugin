#!/usr/bin/env python3
"""Explainer animations drawn over the 3D skin render (g20) and its healed state (g21): slow camera push, glowing
droplets, frost, the 'door', root glow/dissolve, night seal. Small label chips explain each step. 720x1280, 30 fps."""
import math, random, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops
P = Path(__file__).resolve().parent.parent; OUT = P / "work/gfx"; W, H, FPS = 720, 1280, 30
A = Image.open(P / "raw/gen/frames/g20_skin3d.png").convert("RGB").resize((W, H), Image.LANCZOS)
B = Image.open(P / "raw/gen/frames/g21_skin3d_healed.png").convert("RGB").resize((W, H), Image.LANCZOS)
BUMP = (360, 372); BR = 52; ROOT = [(350, 470), (340, 560), (332, 650), (322, 740), (312, 830), (304, 905)]
NAVY, BLUE, ORANGE, WHITE = (11, 42, 91), (23, 99, 184), (224, 78, 24), (255, 255, 255)
IB = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"; IX = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
def F(p, s): return ImageFont.truetype(p, s)
def ease(t): t = max(0., min(1., t)); return t * t * (3 - 2 * t)
def back(t): t = max(0., min(1., t)); c = 1.70158; return 1 + (c + 1) * (t - 1) ** 3 + c * (t - 1) ** 2
def lerp(a, b, t): return a + (b - a) * t
def along(pts, u):
    u = max(0, min(1, u)) * (len(pts) - 1); i = min(int(u), len(pts) - 2); f = u - i
    return (lerp(pts[i][0], pts[i + 1][0], f), lerp(pts[i][1], pts[i + 1][1], f))
def cam(im, t, dur, z0=1.0, z1=1.1, cy=0.42):
    z = lerp(z0, z1, ease(t / dur)); w, h = W / z, H / z; x0 = (W - w) / 2 + 6 * math.sin(t * 0.9); y0 = (H - h) * cy
    return im.crop((int(x0), int(y0), int(x0 + w), int(y0 + h))).resize((W, H), Image.LANCZOS)
def glow(base, draw_fn, color, blur=14, strength=1.0):
    L = Image.new("L", (W, H), 0); draw_fn(ImageDraw.Draw(L))
    g = L.filter(ImageFilter.GaussianBlur(blur)).point(lambda v: int(min(255, v * strength)))
    base.paste(color, mask=g); base.paste(tuple(min(255, c + 60) for c in color), mask=L.point(lambda v: int(v * 0.6 * strength)))
def droplet(im, x, y, r, col, a=1.0):
    L = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    d.ellipse((x - r, y - r * 1.05, x + r, y + r * 0.95), fill=col + (int(235 * a),))
    d.polygon([(x - r * .72, y - r * .45), (x, y - r * 2.2), (x + r * .72, y - r * .45)], fill=col + (int(235 * a),))
    d.ellipse((x - r * .5, y - r * .6, x - r * .1, y - r * .15), fill=(255, 255, 255, int(220 * a)))
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).ellipse((x - r, y - r, x + r, y + r), fill=col + (int(110 * a),))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(r * .8))); im.alpha_composite(L)
def chip(im, cx, cy, text, a, fg=NAVY, bg=WHITE, size=34, icon=None):
    if a <= 0: return
    f = F(IX, size); d0 = ImageDraw.Draw(im); tw = d0.textlength(text, font=f); w, h = tw + 60 + (44 if icon else 0), size + 30
    s = back(a); L = Image.new("RGBA", (int(w) + 4, int(h) + 4), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    d.rounded_rectangle((2, 2, w, h), int(h / 2), fill=bg + (int(240 * min(1, a)),))
    x = 30
    if icon: d.text((24, 2 + 12), icon, font=F(IX, size), fill=ORANGE + (255,)); x = 70
    d.text((x, 2 + 12), text, font=f, fill=fg + (int(255 * min(1, a)),))
    L = L.resize((max(1, int(L.width * s)), max(1, int(L.height * s))), Image.LANCZOS)
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((cx - L.width / 2, cy - L.height / 2 + 8, cx + L.width / 2, cy + L.height / 2 + 8), int(h / 2), fill=(0, 0, 0, int(70 * min(1, a))))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(12))); im.alpha_composite(L, (int(cx - L.width / 2), int(cy - L.height / 2)))
def write(name, fn, dur):
    n = int(round(dur * FPS)); out = OUT / f"{name}.mp4"
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "15", str(out)], stdin=subprocess.PIPE)
    for i in range(n): p.stdin.write(fn(i / FPS).convert("RGB").tobytes())
    p.stdin.close(); p.wait(); print("wrote", out.name, dur)

def root_line(d, w=10, u1=1.0):
    pts = [along(ROOT, k / 40 * u1) for k in range(41)]; d.line(pts, fill=255, width=w, joint="curve")

def e_top(t):  # 4.1 s: freezing / acid / shaving each hit ONLY the top; the root stays
    base = A.copy(); D = 4.1
    fr = ease((t - 0.35) / 0.5)  # frost on the bump top
    if fr > 0: glow(base, lambda d: d.ellipse((BUMP[0] - BR, BUMP[1] - BR * .8, BUMP[0] + BR, BUMP[1] + BR * .6), fill=255), (235, 245, 255), 16, 0.9 * fr)
    if 1.15 < t < 2.0:  # acid drop + fizz
        pass
    if t > 2.85:  # root highlighted: it stays
        g = ease((t - 2.85) / 0.4) * (0.75 + 0.25 * math.sin(t * 7))
        glow(base, lambda d: root_line(d, 12), (255, 90, 60), 16, g)
    im = cam(base, t, D, 1.0, 1.12, 0.30).convert("RGBA")
    # icons falling onto the top (in camera space approx: bump moves little with this crop)
    bx, by = W / 2, 470
    if 0.2 < t < 1.25:  # snowflake chip + mist puff
        a = ease((t - 0.2) / 0.25) * (1 - ease((t - 1.05) / 0.2)); chip(im, bx, 250, "Freezing", a, icon="●")
        m = Image.new("RGBA", (W, H), (0, 0, 0, 0)); md = ImageDraw.Draw(m)
        for k in range(10):
            x = bx - 120 + k * 26; y = lerp(300, by - 30, ease((t - 0.25) / 0.6)) + (k % 3) * 14
            md.ellipse((x - 30, y - 22, x + 30, y + 22), fill=(255, 255, 255, int(150 * a)))
        im.alpha_composite(m.filter(ImageFilter.GaussianBlur(12)))
    if 1.15 < t < 2.0:
        a = ease((t - 1.15) / 0.2) * (1 - ease((t - 1.8) / 0.2)); chip(im, bx, 250, "Acid", a, icon="●")
        y = lerp(300, by - 20, ease((t - 1.2) / 0.4)); droplet(im, bx + 6, y, 18, (200, 235, 140), a)
        if t > 1.6:
            rnd = random.Random(int(t * 30))
            for k in range(8):
                x = bx + rnd.uniform(-40, 40); yy = by - 20 - rnd.uniform(0, 40) * (t - 1.6) * 4
                L = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(L).ellipse((x - 5, yy - 5, x + 5, yy + 5), outline=(255, 255, 255, int(200 * a)), width=2); im.alpha_composite(L)
    if 1.9 < t < 2.85:
        a = ease((t - 1.9) / 0.2) * (1 - ease((t - 2.65) / 0.2)); chip(im, bx, 250, "Shaving", a, icon="●")
        x = lerp(bx - 140, bx + 140, ease((t - 2.0) / 0.6)); L = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dl = ImageDraw.Draw(L)
        dl.rounded_rectangle((x - 70, by - 52, x + 70, by - 38), 6, fill=(205, 210, 220, int(255 * a)), outline=(120, 125, 140, int(255 * a)), width=2); im.alpha_composite(L)
        rnd = random.Random(7)
        for k in range(10):
            if t < 2.2: break
            px = bx + rnd.uniform(-30, 60) + (t - 2.2) * rnd.uniform(60, 160); py = by - 50 - (t - 2.2) * rnd.uniform(40, 120) + (t - 2.2) ** 2 * 300
            ImageDraw.Draw(im).ellipse((px - 4, py - 4, px + 4, py + 4), fill=(170, 150, 130, int(255 * a)))
    if t > 2.85:
        chip(im, bx, 250, "Only the top", ease((t - 2.85) / 0.3), fg=WHITE, bg=NAVY)
        chip(im, bx + 150, 1000, "The root stays", ease((t - 3.2) / 0.3), fg=WHITE, bg=ORANGE)
    return im

def e_lemon(t):  # 3.1 s: lemon drop lands, the hard top softens, a little door opens
    base = A.copy(); D = 3.1
    sf = ease((t - 0.9) / 1.0)
    if sf > 0:  # warm softening glow over the hard top band
        glow(base, lambda d: d.ellipse((60, 230, 690, 520), fill=255), (255, 214, 120), 40, 0.45 * sf)
    if t > 1.6:  # the 'door': a glowing opening in the hard top beside the bump
        o = ease((t - 1.6) / 0.6); x, y = BUMP[0] + 4, BUMP[1] + 58
        L = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
        d.ellipse((x - 34 * o, y - 12 * o, x + 34 * o, y + 12 * o), fill=(150, 40, 40, 230), outline=(255, 220, 140, 255), width=4)
        base = base.convert("RGBA"); base.alpha_composite(L.filter(ImageFilter.GaussianBlur(1))); base = base.convert("RGB")
        glow(base, lambda d: d.ellipse((x - 40 * o, y - 16 * o, x + 40 * o, y + 16 * o), outline=255, width=6), (255, 230, 150), 10, o)
    im = cam(base, t, D, 1.04, 1.14, 0.28).convert("RGBA")
    if t < 1.0:
        y = lerp(120, 450, ease(t / 0.9)); droplet(im, W / 2 - 20, y, 26, (250, 210, 40))
    if 0.85 < t < 1.5:
        r = 20 + 120 * ease((t - 0.85) / 0.6); a = 1 - ease((t - 0.85) / 0.6)
        L = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(L).ellipse((W / 2 - 20 - r, 470 - r * .35, W / 2 - 20 + r, 470 + r * .35), outline=(255, 230, 90, int(220 * a)), width=4); im.alpha_composite(L)
    chip(im, W / 2, 200, "Lemon softens the hard top", ease((t - 0.3) / 0.3), icon="🍋" if False else "●", size=32)
    return im

def e_root(t):  # 5.1 s: two green drops travel down the root, it glows, cracks, dissolves -> healed
    D = 5.1; mix_ = ease((t - 2.7) / 1.3); base = Image.blend(A, B, mix_)
    if t < 3.4:
        g = ease((t - 1.3) / 0.5) * (1 - ease((t - 2.9) / 0.5))
        glow(base, lambda d: root_line(d, 12, ease((t - 0.4) / 1.2)), (90, 230, 120), 14, max(g, 0.5 * ease((t - 0.4) / 0.4) * (1 - mix_)))
    im = cam(base, t, D, 1.0, 1.08, 0.36).convert("RGBA")
    for k, col in enumerate(((92, 190, 80), (40, 150, 100))):
        u = ease((t - 0.3 - k * 0.15) / 1.3); a = 1 - ease((t - 2.3) / 0.4)
        if a > 0: x, y = along(ROOT, u); y = (y - (H - H / 1.03) * 0.36) * 1.03; droplet(im, x + (k * 2 - 1) * 16, y - 40 * (1 - u), 15, col, a)
    if 2.4 < t < 4.2:  # dissolve sparkle where the root was
        rnd = random.Random(int(t * 15)); a = 1 - ease((t - 3.4) / 0.8)
        L = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
        for k in range(26):
            x, y = along(ROOT, rnd.random()); y += (H - H / 1.06) * -0.1; x += rnd.uniform(-14, 14) + (t - 2.4) * rnd.uniform(-30, 30); y -= (t - 2.4) * rnd.uniform(20, 70)
            r = rnd.uniform(2, 5); d.ellipse((x - r, y - r, x + r, y + r), fill=(200, 255, 200, int(220 * a)))
        im.alpha_composite(L.filter(ImageFilter.GaussianBlur(1)))
    chip(im, W / 2, 190, "Pokeweed + white cedar", ease((t - 0.2) / 0.3) * (1 - ease((t - 2.6) / 0.3)), icon="●")
    chip(im, W / 2, 190, "Broken down from the root", ease((t - 2.8) / 0.3), fg=WHITE, bg=NAVY)
    return im

def e_night(t):  # 1.4 s: clear dot seals the top, oil keeps soaking, evening -> night tint
    base = A.copy(); D = 1.4
    glow(base, lambda d: root_line(d, 16, ease(t / 1.3)), (255, 190, 90), 18, 0.8)
    im = cam(base, t, D, 1.06, 1.1, 0.3).convert("RGBA")
    a = back(t / 0.45); r = 70 * a
    L = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L); bx, by = W / 2, 470
    d.ellipse((bx - r, by - r * .45 - 10, bx + r, by + r * .45 - 10), fill=(255, 255, 255, 80), outline=(255, 255, 255, 230), width=3)
    d.ellipse((bx - r * .55, by - r * .3 - 14, bx - r * .1, by - r * .12 - 14), fill=(255, 255, 255, 170)); im.alpha_composite(L)
    tint = Image.new("RGBA", (W, H), (20, 40, 110, int(90 * ease((t - 0.3) / 1.0)))); im.alpha_composite(tint)
    chip(im, W / 2, 190, "Soaks all night", ease((t - 0.1) / 0.25), fg=WHITE, bg=NAVY, icon="●")
    return im

JOBS = {"e_top": (e_top, 4.1), "e_lemon": (e_lemon, 3.1), "e_root": (e_root, 5.1), "e_night": (e_night, 1.4)}
if __name__ == "__main__":
    for k in (sys.argv[1:] or JOBS): write(k, *JOBS[k])
