#!/usr/bin/env python3
"""Captions for a Set 4 render: whisper the render, fix whisper spellings back to the locked script, bold-pop captions,
then place each caption where it doesn't cover the face, the cut-away, the ranking board or the product.
make_captions.py h1 out/draft_h1.mp4"""
import json, re, subprocess, sys
from pathlib import Path
P = Path("/home/user/video-studio-claude-plugin/video-studio/projects/rootout-set4")
VS = "/home/user/video-studio-claude-plugin/plugins/video-studio/bin/vs"
FIX = {"wort": "wart", "worts": "warts", "hardtop": "hard top", "route": "root", "15": "fifteen", "14": "fourteen", "2": "two", "3": "three",
       "4": "four", "1": "one", "cat": "cap", "rip": "R.I.P.", "r.i.p": "R.I.P.", "pediatrician": "pediatricians", "8x": "8x"}
h, render = sys.argv[1], P / sys.argv[2]
tx = P / f"work/tx_render_{h}.json"
if not tx.exists() or tx.stat().st_mtime < render.stat().st_mtime:
    subprocess.run([VS, "transcribe", str(render), "-o", str(tx.with_suffix("")), "--model", "medium.en"], check=True)
d = json.loads(tx.read_text()); W = d["words"]
out = []
for i, w in enumerate(W):
    t = w["w"].strip(); base = t.lower().strip(".,?!:")
    m = re.match(r"^(\W*)(.*?)(\W*)$", t); pre, core, post = m.groups()
    if base in FIX: w["w"] = pre + FIX[base] + post
    if base == "root" and i + 1 < len(W) and W[i + 1]["w"].strip().lower().startswith("out"):
        w["w"] = "RootOut" + W[i + 1]["w"].strip()[3:]; W[i + 1]["_drop"] = True
    if base == "eight" and i + 1 < len(W) and W[i + 1]["w"].strip().lower().startswith("times"):
        w["w"] = "8x" + W[i + 1]["w"].strip()[5:]; W[i + 1]["_drop"] = True
for w in W:
    if not w.get("_drop"): out.append(w)
edl = json.loads((P / f"work/ads/set4_{h}.edl.json").read_text())
# shot windows on the edit clock -> caption y (centre-bottom anchor)
win, t = [], 0.0
for s in edl["segments"]:
    L = (s["end"] - s["start"]) / (s.get("speed") or 1); src = s["src"]; y = 1660
    if "/work/cutaway/vo_" in src:
        sc = json.loads(Path(src).with_suffix(".json").read_text()); y = 1105 if sc.get("board") else 1660
    if "g_offer" in src: y = 1330
    if "g_calendar" in src: y = 1660
    if "g_end" in src: y = -1
    win.append((t, t + L, y)); t += L
out = [w for w in out if not any(a <= w["s"] < b and y < 0 for a, b, y in win)]
d["words"] = out; d.pop("segments", None)
fx = P / f"work/tx_render_{h}_fixed.json"; fx.write_text(json.dumps(d, indent=1))
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(render)], capture_output=True, text=True).stdout)
ide = P / f"work/ads/identity_{h}.edl.json"; ide.write_text(json.dumps({"segments": [{"src": str(render), "start": 0, "end": round(dur, 3)}]}))
subprocess.run([VS, "captions", str(fx), str(ide), "-o", str(P / f"work/captions_{h}"), "--style", "bold-pop", "--aspect", "9:16",
                "--accent", "#FFD400", "--font", "Inter"], check=True)
def ts(v):
    hh, mm, ss = v.split(":"); return int(hh) * 3600 + int(mm) * 60 + float(ss)
ass = P / f"work/captions_{h}.ass"; lines = []
for ln in ass.read_text().splitlines():
    if ln.startswith("Dialogue:"):
        f = ln.split(",", 9); st = ts(f[1])
        y = next((yy for a, b, yy in win if a - 0.05 <= st < b), 1660)
        f[9] = "{\\an2\\pos(540,%d)}" % y + re.sub(r"^\{\\an\d\\pos\([^)]*\)\}", "", f[9]); ln = ",".join(f)
    lines.append(ln)
ass.write_text("\n".join(lines) + "\n"); print("captions", ass)
