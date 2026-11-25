#!/usr/bin/env python3
"""Set 16 builder: H1/H2/H3 body timeline -> body mp4 (voice only) + timeline json.
Cuts sit on her word timings (work/tr/*.json from vs transcribe). On-camera lines use the Seedance take's own audio
(native, lip-synced); lines under b-roll use the same ElevenLabs Cora line. Each b-roll source once (L4), no held frames:
stills get a continuous push-in. Usage: build16.py [h1|h2|h3]"""
import json, subprocess, sys
from pathlib import Path

P = Path("/home/user/video-studio-claude-plugin/video-studio/projects/rootout-set16")
R, W = P / "raw", P / "work/build"; W.mkdir(parents=True, exist_ok=True)
G = P / "assets/graphics"; IMG = Path("/tmp/claude-0/-home-user-video-studio-claude-plugin/c7e1702a-a22e-5d06-aae3-d1a931e20ed5/scratchpad/set16/img")
HOOK = sys.argv[1] if len(sys.argv) > 1 else "h1"


def ff(*a):
    r = subprocess.run(["ffmpeg", "-y", "-v", "error", *map(str, a)], capture_output=True, text=True)
    if r.returncode: sys.exit(r.stderr)


def src(name):
    for d in ("takes", "reuse", "broll"):
        if (R / d / f"{name}.mp4").exists(): return R / d / f"{name}.mp4"
    if (G / f"{name}.mp4").exists(): return G / f"{name}.mp4"
    if (IMG / f"{name}.png").exists(): return IMG / f"{name}.png"
    sys.exit(f"missing source {name}")


VF = "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1"


def shot(i, name, s_in, dur):
    f, o = src(name), W / f"{HOOK}_{i:02d}_{name}.mp4"
    if f.suffix == ".png":  # still -> slow continuous push-in (never a held frame)
        n = int(dur * 30) + 1
        ff("-loop", "1", "-i", f, "-t", f"{dur:.3f}", "-vf",
           f"scale=2160:-2,zoompan=z='1+0.10*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1920:fps=30,setsar=1",
           "-an", "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", o)
    else:
        ff("-ss", f"{s_in:.3f}", "-i", f, "-t", f"{dur:.3f}", "-vf", VF, "-an", "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", o)
    return o


def apiece(i, f, a, b):
    o = W / f"{HOOK}_a{i:02d}.wav"
    ff("-ss", f"{a:.3f}", "-to", f"{b:.3f}", "-i", f, "-af", "aresample=48000,aformat=channel_layouts=stereo,loudnorm=I=-16:TP=-2:LRA=7", "-ar", "48000", o)
    return o


T = lambda n: R / "takes" / f"{n}.mp4"
V = lambda n: R / "vo" / f"{n}.mp3"

# blocks: (audio pieces [(file, in, out, rel_start)], shots [(src, src_in, rel_start, rel_end)], gap_after)
HOOKS = {
    "h1": ([(T("M1_h1"), 0, 7.30, 0)], [("M1_h1", 0, 0, 7.30)]),
    "h2": ([(T("M1b_h2"), 0, 6.25, 0)], [("M1b_h2", 0, 0, 6.25)]),
    "h3": ([(T("M1c_h3"), 0, 7.70, 0)], [("M1c_h3", 0, 0, 7.70)]),
}
tried_start = 0 if HOOK != "h2" else 1.88  # H2 already says "We tried everything."
BLOCKS = [
    (*HOOKS[HOOK], 0.20),
    ([(V("a02"), tried_start, 10.19, 0)],
     [s for s in [("pad_peel", 0.5, 0, 2.85), ("kit_shelf", 0.3, 2.85, 4.20), ("G11_vinegar", 0.2, 4.20, 5.95),
                  ("sole", 0.4, 5.95, 8.50), ("e1", 0, 8.50, 10.19)]] if HOOK != "h2" else
     [("pad_peel", 1.4, 0, 2.85 - 1.88 + 0.6), ("kit_shelf", 0.3, 2.85 - 1.88 + 0.6, 4.20 - 1.88), ("G11_vinegar", 0.2, 4.20 - 1.88, 5.95 - 1.88),
      ("sole", 0.4, 5.95 - 1.88, 8.50 - 1.88), ("e1", 0, 8.50 - 1.88, 10.19 - 1.88)], 0.30),
    ([(T("M3_q1"), 0, 5.00, 0)], [("M3_q1", 0, 0, 5.00)], 0.25),
    ([(T("M5a_yard"), 0, 3.85, 0), (V("a04"), 3.85, 31.95, 3.85)],
     [("M5a_yard", 0, 0, 3.85), ("dand_snap", 0, 3.85, 5.90), ("soil_cut", 0.2, 5.90, 9.65), ("G12_yard_bottle", 1.9, 9.65, 11.75),
      ("m0_sidecut", 0, 11.75, 13.95), ("skin_m1", 0, 13.95, 18.35), ("depth_sink", 0, 18.35, 21.35), ("depth_label", 0, 21.35, 24.15),
      ("root_x6", 0, 24.15, 29.15), ("root_m2", 2.2, 29.15, 31.95)], 0.35),
    ([(T("M6_safe"), 0, 7.95, 0), (V("a05"), 7.95, 11.96, 7.95)], [("M6_safe", 0, 0, 7.95), ("e2", 0, 7.95, 11.96)], 0.35),
    ([(V("a06"), 0, 12.49, 0)],
     [("file", 0, 0, 4.0), ("brush", 2.0, 4.0, 6.6), ("dot", 0.6, 6.6, 10.4), ("G13_bedroom", 2.4, 10.4, 12.49)], 0.30),
    ([(T("M9_week"), 0, 3.30, 0), (V("a07"), 3.30, 8.55, 3.30), (T("M11_root"), 0, 5.40, 8.55)],
     [("M9_week", 0, 0, 3.30), ("G14_flake", 1.0, 3.30, 5.75), ("G15_smooth", 0.6, 5.75, 8.55), ("M11_root", 0, 8.55, 13.95)], 0.30),
    ([(T("M12_run"), 0, 4.00, 0)], [("M12_run", 0, 0, 4.00)], 0.30),
    ([(T("M13_close"), 0, 7.05, 0)], [("M13_close", 0, 0, 7.05)], 0.0),
]

t, segs, apieces, tl, used = 0.0, [], [], [], set()
for bi, (aud, shots, gap) in enumerate(BLOCKS):
    for (f, a, b, rel) in aud:
        apieces.append((apiece(len(apieces), f, a, b), t + rel))
    for k, (name, s_in, r0, r1) in enumerate(shots):
        r1e = r1 + (gap if k == len(shots) - 1 else 0)  # the last shot covers the breath after the block
        if name in used and not name.startswith("M"): sys.exit(f"source used twice: {name}")
        used.add(name)
        segs.append(shot(len(segs), name, s_in, r1e - r0)); tl.append({"block": bi, "src": name, "start": round(t + r0, 3), "end": round(t + r1e, 3)})
    t += max(r1 for (_, _, _, r1) in shots) + gap
end = G / "endcard.mp4"; segs.append(end); tl.append({"block": len(BLOCKS), "src": "endcard", "start": round(t, 3), "end": round(t + 3.2, 3)})
total = t + 3.2

lst = W / f"{HOOK}_list.txt"; lst.write_text("".join(f"file '{s}'\n" for s in segs))
vid = W / f"{HOOK}_video.mp4"; ff("-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", vid)
ins, fc = [], []
for i, (f, st) in enumerate(apieces):
    ins += ["-i", f]; fc.append(f"[{i}:a]adelay={int(st * 1000)}|{int(st * 1000)}[p{i}]")
fc.append("".join(f"[p{i}]" for i in range(len(apieces))) + f"amix=inputs={len(apieces)}:normalize=0,apad,atrim=0:{total:.3f}[a]")
voice = W / f"{HOOK}_voice.wav"; ff(*ins, "-filter_complex", ";".join(fc), "-map", "[a]", voice)
body = P / f"work/{HOOK}_body.mp4"
ff("-i", vid, "-i", voice, "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", body)
(P / f"work/{HOOK}_timeline.json").write_text(json.dumps(tl, indent=1))
print(body, round(total, 2), "s,", len(segs), "shots")
