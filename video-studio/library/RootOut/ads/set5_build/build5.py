#!/usr/bin/env python3
"""Set 5 H1 edit: hook + body + end card -> captions, music, phone finish.
One LINE = one verbatim VO line (Helena, ElevenLabs) played over b-roll, or one lip-synced talking clip that plays our
ElevenLabs line aligned to the clip's own speech (Seedance re-voices the reference, so its own audio is not used).
Pace follows SoFyre #004 (references/sofyre-004/ANALYSIS.md): NIGHT stamps on the blurred next shot, split screens for
plant + job, grey + red X for old fixes, real PDP card with a tap on the bundle, captions on every shot.
House rules: each source once (talking clips may be cut inside their own line), no frozen frames (slow >= 0.7x, stills
always move), no disclaimer text on screen (L1), lip-synced clip only under its own line.
Usage: build5.py [line names to rebuild...]   -> out/WilloMD_RootOut_Set5_H1_9x16_v2.mp4"""
import json, re, subprocess, sys, difflib
from pathlib import Path

P = Path("/home/user/video-studio-claude-plugin/video-studio/projects/rootout-set5")
L = Path("/home/user/video-studio-claude-plugin/video-studio/library/RootOut")
G, RU, VO, GX, FR = P / "raw/gen", P / "raw/reuse", P / "raw/vo", P / "assets/graphics", P / "raw/frames"
ST = L / "stock/assets/set5"; SV, SP = ST / "video", ST / "photo"
HOWTO = L / "resources/site_videos/shopify-ff701bf4.mp4"
TMP = P / "work/body"; TMP.mkdir(parents=True, exist_ok=True); OUTD = P / "out"; OUTD.mkdir(exist_ok=True)
W, H, FPS = 1080, 1920, 30
ENC = ["-c:v", "libx264", "-crf", "17", "-preset", "medium", "-pix_fmt", "yuv420p", "-r", str(FPS)]
FONT = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"


norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())


def dur(f): return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)]))


def run(a):
    r = subprocess.run(["ffmpeg", "-y", "-v", "error", *a], capture_output=True, text=True)
    if r.returncode: sys.exit(r.stderr[-3000:])


COVER = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1"
EASE = "(1-pow(1-min(1,t/{d}),3))"
TRANS = {  # seven different cuts-in (client note on Set 20: varied, no whoosh)
    "punch": "scale=w='trunc(1080*(1+0.16*max(0,1-t/0.28))/2)*2':h=-2:eval=frame,crop=1080:1920",
    "whip": "pad=2160:1920:1080:0:black,crop=1080:1920:x='1080*" + EASE.format(d=0.26) + "':y=0",
    "dip": "fade=t=in:st=0:d=0.3",
    "flash": "eq=brightness='0.5*max(0,1-t/0.22)':eval=frame",
    "slide": "pad=1080:3840:0:1920:black,crop=1080:1920:x=0:y='1920*" + EASE.format(d=0.28) + "'",
    "spin": "scale=1242:2208,rotate=a='0.14*pow(max(0,1-t/0.32),2)':fillcolor=black,crop=1080:1920",
    "zoomout": "scale=w='trunc(1080*(1+0.22*pow(max(0,1-t/0.35),2))/2)*2':h=-2:eval=frame,crop=1080:1920",
}
CLOCK = None


def clock_filter(d, m0=21 * 60, m1=31 * 60):
    """small bedside-style clock, 9:00 PM -> 7:00 AM over the shot (drawtext, no extra text)."""
    M = f"({m0}+{m1 - m0}*t/{d:.3f})"
    hh = f"mod(floor({M}/60)\\,24)"; h12 = f"(mod({hh}+11\\,12)+1)"; mm = f"mod(floor({M})\\,60)"
    base = (f"drawbox=x=700:y=150:w=320:h=120:color=black@0.45:t=fill,"
            f"drawtext=fontfile={FONT}:fontsize=72:fontcolor=white:x=730:y=172:text='%{{eif\\:{h12}\\:d}}\\:%{{eif\\:{mm}\\:d\\:2}}'")
    pm = f",drawtext=fontfile={FONT}:fontsize=40:fontcolor=white:x=935:y=200:text='PM':enable='lt({M}\\,1440)'"
    am = f",drawtext=fontfile={FONT}:fontsize=40:fontcolor=white:x=935:y=200:text='AM':enable='gte({M}\\,1440)'"
    return base + pm + am


def ovchain(ovs, first=1, base="[v0]"):
    s, cur = "", base
    for i, _ in enumerate(ovs):
        s += f";{cur}[{i + first}:v]overlay=0:0[o{i}]"; cur = f"[o{i}]"
    return s, cur


def src_chain(kind, src, d, idx, ss=0.0, crop=None, extra="", size=(W, H)):
    """filter for one input -> moving picture of size, lasting d."""
    w, h = size; cov = f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},setsar=1"
    if kind == "clip":
        avail = dur(src) - ss; f = min(1.0, avail / d)
        if f < 0.7: sys.exit(f"{src.name}: needs {d:.2f}s from {ss}, has {avail:.2f}s")
        pre = f"crop={crop}," if crop else ""
        return f"[{idx}:v]trim=start={ss},setpts=(PTS-STARTPTS)/{f:.4f},{pre}{cov},fps={FPS}{extra}"
    n = int(d * FPS) + 2  # photo: always-moving push-in
    return (f"[{idx}:v]scale={int(w * 1.3)}:{int(h * 1.3)}:force_original_aspect_ratio=increase,crop={int(w * 1.3)}:{int(h * 1.3)},setsar=1,"
            f"zoompan=z='1.0+0.0016*on':x='iw/2-iw/zoom/2+7*sin(on/11)':y='ih/2-ih/zoom/2+5*sin(on/7+1)':d={n}:s={w}x{h}:fps={FPS}{extra}")


def inp(kind, src): return (["-loop", "1", "-i", str(src)] if kind == "photo" else ["-i", str(src)])


def piece(v, d, out):
    k, src, _, o = v; ovs = o.get("ovs", ()); ss = o.get("ss", o.get("ct", 0.0) if o.get("own") else 0.0)
    ovin = sum((["-loop", "1", "-i", str(x)] for x in ovs), [])
    extra = ""
    if o.get("grey"): extra += ",hue=s=0,eq=contrast=1.08:brightness=-0.03"
    if o.get("rev"): extra = ",reverse" + extra
    if o.get("clock"): extra += "," + clock_filter(d)
    if o.get("tin"): extra += "," + TRANS[o["tin"]] + ",setsar=1"
    if k in ("clip", "photo"):
        g = src_chain(k, src, d, 0, ss, o.get("crop"), extra) + "[v0]"
        s, cur = ovchain(ovs); run([*inp(k, src), *ovin, "-filter_complex", g + s, "-map", cur, "-t", f"{d:.3f}", "-an", *ENC, str(out)])
    elif k == "stamp":  # the next shot, blurred and pulling into focus, with the crayon NIGHT stamp (swipe device)
        bk = o.get("bk", "clip")
        g = (src_chain(bk, src, d, 0, ss) + ",split[s0][s1];[s1]gblur=sigma=26,format=rgba,"
             f"fade=t=out:st={max(0.1, d - 0.45):.2f}:d=0.4:alpha=1[s2];[s0][s2]overlay=format=auto[b];"
             f"[1:v]format=rgba,scale=w='trunc(1080*(1.25-0.25*min(1,t/0.18))/2)*2':h=-2:eval=frame[st];"
             f"[b][st]overlay=x='(W-w)/2':y='(H-h)/2':shortest=1[v0]")
        run([*inp(bk, src), "-loop", "1", "-i", str(o["stamp"]), "-filter_complex", g, "-map", "[v0]", "-t", f"{d:.3f}", "-an", *ENC, str(out)])
    elif k == "cardclip":  # real web card over the same scene, blurred and still moving
        bk = o.get("bk", "clip")
        g = (src_chain(bk, o["bg"], d, 0, o.get("bgss", 0.0)) + ",gblur=sigma=24,eq=brightness=-0.1[bg];"
             f"[1:v]format=rgba,scale=w='trunc(min(1000,iw)*(0.94+0.06*{EASE.format(d=0.3)})/2)*2':h=-2:eval=frame[c];"
             f"[bg][c]overlay=x='(W-w)/2':y='(H-h)/2-{o.get('up', 120)}':shortest=1[v0]")
        run([*inp(bk, o["bg"]), "-loop", "1", "-i", str(src), "-filter_complex", g, "-map", "[v0]", "-t", f"{d:.3f}", "-an", *ENC, str(out)])
    elif k == "split":  # top: the real plant; bottom: what it does (swipe device)
        tk, top = o["top"]; bkind, bot = o.get("bkind", "clip"), src
        g = (src_chain(tk, top, d, 0, o.get("tss", 0.0), size=(W, 954)) + "[t];" + src_chain(bkind, bot, d, 1, ss, size=(W, 954)) + "[b];"
             f"[t][b]vstack,pad={W}:{H}:0:6:white,crop={W}:{H}:0:0{(',' + TRANS[o['tin']]) if o.get('tin') else ''}[v0]")
        s, cur = ovchain(ovs, first=2)
        run([*inp(tk, top), *inp(bkind, bot), *ovin, "-filter_complex", g + s, "-map", cur, "-t", f"{d:.3f}", "-an", *ENC, str(out)])
    else:
        sys.exit(k)


# ---------------- the H1 cut, in script order ----------------
# audio: ("vo", line) | ("talk", clip, vo_audio, slot_seconds) | ("silent", seconds)
R = lambda n: RU / n; Gc = lambda n: G / f"{n}.mp4"
STAMP = lambda n: {"stamp": GX / f"stamp_N{n}.png"}
LINES = [
    # 1 hook (H1): product in frame 1, hook title on top (allowed: hook text)
    ("h1", ("talk", Gc("t01"), VO / "v01.mp3", 0), [
        ("clip", Gc("t01"), 5.6, {"ct": 0.0, "ovs": [GX / "hook_title.png"]}),
        ("photo", FR / "W1.png", 0.9, {"ct": 5.85, "ovs": [GX / "glow.png"], "tin": "punch"}),     # "The wart isn't."
        ("clip", Gc("t01"), 2.85, {"ct": 7.55})]),
    # 2 night 1, the routine
    ("n1a", ("vo", "v02"), [("stamp", Gc("i05_calX"), None, STAMP(1))]),
    ("n1b", ("vo", "v03"), [("clip", R("r00_s19_file_kid.mp4"), 2.35, {"ss": 0.6}), ("photo", SP / "flickr_plantar-wart-case3a_happyfeet34.jpg", None, {})]),
    ("n1c", ("vo", "v04"), [("clip", HOWTO, 1.7, {"ss": 2.35, "crop": "540:960:200:120"}), ("clip", R("r02_s19_dot.mp4"), None, {"ss": 0.5})]),
    ("n1d", ("talk", Gc("t06"), None, 0), [
        ("cardclip", GX / "c_night1.png", 1.25, {"ct": 0.0, "bg": Gc("t06")}),                 # "Two minutes."
        ("clip", Gc("t06"), 2.35, {"ct": 1.65}),
        ("clip", Gc("t06"), 1.8, {"ct": 4.5}),
        ("clip", Gc("t06"), 0.85, {"ct": 7.1}),
        ("clip", Gc("t06"), 1.8, {"ct": 8.25})]),
    # 3 night 1, what's happening inside
    ("n1e", ("vo", "v08"), [("split", R("r03_s13_skin_door.mp4"), 2.2, {"top": ("clip", SV / "mixkit_lemon-tree_966.mp4")}),
                            ("clip", R("r03_s13_skin_door.mp4"), None, {"ss": 1.0})]),
    ("n1f", ("vo", "v09"), [("split", R("r03_s13_skin_door.mp4"), 2.25, {"ss": 3.0, "top": ("photo", SP / "flickr_melaleuca-snow-in-summer_tatters.jpg"), "tin": "slide"}),
                            ("clip", R("r19_s1_towels.mp4"), 2.3, {"ss": 0.3, "ovs": [GX / "gauge_8x.png"]}),
                            ("split", R("r05_s13_root_dot.mp4"), 2.6, {"top": ("photo", SP / "flickr_pokeweed-berries_rkramer62.jpg")}),
                            ("clip", SV / "mixkit_watering-small-plant_33422.mp4", None, {"ss": 1.0})]),
    ("n1g", ("vo", "v10"), [("clip", R("r05_s13_root_dot.mp4"), 1.5, {"ss": 3.4, "clock": True}),
                            ("clip", SV / "coverr-touch-lamp-6697.mp4", None, {"ss": 0.0, "rev": True})]),
    # 4 night 3
    ("n3a", ("vo", "v11"), [("stamp", FR / "W3.png", 1.2, {**STAMP(3), "bk": "photo"}), ("photo", FR / "W3.png", 1.1, {}),
                            ("cardclip", GX / "c_dots.png", None, {"bg": FR / "W1.png", "bk": "photo"})]),
    ("n3b", ("talk", Gc("t13"), VO / "v13.mp3", 0), [("clip", Gc("t13"), 1.8, {"ct": 1.65, "tin": "flash"})]),
    ("n3c", ("vo", "v14"), [("clip", R("r06_s1_dand_snap.mp4"), 3.9, {}),
                            ("clip", R("r07_s17_soil_cutaway.mp4"), 2.6, {"ss": 0.2}),
                            ("clip", R("r08_s1_dand_back.mp4"), 1.2, {"ss": 0.4}),
                            ("cardclip", GX / "c_repeat.png", None, {"bg": SV / "mixkit_dandelion-meadow_33321.mp4"})]),
    # 5 night 7
    ("n7a", ("vo", "v16"), [("stamp", FR / "W7.png", 1.2, {**STAMP(7), "bk": "photo"}), ("photo", FR / "W7.png", None, {})]),
    ("n7b", ("vo", "v17"), [("split", R("r04_s17_root3d.mp4"), 2.5, {"top": ("photo", SP / "flickr_thuja-occidentalis_srae.jpg"), "tin": "whip"}),
                            ("clip", R("r04_s17_root3d.mp4"), 2.4, {"ss": 2.5}),
                            ("photo", SP / "flickr_dandelion-roots-hands_isforinsects.jpg", None, {})]),
    ("n7c", ("vo", "v18"), [("clip", Gc("i02_kidbrush"), None, {"ss": 0.4})]),
    # 6 night 10
    ("n10", ("talk", Gc("t19"), VO / "v19.mp3", 0), [
        ("stamp", SV / "mixkit_pool-feet-splashing_1261.mp4", 1.4, {**STAMP(10), "ss": 3.0, "ct": 0.0}),
        ("clip", SV / "mixkit_pool-feet-splashing_1261.mp4", 1.75, {"ss": 4.5, "ct": 1.55}),
        ("clip", Gc("i03_flipflops"), 0.7, {"ct": 3.6, "tin": "dip"}),
        ("clip", Gc("t19"), 1.15, {"ct": 4.3})]),
    # 7 night 14
    ("n14a", ("vo", "v20"), [("stamp", FR / "W14.png", 1.3, {**STAMP(14), "bk": "photo"}), ("photo", FR / "W14.png", None, {})]),
    ("n14b", ("vo", "v21"), [("clip", R("r12_s19_clear_sole.mp4"), 2.4, {"ss": 0.5}), ("clip", GX / "calendar14.mp4", None, {"tin": "zoomout"})]),
    # 8 what it is
    ("w1", ("vo", "v22"), [("clip", Gc("i04_tap"), 2.75, {"ss": 0.3}),
                           ("clip", R("r10_s1_clinic.mp4"), 0.95, {"ss": 2.0, "grey": True, "ovs": [GX / "redx.png"]}),
                           ("clip", R("r11_s1_acid.mp4"), 1.0, {"ss": 2.0, "grey": True, "ovs": [GX / "redx.png"]}),
                           ("clip", R("r13_s19_mason_sole.mp4"), None, {"ss": 0.5, "grey": True, "ovs": [GX / "redx.png"]})]),
    ("w2", ("vo", "v23"), [("clip", R("r14_s20_feetup.mp4"), 2.3, {"ss": 0.8}), ("clip", HOWTO, None, {"ss": 4.75, "crop": "540:960:270:120"})]),
    # 8b three moms (AI testimonials; platform AI label, no on-screen text: L1)
    ("m1", ("talk", Gc("m1"), VO / "v24.mp3", 0), [("clip", Gc("m1"), 2.75, {"ct": 0.0, "tin": "spin"}), ("clip", Gc("m1"), 1.7, {"ct": 3.3}), ("clip", Gc("m1"), 1.95, {"ct": 5.55})]),
    ("m2", ("talk", Gc("m2"), VO / "v25.mp3", 0), [("clip", Gc("m2"), 1.85, {"ct": 0.0}), ("clip", Gc("m2"), 1.9, {"ct": 2.3}), ("clip", Gc("m2"), 2.55, {"ct": 5.05})]),
    ("m3", ("talk", Gc("m3"), VO / "v26.mp3", 0), [("clip", Gc("m3"), 2.8, {"ct": 0.0}), ("clip", Gc("m3"), 1.4, {"ct": 3.35})]),
    # 9 close
    ("cl", ("talk", Gc("t27"), None, 0), [
        ("clip", Gc("t27"), 3.25, {"ct": 0.0}),
        ("clip", Gc("t27"), 1.05, {"ct": 3.95}),
        ("cardclip", GX / "c_tiers.png", 2.1, {"ct": 5.85, "bg": R("r18_s19_three_bottles.mp4"), "up": 40}),   # "Get two, and the third one's free."
        ("clip", R("r09_s17_three_bottles.mp4"), 2.2, {"ss": 1.6, "ct": 8.45}),                                 # "...you get your money back."
        ("clip", Gc("t27"), 1.6, {"ct": 10.85})]),
    ("end", ("silent", 3.2), [("clip", GX / "endcard.mp4", None, {})]),
]
NOCAP = {"end"}; CARDS = {("n1d", 0), ("n3a", 2), ("n3c", 3), ("cl", 2)}   # captions move up over cards
COMBO = {"n1d": [("v06", 0.0), ("v07", None)], "cl": [("v27", 0.0), ("v29", None)]}  # None = after previous + gap
GAPS = {"n1d": 0.35, "cl": 0.4}
LEAD, TAIL = 0.06, 0.16


def first_word(path):
    from faster_whisper import WhisperModel
    import librosa
    global _WM
    try: _WM
    except NameError: _WM = WhisperModel("small.en", device="cpu", compute_type="int8")
    wav = TMP / "_fw.wav"; run(["-i", str(path), "-vn", "-ac", "1", "-ar", "16000", str(wav)])
    y, _ = librosa.load(str(wav), sr=16000); s, _ = _WM.transcribe(y, word_timestamps=True)
    ws = [w for x in s for w in x.words]; return ws[0].start if ws else 0.0


def clip_words(path):
    from faster_whisper import WhisperModel
    import librosa
    global _WM
    try: _WM
    except NameError: _WM = WhisperModel("small.en", device="cpu", compute_type="int8")
    wav = TMP / "_fw.wav"; run(["-i", str(path), "-vn", "-ac", "1", "-ar", "16000", str(wav)])
    y, _ = librosa.load(str(wav), sr=16000); s, _ = _WM.transcribe(y, word_timestamps=True)
    return [(w.word.strip(), w.start, w.end) for x in s for w in x.words]


def talk_audio(name, clip, vo, slot, ss=0.0):
    """Our ElevenLabs line (Helena / the testimonial voice), time-warped word by word onto the clip's own (re-voiced)
    speech, so the lips match and the narrator's voice is identical to the voice-over lines."""
    cache = P / "work/clipwords.json"; cw = json.load(open(cache)) if cache.exists() else {}
    if name not in cw: cw[name] = clip_words(clip); json.dump(cw, open(cache, "w"), indent=1)
    cws = [(w, s - ss, e - ss) for w, s, e in cw[name]]
    lines = [ln for ln, _ in COMBO[name]] if name in COMBO else [vo.stem]
    # one VO track (combo lines joined with their gap) + its word list
    vws, t, ins, segs = [], 0.0, [], []
    for ln in lines:
        segs.append((ln, t)); vws += [(w, s + t, e + t) for w, s, e in WORDS[ln]["words"]]; t += dur(VO / f"{ln}.mp3") + GAPS.get(name, 0)
    src = TMP / f"vo_{name}.wav"
    f = ";".join(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={int(o * 1000)}|{int(o * 1000)},aresample=async=1[x{i}]" for i, (_, o) in enumerate(segs))
    f += ";" + "".join(f"[x{i}]" for i in range(len(segs))) + f"amix=inputs={len(segs)}:normalize=0[a]"
    run(*[sum((["-i", str(VO / f"{ln}.mp3")] for ln in lines), []) + ["-filter_complex", f, "-map", "[a]", str(src)]])
    a = [norm(w) for w, _, _ in vws]; b = [norm(w) for w, _, _ in cws]
    pairs = []  # (vo word index, clip word index)
    for blk in difflib.SequenceMatcher(None, a, b).get_matching_blocks():
        pairs += [(blk.a + k, blk.b + k) for k in range(blk.size)]
    # phrases: break where the clip pauses (> 0.3 s); each VO phrase is stretched onto its clip phrase and placed there
    phr, cur = [], []
    for vi, ci in pairs:
        if cur and cws[ci][1] - cws[cur[-1][1]][2] > 0.3: phr.append(cur); cur = []
        cur.append((vi, ci))
    if cur: phr.append(cur)
    filt, labs = [], []
    for j, ph in enumerate(phr):
        v0, v1 = vws[ph[0][0]][1], vws[ph[-1][0]][2]; c0, c1 = cws[ph[0][1]][1], cws[ph[-1][1]][2]
        v0 = max(0.0, v0 - 0.04); v1 += 0.08; c0 = max(0.0, c0 - 0.04); c1 += 0.08
        r = min(1.35, max(0.74, (v1 - v0) / (c1 - c0)))
        filt.append(f"[0:a]atrim={v0:.3f}:{v1:.3f},asetpts=PTS-STARTPTS,atempo={r:.4f},adelay={int(c0 * 1000)}|{int(c0 * 1000)},aresample=async=1[p{j}]"); labs.append(f"[p{j}]")
    fc = ";".join(filt) + ";" + "".join(labs) + f"amix=inputs={len(labs)}:normalize=0,apad,atrim=0:{slot:.3f}[a]" if len(labs) > 1 else \
         filt[0].replace(f"[p0]", f",apad,atrim=0:{slot:.3f}[a]")
    out = TMP / f"a_{name}.wav"; run(["-i", str(src), "-filter_complex", fc, "-map", "[a]", str(out)])
    # caption timing follows the clip's own words
    return out, [(ln, None) for ln in lines], cws


def build_line(i, name, audio, vis):
    kind = audio[0]
    if kind == "vo":
        src = VO / f"{audio[1]}.mp3"; slot = LEAD + dur(src) + TAIL; segs = [(audio[1], LEAD)]
        a_in, a_f = ["-i", str(src)], f"aresample=48000,aformat=channel_layouts=stereo,adelay={int(LEAD * 1000)}|{int(LEAD * 1000)},aresample=async=1,apad,atrim=0:{slot:.3f}"
    elif kind == "talk":
        full, segs, cws = talk_audio(name, audio[1], audio[2], dur(audio[1]) + 0.5, 0.0)
        for v in vis:
            if v[1] == audio[1]: v[3]["own"] = True
        slot = sum(v[2] for v in vis); cts = [(v[3]["ct"], v[2]) for v in vis]
        a_in = ["-i", str(full)]
        a_f = "asplit=" + str(len(cts)) + "".join(f"[s{j}]" for j in range(len(cts))) + ";" + ";".join(
            f"[s{j}]atrim={c:.3f}:{c + d:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st={max(0, d - 0.03):.3f}:d=0.03[q{j}]" for j, (c, d) in enumerate(cts)) + ";" + "".join(
            f"[q{j}]" for j in range(len(cts))) + f"concat=n={len(cts)}:v=0:a=1"
        segs = [("CLIP", cws, cts)] + segs
    else:
        slot = audio[1]; segs = []; a_in, a_f = ["-f", "lavfi", "-t", str(slot), "-i", "anullsrc=r=48000:cl=stereo"], "anull"
    fixed = sum(v[2] for v in vis if v[2]); free = [v for v in vis if v[2] is None]; rest = slot - fixed
    if kind != "talk" and free and rest < 0.45: sys.exit(f"{name}: fixed {fixed:.2f}s leave {rest:.2f}s in {slot:.2f}s")
    parts, times, t = [], [], 0.0
    for j, v in enumerate(vis):
        d = v[2] or rest / len(free); out = TMP / f"{i:02d}_{name}_{j}.mp4"; piece(v, d, out); parts.append(out); times.append((t, t + d)); t += d
    ins = sum((["-i", str(p)] for p in parts), [])
    vcat = "".join(f"[{j}:v]" for j in range(len(parts))) + f"concat=n={len(parts)}:v=1:a=0[v]"
    out = TMP / f"line_{i:02d}_{name}.mp4"
    run([*ins, *a_in, "-filter_complex", f"{vcat};[{len(parts)}:a]{a_f}[a]", "-map", "[v]", "-map", "[a]", "-t", f"{slot:.3f}",
         *ENC, "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", str(out)])
    return out, slot, segs, times


# ---------------- captions (script text, VO word timings) ----------------
SCRIPT = {k: v[1] for k, v in json.load(open(P / "work/vo_lines.json")).items()}
DISPLAY = {"v09": "The tea tree is a thin oil. It sinks in, up to 8x deeper than a regular cream, and carries the pokeweed and white cedar down with it.",
           "v01": "One brush of this on my son's wart at bedtime. He's asleep in two minutes. The wart isn't. Here's what happened over the next fourteen nights.",
           "v29": "And if it's not gone, you get your money back. That's a 90-day guarantee.",
           "v23": "It's a kids' formula, for ages 4 and up, and pediatricians recommend it.", "v24": "She's four, and I was nervous. No crying, no fuss. She calls it her bedtime paint."}
WORDS = json.load(open(P / "work/vo_words.json"))


def line_tokens(ln):
    """display tokens of the script line with times from the STT words (aligned by difflib, gaps interpolated)."""
    disp = DISPLAY.get(ln, SCRIPT[ln]).split(); ws = WORDS[ln]["words"]
    a = [norm(x) for x in disp]; b = [norm(w[0]) for w in ws]; times = [None] * len(disp)
    for blk in difflib.SequenceMatcher(None, a, b).get_matching_blocks():
        for k in range(blk.size): times[blk.a + k] = (ws[blk.b + k][1], ws[blk.b + k][2])
    for k in range(len(times)):  # interpolate unmatched (e.g. "8x" vs "8 times", "90-day")
        if times[k] is None:
            prev = next((times[j][1] for j in range(k - 1, -1, -1) if times[j]), 0.0)
            nxt = next((times[j][0] for j in range(k + 1, len(times)) if times[j]), prev + 0.3)
            times[k] = (prev, max(prev + 0.1, nxt - 0.02))
    return [(disp[k], *times[k]) for k in range(len(disp))]


def captions(tl, total):
    toks = []
    for x in tl:
        if x["line"] in NOCAP: continue
        if x["segs"] and x["segs"][0][0] == "CLIP":  # talking clip: script words on the clip's own word times
            cws = x["segs"][0][1]; cts = x["segs"][0][2]; disp = sum((DISPLAY.get(ln, SCRIPT[ln]).split() for ln, _ in x["segs"][1:]), [])
            a = [norm(d) for d in disp]; b = [norm(w[0]) for w in cws]; tm = [None] * len(disp)
            for blk in difflib.SequenceMatcher(None, a, b).get_matching_blocks():
                for k in range(blk.size): tm[blk.a + k] = (cws[blk.b + k][1], cws[blk.b + k][2])
            for k in range(len(tm)):
                if tm[k] is None:
                    prev = next((tm[j][1] for j in range(k - 1, -1, -1) if tm[j]), 0.0); tm[k] = (prev, prev + 0.25)
            def lt(t):
                acc = 0.0
                for c, d in cts:
                    if c - 0.05 <= t < c + d: return acc + max(0.0, t - c)
                    acc += d
                return None
            for k, d in enumerate(disp):
                a0 = lt(tm[k][0])
                if a0 is None: continue
                toks.append((d, x["start"] + a0, x["start"] + a0 + (tm[k][1] - tm[k][0]), x["line"]))
            continue
        for ln, off in x["segs"]:
            for w, s, e in line_tokens(ln): toks.append((w, x["start"] + off + s, x["start"] + off + e, x["line"]))
    groups, cur = [], []
    for t in toks:
        if cur and (t[1] - cur[-1][2] > 0.55 or t[3] != cur[-1][3]): groups.append(cur); cur = []
        cur.append(t); end = t[0][-1:] in ".,?!"
        if len(cur) >= 4 or (end and len(cur) >= 2) or (len(cur) >= 3 and sum(len(z[0]) for z in cur) > 18): groups.append(cur); cur = []
    if cur: groups.append(cur)
    up = [(x["start"] + a, x["start"] + b) for x in tl for (j, (a, b)) in enumerate(x["vis"]) if (x["line"], j) in CARDS]
    def ts(v): return f"{int(v // 3600)}:{int(v % 3600 // 60):02d}:{v % 60:05.2f}"
    ass = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 1080", "PlayResY: 1920", "", "[V4+ Styles]",
           "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
           "Style: Cap,Inter,64,&H00141414,&H00141414,&H00FFFFFF,&H00FFFFFF,-1,0,0,0,100,100,0,0,3,16,0,2,90,90,640,1",
           "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
    for j, g in enumerate(groups):
        s = g[0][1]; e = min(groups[j + 1][0][1] - 0.02, g[-1][2] + 0.35) if j + 1 < len(groups) else g[-1][2] + 0.3
        txt = " ".join(z[0] for z in g).rstrip(",")
        txt = re.sub(r"\bRootOut\b", r"{\\c&HB86317&}RootOut{\\c&H141414&}", txt)
        mv = 260 if any(a <= s < b for a, b in up) else 0
        ass.append(f"Dialogue: 0,{ts(s)},{ts(min(e, total - 3.25))},Cap,,0,0,{640 - mv if mv else 0},,{txt}")
    (P / "work/captions.ass").write_text("\n".join(ass) + "\n"); return len(groups)


def hook_title():
    from PIL import Image, ImageDraw, ImageFont
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im); f = ImageFont.truetype(FONT, 66)
    a, b = "14 nights ", "at bedtime"; wa, wb = d.textlength(a, font=f), d.textlength(b, font=f); x = (W - wa - wb) / 2
    d.rounded_rectangle((x - 34, 220, x + wa + wb + 34, 330), 22, fill=(255, 255, 255, 245))
    d.text((x, 275), a, font=f, fill=(23, 99, 184), anchor="lm"); d.text((x + wa, 275), b, font=f, fill=(11, 42, 91), anchor="lm")
    im.save(GX / "hook_title.png")


if __name__ == "__main__":
    hook_title(); only = set(sys.argv[1:]); outs, tl, t = [], [], 0.0
    cache = json.load(open(TMP / "timeline.json")) if (TMP / "timeline.json").exists() else []
    cmap = {x["line"]: x for x in cache}
    for i, (name, audio, vis) in enumerate(LINES):
        out = TMP / f"line_{i:02d}_{name}.mp4"
        if only and name not in only and out.exists() and name in cmap:
            d, segs, times = dur(out), cmap[name]["segs"], cmap[name]["vis"]
        else:
            out, d, segs, times = build_line(i, name, audio, vis)
        tl.append({"line": name, "start": round(t, 3), "dur": round(d, 3), "segs": segs, "vis": times}); outs.append(out); t += d
        print(f"{name:5s} {t - d:7.2f} +{d:5.2f}  shots {len(vis)}")
    json.dump(tl, open(TMP / "timeline.json", "w"), indent=1)
    (TMP / "list.txt").write_text("".join(f"file '{o}'\n" for o in outs))
    cat = TMP / "cut.mp4"; run(["-f", "concat", "-safe", "0", "-i", str(TMP / "list.txt"), "-c", "copy", str(cat)])
    D = dur(cat); n = captions(tl, D)
    MUS = P / "assets/music/Dreamer.mp3"
    fc = (f"[1:a]atrim=0:{D:.2f},volume=0.20,afade=t=in:d=1.2,afade=t=out:st={D - 2.5:.2f}:d=2.5[m];"
          f"anoisesrc=c=pink:a=0.004:d={D:.2f},lowpass=f=1800[rt];"
          f"[0:a]asplit[vo][sc];[m][sc]sidechaincompress=threshold=0.03:ratio=5:attack=20:release=450[md];"
          f"[vo][md][rt]amix=inputs=3:normalize=0,loudnorm=I=-14:TP=-2:LRA=9[a];"
          f"[0:v]ass={P / 'work/captions.ass'},noise=alls=4:allf=t,vignette=PI/5,unsharp=5:5:0.25[v]")
    final = OUTD / "WilloMD_RootOut_Set5_H1_9x16_v2.mp4"
    run(["-i", str(cat), "-i", str(MUS), "-filter_complex", fc, "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "19",
         "-maxrate", "10M", "-bufsize", "20M", "-preset", "slow", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
         "-map_metadata", "-1", "-movflags", "+faststart", str(final)])
    print("H1", round(dur(final), 2), "s,", sum(len(v) for _, _, v in LINES), "shots,", n, "caption cards ->", final)
