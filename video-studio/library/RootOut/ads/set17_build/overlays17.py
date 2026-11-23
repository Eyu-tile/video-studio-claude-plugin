#!/usr/bin/env python3
"""Animated transparent overlays (720x1280 RGBA, 30 fps, .mov qtrle) for Set 17: hook, plant list, routine steps,
product callout, CTA. Brand: navy #0B2A5B, blue #1763B8, orange #E04E18, Newsreader + Inter. No footnotes on b-roll."""
import math, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont
P = Path(__file__).resolve().parent.parent; OUT = P / "work/ov"; W, H, FPS = 720, 1280, 30
NAVY, BLUE, ORANGE, WHITE = (11, 42, 91), (23, 99, 184), (224, 78, 24), (255, 255, 255)
SERIF = str(P / "assets/fonts/Newsreader-SemiBold.ttf"); IB = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"; IX = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
def F(p, s): return ImageFont.truetype(p, s)
def ease(t): t = max(0., min(1., t)); return t * t * (3 - 2 * t)
def back(t):  # ease-out-back pop
    t = max(0., min(1., t)); c = 1.70158; return 1 + (c + 1) * (t - 1) ** 3 + c * (t - 1) ** 2
def write(name, fn, dur):
    n = int(round(dur * FPS)); out = OUT / f"{name}.mov"
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-c:v", "qtrle", str(out)], stdin=subprocess.PIPE)
    for i in range(n): p.stdin.write(fn(i / FPS).tobytes())
    p.stdin.close(); p.wait(); print("wrote", out.name, dur)
def shadow(im, box, r, a=90, blur=14, dy=8):
    L = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(L).rounded_rectangle((box[0], box[1] + dy, box[2], box[3] + dy), r, fill=(0, 0, 0, a))
    im.alpha_composite(L.filter(ImageFilter.GaussianBlur(blur)))
def pill(im, cx, cy, text, font, fg, bg, sc=1.0, alpha=1.0, padx=30, pady=16):
    if sc <= 0.01 or alpha <= 0: return
    d0 = ImageDraw.Draw(im); tw = d0.textlength(text, font=font); w, h = tw + 2 * padx, font.size + 2 * pady
    L = Image.new("RGBA", (int(w) + 4, int(h) + 4), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    d.rounded_rectangle((2, 2, w, h), int(h / 2), fill=bg + (int(255 * alpha),)); d.text((2 + padx, 2 + pady - font.size * 0.12), text, font=font, fill=fg + (int(255 * alpha),))
    L = L.resize((max(1, int(L.width * sc)), max(1, int(L.height * sc))), Image.LANCZOS)
    shadow(im, (cx - L.width / 2, cy - L.height / 2, cx + L.width / 2, cy + L.height / 2), int(h / 2), int(70 * alpha))
    im.alpha_composite(L, (int(cx - L.width / 2), int(cy - L.height / 2)))

# 1) hook in the lower third, pop in, gentle float, out at 7.3 s
def hook_fn(text, end=7.0):
    size = 64
    while ImageDraw.Draw(Image.new("RGB", (1, 1))).textlength(text, font=F(SERIF, size)) > W - 150: size -= 2
    f = F(SERIF, size)
    def fn(t):
        im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); a = ease((t - 0.2) / 0.25) * (1 - ease((t - end) / 0.3))
        pill(im, W / 2, 1010 - 6 * math.sin(t * 2), text, f, NAVY, WHITE, back((t - 0.2) / 0.35), a, 34, 18); return im
    return fn

# 2) plant list beside mom (L14 timing): arrow + circular real-plant photo + name, then "= 4 bottles?"
THUMBS = {k: Image.open(OUT / f"thumb_{k}.png").convert("RGBA") for k in ("lemon", "teatree", "pokeweed", "cedar")}
ITEMS = [("lemon", "Lemon", 0.84), ("teatree", "Tea tree", 1.86), ("pokeweed", "Pokeweed", 2.78), ("cedar", "White cedar", 3.76)]
def circ(img, d):
    img = img.resize((d, d), Image.LANCZOS); m = Image.new("L", (d, d), 0); ImageDraw.Draw(m).ellipse((0, 0, d - 1, d - 1), fill=255)
    o = Image.new("RGBA", (d + 8, d + 8), (0, 0, 0, 0)); ImageDraw.Draw(o).ellipse((0, 0, d + 7, d + 7), fill=WHITE + (255,)); o.paste(img, (4, 4), m); return o
def plants(t):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); f = F(IB, 34); fa = F(IX, 40); x0, y0, gap = 36, 300, 118
    out = 1 - ease((t - 8.0) / 0.35)
    for k, (key, name, t0) in enumerate(ITEMS):
        a = ease((t - t0 + 0.05) / 0.22) * out
        if a <= 0: continue
        y = y0 + k * gap; s = back((t - t0 + 0.05) / 0.35); c = circ(THUMBS[key], int(84 * max(s, 0.05)))
        d = ImageDraw.Draw(im); tw = d.textlength(name, font=f)
        shadow(im, (x0, y - 46, x0 + 186 + tw, y + 46), 46, int(80 * a))
        card = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dc = ImageDraw.Draw(card)
        dc.rounded_rectangle((x0, y - 46, x0 + 186 + tw, y + 46), 46, fill=WHITE + (int(240 * a),))
        dc.text((x0 + 18, y - 26), "→", font=fa, fill=ORANGE + (int(255 * a),))
        dc.text((x0 + 166, y - 22), name, font=f, fill=NAVY + (int(255 * a),)); im.alpha_composite(card)
        ca = c.copy(); ca.putalpha(ca.getchannel("A").point(lambda v: int(v * a)))
        im.alpha_composite(ca, (int(x0 + 64 + 42 - ca.width / 2), int(y - ca.height / 2)))
    a = ease((t - 5.0) / 0.25) * out
    if a > 0: pill(im, x0 + 150, y0 + 4 * gap + 10, "= 4 bottles?", F(IX, 36), WHITE, ORANGE, back((t - 5.0) / 0.35), a)
    return im

# 3) routine steps (L16 timing): numbered chips that tick on as each step happens
STEPS = [("1", "File the hard top", 0.0, 3.1), ("2", "Brush the oil on", 3.1, 6.0), ("3", "Clear dot on top", 6.0, 7.8)]
def steps(t):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); f = F(IB, 32); fn = F(IX, 34)
    for k, (n, txt, t0, t1) in enumerate(STEPS):
        a = ease((t - t0 - 0.1) / 0.25) * (1 - ease((t - 8.0) / 0.3))
        if a <= 0: continue
        active = t0 <= t < t1; y = 1010 + k * 74 - 74 * len([s for s in STEPS if s[2] <= t]) + 74
        d = ImageDraw.Draw(im); tw = d.textlength(txt, font=f); x = 40
        L = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dl = ImageDraw.Draw(L)
        bg = (BLUE if active else (245, 247, 250)); fg = (WHITE if active else NAVY)
        dl.rounded_rectangle((x, y - 30, x + 90 + tw, y + 30), 30, fill=bg + (int(240 * a),))
        dl.ellipse((x + 8, y - 22, x + 52, y + 22), fill=(WHITE if active else BLUE) + (int(255 * a),))
        dl.text((x + 22 if n != "1" else x + 24, y - 20), n if active else "✓", font=fn, fill=(BLUE if active else WHITE) + (int(255 * a),))
        dl.text((x + 66, y - 19), txt, font=f, fill=fg + (int(255 * a),)); im.alpha_composite(L)
    return im

# 4) product callout: "2 weeks + 14 nights" tag slides in beside the bottle
def callout(t):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); o = 1 - ease((t - 3.85) / 0.3); a = ease((t - 0.3) / 0.3) * o
    pill(im, W / 2 + 60 * (1 - back((t - 0.3) / 0.45)), 200, "Most spots: ~2 weeks", F(IX, 38), WHITE, NAVY, 1, a)
    b = ease((t - 1.6) / 0.3) * o; pill(im, W / 2 + 60 * (1 - back((t - 1.6) / 0.45)), 290, "+ 14 nights for the root", F(IB, 34), NAVY, WHITE, 1, b)
    return im

# 5) CTA over the hero shot (8 s): headline, offer pill, 90-day seal, Shop now pulse + tap
def seal(im, cx, cy, r, a):
    if a <= 0: return
    L = Image.new("RGBA", (2 * r + 6, 2 * r + 6), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    d.ellipse((3, 3, 2 * r + 3, 2 * r + 3), fill=NAVY + (255,)); d.ellipse((3 + r * .12, 3 + r * .12, 2 * r + 3 - r * .12, 2 * r + 3 - r * .12), outline=WHITE + (220,), width=3)
    for txt, f, dy in (("90", F(IX, int(r * .62)), -.42), ("DAY", F(IB, int(r * .2)), .18), ("MONEY-BACK", F(IB, int(r * .18)), .42)):
        w = d.textlength(txt, font=f); d.text((r + 3 - w / 2, r + 3 + dy * r - f.size * .5), txt, font=f, fill=WHITE + (255,))
    sc = 1 + 0.4 * (1 - min(1, a)); L = L.rotate(-14 + 14 * ease(a), resample=Image.BICUBIC).resize((int(L.width * sc), int(L.height * sc)))
    L.putalpha(L.getchannel("A").point(lambda v: int(v * min(1, a * 1.4)))); shadow(im, (cx - r, cy - r, cx + r, cy + r), r, 80)
    im.alpha_composite(L, (int(cx - L.width / 2), int(cy - L.height / 2)))
def cta(t):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    g = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(g).rectangle((0, 0, W, 430), fill=(255, 250, 244, 170)); im.alpha_composite(g.filter(ImageFilter.GaussianBlur(40)))
    a1 = ease((t - 0.2) / 0.4); f1 = F(SERIF, 72)
    for k, line in enumerate(("Not the top.", "The root.")):
        a = ease((t - 0.2 - k * 0.25) / 0.4); tw = d.textlength(line, font=f1)
        d.text(((W - tw) / 2, 120 + k * 84 + 24 * (1 - a)), line, font=f1, fill=NAVY + (int(255 * a),))
    pill(im, W / 2, 350, "Buy 2, get 1 free", F(IX, 44), WHITE, ORANGE, back((t - 1.0) / 0.35) * (1 + 0.03 * math.sin(max(0, t - 1.4) * 6)), ease((t - 1.0) / 0.2))
    seal(im, 116, 1000, 80, ease((t - 1.8) / 0.35))
    ba = ease((t - 2.6) / 0.3); pul = 1 + 0.05 * math.sin(max(0, t - 3.0) * 6.5)
    pill(im, W / 2, 1120, "Shop now  ›", F(IX, 46), WHITE, ORANGE, back((t - 2.6) / 0.35) * pul, ba, 54, 22)
    rt = (t - 3.4) % 1.3
    if t > 3.4 and rt < 0.6:
        r = 24 + 90 * rt / 0.6; L = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(L).ellipse((470 - r, 1120 - r, 470 + r, 1120 + r), outline=WHITE + (int(170 * (1 - rt / 0.6)),), width=5); im.alpha_composite(L)
    fa = ease((t - 3.0) / 0.4); fs = F(IB, 26); s = "Free US shipping · No subscription"; d = ImageDraw.Draw(im)
    d.text(((W - d.textlength(s, font=fs)) / 2, 1192), s, font=fs, fill=NAVY + (int(230 * fa),))
    fd = F(IB, 20); s2 = "Dramatization."; d.text(((W - d.textlength(s2, font=fd)) / 2, 1238), s2, font=fd, fill=(90, 96, 110, int(200 * fa)))
    return im

JOBS = {"hook_h1": (hook_fn('"It came back."'), 7.6), "hook_h2": (hook_fn('"It always came back."', 6.9), 7.4),
        "hook_h3": (hook_fn("His wart is back. Again.", 4.2), 4.7), "plants": (plants, 8.4), "steps": (steps, 8.2), "callout": (callout, 4.2), "cta": (cta, 9.5)}
if __name__ == "__main__":
    for k in (sys.argv[1:] or JOBS): write(k, *JOBS[k])
