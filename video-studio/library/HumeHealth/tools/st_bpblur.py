# Blur the numbers of the Blood Pressure card on a scrolling app recording, frame by frame (OCR finds the card as it moves):
# the reading ("~122/70 mmHg"), the date line and the chart's axis numbers inside the card are blurred; the label stays.
# usage: python3 -I st_bpblur.py IN.mp4 START DUR OUT.mp4
import sys, os, re, glob, subprocess, tempfile
from PIL import Image, ImageFilter
from rapidocr_onnxruntime import RapidOCR
src, a0, dur, out = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
tmp = tempfile.mkdtemp()
subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{a0:.3f}", "-t", f"{dur:.3f}", "-i", src, "-vf",
                "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30", f"{tmp}/%04d.png"], check=True)
ocr = RapidOCR(); last = None; n_hit = 0
for f in sorted(glob.glob(f"{tmp}/*.png")):
    im = Image.open(f).convert("RGB"); res, _ = ocr(f); bx = [([min(p[0] for p in b), min(p[1] for p in b), max(p[0] for p in b), max(p[1] for p in b)], t) for b, t, c in (res or [])]
    # anchor = top of the "Blood Pressure" label, from whichever card element is on screen (measured layout of this card)
    L1 = None
    for b, t in bx:
        tt = t.replace(" ", "").lower()
        if "bloodpressure" in tt: L1 = b[1]; break
    if L1 is None:
        for b, t in bx:
            tt = t.replace(" ", "").lower()
            if tt == "beta": L1 = b[1] + 3; break
            if "mmhg" in tt: L1 = b[1] - 144; break
            if re.search(r"~?\d{2,3}/\d{2,3}", tt): L1 = b[1] - 130; break
    regs = []
    if L1 is not None:
        regs = [(75, L1 + 118, 495, L1 + 252), (945, L1 + 88, 1035, L1 + 256)]   # reading + date line; axis numbers
    for x0, y0_, x1, y1_ in regs:
        r = tuple(int(max(0, v)) for v in (x0, y0_, min(1080, x1), min(1920, y1_)))
        if r[2] - r[0] > 4 and r[3] - r[1] > 4:
            im.paste(im.crop(r).filter(ImageFilter.GaussianBlur(18)), r[:2]); n_hit += 1
    im.save(f)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", "30", "-i", f"{tmp}/%04d.png", "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", out], check=True)
for f in glob.glob(f"{tmp}/*.png"): os.remove(f)
print(os.path.basename(out), "blurred regions", n_hit)
