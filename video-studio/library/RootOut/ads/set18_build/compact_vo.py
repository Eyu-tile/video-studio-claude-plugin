#!/usr/bin/env python3
"""Tighten Seed Audio lines: cut flubbed words, cap silent gaps (cut mid-gap), trim head/tail. -> raw/vo3/c/<name>.wav"""
import json, subprocess, sys
from pathlib import Path
D = Path("/home/user/video-studio-claude-plugin/video-studio/projects/rootout-set18/raw/vo3")
DROP = {"K2a": ["Wart?"], "Y2": ["ran,"]}
CAP = 0.42
def run(name):
    w = [x for x in json.load(open(D / f"{name}.wav.stt.json"))["words"] if x["type"] == "word"]
    w = [x for x in w if x["text"] not in DROP.get(name, [])]
    segs = []; s = w[0]["start"] - 0.08
    for a, b in zip(w, w[1:]):
        g = b["start"] - a["end"]
        if g > CAP:
            segs.append((s, a["end"] + CAP / 2)); s = b["start"] - CAP / 2
    segs.append((s, w[-1]["end"] + 0.15))
    f = ";".join(f"[0]atrim={a:.3f}:{b:.3f},asetpts=N/SR/TB,afade=t=in:d=0.012,afade=t=out:st={b-a-0.012:.3f}:d=0.012[s{i}]" for i, (a, b) in enumerate(segs))
    f += ";" + "".join(f"[s{i}]" for i in range(len(segs))) + f"concat=n={len(segs)}:v=0:a=1[o]"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", D / f"{name}.wav", "-filter_complex", f, "-map", "[o]", "-ar", "44100", "-ac", "1", D / f"c/{name}.wav"], check=True)
for n in sys.argv[1:]: run(n)
