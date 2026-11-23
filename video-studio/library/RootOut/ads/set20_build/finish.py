#!/usr/bin/env python3
"""Set 20 finish: hook + body -> one ad with music bed (ducked), captions in the middle safe zone, light phone-camera
finish, loudness -14 LUFS / TP -2. Usage: finish.py <hook.mp4> <out.mp4>"""
import json, re, subprocess, sys
from pathlib import Path

P = Path(__file__).resolve().parent.parent; T = P / "work/finish"; T.mkdir(parents=True, exist_ok=True)
hook, out = Path(sys.argv[1]), Path(sys.argv[2])
VS = "/home/user/video-studio-claude-plugin/plugins/video-studio/bin/vs"
MUSIC = P / "assets/music/Wholesome.mp3"


def run(a):
    r = subprocess.run(["ffmpeg", "-y", "-v", "error", *a], capture_output=True, text=True)
    if r.returncode: sys.exit(r.stderr)


def dur(f):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)]))


# 1. hook + body, same format
cat = T / "cat.mp4"
run(["-i", str(hook), "-i", str(P / "work/body/body.mp4"), "-filter_complex",
     "[0:v]fps=30,setsar=1[v0];[0:a]aresample=48000,aformat=channel_layouts=stereo[a0];"
     "[1:v]fps=30,setsar=1[v1];[1:a]aresample=48000,aformat=channel_layouts=stereo[a1];"
     "[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]", "-map", "[v]", "-map", "[a]",
     "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", str(cat)])
D = dur(cat)

# 2. captions from the real audio (word timings), spelling fixed to the script
tx = T / "tx"
if not (T / "tx.json").exists():
    subprocess.run([VS, "transcribe", str(cat), "-o", str(tx), "--lang", "en", "--model", "medium",
                    "--prompt", "RootOut, plantar wart, callus, pumice, pumicing, pokeweed, white cedar, tea tree"], capture_output=True)
words = json.load(open(T / "tx.json"))["words"]
FIX = {"root out": "RootOut", "rootout": "RootOut", "planter": "plantar", "callous": "callus", "promising": "pumicing",
       "route": "root", "ward": "wart", "kid's": "kids'"}
toks = []
i = 0
while i < len(words):
    w = words[i]["w"].strip(); s, e = words[i]["s"], words[i]["e"]
    nxt = words[i + 1]["w"].strip().lower().lstrip("-") if i + 1 < len(words) else ""
    if re.sub(r"[^a-z]", "", w.lower()) in ("root", "rootout") and (nxt.startswith("out") or w.lower().rstrip(".,").endswith("-out")):
        if nxt.startswith("out"):
            tail = re.sub(r"^-?out", "", words[i + 1]["w"].strip(), flags=re.I); toks.append(["RootOut" + tail, s, words[i + 1]["e"]]); i += 2; continue
    if re.fullmatch(r"root-?out[.,]?", w.lower()): w = "RootOut" + w[-1] if w[-1] in ".," else "RootOut"
    core = re.sub(r"[^\w']", "", w).lower()
    if core in FIX: w = re.sub(re.escape(re.sub(r"[^\w']", "", w)), FIX[core], w)
    toks.append([w, s, e]); i += 1
# numbers split by whisper ("1" ",500") -> one token
k = 1
while k < len(toks):
    if toks[k][0][:1] == "," and toks[k - 1][0][-1:].isdigit():
        toks[k - 1] = [toks[k - 1][0] + toks[k][0], toks[k - 1][1], toks[k][2]]; del toks[k]
    else: k += 1
# 'picking out a wart' was a whisper slip; the VO says 'picking at a wart' (checked with large-v3)
for k in range(len(toks) - 1):
    if toks[k][0].lower() == "picking" and toks[k + 1][0].lower() == "out": toks[k + 1][0] = "at"

groups, cur = [], []
for t in toks:
    cur.append(t)
    end = t[0][-1:] in ".,?!:"
    if len(cur) >= 4 or (end and len(cur) >= 2) or (len(cur) >= 3 and sum(len(x[0]) for x in cur) > 20):
        groups.append(cur); cur = []
    elif end and len(cur) == 1:  # a lone word ending a sentence joins the card before it (if close in time)
        if groups and len(groups[-1]) < 5 and t[1] - groups[-1][-1][2] < 0.4 and not groups[-1][-1][0][-1:] in ".?!":
            groups[-1].append(t); cur = []
        else:
            groups.append(cur); cur = []
if cur: groups.append(cur)


def ts(x):
    h, m, s = int(x // 3600), int(x % 3600 // 60), x % 60
    return f"{h}:{m:02d}:{s:05.2f}"


ass = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 1080", "PlayResY: 1920", "", "[V4+ Styles]",
       "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, "
       "StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
       "Style: Cap,Inter,62,&H00141414,&H00141414,&H00FFFFFF,&H00FFFFFF,-1,0,0,0,100,100,0,0,3,14,0,2,90,90,760,1",
       "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
# product-safe zones from the body timeline (times are body-relative; the hook comes first)
HK = dur(hook); tl = {x["line"]: x for x in json.load(open(P / "work/body/timeline.json"))}
LOW = [(HK + tl["b11"]["start"] + 4.9, HK + tl["b11"]["start"] + 8.1)]          # bottle photo: captions drop low
NONE = [(HK + tl["b16c"]["start"] - 0.05, D + 1)]             # end card: no captions
for j, g in enumerate(groups):
    s = g[0][1]; e = groups[j + 1][0][1] if j + 1 < len(groups) and groups[j + 1][0][1] - g[-1][2] < 0.6 else g[-1][2] + 0.15
    text = " ".join(x[0] for x in g).rstrip(",")
    if any(a <= s < b for a, b in NONE): continue
    mv = 240 if any(a <= s < b for a, b in LOW) else 0
    for a, b in NONE:
        if s < a < e: e = a - 0.02  # never run onto the end card
    ass.append(f"Dialogue: 0,{ts(s)},{ts(min(e, D))},Cap,,0,0,{mv},,{text}")
(T / "captions.ass").write_text("\n".join(ass) + "\n")

# 3. music bed under the voice (sidechain ducking), fade out; captions burn; light phone-camera finish; loudness
fc = (f"[1:a]aloop=loop=-1:size=2e9,atrim=0:{D:.2f},volume=0.22,afade=t=in:d=1.5,afade=t=out:st={D - 3:.2f}:d=3[m];"
      f"[0:a]asplit[vo][sc];[m][sc]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[md];"
      f"[vo][md]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-2:LRA=9[a];"
      f"[0:v]ass={T / 'captions.ass'},noise=alls=3:allf=t,vignette=PI/5,unsharp=5:5:0.3[v]")
run(["-i", str(cat), "-i", str(MUSIC), "-filter_complex", fc, "-map", "[v]", "-map", "[a]",
     "-c:v", "libx264", "-crf", "20", "-maxrate", "10M", "-bufsize", "20M", "-preset", "slow", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
     "-map_metadata", "-1", "-movflags", "+faststart", str(out)])
print(out, round(dur(out), 2), "s,", len(groups), "caption groups")
