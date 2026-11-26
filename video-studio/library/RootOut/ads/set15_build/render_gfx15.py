#!/usr/bin/env python3
"""Set 15 graphics: hook title boxes (H1-H3) and the end card (no disclaimer text, house L1)."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
LIB = Path(__file__).resolve().parents[2]
G = Path("/home/user/video-studio-claude-plugin/projects/rootout-set15/assets/graphics"); G.mkdir(parents=True, exist_ok=True)
F = "/usr/share/fonts/opentype/inter/Inter-{}.otf"
NAVY, BLUE, ICE, ORANGE, WARM = (11, 42, 91), (23, 99, 184), (238, 244, 250), (224, 78, 24), (250, 244, 236)
def font(w, s): return ImageFont.truetype(F.format(w), s)

def hook(lines, out):
    f = font("ExtraBold", 74); pad = 34
    sizes = [f.getbbox(l) for l in lines]; w = max(b[2] - b[0] for b in sizes) + pad * 2; lh = 92; h = lh * len(lines) + pad * 2 - 10
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, w - 1, h - 1), 26, fill=(255, 255, 255, 245))
    for i, l in enumerate(lines):
        col = NAVY if i == 0 else ORANGE
        d.text((w // 2, pad + i * lh), l, font=f, fill=col, anchor="ma")
    im.save(G / out)

def dandelion(d, x, y, s, whole):
    # flower head + stem above a soil line; whole = long white root below, snapped = short stub only
    soil = y + 1.0 * s
    d.rectangle((x - 0.9 * s, soil, x + 0.9 * s, soil + 0.05 * s), fill=(150, 110, 70))
    if whole:
        d.line((x, y + 0.25 * s, x, soil), fill=(70, 140, 60), width=int(0.06 * s))
        for k in range(12):
            import math; a = k / 12 * 2 * math.pi
            d.ellipse((x + 0.22 * s * math.cos(a) - 0.09 * s, y + 0.22 * s * math.sin(a) - 0.09 * s,
                       x + 0.22 * s * math.cos(a) + 0.09 * s, y + 0.22 * s * math.sin(a) + 0.09 * s), fill=(245, 200, 40))
        d.ellipse((x - 0.12 * s, y - 0.12 * s, x + 0.12 * s, y + 0.12 * s), fill=(230, 170, 20))
        d.line((x, soil, x, soil + 0.9 * s), fill=(196, 170, 120), width=int(0.07 * s))
        d.line((x, soil + 0.45 * s, x - 0.2 * s, soil + 0.75 * s), fill=(196, 170, 120), width=int(0.035 * s))
        d.line((x, soil + 0.6 * s, x + 0.18 * s, soil + 0.85 * s), fill=(196, 170, 120), width=int(0.035 * s))
    else:
        d.line((x, soil - 0.12 * s, x, soil), fill=(70, 140, 60), width=int(0.06 * s))
        d.line((x, soil, x, soil + 0.9 * s), fill=(196, 170, 120), width=int(0.07 * s))
        d.line((x - 0.07 * s, soil - 0.16 * s, x + 0.07 * s, soil - 0.1 * s), fill=(120, 120, 120), width=4)

def end_card():
    W, H = 1080, 1920; im = Image.new("RGB", (W, H), WARM); d = ImageDraw.Draw(im)
    for yy in range(H):  # soft warm gradient
        c = int(250 - 12 * yy / H); d.line((0, yy, W, yy), fill=(c, c - 6, c - 14))
    duo = Image.open(LIB / "brand/images/pdp/A12-duo-transparent.png").convert("RGBA").resize((900, 900), Image.LANCZOS)
    im.paste(duo, ((W - 900) // 2, 560), duo)
    d.text((W // 2, 230), "Not the top.", font=font("ExtraBold", 104), fill=NAVY, anchor="ma")
    d.text((W // 2, 360), "The root.", font=font("ExtraBold", 104), fill=BLUE, anchor="ma")
    dandelion(d, 130, 1240, 120, False); dandelion(d, 950, 1240, 120, True)
    bw, bh = 700, 130; x0 = (W - bw) // 2; y0 = 1640
    d.rounded_rectangle((x0, y0, x0 + bw, y0 + bh), 65, fill=ORANGE)
    d.text((W // 2, y0 + bh // 2), "Buy 2, get 1 free", font=font("ExtraBold", 66), fill="white", anchor="mm")
    im.save(G / "end_card.png")

def inset(src, out, box):
    """Rounded photo card (white border, soft shadow) cropped to the sole, like the swipe's inset photos."""
    im = Image.open(src).convert("RGB").crop(box).resize((420, 420), Image.LANCZOS)
    m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, 419, 419), 34, fill=255)
    card = Image.new("RGBA", (452, 452), (0, 0, 0, 0)); d = ImageDraw.Draw(card)
    d.rounded_rectangle((0, 0, 451, 451), 44, fill=(255, 255, 255, 255)); card.paste(im, (16, 16), m)
    card.save(G / out)

def end_overlay():
    """v2 end card overlay for the hand-held bottle clip (the swipe ends on a bottle in a hand + 'Shop Now!' + arrow)."""
    W, H = 1080, 1920; im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((110, 150, 970, 470), 40, fill=(255, 255, 255, 236))
    d.text((W // 2, 190), "Not the top.", font=font("ExtraBold", 100), fill=NAVY, anchor="ma")
    d.text((W // 2, 318), "The root.", font=font("ExtraBold", 100), fill=BLUE, anchor="ma")
    bw, bh = 760, 132; x0 = (W - bw) // 2; y0 = 1650
    d.rounded_rectangle((x0, y0, x0 + bw, y0 + bh), 66, fill=ORANGE)
    d.text((W // 2, y0 + bh // 2), "Buy 2, get 1 free", font=font("ExtraBold", 68), fill="white", anchor="mm")
    # 'Shop now' sticker, tilted, with a hand-drawn arrow down to the link
    st = Image.new("RGBA", (420, 130), (0, 0, 0, 0)); sd = ImageDraw.Draw(st)
    sd.rounded_rectangle((6, 6, 414, 124), 60, fill=(214, 40, 57, 255), outline="white", width=6)
    sd.text((210, 65), "Shop now!", font=font("Black", 70), fill="white", anchor="mm")
    st = st.rotate(-7, expand=True, resample=Image.BICUBIC); im.alpha_composite(st, (650, 1420))
    pts = [(930 + 70 * (t / 60) ** 0.6, 1520 + 330 * (t / 60) ** 1.4) for t in range(0, 61, 2)]
    d.line(pts, fill="white", width=12, joint="curve")
    ex, ey = pts[-1]; d.polygon([(ex + 4, ey + 34), (ex - 30, ey - 12), (ex + 30, ey - 14)], fill="white")
    im.save(G / "end_overlay.png")

if __name__ == "__main__":
    hook(["They froze my wart", "five times."], "hook_h1.png")  # v2: his exact words, like the swipe's hook caption
    hook(["It came back", "faster every time."], "hook_h2.png")
    hook(["“I'm done", "with my wart!”"], "hook_h3.png")
    GEN = Path("/home/user/video-studio-claude-plugin/projects/rootout-set15/raw/gen")
    inset(GEN / "e7.png", "inset_before.png", (90, 860, 950, 1720)); inset(GEN / "e9.png", "inset_after.png", (90, 860, 950, 1720))
    end_overlay(); end_card(); print("ok", sorted(p.name for p in G.iterdir()))
