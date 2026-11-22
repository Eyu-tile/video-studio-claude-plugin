---
name: ai-presenter
description: Generate the footage an edit is missing - an AI talking-head presenter (UGC creator style or VSL host) with lip-synced speech, b-roll shots, start frames and voiceover - through the Higgsfield MCP (Soul ID character, Seed Audio voice, Seedance talking clips, image and video models) or another connected generator, track every generation, bring the results back into the project and continue the edit. Use when an ad or video needs a presenter who wasn't filmed, "generate the talking head", "make an AI UGC creator", "generate b-roll for line 4", or /ugc-ads has no creator footage.
---

# AI presenter and generated b-roll

Claude runs the generations (MCP tools); `vs gen` plans them as jobs, hands over exact inputs, downloads and
checks the results, and builds the EDL. Then the normal edit continues (`/ugc-ads`, `/video-edit`).

## 0. Connect the account (once per account)
The Higgsfield MCP (`https://mcp.higgsfield.ai/mcp`) signs in through the browser; there is no key to paste. The
plugin ships one connection, `higgsfield`. For several accounts (clients, brands) each gets its own connection
and sign-in: run **`/connect-higgsfield`** (asks which account, adds `higgsfield-<name>`, walks the person through
/mcp → Authenticate, checks the tools, makes it active), or by hand `vs higgsfield add <name>` then /mcp.
`vs higgsfield use <name> [--project $P]` picks the account a project generates with; `vs gen plan` records it
and `vs gen next` names it. Only call that connection's tools (`mcp__higgsfield-<name>__*`, found with your tool
search); never spend credits on another account. Tool names come from the server, so read their descriptions
rather than assuming. In the Claude app: Settings → Connectors → custom connector with the URL, one per account. Not connected → tell the person how to connect it and stop; never fake
generated results. Other generators (HeyGen via `/media-use`, Veo, Kling...) work the same way: the job
file doesn't care which provider ran it, only what came back.

**Before the first billable call in a session or project** (generation, upload, upscale): run
`vs higgsfield current --project $P` and do its `before_billing` steps. If a client's team workspace is set,
`list_workspaces`, then `select_workspace` when it isn't selected; without one, clear a leftover team selection. The
selection persists across sessions and projects, so check every time. Then call `balance` and say which account,
workspace and credits will pay ("Billing Acme's team workspace on higgsfield-acme, 2,140 credits"). After switching
accounts, re-upload reference media: ids don't carry across accounts.

## 1. Script → jobs
Write `$P/work/gen/<v>.script.json` from the ad plan (`/ugc-ads` step 3): the presenter (`look` detailed
enough to repeat, `voice`, `setting`, `consent`), and one entry per line: `say`, `show` (`talking` or `broll`),
`perform` (the gesture/expression on specific words), and for b-roll the shot plus `source`
(`generate`, `library` or `shoot`). Prefer the client's real footage for b-roll and the product: generate only
what doesn't exist.
```bash
vs gen plan $P/work/gen/v1.script.json      # character, voice, then per clip: speech -> start frame -> talking clip
```
Clips are ≤ 12 s of speech (lip-sync models drift on long takes; Higgsfield's talking-character tools cap
around 15–30 s). **GATE:** show the person the presenter description, the lines per clip, the number of
generations, and the provider's cost estimate (Higgsfield shows credits before generating). Generate only
after they agree.

## 2. Run the jobs
```bash
vs gen next $P/work/gen/v1.jobs.json        # the jobs whose inputs are ready, with prompts and dependency results
```
For each ready job, call the matching Higgsfield tool:
- `character`: train a Soul ID once (20–80 reference images, varied angles, one full-height shot; ~10 min) or
  reuse an existing one by name (`presenter.soul_id`). Record its name with `--ref`.
- `voice`: pick a Seed Audio preset matching `presenter.voice` (or a clone of a voice the person owns or has
  written permission for). `--ref` the voice id.
- `speech`: Seed Audio text-to-speech of `text` with that voice. `--url` the audio file.
- `frame`: an image of the character with the frame prompt (neutral mouth, lips closed, the clip's framing and
  aspect). Reuse frame1 for later clips in the same setting.
- `talking`: Seedance 2.5 (or the account's lip-sync video model) with the start frame, the speech audio and the
  video prompt (performance cues written against the script). `--url` the clip.
- `broll`: an image/text-to-video model with the prompt, at the edit's aspect.
Record each result straight away: `vs gen done <jobs> <id> --url <download url> --model <model> --credits <n>`
(or `--file` for a downloaded file, `--ref` for an id). A bad result: `vs gen fail <jobs> <id> --why "..."`,
improve the prompt in the jobs file, `vs gen retry`, run it again. Look at every talking clip before moving on
(`vs watch <file> -o work/gen/check_<id>`): lips in sync, same face as the other clips, no warped hands or text.

## 3. Back into the edit
```bash
vs gen fetch $P/work/gen/v1.jobs.json --project $P              # raw/gen/, checks (audio, length), credits ledger
vs gen edl $P/work/gen/v1.jobs.json -o $P/work/ads/v1.edl.json   # talking clips in order, b-roll over its lines
```
`edl` transcribes each clip to place every b-roll line on the exact words, and lists lines still needing
footage (`library`/`shoot`): fill them from the client's footage (`vs watch`, `vs ingest`) as `overlays`. Then
continue `/ugc-ads` step 4 (punch-ins, hook text, captions, music, CTA) and step 5 (QA).

## Rules
1. Never present an AI presenter as a real customer or a real testimonial (FTC rule on fake reviews and
   testimonials). It may speak as a brand presenter or a clearly fictional character; no invented personal results.
2. Real person's face or voice only with their documented consent (`presenter.consent`). Never imitate a
   celebrity or a real creator.
3. Label AI-generated content where the platform requires it (Meta and TikTok AI labels); keep `ai_generated`
   in the credits ledger.
4. Claims in generated speech follow the brief's claims list exactly; nothing the evidence doesn't support.
5. Report generations used and credits spent per variant.
