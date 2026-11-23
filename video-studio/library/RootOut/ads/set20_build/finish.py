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
       "route": "root", "ward": "wart", "8x": "8x"}
toks = []
i = 0
while i < len(words):
    w = words[i]["w"].strip(); s, e = words[i]["s"], words[i]["e"]
    if i + 1 < len(words) and (w.lower().strip(".,") == "root" and words[i + 1]["w"].lower().strip(".,").startswith("out")):
        tail = words[i + 1]["w"][3:]; toks.append(["RootOut" + tail, s, words[i + 1]["e"]]); i += 2; continue
    core = re.sub(r"[^\w']", "", w).lower()
    if core in FIX: w = re.sub(re.escape(re.sub(r"[^\w']", "", w)), FIX[core], w)
    toks.append([w, s, e]); i += 1
# 'picking out a wart' was a whisper slip; the VO says 'picking at a wart' (checked with large-v3)
for k in range(len(toks) - 1):
    if toks[k][0].lower() == "picking" and toks[k + 1][0].lower() == "out": toks[k + 1][0] = "at"

groups, cur = [], []
for t in toks:
    cur.append(t)
    if len(cur) >= 4 or t[0][-1:] in ".,?!:" or (len(cur) >= 2 and sum(len(x[0]) for x in cur) > 18):
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
for j, g in enumerate(groups):
    s = g[0][1]; e = groups[j + 1][0][1] if j + 1 < len(groups) and groups[j + 1][0][1] - g[-1][2] < 0.6 else g[-1][2] + 0.15
    text = " ".join(x[0] for x in g).rstrip(",")
    ass.append(f"Dialogue: 0,{ts(s)},{ts(min(e, D))},Cap,,0,0,0,,{text}")
(T / "captions.ass").write_text("\n".join(ass) + "\n")

# 3. music bed under the voice (sidechain ducking), fade out; captions burn; light phone-camera finish; loudness
fc = (f"[1:a]aloop=loop=-1:size=2e9,atrim=0:{D:.2f},volume=0.22,afade=t=in:d=1.5,afade=t=out:st={D - 3:.2f}:d=3[m];"
      f"[0:a]asplit[vo][sc];[m][sc]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[md];"
      f"[vo][md]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-2:LRA=9[a];"
      f"[0:v]ass={T / 'captions.ass'},noise=alls=5:allf=t,vignette=PI/5,unsharp=5:5:0.4[v]")
run(["-i", str(cat), "-i", str(MUSIC), "-filter_complex", fc, "-map", "[v]", "-map", "[a]",
     "-c:v", "libx264", "-crf", "17", "-preset", "slow", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
     "-map_metadata", "-1", "-movflags", "+faststart", str(out)])
print(out, round(dur(out), 2), "s,", len(groups), "caption groups")
