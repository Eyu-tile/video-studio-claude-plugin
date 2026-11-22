#!/usr/bin/env python3
"""Generated footage (AI presenter / talking head, b-roll, images, voice) as tracked jobs.

Python can't call MCP tools; Claude can. So the work is split: `vs gen` plans every generation as
a job with its exact inputs and dependencies, Claude runs each job with the connected generator
(Higgsfield MCP: Soul ID character, Seed Audio voice, Seedance talking clips, image and video models;
or any other provider), records the result here, and `vs gen` downloads, checks and assembles it into
an EDL so the edit continues with /ugc-ads and /video-edit.

Script (work/gen/<v>.script.json, written by Claude from the ad plan):
  {"variant": "v1", "aspect": "9:16",
   "presenter": {"name": "Maya", "look": "woman, early 30s, ... (or an existing Soul ID name)",
                 "voice": "warm, conversational, US", "setting": "bright kitchen, morning window light",
                 "consent": "fictional | real person with written consent: <who/when>"},
   "lines": [{"beat": "hook", "say": "My knees used to scream on the stairs.", "show": "talking",
              "perform": "wince on 'scream', small laugh after"},
             {"beat": "demo", "say": "Now I just slip this on...", "show": "broll",
              "broll": "hands wrapping a knee sleeve on a wooden stair, close-up", "source": "generate"}]}

  vs gen plan work/gen/v1.script.json            -> work/gen/v1.jobs.json (+ printed plan, generation count)
  vs gen next work/gen/v1.jobs.json              the jobs that are ready now, with their full inputs
  vs gen done work/gen/v1.jobs.json <job> --url <result url> [--model seedance-2.5 --credits 3.8 --ref <asset id>]
  vs gen fail work/gen/v1.jobs.json <job> --why "..."        (then edit the prompt and `vs gen retry`)
  vs gen retry work/gen/v1.jobs.json <job>
  vs gen list work/gen/v1.jobs.json
  vs gen fetch work/gen/v1.jobs.json --project <dir>        download results to raw/gen/, check, log credits
  vs gen edl work/gen/v1.jobs.json -o work/ads/v1.edl.json  talking clips in order + b-roll over its lines
"""
import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from vs_common import die, fmt_ts, load_json, probe, save_json  # noqa: E402

WPM = 155
MAX_CLIP = 12.0  # seconds of speech per talking clip (Seedance-class models: keep well under 15 s)
LOOK = ("Authentic phone-camera video look: true-to-life skin texture, no beauty filter, faint sensor noise, "
        "deep focus. One person only, no text, no watermark.")


def est(text):
    return max(len(text.split()) / WPM * 60, 1.0)


def clips_of(lines, max_clip):
    """Group lines into talking clips (consecutive speech, <= max_clip s, split at beat changes if long)."""
    clips, cur, t = [], [], 0.0
    for i, ln in enumerate(lines):
        d = est(ln.get("say", ""))
        if cur and t + d > max_clip:
            clips.append(cur)
            cur, t = [], 0.0
        cur.append(i)
        t += d
    if cur:
        clips.append(cur)
    return clips


def frame_prompt(p, aspect):
    orient = "Vertical 9:16" if aspect == "9:16" else ("Square 1:1" if aspect == "1:1" else "Horizontal 16:9")
    return (f"{orient} talking-head portrait, chest-up framing, subject centred, looking directly into the camera, "
            f"calm neutral expression, lips gently closed. {p.get('look', '')}. Setting: {p.get('setting', '')}. "
            f"Hands relaxed. {LOOK}")


def video_prompt(p, lines, aspect):
    perf = "; ".join(f"on \"{ln['say'][:40]}\" {ln['perform']}" for ln in lines if ln.get("perform"))
    return (f"Static handheld-phone {('vertical' if aspect == '9:16' else 'horizontal')} talking-head video, framing "
            f"identical to the start frame from first to last frame. The exact person from the start frame "
            f"({p.get('look', '')}) speaks directly into the lens for the entire clip, lips in precise sync with the "
            f"spoken words. Performance: {perf or 'natural, friendly, energy rising slightly toward the end'}. "
            f"Natural blinks, small natural hand movement, gentle breathing; in the final half second a relaxed "
            f"pause. Background static. {LOOK}")


def cmd_plan(a):
    s = load_json(a.script)
    p, lines = s.get("presenter", {}), s.get("lines", [])
    if not lines:
        die("script has no lines")
    if not str(p.get("consent", "")).strip():
        die("presenter.consent is empty: say 'fictional', or name the real person and their written consent")
    aspect = s.get("aspect", "9:16")
    v = s.get("variant", Path(a.script).stem.split(".")[0])
    jobs = []

    def job(jid, kind, needs=(), **kw):
        jobs.append({"id": jid, "kind": kind, "needs": list(needs), "status": "todo", **kw})
    has_talking = any(ln.get("show", "talking") != "broll" or ln.get("say") for ln in lines)
    if has_talking:
        if p.get("soul_id"):
            job("character", "character", status_note="existing", result={"ref": p["soul_id"]})
            jobs[-1]["status"] = "done"
        else:
            job("character", "character", tool="Soul ID (train) or an image model for a reference set",
                prompt=f"A fictional presenter: {p.get('look', '')}. Reference set of 20-80 images: varied angles, "
                       f"expressions, one full-height shot. {LOOK}",
                note="Train once; reuse by name in every later generation (this and future ads).")
        job("voice", "voice", tool="Seed Audio preset voice (or a clone of a voice you have permission to use)",
            prompt=f"Pick a preset voice: {p.get('voice', 'natural, conversational')}. Record its id/name.")
    for ci, idx in enumerate(clips_of(lines, a.max_clip) if has_talking else []):
        cl = [lines[i] for i in idx]
        text = " ".join(ln["say"].strip() for ln in cl if ln.get("say"))
        n = ci + 1
        job(f"speech{n}", "speech", ["voice"], tool="Seed Audio text to speech", text=text,
            expect_seconds=round(est(text), 1), lines=idx)
        job(f"frame{n}", "frame", ["character"], tool="image with the trained character (Soul ID)",
            prompt=frame_prompt(p, aspect), aspect=aspect,
            note="Reuse frame1's result for later clips in the same setting unless the setting changes.")
        job(f"talk{n}", "talking", [f"speech{n}", f"frame{n}"], tool="Seedance 2.5 (start frame + audio + prompt)",
            prompt=video_prompt(p, cl, aspect), aspect=aspect, expect_seconds=round(est(text), 1), lines=idx)
    for i, ln in enumerate(lines):
        if ln.get("show") == "broll" and ln.get("source", "generate") == "generate":
            job(f"broll{i + 1}", "broll", [], tool="image-to-video or text-to-video model",
                prompt=f"{ln.get('broll', ln.get('say', ''))}. {'Vertical 9:16' if aspect == '9:16' else aspect} "
                       f"phone-shot b-roll, real hands and real places, natural light, smooth slight handheld motion. "
                       f"No text, no watermark, no logos except the product's own.",
                aspect=aspect, line=i, expect_seconds=round(est(ln.get("say", "x x x")) + 0.5, 1))
    from higgsfield import active_state, billing_check
    st = active_state(a.project)
    acct = a.account or s.get("account") or st["account"]
    wsid = s.get("workspace_id") or (st["workspace_id"] if acct == st["account"] else None)
    doc = {"variant": v, "script": a.script, "aspect": aspect, "presenter": p, "lines": lines,
           "account": acct, "workspace_id": wsid, "tool_prefix": f"mcp__{acct}__",
           "before_billing": billing_check(acct, wsid),
           "created": time.strftime("%Y-%m-%d %H:%M"), "jobs": jobs}
    out = Path(a.out or Path(a.script).with_name(f"{v}.jobs.json"))
    save_json(out, doc)
    gens = sum(j["status"] == "todo" for j in jobs)
    print(f"{len(jobs)} jobs ({gens} generations) -> {out}; account {acct}"
          f"{' team workspace ' + wsid if wsid else ''} (tools mcp__{acct}__*)")
    print(f"Before the first generation: {doc['before_billing']}.")
    for j in jobs:
        print(f"  {j['id']:<10} {j['kind']:<9} needs {','.join(j['needs']) or '-':<16} {j.get('tool', '')}")
    print("Confirm the plan and the provider's price estimate with the person before generating.")


def ready(doc):
    done = {j["id"] for j in doc["jobs"] if j["status"] == "done"}
    return [j for j in doc["jobs"] if j["status"] in ("todo", "retry") and all(n in done for n in j["needs"])]


def resolve(doc, j):
    """The job with its dependencies' results filled in."""
    by = {x["id"]: x for x in doc["jobs"]}
    inputs = {n: by[n].get("result", {}) for n in j["needs"]}
    return {**j, "inputs": inputs}


def cmd_next(a):
    doc = load_json(a.jobs)
    r = ready(doc)
    if not r:
        left = [j["id"] for j in doc["jobs"] if j["status"] != "done"]
        print("all jobs done: vs gen fetch, then vs gen edl" if not left else f"nothing ready; waiting on: {left}")
        return
    for j in r:
        print(json.dumps(resolve(doc, j), indent=1, ensure_ascii=False))
    if doc.get("account"):
        print(f"\nUse the {doc['account']} connection (tools {doc['tool_prefix']}*), not another Higgsfield account."
              + (f" Bill team workspace {doc['workspace_id']}." if doc.get("workspace_id") else ""))
    print(f"\n{len(r)} job(s) ready. Run each with the generator, then: vs gen done {a.jobs} <id> --url <result>")


def find(doc, jid):
    j = next((x for x in doc["jobs"] if x["id"] == jid), None)
    if not j:
        die(f"no job {jid} (vs gen list)")
    return j


def cmd_done(a):
    doc = load_json(a.jobs)
    j = find(doc, a.id)
    if not (a.url or a.ref or a.file):
        die("give --url (a downloadable result), --file, or --ref (an asset/voice/character id)")
    j["status"] = "done"
    j["result"] = {k: v for k, v in (("url", a.url), ("file", a.file), ("ref", a.ref), ("model", a.model),
                                     ("credits", a.credits)) if v is not None}
    j["finished"] = time.strftime("%Y-%m-%d %H:%M")
    save_json(a.jobs, doc)
    print(f"{a.id}: done. Ready next: {', '.join(x['id'] for x in ready(doc)) or 'nothing'}")


def cmd_fail(a):
    doc = load_json(a.jobs)
    j = find(doc, a.id)
    j["status"], j["why"] = "failed", a.why
    save_json(a.jobs, doc)
    print(f"{a.id}: failed ({a.why}). Edit its prompt in {a.jobs}, then: vs gen retry {a.jobs} {a.id}")


def cmd_retry(a):
    doc = load_json(a.jobs)
    j = find(doc, a.id)
    j["status"] = "retry"
    j.pop("result", None)
    save_json(a.jobs, doc)
    print(f"{a.id}: queued again")


def cmd_list(a):
    doc = load_json(a.jobs)
    cr = 0.0
    for j in doc["jobs"]:
        r = j.get("result", {})
        cr += float(r.get("credits") or 0)
        print(f"  {j['id']:<10} {j['kind']:<9} {j['status']:<7} {r.get('model', '') or ''}"
              f"{'  ' + str(r.get('file') or r.get('url') or r.get('ref') or '')[:70] if r else ''}")
    print(f"ready: {', '.join(x['id'] for x in ready(doc)) or '-'}; credits used: {cr:g}")


def cmd_fetch(a):
    from watch import http_get
    doc = load_json(a.jobs)
    proj = Path(a.project)
    dest_dir = proj / "raw" / "gen"
    dest_dir.mkdir(parents=True, exist_ok=True)
    problems, n = [], 0
    for j in doc["jobs"]:
        r = j.get("result", {})
        if j["status"] != "done" or j["kind"] not in ("talking", "broll", "frame", "speech"):
            continue
        ext = {"talking": ".mp4", "broll": ".mp4", "frame": ".png", "speech": ".wav"}[j["kind"]]
        if r.get("file") and Path(r["file"]).exists():
            src = Path(r["file"])
            f = dest_dir / f"{doc['variant']}_{j['id']}{src.suffix or ext}"
            if src.resolve() != f.resolve():
                f.write_bytes(src.read_bytes())
        elif r.get("url"):
            m = re.search(r"\.(mp4|mov|webm|png|jpe?g|webp|wav|mp3|m4a)(?:\?|$)", r["url"], re.I)
            f = dest_dir / f"{doc['variant']}_{j['id']}{'.' + m.group(1).lower() if m else ext}"
            if not f.exists() or a.force:
                http_get(r["url"], f, timeout=600)
        else:
            continue
        j["local"] = str(f)
        n += 1
        if j["kind"] in ("talking", "broll"):
            info = probe(str(f))
            if not info["has_video"]:
                problems.append(f"{j['id']}: no video stream")
            if j["kind"] == "talking":
                if not info["has_audio"]:
                    problems.append(f"{j['id']}: talking clip has no audio (lip-synced clips must carry the speech)")
                exp = j.get("expect_seconds")
                if exp and abs(info["duration"] - exp) > max(2.0, 0.35 * exp):
                    problems.append(f"{j['id']}: {info['duration']:.1f}s, expected ~{exp:.1f}s: check it isn't cut off")
    save_json(a.jobs, doc)
    # Credits ledger: generated media is labelled as such.
    led = proj / "assets" / "credits.json"
    entries = load_json(led) if led.exists() else []
    known = {e.get("file") for e in entries}
    for j in doc["jobs"]:
        if j.get("local") and j["local"] not in known:
            entries.append({"file": j["local"], "kind": j["kind"], "source": j.get("result", {}).get("url", "generated"),
                            "license": "AI-generated (provider terms apply)", "author": j.get("result", {}).get("model"),
                            "attribution_required": False, "ai_generated": True, "prompt": j.get("prompt") or j.get("text"),
                            "downloaded": time.strftime("%Y-%m-%dT%H:%M:%S")})
    save_json(led, entries)
    for pr in problems:
        print(f"  check: {pr}")
    print(f"fetched {n} result(s) -> {dest_dir}" + (f"; {len(problems)} to check" if problems else ""))


def line_times(clip_file, lines, idx, transcript=None):
    """Start/end of each script line inside a talking clip: from a transcript when there is one, else
    proportional to word counts."""
    dur = probe(str(clip_file))["duration"]
    counts = [max(len(lines[i].get("say", "").split()), 1) for i in idx]
    words = (transcript or {}).get("words", [])
    out, k = {}, 0
    if words and abs(len(words) - sum(counts)) <= max(2, 0.2 * sum(counts)):
        for i, c in zip(idx, counts):
            seg = words[k:k + c] or words[-1:]
            out[i] = (seg[0]["s"], seg[-1]["e"])
            k += c
        return out
    t, total = 0.0, sum(counts)
    for i, c in zip(idx, counts):
        d = dur * c / total
        out[i] = (t, t + d)
        t += d
    return out


def cmd_edl(a):
    doc = load_json(a.jobs)
    lines = doc["lines"]
    talks = [j for j in doc["jobs"] if j["kind"] == "talking"]
    if not talks:
        die("no talking clips in this plan")
    missing = [j["id"] for j in talks if not j.get("local")]
    if missing:
        die(f"not fetched yet: {missing} (vs gen fetch)")
    segs, overlays, t0, placed = [], [], 0.0, {}
    for j in talks:
        f = j["local"]
        d = probe(f)["duration"]
        tr = None
        tpath = Path(f).with_suffix(".transcript.json")
        if not tpath.exists() and not a.no_transcribe:
            subprocess.run([sys.executable, str(Path(__file__).parent / "transcribe.py"), f, "-o",
                            str(tpath.with_suffix("")), "--model", "small"], capture_output=True, text=True)
        if tpath.exists():
            tr = json.loads(tpath.read_text())
        times = line_times(f, lines, j["lines"], tr)
        segs.append({"src": f, "start": 0, "end": round(d, 3), "note": " / ".join(lines[i]["say"][:30] for i in j["lines"])})
        for i, (s, e) in times.items():
            placed[i] = (t0 + s, t0 + e)
        t0 += d
    brolls = {j["line"]: j for j in doc["jobs"] if j["kind"] == "broll" and j.get("local")}
    todo = []
    for i, ln in enumerate(lines):
        if ln.get("show") != "broll" or i not in placed:
            continue
        s, e = placed[i]
        if i in brolls:
            overlays.append({"file": brolls[i]["local"], "start": round(s, 3), "end": round(e, 3), "fit": True})
        else:
            todo.append(f"line {i + 1} ({fmt_ts(s)[1:]}-{fmt_ts(e)[1:]}): b-roll from {ln.get('source', 'library')}: "
                        f"{ln.get('broll', '')}")
    edl = {"segments": segs, "overlays": overlays, "_generated_from": a.jobs}
    if a.out and Path(a.out).exists() and not a.force:
        die(f"{a.out} exists (use --force, or vs edl to change it)")
    save_json(a.out, edl)
    print(f"EDL -> {a.out}: {len(segs)} talking clip(s), {len(overlays)} generated b-roll overlay(s), {t0:.1f}s")
    for t in todo:
        print(f"  add footage: {t}")
    print("Next: captions, texts (hook + CTA), music, then vs review --brief (see /ugc-ads).")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("plan")
    p.add_argument("script")
    p.add_argument("-o", "--out")
    p.add_argument("--max-clip", type=float, default=MAX_CLIP)
    p.add_argument("--account", help="Higgsfield connection to use (default: vs higgsfield current)")
    p.add_argument("--project", help="project folder, for its active account")
    for name in ("next", "list"):
        sub.add_parser(name).add_argument("jobs")
    d = sub.add_parser("done")
    d.add_argument("jobs")
    d.add_argument("id")
    d.add_argument("--url")
    d.add_argument("--file")
    d.add_argument("--ref")
    d.add_argument("--model")
    d.add_argument("--credits", type=float)
    f = sub.add_parser("fail")
    f.add_argument("jobs")
    f.add_argument("id")
    f.add_argument("--why", required=True)
    r = sub.add_parser("retry")
    r.add_argument("jobs")
    r.add_argument("id")
    g = sub.add_parser("fetch")
    g.add_argument("jobs")
    g.add_argument("--project", required=True, help="project folder (raw/gen/ and assets/credits.json)")
    g.add_argument("--force", action="store_true")
    e = sub.add_parser("edl")
    e.add_argument("jobs")
    e.add_argument("-o", "--out", required=True)
    e.add_argument("--force", action="store_true")
    e.add_argument("--no-transcribe", action="store_true")
    args = ap.parse_args()
    {"plan": cmd_plan, "next": cmd_next, "list": cmd_list, "done": cmd_done, "fail": cmd_fail, "retry": cmd_retry,
     "fetch": cmd_fetch, "edl": cmd_edl}[args.cmd](args)


if __name__ == "__main__":
    main()
