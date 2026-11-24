#!/usr/bin/env python3
"""Set 18 H1 v2 (client notes 24 Nov: voice unnatural + lips off, more b-roll, faster, energetic music).
Voice = the dad's OWN Seedance take audio wherever he is on camera (lips and voice made together, so they cannot drift),
and Seed Audio cloned from those takes for every off-camera line (same voice). Cut ~every 1.3 s, tight gaps.
Usage: python3 build18v2.py   -> out/WilloMD_RootOut_Set18_H1_9x16_v2.mp4"""
import json, os, re, subprocess, sys, difflib
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent)); import timeline as TLm
P = TLm.P; RE = P / "raw/reuse"; ST = P / "raw/stock"; GEN = P / "raw/gen"; G = P / "assets/graphics"; V2 = P / "raw/vo2"
LIB = Path("/home/user/video-studio-claude-plugin/video-studio/library/RootOut")
PDP = LIB / "brand/images/pdp"; SITE = LIB / "resources/site_videos"
OUT = P / "work/build/H1v2"; SH = OUT / "shots"; AU = OUT / "audio"; SH.mkdir(parents=True, exist_ok=True); AU.mkdir(exist_ok=True)
SFX = Path("/home/user/video-studio-claude-plugin/plugins/video-studio/skills/media-use/audio/assets/sfx")
MUSIC = P / "assets/music/Pamgaea.mp3"
FINAL = P / "out/WilloMD_RootOut_Set18_H1_9x16_v2.mp4"
W, H, FPS = 1080, 1920, 30
COVER = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}"
ENC = ["-an", "-c:v", "libx264", "-crf", "17", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-r", str(FPS)]
def ff(*a):
    r = subprocess.run(["ffmpeg", "-v", "error", "-y", *map(str, a)], capture_output=True, text=True)
    if r.returncode: sys.exit(" ".join(map(str, a))[:300] + "\n" + r.stderr[-2000:])
dur = TLm.dur; fr = lambda t: int(round(t * FPS))
def stt(f):
    j = Path(str(f) + ".stt.json")
    if not j.exists():
        subprocess.run(["curl", "-s", "-m", "180", "-X", "POST", "https://api.elevenlabs.io/v1/speech-to-text", "-H", "xi-api-key: dummy",
                        "-F", "model_id=scribe_v1", "-F", "timestamps_granularity=word", "-F", f"file=@{f}", "-o", str(j)], check=True)
    out = []
    for w in json.load(open(j))["words"]:
        if w.get("type") != "word": continue
        for p in w["text"].replace("-", " ").split(): out.append((TLm.NUM.get(TLm.norm(p), TLm.norm(p)), w["start"], w["end"]))
    return out
def find(words, phrase, after=0.0):
    ph = [TLm.NUM.get(TLm.norm(x), TLm.norm(x)) for x in phrase.replace("-", " ").split()]; ph = [x for x in ph if x]
    seq = [w[0] for w in words]; J = "".join
    for i in range(len(seq)):
        if words[i][1] < after - 0.01: continue
        for j in range(i + 1, min(len(seq), i + len(ph) + 3) + 1):
            if J(seq[i:j]) == J(ph): return words[i][1], words[j - 1][2]
    raise KeyError(f"{phrase!r} not in {' '.join(seq)}")
CLIP = lambda t: GEN / f"clips/{t}.mp4"
TTS = lambda t: V2 / f"{t}.wav"

T, Tz = "TAKE", "TAKE"
# (kind, src, text, hold_after, visuals[(phrase|None, source, opts)])
ITEMS = [
 ("take", "K1", "If your kid's doctor said, 'Leave the wart, it'll go away,' I'd bet money there's a second one coming. Ask me how I know.", 0.12,
   [(None, T, {"hook": 1}), ("Leave the wart", ST / "b03_doctor/mixkit_17475_doctor-writing-a-prescription.mp4", {"in": 2.0}),
    ("I'd bet money", T, {}), ("a second one coming", RE / "26_S19_b60_wart_back.mp4", {"in": 1.6}), ("Ask me how", T, {"zoom": 1.15})]),
 ("take", "K1", "This is how we finally got rid of it.", 0.04, [(None, T, {})]),
 ("tts", "t02", "Root and all.", 0.08, [(None, RE / "03_S1_b09_dand_root.mp4", {"in": 0.6})]),
 ("tts", "t03", "My son had one wart on his heel. One. The doctor took a look and said, 'Leave it, it'll go away.'", 0.05,
   [(None, RE / "37_S20_g12_feetup.mp4", {"in": 0.5}), ("on his heel", RE / "27_S19_b21_mason_sole.mp4", {"push": 1.12}),
    ("The doctor took", RE / "16_S17_b1_glove_wart.mp4", {}), ("and said", ST / "b03_doctor/mixkit_32176_doctor-putting-on-a-stethoscope.mp4", {"in": 6.4})]),
 ("take", "K1", "So we left it.", 0.1, [(None, T, {"zoom": 1.1})]),
 ("take", "K1", "Every week it got a little bigger.", 0.04, [(None, T, {})]),
 ("tts", "t04", "I started checking it against a Cheerio. By week six, the wart was winning.", 0.08,
   [(None, GEN / "stills/N1.png", {"push": (1.0, 1.1), "chip": "week1"}), ("By week six", GEN / "stills/N2.png", {"push": (1.05, 1.12), "chip": "week3"}),
    ("the wart was winning", GEN / "stills/N3.png", {"push": (1.05, 1.2), "chip": "week6"})]),
 ("tts", "t05", "Then a second one showed up right next to it. Then my daughter got one, on her finger. She's six.", 0.05,
   [(None, GEN / "stills/N4.png", {"push": (1.0, 1.12)}), ("Then my daughter", RE / "33_S20_g07_sister.mp4", {"in": 0.3}),
    ("on her finger", GEN / "stills/N5.png", {"push": (1.05, 1.2), "fy": 0.62})]),
 ("take", "K1", "She's wanted everything her brother had since she could walk. This, she got.", 0.7,
   [(None, T, {}), ("since she could walk", RE / "31_S19_b32_footprints.mp4", {"in": 0.5}), ("This she got", T, {"zoom": 1.18})]),
 ("take", "K1", "Turns out there's a real study on this.", 0.04, [(None, T, {})]),
 ("tts", "t06", "Almost 1,500 schoolkids. If someone at home has a wart, the other kids are about twice as likely to get one. And the 'it'll go away' part is half right. About half of kids' warts go on their own within a year. Half don't.", 0.05,
   [(None, RE / "41_S19_b29_sneakers.mp4", {"in": 0.3}), ("If someone at home", G / "w1_card.png", {"card": 1, "chip_at": ("twice as likely", "x2")}),
    ("And the", G / "w3_card.png", {"card": 1}), ("About half of", G / "w2_card.png", {"card": 1}), ("Half don't", G / "c_split.mp4", {"anim": 1})]),
 ("take", "K1", "We got the other half.", 0.05, [(None, T, {})]),
 ("pause", None, "", 1.1, [(None, RE / "25_S1_b17_hallway.mp4", {"in": 0.4})]),
 ("take", "K1", "So let me save you some time and money.", 0.04, [(None, T, {})]),
 ("tts", "t07", "Here's what you'll try next.", 0.08, [(None, GEN / "clips/G1.mp4", {})]),
 ("tts", "t08", "Freezing. Ten seconds of screaming, a milkshake on the way home, then you book the next one.", 0.05,
   [(None, RE / "24_S1_b04_clinic.mp4", {"in": 0.3, "whoosh": 1}), ("a milkshake", GEN / "stills/N6.png", {"push": (1.0, 1.1)}),
    ("then you book", G / "c_freezecal.mp4", {"anim": 1})]),
 ("take", "K2a", "Congratulations. You've got a wart subscription.", 0.3, [(None, T, {"zoom": 1.12})]),
 ("take", "K2a", "Acid from the drugstore.", 0.04, [(None, T, {"whoosh": 1})]),
 ("tts", "t09", "It turns the skin around it white.", 0.05, [(None, GEN / "stills/N7.png", {"push": (1.05, 1.2)})]),
 ("take", "K2a", "The wart doesn't even notice.", 0.2, [(None, T, {})]),
 ("tts", "t10", "Duct tape. A week of sticky socks.", 0.05,
   [(None, ST / "b07_ducttape/ov_ducttape_bandage_Conklin.jpg", {"push": (1.0, 1.08), "whoosh": 1}), ("A week of", RE / "40_S19_b25_socks.mp4", {"in": 1.6})]),
 ("take", "K2a", "Same wart.", 0.3, [(None, T, {"zoom": 1.15})]),
 ("tts", "t11a", "Every one of those has the same problem.", 0.05, [(None, RE / "21_S19_b61_shelf_sweep.mp4", {"in": 0.4})]),
 ("take", "Y1", "Freezing, acid and shaving only snap off the top,", 0.02, [(None, T, {})]),
 ("tts", "t11b", "like picking a dandelion. The root stays under the hard skin, so it grows back.", 0.08,
   [(None, RE / "00_S1_b06_dand_snap.mp4", {"in": 1.2}), ("The root stays", RE / "07_S17_x3_soil_cutaway.mp4", {}),
    ("so it grows back", G / "c_sidecut.mp4", {"anim": 1})]),
 ("take", "K2b", "You have to get under that hard skin, down to the root. That's what RootOut does. It's an oil with four plants, and each one has a job.", 0.05,
   [(None, SITE / "shopify-3062835a.mp4", {"in": 4.2, "crop": "540:780:540:100"}), ("down to the root", T, {}),
    ("That's what RootOut does", T, {"zoom": 1.1, "whoosh": 1}), ("It's an oil with four", RE / "13_S17_x9_bottle_counter.mp4", {"in": 0.5, "plants": 1}),
    ("and each one has a job", T, {})]),
 ("tts", "t13a", "Lemon softens the hard skin on top, so the oil can get in.", 0.04, [(None, RE / "08_S13_m1_skin_door.mp4", {})]),
 ("take", "K2b", "Tea tree is a thin oil.", 0.04, [(None, T, {})]),
 ("tts", "t13b", "It sinks in up to 8x deeper than a regular cream,", 0.03, [(None, RE / "46_S1_b10_towels.mp4", {"in": 0.3, "gauge": 1})]),
 ("take", "K2b", "and it carries the last two plants down with it.", 0.04, [(None, T, {})]),
 ("tts", "t13c", "Pokeweed and white cedar break the wart down from the root, so it can't grow back.", 0.08,
   [(None, RE / "15_S17_x6_root_3d.mp4", {}), ("so it can't", RE / "09_S13_m2_skin_root.mp4", {"in": 2.0})]),
 ("take", "K2b", "And it's made for kids. A kids' formula, ages 4 and up. No acid, no freezing, no blister. Just a little cool tingle. Recommended by pediatricians.", 0.15,
   [(None, T, {}), ("A kids' formula", T, {"zoom": 1.08, "chip": "kids4"}), ("No acid", PDP / "pdp-06-vs-freezing-v11.jpg", {"card": 1}),
    ("Just a little cool tingle", RE / "18_S19_b39_dot.mp4", {"in": 0.5}), ("Recommended by", T, {})]),
 ("tts", "t15", "At bedtime, two light rubs with the little file, just on the hard top. Brush the oil on. A clear dot on top. Two minutes, and they're asleep.", 0.15,
   [(None, RE / "30_S19_b52_socks_bed.mp4", {"in": 0.5}), ("two light rubs", RE / "17_S19_b37_file_kid.mp4", {"in": 0.6}),
    ("Brush the oil on", SITE / "shopify-ff701bf4.mp4", {"in": 2.3, "crop": "1080:900:0:150"}), ("A clear dot", RE / "19_S19_b55_dot_v2.mp4", {"in": 1.0}),
    ("Two minutes", ST / "b15_bedtime/mixkit_31411_sleeping-boy-moves-in-bed.mp4", {"in": 1.0, "dark": 1})]),
 ("tts", "t15d", "Does it hurt?", 0.1, [(None, RE / "38_S19_b35_pillow.mp4", {})]),
 ("girl", "r15b_girl", "Nope. It's cold and tingly.", 0.25, []),
 ("tts", "t16", "About two weeks later, his were gone. Hers too.", 0.05,
   [(None, G / "c_nights.mp4", {"anim": 1}), ("his were gone", GEN / "stills/N9.png", {"push": (1.0, 1.1)}), ("Hers too", GEN / "stills/N10.png", {"push": (1.05, 1.15), "fy": 0.62})]),
 ("take", "K3", "We kept going 14 more nights to get the roots.", 0.08, [(None, T, {"chip": "plus14"})]),
 ("tts", "t17", "Last Saturday they both ran barefoot through the sprinkler,", 0.02,
   [(None, RE / "34_S20_g14_run.mp4", {"in": 0.2}), ("through the sprinkler", ST / "b17_sprinkler/mixkit_19551_sprinkler-watering-the-grass.mp4", {"in": 9.0})]),
 ("take", "Y2", "and I didn't check a single foot.", 0.2, [(None, T, {})]),
 ("tts", "t18", "Link's below. Get two and the third one's on us,", 0.04, [(None, RE / "14_S17_x10_three_bottles.mp4", {"in": 0.8, "chip": "offer"})]),
 ("take", "K3", "so every kid has their own. And you've got 90 days. If it's not gone, every penny comes back.", 0.1,
   [(None, T, {}), ("And you've got", PDP / "pdp-09-offer-guarantee-v11.jpg", {"card": 1}), ("If it's not gone", T, {})]),
 ("take", "K3", "Or, you know, leave it. See how that goes.", 0.45, [(None, T, {"zoom": 1.06})]),
]
END = 3.0

# ---------------- audio pieces ----------------
def piece(kind, src, text):
    if kind == "take":
        w = stt(CLIP(src)); after = TAKE_CUR.get(src, 0.0); a, b = find(w, text, after); TAKE_CUR[src] = b
        return CLIP(src), max(0, a - 0.06), b + 0.1, w
    f = TTS(src) if kind == "tts" else P / f"raw/vo/{src}.mp3"; w = stt(f)
    return f, max(0, w[0][1] - 0.04), w[-1][2] + 0.1, w
TAKE_CUR = {}
def layout():
    t = 0.2; L = []
    for k, (kind, src, text, hold, vis) in enumerate(ITEMS):
        if kind == "pause": L.append(dict(k=k, kind=kind, t0=t, t1=t + hold, vis=vis)); t += hold; continue
        f, a, b, w = piece(kind, src, text)
        L.append(dict(k=k, kind=kind, src=src, text=text, f=str(f), a=a, b=b, t0=t, t1=t + (b - a), words=w, vis=vis)); t += (b - a) + hold
    return L, t
def at(item, phrase):  # absolute time of a phrase in an item
    a, _ = find(item["words"], phrase, item["a"]); return item["t0"] + (a - item["a"]) - 0.04

# ---------------- shots ----------------
def render(out, src, o, n, take=None, cin=0.0):
    z = o.get("zoom", 1.0); fy = o.get("fy", 0.5); need = n / FPS
    if src == "TAKE":
        vf = f"{COVER}" + (f",scale=iw*{z}:ih*{z},crop={W}:{H}" if z != 1 else "") + f",fps={FPS},setsar=1,tpad=stop_mode=clone:stop_duration=1"
        return ff("-ss", f"{cin:.3f}", "-i", CLIP(take), "-vf", vf, "-frames:v", n, *ENC, out)
    s = str(src)
    if o.get("card"):
        vf = (f"[0]scale={W*1.1:.0f}:{H*1.1:.0f}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=18:2,eq=brightness=-0.12,setsar=1[bg];"
              f"[1]scale=1000:-1[c];[bg][c]overlay=x=(W-w)/2:y='(H-h)/2-140+max(0,260*(1-t/0.3))',fps={FPS}")
        return ff("-loop", "1", "-i", GEN / "frames/F_K1.png", "-loop", "1", "-i", src, "-filter_complex", vf, "-frames:v", n, *ENC, out)
    if s.endswith((".png", ".jpg")):
        z0, z1 = o.get("push", (1.0, 1.08))
        vf = (f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2}:(iw-{W*2})/2:(ih-{H*2})*{fy},"
              f"zoompan=z='{z0}+({z1-z0:.3f})*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps={FPS},setsar=1")
        return ff("-loop", "1", "-i", src, "-vf", vf, "-frames:v", n, *ENC, out)
    d = dur(src); i0 = o.get("in", 0.0); avail = d - i0
    sp = 1.0 if o.get("anim") is None else max(0.8, min(1.6, d / need))
    if not o.get("anim"): sp = max(0.75, min(1.0, avail / need)) if avail < need else 1.0
    crop = f"crop={o['crop']}," if o.get("crop") else ""
    vf = f"{crop}setpts=PTS/{sp:.4f},scale={W*z:.0f}:{H*z:.0f}:force_original_aspect_ratio=increase,crop={W}:{H}:(iw-{W})/2:(ih-{H})*{fy}"
    if o.get("push"): p = o["push"]; vf += f",zoompan=z='1+({p-1:.3f})*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS}"
    if o.get("dark"): vf += f",fade=t=out:st={max(0.2, need - 0.45):.2f}:d=0.4"
    vf += f",fps={FPS},setsar=1,tpad=stop_mode=clone:stop_duration=2"
    ff("-ss", f"{i0:.3f}", "-i", src, "-vf", vf, "-frames:v", n, *ENC, out)

def build():
    L, VEND = layout(); TOTAL = VEND + END
    cuts = []  # (start, src, opts, item)
    for it in L:
        for ph, src, o in it["vis"]:
            t = it["t0"] if ph is None else at(it, ph); cuts.append((max(0.0, t), src, o, it))
    cuts.sort(key=lambda c: c[0]); cuts.append((VEND, G / "c_end.mp4", {"anim": 1}, None))
    shots = []
    for k, (t0, src, o, it) in enumerate(cuts):
        t1 = cuts[k + 1][0] if k + 1 < len(cuts) else TOTAL; n = fr(t1) - fr(t0); out = SH / f"s{k + 1:03d}.mp4"
        cin = 0.0
        if src == "TAKE": cin = it["a"] + (t0 - it["t0"])
        render(out, src, o, n, it["src"] if it else None, cin)
        shots.append(dict(n=k + 1, t0=round(t0, 3), t1=round(t1, 3), src=str(src), take=(it or {}).get("src"), opts={a: str(b) for a, b in o.items()}))
    (SH / "l.txt").write_text("".join(f"file 's{s['n']:03d}.mp4'\n" for s in shots))
    ff("-f", "concat", "-safe", "0", "-i", SH / "l.txt", "-c", "copy", OUT / "picture.mp4")
    # voice track: every piece levelled the same, light shared room
    ins, fl, mix = [], [], []
    for j, it in enumerate([i for i in L if i["kind"] != "pause"]):
        ins += ["-i", it["f"]]
        fl.append(f"[{j}]atrim={it['a']:.3f}:{it['b']:.3f},asetpts=N/SR/TB,aresample=48000,aformat=channel_layouts=mono,highpass=f=80,"
                  f"loudnorm=I=-18:TP=-3:LRA=7,afade=t=in:d=0.02,afade=t=out:st={it['b'] - it['a'] - 0.05:.3f}:d=0.05,adelay={int(it['t0'] * 1000)}[a{j}]")
        mix.append(f"[a{j}]")
    fl.append("".join(mix) + f"amix=inputs={len(mix)}:normalize=0,acompressor=threshold=-22dB:ratio=3:attack=5:release=120,apad=whole_dur={TOTAL:.3f}[vo]")
    ff(*ins, "-filter_complex", ";".join(fl), "-map", "[vo]", "-t", f"{TOTAL:.3f}", "-c:a", "pcm_s16le", OUT / "vo.wav")
    json.dump(dict(total=TOTAL, items=[{k: v for k, v in i.items() if k != "words"} for i in L], shots=shots), open(OUT / "timeline.json", "w"), indent=1)
    finish(L, shots, TOTAL)

# ---------------- finish: overlays, captions, music, grade ----------------
def ts(x): return f"{int(x // 3600)}:{int(x % 3600 // 60):02d}:{x % 60:05.2f}"
def captions(L, shots, TOTAL, path):
    toks = []
    for it in L:
        if it["kind"] == "pause": continue
        sp = it["text"].replace("1,500", "fifteen hundred").replace("8x", "eight times").split()
        shown = it["text"].split()
        # align shown words to timed words via spoken forms
        A = [TLm.NUM.get(TLm.norm(x), TLm.norm(x)) for x in sp]; ww = [w for w in it["words"] if it["a"] - 0.05 <= w[1] <= it["b"]]
        Bn = [w[0] for w in ww]; tm = [None] * len(A)
        for a, b, n in difflib.SequenceMatcher(None, A, Bn, autojunk=False).get_matching_blocks():
            for q in range(n): tm[a + q] = ww[b + q]
        for i in range(len(tm)):
            if tm[i] is None: p = next((tm[j] for j in range(i - 1, -1, -1) if tm[j]), (0, it["a"], it["a"])); tm[i] = (0, p[2], p[2] + 0.18)
        # map spoken tokens back to shown tokens (1,500 / 8x are 2 spoken words)
        si = 0
        for w in shown:
            n = 2 if w in ("1,500", "8x") else 1; s, e = tm[si][1], tm[si + n - 1][2]; si += n
            toks.append([w, it["t0"] + s - it["a"], it["t0"] + e - it["a"], it["k"]])
    gs, cur = [], []
    for t in toks:
        if cur and (t[3] != cur[-1][3] or t[1] - cur[-1][2] > 0.5): gs.append(cur); cur = []
        cur.append(t)
        if len(cur) >= 3 or (t[0][-1:] in ".,?!" and len(cur) >= 2) or sum(len(x[0]) for x in cur) > 18: gs.append(cur); cur = []
    if cur: gs.append(cur)
    cards = [(s["t0"], s["t1"]) for s in shots if s["opts"].get("card")]
    Lx = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 1080", "PlayResY: 1920", "WrapStyle: 0", "", "[V4+ Styles]",
          "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
          "Style: Cap,Inter ExtraBold,72,&H00201814,&H00201814,&H00FFFFFF,&H50000000,0,0,0,0,100,100,0,0,3,16,0,2,90,90,560,1",
          "Style: CapTop,Inter ExtraBold,66,&H00201814,&H00201814,&H00FFFFFF,&H50000000,0,0,0,0,100,100,0,0,3,16,0,8,90,90,230,1",
          "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
    for i, g in enumerate(gs):
        s = g[0][1] - 0.03; e = min(g[-1][2] + 0.2, gs[i + 1][0][1] - 0.03 if i + 1 < len(gs) else g[-1][2] + 0.2)
        if s >= TOTAL - END - 0.05: continue
        st = "CapTop" if any(a - 0.05 <= s < b for a, b in cards) else "Cap"
        Lx.append(f"Dialogue: 0,{ts(s)},{ts(e)},{st},,0,0,0,,{{\\fad(40,30)\\fscx92\\fscy92\\t(0,90,\\fscx100\\fscy100)}}{' '.join(t[0] for t in g)}")
    Path(path).write_text("\n".join(Lx) + "\n"); return [t[0] for t in toks]

def finish(L, shots, TOTAL):
    T = OUT / "fin"; T.mkdir(exist_ok=True)
    words = captions(L, shots, TOTAL, T / "cap.ass"); json.dump(words, open(T / "caption_words.json", "w"))
    ov = [(G / "hook_h1.png", 0.12, 3.0, "c", 150)]
    for s in shots:
        o = s["opts"]; it = None
        if "chip" in o:
            name = o["chip"]; y = {"offer": 300, "kids4": 820}.get(name, 980)
            ov.append((G / f"chip_{name}.png", s["t0"] + 0.15, s["t1"], "c", y))
        if "plants" in o: ov.append((G / "plants.png", s["t0"] + 0.2, s["t1"], "c", 960))
        if "chip_at" in o:
            ph, name = eval(o["chip_at"]); itm = next(i for i in L if i["kind"] == "tts" and i["src"] == "t06")
            ov.append((G / f"chip_{name}.png", at(itm, ph), s["t1"], "c", 1440))
    ins = ["-i", OUT / "picture.mp4"]; fl = ["[0]setpts=PTS-STARTPTS[v0]"]; last = "v0"
    for k, (png, t0, t1, x, y) in enumerate(ov):
        d = t1 - t0; j = k + 1; ins += ["-loop", "1", "-framerate", "30", "-t", f"{d:.2f}", "-i", png]
        X = "(W-w)/2" if x == "c" else str(x)
        fl.append(f"[{j}]format=rgba,fade=t=in:st=0:d=0.15:alpha=1,fade=t=out:st={d - 0.12:.2f}:d=0.12:alpha=1,setpts=PTS+{t0:.3f}/TB[o{j}]")
        fl.append(f"[{last}][o{j}]overlay=x={X}:y='{y}+max(0,40*(1-(t-{t0:.2f})/0.15))':eof_action=pass[v{j}]"); last = f"v{j}"
    g = next(s for s in shots if s["opts"].get("gauge")); j = len(ov) + 1
    ins += ["-framerate", "30", "-i", G / "gauge/g%03d.png"]
    fl.append(f"[{j}]setpts=PTS-STARTPTS+{g['t0'] + 0.1:.2f}/TB[g]")
    fl.append(f"[{last}][g]overlay=x=770:y=520:eof_action=pass:enable='between(t,{g['t0'] + 0.1:.2f},{g['t1']:.2f})'[vg]")
    fl.append(f"[vg]subtitles={T / 'cap.ass'}:fontsdir=/usr/share/fonts/opentype/inter,noise=alls=5:allf=t,vignette=PI/6,unsharp=5:5:0.3,format=yuv420p[vout]")
    ff(*ins, "-filter_complex", ";".join(fl), "-map", "[vout]", "-t", f"{TOTAL:.3f}", "-c:v", "libx264", "-crf", "21", "-maxrate", "9M",
       "-bufsize", "18M", "-preset", "medium", "-r", "30", T / "picture_fin.mp4")
    # sound: voice + room + whoosh on every b-roll cut (soft) + pops + energetic music ducked under voice
    sfx = []
    for s in shots:
        o = s["opts"]
        if "whoosh" in o: sfx.append((SFX / "whoosh-short.mp3", s["t0"] - 0.1, -9))
        elif s["src"] != "TAKE" and not o.get("card"): sfx.append((SFX / "whoosh-short.mp3", s["t0"] - 0.08, -21))
        if o.get("card"): sfx.append((SFX / "whoosh.mp3", s["t0"] - 0.05, -14))
        if o.get("dark"): sfx.append((SFX / "click-soft.mp3", s["t1"] - 0.5, -6))
    for png, t0, *_ in ov[1:]: sfx.append((SFX / "pop.mp3", t0, -13))
    sfx.append((SFX / "whoosh-cinematic.mp3", TOTAL - END - 0.1, -10))
    ins = ["-i", OUT / "vo.wav", "-i", MUSIC]
    fl = [f"anoisesrc=color=brown:amplitude=0.02:d={TOTAL:.2f},lowpass=f=400,volume=-14dB,aformat=channel_layouts=stereo[room]",
          "[0]aresample=48000,aformat=channel_layouts=stereo,asplit=2[vo][vok]",
          f"[1]atrim=0:{TOTAL:.2f},asetpts=N/SR/TB,volume=-14dB,afade=t=out:st={TOTAL - 1.2:.2f}:d=1.2,aformat=channel_layouts=stereo[mus]",
          "[mus][vok]sidechaincompress=threshold=0.04:ratio=5:attack=15:release=300[duck]"]
    mix = ["[vo]", "[duck]", "[room]"]
    for k, (f, t, db) in enumerate(sfx):
        j = k + 2; ins += ["-i", f]; fl.append(f"[{j}]aresample=48000,aformat=channel_layouts=stereo,volume={db}dB,adelay={max(0, int(t * 1000))}:all=1[x{j}]"); mix.append(f"[x{j}]")
    fl.append("".join(mix) + f"amix=inputs={len(mix)}:normalize=0,atrim=0:{TOTAL:.3f},loudnorm=I=-14:TP=-2.0:LRA=8[aout]")
    ff(*ins, "-filter_complex", ";".join(fl), "-map", "[aout]", "-ar", "48000", T / "mix.wav")
    ff("-i", T / "picture_fin.mp4", "-i", T / "mix.wav", "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
       "-shortest", "-movflags", "+faststart", "-map_metadata", "-1", FINAL)
    print("out", FINAL, round(TOTAL, 2), "s,", len(shots), "shots")

if __name__ == "__main__": build()
