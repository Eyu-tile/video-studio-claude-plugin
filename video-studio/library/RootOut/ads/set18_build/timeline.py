#!/usr/bin/env python3
"""Set 18 shared timing: VO word times (ElevenLabs STT per line), phrase lookup, on-camera pieces per take.
Run as a script to build the lip-sync tracks: work/ls/<take>_lipsync.wav + work/lipsync_map.json."""
import json, re, subprocess, os
from pathlib import Path
P = Path(os.environ.get("S18", "/home/user/video-studio-claude-plugin/video-studio/projects/rootout-set18"))
VO = P / "raw/vo"
def norm(w): return re.sub(r"[^a-z0-9]", "", w.lower())
NUM = {"10": "ten", "14": "fourteen", "90": "ninety"}
def words(line):
    d = json.load(open(VO / f"{line}.stt.json"))
    out = []
    for w in d["words"]:
        if w.get("type") != "word": continue
        for i, part in enumerate(w["text"].replace("-", " ").split()):   # "school kids" -> two words
            n = norm(part); n = NUM.get(n, n)
            out.append((n, w["start"], w["end"]))
    return out
def find(line, phrase):
    """(start, end) seconds of a phrase inside a line's audio."""
    W = words(line); ph = [NUM.get(norm(x), norm(x)) for x in phrase.replace("-", " ").split()]
    ph = [x for x in ph if x]
    seq = [w[0] for w in W]
    # tolerate the STT joining/splitting compound words
    J = lambda s: "".join(s)
    for i in range(len(seq)):
        for j in range(i + 1, min(len(seq), i + len(ph) + 3) + 1):
            if J(seq[i:j]) == J(ph): return W[i][1], W[j - 1][2]
    raise KeyError(f"{line}: {phrase!r} not in {' '.join(seq)}")
def dur(f): return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)]))
TAKES = {
 "K1": [("r01", "If your kid's doctor said Leave the wart it'll go away I'd bet money there's a second one coming Ask me how I know"),
        ("r02", "This is how we finally got rid of it"),
        ("r03", "So we left it"),
        ("r04", "Every week it got a little bigger"),
        ("r05", "She's wanted everything her brother had since she could walk This she got"),
        ("r06", "Turns out there's a real study on this"),
        ("r06", "We got the other half"),
        ("r07", "So let me save you some time and money")],
 "K2a": [("r08", "Congratulations You've got a wart subscription"),
         ("r09", "Acid from the drugstore"),
         ("r09", "The wart doesn't even notice"),
         ("r10", "Same wart")],
 "K2b": [("r12", "You have to get under that hard skin down to the root That's what RootOut does It's an oil with four plants and each one has a job"),
         ("r13", "Tea tree is a thin oil"),
         ("r13", "and it carries the last two plants down with it"),
         ("r14", "And it's made for kids A kids' formula ages four and up No acid no freezing no blister Just a little cool tingle Recommended by pediatricians")],
 "K3": [("r16", "We kept going fourteen more nights to get the roots"),
        ("r18", "so every kid has their own And you've got ninety days If it's not gone every penny comes back"),
        ("r19", "Or you know leave it See how that goes")],
 "Y1": [("r11", "Freezing acid and shaving only snap off the top")],
 "Y2": [("r17", "and I didn't check a single foot")],
}
GAP = 0.45; PAD = 0.12
def build():
    W = P / "work/ls"; W.mkdir(parents=True, exist_ok=True); mp = {}
    for t, segs in TAKES.items():
        parts = []; pos = 0.0; mp[t] = []
        for i, (line, ph) in enumerate(segs):
            a, b = find(line, ph); a = max(0, a - PAD); b = min(dur(VO / f"{line}.mp3"), b + PAD)
            p = W / f"{t}_{i:02d}.wav"
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(VO / f"{line}.mp3"), "-af",
                f"atrim={a:.3f}:{b:.3f},asetpts=N/SR/TB,afade=t=in:d=0.02,afade=t=out:st={b-a-0.04:.3f}:d=0.04,apad=pad_dur={GAP}",
                "-ar", "44100", "-ac", "1", str(p)], check=True)
            mp[t].append({"line": line, "phrase": ph, "src_in": round(a, 3), "src_out": round(b, 3),
                          "take_in": round(pos, 3), "take_out": round(pos + b - a, 3)})
            pos += b - a + GAP; parts.append(p)
        (W / f"{t}.txt").write_text("".join(f"file '{p.name}'\n" for p in parts))
        subprocess.run(f"cd {W} && ffmpeg -v error -y -f concat -safe 0 -i {t}.txt -c:a pcm_s16le {t}_lipsync.wav", shell=True, check=True)
        print(t, round(pos, 2), "s")
    json.dump(mp, open(P / "work/lipsync_map.json", "w"), indent=1)
if __name__ == "__main__": build()
