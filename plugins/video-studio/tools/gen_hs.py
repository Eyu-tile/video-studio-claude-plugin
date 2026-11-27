"""`vs gen` on Hyperscale: shot-on-phone UGC from one character (the HeyGen "Shot-on-iPhone UGC" method,
rebuilt on Hyperscale models).

The method, in order:
  1. character  one selfie-style picture of a real-looking person (GPT Image 2.5, 3-4 candidates, pick one)
  2. sheet      nine angles of the same face in one image (GPT Image 2.5, the pick as identity reference)
  3. master     one still per room that several lines share; other angles = "change only the camera"
  4. still<n>   one new still per script line: new angle, distance or place, built from character + sheet
                (+ the room's master frame, + the brand's real product photos when the product is in shot)
  5. read       ONE voice read of the whole script (ElevenLabs / Gemini TTS on Hyperscale), cut at the
                pauses into one slice per spoken line (`vs gen slice`): one read keeps it one person
  6. talk<n>    the still talks with its slice (OmniHuman 1.5: photo + audio)       [HeyGen Avatar 6]
     broll<n>   hands / props / place from the still, 5 s, one action, keep 1-2 s (Seedance 2.5) [HeyGen Video 1]
     motion<n>  a silent moment of the character from the still (Seedance 2.5) for music-only ads
     (show: still)  no clip: the still itself goes in the cut (frozen selfies, a photo on screen)
  7. edl        cut on the lines: each line whole in its own shot, the read laid back under, pauses trimmed

Claude runs every generation with the Hyperscale MCP (quote first, then generate, then check_generation);
this module plans the jobs with their exact model, inputs and prompts, cuts the read, and assembles the EDL.

Script (work/gen/<v>.script.json):
  {"variant": "v3", "aspect": "9:16", "provider": "hyperscale",
   "character": {"name": "June", "age": 65, "look": "short silver hair, blue-grey eyes, ...",
                 "flaws": "crow's feet, smile lines, a few sun spots, crepey neck",
                 "wardrobe": "faded lilac cardigan over a nightgown", "home": "small lived-in house, Ohio",
                 "consent": "fictional"},
   "product": {"name": "50ml Castor Oil Roll On", "photos": ["https://...", "..."],
               "look": "amber glass, dark green label, gold cap, pink rose quartz roller ball"},
   "voice": {"model": "eleven-tts-v2", "voice": "<voice id>", "style": "warm, a little dry"}   (omit: music only)
   "rooms": {"bathroom": "her small bathroom at night, one warm vanity bulb, a counter crowded with half-used creams"},
   "lines": [{"say": "I'm 65 and I used to do nine steps.", "show": "talking", "room": "bathroom",
              "still": "close to the mirror, glasses on her head, one eyebrow up", "perform": "small shrug on 'nine'"},
             {"show": "broll", "room": "bathroom", "product": true,
              "still": "her hand on the counter next to the roller", "action": "her fingers pick up the roller"},
             {"show": "motion", "room": "kitchen", "camera": "propped",       (camera: selfie | propped | close)
              "still": "mid-laugh with a coffee mug", "action": "she waves off a compliment"},
             {"show": "motion", "room": "bedroom", "still": "in bed, reaching for the lamp",
              "action": "she switches off the bedside lamp", "seconds": 2.0, "caption": "Works while you sleep"}]}
"""
import json
import re
import subprocess
import time
from pathlib import Path

from vs_common import die, load_json, probe, save_json

IMAGE = "gpt-image-2-5"
VIDEO = "seedance-2-5"
TALK = "omnihuman-1-5"
TTS = "eleven-tts-v2"
# Quoted prices seen on the brand's account (always re-quote: they change; charges often come in lower).
PRICE = {"image": 0.05, "video5": 1.58}

CAMERA = ("Photorealistic vertical 9:16 frame, like a paused frame from a casual selfie video filmed on an iPhone "
          "front camera. She holds the phone herself at arm's length, her near arm angling out of the bottom corner "
          "of the frame toward the lens. Slight wide-angle selfie perspective, a couple of degrees of handheld tilt, "
          "slightly off-center, chest-up to face-filling.")
# Visual imperfections are what make it read as real (team tip): harsh-ish light, imperfect framing, real exposure.
IMPERFECT = ("Imperfect on purpose: slightly harsh, uneven light from one real source in the room; imperfect framing "
             "(a little too close, part of the head or shoulder cut off at the edge, not centered); realistic phone "
             "exposure, so the brightest window or lamp is a little blown out and the shadows are a little crushed.")
LOOK = (f"{IMPERFECT} Deep focus, no portrait mode, no background blur. True-to-life flat phone color, not graded. "
        "Real skin texture: pores, the lines and spots named above, slight unevenness, never airbrushed or plastic.")
MOVE = ("iPhone-style UGC: natural handheld movement, small shakes and drifts, the framing slips a little and gets "
        "corrected; realistic exposure shifts as the phone moves, the auto-exposure brightening and dimming slightly "
        "when a window or lamp comes into frame.")
PROPPED = ("Photorealistic vertical 9:16 frame, like a paused frame from a video filmed on a phone propped up nearby "
           "(on a counter, a nightstand, against a bowl), not handheld: the frame does not move and is a couple of degrees "
           "crooked, framed from the waist or chest up.")
CLOSE = ("Photorealistic vertical 9:16 frame, like a paused frame from a selfie video filmed on an iPhone front camera held "
         "very close: EXTREME CLOSE-UP, the face or the body part fills almost the whole frame, a couple of degrees of tilt.")
CLEAN = "No text, no logos except the product's own label, no watermark, no phone visible in frame."
NOT_GRID = "Output ONE single photo, not a grid."


def _person(c):
    age = c.get("age")
    who = f"A {age}-year-old {c.get('who', 'woman')}" if age else f"A {c.get('who', 'woman')}"
    bits = [who + (f" ({c['home']})" if c.get("home") else "") + ". " + c.get("look", "").strip(),
            ("Keep these, never clean them away: " + c["flaws"].strip()) if c.get("flaws") else "",
            ("Wearing " + c["wardrobe"].strip()) if c.get("wardrobe") else "",
            "She is attractive in a real, next-door way, not a model."]
    return " ".join(b.rstrip(".") + "." for b in bits if b)


def _identity(c, n_refs):
    refs = "Image 1 (her selfie) and Image 2 (her character sheet)" if n_refs >= 2 else "the reference image"
    age = f" She is {c['age']}." if c.get("age") else ""
    return (f"Use {refs} strictly as identity references: the EXACT same person. Same face, same bone structure, "
            f"same hair, same eyes, same brows, same skin marks, same jewellery. Never a different person, no identity "
            f"drift, no beautifying, no smoothing.{age} Ignore the references' framing and pose. {NOT_GRID}")


def character_prompt(c, room_txt):
    moment = c.get("moment", "She is caught mid-sentence, talking to the camera like she is talking to a friend: "
                             "mouth slightly open on a word, eyes on the lens.")
    place = room_txt or c.get("place", "An ordinary lived-in room of her home.")
    return f"{CAMERA}\n\n{_person(c)}\n\n{moment}\n\nSetting: {place}\n\n{LOOK}\n\n{CLEAN}"


def sheet_prompt(c):
    return (f"Use the reference image strictly as the identity reference: the EXACT same person in every panel. Same "
            f"face, same bone structure, same hair, same eyes, same brows, same skin marks, same jewellery, same "
            f"clothes. Never a different person, no identity drift, no beautifying, no smoothing."
            f"{' She is ' + str(c['age']) + ' years old.' if c.get('age') else ''}\n\n"
            "Create a character sheet: a clean 3x3 grid of NINE equal vertical panels with thin white gutters. Every "
            "panel is a casual iPhone front-camera selfie frame of this same person, same clothes, same light, the same "
            "room. Only the angle and expression change:\nRow 1: front view, relaxed. Three-quarter left, mid-sentence. "
            "Three-quarter right, soft smile.\nRow 2: clean left profile. Extreme close-up from brows to chin. Looking "
            "down and laughing.\nRow 3: head tilted, eyebrows raised. Cheek on a pillow, sleepy. Chin resting on her "
            "hand, slight smirk.\n\nNo text, no labels, no numbers, no logos, no watermark.")


def master_prompt(c, room, room_txt):
    return (f"{_identity(c, 2)}\n\n{CAMERA}\n\nThis is the master frame for every shot in the {room}. Setting: "
            f"{room_txt}\n\n{c.get('moment', 'Mid-word, eyes on the lens.')}\n\n{LOOK}\n\n{CLEAN}")


def still_prompt(c, ln, room_txt, has_master, has_product, product_look=""):
    refs = []
    if has_master:
        refs.append("Image 1 is the master frame of this room. Keep EVERYTHING about it: the same person, the same "
                    "clothes, the same room and props, the EXACT same lighting. Change only what is described below "
                    "(the camera position, the distance, the pose). Images 2 and 3 are her selfie and character sheet, "
                    f"for identity only. {NOT_GRID}")
    else:
        refs.append(_identity(c, 2))
    if has_product:
        refs.append("The last reference image(s) are the real product" + (f" ({product_look})" if product_look else "")
                    + ": keep its bottle, cap, roller and label exactly as they are; keep it at arm's length or smaller "
                    "in the frame, never a label close-up.")
    shot = ln.get("still") or ln.get("broll") or ""
    cam = ln.get("camera", "selfie")
    who = ("No face in the shot: only her hands and the props, filmed on a phone held close."
           if ln.get("show") == "broll" else {"propped": PROPPED, "close": CLOSE}.get(cam, CAMERA))
    place = "" if has_master else f"\n\nSetting: {room_txt}" if room_txt else ""
    return f"{' '.join(refs)}\n\n{who}\n\n{shot}{place}\n\n{LOOK}\n\n{CLEAN}"


def talk_prompt(ln):
    where = ln.get("still", "Filming herself on her phone")
    tone = ln.get("tone", "warm, natural, conversational")
    move = f" {ln['perform']}." if ln.get("perform") else ""
    return (f"{where}. {tone}.{move} Stays in place, head upright and level, only small natural nods. The phone is "
            f"handheld, so the frame drifts slightly, with small natural exposure shifts.")


def motion_prompt(ln, aspect):
    kind = ln.get("show")
    act = ln.get("action") or ln.get("still") or ""
    face = ("No face in the shot." if kind == "broll" else
            "Keep her face, hair, skin texture and lines exactly as in the start frame.")
    orient = "vertical" if aspect == "9:16" else "horizontal"
    if ln.get("camera") == "propped":
        how = (f"Filmed on a recent iPhone propped up nearby, {orient}: the frame stays put apart from tiny bumps, a "
               f"couple of degrees crooked; realistic exposure shifts when the light in the room changes.")
    else:
        how = f"Shot like a real person filming on a recent iPhone with one hand, {orient}. {MOVE}"
    return (f"5 seconds. {how} Slightly harsh real light, deep focus, flat honest phone color. ONE clear action: "
            f"{act}. {face} The product label stays exactly as it is. No new text, no logos, no captions. "
            f"No beauty filter, no smooth gimbal motion.")


def plan(s, a):
    c = s.get("character") or die("script has no character")
    if not str(c.get("consent", "")).strip():
        die("character.consent is empty: say 'fictional', or name the real person and their written consent")
    lines = s.get("lines") or die("script has no lines")
    aspect = s.get("aspect", "9:16")
    rooms = s.get("rooms", {})
    prod = s.get("product") or {}
    photos = prod.get("photos", [])
    voice = s.get("voice")
    v = s.get("variant", Path(a.script).stem.split(".")[0])
    jobs = []

    def job(jid, kind, needs=(), **kw):
        jobs.append({"id": jid, "kind": kind, "needs": list(needs), "status": "todo", **kw})

    first_room = next((ln.get("room") for ln in lines if ln.get("room")), None)
    job("character", "character", model=IMAGE, aspect=aspect, count=4, usd=PRICE["image"] * 4,
        prompt=character_prompt(c, rooms.get(first_room, "")),
        note="Make 3-4, pick the face that looks like someone you could know: that one picture is the character. "
             "Record the pick with --url.")
    job("sheet", "sheet", ["character"], model=IMAGE, aspect="1:1", usd=PRICE["image"],
        refs=["character"], prompt=sheet_prompt(c),
        note="Keep it: every later still points at the selfie and the sheet.")
    if photos:
        job("product", "product", status_note="brand photos", model="(Products tab)")
        jobs[-1].update(status="done", result={"refs": photos})
    shared = {r for r in rooms if sum(ln.get("room") == r for ln in lines) > 1}
    for r in sorted(shared):
        job(f"master_{r}", "master", ["character", "sheet"], model=IMAGE, aspect=aspect, usd=PRICE["image"],
            refs=["character", "sheet"], prompt=master_prompt(c, r, rooms[r]),
            note="One master frame per room; every other angle in it changes only the camera.")
    speaking = [i for i, ln in enumerate(lines) if ln.get("say")]
    if speaking and voice:
        job("read", "read", [], model=voice.get("model", TTS), voice=voice.get("voice"), style=voice.get("style"),
            text="\n".join(lines[i]["say"].strip() for i in speaking),
            note="ONE read of the whole script, one line per paragraph so the pauses fall between lines.")
        job("slices", "slices", ["read"], tool="local: vs gen slice", lines=speaking,
            note="Cut the read at the pauses, one slice per spoken line; upload each slice (start_reference_upload) "
                 "before the talking shots that need it.")
    elif speaking:
        die("lines have 'say' but the script has no voice: add voice {model, voice}, or drop 'say' for music-only")
    for i, ln in enumerate(lines):
        n = i + 1
        show = ln.get("show", "talking" if ln.get("say") else "motion")
        ln["show"] = show
        r = ln.get("room")
        needs = ["character", "sheet"]
        refs = ["character", "sheet"]
        if r in shared:
            needs.insert(0, f"master_{r}")
            refs.insert(0, f"master_{r}")
        if ln.get("product") and photos:
            needs.append("product")
            refs.append("product")
        if ln.get("source") == "library":
            continue
        job(f"still{n}", "still", needs, model=IMAGE, aspect=aspect, usd=PRICE["image"], refs=refs, line=i,
            prompt=still_prompt(c, ln, rooms.get(r, ""), r in shared, bool(ln.get("product") and photos),
                                prod.get("look", "")))
        if show == "talking":
            job(f"talk{n}", "talking", [f"still{n}", "slices"], model=TALK, line=i, image=f"still{n}",
                audio=f"slice{n}", prompt=talk_prompt(ln),
                note="Quote first (price per second of audio). Image = the still's url, audio = this line's slice url.")
        elif show == "still":
            pass  # a frozen still in the cut (e.g. the reel's old selfies): no video job
        elif show in ("broll", "motion"):
            job(f"{show}{n}", show, [f"still{n}"], model=VIDEO, line=i, aspect=aspect, duration=5,
                resolution="720p", audio=False, start_frame=f"still{n}", usd=PRICE["video5"],
                prompt=motion_prompt(ln, aspect), keep=ln.get("seconds", 2.0),
                note="start_frame_url only (Seedance takes a start frame OR reference images, not both). "
                     "Keep the best 1-2 s in the cut.")
    doc = {"variant": v, "script": a.script, "aspect": aspect, "provider": "hyperscale", "character": c,
           "lines": lines, "tool_prefix": "mcp__Hyperscale__", "created": time.strftime("%Y-%m-%d %H:%M"), "jobs": jobs}
    out = Path(a.out or Path(a.script).with_name(f"{v}.jobs.json"))
    save_json(out, doc)
    todo = [j for j in jobs if j["status"] == "todo" and j["kind"] != "slices"]
    usd = sum(j.get("usd", 0) for j in todo)
    talks = sum(j["kind"] == "talking" for j in jobs)
    print(f"{len(jobs)} jobs ({len(todo)} generations) -> {out}; Hyperscale (tools mcp__Hyperscale__*)")
    for j in jobs:
        print(f"  {j['id']:<16} {j['kind']:<9} {j.get('model', j.get('tool', '')):<16} needs {','.join(j['needs']) or '-'}")
    print(f"Estimate: ~${usd:.2f} quoted for images + 5 s clips"
          + (f", plus {talks} talking shot(s) and the read: quote those" if talks else "")
          + ". Quote with the person and get a yes before the first generate.")
    return doc


def _audio_file(doc):
    r = next((j for j in doc["jobs"] if j["id"] == "read"), None)
    if not r or r["status"] != "done":
        die("the read isn't done yet (vs gen done ... read --url ...)")
    f = r.get("local") or (r.get("result", {}).get("file"))
    if not f or not Path(f).exists():
        die("the read isn't downloaded: vs gen fetch <jobs> --project <dir> first")
    return f


def silences(f, db=-35.0, mn=0.25):
    p = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", f, "-af", f"silencedetect=noise={db}dB:d={mn}",
                        "-f", "null", "-"], capture_output=True, text=True)
    st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", p.stderr)]
    en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", p.stderr)]
    return list(zip(st, en))


def cmd_slice(a):
    doc = load_json(a.jobs)
    sj = next((j for j in doc["jobs"] if j["id"] == "slices"), None) or die("this plan has no spoken lines")
    f = _audio_file(doc)
    dur = probe(f)["duration"]
    n = len(sj["lines"])
    gaps = [(s, e) for s, e in silences(f, a.db, a.min) if s > 0.05 and e < dur - 0.05]
    if len(gaps) < n - 1:
        die(f"found {len(gaps)} pauses for {n} lines: lower --min or raise --db, or re-read with clearer pauses")
    cuts = sorted(sorted(gaps, key=lambda g: g[1] - g[0], reverse=True)[:n - 1])
    lead = silences(f, a.db, 0.05)
    start = lead[0][1] if lead and lead[0][0] < 0.05 else 0.0
    end = dur
    if lead and lead[-1][1] >= dur - 0.05:
        end = lead[-1][0]
    bounds = [start] + [x for s, e in cuts for x in (s, e)] + [end]
    proj = Path(a.project)
    out_dir = proj / "raw" / "gen"
    out_dir.mkdir(parents=True, exist_ok=True)
    pad = a.pad
    slices, parts = [], []
    for k, li in enumerate(sj["lines"]):
        s, e = max(bounds[2 * k] - pad, 0), min(bounds[2 * k + 1] + pad, dur)
        o = out_dir / f"{doc['variant']}_slice{li + 1}.wav"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{s:.3f}", "-to", f"{e:.3f}", "-i", f, "-ac", "1",
                        "-ar", "48000", str(o)], check=True)
        slices.append({"line": li, "file": str(o), "start": round(s, 3), "end": round(e, 3),
                       "seconds": round(e - s, 3)})
        parts.append(o)
    sj["status"] = "done"
    sj["result"] = {"slices": slices}
    save_json(a.jobs, doc)
    for sl in slices:
        print(f"  slice{sl['line'] + 1}: {sl['seconds']:.2f}s  {sl['file']}")
    print(f"{len(slices)} slices. Upload each (start_reference_upload) and give talk<n> its slice url.")


def fetch_ext(kind):
    return {"character": ".png", "sheet": ".png", "master": ".png", "still": ".png", "read": ".mp3",
            "talking": ".mp4", "broll": ".mp4", "motion": ".mp4"}.get(kind)


def edl(doc, a):
    lines = doc["lines"]
    by_line = {}
    for j in doc["jobs"]:
        if j["kind"] in ("talking", "broll", "motion") and j.get("local"):
            by_line[j["line"]] = j
        elif j["kind"] == "still" and j.get("local") and lines[j["line"]].get("show") == "still":
            by_line[j["line"]] = j
    sl = {s["line"]: s for s in next((j.get("result", {}).get("slices", []) for j in doc["jobs"]
                                      if j["id"] == "slices"), [])}
    segs, voice, t, missing = [], [], 0.0, []
    for i, ln in enumerate(lines):
        j = by_line.get(i)
        if not j:
            missing.append(f"line {i + 1} ({ln.get('show')}): {ln.get('still') or ln.get('broll') or ''}"[:90])
            continue
        still = j["kind"] == "still"
        clip_d = 1e9 if still else probe(j["local"])["duration"]
        if i in sl:
            need = sl[i]["seconds"] + a.gap
        else:
            need = float(ln.get("seconds", j.get("keep", 2.0)))
        d = min(need, clip_d)
        st = float(ln.get("in", 0.0))
        if st + d > clip_d:
            st = max(clip_d - d, 0.0)
        if still:
            st = 0.0
        segs.append({"src": j["local"], "start": round(st, 3), "end": round(st + d, 3), "mute": True,
                     "note": (ln.get("say") or ln.get("caption") or ln.get("still") or "")[:40]})
        if i in sl:
            voice.append({"file": sl[i]["file"], "at": round(t, 3)})
        t += d
    out = {"segments": segs, "_generated_from": a.jobs}
    if voice:
        out["tracks"] = [{"name": "voice", "gain_db": 0, "duck": False, "clips": voice}]
    if a.out and Path(a.out).exists() and not a.force:
        die(f"{a.out} exists (use --force)")
    save_json(a.out, out)
    print(f"EDL -> {a.out}: {len(segs)} shots, one per line, {t:.1f}s"
          + (f"; the read under it in {len(voice)} slices" if voice else "; no voice (music-only)"))
    for m in missing:
        print(f"  missing: {m}")
    print("Next: captions (full phrases, one line, inside the safe zone), music low, end on a moment.")
    return json.dumps(out)
