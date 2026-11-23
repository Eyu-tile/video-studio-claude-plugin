#!/usr/bin/env python3
"""Flag frozen stretches (>= 0.4 s) inside b-roll / talking shots. Code cards (g_*) may hold on purpose."""
import json, re, subprocess, sys
from pathlib import Path
P = Path(__file__).resolve().parent.parent
bad = 0
for h in sys.argv[1:]:
    B = P / f"work/build/{h}"; tl = json.load(open(B / "timeline.json"))
    r = subprocess.run(["ffmpeg", "-v", "info", "-i", str(B / "video.mp4"), "-vf", "scale=360:-2,freezedetect=n=0.002:d=0.4",
                        "-an", "-f", "null", "-"], capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r"freeze_start: ([\d.]+)", r)]; en = [float(x) for x in re.findall(r"freeze_end: ([\d.]+)", r)]
    en += [tl["length"]] * (len(st) - len(en))
    for a, b in zip(st, en):
        hits = [s for s in tl["shots"] if s[0] < b and s[1] > a]
        names = sorted({s[2] for s in hits})
        if all(n.startswith("g_") or n.startswith("brand_") for n in names): continue
        bad += 1; print(f"{h} FREEZE {a:7.2f}-{b:7.2f} ({b - a:.2f}s) in {names}")
print("freeze check:", "PASS" if bad == 0 else f"{bad} issues")
