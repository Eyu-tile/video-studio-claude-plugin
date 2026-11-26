#!/usr/bin/env python3
"""Set 15 builder (H1/H2/H3). Every spoken line is a Seedance take's own audio (lips and voice made together):
the mom's takes all use M1's voice as reference, the boy's use B1's. B-roll cuts sit on her words (ElevenLabs STT word
times), ~3 s each, each source once (L2-L4). Captions bold word by word with the active word highlighted (L5), music to
the last frame (L6), voice + music only (L7), no disclaimer text anywhere (house L1).
Usage: HOOK=H1 python3 build15.py [--plan]"""
import difflib, json, os, re, subprocess, sys
from pathlib import Path

P = Path("/home/user/video-studio-claude-plugin/projects/rootout-set15")
CL = P / "raw/gen/clips"; RE = P / "raw/reuse"; G = P / "assets/graphics"; MUSIC = P / "assets/music/Pamgaea.mp3"
SITE = Path("/home/user/video-studio-claude-plugin/video-studio/library/RootOut/resources/site_videos/shopify-3062835a.mp4")
HOOK = os.environ.get("HOOK", "H1"); VER = os.environ.get("VER", "v1")
OUT = P / f"work/{HOOK}"; SH = OUT / "shots"; SH.mkdir(parents=True, exist_ok=True)
FINAL = P / f"out/WilloMD_RootOut_Set15_{HOOK}_9x16_{VER}.mp4"; FINAL.parent.mkdir(exist_ok=True)
W, H, FPS, END = 1080, 1920, 30, 3.0
COVER = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}"
ENC = ["-an", "-c:v", "libx264", "-crf", "17", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-r", str(FPS)]
NUM = {"4": "four", "8x": "eight times", "14": "fourteen", "5": "five", "6": "six"}
TAKE = "TAKE"

def ff(*a):
    r = subprocess.run(["ffmpeg", "-v", "error", "-y", *map(str, a)], capture_output=True, text=True)
    if r.returncode: sys.exit(" ".join(map(str, a))[:400] + "\n" + r.stderr[-1500:])
def dur(f): return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)]))
def norm(w): return re.sub(r"[^a-z0-9]", "", w.lower())
def spoken(text): return " ".join(NUM.get(w.strip(".,!?\"'"), w) for w in text.split())

def stt(f):
    j = Path(str(f) + ".stt.json")
    if not j.exists():
        subprocess.run(["curl", "-s", "-m", "180", "-X", "POST", "https://api.elevenlabs.io/v1/speech-to-text", "-H", "xi-api-key: dummy",
                        "-F", "model_id=scribe_v1", "-F", "timestamps_granularity=word", "-F", f"file=@{f}", "-o", str(j)], check=True)
    out = []
    for w in json.load(open(j))["words"]:
        if w.get("type") != "word": continue
        for p in w["text"].replace("-", " ").split():
            n = norm(p); n = {"8x": "eighttimes", "4": "four", "14": "fourteen"}.get(n, n)
            if n: out.append((n, w["start"], w["end"]))
    return out

def find(words, phrase, after=0.0):
    ph = [norm(x) for x in spoken(phrase).replace("-", " ").split()]; ph = [x for x in ph if x]
    seq = [w[0] for w in words]; J = "".join
    for i in range(len(seq)):
        if words[i][1] < after - 0.01: continue
        for j in range(i + 1, min(len(seq), i + len(ph) + 3) + 1):
            if J(seq[i:j]) == J(ph): return words[i][1], words[j - 1][2]
    raise KeyError(f"{phrase!r} not in {' '.join(seq)}")

VOD = P / "raw/gen/vo"
TK = lambda n: (VOD / f"{n[3:]}.wav") if n.startswith("vo/") else CL / f"{n}.mp4"
# a "vo/<name>" item is a re-voiced line (Seed Audio cloned from the same person's take); its TAKE visual comes from opts vtake
# (take, text spoken in it, gap after, visuals [(phrase|None, source|TAKE, opts)])
ITEMS = [
 ("B1", "They froze my wart five times.", 0.1, [(None, TAKE, {"hook": 1})]),
 ("B1", "It always came back.", 0.4, [(None, RE / "r01_clinic.mp4", {"in": 0.2})]),
 # B2's take says "I miss swim": voice = Seed Audio clone of B1 ("missed"), picture = the B2 take
 ("vo/fix_b2_a", "After every freeze, I missed swim.", 0.25, [(None, TAKE, {"vtake": "B2", "vin": 1.3})]),
 ("M1", "Round six was already booked. Then I found out why.", 0.2, [(None, TAKE, {})]),
 ("M2", "Freezing, acid and shaving only snap off the top, like picking a dandelion. The root stays under the hard skin, so it grows back.", 0.2,
   [(None, TAKE, {}), ("The root stays", RE / "r03_soil_cutaway.mp4", {})]),
 ("M3", "Here's what I told him. RootOut has four plants, bud. Lemon opens up the hard skin. Tea tree carries it down, up to 8x deeper than a regular cream.", 0.1,
   [(None, TAKE, {}), ("Lemon opens", RE / "r05_skin_door.mp4", {"anim": 1}), ("up to", RE / "r07_towels.mp4", {"in": 0.3})]),
 # M3 says "white sledder": this sentence is her voice cloned from M1 (Seed Audio), under the 3D root clip
 ("vo/fix_m3_c", "Then pokeweed and white cedar break the wart down from the root.", 0.2,   # fix_m3_a with pauses tightened
   [(None, RE / "r08_root_3d.mp4", {"anim": 1}), ("break the wart", RE / "r09_root_dissolve.mp4", {"in": 1.8})]),
 ("M4", "Deep doesn't mean harsh. It's a kids' formula, for ages 4 and up. No acid, no freeze blister, no scar. Just a little cool tingle. Recommended by pediatricians.", 0.2,
   [(None, TAKE, {}), ("No acid", SITE, {"in": 2.6, "crop": "1080:700:0:170"}), ("Just a little", TAKE, {})]),
 ("M5", "Rub the little file over it, twice. Only on the hard top, so it doesn't hurt. Brush the oil on. Then a clear dot seals it in, so it keeps soaking all night.", 0.15,
   [(None, TAKE, {}), ("Only on the", RE / "r10_file_macro.mp4", {"in": 0.2}), ("Brush the oil", RE / "r11_routine.mp4", {"in": 2.0, "captop": 1}),
    ("Then a clear", RE / "r12_brush_dot.mp4", {"in": 3.6})]),
 ("B3", "It doesn't hurt at all.", 0.2, [(None, TAKE, {"croptop": 0.2})]),  # crop: his chin/mouth touch the top edge (L10)
 ("B4", "About two weeks with this little bottle, and it was gone.", 0.15, [(None, TAKE, {})]),  # the take already shows the smooth sole
 ("M6", "Then we did fourteen more nights, so the root's gone too.", 0.2, [(None, TAKE, {})]),
 # M7: the take laughs between the sentences and the bottles fly out after ~4 s -> first sentence on camera, laugh dropped,
 # the money-back line over the real three-bottle clip
 ("M7", "Get yours from the link below. Buy a pair, get a third free.", 0.15, [(None, TAKE, {"captop": 1})]),
 ("M7", "And if it's not gone, you get your money back.", 0.3, [(None, RE / "r15_three_bottles.mp4", {"in": 1.0, "captop": 1})]),
]
if HOOK == "H2":
    ITEMS[0:2] = [("H2m", "Every time we froze my son's wart, it came back faster.", 0.1, [(None, TAKE, {"hook": 1})]),
                  ("H2b", "Five times.", 0.15, [(None, RE / "r01_clinic.mp4", {"in": 0.2})])]
if HOOK == "H3":
    ITEMS[0:2] = [("H3b", "I'm done with my wart!", 0.1, [(None, TAKE, {"hook": 1})]),
                  ("H3b", "They froze it five times. It always came back.", 0.15, [(None, TAKE, {}), ("It always", RE / "r01_clinic.mp4", {"in": 0.2})])]

CUR = {}
def layout():
    t, L = 0.15, []
    for k, (tk, text, gap, vis) in enumerate(ITEMS):
        w = stt(TK(tk)); a, b = find(w, text, CUR.get(tk, 0.0)); CUR[tk] = b
        a = max(0.0, a - 0.06); b = min(dur(TK(tk)), b + 0.12)
        L.append(dict(k=k, take=tk, text=text, a=a, b=b, t0=t, t1=t + b - a, words=w, vis=vis)); t += (b - a) + gap
    return L, t

def at(it, ph):
    a, _ = find(it["words"], ph, it["a"]); return it["t0"] + (a - it["a"]) - 0.05

def render(out, src, o, n, take=None, cin=0.0):
    need = n / FPS
    if src == TAKE:
        z = 1.0 + 0.05 * min(1.0, need / 6)  # slow push-in on talking shots
        if o.get("vtake"): take, cin = o["vtake"], float(o.get("vin", 0)) + cin
        ct = float(o.get("croptop", 0)); pre = f"crop=iw:ih*{1 - ct:.3f}:0:ih*{ct:.3f}," if ct else ""
        vf = (f"{pre}fps={FPS},{COVER},zoompan=z='1+{z - 1:.3f}*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS},"
              f"setsar=1,tpad=stop_mode=clone:stop_duration=1")
        return ff("-ss", f"{cin:.3f}", "-i", TK(take), "-vf", vf, "-frames:v", n, *ENC, out)
    if str(src).endswith(".png"):
        return ff("-loop", "1", "-framerate", str(FPS), "-i", src, "-vf", f"{COVER},zoompan=z='1+0.04*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS},setsar=1",
                  "-frames:v", n, *ENC, out)
    d = dur(src); i0 = o.get("in", 0.0); avail = d - i0
    sp = max(0.8, min(1.4, d / need)) if o.get("anim") else (max(0.75, avail / need) if avail < need else 1.0)
    if o.get("anim"): i0 = 0.0
    crop = f"crop={o['crop']}," if o.get("crop") else ""
    vf = (f"{crop}setpts=PTS/{sp:.4f},fps={FPS},{COVER},zoompan=z='1+0.04*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS},"
          f"setsar=1,tpad=stop_mode=clone:stop_duration=0.5")
    ff("-ss", f"{i0:.3f}", "-i", src, "-vf", vf, "-frames:v", n, *ENC, out)

def build(plan_only=False):
    L, VEND = layout(); TOTAL = VEND + END
    cuts = []
    for it in L:
        for ph, src, o in it["vis"]:
            cuts.append((it["t0"] if ph is None else max(it["t0"], at(it, ph)), src, o, it))
    cuts.sort(key=lambda c: c[0]); cuts.append((VEND, G / "end_card.png", {"end": 1}, None))
    # a talking shot must not run past its take's last frame (that would freeze, L4): pull the next cut earlier
    for k in range(len(cuts) - 1):
        t0, src, o, it = cuts[k]
        if src != TAKE: continue
        tk = o.get("vtake") or it["take"]; base = float(o.get("vin", 0)) if o.get("vtake") else it["a"]
        cin = base + (t0 - it["t0"]); last = t0 + dur(TK(tk)) - cin - 0.07
        if cuts[k + 1][0] > last: cuts[k + 1] = (last,) + cuts[k + 1][1:]
    shots = []
    for k, (t0, src, o, it) in enumerate(cuts):
        t1 = cuts[k + 1][0] if k + 1 < len(cuts) else TOTAL; n = round(t1 * FPS) - round(t0 * FPS)
        cin = max(0.0, (it["a"] if not it["take"].startswith("vo/") else 0.0) + (t0 - it["t0"])) if (src == TAKE and it) else 0.0
        shots.append(dict(n=k + 1, t0=round(t0, 3), t1=round(t1, 3), len=round(t1 - t0, 2), src=str(src) if src != TAKE else f"TAKE:{it['take']}",
                          opts={a: str(b) for a, b in o.items()}))
        if not plan_only:
            out = SH / f"s{k + 1:03d}.mp4"
            render(out, src, o, n, it["take"] if it else None, cin)
    for s in shots: print(f"{s['n']:3d} {s['t0']:7.2f} {s['len']:5.2f}s  {Path(s['src']).name if '/' in s['src'] else s['src']}")
    print(f"total {TOTAL:.2f} s")
    if plan_only: return
    (SH / "l.txt").write_text("".join(f"file 's{s['n']:03d}.mp4'\n" for s in shots))
    ff("-f", "concat", "-safe", "0", "-i", SH / "l.txt", "-c", "copy", OUT / "picture.mp4")
    # voice: each take's own audio, trimmed to its words, levelled the same
    ins, fl, mix = [], [], []
    for j, it in enumerate(L):
        ins += ["-i", TK(it["take"])]  # take video (its audio) or a re-voiced wav
        fl.append(f"[{j}:a]atrim={it['a']:.3f}:{it['b']:.3f},asetpts=N/SR/TB,aresample=48000,aformat=channel_layouts=mono,highpass=f=80,"
                  f"loudnorm=I=-17:TP=-3:LRA=7,afade=t=in:d=0.03,afade=t=out:st={it['b'] - it['a'] - 0.06:.3f}:d=0.06,adelay={int(it['t0'] * 1000)}[a{j}]")
        mix.append(f"[a{j}]")
    fl.append("".join(mix) + f"amix=inputs={len(mix)}:normalize=0,acompressor=threshold=-22dB:ratio=3:attack=5:release=120,apad=whole_dur={TOTAL:.3f}[vo]")
    ff(*ins, "-filter_complex", ";".join(fl), "-map", "[vo]", "-t", f"{TOTAL:.3f}", "-c:a", "pcm_s16le", OUT / "vo.wav")
    json.dump(dict(total=TOTAL, items=[{k: v for k, v in i.items() if k not in ("words", "vis")} for i in L], shots=shots),
              open(OUT / "timeline.json", "w"), indent=1, default=str)
    finish(L, shots, TOTAL, VEND)

def ts(x): return f"{int(x // 3600)}:{int(x % 3600 // 60):02d}:{x % 60:05.2f}"
def captions(L, shots, TOTAL, VEND, path):
    toks = []
    for it in L:
        shown = it["text"].split(); A = [norm(spoken(w)) for w in shown]
        ww = [w for w in it["words"] if it["a"] - 0.05 <= w[1] <= it["b"]]
        # spoken words may be split ("eight times"); match on concatenations
        B = [w[0] for w in ww]; tm = [None] * len(A); bi = 0
        for i, a in enumerate(A):
            for j in range(bi, min(len(B), bi + 4)):
                if "".join(B[bi:j + 1]) == a: tm[i] = (ww[bi][1], ww[j][2]); bi = j + 1; break
        for i in range(len(tm)):
            if tm[i] is None: p = next((tm[j] for j in range(i - 1, -1, -1) if tm[j]), (it["a"], it["a"])); tm[i] = (p[1], p[1] + 0.2)
        for w, (s, e) in zip(shown, tm): toks.append([w, it["t0"] + s - it["a"], it["t0"] + e - it["a"], it["k"]])
    gs, cur = [], []
    for t in toks:
        if cur and (t[3] != cur[-1][3] or t[1] - cur[-1][2] > 0.5): gs.append(cur); cur = []
        cur.append(t)
        if len(cur) >= 3 or (t[0][-1:] in ".,?!" and len(cur) >= 2) or sum(len(x[0]) for x in cur) > 16: gs.append(cur); cur = []
    if cur: gs.append(cur)
    top = [(s["t0"], s["t1"]) for s in shots if s["opts"].get("captop")]
    Lx = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 1080", "PlayResY: 1920", "WrapStyle: 0", "", "[V4+ Styles]",
          "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
          "Style: Cap,Inter ExtraBold,76,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,0,0,0,0,100,100,0,0,1,7,3,2,80,80,520,1",
          "Style: CapTop,Inter ExtraBold,72,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,0,0,0,0,100,100,0,0,1,7,3,8,80,80,260,1",
          "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
    HI = "&H0018A0FF&"  # warm yellow-orange (BGR) for the active word
    for i, g in enumerate(gs):
        gend = min(g[-1][2] + 0.25, gs[i + 1][0][1] - 0.02 if i + 1 < len(gs) else g[-1][2] + 0.25)
        if g[0][1] >= VEND - 0.05: continue
        st = "CapTop" if any(a - 0.05 <= g[0][1] < b for a, b in top) else "Cap"
        for wi, w in enumerate(g):
            s = w[1] - 0.02 if wi else g[0][1] - 0.04; e = g[wi + 1][1] - 0.02 if wi + 1 < len(g) else gend
            txt = " ".join((f"{{\\c{HI}}}{x[0]}{{\\c&HFFFFFF&}}" if q == wi else x[0]) for q, x in enumerate(g))
            pop = "{\\fscx94\\fscy94\\t(0,80,\\fscx100\\fscy100)}" if wi == 0 else ""
            Lx.append(f"Dialogue: 0,{ts(s)},{ts(e)},{st},,0,0,0,,{pop}{txt.upper()}")
    Path(path).write_text("\n".join(Lx) + "\n"); return [t[0] for t in toks]

def finish(L, shots, TOTAL, VEND):
    T = OUT / "fin"; T.mkdir(exist_ok=True)
    words = captions(L, shots, TOTAL, VEND, T / "cap.ass"); json.dump(words, open(T / "caption_words.json", "w"))
    hk = next(s for s in shots if s["opts"].get("hook")); hook_end = min(2.6, next(i for i in L)["t1"] + 0.3)
    ins = ["-i", OUT / "picture.mp4", "-loop", "1", "-framerate", "30", "-t", f"{hook_end:.2f}", "-i", G / f"hook_{HOOK.lower()}.png"]
    fl = [f"[1]format=rgba,fade=t=out:st={hook_end - 0.15:.2f}:d=0.15:alpha=1[hk]",
          f"[0][hk]overlay=x=(W-w)/2:y='170+max(0,40*(1-t/0.15))':eof_action=pass[v1]",
          f"[v1]subtitles={T / 'cap.ass'}:fontsdir=/usr/share/fonts/opentype/inter,noise=alls=4:allf=t,format=yuv420p[vout]"]
    ff(*ins, "-filter_complex", ";".join(fl), "-map", "[vout]", "-t", f"{TOTAL:.3f}", "-c:v", "libx264", "-crf", "20", "-maxrate", "9M",
       "-bufsize", "18M", "-preset", "medium", "-r", "30", T / "picture_fin.mp4")
    # music: runs to the last frame, ducked under the voice, lifted on the end card, short fade on the final frame only
    md = dur(MUSIC); start = 6.0 if md - 6.0 > TOTAL else 0.0
    fl = [f"[1:a]atrim={start}:{start + TOTAL:.3f},asetpts=N/SR/TB,aresample=48000,volume=0.22,"
          f"volume='if(gte(t,{VEND:.2f}),2.6,1)':eval=frame,afade=t=out:st={TOTAL - 0.5:.2f}:d=0.5[mu]",
          "[0:a]asplit=2[v][sc]", "[mu][sc]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=350[mud]",
          f"[v][mud]amix=inputs=2:normalize=0,alimiter=limit=0.95,loudnorm=I=-14:TP=-1.5:LRA=9,apad=whole_dur={TOTAL:.3f}[aout]"]
    ff("-i", OUT / "vo.wav", "-i", MUSIC, "-filter_complex", ";".join(fl), "-map", "[aout]", "-t", f"{TOTAL:.3f}", "-ar", "48000", "-c:a", "pcm_s16le", T / "mix.wav")
    ff("-i", T / "picture_fin.mp4", "-i", T / "mix.wav", "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
       "-movflags", "+faststart", "-map_metadata", "-1", "-shortest", FINAL)
    print("wrote", FINAL, f"{dur(FINAL):.2f} s")

if __name__ == "__main__":
    build("--plan" in sys.argv)
