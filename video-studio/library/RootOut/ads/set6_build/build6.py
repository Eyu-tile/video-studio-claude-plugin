#!/usr/bin/env python3
"""Set 6 H1 edit (owner 26 Nov: the whole ad in her own on-camera voice, the hook's natural vibe).
Each section = one Seedance take (her native voice, untouched, no clone, no lip-sync pass). The picture cuts away to
b-roll on the exact word it shows (ElevenLabs STT word times) while her take audio keeps playing, then back to her.
House/RootOut rules: L1 no disclaimer text · L2 ~3 s b-roll on the words · L4 each source once, no freeze, >=0.75x ·
L5 bold word-by-word captions, active word highlighted, kept off graphics · L6 music to the last frame · L7 voice + music only.
Usage: build6.py [--plan]  -> projects/rootout-set6/out/WilloMD_RootOut_Set6_H1_9x16_v1.mp4"""
import json, re, subprocess, sys, difflib
from pathlib import Path

P = Path("/home/user/video-studio-claude-plugin/video-studio/projects/rootout-set6")
TK, RU, ST, GN, GX = P / "raw/takes", P / "raw/reuse", P / "raw/stills", P / "raw/gen", P / "assets/graphics"
TMP = P / "work/v1"; TMP.mkdir(parents=True, exist_ok=True); (P / "out").mkdir(exist_ok=True)
W, H, FPS = 1080, 1920, 24
ENC = ["-c:v", "libx264", "-crf", "16", "-preset", "medium", "-pix_fmt", "yuv420p", "-r", str(FPS)]
COVER = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1"
MUSIC_FILE, MUSIC = P / "assets/music/Wholesome.mp3", 0.12
norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())
NUM = {"4": "four", "90": "ninety", "14": "fourteen", "8": "eight", "1500": "fifteenhundred", "2": "two"}

def dur(f): return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)]))
def run(a):
    r = subprocess.run(["ffmpeg", "-y", "-v", "error", *map(str, a)], capture_output=True, text=True)
    if r.returncode: sys.exit(" ".join(map(str, a))[:400] + "\n" + r.stderr[-2500:])

# ---- script text per take (captions use these words, timed by STT) ----
LINES = {
 "K1": "My son started limping in October. By Christmas, his little sister had a wart too. This is what finally got rid of them, at bedtime, with no freezing.",
 "T02_limp": "It started with a limp. He walked on the side of his foot. Every school morning was a fight over socks. He said it hurt to step on. I thought it was a splinter. I shook out his shoes. I tried tweezers. Nothing.",
 "T03_found": "Then one night at bath time, I turned his foot over. A hard little spot, with tiny black dots. A plantar wart.",
 "T04a_two": "And it didn't stay one. A month later there were two. Then his little sister had one on her heel.",
 "T04b_study": "I looked it up. A study of almost 1,500 schoolkids found that someone at home with a wart makes the other kids about twice as likely to get one.",
 "T05_soccer": "He sat out his soccer games. He wouldn't take his shoes off at a friend's house.",
 "T06_freeze": "So we did what the doctor said. We froze it. Somebody had to hold him still. It blistered, and he limped worse for a week. Three weeks later, it was back. Same spot.",
 "T07_next": "And now his sister was next in line for the freeze.",
 "T08a_tip": "Then a mom from his team told me why it keeps coming back. Freezing, acid and shaving only snap off the top, like picking a dandelion.",
 "T08b_rootout": "The root stays under the hard skin, so it grows back. She used RootOut. It's an oil with four plants, and you brush it on at bedtime.",
 "T09a_honest": "Honestly, I didn't think it would work. But it was two minutes at bedtime, and nobody had to hold anybody down.",
 "T09b_routine": "Two light rubs with the little file, just on the hard top. Brush the oil on. A clear dot on top. He said it felt cool. In about two weeks, it was gone. His sister's too.",
 "T10a_wish": "Here's what I wish I'd known sooner. The lemon softens that hard skin on top. The tea tree is a thin oil.",
 "T10b_root": "It sinks in, up to 8x deeper than a regular cream, and carries the pokeweed and white cedar down to the root. Then those two break the wart down from there, so it can't grow back.",
 "T11_safe": "It's a kids' formula, for ages 4 and up, and pediatricians recommend it. No freezing, no acid, no blister.",
 "T12_after": "We did fourteen more nights after it was gone, so the root was gone too. He's back at soccer. Running, not limping.",
 "T13a_wait": "If your kid's limping and you find a hard spot under his foot, don't wait for it to spread.",
 "T13b_offer": "It's at the link below. Buy two, we'll add a third. And if it's not gone, you've got 90 days to get your money back.",
}
R = lambda n: RU / f"{n}.mp4"; N = lambda n: ST / f"{n}.png"
# (anchor, kind, src, opts); anchor: 0 | (word, occurrence[, words_back]) ; kind: talk | clip | photo | anim
SECTIONS = [
 ("K1", [(0, "talk", None, {"hook": GX / "hook_h1.png"}), (("his", 0), "photo", N("N1"), {}), (("This", 0), "talk", None, {})]),
 ("T02_limp", [(0, "clip", GN / "G1_walk.mp4", {}), (("He", 0), "clip", R("5b408ca8"), {"ss": 0.2}), (("Every", 0), "clip", R("ca35a172"), {"ss": 0.3}),
               (("He", 1), "clip", R("66b36e48"), {"ss": 0.3}), (("I", 0), "talk", None, {}),
               (("shook", 0, 1), "photo", N("N2"), {}), (("tried", 0, 1), "photo", N("N3"), {}), (("Nothing", 0), "talk", None, {})]),
 ("T03_found", [(0, "talk", None, {}), (("A", 0), "clip", R("07db7f0f"), {"ss": 0.2}), (("A", 1), "talk", None, {})]),
 ("T04a_two", [(0, "talk", None, {}), (("A", 0), "photo", N("N4"), {}), (("Then", 0), "clip", R("4d831173"), {"ss": 0.4})]),
 ("T04b_study", [(0, "talk", None, {}), (("A", 0), "clip", R("991d4d67"), {"ss": 0.2}), (("found", 0), "anim", GX / "c_citation.mp4", {"nocap": 1}),
                 (("about", 0), "talk", None, {})]),
 ("T05_soccer", [(0, "photo", N("N5"), {}), (("He", 1), "photo", N("N6"), {})]),
 ("T06_freeze", [(0, "talk", None, {}), (("We", 1), "clip", R("2eadbf23"), {"ss": 0.0}), (("blistered", 0, 1), "clip", R("b959c1ff"), {"ss": 0.3}),
                 (("Three", 0), "clip", R("28fafd4b"), {"ss": 0.6}), (("Same", 0), "talk", None, {})]),
 ("T07_next", [(0, "talk", None, {}), (("next", 0), "photo", N("N7"), {})]),
 ("T08a_tip", [(0, "clip", GN / "G2_sideline.mp4", {}), (("Freezing", 0), "talk", None, {}), (("snap", 0), "clip", R("3e99af22"), {"ss": 0.0})]),
 ("T08b_rootout", [(0, "clip", R("ee317059"), {"ss": 0.0}), (("so", 0), "clip", R("644d4a63"), {"ss": 0.2}), (("She", 0), "talk", None, {})]),
 ("T09a_honest", [(0, "talk", None, {})]),
 ("T09b_routine", [(0, "clip", R("757ba2f9"), {"ss": 0.3}), (("Brush", 0), "clip", R("18e77103"), {"ss": 0.4}), (("A", 0), "clip", R("686ace6f"), {"ss": 0.3}),
                   (("He", 0), "clip", R("e2efa595"), {"ss": 0.2}), (("In", 0), "clip", R("d24782f6"), {"ss": 0.2})]),
 ("T10a_wish", [(0, "talk", None, {}), (("The", 0), "clip", R("56f40499"), {"ss": 0.0}), (("The", 1), "talk", None, {})]),
 ("T10b_root", [(0, "clip", R("ce962fe0"), {"ss": 0.0, "gauge": 1}), (("and", 0), "clip", R("692c7031"), {"ss": 0.0}),
                (("down", 0), "clip", R("b747a959"), {"ss": 0.3}), (("Then", 0), "talk", None, {}), (("break", 0), "clip", R("1d651123"), {"ss": 0.0})]),
    # T10b audio: "and carries the pokeweed and white cedar down to the root." is a Seed Audio patch in her voice
    # (she mispronounced "white cedar" in 3 takes); it plays only under the two cutaways above, never over her lips.
 ("T11_safe", [(0, "talk", None, {})]),
 ("T12_after", [(0, "clip", R("e211dc9d"), {"ss": 0.0}), (("so", 0), "talk", None, {}), (("He's", 0), "clip", R("ee26b25b"), {"ss": 0.0}), (("Running", 0), "talk", None, {})]),
 ("T13a_wait", [(0, "talk", None, {})]),
 ("T13b_offer", [(0, "talk", None, {}), (("Buy", 0), "clip", R("5e57f5fc"), {"ss": 0.6}), (("And", 0), "anim", GX / "c_offer.mp4", {"nocap": 1})]),
]
GAP_IN, GAP_OUT = 0.10, 0.22   # breath kept before the first and after the last word of each take
ZOOM = [1.0, 1.07]             # alternate framing between consecutive takes (hides jump cuts on her)

def words(name):
    f = TK / f"{name}.mp4"; j = TK / f"{name}.stt.json"
    if not j.exists():
        a = TK / f"{name}.mp3"; run(["-i", f, "-vn", "-ac", "1", a])
        subprocess.run(["curl", "-s", "-m", "180", "-X", "POST", "https://api.elevenlabs.io/v1/speech-to-text", "-H", "xi-api-key: dummy",
                        "-F", "model_id=scribe_v1", "-F", "timestamps_granularity=word", "-F", f"file=@{a}", "-o", str(j)], check=True)
    out = []
    for w in json.load(open(j))["words"]:
        if w.get("type") != "word": continue
        for p in w["text"].replace("-", " ").split():
            n = norm(p); out.append((NUM.get(n, n), w["start"], w["end"], p))
    return out

def check_words(name, ws):
    sc = [NUM.get(norm(x), norm(x)) for x in LINES[name].replace("-", " ").replace("1,500", "fifteen hundred").replace("8x", "eight times").split()]
    sc = [x for x in sc if x]; hw = [w[0] for w in ws]
    sm = difflib.SequenceMatcher(None, sc, hw, autojunk=False)
    miss = [(op, " ".join(sc[a:b]), " ".join(hw[c:d])) for op, a, b, c, d in sm.get_opcodes() if op != "equal"]
    return miss

def anchor(ws, a):
    if a == 0: return 0.0
    w, occ = a[0], a[1]; back = a[2] if len(a) > 2 else 0
    idx = [i for i, x in enumerate(ws) if x[0] == NUM.get(norm(w), norm(w))]
    if occ >= len(idx): sys.exit(f"anchor {a} not found in {' '.join(x[0] for x in ws)}")
    return ws[max(0, idx[occ] - back)][1]

def chain(kind, src, d, ss=0.0, zoom=1.0):
    if kind in ("clip", "anim", "talk"):
        avail = dur(src) - ss; f = 1.0 if kind == "talk" else min(1.0, avail / d)
        if f < 0.75: sys.exit(f"{src.name}: needs {d:.2f}s from {ss:.2f}, has {avail:.2f}s (would be {f:.2f}x)")
        rate = f"minterpolate=fps={FPS}:mi_mode=blend" if f < 0.97 else f"fps={FPS}"
        z = f",scale={int(W * zoom)}:{int(H * zoom)},crop={W}:{H},setsar=1" if zoom != 1.0 else ""
        return f"[0:v]trim=start={ss:.3f},setpts=(PTS-STARTPTS)/{f:.4f},{rate},{COVER}{z}"
    n = int(d * FPS) + 2
    return (f"[0:v]scale={W * 2}:{H * 2}:force_original_aspect_ratio=increase,crop={W * 2}:{H * 2},setsar=1,"
            f"zoompan=z='1+0.06*on/{n}':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d={n}:s={W}x{H}:fps={FPS}")

def piece(kind, src, d, o, out):
    ins = ["-loop", "1", "-i", src] if kind == "photo" else ["-i", src]
    g = chain(kind, src, d, o.get("ss", 0.0), o.get("zoom", 1.0)) + "[v0]"; cur = "[v0]"
    if o.get("hook"):
        ins += ["-loop", "1", "-i", o["hook"]]; g += f";{cur}[1:v]overlay=x=(W-w)/2:y=150:enable='between(t,0.15,3.2)'[vh]"; cur = "[vh]"
    if o.get("gauge"):
        ins += ["-framerate", str(FPS), "-i", GX / "gauge/g%03d.png"]; k = len([x for x in ins if x == "-i"]) - 1
        g += f";[{k}:v]tpad=stop_mode=clone:stop_duration=30[gg];{cur}[gg]overlay=x=760:y=420:shortest=0[vg]"; cur = "[vg]"
    run([*ins, "-filter_complex", g, "-map", cur, "-t", f"{d:.3f}", "-an", *ENC, out])

def build_section(si, name, items):
    src = TK / f"{name}.mp4"; ws = words(name)
    first = NUM.get(norm(LINES[name].split()[0]), norm(LINES[name].split()[0]))
    k0 = next(i for i, w in enumerate(ws) if w[0] == first); ws = ws[k0:]   # drop words she added before the line (T09b)
    miss = check_words(name, ws)
    if miss: print(f"  ! {name} words differ from script: {miss}")
    a = max(0.0, ws[0][1] - GAP_IN); b = min(dur(src), ws[-1][2] + GAP_OUT); total = b - a
    wsr = [(w, s - a, e - a, p) for w, s, e, p in ws]
    starts = [max(0.0, anchor(wsr, it[0]) - 0.04) if it[0] != 0 else 0.0 for it in items]
    if any(y <= x + 0.3 for x, y in zip(starts, starts[1:])): sys.exit(f"{name}: shots too close {starts}")
    zoom = ZOOM[si % 2]; parts, plan = [], []
    for j, ((_, kind, s, o), t0) in enumerate(zip(items, starts)):
        t1 = starts[j + 1] if j + 1 < len(items) else total; d = t1 - t0; o = dict(o)
        if kind == "talk": s = src; o["ss"] = a + t0; o["zoom"] = zoom
        out = TMP / f"{si:02d}_{name}_{j}.mp4"
        if "--plan" not in sys.argv and not ("--assemble" in sys.argv and out.exists() and name not in REBUILD): piece(kind, s, d, o, out)
        parts.append(out); plan.append((round(t0, 2), round(d, 2), kind, Path(s).stem, o.get("nocap", 0)))
    sec = TMP / f"sec_{si:02d}_{name}.mp4"
    if "--plan" not in sys.argv and not ("--assemble" in sys.argv and sec.exists() and name not in REBUILD):
        ins = sum((["-i", p] for p in parts), [])
        vc = "".join(f"[{j}:v]setsar=1[s{j}];" for j in range(len(parts))) + "".join(f"[s{j}]" for j in range(len(parts))) + f"concat=n={len(parts)}:v=1:a=0[v]"
        run([*ins, "-ss", f"{a:.3f}", "-t", f"{total:.3f}", "-i", src, "-filter_complex",
             f"{vc};[{len(parts)}:a]aresample=48000,aformat=channel_layouts=stereo,apad,atrim=0:{total:.3f}[a]",
             "-map", "[v]", "-map", "[a]", "-t", f"{total:.3f}", *ENC, "-c:a", "aac", "-b:a", "192k", sec])
    return sec, total, wsr, plan

def captions(tl, D):
    """L5: bold word-by-word captions, active word highlighted; moved to the top over full-frame graphics."""
    toks = []
    for x in tl:
        disp = LINES[x["take"]].split(); ws = x["words"]
        a = [NUM.get(norm(d), norm(d)) for d in disp]; b = [w[0] for w in ws]
        a = sum(([y] if y != "8x" else ["eight", "times"] for y in a), [])
        tm = [None] * len(a)
        for blk in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks():
            for k in range(blk.size): tm[blk.a + k] = (ws[blk.b + k][1], ws[blk.b + k][2])
        for k in range(len(tm)):
            if tm[k] is None:
                prev = next((tm[j][1] for j in range(k - 1, -1, -1) if tm[j]), 0.0)
                nxt = next((tm[j][0] for j in range(k + 1, len(tm)) if tm[j]), prev + 0.3); tm[k] = (prev, max(prev + 0.08, nxt - 0.02))
        # fold the expanded number tokens back onto the display words
        i = 0
        for d in disp:
            n = 2 if norm(d) == "8x" else 1
            s, e = tm[i][0], tm[i + n - 1][1]; i += n
            toks.append((d, x["start"] + s, x["start"] + e, x["take"]))
    groups, cur = [], []
    for t in toks:
        if cur and (t[1] - cur[-1][2] > 0.5 or t[3] != cur[-1][3]): groups.append(cur); cur = []
        cur.append(t)
        if len(cur) >= 4 or (t[0][-1:] in ".,?!" and len(cur) >= 2) or (len(cur) >= 3 and sum(len(z[0]) for z in cur) > 17): groups.append(cur); cur = []
    if cur: groups.append(cur)
    top = [(z["t0"], z["t1"]) for z in TOPS]
    ts = lambda v: f"{int(v // 3600)}:{int(v % 3600 // 60):02d}:{v % 60:05.2f}"
    ass = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 1080", "PlayResY: 1920", "", "[V4+ Styles]",
           "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
           "Style: Cap,Inter,72,&H00FFFFFF,&H00FFFFFF,&H00141414,&H64000000,-1,0,0,0,100,100,0,0,1,7,2,2,80,80,400,1",
           "Style: Top,Inter,72,&H00FFFFFF,&H00FFFFFF,&H00141414,&H64000000,-1,0,0,0,100,100,0,0,1,7,2,8,80,80,190,1",
           "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
    for j, g in enumerate(groups):
        gend = min(groups[j + 1][0][1] - 0.02, g[-1][2] + 0.35) if j + 1 < len(groups) else g[-1][2] + 0.3
        gend = min(gend, D - END_D - 0.05)
        for k, w in enumerate(g):
            s = w[1] if k else g[0][1]; e = g[k + 1][1] if k + 1 < len(g) else gend
            if e <= s: continue
            st = "Top" if any(a0 - 0.05 <= s < a1 for a0, a1 in top) else "Cap"
            txt = " ".join(("{\\c&H1858E0&}" + z[0] + "{\\c&HFFFFFF&}") if i == k else z[0] for i, z in enumerate(g)).rstrip(",")
            ass.append(f"Dialogue: 0,{ts(s)},{ts(e)},{st},,0,0,0,,{txt}")
    (TMP / "captions.ass").write_text("\n".join(ass) + "\n"); return len(groups)

END_D = 3.2; TOPS = []; PREVIEW = "--preview" in sys.argv
REBUILD = set(sys.argv[sys.argv.index("--rebuild") + 1].split(",")) if "--rebuild" in sys.argv else set()
if __name__ == "__main__":
    outs, tl, t = [], [], 0.0; used = []
    for si, (name, items) in enumerate(SECTIONS):
        out, d, ws, plan = build_section(si, name, items)
        for t0, dd, kind, stem, nocap in plan:
            print(f"  {t + t0:7.2f} {dd:5.2f}s {kind:5s} {stem}" + ("  <- b-roll outside 1.5-4.2 s" if kind != "talk" and not (1.4 <= dd <= 4.2) else ""))
            if kind != "talk": used.append(stem)
            if nocap: TOPS.append({"t0": t + t0, "t1": t + t0 + dd})
        tl.append({"take": name, "start": round(t, 3), "dur": round(d, 3), "words": [list(w) for w in ws]}); outs.append(out); t += d
        print(f"{name:14s} {t - d:7.2f} +{d:6.2f}")
    dup = {s for s in used if used.count(s) > 1}
    if dup: sys.exit(f"L4: sources used twice: {dup}")
    print(f"total {t + END_D:.1f} s with end card; {len(used)} cutaways")
    if "--plan" in sys.argv: sys.exit()
    end = TMP / "sec_99_end.mp4"
    run(["-i", GX / "c_end.mp4", "-f", "lavfi", "-t", str(END_D), "-i", "anullsrc=r=48000:cl=stereo", "-vf", f"{COVER},fps={FPS}", "-t", str(END_D), *ENC, "-c:a", "aac", "-b:a", "192k", "-shortest", end])
    outs.append(end); (TMP / "list.txt").write_text("".join(f"file '{o}'\n" for o in outs)); json.dump(tl, open(TMP / "timeline.json", "w"), indent=1)
    cat = TMP / "cut.mp4"; run(["-f", "concat", "-safe", "0", "-i", TMP / "list.txt", "-c", "copy", cat])
    D = dur(cat); n = captions(tl, D)
    fc = (f"[1:a]atrim=0:{D:.2f},asetpts=PTS-STARTPTS,volume={MUSIC},afade=t=in:d=1.0,afade=t=out:st={D - 0.6:.2f}:d=0.6[m];"
          f"[0:a]asplit[vo][sc];[m][sc]sidechaincompress=threshold=0.03:ratio=4:attack=20:release=400[md];"
          f"[vo][md]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-2:LRA=9,alimiter=limit=0.79:level=false[a];"
          f"[0:v]ass={TMP / 'captions.ass'},noise=alls=3:allf=t,vignette=PI/6[v]")
    final = P / "out/WilloMD_RootOut_Set6_H1_9x16_v1.mp4"
    run(["-i", cat, "-i", MUSIC_FILE, "-filter_complex", fc, "-map", "[v]", "-map", "[a]", "-r", str(FPS),
         "-c:v", "libx264", "-crf", "20" if PREVIEW else "18", "-maxrate", "10M", "-bufsize", "20M", "-preset", "veryfast" if PREVIEW else "slow", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-map_metadata", "-1", "-movflags", "+faststart", final])
    print("H1", round(dur(final), 2), "s,", n, "caption groups ->", final)
