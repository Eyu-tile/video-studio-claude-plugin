---
name: feedback-learning
description: Learn from every piece of feedback so the same mistake never reaches a client twice - turn notes into per-brand lessons (with machine checks where possible), brief them before planning, flag repeated feedback, and fail QA when a lesson is broken. Use at the start of every edit for a client, after every revision round, and when the person says "remember this", "always", "never", "don't do that again", "we told you before", "same mistake", or "what have we learned about <client>".
---

# Learning from feedback

Lessons are concrete rules learned from notes, kept where they apply:
- **per brand**: `video-studio/library/<Brand>/lessons.json` + `LESSONS.md` (each client has its own library);
- **house rules** for every brand: `video-studio/style/lessons.json` (`--global`). Old one-liners in `style/notes.md`
  still show up in the brief.

The brand is the task's client (`vs task new ... --client`), so `--project <folder>` or a notes file inside
`projects/<P>/` finds it by itself; otherwise pass `--brand <Client>` or set `VS_BRAND`.

## 1. Before planning anything for a client
```bash
vs lessons brief --brand <Client> [--kind reels|youtube|ad|podcast...]
```
A short ranked list (MUST first, then what was repeated most). Apply every line in the plan and say in the plan which
lessons shaped it ("music at -22 dB per L1"). Read `LESSONS.md` only when the brief points to more.

## 2. When notes arrive
`vs notes add ...` and `vs task feedback ...` log every note in the brand's feedback history and compare it with the
lessons. **`REPEAT:`** means we made a mistake we had already learned about. Fix it first, tell the person plainly
("this was already a lesson, L1; it slipped because there was no check"), then tighten the lesson: add a `--check`,
make it `--must`, or sharpen the rule with `vs lessons edit`.

## 3. After every revision round: decide what each note teaches
```bash
vs lessons learn --brand <Client> --notes $P/work/notes.json
```
It lists the handled notes not yet classified, and feedback that came back across projects with no lesson yet (the
strongest candidates). For each note ask: **would this note apply to the next video for this client?**
- One-off ("swap this shot", "typo at 0:12"): `vs lessons none $P/work/notes.json <ids>`.
- Taste or rule ("music too loud", "captions too small", "never the old logo"): write a GENERAL rule with the number
  you actually fixed it to, not the note's words:
  ```bash
  vs lessons add --brand <Client> --rule "Music bed at -22 dB or lower under speech" --category music \
      --check music_gain_max=-22 --from $P/work/notes.json:3 [--when reels] [--must] [--told]
  ```
  `--told` when the person said always/never; `--must` when they insisted or it was a repeat (breaking it fails QA);
  `--when` when it only applies to some formats. For a house rule for everyone, use `--global`.
- Add a `--check` whenever the rule is measurable (`vs lessons checks`): `music_gain_max`, `sfx_gain_max`,
  `sfx_per_min_max`, `shot_min`/`shot_max`, `hook_max`, `duration_max`/`duration_min`, `banned_transitions`,
  `banned_grades`, `banned_sources`, `required_sources`, `banned_words`, `text_size_min`, `text_font`,
  `caption_words_max`, `caption_case`, `lufs`. Rules about taste that can't be measured stay as rules in the brief.
- A lesson you inferred (they didn't say "always") goes in too. Tell the person in one line what you'll remember, and
  that `vs lessons retire --brand <Client> <id> --why "..."` forgets it. A note that contradicts a lesson means the
  lesson changed: `vs lessons edit` or `retire` it, never keep both.

## 4. Before every delivery
`vs qa ... --brand <Client> [--captions <the .ass>]` (or `vs lessons check $P/work/edl.json --brand <Client>`) runs
every checked lesson: FAIL for a broken MUST lesson (blocks delivery), WARN otherwise. Fix and re-run; a caught
violation is counted on the lesson ("caught before delivery").

## Rules
- Never add a lesson from a client to another client's library; brand taste does not transfer.
- One lesson per rule: `add` refuses a near-duplicate (it counts it as seen again instead).
- Lessons are short, general and have a number where one exists. "Make it pop" is not a lesson; ask what it meant.
