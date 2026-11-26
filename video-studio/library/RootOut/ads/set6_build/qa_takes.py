#!/usr/bin/env python3
"""Check each downloaded take: words vs script (ElevenLabs STT), voice pitch vs K1, length."""
import sys, subprocess, numpy as np
sys.argv = [sys.argv[0], "--plan"]; import build6 as B
def f0(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
    x = np.frombuffer(raw, np.int16).astype(float); fs = 16000; out = []
    for i in range(0, len(x) - 1024, 512):
        w = x[i:i + 1024]
        if np.abs(w).mean() < 400: continue
        c = np.correlate(w, w, 'full')[1023:]; lo, hi = fs // 350, fs // 80; k = lo + np.argmax(c[lo:hi])
        if c[k] > 0.3 * c[0]: out.append(fs / k)
    return float(np.median(out)) if out else 0
for name in B.LINES:
    f = B.TK / f"{name}.mp4"
    if not f.exists(): print(f"{name:14s} --"); continue
    ws = B.words(name); miss = B.check_words(name, ws)
    print(f"{name:14s} {B.dur(f):5.1f}s  f0 {f0(f):4.0f} Hz  speech {ws[0][1]:.2f}-{ws[-1][2]:.2f}  " + ("OK" if not miss else f"DIFF {miss}"))
