#!/usr/bin/env python3
"""Set 4 v2 working sheet -> sheet.html (one shot per row, ≤3 s each, script locked)."""
import html, json
from pathlib import Path
OUT = Path(__file__).resolve().parent / "sheet.html"
# (t0, t1, VO exactly as in the brief, picture, source, on-screen text)
R = [
# --- HOOK H1 (banner "EVERY WART FIX, RANKED" stays 0–8.5 s, like the reference's pink banner)
("Hook", 0.0, 1.5, "There are only four ways", "Mom, kitchen table selfie (real home, filmed in Higgsfield, no cut-out), holds up four fingers", "HF-MOM", "Banner: EVERY WART FIX, RANKED"),
("Hook", 1.5, 3.2, "to get rid of a kid's wart,", "Bathroom counter: duct tape, acid pads, freeze can and the RootOut bottle in a row, hand sweeps along them", "HF-PRODUCT", "banner"),
("Hook", 3.2, 4.6, "ranked from weakest", "Hand lines up tape → pads → can, left to right, push-in", "HF-BROLL", "banner"),
("Hook", 4.6, 6.1, "to strongest.", "RootOut bottle slides in at the end of the row, label facing camera, fully in frame", "HF-PRODUCT", "banner"),
("Hook", 6.1, 8.5, "Most families never make it to number four.", "Mom, same take: small knowing shrug", "HF-MOM", "banner"),
# --- #1
("#1", 8.5, 9.9, "Number one,", "Real duct-tape roll on a table (CC photo), slow push-in", "REAL", "Rank card: 1 · DUCT TAPE"),
("#1", 9.9, 11.6, "duct tape.", "Hand tears a strip off a plain grey roll, close-up", "HF-BROLL", "—"),
("#1", 11.6, 13.2, "It sits on top of the wart for weeks.", "Small foot, side view: tape strip pressed over the bump, smoothed down", "HF-BROLL", "—"),
("#1", 13.2, 14.7, "Rent free.", "A sock peeled off, the tape stuck inside it, wart unchanged (dry humour)", "HF-BROLL", "—"),
("#1", 14.7, 16.6, "It never gets under the hard skin.", "3D skin cut-away: tape sits on the hard top, root untouched below", "HF-3D", "Source card: aafp.org “little documented evidence”"),
# --- #2
("#2", 16.6, 17.9, "Number two,", "Macro of round foam acid pads on a sheet", "HF-BROLL", "Rank card: 2 · ACID PADS"),
("#2", 17.9, 19.4, "acid pads.", "Fingers peel one pad off its backing", "HF-BROLL", "—"),
("#2", 19.4, 20.2, "A bit stronger.", "Pad pressed onto the ball of a small foot", "HF-BROLL", "—"),
("#2", 20.2, 21.8, "They peel it down", "Pad peeled back, skin white (v1 clip, keeps)", "REUSE", "—"),
("#2", 21.8, 23.5, "till the black dots are gone.", "Real plantar wart whitened after salicylic acid (CC photo)", "REAL", "—"),
("#2", 23.5, 25.3, "And it always seems to come back.", "NHS page: “may irritate your skin and do not always work”, phone screen, line highlighted", "REAL", "Source: nhs.uk"),
# --- #3
("#3", 25.3, 26.8, "Number three,", "Macro: white cold vapour rolling across a dark surface", "HF-BROLL", "Rank card: 3 · FREEZING"),
("#3", 26.8, 28.9, "freezing at the doctor's.", "Clinic: gloved hand, unbranded can, cold puff on a small sole (v1 clip, punched in)", "REUSE", "—"),
("#3", 28.9, 30.9, "The strongest one most of us know.", "Real wart being frozen with a cotton swab (public-domain photo)", "REAL", "—"),
("#3", 30.9, 33.6, "Somebody held him still every time.", "Adult hands hold a small ankle on exam-table paper; small fingers grip the paper", "HF-BROLL", "—"),
("#3", 33.6, 36.2, "It was agonizing for all of us.", "Mom in the parked car after the appointment, quiet, the joke gone", "HF-MOM", "—"),
("#3", 36.2, 38.0, "And after every visit,", "Clinic car park: small sneakers kicking in the back seat, appointment card on the dash", "HF-BROLL", "—"),
("#3", 38.0, 39.5, "there were two or three more.", "Small sole, now three small warts", "HF-BROLL", "Source card: clevelandclinic.org “can reappear”"),
# --- reveal
("Reveal", 39.5, 41.4, "Here's what nobody told me.", "Mom leans into the lens, sharing a secret", "HF-MOM", "—"),
("Reveal", 41.4, 42.7, "Freezing,", "3D skin: frost hits the hard top only", "HF-3D", "—"),
("Reveal", 42.7, 44.2, "acid and shaving", "3D skin: an acid drop and a blade scrape the top only (same render, 2nd half)", "HF-3D", "—"),
("Reveal", 44.2, 45.6, "only snap off the top,", "Real 1947 film: hand cuts a weed off at the ground (public domain)", "REAL", "—"),
("Reveal", 45.6, 47.5, "like picking a dandelion.", "Ground level: hand pinches a dandelion, stem snaps at the soil line, stub stays", "HF-BROLL", "—"),
("Reveal", 47.5, 49.8, "The root stays under the hard skin,", "Glass-sided soil box: snapped stub above, long white root still in the soil", "HF-BROLL", "—"),
("Reveal", 49.8, 51.1, "so it grows back.", "Real dandelion back at a kerb (CC photo)", "REAL", "—"),
("Reveal", 51.1, 53.2, "Every fix made it look done,", "Small sole looks smooth, a mom's thumb rubs the spot, relieved", "HF-BROLL", "—"),
("Reveal", 53.2, 55.4, "but the root never left.", "3D skin: camera dives under the smooth top, the root is still there, glowing", "HF-3D", "—"),
("Reveal", 55.4, 56.8, "It was never our fault.", "Mom: small shrug, relieved smile", "HF-MOM", "—"),
# --- #4
("#4", 56.8, 58.4, "Number four", "RootOut bottle hero on a bright bathroom counter, slow push-in, label front", "HF-PRODUCT", "Rank card: 4 · ROOTOUT (gold)"),
("#4", 58.4, 59.2, "gets the root.", "Real hand holding a whole dandelion with its long root (CC photo)", "REAL", "—"),
("#4", 59.2, 61.3, "It's RootOut, an oil with four plants,", "Mom holds the bottle beside her face, label clean and readable", "HF-MOM", "—"),
("#4", 61.3, 64.1, "and each one takes it a little deeper.", "Flat lay: bottle in the centre, lemon slice, tea-tree sprig, pokeweed berries, white-cedar twig around it", "HF-PRODUCT", "—"),
("#4", 64.1, 66.0, "Lemon goes first", "Macro: lemon cut open, one drop falls", "HF-BROLL", "label: LEMON"),
("#4", 66.0, 67.6, "and softens the hard top.", "3D skin: a yellow drop softens the hard top, a small door opens", "HF-3D", "—"),
("#4", 67.6, 69.5, "Tea tree is a thin oil,", "Macro: thin golden tea-tree oil drips from a dropper", "HF-BROLL", "label: TEA TREE"),
("#4", 69.5, 71.1, "so it sinks right in,", "3D skin: the thin oil slides down through the layers", "HF-3D", "—"),
("#4", 71.1, 73.9, "up to 8x deeper than a regular cream,", "3-paper-towel test (v1 clip)", "REUSE", "8x† + “AI placeholder · proof needed”"),
("#4", 73.9, 75.6, "and it carries the last two plants", "3D skin: two green droplets climb onto the golden oil", "HF-3D", "—"),
("#4", 75.6, 77.0, "down with it.", "3D skin: they ride it down through the layers (same render, 2nd half)", "HF-3D", "—"),
("#4", 77.0, 79.7, "Pokeweed and white cedar break the wart down from the", "Macro: pokeweed berries and a white-cedar twig, soft light", "HF-BROLL", "labels: POKEWEED · WHITE CEDAR"),
("#4", 79.7, 82.3, "root, so there's nothing left to grow back.", "3D skin: the root crumbles, the surface turns smooth", "HF-3D", "*homeopathic disclaimer"),
("#4", 82.3, 84.0, "Any one of them alone", "3D skin: a single drop sets off alone", "HF-3D", "—"),
("#4", 84.0, 85.6, "stops halfway.", "3D skin: it stalls halfway down (same render, 2nd half)", "HF-3D", "—"),
("#4", 85.6, 87.2, "Together, they reach the root.", "3D skin: all four reach the root, warm glow (same render, 2nd half)", "HF-3D", "—"),
# --- safety
("Safety", 87.2, 89.9, "And deep doesn't mean harsh.", "Mom, calm, bottle held low near her chest, label in frame", "HF-MOM", "—"),
("Safety", 89.9, 92.8, "It's a kids' formula, for ages 4 and up.", "Bottle on a kid's nightstand beside a picture book, label front", "HF-PRODUCT", "—"),
("Safety", 92.8, 94.0, "No acid,", "Hand drops an unbranded acid bottle into a bin", "HF-BROLL", "✕ ACID"),
("Safety", 94.0, 95.1, "no freezing,", "Spray can follows it in, lid closes (same render, 2nd half)", "HF-BROLL", "✕ FREEZING"),
("Safety", 95.1, 96.4, "no blister.", "Close side view of a smooth small sole, no blister", "HF-BROLL", "✕ BLISTER"),
("Safety", 96.4, 98.5, "Just a little cool tingle.", "Toes wiggle on the couch (v1 clip, cropped)", "REUSE", "—"),
("Safety", 98.5, 100.3, "And pediatricians recommend it.", "Pediatric office desk: stethoscope beside the bottle, label front", "HF-PRODUCT", "claim needs client proof"),
# --- routine
("Routine", 100.3, 101.9, "At bedtime, it's three steps.", "Nightstand under a warm lamp: bottle, files, dots", "HF-PRODUCT", "—"),
("Routine", 101.9, 104.1, "File:", "RootOut's own how-to video: 1 File", "REAL", "1 FILE"),
("Routine", 104.1, 106.1, "rub the little file over it twice,", "Small foot on a pillow, file strokes (v1 clip)", "REUSE", "—"),
("Routine", 106.1, 107.8, "just on the hard top.", "How-to video, file macro", "REAL", "—"),
("Routine", 107.8, 110.3, "Soak: brush the oil on.", "How-to video: 2 Brush", "REAL", "2 SOAK"),
("Routine", 110.3, 112.4, "Cover: a clear dot on top,", "How-to video: 3 Cover", "REAL", "3 COVER"),
("Routine", 112.4, 114.2, "so it soaks all night.", "Bedroom window night to dawn time-lapse, bottle on the nightstand in frame", "HF-PRODUCT", "9 PM → 5 AM"),
("Routine", 114.2, 116.8, "He's asleep before I put the cap back on.", "Mom whispering, screws the cap on, bottle fully visible", "HF-MOM", "—"),
# --- result
("Result", 116.8, 119.4, "Most spots, on a hand or a foot,", "A small hand and a small foot side by side on a blanket, no face", "HF-BROLL", "—"),
("Result", 119.4, 121.5, "are gone in about two weeks.", "Fridge calendar: 14 days crossed off (drawn in code so numbers stay sharp)", "CODE", "—"),
("Result", 121.5, 123.4, "Then you do fourteen more nights,", "Small hand writes “+14” on the calendar", "HF-BROLL", "+14 NIGHTS"),
("Result", 123.4, 125.4, "so the root is gone too.", "3D skin: clean layers, no root left", "HF-3D", "—"),
("Result", 125.4, 126.5, "Nobody gets held down,", "Kid runs barefoot down a hallway, from behind", "HF-BROLL", "—"),
("Result", 126.5, 128.2, "and there's nothing to book.", "Mom's thumb deletes a “Wart freeze” calendar event on her phone (screen text added in edit)", "HF-BROLL", "—"),
# --- close
("Close", 128.2, 130.7, "If your kid's wart keeps coming back,", "Mom on the sofa, direct to camera", "HF-MOM", "—"),
("Close", 130.7, 133.0, "you've been stuck at number three.", "Tape, pads and can swept into a drawer, drawer shuts", "HF-BROLL", "—"),
("Close", 133.0, 134.0, "Skip to number four.", "Bottle hero, gold light sweep", "HF-PRODUCT", "4 · ROOTOUT"),
# --- new CTA
("CTA", 134.0, 135.7, "It's at the link below.", "Real RootOut product page on a phone, finger taps the bundle", "REAL", "arrow ↓"),
("CTA", 135.7, 137.6, "Three for the price of two.", "Three bottles on the counter, a hand sets the third down (v1 clip, labels clean, caps fully in frame)", "REUSE", "BUY 2, GET 1 FREE"),
("CTA", 137.6, 140.1, "And if it's not gone, you get your money back.", "Real product page: “Buy 2 Get 1 Free” circled, 90-day badge pops", "REAL", "90-DAY MONEY-BACK"),
("CTA", 140.1, 143.1, "(no VO)", "End card: bottle slowly turning on a clean ice-blue set, full cap and label in frame, generous margins", "HF-PRODUCT", "Not the top. The root. · Shop now · AI illustration."),
]
ALT = [
("H2", "One wart turned into fifteen.", "Small foot on a towel, a cluster of small warts (v1 clip)", "REUSE"),
("H2", "So here's every fix we tried, ranked from weakest to strongest.", "Crowded shelf of half-used remedies (v1 clip) → the counter line-up from shot 2", "REUSE + HF"),
("H2", "Only number four got the root.", "Mom holds the RootOut bottle up on “four” (no finger counting, so the four-finger mistake can't recur)", "HF-MOM"),
("H3", "R.I.P., my kid's wart.", "Bathroom counter: a small blank cardboard tombstone beside the remedies; “R.I.P. WART” added in edit", "HF-BROLL"),
("H3", "You will not be missed.", "Mom, deadpan, taps the tombstone over", "HF-MOM"),
("H3", "Here's every fix we tried, ranked from weakest to strongest.", "Counter line-up (shots 2–4)", "HF-PRODUCT"),
]
SRC = {"HF-MOM": "Higgsfield · mom", "HF-PRODUCT": "Higgsfield · product", "HF-BROLL": "Higgsfield · b-roll", "HF-3D": "Higgsfield · 3D skin",
       "REAL": "Real footage / page", "REUSE": "v1 Higgsfield clip", "CODE": "Code graphic"}
from collections import Counter
cnt = Counter(r[5] for r in R)
lens = [r[2] - r[1] for r in R]
rows = "\n".join(
    f'<tr><td class="n">{i+1}</td><td class="t">{r[1]:.1f}–{r[2]:.1f}<span>{r[2]-r[1]:.1f}s</span></td><td class="sec">{html.escape(r[0])}</td>'
    f'<td class="vo">“{html.escape(r[3])}”</td><td>{html.escape(r[4])}</td><td><span class="chip {r[5].lower()}">{SRC[r[5]]}</span></td>'
    f'<td class="ost">{html.escape(r[6])}</td></tr>' for i, r in enumerate(R))
alts = "\n".join(f'<tr><td class="sec">{a}</td><td class="vo">“{html.escape(v)}”</td><td>{html.escape(p)}</td><td><span class="chip {s.split()[0].lower()}">{s}</span></td></tr>' for a, v, p, s in ALT)
# credit quote (Seedance 2.5 720p high = 7 cr/s)
q = [("Mom clips, lip-synced, real home settings (8 lines + H2/H3)", "10 clips · ~65 s", 455),
     ("Product shots with the real bottle as reference", "9 clips · ~40 s", 280),
     ("3D skin animations (one locked style frame)", "8 clips · 32 s", 224),
     ("B-roll", "24 clips · 96 s", 672),
     ("Start frames (Soul) + style frame", "~40 images", 25)]
tot = sum(x[2] for x in q)
qrows = "\n".join(f"<tr><td>{a}</td><td>{b}</td><td class='num'>{c:,}</td></tr>" for a, b, c in q)
doc = f"""<title>RootOut Set 4 Working Sheet</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,500;6..72,600&family=Inter:wght@400;500;600;700&display=swap">
<style>
/* Layout: one production document, rules first, then the shot list as a wide scrolling table */
:root {{ --bg:#F6F8FB; --panel:#FFFFFF; --fg:#13223D; --muted:#5A6678; --line:#DCE3EC; --navy:#0B2A5B; --blue:#1763B8; --orange:#E04E18;
  --mom:#E8F0FB; --prod:#FDEBE3; --broll:#EAF5EC; --d3:#F2ECFA; --real:#FFF6D9; --reuse:#EEF0F3; --code:#E9F6F7;
  --serif:"Newsreader", Georgia, serif; --sans:"Inter", system-ui, sans-serif; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --bg:#0E1522; --panel:#152035; --fg:#E7EDF6; --muted:#9AA8BC; --line:#26344C; --navy:#9CC0F0; --blue:#6FA8EC; --orange:#F2875C;
  --mom:#1C2D4A; --prod:#3A2418; --broll:#18301F; --d3:#2A2140; --real:#3A3216; --reuse:#232A36; --code:#173236; color-scheme:dark; }} }}
:root[data-theme="dark"] {{ --bg:#0E1522; --panel:#152035; --fg:#E7EDF6; --muted:#9AA8BC; --line:#26344C; --navy:#9CC0F0; --blue:#6FA8EC; --orange:#F2875C;
  --mom:#1C2D4A; --prod:#3A2418; --broll:#18301F; --d3:#2A2140; --real:#3A3216; --reuse:#232A36; --code:#173236; color-scheme:dark; }}
body {{ background:var(--bg); color:var(--fg); font-family:var(--sans); font-size:15px; line-height:1.5; }}
.wrap {{ max-width:1180px; margin:0 auto; padding-left:max(16px, env(safe-area-inset-left, 0px)); padding-right:max(16px, env(safe-area-inset-right, 0px)); padding-block:32px 64px; display:grid; gap:28px; }}
h1 {{ font-family:var(--serif); font-weight:600; font-size:clamp(28px,4vw,40px); letter-spacing:-.02em; line-height:1.1; margin:0; color:var(--navy); text-wrap:balance; }}
h2 {{ font-family:var(--serif); font-weight:600; font-size:24px; margin:0 0 12px; color:var(--navy); }}
.lede {{ color:var(--muted); max-width:70ch; margin:6px 0 0; }}
.meta {{ display:flex; flex-wrap:wrap; gap:8px 18px; font-size:13px; color:var(--muted); margin-top:12px; }}
.meta b {{ color:var(--fg); font-weight:600; }}
section {{ background:var(--panel); border:1px solid var(--line); border-radius:14px; padding:22px; min-width:0; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:16px; }}
.grid > div {{ min-width:0; }}
h3 {{ font-size:13px; text-transform:uppercase; letter-spacing:.06em; color:var(--blue); margin:0 0 6px; }}
ul {{ margin:0; padding-left:18px; display:grid; gap:4px; }}
.fix td:first-child {{ color:var(--muted); width:40%; }}
.scroll {{ overflow-x:auto; }}
table {{ border-collapse:collapse; width:100%; font-size:13.5px; }}
th {{ text-align:left; font-size:11.5px; text-transform:uppercase; letter-spacing:.06em; color:var(--muted); border-bottom:2px solid var(--line); padding:8px 10px; position:sticky; top:0; background:var(--panel); }}
td {{ border-bottom:1px solid var(--line); padding:8px 10px; vertical-align:top; }}
.shots table {{ min-width:1040px; }}
td.n {{ color:var(--muted); font-variant-numeric:tabular-nums; }}
td.t {{ white-space:nowrap; font-variant-numeric:tabular-nums; }}
td.t span {{ display:block; font-size:11.5px; color:var(--muted); }}
td.sec {{ font-weight:600; white-space:nowrap; }}
td.vo {{ font-family:var(--serif); font-size:15px; min-width:200px; }}
td.ost {{ color:var(--muted); font-size:12.5px; }}
.chip {{ display:inline-block; font-size:11.5px; font-weight:600; padding:3px 8px; border-radius:999px; white-space:nowrap; color:var(--fg); }}
.hf-mom {{ background:var(--mom); }} .hf-product {{ background:var(--prod); }} .hf-broll {{ background:var(--broll); }} .hf-3d {{ background:var(--d3); }}
.real {{ background:var(--real); }} .reuse {{ background:var(--reuse); }} .code {{ background:var(--code); }}
.counts {{ display:flex; flex-wrap:wrap; gap:8px; margin-bottom:12px; }}
.num {{ text-align:right; font-variant-numeric:tabular-nums; }}
tfoot td {{ font-weight:700; border-bottom:none; }}
.safe {{ display:grid; grid-template-columns:minmax(0,170px) minmax(0,1fr); gap:18px; align-items:start; }}
.phone {{ aspect-ratio:9/16; max-width:170px; border:2px solid var(--fg); border-radius:18px; position:relative; overflow:hidden; background:var(--bg); }}
.phone div {{ position:absolute; font-size:9px; font-weight:600; display:flex; align-items:center; justify-content:center; text-align:center; }}
.z-ui {{ background:color-mix(in srgb, var(--orange) 22%, transparent); color:var(--orange); }}
.z-ok {{ border:1.5px dashed var(--blue); color:var(--blue); }}
.ask {{ border-left:3px solid var(--orange); padding-left:12px; }}
@media (max-width:560px) {{ .safe {{ grid-template-columns:1fr; }} }}
@media (prefers-reduced-motion: reduce) {{ * {{ scroll-behavior:auto; }} }}
</style>
<div class="wrap">
<header>
  <h1>RootOut Set 4 · v2 working sheet</h1>
  <p class="lede">“Every wart fix, ranked.” A full rebuild of v1, cut to the reference ad's pace. Nothing gets generated until you approve this sheet. The spoken script is the client's brief, word for word: same voice, same lines, nothing added or removed.</p>
  <div class="meta"><span><b>{len(R)}</b> shots</span><span>median shot <b>{sorted(lens)[len(lens)//2]:.1f} s</b>, longest <b>{max(lens):.1f} s</b></span><span>runtime <b>~2:23</b> (H1)</span><span>9:16 · captions on</span><span>reference: SoFyre #035</span></div>
</header>

<section>
  <h2>What changes from v1</h2>
  <table class="fix"><tbody>
  <tr><td>One cut-away animation held for long stretches</td><td>A new picture at least every 3 s. Each shot shows the words being said. The 3D skin animation appears in short 1–3 s bursts only, mixed with real footage and b-roll.</td></tr>
  <tr><td>Mom keyed out of a green screen (rough edges)</td><td>No cut-outs. The mom is filmed whole inside Higgsfield in a real home (kitchen, car, sofa), and appears in short beats like a UGC host.</td></tr>
  <tr><td>Product sometimes small, covered or cropped</td><td>Every product shot is made in Higgsfield with the real bottle as reference. Label always facing camera, cap and base in frame, hands never over the label. Any frame that breaks this gets re-rolled.</td></tr>
  <tr><td>2:30–2:37 end card cut off the bottle's cap</td><td>New CTA: the real product page on a phone, a three-bottle shot, the offer circled like the reference, then a clean end card made in Higgsfield with the whole bottle and wide margins.</td></tr>
  <tr><td>Glitches (edge fringing, keyed hair, zoomed-in takes)</td><td>Every clip comes from Higgsfield at one size, with no compositing. Each clip is checked frame by frame before the edit, and every talking clip is checked word for word against the script.</td></tr>
  </tbody></table>
</section>

<section>
  <h2>How the reference is cut (SoFyre #035, measured)</h2>
  <div class="grid">
    <div><h3>Pace</h3><ul><li>44 shots in 78.6 s, median 1.6 s</li><li>Hard cuts only, many with a slow push-in or pull-out</li><li>The first cut lands at 1.4 s</li></ul></div>
    <div><h3>Structure</h3><ul><li>A hook banner sits on screen for the first 9 s</li><li>Each rank opens on a big number and name card</li><li>Every line is shown literally (“bad air freshener” = mint in a jar)</li></ul></div>
    <div><h3>Mechanism and proof</h3><ul><li>One or two short “inside the body” 3D shots per rank</li><li>Product held, turned and placed, always fully in view</li><li>Ends on the real checkout page with the offer circled</li></ul></div>
  </div>
</section>

<section>
  <h2>Rules for every frame</h2>
  <div class="safe">
    <div class="phone" aria-label="9:16 safe zone diagram">
      <div class="z-ui" style="left:0;right:0;top:0;height:7%">top UI</div>
      <div class="z-ui" style="right:0;top:7%;bottom:20%;width:13%;writing-mode:vertical-rl">buttons</div>
      <div class="z-ui" style="left:0;right:0;bottom:0;height:20%">caption + CTA bar</div>
      <div class="z-ok" style="left:7%;right:15%;top:12%;bottom:24%">text safe zone</div>
    </div>
    <div class="grid">
      <div><h3>Text and headlines</h3><ul><li>All titles, rank cards, source cards and captions sit inside the safe zone: clear of the top bar, the right-hand buttons and the bottom 20%</li><li>Captions: 2–4 words, lower middle (as in the reference)</li><li>Hook banner and rank cards: upper third</li><li>Disclaimers (†, *) small, above the caption line</li></ul></div>
      <div><h3>Product</h3><ul><li>The real RootOut bottle in every product shot (front + duo images as reference)</li><li>Label front-on and readable, never mirrored, nothing covering it</li><li>Whole bottle in frame, cap included, with margin on every side</li></ul></div>
      <div><h3>Kids and claims</h3><ul><li>No child faces: feet, hands, sleeves, backs of heads only</li><li>Paper-towel test stays labelled “AI placeholder · proof needed”</li><li>Source cards quote the page unchanged, with no logos and nothing implying endorsement</li></ul></div>
    </div>
  </div>
</section>

<section class="shots">
  <h2>Shot list · H1</h2>
  <div class="counts">{''.join(f'<span class="chip {k.lower()}">{SRC[k]} · {v}</span>' for k, v in cnt.most_common())}</div>
  <div class="scroll"><table>
  <thead><tr><th>#</th><th>Time (s)</th><th>Beat</th><th>Voice-over (locked)</th><th>Picture</th><th>Source</th><th>On screen</th></tr></thead>
  <tbody>{rows}</tbody></table></div>
</section>

<section>
  <h2>H2 and H3 openings</h2>
  <p class="lede" style="margin:0 0 10px">Everything after the hook is the H1 cut. Only the first 7–9 seconds change.</p>
  <div class="scroll"><table><thead><tr><th>Hook</th><th>Voice-over (locked)</th><th>Picture</th><th>Source</th></tr></thead><tbody>{alts}</tbody></table></div>
</section>

<section>
  <h2>Look and sound</h2>
  <div class="grid">
    <div><h3>One story, one family</h3><ul><li>Same mom, same home, same kid (feet only) in every shot</li><li>Warm, natural phone look, matching the reference's warm grade</li><li>One 3D skin style frame, locked first and reused for every 3D shot</li></ul></div>
    <div><h3>Edit</h3><ul><li>Cuts land on the voice phrase, as in the reference</li><li>A slow push-in or pull-out on most shots, no flashy transitions</li><li>Sound under every shot: room tone and a small effect on each action</li></ul></div>
    <div><h3>Kept from v1</h3><ul><li>The locked voice (Quinn) and the word-for-word script checks</li><li>Seven v1 clips that passed review: pad, clinic, paper towels, toes, file, bottles, shelf/cluster</li><li>Real photos, the 1947 film, the brand how-to, the source pages</li></ul></div>
  </div>
</section>

<section>
  <h2>Higgsfield quote (WilloMd)</h2>
  <div class="scroll"><table><thead><tr><th>What</th><th>Amount</th><th class="num">Credits</th></tr></thead>
  <tbody>{qrows}</tbody>
  <tfoot><tr><td>First pass</td><td></td><td class="num">{tot:,}</td></tr>
  <tr><td>Re-roll budget (~25%, product and hands rules are strict)</td><td></td><td class="num">{round(tot*.25):,}</td></tr>
  <tr><td>Ceiling</td><td></td><td class="num">{round(tot*1.25):,}</td></tr></tfoot></table></div>
  <p class="lede">Seedance 2.5 at 720p, high bitrate, 7 credits per second. Balance when this sheet was written: 4,259 credits, shared with the other sets' sessions on the same workspace.</p>
</section>

<section class="ask">
  <h2>To confirm before I start</h2>
  <ul>
    <li><b>Approve this sheet and the credit ceiling.</b></li>
    <li>“Text heading line has to be safe”: I read this as all on-screen text inside the platform safe zone (diagram above). Tell me if you meant something else.</li>
    <li>The mom appears in 8 short beats (≤3 s each) and the rest is voice-over over b-roll, like the reference. Say if you want more or fewer of her.</li>
    <li>Still open with the client: “pediatricians recommend it”, the kids' formula vs pokeweed/white cedar, real paper-towel test footage.</li>
  </ul>
</section>
</div>
"""
OUT.write_text(doc); print(OUT, len(R), "shots", tot, "credits", "max", max(lens), "median", sorted(lens)[len(lens)//2])
