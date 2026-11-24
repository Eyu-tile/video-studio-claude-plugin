#!/usr/bin/env python3
"""Set 5 H1 v4 — client workflow (24 Nov): mom = Higgsfield Soul base -> GPT Image 2.6 scene edits -> Seedance 2.5 720p,
no Sync. Her on-camera shots play their own Seedance audio (her native voice, untouched); her off-camera lines are
Seed Audio 1.0 reads with her voice-lock clip as the voice reference, so VO and on-camera are the same voice.
Testimonial moms: their own Seedance voices. Each section's audio = its blocks (VO takes / talking clips) back to back,
trimmed to speech; talking shots cut from the same clip at the same time as their audio.
- Every shot starts on the word it illustrates (anchors in the take's word timings).
- Smoothness: 24 fps end to end (the sources are 24), straight cuts (only the NIGHT stamps blur in), stills rendered at
  2x then a single linear push-in (no jitter), slowed clips frame-blended, no jump cuts inside talking shots.
Usage: build7.py  -> out/WilloMD_RootOut_Set5_H1_9x16_v5.mp4"""
import json, re, subprocess, sys, difflib
from pathlib import Path

P = Path("/home/user/video-studio-claude-plugin/video-studio/projects/rootout-set5")
L = Path("/home/user/video-studio-claude-plugin/video-studio/library/RootOut")
G, RU, VO, VO3, GX, FR, LS = P / "raw/gen", P / "raw/reuse", P / "raw/vo", P / "raw/vo3", P / "assets/graphics", P / "raw/frames", P / "raw/ls"
SV, SP = L / "stock/assets/set5/video", L / "stock/assets/set5/photo"
HOWTO = L / "resources/site_videos/shopify-ff701bf4.mp4"
TMP = P / "work/v4"; TMP.mkdir(parents=True, exist_ok=True)
W, H, FPS = 1080, 1920, 24
ENC = ["-c:v", "libx264", "-crf", "16", "-preset", "medium", "-pix_fmt", "yuv420p", "-r", str(FPS)]
FONT = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
COVER = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1"
norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())
V4 = P / "raw/v4"
VOC = P / "work/clone/pick"   # VO in her own voice: Seed Audio 1.0 with her Seedance voice-lock clip as the reference
MUSIC = 0.11            # music bed level (v4 was 0.20; client: too loud)
SCRIPT = {k: v[1] for k, v in json.load(open(P / "work/vo_lines.json")).items()}


def dur(f): return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)]))


def run(a):
    r = subprocess.run(["ffmpeg", "-y", "-v", "error", *a], capture_output=True, text=True)
    if r.returncode: sys.exit(r.stderr[-3000:])


def clock_filter(d, m0=21 * 60, m1=31 * 60):
    M = f"({m0}+{m1 - m0}*t/{d:.3f})"; hh = f"mod(floor({M}/60)\\,24)"; h12 = f"(mod({hh}+11\\,12)+1)"; mm = f"mod(floor({M})\\,60)"
    return (f"drawbox=x=700:y=150:w=320:h=120:color=black@0.45:t=fill,"
            f"drawtext=fontfile={FONT}:fontsize=72:fontcolor=white:x=730:y=172:text='%{{eif\\:{h12}\\:d}}\\:%{{eif\\:{mm}\\:d\\:2}}',"
            f"drawtext=fontfile={FONT}:fontsize=40:fontcolor=white:x=935:y=200:text='PM':enable='lt({M}\\,1440)',"
            f"drawtext=fontfile={FONT}:fontsize=40:fontcolor=white:x=935:y=200:text='AM':enable='gte({M}\\,1440)'")


def chain(kind, src, d, idx, ss=0.0, crop=None, size=(W, H), extra=""):
    w, h = size; cov = f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},setsar=1"
    if kind == "clip":
        avail = dur(src) - ss; f = min(1.0, avail / d)
        if f < 0.75: sys.exit(f"{src.name}: needs {d:.2f}s from {ss:.2f}, has {avail:.2f}s")
        pre = f"crop={crop}," if crop else ""
        rate = f"minterpolate=fps={FPS}:mi_mode=blend" if f < 0.97 else f"fps={FPS}"   # slowed shots: blend, never repeat
        return f"[{idx}:v]trim=start={ss:.3f},setpts=(PTS-STARTPTS)/{f:.4f},{rate},{pre}{cov}{extra}"
    n = int(d * FPS) + 2  # still: render big, then one smooth linear push-in
    return (f"[{idx}:v]scale={w * 2}:{h * 2}:force_original_aspect_ratio=increase,crop={w * 2}:{h * 2},setsar=1,"
            f"zoompan=z='1+0.05*on/{n}':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d={n}:s={w}x{h}:fps={FPS}{extra}")


def inp(kind, src): return ["-loop", "1", "-i", str(src)] if kind == "photo" else ["-i", str(src)]


def piece(k, src, d, o, out):
    ovs = o.get("ovs", ()); ss = o.get("ss", 0.0); ovin = sum((["-loop", "1", "-i", str(x)] for x in ovs), [])
    extra = ""
    if o.get("grey"): extra += ",hue=s=0,eq=contrast=1.08:brightness=-0.03"
    if o.get("rev"): extra = ",reverse" + extra
    if o.get("clock"): extra += "," + clock_filter(d)
    def ovc(first, base="[v0]"):
        s, cur = "", base
        for i, _ in enumerate(ovs): s += f";{cur}[{i + first}:v]overlay=0:0[o{i}]"; cur = f"[o{i}]"
        return s, cur
    if k in ("clip", "photo"):
        g = chain(k, src, d, 0, ss, o.get("crop"), extra=extra) + "[v0]"; s, cur = ovc(1)
        run([*inp(k, src), *ovin, "-filter_complex", g + s, "-map", cur, "-t", f"{d:.3f}", "-an", *ENC, str(out)])
    elif k == "stamp":  # next shot blurred, easing into focus under the crayon NIGHT stamp (gentle, no pop)
        bk = o.get("bk", "clip")
        g = (chain(bk, src, d, 0, ss) + ",split[s0][s1];[s1]gblur=sigma=22,format=rgba,"
             f"fade=t=out:st={max(0.1, d - 0.6):.2f}:d=0.55:alpha=1[s2];[s0][s2]overlay=format=auto[b];"
             f"[1:v]format=rgba,fade=t=in:st=0:d=0.25:alpha=1[st];[b][st]overlay=0:0:shortest=1[v0]")
        run([*inp(bk, src), "-loop", "1", "-i", str(o["stamp"]), "-filter_complex", g, "-map", "[v0]", "-t", f"{d:.3f}", "-an", *ENC, str(out)])
    elif k == "cardclip":
        bk = o.get("bk", "clip")
        g = (chain(bk, o["bg"], d, 0, o.get("bgss", 0.0)) + ",gblur=sigma=24,eq=brightness=-0.1[bg];"
             f"[1:v]format=rgba,fade=t=in:st=0:d=0.2:alpha=1[c];[bg][c]overlay=x='(W-w)/2':y='(H-h)/2-{o.get('up', 120)}':shortest=1[v0]")
        run([*inp(bk, o["bg"]), "-loop", "1", "-i", str(src), "-filter_complex", g, "-map", "[v0]", "-t", f"{d:.3f}", "-an", *ENC, str(out)])
    elif k == "split":
        tk, top = o["top"]
        g = (chain(tk, top, d, 0, o.get("tss", 0.0), size=(W, 954)) + "[t];" + chain("clip", src, d, 1, ss, size=(W, 954)) + "[b];"
             f"[t][b]vstack,pad={W}:{H}:0:6:white,crop={W}:{H}:0:0[v0]")
        s, cur = ovc(2)
        run([*inp(tk, top), "-i", str(src), *ovin, "-filter_complex", g + s, "-map", cur, "-t", f"{d:.3f}", "-an", *ENC, str(out)])
    else:
        sys.exit(k)


# ---------------- sections: one voice take each; shots start on their words ----------------
Gc = lambda n: G / f"{n}.mp4"; R = lambda n: RU / n
ST = lambda n: {"stamp": GX / f"stamp_N{n}.png"}
# anchor: 0 = section start | ("word", occurrence[, words_back]) | "END" = end of the take (tail shots)
SECTIONS = [
    ("h1", "h1", 0.25, [
        (0, "talk", "E1", {"ovs": [GX / "hook_title.png"]}),
        (("The", 0), "photo", FR / "W1.png", {"ovs": [GX / "glow.png"]}),
        (("Here's", 0), "talk", "E1", {})]),
    ("n1", "n1", 0.9, [
        (0, "stamp", Gc("i05_calX"), ST(1)),
        (("Two", 0), "clip", R("r00_s19_file_kid.mp4"), {"ss": 0.6}),
        (("just", 0), "photo", SP / "flickr_plantar-wart-case3a_happyfeet34.jpg", {}),
        (("Brush", 0), "clip", HOWTO, {"ss": 2.35, "crop": "540:960:200:120"}),
        (("a", 0), "clip", R("r02_s19_dot.mp4"), {"ss": 0.5}),
        (("Two", 1), "cardclip", GX / "c_night1.png", {"bg": "N1T", "bgss": 0.0}),
        (("He", 0), "talk", "N1T", {}),
        (("lemon", 0, 1), "split", R("r03_s13_skin_door.mp4"), {"top": ("clip", SV / "mixkit_lemon-tree_966.mp4")}),
        (("so", 0), "clip", R("r03_s13_skin_door.mp4"), {"ss": 1.1}),
        (("tea", 0, 1), "split", R("r03_s13_skin_door.mp4"), {"ss": 2.6, "top": ("photo", SP / "flickr_melaleuca-snow-in-summer_tatters.jpg")}),
        (("sinks", 0, 1), "clip", R("r19_s1_towels.mp4"), {"ss": 0.3, "ovs": [GX / "gauge_8x.png"]}),
        (("carries", 0, 1), "split", R("r05_s13_root_dot.mp4"), {"top": ("photo", SP / "flickr_pokeweed-berries_rkramer62.jpg")}),
        (("dot", 1, 1), "clip", R("r05_s13_root_dot.mp4"), {"ss": 2.5, "clock": True}),
        ("END", "clip", SV / "coverr-touch-lamp-6697.mp4", {"rev": True})]),
    ("n3", "n3", 1.5, [
        (0, "stamp", FR / "W3.png", {**ST(3), "bk": "photo"}),
        (("little", 0, 1), "photo", FR / "W3.png", {}),
        (("are", 0), "cardclip", GX / "c_dots.png", {"bg": FR / "W1.png", "bk": "photo"}),
        (("That's", 0), "talk", "E3", {}),
        (("Freezing", 0), "clip", R("r16_s19_wart_back.mp4"), {"grey": True}),   # v5: the fixes, greyed (swipe grammar)
        (("snap", 0), "clip", R("r06_s1_dand_snap.mp4"), {}),
        (("like", 0), "clip", SV / "mixkit_dandelion-closeup_45332.mp4", {}),   # v5: slower VO needs a 2nd shot here
        (("root", 0, 1), "clip", R("r07_s17_soil_cutaway.mp4"), {"ss": 0.2}),
        (("so", 0), "clip", R("r08_s1_dand_back.mp4"), {"ss": 0.4}),
        ("END", "cardclip", GX / "c_repeat.png", {"bg": SV / "mixkit_dandelion-meadow_33321.mp4"})]),
    ("n7", "n7", 0.25, [
        (0, "stamp", FR / "W7.png", {**ST(7), "bk": "photo"}),
        (("It's", 0), "photo", FR / "W7.png", {}),
        (("Pokeweed", 0), "split", R("r04_s17_root3d.mp4"), {"top": ("photo", SP / "flickr_thuja-occidentalis_srae.jpg")}),
        (("breaking", 0), "clip", R("r04_s17_root3d.mp4"), {"ss": 2.4}),
        (("so", 0), "photo", SP / "flickr_dandelion-roots-hands_isforinsects.jpg", {}),
        (("And", 1), "clip", Gc("i02_kidbrush"), {"ss": 0.3})]),
    ("n10", "n10", 0.25, [
        (0, "stamp", SV / "mixkit_pool-feet-splashing_1261.mp4", {**ST(10), "ss": 3.0}),
        (("He", 0), "clip", SV / "mixkit_pool-feet-splashing_1261.mp4", {"ss": 4.6}),
        (("I", 0), "clip", Gc("i03_flipflops"), {}),
        (("on", 0), "talk", "E4", {})]),
    ("n14", "n14", 0.25, [
        (0, "stamp", FR / "W14.png", {**ST(14), "bk": "photo"}),
        (("It's", 0), "photo", FR / "W14.png", {}),
        (("Most", 0), "clip", R("r12_s19_clear_sole.mp4"), {"ss": 0.4}),
        (("But", 0), "clip", GX / "calendar14.mp4", {}),
        (("One", 0), "clip", Gc("i04_tap"), {"ss": 0.3}),
        (("No", 0), "clip", R("r10_s1_clinic.mp4"), {"ss": 2.0, "grey": True, "ovs": [GX / "redx.png"]}),
        (("no", 1), "clip", R("r11_s1_acid.mp4"), {"ss": 2.0, "grey": True, "ovs": [GX / "redx.png"]}),
        (("no", 2), "clip", R("r13_s19_mason_sole.mp4"), {"ss": 0.5, "grey": True, "ovs": [GX / "redx.png"]}),
        (("It's", 1), "clip", R("r14_s20_feetup.mp4"), {"ss": 0.6}),
        (("pediatricians", 0, 1), "clip", HOWTO, {"ss": 4.75, "crop": "540:960:270:120"})]),
    ("m1", "m1", 0.2, [(0, "talk", "M1", {})]),
    ("m2", "m2", 0.2, [(0, "talk", "M2", {})]),
    ("m3", "m3", 0.25, [(0, "talk", "M3", {})]),
    ("cl", "cl", 0.2, [
        (0, "talk", "E5", {}),
        (("Get", 0), "cardclip", GX / "c_tiers.png", {"bg": R("r18_s19_three_bottles.mp4"), "up": 40}),
        (("And", 1), "clip", R("r09_s17_three_bottles.mp4"), {"ss": 1.6}),
        (("That's", 0), "talk", "E5", {})]),
]


# ---------------- audio blocks: each section = its blocks back to back (VO takes in the S7 voice / talking clips) -------
# block key -> (file, script lines, is_talking_clip)
BLK = {
    "E1": (V4 / "E1_hook.mp4", ["v01"], True),
    "N1a": (VOC / "N1a.wav", ["v02", "v03", "v04"], False),
    "N1T": (V4 / "c_n1.mp4", ["v06", "v07"], True),
    "N1b": (VOC / "N1b.wav", ["v08", "v09", "v10"], False),
    "N3a": (VOC / "N3a.wav", ["v11"], False),
    "E3": (V4 / "E3_n3.mp4", ["v13"], True),
    "N3b": (VOC / "N3b.wav", ["v14"], False),
    "N7": (VOC / "N7.wav", ["v16", "v17", "v18"], False),
    "E4": (V4 / "E4_car.mp4", ["v19"], True),
    "N14": (VOC / "N14.wav", ["v20", "v21", "v22", "v23"], False),
    "M1": (V4 / "m1.mp4", ["v24"], True),
    "M2": (V4 / "m2.mp4", ["v25"], True),
    "M3": (V4 / "m3.mp4", ["v26"], True),
    "E5": (V4 / "E5_close.mp4", ["v27", "v29"], True),
}
TAKES = {"h1": ["E1"], "n1": ["N1a", "N1T", "N1b"], "n3": ["N3a", "E3", "N3b"], "n7": ["N7"], "n10": ["E4"],
         "n14": ["N14"], "m1": ["M1"], "m2": ["M2"], "m3": ["M3"], "cl": ["E5"]}
GAP = 0.18   # breath between blocks inside a section
WJ = P / "work/v4_words.json"


def block_words():
    """Word timings per block (whisper medium.en, cached). Times are in the block file's own clock."""
    cache = json.load(open(WJ)) if WJ.exists() else {}
    todo = [k for k in BLK if k not in cache or cache[k]["mtime"] != BLK[k][0].stat().st_mtime]
    if todo:
        from faster_whisper import WhisperModel
        import librosa, numpy as np
        m = WhisperModel("medium.en", device="cpu", compute_type="int8")
        for k in todo:
            f = BLK[k][0]; wav = TMP / f"_{k}.wav"; run(["-i", str(f), "-ac", "1", "-ar", "16000", str(wav)])
            y, _ = librosa.load(str(wav), sr=16000); pad = 0.5
            segs, _ = m.transcribe(np.concatenate([np.zeros(int(pad * 16000), dtype=y.dtype), y]), word_timestamps=True,
                                   initial_prompt="RootOut, pokeweed, white cedar, tea tree, plantar wart, the root, pediatricians")
            ws = [[w.word.strip(), round(max(0.0, w.start - pad), 3), round(w.end - pad, 3)] for sg in segs for w in sg.words]
            cache[k] = {"mtime": f.stat().st_mtime, "dur": dur(f), "words": ws}; print("words", k, len(ws))
        json.dump(cache, open(WJ, "w"), indent=1)
    return cache


BW = block_words()


def take(name):
    """Section audio: blocks trimmed to speech, joined with short gaps. Returns (wav, dur, words, block offsets)."""
    parts, words, offs, t = [], [], {}, 0.0
    for k in TAKES[name]:
        f, _, talk = BLK[k]; ws = BW[k]["words"]
        a = max(0.0, ws[0][1] - 0.12); b = min(BW[k]["dur"], ws[-1][2] + 0.22)
        offs[k] = (t, a, b)   # block k occupies section time [t, t+b-a); file time = section time - t + a
        words += [(w, round(s - a + t, 3), round(e - a + t, 3), k) for w, s, e in ws]
        parts.append((f, a, b)); t += (b - a) + GAP
    t -= GAP; wav = TMP / f"take_{name}.wav"
    ins = sum((["-i", str(f)] for f, _, _ in parts), [])
    fc = "".join(f"[{i}:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo"
                 + (f",apad=pad_dur={GAP}" if i < len(parts) - 1 else "") + f"[a{i}];" for i, (_, a, b) in enumerate(parts))
    fc += "".join(f"[a{i}]" for i in range(len(parts))) + f"concat=n={len(parts)}:v=0:a=1[a]"
    run([*ins, "-filter_complex", fc, "-map", "[a]", str(wav)])
    return wav, t, words, offs

def anchor_time(words, a, total):
    if a == 0: return 0.0
    if a == "END": return total
    w, occ = a[0], a[1]; back = a[2] if len(a) > 2 else 0
    idx = [i for i, x in enumerate(words) if norm(x[0]) == norm(w)]
    if occ >= len(idx): sys.exit(f"anchor {a} not found")
    i = max(0, idx[occ] - back); return max(0.0, words[i][1] - 0.06)


def build_section(si, sec):
    name, tk, tail, items = sec; af, tdur, words, offs = take(tk); total = tdur + tail
    if items[-1][1] == "talk":  # a section that ends on a talking shot can't run past the end of that clip
        bt, ba, _ = offs[items[-1][2]]; total = min(total, bt + dur(BLK[items[-1][2]][0]) - ba - 0.05)
    starts = [anchor_time(words, it[0], tdur) for it in items]
    if any(b <= a + 0.3 for a, b in zip(starts, starts[1:])): sys.exit(f"{name}: shots too close {starts}")
    parts = []
    for j, (it, t0) in enumerate(zip(items, starts)):
        t1 = starts[j + 1] if j + 1 < len(items) else total
        _, k, src, o = it; o = dict(o); d = t1 - t0
        if isinstance(o.get("bg"), str): bt, ba, _ = offs[o["bg"]]; o["bgss"] = max(0.0, t0 - bt + ba); o["bg"] = BLK[o["bg"]][0]
        if k == "talk":  # the clip whose own audio is playing: picture time == audio time
            bt, ba, bb = offs[src]; src = BLK[src][0]; k = "clip"; o["ss"] = max(0.0, t0 - bt + ba)
            if dur(src) - o["ss"] < d - 0.02: sys.exit(f"{name}: talk shot {j} runs past {src.name} ({o['ss']:.2f}+{d:.2f} > {dur(src):.2f})")
        out = TMP / f"{si:02d}_{name}_{j}.mp4"; piece(k, src, d, o, out); parts.append(out)
    ins = sum((["-i", str(p)] for p in parts), [])
    vc = "".join(f"[{j}:v]" for j in range(len(parts))) + f"concat=n={len(parts)}:v=1:a=0[v]"
    out = TMP / f"sec_{si:02d}_{name}.mp4"
    run([*ins, "-i", str(af), "-filter_complex", f"{vc};[{len(parts)}:a]aresample=48000,aformat=channel_layouts=stereo,apad,atrim=0:{total:.3f}[a]",
         "-map", "[v]", "-map", "[a]", "-t", f"{total:.3f}", *ENC, "-c:a", "aac", "-b:a", "192k", str(out)])
    return out, total, words, starts


DISPLAY = {"v09": "The tea tree is a thin oil. It sinks in, up to 8x deeper than a regular cream, and carries the pokeweed and white cedar down with it.",
           "v29": "And if it's not gone, you get your money back. That's a 90-day guarantee.",
           "v23": "It's a kids' formula, for ages 4 and up, and pediatricians recommend it."}


def captions(tl, D):
    toks = []
    for x in tl:
        lines = sum((BLK[k][1] for k in TAKES[x["take"]]), [])
        disp = sum((DISPLAY.get(l, SCRIPT[l]).split() for l in lines), []); ws = x["words"]
        a = [norm(d) for d in disp]; b = [norm(w[0]) for w in ws]; tm = [None] * len(disp)
        for blk in difflib.SequenceMatcher(None, a, b).get_matching_blocks():
            for k in range(blk.size): tm[blk.a + k] = (ws[blk.b + k][1], ws[blk.b + k][2])
        for k in range(len(tm)):
            if tm[k] is None:
                prev = next((tm[j][1] for j in range(k - 1, -1, -1) if tm[j]), 0.0)
                nxt = next((tm[j][0] for j in range(k + 1, len(tm)) if tm[j]), prev + 0.3); tm[k] = (prev, max(prev + 0.1, nxt - 0.02))
        toks += [(d, x["start"] + tm[k][0], x["start"] + tm[k][1], x["sec"]) for k, d in enumerate(disp)]
    groups, cur = [], []
    for t in toks:
        if cur and (t[1] - cur[-1][2] > 0.45 or t[3] != cur[-1][3]): groups.append(cur); cur = []
        cur.append(t)
        if len(cur) >= 4 or (t[0][-1:] in ".,?!" and len(cur) >= 2) or (len(cur) >= 3 and sum(len(z[0]) for z in cur) > 18): groups.append(cur); cur = []
    if cur: groups.append(cur)
    def ts(v): return f"{int(v // 3600)}:{int(v % 3600 // 60):02d}:{v % 60:05.2f}"
    ass = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 1080", "PlayResY: 1920", "", "[V4+ Styles]",
           "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
           "Style: Cap,Inter,64,&H00141414,&H00141414,&H00FFFFFF,&H00FFFFFF,-1,0,0,0,100,100,0,0,3,16,0,2,90,90,640,1",
           "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
    for j, g in enumerate(groups):
        s = g[0][1]; e = min(groups[j + 1][0][1] - 0.02, g[-1][2] + 0.4) if j + 1 < len(groups) else g[-1][2] + 0.3
        txt = re.sub(r"\bRootOut\b", r"{\\c&HB86317&}RootOut{\\c&H141414&}", " ".join(z[0] for z in g).rstrip(","))
        ass.append(f"Dialogue: 0,{ts(s)},{ts(min(e, D - 3.25))},Cap,,0,0,0,,{txt}")
    (TMP / "captions.ass").write_text("\n".join(ass) + "\n"); return len(groups)


if __name__ == "__main__":
    outs, tl, t = [], [], 0.0
    for si, sec in enumerate(SECTIONS):
        out, d, words, starts = build_section(si, sec)
        tl.append({"sec": sec[0], "take": sec[1], "start": round(t, 3), "dur": round(d, 3), "words": [list(w) for w in words], "shots": [round(x, 2) for x in starts]})
        outs.append(out); t += d; print(f"{sec[0]:4s} {t - d:7.2f} +{d:6.2f}  shots {len(starts)}")
    end = TMP / "sec_99_end.mp4"
    run(["-i", str(GX / "endcard.mp4"), "-f", "lavfi", "-t", "3.2", "-i", "anullsrc=r=48000:cl=stereo", "-vf", f"fps={FPS}", "-t", "3.2", *ENC, "-c:a", "aac", "-b:a", "192k", "-shortest", str(end)])
    outs.append(end); json.dump(tl, open(TMP / "timeline.json", "w"), indent=1)
    (TMP / "list.txt").write_text("".join(f"file '{o}'\n" for o in outs))
    cat = TMP / "cut.mp4"; run(["-f", "concat", "-safe", "0", "-i", str(TMP / "list.txt"), "-c", "copy", str(cat)])
    D = dur(cat); n = captions(tl, D)
    fc = (f"[1:a]atrim=0:{D:.2f},volume={MUSIC},afade=t=in:d=1.2,afade=t=out:st={D - 2.5:.2f}:d=2.5[m];"
          f"[0:a]asplit[vo][sc];[m][sc]sidechaincompress=threshold=0.03:ratio=5:attack=20:release=450[md];"
          f"[vo][md]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-2:LRA=9[a];"   # no SFX / room tone (client note, Set 18)
          f"[0:v]ass={TMP / 'captions.ass'},noise=alls=3:allf=t,vignette=PI/5[v]")
    final = P / "out/WilloMD_RootOut_Set5_H1_9x16_v5.mp4"
    run(["-i", str(cat), "-i", str(P / "assets/music/Dreamer.mp3"), "-filter_complex", fc, "-map", "[v]", "-map", "[a]", "-r", str(FPS),
         "-c:v", "libx264", "-crf", "18", "-maxrate", "10M", "-bufsize", "20M", "-preset", "slow", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-map_metadata", "-1", "-movflags", "+faststart", str(final)])
    shots = sum(len(s[3]) for s in SECTIONS) + 1
    print("H1 v5", round(dur(final), 2), "s,", shots, "shots,", n, "caption cards ->", final)
