#!/usr/bin/env python3
"""check_take.py NAME URL "expected line"  -> downloads to raw/gen/clips/NAME.mp4, STT word check, voice pitch, frame strip."""
import json, subprocess, sys, re, wave, io
import numpy as np
from pathlib import Path
from PIL import Image
CL = Path("/home/user/video-studio-claude-plugin/projects/rootout-set15/raw/gen/clips")
name, url, exp = sys.argv[1:4]; f = CL / f"{name}.mp4"
if not f.exists(): subprocess.run(["curl", "-s", "-o", str(f), url], check=True)
j = Path(str(f) + ".stt.json")
if not j.exists():
    subprocess.run(["curl", "-s", "-m", "180", "-X", "POST", "https://api.elevenlabs.io/v1/speech-to-text", "-H", "xi-api-key: dummy",
                    "-F", "model_id=scribe_v1", "-F", "timestamps_granularity=word", "-F", f"file=@{f}", "-o", str(j)], check=True)
got = json.load(open(j))["text"]
D = {"4": "four", "14": "fourteen", "5": "five", "6": "six", "2": "two"}
n = lambda s: [D.get(re.sub(r"[^a-z0-9]", "", w), re.sub(r"[^a-z0-9]", "", w)) for w in s.lower().replace("8x", "eight times").replace("-", " ").split() if re.sub(r"[^a-z0-9]", "", w)]
ok = n(got) == n(exp)
d = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)]))
raw = subprocess.check_output(["ffmpeg", "-v", "error", "-i", str(f), "-ac", "1", "-f", "wav", "-"])
w = wave.open(io.BytesIO(raw)); sr = w.getframerate(); x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(float)
fs = []; N = int(sr * 0.04)
for i in range(0, len(x) - N, N):
    s = x[i:i + N]
    if np.abs(s).mean() < 500: continue
    s = s - s.mean(); c = np.correlate(s, s, "full")[N - 1:]; lo, hi = int(sr / 400), int(sr / 80); fs.append(sr / (lo + np.argmax(c[lo:hi])))
ims = []
for t in np.linspace(0.3, d - 0.3, 5):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", str(f), "-frames:v", "1", "-vf", "scale=-2:360", "/tmp/_c.png"])
    ims.append(Image.open("/tmp/_c.png").copy())
c = Image.new("RGB", (sum(i.width for i in ims), 360)); xx = 0
for i in ims: c.paste(i, (xx, 0)); xx += i.width
c.save(f"/tmp/chk_{name}.jpg", quality=80)
print(f"{name} {d:.1f}s pitch {np.median(fs):.0f}Hz words {'OK' if ok else 'MISMATCH'}\n  got: {got}\n  exp: {exp}")
