# Hume Health: Video Editor SOP digest

Source: public Notion page "Video Editor Day 1 Onboarding SOP" and every page and database it links to. Crawled 2026-11-12 through Notion's public API: 21 pages and 27 databases. Redacted copies of the pages are in `pages/`. Database rows are in `data/` as JSON.
Shared logins, passwords and staff emails in the SOP were **removed on purpose**. Ask ops through the approved password manager or invite flow; never copy them into this repo.

Precedence: when older pages disagree, the **Day 1 Onboarding SOP wins** over the Video Editor SOP, the Creatives SOP and Creative Briefing (OLD). Notion replaces ClickUp and Trello. Fish Audio replaces ElevenLabs. The new naming scheme replaces the old one.

---

## 1. Company, products, people
- **Client:** Hume Health Corp. The agency side is Cubert. Slack workspace: itsfittrack, channel #video-editor-chat.
- **Products (keep them as separate tracks; never combine unless the brief says so):**
  - **Hume Pod** (also called Body Pod, Pod 2.0). An at-home body-composition device. It uses hand-and-foot (8-sensor), multi-frequency BIA and gives segmental composition: body fat, muscle, hydration and trends. Promise: *"Know what your body is made of, not just what you weigh."* HSA/FSA eligible where applicable (claim still in review). "45+ body metrics" is also still in review.
  - **Hume Band 2.0** (in the database also "Band", "Band Strap"). A wrist wearable plus the Hume app. It tracks sleep, stress, recovery, activity and trends. Positioning: interpreted data, not another dashboard, and no required monthly subscription for core use (in review; verify the offer first).
  - **Pod + Band Ecosystem** (product code PODBAND). Body composition from the Pod plus daily signals from the Band. Use it only when explicitly briefed.
  - **Prof AI**: the in-app AI. Always call it "Prof AI". Pronunciation test in VO: "Hume Pod", "Hume Band 2.0", "Prof AI".
- **Roles:** Isabel Moreno handles editing coordination, capacity and review routing. The assigned creative strategist owns the script, angle and feedback (strategists in the trackers: Ani, Jet, Kush, Priyansh). Poorvi / ops handles the Notion Office, permissions and task visibility. Ani handles Fish Audio access. A VA handles the final upload handoff. A Creative Director reviews when the task requires it.

## 2. The Hume editing bar (the core taste rules)
Hume creative is **belief-change first, not feature-first.**
- Hook in the **first 2 seconds**. "If it doesn't hook in the first 2 seconds, it doesn't ship."
- Make **one belief shift** clear (old belief → new belief).
- Use **one main proof point or metric.**
- Show app UI, the body map, the product, a testimonial or a graph **only when it proves the claim**.
- **The app screen must match the spoken metric.** Biological age gets the biological-age screen. A Prof AI insight gets the relevant Prof AI screen. If a proof asset is missing, ask for it; never substitute a generic dashboard.
- Confirm the hardware generation (Hume Pod vs Hume Band 2.0). If the database says "Band", the brief must clarify it.
- Avoid: feature dumping, logo-first or slow intros, pretty b-roll that proves nothing, over-produced TikTok-style UGC, unsupported medical claims.
- **Claim grammar:** the *product* detects, tracks, reveals, surfaces and helps users see patterns. The *user* prevents, protects, decides and acts.

## 3. Editing rules
**Hook / first frame**
- Hook text appears immediately (frame 1). Large, high contrast.
- The first frame must make the concept clear. **Never animate the scroll-stopper text in** (the Creatives SOP has an example of what not to do).
- Approved hook styles: shock/disbelief, fake apology, direct callout, before/after implication, desire-based ("younger", "stronger", "energy").
- Vocabulary: **HOOK** = text + audio in the first seconds. **HEADLINE** = hook text that differs from the audio. **SCROLL STOPPER (SS)** = the visual that goes with the hook.

**Pacing**
- A visual change every **1–3 s**. Never let a static frame sit too long.
- Ways to change the visual: zoom in/out, crop jump, cut to b-roll, app chart overlay, body render, product close-up. Use them intentionally and don't overuse them.
- Zooms are subtle and digital, and should feel organic or handheld, not robotic or patterned.
- Music feels native and emotional, matches the cut rhythm, and supports the VO without overpowering it.

**Captions**
- A caption **starts and finishes on the same clip.** It never crosses a cut.
- Lines are balanced: "I always struggle / with dark spots", not "I always struggle with dark / spots".
- Short, punchy, typo-free, readable on mobile.
- **Color only 1–3 words** in red or blue: problem words, negative states (pain, risk, mistake), triggers ("STOP", "WARNING", "DON'T", "THIS IS WHY"). Everything else is white. Example: "This is why your **METABOLISM** is failing".
- Native TikTok concepts need organic captions (TikTok native font). No shadows on organic/lo-fi videos.
- Use **no more than two text styles per video.**
- Emojis: **iOS emojis only**, small, placed intentionally next to the text.
- Headlines need breathing room, so use generous margins.

**Safe zones and framing**
- All text and faces sit inside the platform safe zones. Overlay the 9:16 Reels and 4:5 Feed safe-zone PNGs before delivery and check that nothing is covered.
- Not too low (CTA/caption UI) and not too high (username UI).
- Faces stay fully visible, with eyes in the upper-middle. Never crop the forehead, eyes or mouth.
- Preview at mobile scale before export.

**Style by concept type**
- Lo-fi UGC stays native and organic. Don't over-produce it.
- Polished concepts may use **CTA end cards** with this hierarchy: small logo → headline → subheadline → button. Product render/video or an image at the bottom.

**Voiceover (Fish Audio)**
- Sentence endings need clear pauses. "This is the Hume Health Pod." must sound finished. Known error: a missing period in the Concept 16 Pod ad at 0:21.
- Control phrasing with punctuation: commas, periods for pauses, "!" for energy, "..." for hesitation, dashes for a turn, "?" for curiosity, CAPS for occasional emphasis.
- Generate a short test first and check pronunciation. Use a library voice or a clone of an approved creator recording. Save the voice reference and the VO file with the task assets.

## 4. Brand
- Principle: make health data feel clear, credible and actionable, not intimidating or fluffy. Data first, not decoration. Clinical clarity with modern polish. Performance beats prettiness. Every element earns its place.
- **Colors:** Hume Blue primary **#1882FF**, secondary **#31ABE8**, plus black and white. Blue means trust/science, white means clinical/clean, black means authority/contrast. Gradients only for tests and backgrounds.
- **Fonts:** **Red Hat Display** (principal), **Canela** (serif accent), **TikTok Display** (native UGC).
- Asset sources (access via ops): Figma Creative Guideline, Figma "Hume Ads", Figma mobile-app designs, the Drive LOGOS and TYPOGRAPHY folders, and a Frame.io "Band animation" share. See `SOURCE_LINKS.md`.

## 5. Formats, specs, deliverables
- Formats: UGC talking head, VO + b-roll, podcast clips, AI/hybrid UGC, high-end. Production-database creative styles: Static, UGC, Classic, UGC B-roll + VO, AI Slop, UGC Creator, B-Roll Lifestyle, Meme, Yapper, Visual Concept, Brand Commercial, Motion Graphics, Physical Props.
- **Edit 9:16 first.** First review = **two renders**: (a) one with all requested hooks / scroll stoppers, and (b) one full body edit with a selected hook. Use at least 3 brief-provided hooks; ask before inventing hook copy.
- **Final default sizes: 1:1, 9:16, 16:9** (Day 1 SOP). The older checklist asks for 1080×1350 (4:5) and 1080×1920; 4:5 is still used heavily (395 of 1,000 tasks). Follow the task's Size field. Reframe and QA each size.
- Platforms: Meta (main), TikTok, YouTube (Shorts/TV/Demand Gen), AppLovin, Snapchat, CTV.
- Length depends on the brief. Channel playbook: Meta UGC runs 6–35 s with the hook in **1.5 s and proof by second 5**. TikTok 12–45 s. YouTube 30–90 s (long-form 2–4 min). CTV 15/30/60 s.

## 6. Naming (Hume Ad Namer, hume-ad-namer.netlify.app)
`FORMAT_PRODUCT_PARENTANGLE_SUBANGLE_HOOK_ASSIGNEE_EDITOR_TAG_DDMMYY_YYYYWeek##_RATIO`, with no spaces.
Product codes: POD, BAND, PODBAND. HOOK is 2–5 words in CamelCase. Each ratio and hook variation gets its own name. **Keep the same base name across revisions** so Frame.io stacks the versions. The older names in the winner library (e.g. `Video_BFCM_SorryMenOver40_4_…`) are historical.
Parent angles used: Seasonal, Health, Tech, Longevity, VsCompetitor, WeightLoss, Value, Persona, Proof, Enemy, Motivation, Muscle, Stress, Action. Top sub-angles: VisceralFat, BlackFriday, Offer, VsAllWearables, PreventiveHealth, BloodPressure, GLP1, Holiday, DEXAAccuracy, VsSmartScale, ProgressTracking, ChronicDetection, VsWhoop, VsCheapScale.

## 7. Workflow (Notion production database "Video and Static Ad Database")
Status labels: Ready for Editor → Edit In-Progress → Needs Feedback - CS / Needs Feedback - CD → Edit In-Revision → Edit Needs Resize → VA to upload. Side states: Blocked / Missing files/footage, Moved to Sheet (ops only). There is no "Approved" status; record approval in a comment. Never edit status options.
Frame.io: stack versions, never delete old versions, never rename, and share with the **Share** link (not the browser URL). Post the link in the Notion task comment and mention the reviewer.
After approval: upload the finals and the Premiere/FCP project to the delivery folder (keep CapCut projects locally and note where). Write a handoff comment (approver, date, folder, hooks/sizes, project location), set VA to upload and mention the VA.
Flag blockers within 4 hours of pickup. Old cadence: brief Thursday → draft Tuesday → finals Friday.

## 8. Final QA checklist (merged)
Brief followed · correct product and generation · hook lands in 2 s · captions typo-free · each caption on one clip · readable on mobile · text and faces in safe zones · VO paced with clean sentence endings · visual change every 1–3 s · proof assets match the claim (screen = spoken metric) · CTA if required · claims brand-safe (see `../04_do_not_use/DO_NOT_USE.md`) · targets a specific audience · backed by research · color on 1–3 key words · ≤2 text styles · correct ratios · file name correct, no spaces · Frame.io versions kept · finals only after approval · project files uploaded or kept.
