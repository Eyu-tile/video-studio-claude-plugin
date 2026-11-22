# Find windows where a metric row stays still on screen (for a static marker). usage: python3 -I app_windows.py ROWS_JSON... 
import json, sys, collections
for f in sys.argv[1:]:
    for v, rows in json.load(open(f)).items():
        g = collections.defaultdict(dict)
        for x in rows: g[x["metric"]][x["t"]] = x["y"]
        for m, ty in g.items():
            ts = sorted(ty); out = []
            i = 0
            while i < len(ts):
                j = i
                while j + 1 < len(ts) and ts[j + 1] - ts[j] <= 0.5 and abs(ty[ts[j + 1]] - ty[ts[i]]) < 0.02: j += 1
                if ts[j] - ts[i] >= 2.0: out.append((ts[i], ts[j], round(ty[ts[i]], 2)))
                i = j + 1
            if out: print(f"{v[:12]:12s} {m:14s} {out}")
