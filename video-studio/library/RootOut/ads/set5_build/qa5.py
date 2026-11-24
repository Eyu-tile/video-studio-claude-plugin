#!/usr/bin/env python3
"""Set 5 QA: (1) the final audio says the brief's script word for word, (2) every b-roll source used once
(talking clips may be cut within their own line; the wart stills are the night-by-night progression device),
(3) no frozen picture >= 0.5 s, (4) loudness. Usage: qa5.py out/<file>.mp4"""
import json, re, subprocess, sys, difflib, collections
from pathlib import Path
P = Path("/home/user/video-studio-claude-plugin/video-studio/projects/rootout-set5"); f = Path(sys.argv[1])
sys.path.insert(0, str(Path(__file__).parent)); import build5 as B

NUM = {"8x": "eight times", "90-day": "ninety day", "14": "fourteen", "4": "four", "2": "two", "90": "ninety", "10": "ten", "8": "eight"}
def norm(t):
    t = t.lower().replace("-", " ")
    return [NUM.get(w, w) for w in re.sub(r"[^a-z0-9' ]", " ", t).replace("'", "").split() for w in [w]]
def flat(ws): return " ".join(ws).split()

script = []
for name, audio, _ in B.LINES:
    if audio[0] == "vo": script += norm(B.SCRIPT[audio[1]])
    elif audio[0] == "talk":
        for ln, _ in (B.COMBO.get(name) or [(audio[2].stem, 0)]): script += norm(B.SCRIPT[ln])
script = flat(script)
wav = P / "work/qa.wav"; subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(f), "-ac", "1", "-ar", "16000", str(wav)], check=True)
from faster_whisper import WhisperModel
m = WhisperModel("medium.en", device="cpu", compute_type="int8")
import librosa; y, _ = librosa.load(str(wav), sr=16000)
segs, _ = m.transcribe(y, initial_prompt="RootOut, pokeweed, white cedar, tea tree, plantar wart, pediatricians, dandelion")
heard = flat(norm(" ".join(s.text for s in segs)))
sm = difflib.SequenceMatcher(None, script, heard); ok = sum(b.size for b in sm.get_matching_blocks())
print(f"[1] script words {len(script)}, matched {ok}")
for op, a1, a2, b1, b2 in sm.get_opcodes():
    if op != "equal": print(f"    {op}: script '{' '.join(script[a1:a2])}'  heard '{' '.join(heard[b1:b2])}'")

talk = {a[1] for _, a, _ in B.LINES if a[0] == "talk"}; prog = {B.FR / x for x in ("W1.png", "W3.png", "W7.png", "W14.png")}
use = collections.Counter()
for _, _, vis in B.LINES:
    for k, src, _, o in vis:
        for s in (src, o.get("bg"), (o.get("top") or (None, None))[1]):
            if s and s not in talk and s not in prog and "graphics" not in str(s): use[s] += 1
dup = {str(k.name): v for k, v in use.items() if v > 1}
print(f"[2] b-roll sources {len(use)}, used more than once: {dup or 'none'}")
fz = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(f), "-vf", "freezedetect=n=-60dB:d=0.5", "-an", "-f", "null", "-"], capture_output=True, text=True).stderr
fr = re.findall(r"freeze_start: ([\d.]+)", fz); print(f"[3] frozen spans >= 0.5 s: {fr or 'none'}")
lu = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(f), "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
print("[4]", " ".join(re.findall(r"I:\s+[-\d.]+ LUFS", lu)[-1:]), " ".join(re.findall(r"Peak:\s+[-\d.]+ dBFS", lu)[-1:]))
