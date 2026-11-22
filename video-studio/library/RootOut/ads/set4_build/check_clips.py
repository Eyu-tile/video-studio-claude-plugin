#!/usr/bin/env python3
"""Word-for-word check of every lip-synced mom clip's own audio against SCRIPT_LOCK (medium.en whisper)."""
import json, re, subprocess, sys
from pathlib import Path
B = Path(__file__).resolve().parent; sys.path.insert(0, str(B))
from check_script import norm
P = Path("/home/user/video-studio-claude-plugin/video-studio/projects/rootout-set4"); C = P / "raw/gen/clips"
import build4
L = {l["id"]: l for l in json.loads((B / "SCRIPT_LOCK.json").read_text())["lines"]}
NUM = {"3": "three", "2": "two", "4": "four", "1": "one", "15": "fifteen", "14": "fourteen", "8": "eight"}
def n2(ws): return [NUM.get(w, w).replace("wort", "wart").replace("hardtop", "hard top") for w in ws]
if __name__ == "__main__":
    for k, (clip, vid) in build4.MOM.items():
        f = C / f"{clip}.mp4"
        if not f.exists(): continue
        tx = P / "work/tx_clips" / f"{clip}.json"
        got = " ".join(n2(norm(" ".join(w["w"] for w in json.loads(tx.read_text())["words"])))) if tx.exists() else None
        if got is None:
            build4.words(f); got = " ".join(n2(norm(" ".join(w["w"] for w in json.loads(tx.read_text())["words"]))))
        want = " ".join(n2(norm(L[vid]["text"]))).replace("hard top", "hard top")
        ok = got.replace(" ", "") == want.replace(" ", "")
        print(f"{'OK ' if ok else 'BAD'} {clip:14} {'' if ok else chr(10)+'   want: '+want+chr(10)+'   got:  '+got}")
