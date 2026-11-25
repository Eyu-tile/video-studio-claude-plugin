#!/usr/bin/env python3
"""RootOut Set 7 "Things I wish I knew": build H1/H2/H3 from the 23 Nov mom takes + reused/new b-roll.

Layout (swipe Azure #007): scene on top (1080x1200), mom inset below (1080x720, her face cropped from the
vertical selfie). 'full' = mom full frame, 'bfull' = b-roll full frame under her voice.
Usage: python3 build7.py H1 [--preview]
"""
import json, subprocess, sys, os
from pathlib import Path

P = Path(__file__).resolve().parents[4] / "projects/rootout-set7"
RAW, WORK, OUT = P / "raw", P / "work", P / "out"
FPS, W, H, TOP = 30, 1080, 1920, 1200
HOOK = sys.argv[1] if len(sys.argv) > 1 else "H1"
PREVIEW = "--preview" in sys.argv

TAKES = {  # name: (file, transcript)
    "h1": "prev/h1a_a3bb28d0", "h2": "prev/h2b_00c5230d", "h3": "prev/h3b_c1a8838d",
    "r1": "prev/r1a_aa43466d", "r2": "prev/r2b_abf890fe", "r3": "prev/r3a_002dcd0d", "r4": "prev/r4a_8a0f08eb",
    "bonus": "prev/bonus_b_098057df", "use": "prev/use_b_bf27f921", "offer": "prev/offer_b_4c1def64",
    "dad": "prev/dad_1868c6b5", "mom1": "prev/mom1b_ad40b24e", "mom2": "prev/mom2b_fb3d68c7",
}
TR = {k: f"{Path(v).name}_lg" if (WORK / f"tr/{Path(v).name}_lg.json").exists() else Path(v).name for k, v in TAKES.items()}

# shots: (t_local_start, layout, source, source_in). Each shot runs to the next start or the take end.
B = lambda n: f"reuse/{n}"
HOOKS = {
    "H1": ("h1", [(0, "inset", "new/g1_bath", 0.3)]),
    "H2": ("h2", [(0, "full", None, 0)]),
    "H3": ("h3", [(0, "inset", B("scrub"), 0.2), (3.8, "full", None, 0)]),
}
BODY = [
    ("r1", [(0, "inset", B("sole"), 0), (2.85, "inset", "SPLIT", 0), (4.25, "inset", "new/g2_pick", 0.2),
            (6.9, "inset", B("footprints"), 0), (8.9, "inset", "new/g4_aisle", 0.3), (11.4, "inset", B("toponly"), 0),
            (14.15, "inset", B("dsnap"), 0.4), (15.25, "inset", B("soilcut"), 0.6)]),
    ("r2", [(0, "inset", B("dwater"), 0.5), (2.8, "inset", B("rootstill"), 1.5), (4.0, "inset", B("plants"), 1.2),
            (6.55, "inset", B("hero"), 1.0), (7.8, "inset", B("lemon3d"), 0.8), (9.75, "inset", B("carry3d"), 0),
            (13.15, "inset", B("root3d"), 0.6), (16.25, "inset", B("towels"), 0.3), (19.7, "inset", B("lampoff"), 0.8)]),
    ("r3", [(0, "inset", B("nightbook"), 0.5), (2.65, "inset", B("feetup"), 0.5), (3.8, "inset", B("lemon"), 0.6), (5.25, "inset", B("pokeweed"), 0.6),
            (8.0, "inset", B("bin"), 1.0), (9.9, "inset", B("pillow"), 0.8), (11.2, "inset", B("clinicdesk"), 1.0)]),
    ("r4", [(0, "full", None, 0), (1.55, "inset", B("wartback"), 0.3), (4.8, "inset", B("nightkit"), 0.6),
            (7.85, "inset", B("heels"), 0.5), (11.0, "inset", B("hallway"), 0.8), (13.0, "full", None, 0),
            (14.0, "inset", B("sister"), 0.8), (16.2, "inset", B("clearsole"), 0.6), (18.7, "full", None, 0),
            (20.0, "inset", "SOCCER", 0.8)]),
    ("bonus", [(0, "full", None, 0), (1.45, "inset", B("socksbed"), 1.0), (2.85, "inset", B("smoothsole"), 0.5),
               (5.0, "inset", B("nightdawn"), 0.8), (7.5, "inset", B("plus14"), 0.4)]),
    ("use", [(0, "full", None, 0), (2.6, "bfull", B("shelf"), 0), (6.55, "bfull", B("brushdot_b"), 0.3),
             (8.0, "bfull", B("file"), 1.0), (9.95, "bfull", B("brushdot"), 2.2), (12.4, "bfull", B("lightsout"), 0.8)]),
    ("dad", [(0, "full", None, 0)]),
    ("mom1", [(0, "full", None, 0)]),
    ("mom2", [(0, "full", None, 0)]),
    ("offer", [(0, "inset", B("threebottles"), 0.5), (4.25, "full", None, 0)]),
]
END_LEN = 2.6


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(" ".join(map(str, cmd))[:600]); print(r.stderr[-1500:]); sys.exit(1)
    return r.stdout


def dur(f):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)]))


def words(take):
    return json.loads((WORK / f"tr/{TR[take]}.json").read_text())["words"]


def take_range(take):
    w = words(take)
    return 0.0, min(w[-1]["e"] + 0.28, dur(RAW / f"{TAKES[take]}.mp4"))


COVER = lambda w, h: f"scale={w}:{h}:force_original_aspect_ratio=increase:flags=lanczos,crop={w}:{h}"


def broll_chain(src, sin, L, w, h):
    """input args + filter for a b-roll source covering w x h for L seconds (slowed to >=0.75x if short)."""
    if src == "SPLIT":  # callus vs wart, two stills side by side, slow push-in
        a, b = RAW / "new/g3_callus_4be26c88.png", RAW / "new/g2_pick_77c3c4aa.png"
        n = int(L * FPS) + 2
        z = lambda: f"scale={w}:-2,crop={w//2}:{h},zoompan=z='1+0.06*on/{n}':d={n}:s={w//2}x{h}:fps={FPS}"
        return (["-loop", "1", "-i", str(a), "-loop", "1", "-i", str(b)],
                f"[{{i}}:v]{z()}[sa];[{{j}}:v]{z()}[sb];[sa][sb]hstack,drawbox=x={w//2-3}:y=0:w=6:h={h}:color=white@0.9:t=fill")
    if src == "SOCCER":  # waist-down crop: no faces (L10)
        f = RAW / "reuse/soccer.mp4"
        return (["-ss", f"{sin}", "-i", str(f)], f"[{{i}}:v]crop=936:1040:40:880,{COVER(w, h)}")
    f = RAW / f"{src}.mp4"
    avail = dur(f) - sin - 0.05
    speed = 1.0
    if avail < L:
        speed = avail / L
        if speed < 0.75:
            sys.exit(f"{src}: {L:.2f}s needed, {avail:.2f}s available (speed {speed:.2f} < 0.75)")
    return (["-ss", f"{sin}", "-i", str(f)], f"[{{i}}:v]setpts=PTS/{speed:.4f},{COVER(w, h)}")


def render_piece(idx, take, t0, L, layout, src, sin):
    out = WORK / f"pieces/{idx:03d}.mp4"
    tf = RAW / f"{TAKES[take]}.mp4"
    args, fc = [], []
    if layout in ("inset", "full"):
        args += ["-ss", f"{t0}", "-i", str(tf)]
        mom = f"[0:v]scale={W}:{H}:flags=lanczos"
    k = 1 if layout in ("inset", "full") else 0
    if layout == "full":
        fc.append(f"{mom}[v]")
    else:
        h = TOP if layout == "inset" else H
        a, chain = broll_chain(src, sin, L, W, h)
        args += a
        nin = 2 if src == "SPLIT" else 1
        chain = chain.replace("{i}", str(k)).replace("{j}", str(k + 1))
        if layout == "inset":
            fc.append(f"{chain}[top]")
            # her face + chin + a bit of shoulder: 900 px of the selfie fit into 720 px, sides filled with a soft blur
            fc.append(f"{mom},crop={W}:900:0:330,split[m1][m2];[m1]scale={W}:{H-TOP},boxblur=20:2,eq=brightness=-0.05[bg];"
                      f"[m2]scale=-2:{H-TOP}[fg];[bg][fg]overlay=(W-w)/2:0[bot]")
            fc.append("[top][bot]vstack,drawbox=x=0:y=1196:w=1080:h=8:color=white@0.95:t=fill[v]")
        else:
            fc.append(f"{chain}[v]")
    fc[-1] = fc[-1].replace("[v]", f",fps={FPS},format=yuv420p,trim=duration={L:.4f},setpts=PTS-STARTPTS[v]")
    q = ["-c:v", "libx264", "-preset", "veryfast" if PREVIEW else "medium", "-crf", "23" if PREVIEW else "17"]
    run(["ffmpeg", "-v", "error", "-y", *args, "-filter_complex", ";".join(fc), "-map", "[v]", "-an",
         "-frames:v", str(round(L * FPS)), *q, "-r", str(FPS), "-video_track_timescale", "15360", str(out)])
    return out


def main():
    (WORK / "pieces").mkdir(parents=True, exist_ok=True); OUT.mkdir(exist_ok=True)
    plan = [HOOKS[HOOK]] + BODY
    timeline, pieces, audio, capwords, t = [], [], [], [], 0.0
    layouts, segs = [], []
    for take, shots in plan:
        a, b = take_range(take)
        frames_total = round((b - a) * FPS)
        b = a + frames_total / FPS
        for i, (s, lay, src, sin) in enumerate(shots):
            f0 = round(s * FPS)
            f1 = round(shots[i + 1][0] * FPS) if i + 1 < len(shots) else frames_total
            L = (f1 - f0) / FPS
            pieces.append(render_piece(len(pieces), take, a + f0 / FPS, L, lay, src, sin))
            layouts.append((t + f0 / FPS, t + f1 / FPS, lay))
            srcf = str(RAW / f"{TAKES[take]}.mp4") if lay == "full" else str(RAW / ("reuse/soccer" if src == "SOCCER" else ("new/g3_callus_4be26c88" if src == "SPLIT" else src)) ) + ("" if src == "SPLIT" else ".mp4")
            segs.append({"src": srcf, "start": round(sin if lay != "full" else a + f0 / FPS, 3),
                         "end": round((sin if lay != "full" else a + f0 / FPS) + L, 3), "layout": lay, "voice": take})
        audio.append((take, a, b))
        for w in words(take):
            capwords.append({"w": w["w"], "s": t + w["s"] - a, "e": t + w["e"] - a})
        timeline.append((take, t, b - a)); t += b - a
    # end card: real bottle on the pedestal, text in code
    ec = WORK / f"pieces/{len(pieces):03d}.mp4"
    txt = lambda s, y, size, c="0x0B2A5B": (f"drawtext=fontfile=/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf:"
                                            f"text='{s}':fontsize={size}:fontcolor={c}:x=(w-text_w)/2:y={y}")
    pack = P.parents[1] / "library/RootOut/brand/images/pdp/A08-tier-90-nights-3-pack.jpg"  # real PDP photo (L1)
    n = round(END_LEN * FPS)
    run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-i", str(pack), "-filter_complex",
         f"color=c=white:s={W}x{H}:r={FPS}:d={END_LEN}[bg];"
         f"[0:v]scale=1000:-2,zoompan=z='1+0.05*on/{n}':d={n}:s=1000x1000:fps={FPS}[p];"
         f"[bg][p]overlay=(W-w)/2:620,"
         f"{txt('Not the top. The root.', 330, 80)},{txt('Buy 2, get 1 free · 90-day money-back', 460, 48, '0xE04E18')},"
         f"format=yuv420p,trim=duration={END_LEN},setpts=PTS-STARTPTS[v]",
         "-map", "[v]", "-frames:v", str(n), "-c:v", "libx264", "-crf", "18", "-r", str(FPS), "-video_track_timescale", "15360", str(ec)])
    pieces.append(ec); layouts.append((t, t + END_LEN, "end"))
    total = t + END_LEN
    lst = WORK / "pieces/list.txt"; lst.write_text("".join(f"file '{p}'\n" for p in pieces))
    vid = WORK / f"video_{HOOK}.mp4"
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(vid)])

    # ---- audio: the takes' own voices, patch "drop" -> "dot" in the routine line (her lips are off screen there)
    parts, inputs, fc = [], [], []
    for n, (take, a, b) in enumerate(audio):
        inputs += ["-i", str(RAW / f"{TAKES[take]}.mp4")]
        if take == "use":
            # measured from the waveform (whisper's word edges clip the "d" and the next word)
            d = {"s": 11.72, "e": 12.04}; rw = {"s": 20.28, "e": 20.60}
            dlen = d["e"] - d["s"]
            inputs += ["-i", str(RAW / f"{TAKES['r2']}.mp4")]
            m = len(inputs) // 2 - 1
            fc.append(f"[{m-1}:a]atrim={a}:{d['s']:.3f},asetpts=PTS-STARTPTS,afade=t=out:st={d['s']-a-0.02:.3f}:d=0.02[u1]")
            fc.append(f"[{m}:a]atrim={rw['s']:.3f}:{rw['e']:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.01,afade=t=out:st={rw['e']-rw['s']-0.012:.3f}:d=0.012,apad=whole_dur={dlen:.3f}[ud]")
            fc.append(f"[{m-1}:a]atrim={d['e']:.3f}:{b:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.02[u2]")
            fc.append(f"[u1][ud][u2]concat=n=3:v=0:a=1,aresample=48000[a{n}]")
        else:
            m = len(inputs) // 2 - 1
            fc.append(f"[{m}:a]atrim={a}:{b},asetpts=PTS-STARTPTS,aresample=48000[a{n}]")
        parts.append(f"[a{n}]")
    fc.append(f"{''.join(parts)}concat=n={len(parts)}:v=0:a=1,apad=whole_dur={total:.3f}[vo]")
    # music to the last frame, lifted on the end card, short fade on the final frame only (L6)
    inputs += ["-i", str(RAW / "music_wholesome.mp3")]
    m = len(inputs) // 2 - 1
    fc.append(f"[{m}:a]atrim=0:{total:.3f},asetpts=PTS-STARTPTS,aresample=48000,"
              f"volume='if(gte(t,{t:.2f}),0.55,0.16)':eval=frame,afade=t=out:st={total-0.4:.2f}:d=0.4[mu]")
    fc.append(f"[vo]apad=pad_dur=4,loudnorm=I=-16:TP=-2:LRA=11,aresample=48000,atrim=0:{total:.3f}[vn];[vn][mu]amix=inputs=2:normalize=0:duration=first,alimiter=limit=0.89[aout]")
    mix = WORK / f"audio_{HOOK}.wav"
    run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", "[aout]", str(mix)])

    # ---- captions: bold word-by-word, active word yellow (L5); y depends on the layout under it
    fix = {"root": "RootOut", "drop": "dot", "wort": "wart", "sons": "son's"}
    cw = []
    for i, w in enumerate(capwords):
        s = w["w"].strip(); low = s.lower().strip(".,?!")
        if low == "out" and cw and cw[-1]["w"].startswith("RootOut"): continue
        if low in fix and not (low == "root" and not (i + 1 < len(capwords) and capwords[i + 1]["w"].lower().startswith("out"))):
            s = fix[low] + ("." if s.endswith(".") and not fix[low].endswith(".") else "")
        cw.append({**w, "w": s})
    write_ass(cw, layouts, total)
    out = OUT / f"WilloMD_RootOut_Set7_{HOOK}_9x16_v1{'_preview' if PREVIEW else ''}.mp4"
    ass = WORK / f"captions_{HOOK}.ass"
    run(["ffmpeg", "-v", "error", "-y", "-i", str(vid), "-i", str(mix), "-filter_complex",
         f"[0:v]ass={ass}:fontsdir=/usr/share/fonts/opentype/inter,noise=alls=4:allf=t[v]", "-map", "[v]", "-map", "1:a",
         "-c:v", "libx264", "-preset", "veryfast" if PREVIEW else "slow", "-crf", "22" if PREVIEW else "18",
         "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "-map_metadata", "-1", "-shortest", str(out)])
    json.dump({"hook": HOOK, "total": total, "timeline": timeline, "layouts": layouts, "segments": segs}, open(WORK / f"edl_{HOOK}.json", "w"), indent=1)
    print(out, f"{total:.2f}s")


HOOK_TEXT = {"H1": "Things I wish I knew when I found his first wart", "H2": 'Just googled "is this a wart?"',
             "H3": "Found his first wart. Scrubbed the whole bathroom."}


def ts(x):
    x = max(0, x); return f"{int(x//3600)}:{int(x%3600//60):02d}:{x%60:05.2f}"


def write_ass(cw, layouts, total):
    hdr = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Inter ExtraBold,78,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,0,0,1,6,2,2,60,60,0,1
Style: Hook,Inter ExtraBold,62,&H005B2A0B,&H005B2A0B,&H00FFFFFF,&H00FFFFFF,1,0,0,0,100,100,0,0,3,18,0,8,70,70,170,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    ev = [f"Dialogue: 1,{ts(0)},{ts(3.0)},Hook,,0,0,0,,{HOOK_TEXT[HOOK]}"]
    def ypos(t):
        for a, b, lay in layouts:
            if a <= t < b:
                return None if lay == "end" else (1150 if lay == "inset" else 1480)
        return 1480
    # group 1-3 words, break on punctuation
    groups, g = [], []
    for w in cw:
        g.append(w)
        if len(g) == 3 or w["w"][-1:] in ".,?!" or (len(g) >= 2 and len(w["w"]) > 9):
            groups.append(g); g = []
    if g: groups.append(g)
    for gi, g in enumerate(groups):
        end_g = groups[gi + 1][0]["s"] if gi + 1 < len(groups) else g[-1]["e"] + 0.3
        end_g = min(end_g, g[-1]["e"] + 0.6)
        for k, w in enumerate(g):
            s = w["s"]; e = g[k + 1]["s"] if k + 1 < len(g) else end_g
            y = ypos(s)
            if y is None or e <= s: continue
            txt = " ".join(("{\\c&H00D4FF&}" + x["w"].upper().strip(",") + "{\\c&HFFFFFF&}") if j == k else x["w"].upper().strip(",")
                           for j, x in enumerate(g))
            ev.append(f"Dialogue: 0,{ts(s)},{ts(e)},Cap,,0,0,0,,{{\\pos(540,{y})}}{txt}")
    (WORK / f"captions_{HOOK}.ass").write_text(hdr + "\n".join(ev) + "\n")


if __name__ == "__main__":
    main()
