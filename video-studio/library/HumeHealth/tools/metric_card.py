# Metric card: one still frame of a Hume app screen recording, full-width 9:16 crop with the metric row at ~38% height,
# red rounded box around the row (label + value) that fades in, slow 1.00 -> 1.04 push-in. Output: 2.8 s 1080x1920 mp4.
# usage: python3 -I metric_card.py SRC T LABEL_REGEX OUT.mp4 [ROW_TARGET_Y=0.38]
import sys, re, subprocess, json, os, tempfile
from PIL import Image, ImageDraw
from rapidocr_onnxruntime import RapidOCR
src, t, rx, out = sys.argv[1], float(sys.argv[2]), sys.argv[3], sys.argv[4]
TY = float(sys.argv[5]) if len(sys.argv) > 5 and not sys.argv[5].startswith('--') else 0.38
tmp = tempfile.mkdtemp(); full = f"{tmp}/full.png"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", src, "-frames:v", "1", full], check=True)
im = Image.open(full).convert("RGB"); W0, H0 = im.size
ocr = RapidOCR(); res, _ = ocr(full)
boxes = [([min(p[0] for p in b), min(p[1] for p in b), max(p[0] for p in b), max(p[1] for p in b)], txt) for b, txt, c in (res or [])]
lab = [b for b, txt in boxes if re.search(rx, txt.replace(" ", ""), re.I)]
if not lab: sys.exit(f"label {rx!r} not found at t={t}: " + " | ".join(txt for _, txt in boxes)[:400])
L = min(lab, key=lambda b: b[1])
# value boxes: numbers / status words on the same row or just under the label (cards put the value below the label)
rowh = L[3] - L[1]
vals = [b for b, txt in boxes if b is not L and re.search(r"\d|standard|high|low|excellent|good", txt, re.I)
        and L[1] - rowh * 1.2 <= (b[1] + b[3]) / 2 <= L[3] + rowh * 4.2 and b[0] > 0]
GRID = "--grid" in sys.argv          # side-by-side tiles (e.g. Age | Metabolic Age | Height): keep only values under the label
if GRID: vals = [v for v in vals if L[0] - 60 <= (v[0] + v[2]) / 2 <= L[2] + 60]
x0 = min([L[0]] + [v[0] for v in vals]); y0 = min([L[1]] + [v[1] for v in vals]); y1 = max([L[3]] + [v[3] for v in vals])
x1g = max([L[2]] + [v[2] for v in vals])
# 9:16 crop, full width, row centred at TY
cw = W0; ch = int(round(cw * 16 / 9))
if ch > H0: ch = H0; cw = int(round(ch * 9 / 16))
cx = (W0 - cw) // 2; cy = int(min(max(0, (y0 + y1) / 2 - ch * TY), H0 - ch))
card = im.crop((cx, cy, cx + cw, cy + ch)).resize((1080, 1920), Image.LANCZOS); s = 1080 / cw
bx = [max(20, (x0 - cx) * s - 28), (y0 - cy) * s - 22, ((x1g - cx) * s + 28) if GRID else 1080 - 26, (y1 - cy) * s + 22]
card.save(f"{tmp}/card.png")
mk = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0)); ImageDraw.Draw(mk).rounded_rectangle(bx, radius=26, outline=(255, 75, 75, 255), width=10)
mk.save(f"{tmp}/mark.png")
fc = ("[1:v]format=rgba,fade=t=in:st=0.25:d=0.25:alpha=1[m];[0:v][m]overlay=0:0,format=yuv420p,"
      "zoompan=z='1+0.04*on/84':x='iw/2-(iw/zoom/2)':y='ih*%.3f-(ih/zoom)*%.3f':d=1:s=1080x1920:fps=30[v]" % ((bx[1] + bx[3]) / 2 / 1920, (bx[1] + bx[3]) / 2 / 1920))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-t", "2.8", "-framerate", "30", "-i", f"{tmp}/card.png", "-loop", "1", "-t", "2.8", "-framerate", "30", "-i", f"{tmp}/mark.png",
                "-filter_complex", fc, "-map", "[v]", "-t", "2.8", "-c:v", "libx264", "-crf", "16", "-preset", "fast", "-pix_fmt", "yuv420p", out], check=True)
Image.open(f"{tmp}/card.png").convert("RGBA").__class__
prev = Image.alpha_composite(card.convert("RGBA"), mk); prev.convert("RGB").resize((270, 480)).save(out[:-4] + "_preview.jpg")
print(os.path.basename(out), "label", [txt for b, txt in boxes if b is L], "values", [txt for b, txt in boxes if b in vals], "box", [int(v) for v in bx])
