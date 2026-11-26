#!/usr/bin/env python3
"""RootOut Set 2 · real cut builder (voice-timed).

Units run in script order. A unit is either a cloned narrator VO line (vo/<id>.wav, Seed Audio) covered by b-roll
shots that start on a given word, or an on-camera take (its own picture + voice). Cuts land on the voice's word
timings (vs transcribe JSON). Long pauses inside VO lines are tightened (max gap 0.30 s). Captions: word by word,
active word highlighted (L5). Music: "Life of Riley", Kevin MacLeod (incompetech.com), CC BY 4.0, ducked under the
voice and lifted where nobody speaks, short fade on the last frame only (L6). Voice + music only (L7).

Usage: HOOK=H1|H2|H3 PREVIEW=1 python3 -I build_v1.py
"""
import json, os, re, subprocess, pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3] / "projects" / "rootout-set2"
RAW, WORK, OUT = ROOT / "raw", ROOT / "work" / "v1", ROOT / "out"
WORK.mkdir(parents=True, exist_ok=True); OUT.mkdir(parents=True, exist_ok=True)
HOOK = os.environ.get("HOOK", "H1"); PREVIEW = os.environ.get("PREVIEW", "1") == "1"
W, H = (720, 1280) if PREVIEW else (1080, 1920)
FPS, SR = 30, 48000
GAP_UNIT, MAX_GAP, MIN_SPEED = 0.22, 0.30, 0.75
BOLD = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
MUSIC = RAW / "music" / "Life_of_Riley.mp3"

R, N, ST, TK = "reuse", "new", "still", "take"   # source kinds
def r(name, inp=0.0): return (R, name, inp)
def n(name, inp=0.0): return (N, name, inp)
def s(name): return (ST, name, 0.0)

HOOKS = {
 "H1": [("vo", "v01", [("we", n("V01_three_socks"))]), ("vo", "v03", [("a", r("s4_P1_lineup"))])],
 "H2": [("vo", "h2a", [("ten", r("s19_shelf_sweep"))]), ("vo", "h2b", [("so", n("V01_three_socks"))])],
 "H3": [("vo", "h3a", [("your", r("s19_wart_back"))]), ("vo", "h3b", [("so", n("V01_three_socks"))])],
}
HOOK_TITLE = {"H1": "3 kids. 3 wart fixes. 2 weeks.", "H2": "10 boxes. 1 wart.", "H3": "It always seems to come back."}
# In H3 the wart-back clip opens the ad, so the two-weeks beat uses the pad clip instead (each source once, L4).
WART_BACK = r("s4_B10_threewarts") if HOOK == "H3" else r("s19_wart_back")

BODY = [
 ("take", "takes/T1_row2.mp4", (0.0, 5.75)),
 ("vo", "v05", [("here's", r("s5_calX"))]),
 ("vo", "v06", [("night", n("V06_blue_freeze")), ("got", r("s4_B7_vapour")), ("he", r("s4_B8_holdankle"))]),
 ("vo", "v08", [("kid", s("s2_s08_yellow_pad"))]),
 ("vo", "v09", [("kid", n("V09_green_bed")), ("she", r("s20_feet_up"))]),
 ("vo", "v11", [("week", s("s2_s11a_blue_blister")), ("the", r("s19_mason_sole"))]),
 ("vo", "v12", [("kid", s("s2_s12_yellow_sock_pad"))]),
 ("vo", "v13", [("kid", s("s2_s13_green_dot"))]),
 ("vo", "v14", [("two", WART_BACK), ("kid#2", r("s4_B6_padpress")), ("kid#3", s("s2_s16_green_smooth"))]),
 ("take", "new/T18_why.mp4", (0.0, 2.5)),
 ("vo", "v19", [("freezing", r("s4_D2_toponly")), ("like", r("s1_dand_snap", 0.5)), ("the", r("s4_D3_rootstill")), ("so", r("s1_dand_back"))]),
 ("vo", "v23", [("kid", r("s4_P2_slidein")), ("it's", r("s4_P4_flatlay")), ("the", r("s4_B14_lemon")), ("so", r("s4_D4_lemon3d", 1.0))]),
 ("vo", "v25", [("the", r("s4_D5_sink")), ("up", r("s1_towels")), ("and", r("s4_D6_carry"))]),
 ("vo", "v28", [("then", r("s4_D7_crumble")), ("so", r("s17_x6_root", 2.5)), ("one", r("s4_D8_together")), ("and", r("s4_D9_clean"))]),
 ("vo", "v31", [("deep", r("s4_P5_nightbook")), ("it's", r("s20_socks_bed")), ("no", r("s4_B17_bin")), ("just", r("s17_b2_routine", 2.0)),
                ("recommended", r("s4_P3_hero"))]),
 ("take", "new/T35_mom2.mp4", [(0.0, 2.2), (3.6, 6.9)]),
 ("vo", "v36", [("here's", n("V36_green_bedtime")), ("two", r("s20_file_kid")), ("then", n("V38_brush"))]),
 ("vo", "v39", [("the", r("s4_B13_thumbrub")), ("never", r("s19_dot_v2"))]),
 ("take", "new/T41_mom1.mp4", (0.0, 6.95)),
 ("vo", "v42", [("when", r("s19_clear_sole")), ("keep", r("s4_B20_plus14"))]),
 ("take", "new/T43_mom3.mp4", [(0.0, 3.85), (4.3, 6.9)]),
 ("vo", "v44", [("warts", r("s19_splash_v2")), ("every", n("V45_checkout"))]),
 ("take", "new/T46_close.mp4", (0.0, 9.4)),
]
END_CARD_S = 3.0
CHIPS = {"s4_D9_clean": "9 PM  →  5 AM"}

def run(cmd): subprocess.run(cmd, check=True)
def dur(p): return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)]))
def norm(w): return re.sub(r"[^a-z0-9']", "", w.lower().replace("’", "'"))

def words_of(path):
    j = pathlib.Path(str(path).rsplit(".", 1)[0] + ".json")
    if not j.exists(): run(["vs", "transcribe", str(path), "-o", str(j)])
    return [dict(w=x["w"], s=x["s"], e=x["e"]) for x in json.load(open(j))["words"]]

def compact(wav, words, name):
    """Cut pauses longer than MAX_GAP down to MAX_GAP; return new wav + remapped words."""
    keep, t0 = [], max(0.0, words[0]["s"] - 0.05)
    cur = [t0, words[0]["e"]]
    for w in words[1:]:
        if w["s"] - cur[1] > MAX_GAP: keep.append(cur); cur = [w["s"] - MAX_GAP / 2, w["e"]]
        else: cur[1] = w["e"]
    cur[1] += 0.12; keep.append(cur)
    for k in keep[:-1]: k[1] += MAX_GAP / 2
    out = WORK / f"vo_{name}.wav"
    parts = "".join(f"[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS[p{i}];" for i, (a, b) in enumerate(keep))
    run(["ffmpeg", "-v", "error", "-y", "-i", str(wav), "-filter_complex",
         parts + "".join(f"[p{i}]" for i in range(len(keep))) + f"concat=n={len(keep)}:v=0:a=1,aresample={SR},aformat=channel_layouts=stereo[a]",
         "-map", "[a]", str(out)])
    nw, off = [], 0.0
    for a, b in keep:
        for w in words:
            if a <= w["s"] < b: nw.append(dict(w=w["w"], s=w["s"] - a + off, e=min(w["e"], b) - a + off))
        off += b - a
    return out, nw, off

def find_starts(words, cues):
    """First cue covers the unit start; later cues start on the next matching word ('kid#3' = 3rd 'kid' in the line)."""
    res, idx = [(0, cues[0][1])], 0
    for cue, src in cues[1:]:
        base, _, nth = cue.partition("#")
        if nth:
            hits = [k for k, w in enumerate(words) if norm(w["w"]) == base]
            if len(hits) < int(nth): raise SystemExit(f"cue {cue!r}: only {len(hits)} in {[w['w'] for w in words]}")
            found = hits[int(nth) - 1]
        else:
            found = next((k for k in range(idx + 1, len(words)) if norm(words[k]["w"]) == base), None)
            if found is None: raise SystemExit(f"cue {cue!r} not found after word {idx} in {[w['w'] for w in words]}")
        res.append((found, src)); idx = found
    return res

def src_path(kind, name):
    return {R: RAW / "reuse" / f"{name}.mp4", N: RAW / "new" / f"{name}.mp4", ST: RAW / "frames" / f"{name}.png"}[kind]

def render_shot(i, kind, name, inp, sec):
    out = WORK / f"shot_{i:03d}.mp4"
    vf_scale = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1"
    chip = ""
    if name in CHIPS:
        chip = (f",drawtext=fontfile={BOLD}:text='{CHIPS[name]}':fontsize={int(W*0.05)}:fontcolor=white:box=1:boxcolor=0x0B2A5B@0.85:"
                f"boxborderw={int(W*0.02)}:x=w-text_w-{int(W*0.06)}:y={int(H*0.08)}")
    flag = ""
    if kind == ST:
        frames = int(round(sec * FPS))
        vf = (f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},"
              f"zoompan=z='1+0.10*on/{frames}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s={W}x{H}:fps={FPS},setsar=1")
        run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-i", str(src_path(kind, name)), "-vf", vf + chip, "-t", f"{sec:.3f}",
             "-r", str(FPS), "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", str(out)])
        return out, "still push-in"
    p = src_path(kind, name); avail = dur(p) - inp; speed = 1.0
    if avail < sec:
        speed = max(MIN_SPEED, avail / sec); flag = f"slowed {speed:.2f}x"
        if avail / speed < sec - 0.02: flag += f" SHORT by {sec - avail/speed:.2f}s (last frames hold-free: tpad clone)"
    vf = f"trim=start={inp},setpts=(PTS-STARTPTS)/{speed},{vf_scale},fps={FPS},tpad=stop_mode=clone:stop_duration=2,trim=duration={sec:.3f}"
    run(["ffmpeg", "-v", "error", "-y", "-i", str(p), "-vf", vf + chip, "-an", "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast",
         "-crf", "20", "-pix_fmt", "yuv420p", str(out)])
    return out, flag

def render_take(i, path, ranges):
    out_v, out_a = WORK / f"shot_{i:03d}.mp4", WORK / f"take_{i:03d}.wav"
    if isinstance(ranges, tuple): ranges = [ranges]
    p = RAW / path
    vparts = "".join(f"[0:v]trim={a}:{b},setpts=PTS-STARTPTS[v{k}];" for k, (a, b) in enumerate(ranges))
    aparts = "".join(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS[a{k}];" for k, (a, b) in enumerate(ranges))
    m = len(ranges)
    fc = (vparts + aparts + "".join(f"[v{k}]" for k in range(m)) + f"concat=n={m}:v=1:a=0,scale={W}:{H}:force_original_aspect_ratio=increase,"
          f"crop={W}:{H},setsar=1,fps={FPS}[v];" + "".join(f"[a{k}]" for k in range(m)) + f"concat=n={m}:v=0:a=1,aresample={SR},"
          "aformat=channel_layouts=stereo[a]")
    run(["ffmpeg", "-v", "error", "-y", "-i", str(p), "-filter_complex", fc, "-map", "[v]", "-c:v", "libx264", "-preset", "veryfast",
         "-crf", "20", "-pix_fmt", "yuv420p", "-r", str(FPS), str(out_v), "-map", "[a]", str(out_a)])
    # word timings for captions, remapped through the cuts
    words, nw, off = words_of(p), [], 0.0
    for a, b in ranges:
        for w in words:
            if a <= w["s"] < b: nw.append(dict(w=w["w"], s=w["s"] - a + off, e=min(w["e"], b) - a + off))
        off += b - a
    return out_v, out_a, nw, dur(out_v)

def ass_time(t):
    h, rem = divmod(max(t, 0), 3600); m, s_ = divmod(rem, 60)
    return f"{int(h)}:{int(m):02d}:{s_:05.2f}"

def captions(all_words, path):
    fs = int(W * 0.085)
    head = ("[Script Info]\nScriptType: v4.00+\nPlayResX: %d\nPlayResY: %d\n\n[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, "
            "SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, "
            "Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\nStyle: Cap,Inter,%d,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,"
            "0,0,1,%d,2,2,%d,%d,%d,1\n\n[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n"
            % (W, H, fs, max(3, fs // 9), int(W * .08), int(W * .08), int(H * .30)))
    ev, chunk = [], []
    def flush():
        for k, w in enumerate(chunk):
            end = chunk[k + 1]["s"] if k + 1 < len(chunk) else w["e"] + 0.15
            txt = " ".join(("{\\c&H1A4EE0&}" + x["w"].upper() + "{\\c&HFFFFFF&}") if j == k else x["w"].upper() for j, x in enumerate(chunk))
            ev.append(f"Dialogue: 0,{ass_time(w['s'])},{ass_time(end)},Cap,,0,0,0,,{txt}")
    for w in all_words:
        if chunk and (len(chunk) >= 4 or w["s"] - chunk[-1]["e"] > 0.35 or chunk[-1]["w"].endswith((".", "?", ","))):
            flush(); chunk = []
        chunk.append(w)
    if chunk: flush()
    path.write_text(head + "\n".join(ev) + "\n")

# ---- assemble -------------------------------------------------------------------------------------------------
units = HOOKS[HOOK] + BODY
shots, voice_parts, cap_words, report, t = [], [], [], [], 0.0
i = 0
for u in units:
    if u[0] == "vo":
        wav = RAW / "vo" / f"{u[1]}.wav"
        vw, ww, length = compact(wav, words_of(wav), u[1])
        starts = find_starts(ww, u[2])
        unit_len = length + GAP_UNIT
        bounds = [0.0] + [ww[k]["s"] - 0.04 for k, _ in starts[1:]] + [unit_len]
        for j, (_, (kind, name, inp)) in enumerate(starts):
            sec = round(bounds[j + 1] - bounds[j], 3)
            out, flag = render_shot(i, kind, name, inp, sec); i += 1
            shots.append(out); report.append((u[1], f"{t + bounds[j]:.2f}", f"{sec:.2f}", kind, name, flag))
        voice_parts.append((vw, t)); cap_words += [dict(w=w["w"], s=w["s"] + t, e=w["e"] + t) for w in ww]
        t += unit_len
    else:
        out_v, out_a, ww, length = render_take(i, u[1], u[2]); i += 1
        shots.append(out_v); voice_parts.append((out_a, t)); cap_words += [dict(w=w["w"], s=w["s"] + t, e=w["e"] + t) for w in ww]
        report.append((pathlib.Path(u[1]).stem, f"{t:.2f}", f"{length:.2f}", "take", u[1], ""))
        # tiny breath after a take
        gap = WORK / f"shot_{i:03d}.mp4"; i += 1
        run(["ffmpeg", "-v", "error", "-y", "-sseof", "-0.04", "-i", str(out_v), "-vf", f"tpad=stop_mode=clone:stop_duration={GAP_UNIT}",
             "-t", f"{GAP_UNIT}", "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", "-r", str(FPS), str(gap)])
        shots.append(gap); t += length + GAP_UNIT
# end card
card = WORK / f"shot_{i:03d}.mp4"
bottle = RAW / "frames" / "endcard_bottle.png"
run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=c=0xEEF4FA:s={W}x{H}:r={FPS}:d={END_CARD_S}", "-i", str(bottle), "-filter_complex",
     f"[1]scale=-2:{int(H*0.42)}[b];[0][b]overlay=(W-w)/2:{int(H*0.40)},scale={W*2}:{H*2},"
     f"zoompan=z='1+0.06*on/{int(END_CARD_S*FPS)}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS},"
     f"drawtext=fontfile={BOLD}:text='Not the top. The root.':fontsize={int(W*0.075)}:fontcolor=0x0B2A5B:x=(w-text_w)/2:y={int(H*0.14)},"
     f"drawtext=fontfile={BOLD}:text='Buy 2, get 1 free':fontsize={int(W*0.06)}:fontcolor=white:box=1:boxcolor=0xE04E18:boxborderw={int(W*0.025)}:"
     f"x=(w-text_w)/2:y={int(H*0.27)},setsar=1", "-t", str(END_CARD_S), "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
     "-pix_fmt", "yuv420p", str(card)])
shots.append(card); report.append(("end", f"{t:.2f}", f"{END_CARD_S:.2f}", "card", "end card", "")); total = t + END_CARD_S

lst = WORK / "shots.txt"; lst.write_text("".join(f"file '{p}'\n" for p in shots))
video = WORK / "video.mp4"
run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(video)])

# voice track
ins, fl = [], []
for k, (p, at) in enumerate(voice_parts):
    ins += ["-i", str(p)]; fl.append(f"[{k}:a]aresample={SR},aformat=channel_layouts=stereo,adelay={int(at*1000)}|{int(at*1000)}[v{k}]")
voice = WORK / "voice.wav"
run(["ffmpeg", "-v", "error", "-y"] + ins + ["-filter_complex", ";".join(fl) + ";" + "".join(f"[v{k}]" for k in range(len(voice_parts)))
     + f"amix=inputs={len(voice_parts)}:normalize=0,apad,atrim=0:{total:.3f},loudnorm=I=-16:TP=-1.5:LRA=7[a]", "-map", "[a]", str(voice)])

# music: ducked under the voice (sidechain), bed lifted where nobody speaks, short fade at the very end
mix = WORK / "mix.wav"
run(["ffmpeg", "-v", "error", "-y", "-i", str(voice), "-i", str(MUSIC), "-filter_complex",
     f"[1:a]atrim=0:{total:.3f},asetpts=PTS-STARTPTS,aresample={SR},volume=-11dB,afade=t=out:st={total-0.6:.3f}:d=0.6[m];"
     "[0:a]asplit[vk][vo];[m][vk]sidechaincompress=threshold=0.02:ratio=6:attack=20:release=450[md];"
     "[vo][md]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-2.0:LRA=9,alimiter=limit=0.85:level=false[a]", "-map", "[a]", str(mix)])

ass = WORK / f"captions_{HOOK}.ass"; captions(cap_words, ass)
hook_txt = HOOK_TITLE[HOOK]
final = OUT / f"WilloMD_RootOut_Set2_{HOOK}_9x16_v1{'_preview' if PREVIEW else ''}.mp4"
vf = (f"ass={ass},drawtext=fontfile={BOLD}:text='{hook_txt}':fontsize={int(W*0.075)}:fontcolor=white:box=1:boxcolor=0xE04E18:"
      f"boxborderw={int(W*0.025)}:x=(w-text_w)/2:y={int(H*0.10)}:enable='lt(t,3)'")
run(["ffmpeg", "-v", "error", "-y", "-i", str(video), "-i", str(mix), "-vf", vf, "-map", "0:v", "-map", "1:a", "-c:v", "libx264",
     "-preset", "veryfast" if PREVIEW else "slow", "-crf", "23" if PREVIEW else "18", "-c:a", "aac", "-b:a", "192k", "-shortest",
     "-movflags", "+faststart", "-map_metadata", "-1", str(final)])

used = [x[4] for x in report if x[3] in (R, N, ST)]
dups = sorted({u for u in used if used.count(u) > 1})
md = [f"# Set 2 · {HOOK} v1 shot list", "", f"{total:.1f} s · {len(report)} shots · duplicate sources: {dups or 'none'}", "",
      "| unit | in | sec | kind | source | flag |", "|---|---|---|---|---|---|"] + [f"| {' | '.join(map(str, x))} |" for x in report]
(HERE / f"SHOTS_{HOOK}_v1.md").write_text("\n".join(md) + "\n")
print(final, f"{total:.1f}s", "dups:", dups)
