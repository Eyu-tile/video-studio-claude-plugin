#!/usr/bin/env python3
"""Lessons: what feedback taught us, kept per brand, applied and checked on every later project.

A lesson is one concrete rule learned from a note ("music sits at -22 dB or lower under speech"), stored in the
brand's library so it follows the client into every project, or in the workspace style folder when it is a house
rule for everyone. A lesson can carry a machine check, so `vs qa --brand X` (and `vs lessons check`) catches the
mistake before the client sees it again. Every note logged with `vs notes add --brand X` is compared against the
lessons: a note that repeats one is flagged as a repeat (the lesson failed), and notes that keep coming back across
projects without a lesson are offered as new lessons by `vs lessons learn`.

  vs lessons brief --brand TrueClean [--kind reels]      the rules to apply before planning (short, ranked)
  vs lessons add --brand TrueClean --rule "Music at -22 dB or lower under speech" --category music \\
        --check music_gain_max=-22 [--must] [--when reels,ads] [--from work/notes.json:3] [--told]
  vs lessons add --global --rule "..."                    a house rule for every brand (style/lessons.json)
  vs lessons learn --brand TrueClean [--notes work/notes.json]   notes not yet turned into lessons + repeated feedback
  vs lessons none work/notes.json 4 5                     those notes were one-offs (not a lesson)
  vs lessons check work/edl.json --brand TrueClean [--captions work/c.ass] [--video out/final.mp4]
  vs lessons list --brand TrueClean [--all]   |   vs lessons retire --brand TrueClean L3 --why "client changed mind"
  vs lessons edit --brand TrueClean L3 --rule "..." --check music_gain_max=-24   |   vs lessons checks

Files: <workspace>/library/<Brand>/lessons.json + LESSONS.md, feedback.jsonl (every note, for spotting repeats);
house rules: <workspace>/style/lessons.json + LESSONS.md.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from vs_common import die, load_json, save_json  # noqa: E402

CATEGORIES = {
    "music": "music song track beat soundtrack bgm",
    "sound": "sfx sound whoosh effect effects swoosh ding hit riser",
    "audio": "loud quiet volume voice audio mix noise levels hiss mic loudness lufs",
    "captions": "caption captions subtitle subtitles subs",
    "text": "text title font typo logo lower third card cta headline overlay",
    "pacing": "fast slow pace pacing long short drag dragging boring hook speed tight",
    "cuts": "cut cuts jump transition transitions shot shots trim zoom",
    "color": "color colour grade grading warm cool dark bright saturation skin exposure",
    "framing": "crop framing frame reframe headroom center centre aspect vertical",
    "assets": "footage clip clips stock broll b-roll image images",
    "brand": "brand colors palette guideline guidelines tone",
    "delivery": "export format resolution file deliver delivery size",
}
STOP = set("""the a an and or but to of in on at for with this that these those it its is are was were be been being
too very so just really more less much make makes made please can could should would we you i me my our your they them
there here then than also like want need get got have has had do does did not no yes all any some one two from into
out up down over again still bit lot little thing things way feel feels looks look seems seem same video edit""".split())
CHECKS = {
    "music_gain_max": "music bed gain in dB must be at or below this (EDL music.gain_db / music track)",
    "music_gain_min": "music bed gain in dB must be at or above this",
    "sfx_gain_max": "every sound effect's gain in dB at or below this",
    "sfx_per_min_max": "at most this many sound effects per minute",
    "shot_min": "no shot shorter than this many seconds",
    "shot_max": "no shot longer than this many seconds",
    "hook_max": "the first shot ends by this many seconds",
    "duration_max": "the video is at most this long (s)",
    "duration_min": "the video is at least this long (s)",
    "banned_transitions": "transition types never to use (comma list: fade,wipe,zoom...)",
    "banned_grades": "grades/LUT names never to use (comma list)",
    "banned_sources": "file name parts never to use in shots, overlays, music or sfx (comma list)",
    "required_sources": "file name parts that must appear somewhere (e.g. logo.png) (comma list)",
    "banned_words": "words never shown in on-screen text or captions (comma list)",
    "text_size_min": "on-screen text size at least this (EDL texts size, share of height, e.g. 0.06)",
    "text_font": "on-screen text font must be this family",
    "caption_words_max": "at most this many words on screen per caption event",
    "caption_case": "captions all 'upper' or 'lower' case",
    "lufs": "integrated loudness of the render within 1 LU of this (needs --video)",
}
LIST_CHECKS = {"banned_transitions", "banned_grades", "banned_sources", "required_sources", "banned_words"}


def now():
    return time.strftime("%Y-%m-%d %H:%M")


# --------------------------------------------------------------------------------------------
# Where lessons live

def workspace():
    ws = os.environ.get("VS_WORKSPACE")
    if ws:
        return Path(ws)
    try:
        root = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip()
    except OSError:
        root = ""
    return Path(root or os.getcwd()) / "video-studio"


def brand_dir(brand):
    """library/<Brand>/, matching an existing folder whatever its case."""
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9 ._&-]{0,60}", brand or ""):
        die("brand: letters, digits, space, '.', '_', '&' or '-' (the library folder name, e.g. TrueClean)")
    lib = workspace() / "library"
    if lib.is_dir():
        for d in lib.iterdir():
            if d.is_dir() and d.name.lower() == brand.lower():
                return d
    return lib / brand


def brand_for_project(project):
    """The client of the task whose project folder is `project` (from history/), if any."""
    name = Path(project).name
    for f in sorted((workspace() / "history").glob("*.json")):
        try:
            t = load_json(f)
        except (OSError, ValueError):
            continue
        if isinstance(t, dict) and t.get("project") == name and t.get("client"):
            return t["client"]
    return None


def resolve_brand(a):
    b = getattr(a, "brand", None) or os.environ.get("VS_BRAND")
    if not b and getattr(a, "project", None):
        b = brand_for_project(a.project)
    return b


def book_path(brand=None, glob=False):
    return (workspace() / "style" / "lessons.json") if glob else (brand_dir(brand) / "lessons.json")


def load_book(path):
    if path.exists():
        b = load_json(path)
        b.setdefault("lessons", [])
        return b
    return {"version": 1, "lessons": []}


def save_book(path, book, title):
    path.parent.mkdir(parents=True, exist_ok=True)
    save_json(path, book)
    path.with_name("LESSONS.md").write_text(render_md(book, title), encoding="utf-8")


def books(brand, include_global=True):
    """[(scope, path, book)] for the brand and the house rules."""
    out = []
    if brand:
        p = book_path(brand)
        out.append((brand_dir(brand).name, p, load_book(p)))
    if include_global:
        p = book_path(glob=True)
        out.append(("house", p, load_book(p)))
    return out


def legacy_notes():
    """Bullets from style/notes.md (the old one-line rules) so nothing learned before is lost."""
    p = workspace() / "style" / "notes.md"
    if not p.exists():
        return []
    return [ln.strip()[2:].strip() for ln in p.read_text(encoding="utf-8").splitlines()
            if ln.strip().startswith(("- ", "* ")) and len(ln.strip()) > 4]


# --------------------------------------------------------------------------------------------
# Text matching (deterministic: shared content words + category)

def tokens(text):
    out = set()
    for w in re.findall(r"[a-z0-9][a-z0-9-]+", (text or "").lower()):
        if w in STOP or len(w) < 3 or w.isdigit():
            continue
        for suf in ("ing", "ed", "es", "er", "ly", "s"):
            if w.endswith(suf) and len(w) - len(suf) >= 3:
                w = w[: -len(suf)]
                break
        out.add(w)
    return out


CAT_TOKENS = {c: tokens(words) for c, words in CATEGORIES.items()}
# the thing a note is about outweighs how it describes it ("the music is too loud over the voice" is about music)
SUBJECTS = {c: tokens(w) for c, w in {"music": "music song track soundtrack bgm", "sound": "sfx sound whoosh effect",
                                      "captions": "caption subtitle subs", "text": "text title font logo typo",
                                      "color": "color colour grade", "framing": "crop framing reframe"}.items()}


def category_of(text):
    tk = tokens(text)
    score = {c: len(tk & CAT_TOKENS[c]) + 2 * bool(tk & SUBJECTS.get(c, set())) for c in CAT_TOKENS}
    best = max(score, key=score.get)
    return best if score[best] else "other"


def lesson_tokens(lesson):
    return tokens(lesson["rule"] + " " + " ".join(lesson.get("keywords", [])))


def similarity(text, lesson):
    """Shared content words, plus one when the note's category is the lesson's."""
    shared = tokens(text) & lesson_tokens(lesson)
    return len(shared) + (1 if lesson.get("category") == category_of(text) and shared else 0), shared


def match(text, lessons, threshold=2):
    """Best active lesson this note repeats, or None."""
    best = None
    for les in lessons:
        if les.get("status", "active") != "active":
            continue
        s, shared = similarity(text, les)
        if s >= threshold and (best is None or s > best[0]):
            best = (s, les, shared)
    return best


# --------------------------------------------------------------------------------------------
# Called by `vs notes add --brand`: log every note, flag the ones that repeat a lesson

def record_notes(brand, notes, project=None, source=None):
    """Append notes to the brand's feedback log and return [(note, lesson, scope)] for repeats."""
    if not brand:
        return []
    d = brand_dir(brand)
    d.mkdir(parents=True, exist_ok=True)
    repeats = []
    all_books = books(brand)
    with (d / "feedback.jsonl").open("a", encoding="utf-8") as log:
        for n in notes:
            text = n.get("text", "")
            entry = {"date": now(), "project": project, "source": source, "note": n.get("id"), "text": text,
                     "category": category_of(text)}
            for scope, path, book in all_books:
                m = match(text, book["lessons"])
                if m:
                    les = m[1]
                    les["repeats"] = les.get("repeats", 0) + 1
                    les.setdefault("repeat_log", []).append({"date": now(), "project": project, "text": text[:200]})
                    les["repeat_log"] = les["repeat_log"][-10:]
                    entry["lesson"] = les["id"]
                    n["lesson"] = les["id"]
                    repeats.append((n, les, scope))
                    break
            log.write(json.dumps(entry, ensure_ascii=False) + "\n")
    for scope, path, book in all_books:
        if any(r[2] == scope for r in repeats):
            save_book(path, book, scope)
    return repeats


# --------------------------------------------------------------------------------------------
# Checks against an EDL, captions and a render

def parse_check(items):
    out = {}
    for it in items or []:
        if "=" not in it:
            die(f"--check {it!r}: use key=value (see `vs lessons checks`)")
        k, v = it.split("=", 1)
        k = k.strip()
        if k not in CHECKS:
            die(f"unknown check {k!r}; available: {', '.join(CHECKS)}")
        if k in LIST_CHECKS:
            out[k] = [x.strip() for x in v.split(",") if x.strip()]
        elif k in ("text_font", "caption_case"):
            out[k] = v.strip()
        else:
            try:
                out[k] = float(v)
            except ValueError:
                die(f"--check {k}: needs a number")
    return out


def ass_texts(path):
    out = []
    for line in Path(path).read_text(encoding="utf-8", errors="ignore").splitlines():
        if line.startswith("Dialogue:"):
            parts = line.split(",", 9)
            if len(parts) == 10:
                out.append(re.sub(r"\{[^}]*\}", "", parts[9]).replace("\\N", " ").strip())
    return out


def measure_lufs(video):
    p = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(video), "-vn", "-sn", "-dn",
                        "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True)
    summ = p.stderr[p.stderr.rfind("Summary:"):]
    m = re.search(r"I:\s+(-?[\d.]+) LUFS", summ)
    return float(m.group(1)) if m else None


def run_checks(lessons, edl=None, captions=None, video=None):
    """[(lesson, ok, detail)] for every active lesson that has a check this input can answer."""
    from vs_common import timeline, total_duration
    res = []
    shots, total, sources, music_gains = [], None, [], []
    if edl is not None:
        tl = [g for g in timeline(edl) if not g.get("join")]
        shots = [(i + 1, g["out_end"] - g["out_start"]) for i, g in enumerate(tl)]
        total = total_duration(edl)
        sources = [str(s.get("src", "")) for s in edl.get("segments", [])]
        sources += [str(o.get("file", "")) for o in edl.get("overlays", []) or []]
        sources += [str(s.get("file", "")) for s in edl.get("sfx", []) or []]
        if edl.get("music"):
            sources.append(str(edl["music"].get("file", "")))
            music_gains.append(float(edl["music"].get("gain_db", -18)))
        for tr in edl.get("tracks", []) or []:
            if "music" in str(tr.get("name", "")).lower():
                music_gains.append(float(tr.get("gain_db", 0)))
            sources += [str(c.get("file", "")) for c in tr.get("clips", []) or []]
    caps = ass_texts(captions) if captions and Path(captions).exists() else None
    texts = [str(t.get("text", "")) for t in (edl or {}).get("texts", []) or []]
    lufs = None
    for les in lessons:
        if les.get("status", "active") != "active":
            continue
        for k, v in (les.get("check") or {}).items():
            ok, detail = None, ""
            if edl is not None:
                if k == "music_gain_max" and music_gains:
                    ok, detail = max(music_gains) <= v, f"music at {max(music_gains):g} dB (max {v:g})"
                elif k == "music_gain_min" and music_gains:
                    ok, detail = min(music_gains) >= v, f"music at {min(music_gains):g} dB (min {v:g})"
                elif k == "sfx_gain_max":
                    loud = [float(s.get("gain_db", s.get("gain", -12))) for s in edl.get("sfx", []) or []]
                    ok, detail = (not loud or max(loud) <= v), (f"loudest sfx {max(loud):g} dB (max {v:g})"
                                                                if loud else "no sfx")
                elif k == "sfx_per_min_max" and total:
                    rate = len(edl.get("sfx", []) or []) / (total / 60)
                    ok, detail = rate <= v, f"{rate:.1f} sfx/min (max {v:g})"
                elif k == "shot_min" and shots:
                    bad = [f"shot {i} {ln:.2f}s" for i, ln in shots if ln < v - 1e-3]
                    ok, detail = not bad, ", ".join(bad[:6]) or f"all shots >= {v:g}s"
                elif k == "shot_max" and shots:
                    bad = [f"shot {i} {ln:.2f}s" for i, ln in shots if ln > v + 1e-3]
                    ok, detail = not bad, ", ".join(bad[:6]) or f"all shots <= {v:g}s"
                elif k == "hook_max" and shots:
                    ok, detail = shots[0][1] <= v + 1e-3, f"first shot {shots[0][1]:.2f}s (max {v:g}s)"
                elif k == "duration_max" and total:
                    ok, detail = total <= v + 1e-3, f"{total:.2f}s (max {v:g}s)"
                elif k == "duration_min" and total:
                    ok, detail = total >= v - 1e-3, f"{total:.2f}s (min {v:g}s)"
                elif k == "banned_transitions":
                    used = []
                    for i, s in enumerate(edl.get("segments", [])):
                        tr = s.get("transition_in")
                        if tr:
                            typ = tr.get("type", "fade") if isinstance(tr, dict) else "fade"
                            if typ.lower() in {x.lower() for x in v}:
                                used.append(f"shot {i + 1} {typ}")
                    ok, detail = not used, ", ".join(used) or "none used"
                elif k == "banned_grades":
                    g = [str(edl.get(x, "")) for x in ("grade", "lut")]
                    g += [str(s.get(x, "")) for s in edl.get("segments", []) for x in ("grade", "lut")]
                    bad = sorted({x for x in g if x and any(b.lower() in x.lower() for b in v)})
                    ok, detail = not bad, ", ".join(bad) or "none used"
                elif k == "banned_sources":
                    bad = sorted({Path(s).name for s in sources if s and any(b.lower() in s.lower() for b in v)})
                    ok, detail = not bad, ", ".join(bad) or "none used"
                elif k == "required_sources":
                    miss = [b for b in v if not any(b.lower() in s.lower() for s in sources)]
                    ok, detail = not miss, ("missing " + ", ".join(miss)) if miss else "present"
                elif k == "text_size_min" and edl.get("texts"):
                    bad = [t.get("text", "")[:20] for t in edl["texts"] if float(t.get("size", 0.075)) < v]
                    ok, detail = not bad, (", ".join(bad) + f" smaller than {v:g}") if bad else "ok"
                elif k == "text_font" and edl.get("texts"):
                    bad = sorted({str(t.get("font")) for t in edl["texts"] if t.get("font")
                                  and str(t["font"]).lower() != v.lower()})
                    ok, detail = not bad, (f"uses {', '.join(bad)} (want {v})" if bad else f"{v} or default")
            if k == "banned_words" and (texts or caps):
                pool = texts + (caps or [])
                bad = sorted({w for w in v for t in pool if re.search(rf"\b{re.escape(w)}\b", t, re.I)})
                if bad or edl is not None or caps is not None:
                    ok, detail = not bad, ("shows " + ", ".join(bad)) if bad else "none shown"
            elif k == "caption_words_max" and caps:
                worst = max((len(t.split()) for t in caps), default=0)
                ok, detail = worst <= v, f"up to {worst} words per caption (max {v:g})"
            elif k == "caption_case" and caps:
                bad = [t for t in caps if (t != t.upper() if v == "upper" else t != t.lower())]
                ok, detail = not bad, (f"{len(bad)} caption(s) not {v} case, e.g. {bad[0][:30]!r}" if bad
                                       else f"all {v} case")
            elif k == "lufs" and video:
                if lufs is None:
                    lufs = measure_lufs(video)
                if lufs is not None:
                    ok, detail = abs(lufs - v) <= 1.0, f"{lufs:.1f} LUFS (target {v:g})"
            if ok is not None:
                res.append((les, ok, f"{k}: {detail}"))
    return res


def qa_lines(brand, edl=None, captions=None, video=None):
    """For `vs qa --brand`: [(level, name, detail)], FAIL for a broken must-lesson, WARN otherwise."""
    out = []
    for scope, path, book in books(brand):
        hits = run_checks(book["lessons"], edl, captions, video)
        changed = False
        for les, ok, detail in hits:
            if not ok:
                les["caught"] = les.get("caught", 0) + 1
                changed = True
            lvl = "PASS" if ok else ("FAIL" if les.get("must") else "WARN")
            out.append((lvl, f"lesson {les['id']}", f"{les['rule']} | {detail}"))
        if changed:
            save_book(path, book, scope)
    return out


# --------------------------------------------------------------------------------------------
# Output

def rank(les):
    return (not les.get("must"), -les.get("repeats", 0), -les.get("seen", 1), les["id"])


def line(les, scope=None):
    tags = []
    if les.get("must"):
        tags.append("MUST")
    if les.get("when"):
        tags.append("/".join(les["when"]))
    if les.get("repeats"):
        tags.append(f"repeated {les['repeats']}x")
    if les.get("check"):
        tags.append("checked")
    pre = f"{scope}:" if scope else ""
    return f"- [{pre}{les['id']}] {les['rule']}" + (f"  ({', '.join(tags)})" if tags else "")


def render_md(book, title):
    act = sorted([x for x in book["lessons"] if x.get("status", "active") == "active"], key=rank)
    old = [x for x in book["lessons"] if x.get("status") == "retired"]
    out = [f"# Lessons: {title}", "",
           "Learned from feedback. Apply before planning; `vs qa --brand` checks the ones marked checked.", ""]
    by = {}
    for les in act:
        by.setdefault(les.get("category", "other"), []).append(les)
    for cat in sorted(by):
        out.append(f"## {cat}")
        out += [line(x) + (f"\n  - from: {x['from']}" if x.get("from") else "") for x in by[cat]]
        out.append("")
    if old:
        out.append("## retired")
        out += [f"- ~~{x['id']} {x['rule']}~~ ({x.get('retired_why', '')})" for x in old]
    return "\n".join(out).rstrip() + "\n"


def applies(les, kind):
    return not kind or not les.get("when") or any(k.lower() in [w.lower() for w in les["when"]] for k in kind)


# --------------------------------------------------------------------------------------------
# Commands

def cmd_brief(a):
    brand = resolve_brand(a)
    kind = [k for k in (a.kind or "").split(",") if k]
    rows = []
    for scope, path, book in books(brand):
        rows += [(les, scope) for les in book["lessons"]
                 if les.get("status", "active") == "active" and applies(les, kind)]
    rows.sort(key=lambda r: rank(r[0]))
    legacy = legacy_notes()
    if not rows and not legacy:
        print(f"no lessons yet for {brand or 'this workspace'}" + ("" if brand else " (pass --brand <client>)"))
        return
    print(f"Lessons for {brand or 'all brands (house rules)'}" + (f" ({', '.join(kind)})" if kind else "")
          + ": apply these in the plan; checked ones run in `vs qa --brand`.")
    for les, scope in rows[: a.max]:
        print(line(les, None if scope != "house" else "house"))
    if len(rows) > a.max:
        print(f"... {len(rows) - a.max} more: vs lessons list --brand {brand}")
    if legacy:
        print("House notes (style/notes.md):")
        for x in legacy[:10]:
            print(f"- {x}")


def next_id(book):
    return "L" + str(max((int(x["id"][1:]) for x in book["lessons"] if x["id"][1:].isdigit()), default=0) + 1)


def cmd_add(a):
    brand = None if a.glob else resolve_brand(a)
    if not a.glob and not brand:
        die("which brand? --brand <client> (or --global for a house rule)")
    path = book_path(brand, a.glob)
    book = load_book(path)
    check = parse_check(a.check)
    same = match(a.rule, book["lessons"], threshold=3)
    if same and not a.force:
        les = same[1]
        les["seen"] = les.get("seen", 1) + 1
        save_book(path, book, "house" if a.glob else brand_dir(brand).name)
        print(f"already a lesson: {les['id']} {les['rule']} (seen {les['seen']}x). "
              f"Change it with `vs lessons edit`, or add anyway with --force.")
        return
    les = {"id": next_id(book), "rule": a.rule.strip(), "category": a.category or category_of(a.rule),
           "added": now(), "source": "told" if a.told else "inferred", "seen": 1, "repeats": 0}
    if check:
        les["check"] = check
    if a.must:
        les["must"] = True
    if a.when:
        les["when"] = [w.strip() for w in a.when.split(",") if w.strip()]
    if a.keywords:
        les["keywords"] = [w.strip() for w in a.keywords.split(",") if w.strip()]
    if a.from_:
        les["from"] = a.from_
        mark_note(a.from_, les["id"])
    book["lessons"].append(les)
    save_book(path, book, "house" if a.glob else brand_dir(brand).name)
    print(f"{les['id']} added to {path.parent.name}/LESSONS.md: {les['rule']}"
          + (f" | checks {', '.join(f'{k}={v}' for k, v in check.items())}" if check else ""))


def mark_note(ref, value):
    """`work/notes.json:3` -> set that note's `lesson` field."""
    m = re.fullmatch(r"(.+):(\d+(?:,\d+)*)", ref)
    if not m or not Path(m.group(1)).exists():
        return
    p = Path(m.group(1))
    book = load_json(p)
    ids = {int(x) for x in m.group(2).split(",")}
    for n in book.get("notes", []):
        if n["id"] in ids:
            n["lesson"] = value
    save_json(p, book)


def cmd_none(a):
    mark_note(f"{a.notes}:{','.join(map(str, a.ids))}", "none")
    print(f"notes {', '.join(map(str, a.ids))}: one-off, not a lesson")


def cmd_learn(a):
    brand = resolve_brand(a)
    if not brand:
        die("which brand? --brand <client>")
    lessons = [les for _, _, b in books(brand) for les in b["lessons"]]
    if a.notes:
        nb = load_json(a.notes) if Path(a.notes).exists() else {"notes": []}
        todo = [n for n in nb["notes"] if n.get("status") in ("done", "skipped") and not n.get("lesson")]
        print(f"Notes handled but not yet classified ({len(todo)}). For each: will it matter on the NEXT project?")
        print("  yes -> vs lessons add --brand {b} --rule \"<general rule, with the number>\" [--check k=v] "
              "--from {p}:<id>\n  no  -> vs lessons none {p} <ids>".format(b=brand, p=a.notes))
        for n in todo:
            m = match(n["text"], lessons)
            hint = f"  (close to {m[1]['id']}: {m[1]['rule']})" if m else ""
            print(f"  #{n['id']} [{category_of(n['text'])}] {n['text']}"
                  + (f"  -> {n['resolution']}" if n.get("resolution") else "") + hint)
    # Feedback that keeps coming back without a lesson
    log = brand_dir(brand) / "feedback.jsonl"
    entries = []
    if log.exists():
        for ln in log.read_text(encoding="utf-8").splitlines():
            try:
                entries.append(json.loads(ln))
            except ValueError:
                pass
    loose = [e for e in entries if not e.get("lesson")]
    groups = []
    for e in loose:
        tk = tokens(e["text"])
        for g in groups:
            if len(tk & g["tokens"]) >= 2 or (e["category"] == g["category"] and len(tk & g["tokens"]) >= 1
                                               and g["category"] != "other"):
                g["items"].append(e)
                g["tokens"] |= tk
                break
        else:
            groups.append({"tokens": set(tk), "category": e["category"], "items": [e]})
    rep = [g for g in groups if len({(i.get("project") or "?") for i in g["items"]}) >= 2 or len(g["items"]) >= 3]
    if rep:
        print(f"\nFeedback that came back {'more than once' if len(rep) == 1 else 'repeatedly'} with no lesson yet "
              "(strong candidates):")
        for g in sorted(rep, key=lambda g: -len(g["items"])):
            projs = sorted({i.get("project") or "?" for i in g["items"]})
            print(f"  [{g['category']}] {len(g['items'])}x in {', '.join(projs)}:")
            for i in g["items"][-4:]:
                print(f"     - {i['date'][:10]} {i['text'][:110]}")
    elif not a.notes:
        print("no repeated feedback without a lesson")


def cmd_check(a):
    brand = resolve_brand(a)
    edl = load_json(a.edl) if a.edl else None
    fails = 0
    any_hit = False
    for lvl, name, detail in qa_lines(brand, edl, a.captions, a.video):
        any_hit = True
        fails += lvl == "FAIL"
        print(f"{lvl:4} {name}: {detail}")
    if not any_hit:
        print("no checkable lessons for this input")
    sys.exit(1 if fails else 0)


def cmd_list(a):
    brand = resolve_brand(a)
    for scope, path, book in books(brand):
        rows = [x for x in book["lessons"] if a.all or x.get("status", "active") == "active"]
        print(f"== {scope} ({len(rows)}) {path}")
        for les in sorted(rows, key=rank):
            extra = []
            if les.get("check"):
                extra.append("check " + ", ".join(f"{k}={v}" for k, v in les["check"].items()))
            if les.get("caught"):
                extra.append(f"caught before delivery {les['caught']}x")
            if les.get("status") == "retired":
                extra.append("RETIRED: " + les.get("retired_why", ""))
            print(line(les) + (f"\n    {'; '.join(extra)}" if extra else ""))


def find(a):
    brand = None if a.glob else resolve_brand(a)
    path = book_path(brand, a.glob)
    book = load_book(path)
    les = next((x for x in book["lessons"] if x["id"].upper() == a.id.upper()), None)
    if not les:
        die(f"no lesson {a.id} in {path}")
    return path, book, les, ("house" if a.glob else brand_dir(brand).name)


def cmd_retire(a):
    path, book, les, scope = find(a)
    les["status"] = "retired"
    les["retired_why"] = a.why
    save_book(path, book, scope)
    print(f"{les['id']} retired: {les['rule']}")


def cmd_edit(a):
    path, book, les, scope = find(a)
    if a.rule:
        les["rule"] = a.rule
    if a.check:
        les["check"] = {**les.get("check", {}), **parse_check(a.check)}
    if a.uncheck:
        for k in a.uncheck:
            les.get("check", {}).pop(k, None)
    if a.must is not None:
        les["must"] = a.must
    if a.when is not None:
        les["when"] = [w.strip() for w in a.when.split(",") if w.strip()]
    les["status"] = "active"
    les["edited"] = now()
    save_book(path, book, scope)
    print(line(les))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    def scoped(p, glob=True):
        p.add_argument("--brand", help="client / library name (default: $VS_BRAND, or the task of --project)")
        p.add_argument("--project", help="project folder: its task's client is the brand")
        if glob:
            p.add_argument("--global", dest="glob", action="store_true", help="house rule (style/lessons.json)")
        return p

    b = scoped(sub.add_parser("brief", help="the rules to apply before planning"), glob=False)
    b.add_argument("--kind", help="reels,tiktok,youtube,ad,podcast...: only lessons for these (plus general ones)")
    b.add_argument("--max", type=int, default=25)
    ad = scoped(sub.add_parser("add"))
    ad.add_argument("--rule", required=True, help="one general, concrete rule with the number")
    ad.add_argument("--category", choices=list(CATEGORIES) + ["other"])
    ad.add_argument("--check", action="append", help="machine check key=value (vs lessons checks)")
    ad.add_argument("--must", action="store_true", help="breaking it fails QA (the client insisted)")
    ad.add_argument("--when", help="only for these kinds: reels,youtube,ad...")
    ad.add_argument("--keywords", help="extra words that identify this feedback (comma list)")
    ad.add_argument("--from", dest="from_", help="the note it came from: work/notes.json:3")
    ad.add_argument("--told", action="store_true", help="the person stated it as a rule (always/never)")
    ad.add_argument("--force", action="store_true")
    le = scoped(sub.add_parser("learn", help="unclassified notes and repeated feedback"), glob=False)
    le.add_argument("--notes", help="the project's work/notes.json")
    no = sub.add_parser("none", help="notes that were one-offs")
    no.add_argument("notes")
    no.add_argument("ids", nargs="+", type=int)
    ch = scoped(sub.add_parser("check"), glob=False)
    ch.add_argument("edl", nargs="?")
    ch.add_argument("--captions")
    ch.add_argument("--video", help="a render: enables the loudness check")
    li = scoped(sub.add_parser("list"))
    li.add_argument("--all", action="store_true")
    re_ = scoped(sub.add_parser("retire"))
    re_.add_argument("id")
    re_.add_argument("--why", required=True)
    ed = scoped(sub.add_parser("edit"))
    ed.add_argument("id")
    ed.add_argument("--rule")
    ed.add_argument("--check", action="append")
    ed.add_argument("--uncheck", action="append")
    ed.add_argument("--must", action=argparse.BooleanOptionalAction, default=None)
    ed.add_argument("--when")
    sub.add_parser("checks", help="the machine checks a lesson can carry")
    a = ap.parse_args()
    if a.cmd == "checks":
        for k, v in CHECKS.items():
            print(f"  {k:18} {v}")
        return
    {"brief": cmd_brief, "add": cmd_add, "learn": cmd_learn, "none": cmd_none, "check": cmd_check,
     "list": cmd_list, "retire": cmd_retire, "edit": cmd_edit}[a.cmd](a)


if __name__ == "__main__":
    main()
