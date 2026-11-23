#!/usr/bin/env python3
"""v2 captions: whisper the render, force the words back to the locked script (same alignment as v1), bold-pop,
one fixed spot inside the safe zone (bottom of the caption at y 1330 on 1080x1920), none over the end card.
make_captions_v2.py h1 out/v2/raw_h1.mp4"""
import difflib, json, re, subprocess, sys
from pathlib import Path
B = Path(__file__).resolve().parent; sys.path.insert(0, str(B.parent))
from check_script import norm
from check_clips import n2
P = Path("/home/user/video-studio-claude-plugin/video-studio/projects/rootout-set4"); V2 = P / "v2"
VS = "/home/user/video-studio-claude-plugin/plugins/video-studio/bin/vs"
h, render = sys.argv[1], P / sys.argv[2]
tx = V2 / f"edl/tx_render_{h}.json"
if not tx.exists() or tx.stat().st_mtime < render.stat().st_mtime:
    subprocess.run([VS, "transcribe", str(render), "-o", str(tx.with_suffix("")), "--model", "medium.en"], check=True, capture_output=True)
d = json.loads(tx.read_text()); out = d["words"]
L = json.loads((B.parent / "SCRIPT_LOCK.json").read_text())["lines"]
hook = {"h1": ["h1"], "h2": ["h2a", "h2b"], "h3": ["h3"]}[h]
script = " ".join(l["text"] for l in L if l["id"] in hook or not l["id"].startswith("h")).split()
key = lambda tok: "".join(n2(norm(tok))) or tok.lower()
sm = difflib.SequenceMatcher(a=[key(w["w"]) for w in out], b=[key(t) for t in script], autojunk=False); al = []
for op, a0, a1, b0, b1 in sm.get_opcodes():
    if op == "equal":
        for i, j in zip(range(a0, a1), range(b0, b1)): al.append(dict(out[i], w=script[j]))
    elif op in ("replace", "insert"):
        src = out[a0:a1]; t0 = src[0]["s"] if src else (al[-1]["e"] if al else 0.0)
        t1 = src[-1]["e"] if src else (out[a1]["s"] if a1 < len(out) else t0 + 0.4 * (b1 - b0))
        n = b1 - b0; step = max((t1 - t0) / max(n, 1), 0.12)
        for k, j in enumerate(range(b0, b1)): al.append({"w": script[j], "s": round(t0 + k * step, 3), "e": round(t0 + (k + 1) * step, 3)})
        print("caption fix:", " ".join(w["w"] for w in src) or "(missed)", "->", " ".join(script[b0:b1]))
    else:
        print("caption drop (not in script):", " ".join(w["w"] for w in out[a0:a1]))
pos = json.loads((V2 / f"edl/set4v2_{h}.pos.json").read_text()); end_at = pos[-1][2]
al = [w for w in al if w["s"] < end_at - 0.02]
d["words"] = al; d.pop("segments", None)
fx = V2 / f"edl/tx_render_{h}_fixed.json"; fx.write_text(json.dumps(d, indent=1))
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(render)], capture_output=True, text=True).stdout)
ide = V2 / f"edl/identity_{h}.edl.json"; ide.write_text(json.dumps({"segments": [{"src": str(render), "start": 0, "end": round(dur, 3)}]}))
cap = V2 / f"edl/captions_{h}"
subprocess.run([VS, "captions", str(fx), str(ide), "-o", str(cap), "--style", "bold-pop", "--aspect", "9:16", "--accent", "#FFD400", "--font", "Inter"], check=True, capture_output=True)
BOXED = ("offer", "R_pdp_scroll", "phone_delete", "g_calendar")
boxwin = [(p[2], p[2] + p[3]) for p in pos if p[1] in BOXED]
def ts(v):
    hh, mm, ss = v.split(":"); return int(hh) * 3600 + int(mm) * 60 + float(ss)
# caption bottom edge per shot (y on 1080x1920); default 1330. Shots with the bottle low in frame get the caption above it.
CAPY = {"P2_slidein": 760, "P3_hero_wide": 525, "P4_flatlay": 470, "M6b_safe": 1190, "P6_clinicdesk": 510, "P7_nightkit": 650,
        "P8_timelapse": 740, "M7_cap": 520, "i16_bottles": 720}
capwin = [(p[2], p[2] + p[3], CAPY[p[1]]) for p in pos if p[1] in CAPY]
ass = cap.with_suffix(".ass"); lines = []
for ln in ass.read_text().splitlines():
    if ln.startswith("Style: Cap,"):
        lines.append(ln); g = ln.split(","); g[0] = "Style: CapBox"; g[5] = "&H40000000"; g[6] = "&H40000000"; g[15] = "3"; g[16] = "14"; ln = ",".join(g)
    if ln.startswith("Dialogue:"):
        f = ln.split(",", 9); st = ts(f[1])
        if any(a - 0.05 <= st < b for a, b in boxwin): f[3] = "CapBox"
        y = next((yy for a, b, yy in capwin if a - 0.05 <= st < b), 1330)
        f[9] = "{\\an2\\pos(491,%d)}" % y + re.sub(r"^\{\\an\d\\pos\([^)]*\)\}", "", f[9]); ln = ",".join(f)
    lines.append(ln)
ass.write_text("\n".join(lines) + "\n"); print("captions", ass)
