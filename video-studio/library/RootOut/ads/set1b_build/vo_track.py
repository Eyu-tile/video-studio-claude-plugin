# Assemble the VO track for each hook variant; writes work/vo_<H>.wav + work/lines_<H>.json (line start/end)
import json, subprocess, sys
W = "work/vo2/"
BODY = ["k07","k08","k09","m01","m02","k10","m03","k11","m04","m05","k12","m06","k13","m07","k14","k15","t01","t02","t03","k16","m08"]
HOOKS = {"H1": ["k01","k02"], "H2": ["k03","k04"], "H3": ["k05","k06"]}
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]))
def spk(l): return l[0]
for h, hook in HOOKS.items():
    seq = hook + BODY; t = 0.15; lines = []; parts = []
    for i, l in enumerate(seq):
        gap = 0 if i == 0 else (0.45 if spk(l) != spk(seq[i-1]) or l.startswith("t") else 0.28)
        t += gap; d = dur(W + l + ".wav"); lines.append({"id": l, "s": round(t, 3), "e": round(t + d, 3)}); t += d
    total = t
    flt = "".join(f"[{i}:a]adelay={int(x['s']*1000)}|{int(x['s']*1000)}[a{i}];" for i, x in enumerate(lines))
    flt += "".join(f"[a{i}]" for i in range(len(lines))) + f"amix=inputs={len(lines)}:normalize=0,apad=whole_dur={total+0.05}[o]"
    cmd = ["ffmpeg","-v","error","-y"] + sum([["-i", W + x["id"] + ".wav"] for x in lines], []) + ["-filter_complex", flt, "-map", "[o]", "-ar", "48000", "-ac", "1", f"work/vo_{h}.wav"]
    subprocess.run(cmd, check=True)
    json.dump({"total": round(total, 3), "lines": lines}, open(f"work/lines_{h}.json", "w"), indent=1)
    print(h, round(total, 2))
