# OCR full-screen app recordings at 2 fps and record, per metric, where its row sits on screen (y as fraction of height).
# usage: python3 -I app_rows.py OUT_JSON VIDEO [VIDEO ...]
import sys, json, re, subprocess, os, glob, tempfile
from rapidocr_onnxruntime import RapidOCR
OUT, vids = sys.argv[1], sys.argv[2:]
RX = {"body fat %": r"body ?fat ?percent", "metabolic age": r"metabolic ?age", "bmr": r"basal ?metabolic|\bbmr\b|resting metabolic",
      "visceral fat": r"visceral", "body water %": r"body ?water ?percent|body ?water", "muscle mass": r"skeletal ?muscle ?mass|muscle ?mass",
      "goals": r"goal", "weigh-in time": r"weigh.?in|best time", "health score": r"health ?score"}
ocr = RapidOCR(); res = {}
for v in vids:
    d = tempfile.mkdtemp(); subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", v, "-vf", "fps=2,scale=720:-2", "-q:v", "3", f"{d}/%04d.jpg"])
    fr = sorted(glob.glob(f"{d}/*.jpg")); rows = []
    for k, f in enumerate(fr):
        r, _ = ocr(f)
        if not r: continue
        from PIL import Image
        H = Image.open(f).height
        for box, txt, conf in r:
            for m, rx in RX.items():
                if re.search(rx, txt, re.I):
                    y = sum(p[1] for p in box) / 4 / H
                    rows.append({"t": k / 2, "metric": m, "y": round(y, 3), "text": txt})
    res[os.path.basename(v)] = rows
    print(os.path.basename(v), len(fr), sorted({x["metric"] for x in rows}), flush=True)
json.dump(res, open(OUT, "w"), indent=0)
