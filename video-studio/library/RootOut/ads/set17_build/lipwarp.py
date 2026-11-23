#!/usr/bin/env python3
"""Lip-sync fix: Seedance re-voices the reference audio with its own timing, so its lips follow ITS speech.
Word-align the clip's own speech to our lip-sync track, then retime the picture chunk by chunk so each word lands on
the voice we actually play. warp(take, t0, t1, out): video for lip-sync-track time [t0, t1] (720x1280, 30 fps)."""
import json, re, subprocess, difflib, os, numpy as np
from pathlib import Path
P = Path(__file__).resolve().parent.parent; CACHE = P / "work/lipwarp_words.json"
def _load(p):
    raw = subprocess.check_output(["ffmpeg", "-v", "error", "-i", str(p), "-ac", "1", "-ar", "16000", "-f", "s16le", "-"])
    return np.frombuffer(raw, np.int16).astype(np.float32) / 32768
def words():
    out = json.load(open(CACHE)) if CACHE.exists() else {}
    need = [(t, k, src) for t in ("D1", "D2", "M1", "MH", "DH") for k, src in (("clip", P / f"raw/gen/clips/{t}.mp4"), ("ls", P / f"work/ls/{t}_lipsync.wav")) if f"{t}_{k}" not in out and src.exists()]
    if not need: return out
    from faster_whisper import WhisperModel
    m = WhisperModel("medium.en", device="cpu", compute_type="int8")
    for t, k, src in need:
            out[f"{t}_{k}"] = [[w.word.strip(), w.start, w.end] for s in m.transcribe(_load(src), word_timestamps=True, beam_size=5)[0] for w in s.words]
    json.dump(out, open(CACHE, "w")); return out
def norm(w): return re.sub(r"[^a-z0-9]", "", w.lower()).replace("wort", "wart")
def anchors(t):
    W = words(); c, l = W[f"{t}_clip"], W[f"{t}_ls"]
    sm = difflib.SequenceMatcher(None, [norm(x[0]) for x in l], [norm(x[0]) for x in c], autojunk=False)
    pts = [(0.0, 0.0)]
    for a, b, n in sm.get_matching_blocks():
        for k in range(n): pts.append((l[a + k][1], c[b + k][1])); pts.append((l[a + k][2], c[b + k][2]))
    pts = sorted(set(pts)); mono = [pts[0]]
    for p in pts[1:]:
        if p[0] > mono[-1][0] + 0.02 and p[1] > mono[-1][1] + 0.02: mono.append(p)
    return mono
def fmap(t, x):
    a = anchors(t); xs, ys = [p[0] for p in a], [p[1] for p in a]
    if x <= xs[-1]: return float(np.interp(x, xs, ys))
    return ys[-1] + (x - xs[-1])
def warp(t, t0, t1, out, vf_extra=""):
    clip = P / f"raw/gen/clips/{t}.mp4"; a = anchors(t)
    cuts = [t0] + [p[0] for p in a if t0 + 0.25 < p[0] < t1 - 0.25] + [t1]
    keep = [cuts[0]]
    for c in cuts[1:-1]:
        if c - keep[-1] >= 0.35: keep.append(c)
    keep.append(t1); parts = []; tmp = Path(str(out) + "_parts"); tmp.mkdir(exist_ok=True)
    for i in range(len(keep) - 1):
        x0, x1 = keep[i], keep[i + 1]; s0, s1 = fmap(t, x0), fmap(t, x1); dd = x1 - x0; sd = max(s1 - s0, 0.05)
        pp = tmp / f"{i:03d}.mp4"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{s0:.3f}", "-t", f"{sd:.3f}", "-i", str(clip), "-vf",
            f"setpts=PTS*{dd/sd:.5f},scale=720:1280,setsar=1,fps=30{vf_extra},format=yuv420p", "-t", f"{dd:.3f}", "-an",
            "-c:v", "libx264", "-crf", "16", "-preset", "veryfast", str(pp)], check=True); parts.append(pp)
    (tmp / "l.txt").write_text("".join(f"file '{p.name}'\n" for p in parts))
    subprocess.run(f"cd '{tmp}' && ffmpeg -v error -y -f concat -safe 0 -i l.txt -c:v libx264 -crf 16 -preset veryfast -r 30 '{out}'", shell=True, check=True)
if __name__ == "__main__":
    for t in ("D1", "D2", "M1"):
        a = anchors(t); print(t, len(a), "anchors; max drift", round(max(abs(x - y) for x, y in a), 2), "s")
