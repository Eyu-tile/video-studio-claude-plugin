#!/usr/bin/env python3
"""Compare a whisper transcript (work/tx/<id>.json, words[{w,s,e}]) with SCRIPT_LOCK.json, line by line, or a full render."""
import json, re, sys
from pathlib import Path
B = Path(__file__).resolve().parent
L = json.loads((B / "SCRIPT_LOCK.json").read_text())["lines"]
def norm(s):
    s = s.lower().replace("8x", "eight times").replace("r.i.p.", "r i p").replace("r. i. p.", "r i p").replace("rip", "r i p").replace("-", " ")
    s = re.sub(r"\b4\b", "four", s); s = s.replace("root out", "rootout")
    return re.sub(r"[^a-z0-9 ]", "", s).split()
def words(f): return [w["w"] for w in json.loads(Path(f).read_text())["words"]]
if __name__ == "__main__":
    txdir = Path(sys.argv[1]); bad = 0
    for l in L:
        got, want = norm(" ".join(words(txdir / f"{l['id']}.json"))), norm(l["text"])
        if got != want: bad += 1; print(f"{l['id']}\n  want: {' '.join(want)}\n  got:  {' '.join(got)}")
    print("lines checked", len(L), "mismatches", bad)
