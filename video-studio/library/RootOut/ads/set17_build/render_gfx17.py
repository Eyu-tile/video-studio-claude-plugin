#!/usr/bin/env python3
"""Set 17 graphics: the side cut lives on the doctor's patient-education tablet; real-photo phone inserts; sticky note;
offer and end card with 'Dramatization. AI illustration.' and the † footnote. 720x1280, 30 fps -> work/gfx/."""
import sys, math
from gfx_base import *   # skin_base, drop, ease, lerp, mix, font, write, push, sweep, badge, place_duo, warm_bg, offer_cta, ...
from PIL import Image, ImageDraw, ImageFilter
BROLL = Path("/tmp/claude-0/-home-user-video-studio-claude-plugin/0f792524-13bc-5526-a041-7b468e4bc249/scratchpad/broll")
DAG = "†Based on our manufacturer's absorption testing against a regular cream."
FOOT = "*Homeopathic claims are based on traditional homeopathic practice, not accepted medical evidence, and are not FDA evaluated. Results vary."

def tablet(inner, t, dur):
    """Frame a 720x1280 diagram as a tablet screen held in front of a blurred exam-room tone (slow drift)."""
    bg = Image.new("RGB", (W, H)); d = ImageDraw.Draw(bg)
    for y in range(H): d.line((0, y, W, y), fill=mix((196, 226, 214), (170, 200, 190), y / H))
    s = 0.86; iw, ih = int(W * s), int(H * s); scr = inner.resize((iw, ih), Image.LANCZOS)
    x0 = (W - iw) // 2 + int(6 * math.sin(t * 1.3)); y0 = (H - ih) // 2 + int(5 * math.sin(t * 0.9 + 1))
    sh = Image.new("L", (W, H), 0); ImageDraw.Draw(sh).rounded_rectangle((x0 - 10, y0 + 10, x0 + iw + 34, y0 + ih + 44), 46, fill=140)
    bg.paste((60, 70, 70), mask=sh.filter(ImageFilter.GaussianBlur(22)))
    ImageDraw.Draw(bg).rounded_rectangle((x0 - 22, y0 - 22, x0 + iw + 22, y0 + ih + 22), 44, fill=(28, 30, 34))
    m = Image.new("L", scr.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, iw - 1, ih - 1), 22, fill=255); bg.paste(scr, (x0, y0), m)
    return push(bg, t, dur, 1.0, 1.05)

def foot_note(im, txt, y=1222, size=19):
    d = ImageDraw.Draw(im); f = font(INTER_M, size); words = txt.split(); lines, cur = [], ""
    for w_ in words:
        if d.textlength(cur + " " + w_, font=f) > W - 60: lines.append(cur); cur = w_
        else: cur = (cur + " " + w_).strip()
    lines.append(cur)
    for k, l in enumerate(lines): d.text(((W - d.textlength(l, font=f)) / 2, y - (len(lines) - 1 - k) * (size + 5)), l, font=f, fill=(90, 96, 110))

def s_lemon(t, i):  # 4.5 s: the lemon drop lands, the hard top softens, a little door opens
    soft = ease((t - 1.4) / 1.4); door = ease((t - 2.4) / 1.0)
    im = skin_base(soft=soft, door=door)
    tl = ease((t - 0.2) / 0.6)
    if tl > 0:
        s = ease((t - 1.2) / 1.2); y = lerp(lerp(TOP - 330, TOP - 70, tl), TOP - 30, s)
        drop(im, CX, y, 30 * (1 - 0.7 * s), LEMON, int(255 * (1 - s)))
    return tablet(im, t, 4.5)

def gauge(im, f):
    d = ImageDraw.Draw(im); x0, y0, y1 = 650, TOP - 40, BOT - 40
    d.rounded_rectangle((x0 - 14, y0, x0 + 14, y1), 14, fill=(225, 232, 242), outline=NAVY, width=3)
    yf = lerp(y0 + 8, y1 - 8, f); d.rounded_rectangle((x0 - 9, y0 + 6, x0 + 9, yf), 9, fill=(242, 170, 60))
    for k in range(9): yy = lerp(y0 + 10, y1 - 10, k / 8); d.line((x0 - 24, yy, x0 - 16, yy), fill=NAVY, width=2)
    if f > 0.85: fb = font(INTER_B, 44); d.text((x0 - 58 - d.textlength("8x†", font=fb), yf - 28), "8x†", font=fb, fill=NAVY)

def s_tea(t, i):  # 6.5 s: cream blob stuck on top; the thin tea tree drop slides down through the door with two greens on its back
    im = skin_base(soft=1.0, door=1.0)
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)  # thick cream blob that never moves
    cx = CX - 170; dl.ellipse((cx - 70, TOP - 58, cx + 70, TOP + 6), fill=(252, 252, 250, 245), outline=(225, 225, 220, 255), width=2)
    dl.ellipse((cx - 30, TOP - 82, cx + 34, TOP - 40), fill=(252, 252, 250, 245)); im.paste(lay, (0, 0), lay)
    mv = ease((t - 1.0) / 3.6); x = CX; y = lerp(TOP - 200, HARD + 260, mv)
    drop(im, x, y, 26, TEA, 240); drop(im, x - 26, y - 40, 15, POKE, 235); drop(im, x + 26, y - 40, 15, CEDAR, 235)
    gauge(im, ease((t - 1.0) / 3.8))
    if t > 4.8: foot_note(im, DAG, y=1235, size=21)
    return tablet(im, t, 6.5)

def s_root(t, i):  # 4.5 s: pokeweed + white cedar reach the root; it cracks and breaks apart
    rb = ease((t - 0.8) / 2.4)
    im = skin_base(soft=1.0, root_break=rb, door=1.0)
    for k, col in enumerate((POKE, CEDAR)):
        y = lerp(HARD + 120, BOT - 230 + k * 40, ease(t / 1.1)); drop(im, CX - 22 + k * 44, y, 19, col, int(235 * (1 - ease((t - 2.4) / 0.8))))
    if t > 3.0: foot_note(im, FOOT, y=1235, size=17)
    return tablet(im, t, 4.5)

def s_night(t, i): return tablet(clock_scene(t, i), t, 3.2)

def phone_photo(path, t, dur, label="Photos"):
    """Mom's phone held up close: the photo app showing a real photo (CC), slight hand drift."""
    bg = Image.new("RGB", (W, H), (214, 226, 220)); bg = bg.filter(ImageFilter.GaussianBlur(4))
    ph = Image.open(path).convert("RGB"); pw, phh = 560, 1110
    scr = Image.new("RGB", (pw, phh), (0, 0, 0)); d = ImageDraw.Draw(scr)
    s = pw / ph.width; img = ph.resize((pw, int(ph.height * s)), Image.LANCZOS)
    if img.height > 820: img = img.crop((0, (img.height - 820) // 2, pw, (img.height - 820) // 2 + 820))
    scr.paste(img, (0, (phh - img.height) // 2)); f = font(INTER_M, 26)
    d.text((24, 40), "‹ " + label, font=f, fill=(80, 150, 255)); d.text((pw - 70, 40), "Edit", font=f, fill=(80, 150, 255))
    for k in range(6): d.rounded_rectangle((24 + k * 88, phh - 110, 100 + k * 88, phh - 40), 6, fill=(60 + k * 12, 60 + k * 10, 62))
    x0 = (W - pw) // 2 + int(8 * math.sin(t * 1.7)); y0 = (H - phh) // 2 + int(6 * math.sin(t * 1.1))
    ImageDraw.Draw(bg).rounded_rectangle((x0 - 16, y0 - 16, x0 + pw + 16, y0 + phh + 16), 58, fill=(20, 20, 22))
    m = Image.new("L", (pw, phh), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, pw - 1, phh - 1), 44, fill=255); bg.paste(scr, (x0, y0), m)
    return push(bg, t, dur, 1.02, 1.08)

def p_sole(t, i): return phone_photo(BROLL / "plantar_wart/Painful_plantar_warts.jpg", t, 3.0)
def p_heel(t, i): return phone_photo(BROLL / "plantar_wart/Plantar_wart_at_heel.jpg", t, 2.6)

BOT_IMG = Image.open(P / "assets/graphics/A01-bottle-front-white.jpg").convert("RGB")
def sticky(t, i):  # 3.2 s: a yellow sticky note "2 weeks + 14 nights" presses onto the real bottle photo
    s = H / BOT_IMG.height; b = BOT_IMG.resize((int(BOT_IMG.width * s), H), Image.LANCZOS)
    im = b.crop(((b.width - W) // 2, 0, (b.width - W) // 2 + W, H))
    a = ease((t - 0.4) / 0.5); nw, nh = 330, 250
    note = Image.new("RGBA", (nw, nh), (255, 236, 120, 255)); d = ImageDraw.Draw(note)
    fh = font(INTER_B, 46); fs = font(INTER_B, 40)
    d.text((26, 40), "2 weeks", font=fh, fill=(30, 40, 70)); d.text((26, 110), "+ 14 nights", font=fs, fill=(30, 40, 70))
    d.line((26, 178, 290, 182), fill=(224, 78, 24), width=5)
    note = note.rotate(-6 + 4 * (1 - a), expand=True, resample=Image.BICUBIC)
    sc = 1.25 - 0.25 * a; note = note.resize((int(note.width * sc), int(note.height * sc)))
    if a > 0:
        sh = Image.new("L", (W, H), 0); x, y = W - note.width - 18, 250 - note.height // 2
        ImageDraw.Draw(sh).rectangle((x + 12, y + 18, x + note.width + 8, y + note.height + 14), fill=int(120 * a))
        im.paste((60, 50, 40), mask=sh.filter(ImageFilter.GaussianBlur(14))); im.paste(note, (x, y), note)
    return push(im, t, 3.2, 1.0, 1.05)

def towels(t, i):  # 3 s: the paper-towel still, slow push-in, labelled as an illustration (proof pending)
    src = Image.open(P / "raw/gen/frames/f4_towels.png").convert("RGB").resize((W, H), Image.LANCZOS)
    im = push(src, t, 3.0, 1.0, 1.1); d = ImageDraw.Draw(im); f = font(INTER_M, 22); s = "Illustration"
    d.rounded_rectangle((W - 40 - d.textlength(s, font=f) - 24, 40, W - 40, 80), 18, fill=(0, 0, 0)); d.text((W - 40 - d.textlength(s, font=f) - 12, 47), s, font=f, fill=(255, 255, 255))
    foot_note(im, DAG, y=1235, size=21); return im

def end17(t, i):  # 3.2 s
    im = end_cta(t, i); d = ImageDraw.Draw(im)
    d.rectangle((0, 1196, W, H), fill=mix((250, 236, 222), (236, 214, 196), 0.95))
    f = font(INTER_B, 28); s = "Buy 2, get 1 free · 90-day money-back"; d.text(((W - d.textlength(s, font=f)) / 2, 245), s, font=f, fill=NAVY)
    foot_note(im, "Dramatization. AI illustration.", y=1205, size=22); foot_note(im, DAG, y=1240, size=17)
    return im

JOBS = {"lemon": ("t_lemon", s_lemon, 4.5), "tea": ("t_tea", s_tea, 6.5), "root": ("t_root", s_root, 4.5), "night": ("t_night", s_night, 3.2),
        "p_sole": ("p_sole", p_sole, 3.0), "p_heel": ("p_heel", p_heel, 2.6), "sticky": ("g_sticky", sticky, 3.2),
        "towels": ("g_towels", towels, 3.0), "offer": ("g_offer", offer_cta, 4.2), "end": ("g_end", end17, 3.2)}
if __name__ == "__main__":
    for k in (sys.argv[1:] or JOBS): write(*JOBS[k])
