#!/usr/bin/env python3
"""Set 18 QA: (1) transcript of the render == script VO, word for word (ElevenLabs STT); (2) no frozen picture >= 0.5 s
outside the end card and the scripted holds; (3) each b-roll source used once. Usage: qa18.py <render.mp4>"""
import json, re, subprocess, sys, difflib
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent)); import timeline as TLm
P = TLm.P; f = Path(sys.argv[1]); T = P / "work/qa"; T.mkdir(parents=True, exist_ok=True)
L = [l[2] for l in json.load(open(P / "work/lines.json"))["lines"]]
norm = lambda s: [TLm.NUM.get(x, x) for x in re.findall(r"[a-z0-9']+", s.lower().replace("’", "'").replace("school kids", "schoolkids").replace("root out", "rootout"))]
want = [w.replace("'", "") for l in L for w in norm(l)]
sj = T / (f.stem + ".stt.json")
if not sj.exists():
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(f), "-vn", "-ac", "1", "-ar", "16000", "-b:a", "64k", str(T / "a.mp3")], check=True)
    subprocess.run(["curl", "-s", "-m", "300", "-X", "POST", "https://api.elevenlabs.io/v1/speech-to-text", "-H", "xi-api-key: dummy",
                    "-F", "model_id=scribe_v1", "-F", f"file=@{T / 'a.mp3'}", "-o", str(sj)], check=True)
got = [w.replace("'", "") for w in norm(json.load(open(sj))["text"])]
fix = {"1500": ["fifteen", "hundred"], "8": ["eight"], "4": ["four"], "14": ["fourteen"], "90": ["ninety"], "10": ["ten"]}
g2 = []
for w in got: g2 += fix.get(w, [w])
ops = [o for o in difflib.SequenceMatcher(None, want, g2, autojunk=False).get_opcodes() if o[0] != "equal"]
print(f"transcript: {len(want)} script words, {len(g2)} heard, {len(ops)} differences")
for o in ops[:20]: print("  ", o[0], want[o[1]:o[2]], "->", g2[o[3]:o[4]])
fr = subprocess.run(["ffmpeg", "-i", str(f), "-vf", "freezedetect=n=0.003:d=0.5", "-map", "0:v", "-f", "null", "-"], capture_output=True, text=True).stderr
fz = re.findall(r"freeze_start: ([\d.]+).*?freeze_duration: ([\d.]+)", fr, re.S)
print("freezes >=0.5s:", [(round(float(a), 1), round(float(b), 1)) for a, b in fz] or "none")
tl = json.load(open(sys.argv[2] if len(sys.argv) > 2 else P / "work/build/H1/timeline.json"))
srcs = [Path(s["src"]).stem for s in tl["shots"] if s.get("kind", "x") in ("clip", "still", "card", "anim", "x") and s["src"] != "TAKE"]
dup = {s for s in srcs if srcs.count(s) > 1}
print("b-roll used more than once:", dup or "none")
