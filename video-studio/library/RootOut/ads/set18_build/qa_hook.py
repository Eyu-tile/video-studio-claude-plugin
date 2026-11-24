#!/usr/bin/env python3
"""QA for a v3 hook cut: transcript vs that hook's script lines (ITEMS of build18v3 with HOOK=Hn), freezes, loudness.
Usage: HOOK=H2 python3 qa_hook.py"""
import json, os, re, subprocess, sys, difflib
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import build18v3 as B
f = B.FINAL; T = B.P / "work/qa"; T.mkdir(parents=True, exist_ok=True)
NUM = {"1500": "fifteen hundred", "8x": "eight times", "8": "eight", "4": "four", "14": "fourteen", "90": "ninety", "10": "ten"}
def norm(s):
    s = s.lower().replace("’", "'").replace("school kids", "schoolkids").replace("root out", "rootout").replace("1,500", "1500")
    out = []
    for w in re.findall(r"[a-z0-9']+", s): out += NUM.get(w, w).split()
    return [w.replace("'", "") for w in out]
want = [w for it in B.ITEMS for w in norm(it[2])]
sj = T / (f.stem + ".stt.json")
if not sj.exists():
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(f), "-vn", "-ac", "1", "-ar", "16000", "-b:a", "64k", str(T / "a.mp3")], check=True)
    subprocess.run(["curl", "-s", "-m", "300", "-X", "POST", "https://api.elevenlabs.io/v1/speech-to-text", "-H", "xi-api-key: dummy",
                    "-F", "model_id=scribe_v1", "-F", f"file=@{T / 'a.mp3'}", "-o", str(sj)], check=True)
got = norm(json.load(open(sj))["text"])
ops = [o for o in difflib.SequenceMatcher(None, want, got, autojunk=False).get_opcodes() if o[0] != "equal"]
print(f"{f.name}: transcript {len(want)} script words, {len(got)} heard, {len(ops)} differences")
for o in ops[:20]: print("  ", o[0], want[o[1]:o[2]], "->", got[o[3]:o[4]])
fr = subprocess.run(["ffmpeg", "-i", str(f), "-vf", "freezedetect=n=0.003:d=0.5", "-map", "0:v", "-f", "null", "-"], capture_output=True, text=True).stderr
fz = re.findall(r"freeze_start: ([\d.]+).*?freeze_duration: ([\d.]+)", fr, re.S)
print("freezes >=0.5s:", [(round(float(a), 1), round(float(b), 1)) for a, b in fz] or "none")
lu = subprocess.run(["ffmpeg", "-i", str(f), "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True).stderr
print("loudness:", re.findall(r"I:\s+(-?[\d.]+) LUFS", lu)[-1], "LUFS")
