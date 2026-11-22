---
name: ugc-ads
description: Produce direct-response video ads - UGC (creator/testimonial style, phone-shot, native to the feed) and VSLs (video sales letters: scripted argument over a presenter or b-roll) - from a client brief to several tested variants. Brief → audience/emotion/awareness decisions → scripts per hook angle → footage pull list → edits → ad QA (hook, words on screen, stimulus, safe zones, CTA, loudness, compliance) → review page. Use for "make UGC ads", "cut 5 variants of this ad", "turn this brief into ads", VSLs, testimonial ads, performance creative, or batches of ads for Meta/TikTok/YouTube.
---

# UGC and VSL ads

You are engineering a decision, not cutting a nice video. Every ad is judged by numbers (hook rate, hold
rate, CTR, ROAS); taste is a tool for hitting them. Read `references/playbook.md` once per client: it is
the house standard with the sources behind it.

Project folder `$P` as in `/video-edit` (`vs new <client>-<product>`).

Task code: start or resume the client task first (`/task-history`): `vs task new <CODE> ...`, or `vs task resume <CODE>`
when returning to one. After delivering, `vs task deliver <CODE> --file ... --note ...`; log client comments with
`vs task feedback`.

## 1. Brief → GATE (never open a timeline without it)
```bash
vs ads brief $P/work/brief.json          # writes a template the first time
```
Fill it from the client's brief and assets, then run the same command to check it. It must answer the
five questions in writing: **who exactly** (`audience.who`), **age/gender skew**, **one primary emotion**,
**awareness level** (Schwartz: unaware, problem, solution, product, most), **where it runs** (platform). Plus
the offer, the single CTA, every claim with its evidence, the creator and how they're paid (disclosure), and
the policy category (health, weight_loss, supplement, beauty, finance...). Missing answers → ask the
account lead; don't guess. FAILs here (claims without evidence, paid creator without disclosure,
before/after for weight loss) block production.

## 2. Plan
```bash
vs ads plan $P/work/brief.json -o $P/work/ads [--variants 5 --length 25]
```
`plan.md` turns the brief into decisions: hook type from awareness, voice and pace from age, caption flags,
music mood/tempo with a drop on the reveal, stimulus gap, length range, safe zone, and a beat map per variant
(UGC: hook → problem → discovery → demo/result → proof → CTA; VSL: hook → problem → agitation → mechanism →
proof → offer → CTA). Variants differ in **hook angle**; the body can be shared. Show the person the plan
and the hook lines before cutting (GATE) unless told "no stops".

## 3. Scripts and pull list
For each variant, write the script into its beats: one idea per line, the benefit word early in the line,
specifics (numbers, timeframes, named problems), no adjectives without a visual claim, ≤ `max_words`. Then a
pull list: for every line, the shot that proves it (product in use, real hands, real environment, the
mechanism up close, the result). Find them in the client's footage (`vs ingest`, `vs breakdown`, the library),
mark gaps to shoot or source (`/video-assets`, never generic stock that could sell anything).
**No creator footage, or missing shots?** Generate them with `/ai-presenter`: an AI talking-head presenter
(Higgsfield MCP: Soul ID, Seed Audio, Seedance lip-sync) and b-roll as tracked jobs; `vs gen edl` hands back a
ready EDL for step 4. Winning
reference ads: `/video-breakdown` them first and follow their pacing.

## 4. Edit each variant
Build `$P/work/ads/vN.edl.json` with `/video-edit` mechanics (`vs cuts` on the creator's takes, `vs edl`):
- **Hook (≤ 3 s):** motion, a face or the product in frame 1; no logo, intro or fade-in; the first spoken
  words on screen by 0.5 s (captions, or a hook `texts` line at `pos: top`). Strongest line first, even if
  it was later in the script.
- **Body:** b-roll that literally matches each line within the same second; a new visual every 1.5–3.5 s
  (cut, punch-in `zoom`/`kf`, text pop, overlay); demo and result, not features. One look: match sourced clips
  (`vs ai match`).
- **CTA (last 3–5 s):** the offer as text (`texts`, held ≥ 2.5 s), product hero shot held longer, calm
  voice, one action, the last note of music after the last word.
- **UGC voice:** keep natural breaths and a small stumble; slight room tone is fine; no studio polish.
  **VSL voice:** zero dead air (gaps < 400 ms except one dramatic beat), clean and compressed
  (`audio.enhance`), slow down on the single most important sentence.
- Music per the plan: impact/riser or a sudden silence under the hook, tension under the problem, drop on
  the reveal (`vs beats`, `vs music fit`), ducked 12–18 dB under speech.
- Captions last, after the cut is locked: `vs captions ... <captions_args from plan.json>` (they keep out of
  the platform UI for the preset automatically). One font, white with a heavy outline, one accent colour on
  the benefit word.

## 5. QA every variant (the delivery standard)
```bash
vs review $P/work/ads/v1.edl.json --brief $P/work/brief.json --preset reels --captions $P/work/ads/v1.ass
vs ads qa $P/out/ads/v1.mp4 --edl $P/work/ads/v1.edl.json --brief $P/work/brief.json \
    --captions $P/work/ads/v1.ass -o $P/out/ads/v1.qa.json            # on the final render
```
Automated: spec and length, first frame (no black/fade, something moving), first words on screen by
0.5 s, hook ≤ 3 s, no stretch > 3 s without a new visual, safe zones, one CTA held ≥ 2.5 s that matches the
brief, −14 LUFS / ≤ −1 dBTP, music ducked, one look across shots, compliance from the brief. By hand
(say you did): watch once fully muted, once on a phone at arm's length; every claim has its visual on the
same beat. No variant ships with a FAIL.

## 6. Review page and delivery
```bash
vs ads sheet $P/out/ads -o $P/out/ads/review.html --brief $P/work/brief.json
```
One page with every variant, its verdict and open warnings, for the client. Deliver 1080×1920 (or the
platform's aspect) named `<client>_<product>_<variant>_<platform>.mp4`, plus `.srt`. Report per variant:
angle, length, QA verdict, anything not verified. When results come back, write what won (hook type,
length, pacing) into `style/moves.md` for this client.

## Rules
1. Brief before timeline. Audience and emotion decide script tone, music, b-roll and captions.
2. Never fabricate a testimonial, a reviewer, a result or a "customer" (FTC rule on fake reviews and
   testimonials, in force since Oct 21, 2024). AI avatars or voices only when the client asks, never presented
   as a real customer; never clone a real person's voice or face without their consent.
3. Paid creators: the material connection is disclosed (platform paid-partnership label and/or #ad).
4. Every claim in the script has evidence in the brief; health, weight-loss, supplement, finance and beauty
   ads get a policy check (Meta bans before/after side-by-sides for weight loss).
5. Don't polish UGC into a brand film. Raw, native and specific beats glossy.
