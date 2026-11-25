#!/usr/bin/env python3
"""Set 14 H1 builder: narrator VO + two parent takes, ~3 s b-roll cut on the narrator's words (L2/L3), each source once
(L4), captions = the script text word by word (L5), voice + music only (L7), music to the last frame (L6), no disclaimer
text (house L1). Inputs: projects/rootout-set14/raw/{reuse,gen}. Usage: python3 build14.py [--preview]
Out: projects/rootout-set14/out/WilloMD_RootOut_Set14_H1_9x16_v1.mp4"""
import json, re, subprocess, sys, difflib, math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

P = Path("/home/user/video-studio-claude-plugin/video-studio/projects/rootout-set14")
LIB = Path("/home/user/video-studio-claude-plugin/video-studio/library/RootOut")
R, GN = P / "raw/reuse", P / "raw/gen"
W, H, FPS = 1080, 1920, 30
PREVIEW = "--preview" in sys.argv
T = P / "work/h1"; T.mkdir(parents=True, exist_ok=True); G = P / "work/gfx"; G.mkdir(parents=True, exist_ok=True)
OUT = P / "out" / ("WilloMD_RootOut_Set14_H1_9x16_v1" + ("_preview" if PREVIEW else "") + ".mp4"); OUT.parent.mkdir(exist_ok=True)
NAVY, BLUE, ICE, ORANGE, WHITE = (11, 42, 91), (23, 99, 184), (238, 244, 250), (224, 78, 24), (255, 255, 255)
F = lambda w, s: ImageFont.truetype(f"/usr/share/fonts/opentype/inter/Inter-{w}.otf", s)

def run(*a):
    r = subprocess.run([str(x) for x in a], capture_output=True, text=True)
    if r.returncode: sys.exit(r.stderr[-3000:])
    return r.stdout
def ff(*a): run("ffmpeg", "-v", "error", "-y", *a)
def dur(f): return float(run("ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f))

# ---------------- script lines (verbatim brief text) ----------------
LINES = [
 ("n01", "Why won't store wart treatments work on the bottom of a kid's foot?"),
 ("n02", "If you've tried everything and nothing is working, here's why."),
 ("n03", "On a foot, dead skin piles up on top of the wart. Store stuff stops there."),
 ("n04", "Freezing, acid and shaving only snap off the top, like picking a dandelion. The root stays under the hard skin, so it grows back."),
 ("n05", "RootOut takes a different path. It's an oil with four plants, and each one has a job. Lemon opens the hard skin on top, so the oil can get in. Tea tree is a thin oil that carries the others down, up to 8x deeper than a regular cream."),
 ("n06", "Then pokeweed and white cedar, used on warts for over a hundred years, break the wart down from the root, so it can't grow back. One alone can't do it. Together, they reach all the way down. And a clear dot locks them in all night."),
 ("n07", "Deep doesn't mean harsh. It's a kids' formula, ages 4 and up. No acid, no freezing, no blister. Just a little cool tingle. Recommended by pediatricians."),
 ("n08", "Here's what you do at bedtime. Rub the little file over it, twice. Only on the hard top, so it doesn't hurt. Then brush the oil on."),
 ("t1",  "She said it didn't hurt. Kept reading her book."),
 ("n09", "It dries out, goes darker, then flakes off. Smooth skin underneath. No scar."),
 ("n10", "Most spots are gone in about 2 weeks. Then keep going 14 more nights, so the root goes too. That's the Root Rule."),
 ("t2",  "His heel took about two weeks. We kept going, to make sure it was gone."),
 ("n11", "Tried the store stuff already? Get yours from the link below. Order two, get a third free. And if it's not gone, you get your money back within 90 days. You don't even send it back."),
]
TEXT = dict(LINES)
AUDIO = {k: GN / f"{k}.mp3" for k, _ in LINES if k.startswith("n")}
AUDIO["t1"], AUDIO["t2"] = GN / "t1.mp4", GN / "t2.mp4"
GAP = {"n01": 0.35, "n08": 0.3, "t1": 0.35, "n10": 0.3, "t2": 0.35}  # pause after a line (default 0.22)
END_CARD = 3.0

NUM = {"8x": "eight", "4": "four", "2": "two", "14": "fourteen", "90": "ninety", "rootout": "rootout"}
def norm(w): return re.sub(r"[^a-z0-9x]", "", w.lower().replace("’", "'"))
def words(key):
    f = T / f"tr_{key}.json"
    if not f.exists(): run("vs", "transcribe", AUDIO[key], "-o", T / f"tr_{key}", "--prompt", TEXT[key])
    out = []
    for w in json.load(open(f))["words"]:
        for i, part in enumerate(w["w"].split()):
            out.append((norm(part), w["s"], w["e"]))
    return out

# speech span (trim lead/tail silence) per line
def span(key):
    W_ = words(key); return max(0, W_[0][1] - 0.06), W_[-1][2] + 0.12

# ---------------- timeline: line start times ----------------
AT, SPAN, t = {}, {}, 0.0
for k, _ in LINES:
    s, e = span(k); SPAN[k] = (s, e); AT[k] = t - s; t += (e - s) + GAP.get(k, 0.22)
TOTAL = t + END_CARD

def script_tokens(key):  # script words with times, joined to the transcript by difflib
    spoken = TEXT[key].split(); A = []
    for x in spoken:
        n = norm(x); A.append(NUM.get(n, n))
    A = [a.replace("kids", "kids") for a in A]; Wd = words(key); Bn = [w[0] for w in Wd]
    # transcript quirks seen on these takes
    Bn = ["rootout" if (b == "root" and i + 1 < len(Bn) and Bn[i + 1] == "out") else b for i, b in enumerate(Bn)]
    sm = difflib.SequenceMatcher(None, A, Bn, autojunk=False); times = [None] * len(A)
    for a, b, n in sm.get_matching_blocks():
        for k in range(n): times[a + k] = (Wd[b + k][1], Wd[b + k][2])
    for i in range(len(A)):
        if times[i] is None:
            p = next((times[j] for j in range(i - 1, -1, -1) if times[j]), (SPAN[key][0], SPAN[key][0]))
            nx = next((times[j] for j in range(i + 1, len(A)) if times[j]), (p[1] + 0.3, p[1] + 0.3))
            times[i] = (p[1], max(p[1] + 0.12, nx[0]))
    return [(spoken[i], AT[key] + times[i][0], AT[key] + times[i][1]) for i in range(len(A))]
TOK = {k: script_tokens(k) for k, _ in LINES}
def at(key, phrase):  # absolute time where `phrase` (script words) starts in line `key`
    toks = TOK[key]; ph = [norm(x) for x in phrase.split()]
    for i in range(len(toks)):
        if [norm(x[0]) for x in toks[i:i + len(ph)]] == ph: return toks[i][1] - 0.08
    sys.exit(f"phrase not found: {key} / {phrase}")
def line_start(key): return AT[key] + SPAN[key][0]
def line_end(key): return AT[key] + SPAN[key][1]

# ---------------- shot list: (start time, source, src offset, options) ----------------
S = lambda n: R / n
SHOTS = [
 (line_start("n01"), GN / "hook.mp4", 0.0, {}),
 (line_start("n02"), S("01_s4_B6_padpress.mp4"), 0.6, {}),
 (at("n02", "and nothing is working"), S("48_s1_b04_clinic.mp4"), 0.4, {}),
 (at("n02", "here's why."), S("04_s4_D3_rootstill.mp4"), 0.0, {}),
 (at("n03", "Store stuff stops there."), S("05_s4_D1_tape3d.mp4"), 0.5, {}),
 (line_start("n04"), S("03_s4_D2_toponly.mp4"), 0.0, {}),
 (at("n04", "like picking a dandelion."), S("12_s1_dand_snap.mp4"), 0.6, {}),
 (at("n04", "The root stays"), S("13_s17_x3_soil.mp4"), 0.0, {}),
 (line_start("n05"), S("44_s4_P2_slidein.mp4"), 0.0, {}),
 (at("n05", "It's an oil with four plants"), S("28_s4_P4_flatlay.mp4"), 0.0, {}),
 (at("n05", "Lemon opens the hard skin"), S("21_s4_D4_lemon.mp4"), 0.4, {}),
 (at("n05", "Tea tree is a thin oil"), S("30_s4_B15_teatree.mp4"), 0.0, {}),
 (at("n05", "that carries the others down"), S("23_s4_D6_carry.mp4"), 0.3, {}),
 (at("n05", "up to 8x deeper"), S("22_s4_D5_sink.mp4"), 0.2, {"gauge": 1}),
 (line_start("n06"), S("31_s4_B16_pokeweed.mp4"), 0.0, {}),
 (at("n06", "break the wart down"), S("24_s4_D7_crumble.mp4"), 0.0, {}),
 (at("n06", "One alone can't do it."), S("25_s4_D8_together.mp4"), 0.0, {}),
 (at("n06", "And a clear dot"), S("34_s19_b55_dot.mp4"), 0.5, {"clock": 1}),
 (line_start("n07"), S("27_s4_P3_hero.mp4"), 0.0, {}),
 (at("n07", "No acid, no freezing"), S("43_s4_P1_lineup.mp4"), 0.0, {}),
 (at("n07", "Just a little cool tingle."), S("38_s19_b43_clear.mp4"), 0.3, {}),
 (at("n07", "Recommended by pediatricians."), S("47_s17_b1_glove.mp4"), 0.3, {}),
 (line_start("n08"), S("60_s5_h3_foot.mp4"), 1.5, {}),
 (at("n08", "Rub the little file"), S("32_s19_file_kid.mp4"), 0.6, {}),
 (at("n08", "Only on the hard top"), S("33_s17_b2_routine.mp4"), 0.0, {"zoom": 1.12}),
 (line_start("t1") - 0.12, GN / "t1.mp4", None, {"talk": "t1"}),
 (line_start("n09"), S("11_k25_a72f.mp4"), 0.0, {}),
 (at("n09", "Smooth skin underneath."), S("37_s4_B18_smoothsole.mp4"), 0.0, {}),
 (line_start("n10"), S("40_s5_i05_calX.mp4"), 0.0, {}),
 (at("n10", "Then keep going 14"), S("39_s4_B20_plus14.mp4"), 0.0, {}),
 (at("n10", "That's the Root Rule."), S("61_s1_dand_root.mp4"), 0.5, {}),
 (line_start("t2") - 0.12, GN / "t2.mp4", None, {"talk": "t2"}),
 (line_start("n11"), S("62_s19_shelf_sweep.mp4"), 0.0, {}),
 (at("n11", "Get yours from the link below."), S("42_s19_three.mp4"), 0.0, {}),
 (at("n11", "Order two, get a third free."), S("41_s17_x10_three.mp4"), 1.0, {}),
 (at("n11", "And if it's not gone"), "CARD_OFFER", 0.0, {}),
 (at("n11", "You don't even send it back."), S("63_s4_P9_endcard.mp4"), 0.0, {}),
 (TOTAL - END_CARD, "END_CARD", 0.0, {}),
]

# ---------------- graphics ----------------
def shadowed(img, r=34, blur=16, off=8, alpha=110):
    w, h = img.size; sh = Image.new("RGBA", (w + 80, h + 80), (0, 0, 0, 0))
    m = Image.new("L", (w, h), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, w - 1, h - 1), r, fill=alpha)
    sh.paste((0, 0, 0, alpha), (40, 40 + off), m); sh = sh.filter(ImageFilter.GaussianBlur(blur)); sh.alpha_composite(img, (40, 40)); return sh
def hook_box(out):
    lines = ["Why store wart stuff", "fails on kids' feet"]; f = F("ExtraBold", 70)
    d0 = ImageDraw.Draw(Image.new("RGB", (1, 1))); tw = max(d0.textlength(l, font=f) for l in lines)
    w, h = int(tw + 96), 2 * 84 + 56; img = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    d.rounded_rectangle((0, 0, w - 1, h - 1), 26, fill=ORANGE + (255,))
    for i, l in enumerate(lines): d.text(((w - d.textlength(l, font=f)) / 2, 22 + i * 84), l, font=f, fill=WHITE)
    shadowed(img, 26).save(out)
def gauge_frames(d):
    d.mkdir(exist_ok=True); n = 60
    for i in range(n):
        p = min(1, i / 45); p = 1 - (1 - p) ** 3
        img = Image.new("RGBA", (240, 760), (0, 0, 0, 0)); g = ImageDraw.Draw(img)
        g.rounded_rectangle((70, 40, 170, 640), 50, fill=(255, 255, 255, 215))
        top = 640 - int(600 * p); g.rounded_rectangle((80, max(50, top), 160, 630), 40, fill=(240, 170, 40, 255))
        f = F("Black", 92); txt = f"{max(1, round(8 * p))}x"; tw = g.textlength(txt, font=f)
        g.text(((240 - tw) / 2, 652), txt, font=f, fill=WHITE, stroke_width=6, stroke_fill=NAVY)
        img.save(d / f"g{i:03d}.png")
def clock_frames(d):
    d.mkdir(exist_ok=True); n = 90
    for i in range(n):
        p = i / (n - 1); hrs = 9 + 8 * p; hh = int(hrs) % 12 or 12; ap = "PM" if int(hrs) < 12 else "AM"
        img = Image.new("RGBA", (420, 160), (0, 0, 0, 0)); g = ImageDraw.Draw(img)
        g.rounded_rectangle((0, 0, 419, 159), 80, fill=NAVY + (235,))
        cx, cy, r = 80, 80, 52; g.ellipse((cx - r, cy - r, cx + r, cy + r), outline=WHITE, width=6)
        a = math.radians((hrs % 12) / 12 * 360 - 90); g.line((cx, cy, cx + 30 * math.cos(a), cy + 30 * math.sin(a)), fill=WHITE, width=7)
        a2 = math.radians((p * 8 % 1) * 360 - 90); g.line((cx, cy, cx + 44 * math.cos(a2), cy + 44 * math.sin(a2)), fill=(240, 170, 40), width=4)
        g.text((160, 38), f"{hh} {ap}", font=F("ExtraBold", 76), fill=WHITE)
        img.save(d / f"c{i:03d}.png")
def offer_card(out):
    bg = Image.new("RGB", (W, H), (229, 238, 248)); card = Image.open(LIB / "brand/images/pdp/pdp-09-offer-guarantee-v11.jpg").convert("RGB").resize((1040, 1040), Image.LANCZOS)
    bg.paste(card, (20, (H - 1040) // 2 - 60)); bg.save(out)
def end_card(out):
    bg = Image.new("RGB", (W, H), ICE); d = ImageDraw.Draw(bg)
    snap = Image.open(G / "stub.png").convert("RGB"); root = Image.open(G / "root.png").convert("RGB")
    def tile(im, x, y, s=380):
        im = im.resize((s, int(s * im.height / im.width)), Image.LANCZOS).crop((0, 0, s, s))
        m = Image.new("L", (s, s), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, s - 1, s - 1), 40, fill=255); bg.paste(im, (x, y), m)
    tile(snap, 120, 300); tile(root, W - 500, 300)
    f = F("ExtraBold", 54); d.text((310 - d.textlength("The top", font=f) / 2, 700), "The top", font=f, fill=(120, 130, 150))
    d.text((W - 310 - d.textlength("The root", font=f) / 2, 700), "The root", font=f, fill=NAVY)
    d.line((178, 727, 442, 727), fill=ORANGE, width=8)
    bott = Image.open(LIB / "brand/images/pdp/A12-duo-transparent.png").convert("RGBA"); bott = bott.resize((760, 760), Image.LANCZOS)
    bg.paste(bott, ((W - 760) // 2, 790), bott)
    f2 = F("Black", 96); t1 = "Not the top. The root."; f2 = F("Black", 84)
    d.text(((W - d.textlength(t1, font=f2)) / 2, 150), t1, font=f2, fill=NAVY)
    t2 = "Order 2, get 1 free"; f3 = F("ExtraBold", 66); tw = d.textlength(t2, font=f3)
    d.rounded_rectangle(((W - tw) / 2 - 50, 1580, (W + tw) / 2 + 50, 1700), 60, fill=ORANGE)
    d.text(((W - tw) / 2, 1598), t2, font=f3, fill=WHITE); bg.save(out)

def make_gfx():
    hook_box(G / "hook.png"); gauge_frames(G / "gauge"); clock_frames(G / "clock"); offer_card(G / "offer.png")
    ff("-ss", "3.5", "-i", R / "12_s1_dand_snap.mp4", "-frames:v", "1", "-vf", "crop=iw:iw:0:ih*0.35", G / "stub.png")
    ff("-ss", "2.0", "-i", R / "61_s1_dand_root.mp4", "-frames:v", "1", "-vf", "crop=iw:iw:0:ih*0.15", G / "root.png")
    end_card(G / "end.png")

# ---------------- render shots ----------------
VF = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,fps={FPS}"
def render_shot(i, t0, t1, src, off, o):
    d = t1 - t0; out = T / f"s{i:02d}.mp4"
    if src in ("CARD_OFFER", "END_CARD"):
        png = G / ("offer.png" if src == "CARD_OFFER" else "end.png"); z = 0.06 if src == "CARD_OFFER" else 0.03
        ff("-loop", "1", "-framerate", FPS, "-t", f"{d:.3f}", "-i", png, "-vf",
           f"scale={W*2}:{H*2},zoompan=z='1+{z}*on/({d*FPS:.0f})':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS},setsar=1",
           "-t", f"{d:.3f}", "-an", "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", out); return out, 1.0
    if o.get("talk"):
        k = o["talk"]; s0 = SPAN[k][0] - 0.12; src_d = dur(src); s0 = max(0, min(s0, src_d - d))
        ff("-ss", f"{s0:.3f}", "-i", src, "-t", f"{d:.3f}", "-vf", VF, "-an", "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", out); return out, 1.0
    avail = dur(src) - off; speed = 1.0
    if avail < d: speed = avail / d
    if speed < 0.75: sys.exit(f"shot {i} {src.name}: needs {d:.2f}s, has {avail:.2f}s (speed {speed:.2f} < 0.75)")
    z = o.get("zoom", 1.0); vf = VF + (f",scale={int(W*z)}:{int(H*z)},crop={W}:{H}" if z != 1.0 else "")
    ff("-ss", f"{off:.3f}", "-i", src, "-vf", f"setpts=PTS/{speed:.4f},{vf}", "-t", f"{d:.3f}", "-an", "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", out)
    return out, speed

def main():
    make_gfx()
    starts = [s[0] for s in SHOTS] + [TOTAL]; rows = []
    for i, (t0, src, off, o) in enumerate(SHOTS):
        t1 = starts[i + 1]; f, sp = render_shot(i, t0, t1, src, off, o)
        rows.append({"i": i, "t0": round(t0, 3), "t1": round(t1, 3), "dur": round(t1 - t0, 2), "src": str(src if isinstance(src, str) else src.name), "speed": round(sp, 3), "opts": o})
    json.dump({"total": TOTAL, "at": AT, "shots": rows}, open(T / "timeline.json", "w"), indent=1)
    (T / "list.txt").write_text("".join(f"file 's{r['i']:02d}.mp4'\n" for r in rows))
    ff("-f", "concat", "-safe", "0", "-i", T / "list.txt", "-c", "copy", T / "picture.mp4")
    # ---- voice track ----
    ins, fl = [], []
    for j, (k, _) in enumerate(LINES):
        s, e = SPAN[k]; ins += ["-i", AUDIO[k]]
        fl.append(f"[{j}:a]atrim={s:.3f}:{e:.3f},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=mono,"
                  f"afade=t=in:d=0.03,afade=t=out:st={e - s - 0.05:.3f}:d=0.05,adelay={int((AT[k] + s) * 1000)}[a{j}]")
    fl.append("".join(f"[a{j}]" for j in range(len(LINES))) + f"amix=inputs={len(LINES)}:normalize=0,apad,atrim=0:{TOTAL:.3f}[vo]")
    ff(*ins, "-filter_complex", ";".join(fl), "-map", "[vo]", "-ar", "48000", T / "vo.wav")
    # ---- captions (script text, word by word, active word highlighted) ----
    toks = [x + (k,) for k, _ in LINES for x in TOK[k]]
    groups, cur = [], []
    for tk in toks:
        if cur and (tk[3] != cur[-1][3] or tk[1] - cur[-1][2] > 0.5): groups.append(cur); cur = []
        cur.append(tk)
        if len(cur) >= 3 or (tk[0][-1:] in ".,?!" and len(cur) >= 2) or sum(len(x[0]) for x in cur) > 18: groups.append(cur); cur = []
    if cur: groups.append(cur)
    def ts(x): return f"{int(x // 3600)}:{int(x % 3600 // 60):02d}:{x % 60:05.2f}"
    A = ["[Script Info]", "ScriptType: v4.00+", f"PlayResX: {W}", f"PlayResY: {H}", "WrapStyle: 2", "", "[V4+ Styles]",
         "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
         "Style: Cap,Inter ExtraBold,74,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,0,0,0,0,100,100,0,0,1,7,2,2,80,80,430,1",
         "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
    offer_t0 = next(r["t0"] for r in rows if r["src"] == "CARD_OFFER"); offer_t1 = next(r["t1"] for r in rows if r["src"] == "CARD_OFFER")
    for gi, g in enumerate(groups):
        g_end = min(g[-1][2] + 0.3, groups[gi + 1][0][1] if gi + 1 < len(groups) else g[-1][2] + 0.3)
        mv = 250 if offer_t0 - 0.05 <= g[0][1] < offer_t1 else 430   # keep clear of the offer card
        for wi, w in enumerate(g):
            s = w[1]; e = g[wi + 1][1] if wi + 1 < len(g) else g_end
            txt = " ".join(("{\\c&H2AB4F5&}" + x[0].upper() + "{\\c&HFFFFFF&}") if xi == wi else x[0].upper() for xi, x in enumerate(g))
            A.append(f"Dialogue: 0,{ts(s)},{ts(e)},Cap,,0,0,{mv},,{txt}")
    (T / "captions.ass").write_text("\n".join(A) + "\n")
    # ---- overlays + captions + finish ----
    hook_end = SHOTS[1][0]; g_shot = next(r for r in rows if r["opts"].get("gauge")); c_shot = next(r for r in rows if r["opts"].get("clock"))
    ins = ["-i", T / "picture.mp4", "-loop", "1", "-framerate", FPS, "-t", f"{hook_end:.2f}", "-i", G / "hook.png",
           "-framerate", FPS, "-i", G / "gauge/g%03d.png", "-framerate", FPS, "-i", G / "clock/c%03d.png"]
    cd = c_shot["t1"] - c_shot["t0"]
    fl = ["[1]format=rgba,fade=t=out:st=%.2f:d=0.2:alpha=1[hk]" % (hook_end - 0.25),
          "[0][hk]overlay=x=(W-w)/2:y=170:eof_action=pass[v1]",
          f"[2]setpts=PTS-STARTPTS+{g_shot['t0'] + 0.15:.2f}/TB,tpad=stop_mode=clone:stop_duration=8[g]",
          f"[v1][g]overlay=x=800:y=360:enable='between(t,{g_shot['t0'] + 0.15:.2f},{g_shot['t1']:.2f})'[v2]",
          f"[3]setpts=(PTS-STARTPTS)*{cd * 0.95 / 3.0:.4f}+{c_shot['t0'] + 0.1:.2f}/TB,tpad=stop_mode=clone:stop_duration=8[c]",
          f"[v2][c]overlay=x=(W-w)/2:y=240:enable='between(t,{c_shot['t0'] + 0.1:.2f},{c_shot['t1']:.2f})'[v3]",
          f"[v3]subtitles={T / 'captions.ass'}:fontsdir=/usr/share/fonts/opentype/inter,noise=alls=5:allf=t,unsharp=5:5:0.3,format=yuv420p[vout]"]
    enc = ["-c:v", "libx264", "-crf", "28" if PREVIEW else "19", "-preset", "veryfast" if PREVIEW else "medium", "-maxrate", "9M", "-bufsize", "18M"]
    ff(*ins, "-filter_complex", ";".join(fl), "-map", "[vout]", "-t", f"{TOTAL:.3f}", *enc, "-r", FPS, T / "picture_fin.mp4")
    # ---- mix: voice + music (ducked under speech, lifted where nobody speaks, short fade on the last frame) ----
    MUS = P / "assets/music/Inspired.mp3"
    fl = ["[0]aresample=48000,aformat=channel_layouts=stereo,asplit=2[vo][key]",
          f"[1]atrim=0:{TOTAL:.3f},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,volume=-15dB[m]",
          "[m][key]sidechaincompress=threshold=0.02:ratio=5:attack=30:release=500[duck]",
          f"[vo][duck]amix=inputs=2:normalize=0,afade=t=out:st={TOTAL - 0.6:.3f}:d=0.6,atrim=0:{TOTAL:.3f},loudnorm=I=-14:TP=-2.0:LRA=9[aout]"]
    ff("-i", T / "vo.wav", "-stream_loop", "-1", "-i", MUS, "-filter_complex", ";".join(fl), "-map", "[aout]", "-ar", "48000", T / "mix.wav")
    ff("-i", T / "picture_fin.mp4", "-i", T / "mix.wav", "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
       "-map_metadata", "-1", "-shortest", "-movflags", "+faststart", OUT)
    print("out", OUT, round(TOTAL, 2), "s,", len(rows), "shots")
    for r in rows: print(f"{r['i']:2d} {r['t0']:7.2f} {r['dur']:5.2f}s x{r['speed']:.2f} {r['src']}")
if __name__ == "__main__": main()
