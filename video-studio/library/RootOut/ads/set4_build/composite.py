#!/usr/bin/env python3
"""Key the green-wall mom clip and lay her over a cut-away background (TikTok green-screen look).
composite.py <mom.mp4> <bg.mp4|png> <out.mp4> [--ss S --to T --scale 1.0 --y 760 --x 0]
Keeps the mom clip's own (lip-synced) audio. Output 1080x1920 30 fps."""
import argparse, subprocess
import numpy as np

W, H, FPS = 1080, 1920, 30

def reader(cmd, w, h):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL); n = w * h * 3
    while True:
        b = p.stdout.read(n)
        if len(b) < n: return
        yield np.frombuffer(b, np.uint8).reshape(h, w, 3)

def key(fr):
    f = fr.astype(np.float32); r, g, b = f[..., 0], f[..., 1], f[..., 2]
    gd = g - np.maximum(r, b)                      # how green a pixel is
    a = 1.0 - np.clip((gd - 28.0) / (70.0 - 28.0), 0, 1)
    g2 = np.minimum(g, np.maximum(r, b) * 1.02 + 4)  # spill suppression
    out = np.stack([r, g2, b], -1)
    return out, a

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("mom"); ap.add_argument("bg"); ap.add_argument("out")
    ap.add_argument("--ss", type=float, default=0.0); ap.add_argument("--to", type=float, default=None)
    ap.add_argument("--scale", type=float, default=1.0); ap.add_argument("--y", type=int, default=760); ap.add_argument("--x", type=int, default=0); ap.add_argument("--trim", type=int, default=28)
    a = ap.parse_args()
    dur = (a.to - a.ss) if a.to else None
    mw = int(W * a.scale) // 2 * 2; mh = int(mw * 16 / 9) // 2 * 2
    tcut = ["-t", f"{dur:.3f}"] if dur else []
    mom = reader(["ffmpeg", "-v", "error", "-ss", f"{a.ss:.3f}", *tcut, "-i", a.mom, "-vf", f"fps={FPS},crop=iw-{2*a.trim}:ih*(iw-{2*a.trim})/iw:{a.trim}:0,scale={mw}:{mh}:flags=bicubic",
                  "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], mw, mh)
    bgin = ["-loop", "1", "-i", a.bg] if a.bg.endswith(".png") else ["-stream_loop", "-1", "-i", a.bg]
    bg = reader(["ffmpeg", "-v", "error", *bgin, "-vf", f"fps={FPS},scale={W}:{H}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], W, H)
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                            "-ss", f"{a.ss:.3f}", *tcut, "-i", a.mom, "-map", "0:v", "-map", "1:a?", "-c:v", "libx264", "-preset", "medium",
                            "-crf", "17", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", a.out], stdin=subprocess.PIPE)
    # soft fade at the clip's side edges so the sweater doesn't end in a hard line when scaled < 1
    edge = np.ones(mw, np.float32)
    if a.scale < 0.999:
        k = max(8, mw // 14); edge[:k] = np.linspace(0, 1, k); edge[-k:] = np.linspace(1, 0, k)
    for fm, fb in zip(mom, bg):
        rgb, al = key(fm); al = al * edge[None, :]
        out = fb.astype(np.float32).copy()
        y0, x0 = a.y, a.x; y1, x1 = min(H, y0 + mh), min(W, x0 + mw)
        sub = (slice(0, y1 - y0), slice(0, x1 - x0))
        A = al[sub][..., None]
        out[y0:y1, x0:x1] = rgb[sub] * A + out[y0:y1, x0:x1] * (1 - A)
        enc.stdin.write(out.clip(0, 255).astype(np.uint8).tobytes())
    enc.stdin.close(); enc.wait(); print("wrote", a.out)

if __name__ == "__main__":
    main()
