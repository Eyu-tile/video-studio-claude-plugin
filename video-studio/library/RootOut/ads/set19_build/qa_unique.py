#!/usr/bin/env python3
"""Every b-roll source may appear only once per hook (talking clips and code cards excluded)."""
import json, sys
from collections import defaultdict
from pathlib import Path
P = Path(__file__).resolve().parent.parent
bad = 0
for h in sys.argv[1:]:
    tl = json.load(open(P / f"work/build/{h}/timeline.json"))
    talk_starts = {round(p[4], 2) for p in tl["pieces"] if p[0] == "talk"}
    seen = defaultdict(list)
    for a, b, n in tl["shots"]:
        if n.startswith("g_") or round(a, 2) in talk_starts: continue
        seen[n].append(f"{int(a // 60)}:{a % 60:04.1f}")
    for n, ts in seen.items():
        if len(ts) > 1: bad += 1; print(h, "REUSED", n, ts)
print("unique b-roll check:", "PASS" if not bad else f"{bad} reused")
