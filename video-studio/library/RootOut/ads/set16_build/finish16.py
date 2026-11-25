#!/usr/bin/env python3
"""Set 16 finish: body (voice) -> ad. Music bed ducked under the voice and lifted where nobody speaks, audible to the last
frame (L6: only a short fade on the final frame); bold word-by-word captions with the active word highlighted (L5), kept
off the product, the 3D/graphics and the hook title; hook title; light phone-camera finish; -14 LUFS / TP -2.
Usage: finish16.py h1|h2|h3 [--preview] -> projects/rootout-set16/out/RootOut_S16_<HOOK>_vN.mp4"""
import json, re, subprocess, sys
from pathlib import Path

P = Path("/home/user/video-studio-claude-plugin/video-studio/projects/rootout-set16")
HOOK = sys.argv[1]; PREVIEW = "--preview" in sys.argv
VS = "/home/user/video-studio-claude-plugin/plugins/video-studio/bin/vs"
body, tl = P / f"work/{HOOK}_body.mp4", json.load(open(P / f"work/{HOOK}_timeline.json"))
MUSIC = P / "raw/music/bed_3104bae9.mp3"; T = P / f"work/finish_{HOOK}"; T.mkdir(parents=True, exist_ok=True)
OUT = P / "out"; OUT.mkdir(exist_ok=True)


def run(a):
    r = subprocess.run(["ffmpeg", "-y", "-v", "error", *map(str, a)], capture_output=True, text=True)
    if r.returncode: sys.exit(r.stderr)


D = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(body)]))

# captions from the real audio (word timings), spelled to the script
if not (T / "tx.json").exists():
    subprocess.run([VS, "transcribe", str(body), "-o", str(T / "tx"), "--lang", "en", "--model", "medium",
                    "--prompt", "RootOut, plantar wart, pokeweed, white cedar, tea tree, apple cider vinegar"], capture_output=True)
words = json.load(open(T / "tx.json"))["words"]
FIX = {"planter": "plantar", "ward": "wart", "warts": "warts", "rootout": "RootOut", "route": "root", "pokeweed": "pokeweed",
       "kid's": "kids'", "8x": "8x", "eight": "8x"}
toks, i = [], 0
while i < len(words):
    w = words[i]["w"].strip(); s, e = words[i]["s"], words[i]["e"]
    nxt = words[i + 1]["w"].strip().lower() if i + 1 < len(words) else ""
    if re.sub(r"[^a-z]", "", w.lower()) == "root" and nxt.startswith("out"):
        toks.append(["RootOut" + re.sub(r"^out", "", nxt), s, words[i + 1]["e"]]); i += 2; continue
    core = re.sub(r"[^\w']", "", w).lower()
    if core == "eight" and nxt.startswith("times"):
        toks.append(["8x", s, words[i + 1]["e"]]); i += 2; continue
    if core in FIX: w = w.lower().replace(core, FIX[core]) if core != "kid's" or nxt.startswith("formula") else w
    toks.append([w, s, e]); i += 1
groups, cur = [], []
for t in toks:
    cur.append(t)
    if len(cur) >= 3 or (t[0][-1:] in ".,?!" and len(cur) >= 1):
        groups.append(cur); cur = []
if cur: groups.append(cur)


def ts(x):
    return f"{int(x // 3600)}:{int(x % 3600 // 60):02d}:{x % 60:05.2f}"


ZONE = {}  # caption height per shot: product/graphics stay clear
for s in tl:
    n = s["src"]
    if n in ("m0_sidecut", "skin_m1", "root_x6", "root_m2", "soil_cut", "dand_snap"): ZONE[(s["start"], s["end"])] = 130
    elif n in ("depth_sink", "depth_label"): ZONE[(s["start"], s["end"])] = 1470
    elif n == "endcard": ZONE[(s["start"], s["end"])] = None
HOOK_END = 2.8
ass = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 1080", "PlayResY: 1920", "", "[V4+ Styles]",
       "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, "
       "StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
       "Style: Cap,Inter ExtraBold,74,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,7,2,2,80,80,620,1",
       "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
for j, g in enumerate(groups):
    s = g[0][1]; e = groups[j + 1][0][1] if j + 1 < len(groups) and groups[j + 1][0][1] - g[-1][2] < 0.6 else g[-1][2] + 0.2
    mv = 0
    for (a, b), z in ZONE.items():
        if a <= s < b:
            mv = -1 if z is None else z
        elif s < a < e: e = a - 0.02  # never carry a caption across into a graphic, the 3D or the end card
    if mv == -1: continue
    for k, w in enumerate(g):  # active word highlighted (brand orange), the rest white
        ws = w[1]; we = g[k + 1][1] if k + 1 < len(g) else e
        if we <= ws: continue
        txt = " ".join(("{\\c&H184EE0&}" + x[0].rstrip(",") + "{\\c&HFFFFFF&}") if x is w else x[0].rstrip(",") for x in g)
        ass.append(f"Dialogue: 0,{ts(ws)},{ts(min(we, D))},Cap,,0,0,{mv},,{txt}")
(T / "captions.ass").write_text("\n".join(ass) + "\n")

# music: ducked under voice, lifted when nobody speaks; full on the end card; 0.4 s fade on the last frame only
endst = next(s["start"] for s in tl if s["src"] == "endcard")
fc = (f"[1:a]atrim=1.2:{D + 1.2:.2f},asetpts=PTS-STARTPTS,volume=0.30,"
      f"volume='if(gte(t,{endst:.2f}),1.8,1)':eval=frame,afade=t=out:st={D - 0.4:.2f}:d=0.4[m];"
      f"[0:a]asplit[vo][sc];[m][sc]sidechaincompress=threshold=0.02:ratio=5:attack=30:release=350[md];"
      f"[vo][md]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-2:LRA=9[a];"
      f"[0:v][2:v]overlay=0:0:enable='lt(t,{HOOK_END})'[vh];[vh]ass={T / 'captions.ass'},noise=alls=3:allf=t,vignette=PI/6,unsharp=5:5:0.3[v]")
vers = sorted(OUT.glob(f"RootOut_S16_{HOOK.upper()}_v*.mp4"))
n = (int(re.search(r"_v(\d+)", vers[-1].name).group(1)) + 1) if vers else 1
out = OUT / f"RootOut_S16_{HOOK.upper()}_v{n}{'_preview' if PREVIEW else ''}.mp4"
q = ["-crf", "26", "-preset", "veryfast"] if PREVIEW else ["-crf", "19", "-preset", "slow", "-maxrate", "10M", "-bufsize", "20M"]
run(["-i", body, "-i", MUSIC, "-i", P / f"assets/graphics/hook_{HOOK}.png", "-filter_complex", fc, "-map", "[v]", "-map", "[a]",
     "-c:v", "libx264", *q, "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
     "-map_metadata", "-1", "-movflags", "+faststart", out])
print(out, round(D, 2), "s,", len(groups), "caption groups")
