# Scrolling metric card (client: metrics are real scrolling app recordings, scroll until the metric arrives, then the red mark animates on).
# The recording plays from A to B (or B back to A with --reverse) retimed to fill DUR-HOLD, then holds on the final frame for HOLD seconds
# while a red rounded box fades in around the metric row(s), with a slow push-in. One fixed 9:16 crop (full width) keeps the row at ~TY.
# usage: python3 -I dx_scroll_card.py SRC A B OUT.mp4 DUR [--hold 0.9] [--ty 0.40] [--reverse] [--tile] [--union] [--fit] RX1 [RX2 ...]
# --union: one box around everything the RXs matched (e.g. a label and its big number on separate lines)
import sys, re, subprocess, tempfile, os
from PIL import Image, ImageDraw
from rapidocr_onnxruntime import RapidOCR
a = sys.argv[1:]
def opt(name, default):
    if name in a: i = a.index(name); v = a[i + 1]; del a[i:i + 2]; return float(v)
    return default
HOLD = opt("--hold", 0.9); TY = opt("--ty", 0.40); BELOW = opt("--below", 2.4)
REV = "--reverse" in a; TILE = "--tile" in a; UNION = "--union" in a; a = [x for x in a if x not in ("--reverse", "--tile", "--union")]
SRC, A, B, OUT, DUR, rxs = a[0], float(a[1]), float(a[2]), a[3], float(a[4]), a[5:]
tmp = tempfile.mkdtemp(); end_t = A if REV else B
subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{end_t:.3f}", "-i", SRC, "-frames:v", "1", f"{tmp}/end.png"], check=True)
im = Image.open(f"{tmp}/end.png").convert("RGB"); W0, H0 = im.size
res, _ = RapidOCR()(f"{tmp}/end.png")
boxes = [([min(p[0] for p in b), min(p[1] for p in b), max(p[0] for p in b), max(p[1] for p in b)], t) for b, t, c in (res or [])]
found = []
for rx in rxs:
    lab = [b for b, t in boxes if re.search(rx, t.replace(" ", ""), re.I)]
    if not lab: sys.exit(f"{rx!r} not found at {end_t}: " + " | ".join(t for _, t in boxes)[:600])
    L = min(lab, key=lambda b: b[1]); rh = L[3] - L[1]
    vals = [b for b, t in boxes if b is not L and re.search(r"\d|standard|high|low|good|excellent", t, re.I) and L[1] - rh * 0.6 <= (b[1] + b[3]) / 2 <= L[3] + rh * BELOW]
    if TILE: vals = [v for v in vals if L[0] - 60 <= v[0] <= L[2] + 80]
    x0 = min([L[0]] + [v[0] for v in vals]); y0 = min([L[1]] + [v[1] for v in vals]); y1 = max([L[3]] + [v[3] for v in vals]); x1 = max([L[2]] + [v[2] for v in vals])
    found.append([x0, y0, x1, y1, [t for b, t in boxes if b is L or b in vals]])
if UNION and len(found) > 1:
    found = [[min(f[0] for f in found), min(f[1] for f in found), max(f[2] for f in found), max(f[3] for f in found), sum((f[4] for f in found), [])]]
# fixed crop: full width, 9:16, row centre at TY of the frame
s = 1080 / W0; ch = round(1920 / s); cy0 = min(f[1] for f in found); cy1 = max(f[3] for f in found)
cy = int(min(max(0, (cy0 + cy1) / 2 - ch * TY), max(0, H0 - ch)))
bxs = []
mk = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0)); d = ImageDraw.Draw(mk)
for x0, y0, x1, y1, _ in found:
    bx = [max(16, x0 * s - 24), (y0 - cy) * s - 18, (x1 * s + 24) if TILE else 1080 - 22, (y1 - cy) * s + 18]
    d.rounded_rectangle(bx, radius=24, outline=(255, 75, 75, 255), width=10); bxs.append([int(v) for v in bx])
mk.save(f"{tmp}/mark.png")
play = DUR - HOLD; seg = abs(B - A); speed = seg / play if play > 0.05 else 1.0
crop = f"scale=1080:-2,crop=1080:1920:0:{int(cy * s)}"
rev = ",reverse" if REV else ""
# part 1: the scroll, retimed to `play` seconds;  part 2: hold on the end frame with the mark
subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{min(A, B):.3f}", "-t", f"{seg:.3f}", "-i", SRC, "-vf",
                f"{crop}{rev},setpts=PTS/{speed:.4f},fps=30,format=yuv420p", "-t", f"{play:.3f}", "-an", "-c:v", "libx264", "-crf", "16", "-preset", "fast", f"{tmp}/p1.mp4"], check=True)
im.resize((1080, round(H0 * s)), Image.LANCZOS).crop((0, int(cy * s), 1080, int(cy * s) + 1920)).save(f"{tmp}/hold.png")
fy = (min(b[1] for b in bxs) + max(b[3] for b in bxs)) / 2 / 1920; n = max(1, int(HOLD * 30))
fc = (f"[1:v]format=rgba,fade=t=in:st=0.12:d=0.25:alpha=1[m];[0:v][m]overlay=0:0,format=yuv420p,"
      f"zoompan=z='1+0.03*on/{n}':x='iw/2-(iw/zoom/2)':y='ih*{fy:.3f}-(ih/zoom)*{fy:.3f}':d=1:s=1080x1920:fps=30[v]")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-t", f"{HOLD:.3f}", "-framerate", "30", "-i", f"{tmp}/hold.png", "-loop", "1", "-t", f"{HOLD:.3f}", "-framerate", "30",
                "-i", f"{tmp}/mark.png", "-filter_complex", fc, "-map", "[v]", "-t", f"{HOLD:.3f}", "-c:v", "libx264", "-crf", "16", "-preset", "fast", "-pix_fmt", "yuv420p", f"{tmp}/p2.mp4"], check=True)
open(f"{tmp}/l.txt", "w").write(f"file '{tmp}/p1.mp4'\nfile '{tmp}/p2.mp4'\n")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{tmp}/l.txt", "-c:v", "libx264", "-crf", "16", "-preset", "fast", "-pix_fmt", "yuv420p", OUT], check=True)
p = Image.open(f"{tmp}/hold.png").convert("RGBA"); p.alpha_composite(mk); p.convert("RGB").resize((270, 480)).save(OUT[:-4] + "_preview.jpg")
print(os.path.basename(OUT), "speed", round(speed, 2), [f[4] for f in found], "boxes", bxs)
