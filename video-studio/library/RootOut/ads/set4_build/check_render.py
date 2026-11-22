#!/usr/bin/env python3
"""Whole-render check: the render's transcript (medium.en) must contain the locked script for that hook, in order, word for word."""
import json, sys, difflib
from pathlib import Path
B = Path(__file__).resolve().parent; sys.path.insert(0, str(B))
from check_script import norm
from check_clips import n2
L = json.loads((B / "SCRIPT_LOCK.json").read_text())["lines"]
h, tx = sys.argv[1], Path(sys.argv[2])
hook = {"h1": ["h1"], "h2": ["h2a", "h2b"], "h3": ["h3"]}[h]
want = n2(norm(" ".join(l["text"] for l in L if l["id"] in hook or not l["id"].startswith("h"))))
got = n2(norm(" ".join(w["w"] for w in json.loads(tx.read_text())["words"])))
want, got = [w.replace("hardtop", "hard top") for w in want], [w for w in got]
sm = difflib.SequenceMatcher(a=want, b=got, autojunk=False); bad = 0
for op, a0, a1, b0, b1 in sm.get_opcodes():
    if op != "equal": bad += 1; print(op, "script:", " ".join(want[a0:a1]), "| heard:", " ".join(got[b0:b1]))
print(f"{h}: {len(want)} script words, {bad} differences")
