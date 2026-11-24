# Set 19 build kit (ROS19, v1, 22 Nov): "It's in our house" · the school nurse with 400 kids

H1/H2/H3/H4, 9:16, 3:04–3:14, captions throughout. Script used **word for word** (`SCRIPT.md`): VO lines and every
caption word are checked against it (captions.py asserts the caption words equal the script).
Project (media, renders) lives in `video-studio/projects/rootout-set19/` and is git-ignored.

| file | what |
|---|---|
| `SCRIPT.md` | the locked Set 19 brief text from the client's Round 1 doc |
| `SHOT_PLAN.md` | beat-by-beat routing: real footage → real screenshot → code graphic → Higgsfield, with the quote |
| `WEB_SOURCES.md` | the study (checked: 1,465 kids, OR 1.9, pool/showers/barefoot "not related"), Mixkit ids, CC photos, what was blocked |
| `GEN_LOG.md` / `jobs.json` | every Higgsfield job (voice, cast refs, 11 talking clips, 24 b-roll), safety-filter rewrites, spend |
| `broll_prompts.json` | the b-roll prompts (reuse for other sets) |
| `edit.py` | the cut, row by row: talking pieces keep their lip-synced audio, VO rows cut b-roll on exact words |
| `build.py` | piece renderer (9:16 crop of 16:9 stock, Ken Burns on photos, overlays, label blur, ambience bed) |
| `render_gfx.py` | code graphics: real PubMed page card + sentence close-up, "about 2x" house card, $250 receipt, 8x gauge with † line, calendar label, end card |
| `captions.py` | script-text captions timed from the audio, bold-pop, moved to the top over the study page, off the end card |
| `finish.py` | mix (voice + ambience + "Carefree" ducked), hook text, captions, phone-camera finish, loudnorm |
| `shot_study.js` | Playwright phone-size capture with highlights (`node shot_study.js <url> <out.png>`) |

Rebuild: `python3 work/edit.py H1 && python3 work/captions.py H1 && python3 work/finish.py H1 v1` (needs `work/vo_words.json`
and `work/talk_words.json`, whisper word stamps of the VO lines and talking clips).

## What's different from Set 1
New mom, voice (Hallie), rooms (bathroom, car, couch); the family-feet motif; real study page instead of AAD cards; new skin
cutaway clips; brand how-to footage for the brush step; Mixkit real b-roll; music "Carefree" (Set 1: "Promises to Keep").

## Open items for the client (unchanged claim checks + Set 19 specifics)
- "Recommended by pediatricians", "kids' formula, ages 4 and up" + pokeweed/white cedar (ROUND1 checks 1–3) are in the
  script and were kept as written; they still need sign-off.
- Study wording: the paper says "a family member with warts"; the script says "someone at home". Close; legal to confirm.
- AI people: the second mom's line is an AI testimonial; per client, no on-screen "AI testimonial" text (use the platform AI label).
- Real PubMed page in a paid ad: no NIH logo shown; legal to confirm.
- Credit lines for the post copy: Music "Carefree" by Kevin MacLeod (incompetech.com), CC BY 4.0; photo "Painful plantar
  warts", Wikimedia Commons, CC BY-SA 4.0.
- Review page (H1–H4 v3, one tab per hook, comments per hook in collections comments_H1..H4): https://claude.ai/artifact/5GAPigi1KyMvdJz82y4cAj
- **Delivered 2026-11-24:** v3 H1–H4 (9:16) to WilloMD Drive `WilloMD/WilloMD_RootOut_Set19` (https://drive.google.com/drive/folders/1OT17hpS4mqtIVVzu0I1A_XByHB-HOwV4), all 4 verified at full size.
