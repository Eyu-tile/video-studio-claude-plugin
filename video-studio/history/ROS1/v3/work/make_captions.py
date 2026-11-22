#!/usr/bin/env python3
"""Fix whisper spellings in a render's transcript, then build bold-pop captions on that render (identity EDL)."""
import json, re, subprocess, sys
from pathlib import Path
P = Path(__file__).resolve().parent.parent; VS = P.parents[2] / "plugins/video-studio/bin/vs"
FIX = {"wort": "wart", "hardtop": "hard top", "chapstick": "Chapstick"}
h = sys.argv[1]; raw = P / f"out/set1_{h}_v2raw.mp4"; tx = P / f"work/tx_{h}.json"
d = json.loads(tx.read_text()); W = d["words"]
key = "w" if "w" in W[0] else ("word" if "word" in W[0] else "text")
out = []
for i, w in enumerate(W):
    t = w[key].strip()
    if t.lower().strip(".,?") == "root" and i + 1 < len(W) and W[i + 1][key].strip().lower().startswith("out"):
        w[key] = "RootOut" + W[i + 1][key].strip()[3:]; W[i + 1]["_drop"] = True
    base = t.lower().strip(".,?!"); 
    if base in FIX: w[key] = t.lower().replace(base, FIX[base])
    w[key] = w[key].replace("?", "") if w[key].strip() not in ("sting?",) else w[key]
for w in W:
    if w.get("_drop"): continue
    if w["s"] > float(d["duration"]) - 3.0 and w[key].strip(" ?.").lower() == "you": continue  # music hallucination on the end card
    out.append(w)
merged = []
for w in out:  # whisper splits "90-day" / "money-back" into "90" + "-day"
    if merged and w[key].strip().startswith("-"):
        merged[-1][key] = merged[-1][key].rstrip() + w[key].strip(); merged[-1]["e"] = w["e"]
    else: merged.append(w)
out = merged
d["words"] = out; d.pop("segments", None)
fx = P / f"work/tx_{h}_fixed.json"; fx.write_text(json.dumps(d, indent=1))
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(raw)], capture_output=True, text=True).stdout)
ide = P / f"work/ads/identity_{h}.edl.json"; ide.write_text(json.dumps({"segments": [{"src": str(raw), "start": 0, "end": round(dur, 3)}]}))
subprocess.run([str(VS), "captions", str(fx), str(ide), "-o", str(P / f"work/captions_{h}"), "--style", "bold-pop", "--aspect", "9:16",
                "--accent", "#FFD400", "--font", "Inter"], check=True)

# ---- keep captions off the disclaimers and the product graphics ----
edl = json.loads((P / f"work/ads/set1_{h}.edl.json").read_text())
win, t = [], 0.0
for s in edl["segments"]:
    L = (s["end"] - s["start"]) / (s.get("speed") or 1)
    if any(k in s["src"] for k in ("g26_stakes", "g27_offer", "g27b_offer")): win.append((t, t + L, 1580))  # below the bottles
    t += L
for x in edl["texts"]:
    if x["text"][0] in "*†": win.append((x["start"], x["end"], 560))  # above the disclaimer / skin graphic
def ts(v):
    hh, mm, ss = v.split(":"); return int(hh) * 3600 + int(mm) * 60 + float(ss)
ass = P / f"work/captions_{h}.ass"; lines = []
for ln in ass.read_text().splitlines():
    if ln.startswith("Dialogue:"):
        f = ln.split(",", 9); st = ts(f[1])
        for a, b, y in win:
            if a - 0.05 <= st < b: f[9] = "{\\an2\\pos(540,%d)}" % y + f[9]; break
        ln = ",".join(f)
    lines.append(ln)
ass.write_text("\n".join(lines) + "\n"); print("moved captions in", len(win), "windows")
