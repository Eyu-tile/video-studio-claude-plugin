#!/usr/bin/env python3
"""Lip-sync QA for every on-camera piece: rebuild the warp's chunk plan, warp the take's OWN speech with it, transcribe,
and compare word times with our VO for the same span. Prints mean / max |Δ| per piece. Usage: check_lips.py h1"""
import json, subprocess, sys, re, numpy as np
from pathlib import Path
from lipwarp import anchors, fmap, clampspan
from faster_whisper import WhisperModel
P = Path(__file__).resolve().parent.parent; m = WhisperModel("small.en", device="cpu", compute_type="int8")
TMP = Path("/tmp/claude-0/-home-user-video-studio-claude-plugin/0f792524-13bc-5526-a041-7b468e4bc249/scratchpad/lips"); TMP.mkdir(exist_ok=True)
def plan(t, t0, t1):  # same logic as lipwarp.warp
    a = anchors(t); cuts = [t0] + [p[0] for p in a if t0 + 0.25 < p[0] < t1 - 0.25] + [t1]; keep = [cuts[0]]
    for c in cuts[1:-1]:
        if c - keep[-1] >= 0.35: keep.append(c)
    keep.append(t1); out = []; last_word = max(p[0] for p in a); s1p = None
    for i in range(len(keep) - 1):
        x0, x1 = keep[i], keep[i + 1]; dd = x1 - x0; s0 = fmap(t, x0) if i == 0 else s1p
        s1 = s0 + dd if x0 >= last_word else s0 + clampspan(t, s0, fmap(t, x1) - fmap(t, x0), dd); s1p = s1
        out.append((x0, x1, s0, s1))
    return out
def pcm(args): return np.frombuffer(subprocess.check_output(["ffmpeg", "-v", "error"] + args + ["-ac", "1", "-ar", "16000", "-f", "s16le", "-"]), np.int16).astype(np.float32) / 32768
def words(x): return [(re.sub(r"[^a-z]", "", w.word.lower()), w.start) for s in m.transcribe(x, word_timestamps=True)[0] for w in s.words]
if __name__ != "__main__": raise SystemExit
hook = (sys.argv[1:] or ["h1"])[0]
segs = json.load(open(P / f"work/{hook}_take_segs.json"))
for t, a, d in segs:
    ch = plan(t, a, a + d); parts = []
    for x0, x1, s0, s1 in ch:
        r = (s1 - s0) / (x1 - x0); parts.append(pcm(["-ss", f"{s0:.3f}", "-t", f"{s1-s0:.3f}", "-i", str(P / f"raw/gen/clips/{t}.mp4"), "-af", f"atempo={min(2,max(.5,r)):.4f}"]))
    wa = words(np.concatenate(parts)); wb = words(pcm(["-ss", f"{a:.3f}", "-t", f"{d:.3f}", "-i", str(P / f"work/ls/{t}_lipsync.wav")]))
    import difflib
    sm = difflib.SequenceMatcher(None, [w for w, _ in wa], [w for w, _ in wb], autojunk=False); dl = []
    for i, j, n in sm.get_matching_blocks():
        dl += [abs(wa[i + k][1] - wb[j + k][1]) for k in range(n)]
    print(f"{t} {a:6.2f}+{d:4.2f}s words {len(wb):2d} matched {len(dl):2d}  mean {np.mean(dl) if dl else -1:.3f}  max {max(dl) if dl else -1:.3f}")
