# STRICT uniqueness audit for an ad's EDL: every b-roll / metric shot must come from different footage.
# 1) same source file (Drive id from the .json sidecar, else the file path)  2) visually the same footage under another name:
# a 16x16 grey fingerprint of 5 frames across the used range, compared between every pair of shots (A-roll pieces skipped).
# usage: python3 -I broll_unique.py EDL.json [AROLL_SUBSTR]   (AROLL_SUBSTR: path part that marks the creator A-roll, skipped; default "/work/aroll/")
import sys, json, os, subprocess, itertools, numpy as np
E = json.load(open(sys.argv[1])); skip = sys.argv[2] if len(sys.argv) > 2 else "/work/aroll/"
def fp(src, a, b, sp):
    out = []
    for f in np.linspace(0.1, 0.9, 5):
        t = a + (b - a) * f
        raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", src, "-frames:v", "1", "-vf", "scale=16:16,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
        if len(raw) == 256: v = np.frombuffer(raw, np.uint8).astype(float); out.append((v - v.mean()) / (v.std() + 1e-6))
    return out
shots = []
for s in E["segments"]:
    if skip in s["src"] or s["src"].endswith(".png"): continue
    sid = json.load(open(s["src"] + ".json")).get("id") if os.path.exists(s["src"] + ".json") else s["src"]
    shots.append((s["label"], s["src"], sid, fp(s["src"], s["start"], s["end"], s.get("speed", 1))))
bad = []
for (l1, f1, i1, p1), (l2, f2, i2, p2) in itertools.combinations(shots, 2):
    if i1 == i2: bad.append(f"SAME SOURCE: {l1} / {l2}"); continue
    best = max((float((x * y).mean()) for x in p1 for y in p2), default=0)
    if best > 0.93: bad.append(f"LOOKS THE SAME (r={best:.2f}): {l1} / {l2}")
print(os.path.basename(sys.argv[1]), "b-roll/metric shots:", len(shots), "| unique labels:", len({x[0] for x in shots}))
for b in bad: print("  !!", b)
if not bad: print("  OK: no shot repeats a source or its footage")
