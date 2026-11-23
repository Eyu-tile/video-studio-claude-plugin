#!/usr/bin/env python3
"""Set 4 v2 graphics, all inside the 9:16 safe zone (x 65–918, y 230–1344 on 1080x1920).
gfx_v2.py      -> v2/gfx/*.png (banner, rank cards, labels) + v2/gfx/*.mp4 (tombstone, offer, end card)"""
import math, subprocess, shutil
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

P = Path("/home/user/video-studio-claude-plugin/video-studio/projects/rootout-set4")
V2 = P / "v2"; OUT = V2 / "gfx"; OUT.mkdir(parents=True, exist_ok=True)
FD = "/usr/share/fonts/opentype/inter/"
NAVY, GOLD, ORANGE, WHITE, INK = "#0B2A5B", "#F5B700", "#E04E18", "#FFFFFF", "#13223D"
SAFE = dict(x0=65, x1=918, y0=230, y1=1344)

def font(w, s): return ImageFont.truetype(FD + {"xb": "Inter-ExtraBold.otf", "b": "Inter-Bold.otf", "sb": "Inter-SemiBold.otf", "m": "Inter-Medium.otf"}[w], s)

def shadowed(card, blur=18, off=8, alpha=90):
    """card RGBA -> same card with a soft drop shadow (canvas grows by 2*blur)."""
    W, H = card.size; c = Image.new("RGBA", (W + 4 * blur, H + 4 * blur), (0, 0, 0, 0))
    sh = Image.new("RGBA", c.size, (0, 0, 0, 0)); m = card.split()[3].point(lambda a: a * alpha // 255)
    sh.paste((0, 0, 0, 255), (2 * blur, 2 * blur + off), m); sh = sh.filter(ImageFilter.GaussianBlur(blur))
    c.alpha_composite(sh); c.alpha_composite(card, (2 * blur, 2 * blur)); return c

def pill(text, size=54, fg=WHITE, bg=(11, 42, 91, 235), pad=(34, 18), weight="xb", icon=None):
    f = font(weight, size); tw = f.getbbox(text)[2]; th = int(size * 1.0)
    iw = int(size * 1.15) if icon else 0
    W, H = tw + iw + 2 * pad[0], th + 2 * pad[1]
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, W - 1, H - 1), H // 2, fill=bg)
    x = pad[0]
    if icon == "x":
        r = size * 0.48; cx, cy = x + r, H / 2
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill="#E5383B"); k = r * 0.45
        d.line((cx - k, cy - k, cx + k, cy + k), fill=WHITE, width=max(4, size // 9)); d.line((cx - k, cy + k, cx + k, cy - k), fill=WHITE, width=max(4, size // 9))
        x += iw
    d.text((x, pad[1] + th / 2), text, font=f, fill=fg, anchor="lm")
    return shadowed(im, blur=12, off=6, alpha=70)

def rank_card(n, name, gold=False):
    W, H = 800, 156
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, W - 1, H - 1), 34, fill=NAVY if gold else WHITE)
    r = 56; cx, cy = 30 + r, H // 2
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=GOLD if gold else NAVY)
    d.text((cx, cy + 2), str(n), font=font("xb", 76), fill=NAVY if gold else WHITE, anchor="mm")
    d.text((cx + r + 34, cy - 30), "NUMBER " + str(n), font=font("b", 26), fill=GOLD if gold else "#5A6678", anchor="lm")
    d.text((cx + r + 32, cy + 18), name, font=font("xb", 64), fill=WHITE if gold else INK, anchor="lm")
    return shadowed(im)

def banner(text):
    f = font("xb", 62); tw = f.getbbox(text)[2]; W, H = tw + 80, 118
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, W - 1, H - 1), 28, fill=NAVY)
    d.rounded_rectangle((40, H - 22, W - 40, H - 14), 4, fill=GOLD)
    d.text((W / 2, 50), text, font=f, fill=WHITE, anchor="mm")
    return shadowed(im)

def save(im, name):
    im.save(OUT / f"{name}.png"); return im.size

def pngs():
    sizes = {}
    sizes["banner"] = save(banner("EVERY WART FIX, RANKED"), "banner")
    for n, name in ((1, "DUCT TAPE"), (2, "ACID PADS"), (3, "FREEZING")): sizes[f"rank{n}"] = save(rank_card(n, name), f"rank{n}")
    sizes["rank4"] = save(rank_card(4, "ROOTOUT", gold=True), "rank4")
    for key, txt, kw in (("lab_lemon", "LEMON", {}), ("lab_tea", "TEA TREE", {}), ("lab_poke", "POKEWEED · WHITE CEDAR", {"size": 46}),
                         ("x_acid", "ACID", {"icon": "x"}), ("x_freeze", "FREEZING", {"icon": "x"}), ("x_blister", "BLISTER", {"icon": "x"}),
                         ("step1", "1  FILE", {}), ("step2", "2  SOAK", {}), ("step3", "3  COVER", {}), ("night", "9 PM  →  5 AM", {}),
                         ("plus14", "+14 NIGHTS", {"bg": (245, 183, 0, 240), "fg": NAVY}),
                         ("b2g1", "BUY 2, GET 1 FREE", {"bg": (224, 78, 24, 240)}),
                         ("link", "LINK BELOW  ↓", {"bg": (224, 78, 24, 240)}),
                         ("x8", "UP TO 8x DEEPER", {"bg": (245, 183, 0, 240), "fg": NAVY}),
                         ("aiph", "AI placeholder · proof needed", {"size": 30, "weight": "sb", "bg": (0, 0, 0, 150), "pad": (22, 12)})):
        sizes[key] = save(pill(txt, **kw), key)
    return sizes

# ---------------------------------------------------------------- moving pieces (rendered frame by frame)
def frames_to_mp4(d, out, fps):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(fps), "-i", str(d / "%04d.png"), "-c:v", "libx264", "-pix_fmt", "yuv420p",
                    "-crf", "16", "-r", str(fps), str(out)], check=True); shutil.rmtree(d)

def tombstone():
    """B24 0.2–2.0 s with "R.I.P. / WART" stamped on the cardboard, tracked through the push-in."""
    src = V2 / "clips/B24_tombstone.mp4"; tmp = OUT / "_tomb"; shutil.rmtree(tmp, ignore_errors=True); tmp.mkdir()
    subprocess.run(["ffmpeg", "-v", "error", "-ss", "0.2", "-t", "1.8", "-i", str(src), "-vf", "scale=1080:1920,fps=24", str(tmp / "s%04d.png")], check=True)
    fs = sorted(tmp.glob("s*.png"))
    for i, f in enumerate(fs):
        t = 0.2 + i / 24; k = (t - 0.2) / 2.8
        cx, cy, w = (0.34 + k * 0.06) * 1080, (0.506 + k * 0.02) * 1920, (0.38 + k * 0.135) * 1080
        im = Image.open(f).convert("RGBA"); lay = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        s1 = int(w * 0.24); s2 = int(w * 0.2)
        d.text((cx, cy - s1 * 0.62), "R.I.P.", font=font("xb", s1), fill=(58, 36, 20, 225), anchor="mm")
        d.text((cx, cy + s2 * 0.72), "WART", font=font("xb", s2), fill=(58, 36, 20, 225), anchor="mm")
        im.alpha_composite(lay); im.convert("RGB").save(tmp / f"{i + 1:04d}.png"); f.unlink()
    frames_to_mp4(tmp, OUT / "tombstone.mp4", 24)

def ease(x): x = min(max(x, 0), 1); return 1 - (1 - x) ** 3

def offer():
    """Real product page (Buy 2 Get 1 selected): slow push-in, the bundle gets circled, 90-day badge pops."""
    pg = Image.open(V2 / "web/pdp_90_selected.png").convert("RGB"); pg = pg.resize((1080, round(pg.height * 1080 / pg.width)), Image.LANCZOS)
    pg = pg.crop((0, 0, 1080, 1920)) if pg.height >= 1920 else pg
    base = Image.new("RGB", (1080, 1920), "white"); base.paste(pg, (0, 0))
    tmp = OUT / "_offer"; shutil.rmtree(tmp, ignore_errors=True); tmp.mkdir(); fps, N = 30, 105
    box = (34, 566, 1046, 1070)  # the selected 90-night card
    for i in range(N):
        t = i / fps; z = 1 + 0.05 * t / (N / fps); cx, cy = 540, 820
        W, H = 1080 / z, 1920 / z; im = base.crop((cx - W * cx / 1080, cy - H * cy / 1920, cx - W * cx / 1080 + W, cy - H * cy / 1920 + H)).resize((1080, 1920), Image.LANCZOS).convert("RGBA")
        lay = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        p = ease((t - 0.15) / 0.55)
        if p > 0:
            x0, y0, x1, y1 = [(v - c) * z + c for v, c in zip(box, (cx, cy, cx, cy))]
            ex, ey, rx, ry = (x0 + x1) / 2, (y0 + y1) / 2, (x1 - x0) / 2 + 2, (y1 - y0) / 2 + 46
            pts = [(ex + rx * math.cos(-math.pi * 0.62 + a * 2.08 * math.pi * p / 60), ey + ry * math.sin(-math.pi * 0.62 + a * 2.08 * math.pi * p / 60)) for a in range(61)]
            d.line(pts, fill=(229, 56, 59, 255), width=14, joint="curve")
        q = ease((t - 0.9) / 0.3)
        if q > 0:
            r = 118 * (0.6 + 0.4 * q) * (1 + 0.06 * math.sin(min(q, 1) * math.pi)); bx, by = 900, 345
            d.ellipse((bx - r, by - r, bx + r, by + r), fill=(245, 183, 0, 255), outline=(11, 42, 91, 255), width=8)
            s = r / 150 * 1.0
            d.text((bx, by - 52 * s), "90-DAY", font=font("xb", int(50 * s)), fill=NAVY, anchor="mm")
            d.text((bx, by + 4 * s), "MONEY", font=font("xb", int(50 * s)), fill=NAVY, anchor="mm")
            d.text((bx, by + 56 * s), "BACK", font=font("xb", int(50 * s)), fill=NAVY, anchor="mm")
        im.alpha_composite(lay); im.convert("RGB").save(tmp / f"{i + 1:04d}.png")
    frames_to_mp4(tmp, OUT / "offer.mp4", fps)

def endcard():
    """Higgsfield end-card bottle (P9), whole bottle in frame with wide margins on a blurred plate of itself; type in the safe zone."""
    W, H = 1080, 1920; sc = 0.5; fw, fh = round(1080 * sc), round(1920 * sc); fx, fy = 491 - round(0.46 * fw), 290
    fr = OUT / "_p9.png"; subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "2.5", "-i", str(V2 / "clips/P9_endcard.mp4"), "-frames:v", "1", "-vf", "scale=1080:1920", str(fr)], check=True)
    px = Image.open(fr).convert("RGB"); ctop = px.getpixel((40, 120)); cbot = px.getpixel((1040, 1300))
    bg = Image.new("RGB", (W, H)); dd = ImageDraw.Draw(bg)
    for y in range(H):
        k = y / H; dd.line((0, y, W, y), fill=tuple(round(a + (b - a) * k) for a, b in zip(ctop, cbot)))
    bg.save(OUT / "_end_bg.png")
    m = Image.new("L", (fw, fh), 0); ImageDraw.Draw(m).rounded_rectangle((40, 40, fw - 40, fh - 40), 60, fill=255)
    m.filter(ImageFilter.GaussianBlur(34)).save(OUT / "_mask.png")
    top = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(top)
    d.text((491, 250), "Not the top. The root.", font=font("xb", 66), fill=NAVY, anchor="mt")
    o = pill("Buy 2, get 1 free · 90-day money-back", size=36, bg=(224, 78, 24, 245)); top.alpha_composite(o, (491 - o.width // 2, 322))
    top.save(OUT / "_end_top.png")
    bot = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(bot)
    bw, bh, by = 440, 104, 1130
    btn = Image.new("RGBA", (bw, bh), (0, 0, 0, 0)); ImageDraw.Draw(btn).rounded_rectangle((0, 0, bw - 1, bh - 1), bh // 2, fill=NAVY)
    ImageDraw.Draw(btn).text((bw / 2, bh / 2), "Shop now  →", font=font("xb", 46), fill=WHITE, anchor="mm")
    b = shadowed(btn); bot.alpha_composite(b, (491 - b.width // 2, by - 24))
    d.text((491, 1290), "AI illustration.", font=font("m", 28), fill=(19, 34, 61, 200), anchor="mm")
    bot.save(OUT / "_end_bot.png")
    g = (f"[4:v]format=rgb24[bg];[0:v]scale={fw}:{fh},format=rgba[fg0];[1:v]format=gray[mk];"
         f"[fg0][mk]alphamerge[fg];[bg][fg]overlay={fx}:{fy}[b];"
         f"[2:v]format=rgba,fade=in:st=0.15:d=0.35:alpha=1[t];[3:v]format=rgba,fade=in:st=0.7:d=0.35:alpha=1[u];"
         f"[b][t]overlay=0:0[c];[c][u]overlay=0:0,fps=30,format=yuv420p[v]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "1.8", "-t", "3.2", "-i", str(V2 / "clips/P9_endcard.mp4"), "-loop", "1", "-i", str(OUT / "_mask.png"),
                    "-loop", "1", "-i", str(OUT / "_end_top.png"), "-loop", "1", "-i", str(OUT / "_end_bot.png"), "-loop", "1", "-i", str(OUT / "_end_bg.png"), "-filter_complex", g, "-map", "[v]",
                    "-t", "3.2", "-c:v", "libx264", "-crf", "16", str(OUT / "endcard.mp4")], check=True)


QUOTES = {"w_tape": ("“little documented evidence”", "aafp.org · on duct tape"), "w_acid": ("“do not always work”", "nhs.uk · on wart creams and pads"),
          "w_freeze": ("“Repeat every two or three weeks”", "aafp.org · on freezing"), "w_cryo": ("“warts can reappear”", "clevelandclinic.org")}
def srccards():
    """Big quoted line (exact words from the source) over the real page crop, so the proof reads on a phone."""
    for n, (q, who) in QUOTES.items():
        shot = Image.open(P / "assets/graphics" / f"{n}_card.png"); shot = shot.resize((853, round(shot.height * 853 / shot.width)), Image.LANCZOS)
        f = font("xb", 56); lines, cur = [], ""
        for w in q.split():
            if font("xb", 56).getbbox((cur + " " + w).strip())[2] > 700: lines.append(cur); cur = w
            else: cur = (cur + " " + w).strip()
        lines.append(cur)
        qh = 40 + 70 * len(lines) + 56
        qc = Image.new("RGBA", (853, qh), (0, 0, 0, 0)); d = ImageDraw.Draw(qc)
        d.rounded_rectangle((0, 0, 852, qh - 1), 30, fill=WHITE)
        for i, ln in enumerate(lines):
            tw = f.getbbox(ln)[2]; y = 34 + i * 70
            d.rounded_rectangle((40, y + 14, 48 + tw, y + 62), 8, fill=(255, 212, 0, 255)); d.text((44, y), ln, font=f, fill=INK)
        d.text((44, qh - 46), who, font=font("sb", 30), fill="#5A6678")
        qc = shadowed(qc)
        out = Image.new("RGBA", (qc.width, qc.height + shot.height - 40), (0, 0, 0, 0))
        out.alpha_composite(shot, ((qc.width - shot.width) // 2, qc.height - 60)); out.alpha_composite(qc, (0, 0))
        save(out, f"src_{n}")

def phone_delete():
    """Phone calendar: the 'Wart freeze' appointment gets deleted (drawn in code so every word is real)."""
    tmp = OUT / "_phone"; shutil.rmtree(tmp, ignore_errors=True); tmp.mkdir(); fps, N = 30, 84
    for i in range(N):
        t = i / fps; im = Image.new("RGBA", (1080, 1920), (242, 242, 247, 255)); d = ImageDraw.Draw(im)
        d.text((80, 250), "‹ Calendar", font=font("sb", 40), fill="#0A84FF")
        slide = ease((t - 1.75) / 0.35) * 1200
        y0 = 360
        card = Image.new("RGBA", (920, 560), (0, 0, 0, 0)); c = ImageDraw.Draw(card)
        c.rounded_rectangle((0, 0, 919, 559), 36, fill=WHITE)
        c.rounded_rectangle((44, 50, 56, 150), 6, fill="#E5383B")
        c.text((84, 44), "Wart freeze", font=font("xb", 64), fill=INK)
        c.text((84, 130), "Pediatric clinic", font=font("m", 38), fill="#5A6678")
        c.text((84, 230), "Thursday, 3:30 – 4:00 PM", font=font("sb", 40), fill=INK)
        c.text((84, 300), "Repeat: every 2 weeks", font=font("m", 38), fill="#5A6678")
        c.text((84, 370), "Alert: 1 day before", font=font("m", 38), fill="#5A6678")
        c.line((40, 450, 880, 450), fill="#E3E3E8", width=2)
        c.text((460, 500), "Delete Event", font=font("sb", 44), fill="#E5383B", anchor="mm")
        if slide < 1150: im.alpha_composite(card, (80 - int(slide), y0))
        if t >= 1.95:
            d.text((540, 820), "No events", font=font("sb", 48), fill="#8E8E93", anchor="mm")
        # action sheet
        a = ease((t - 0.75) / 0.2) * (1 - ease((t - 1.6) / 0.15))
        if a > 0:
            sh = Image.new("RGBA", (920, 300), (0, 0, 0, 0)); s2 = ImageDraw.Draw(sh)
            s2.rounded_rectangle((0, 0, 919, 299), 30, fill=(250, 250, 252, 255))
            s2.text((460, 60), "This is a repeating event.", font=font("m", 34), fill="#8E8E93", anchor="mm")
            s2.line((0, 120, 920, 120), fill="#E3E3E8", width=2)
            s2.text((460, 210), "Delete All Future Events", font=font("sb", 44), fill="#E5383B", anchor="mm")
            sh.putalpha(sh.split()[3].point(lambda v: int(v * a)))
            im.alpha_composite(sh, (80, 960 + int((1 - a) * 80)))
        # fingertip taps
        for tt, (fx, fy) in ((0.55, (540, 860)), (1.35, (540, 1170))):
            k = (t - tt) / 0.35
            if 0 <= k <= 1:
                r = 46 + 20 * k; al = int(150 * (1 - k)); d2 = ImageDraw.Draw(im)
                d2.ellipse((fx - r, fy - r, fx + r, fy + r), fill=(120, 120, 130, al))
        im.convert("RGB").save(tmp / f"{i + 1:04d}.png")
    frames_to_mp4(tmp, OUT / "phone_delete.mp4", fps)

def wide(name="P3_hero", sc=0.62, fy=330, out="P3_hero_wide"):
    """Pull a product clip back in code: each frame shrinks to `sc`, its own edge pixels are replicated outward and blurred to
    fill the 9:16 canvas, the sharp frame is feathered in. Leaves room for the rank card and caption above the bottle."""
    import numpy as np
    src = V2 / f"clips/{name}.mp4"; fw, fh = round(1080 * sc / 2) * 2, round(1920 * sc / 2) * 2; fx = (1080 - fw) // 2
    m = Image.new("L", (fw, fh), 0); ImageDraw.Draw(m).rectangle((30, 30, fw - 30, fh - 30), fill=255); m = m.filter(ImageFilter.GaussianBlur(26))
    tmp = OUT / "_wide"; shutil.rmtree(tmp, ignore_errors=True); tmp.mkdir()
    subprocess.run(["ffmpeg", "-v", "error", "-i", str(src), "-vf", f"scale={fw}:{fh}", str(tmp / "s%04d.png")], check=True)
    for i, f in enumerate(sorted(tmp.glob("s*.png"))):
        fr = Image.open(f).convert("RGB"); a = np.asarray(fr)
        bg = Image.fromarray(np.pad(a, ((fy, 1920 - fh - fy), (fx, 1080 - fw - fx), (0, 0)), mode="edge")).filter(ImageFilter.GaussianBlur(30))
        bg.paste(fr, (fx, fy), m); bg.save(tmp / f"{i + 1:04d}.png"); f.unlink()
    frames_to_mp4(tmp, OUT / f"{out}.mp4", 24)

if __name__ == "__main__":
    import sys
    what = sys.argv[1:] or ["pngs", "srccards", "tombstone", "offer", "endcard", "phone_delete"]
    for w in what: print(w, globals()[w]() or "ok")
