# RootOut library (WilloMD)

WilloMD RootOut™ Advanced Wart, Corn & Callus Oil: a brush-on bedtime oil, **File · Soak · Cover**.
"Freezing burns the top. This oil soaks down to the root.*" Brand: WilloMD (Alderion LLC). Read before any RootOut edit:

1. `DO_NOT_USE.md`: hard rules. The site's before/after photos and reviews are **illustrative/AI**: never use as real results.
2. `CLAIMS.md`: every claim on the site with its risk and the disclaimers (`*`, `†`) that must travel with it.
3. `BRAND_GUIDE.md`: palette (navy `#0B2A5B`, blue `#1763B8`, ice `#EEF4FA`, CTA orange `#E04E18`), Newsreader + Inter,
   look, voice, current offer.
4. `ads/SET13_BRIEF.md` (Set 13 script, verbatim) + `ads/set13_build/` (shot plan, job ids, builder, web-insert credits). `ads/ROUND1_SCRIPTS.md`: the client's Round 1 scripts (locked Sets 1, 4, 5, 13, 17, 18, 19, 20), footage needs
   mapped to this library, and the claim checks to clear first. `references/REFERENCES.md`: every swipe ad behind
   them (video, scene breakdown, frame sheet, what to steal, what not to copy) + `references/PLAYBOOKS.md`.
   `ads/AD_ANGLES.md`: the angles the PDP uses (site-derived, not tested winners).
5. `resources/ATLAS.md`: every site asset with status (built with `vs learn`). `WINNING_ADS.md`, `USAGE_LOG.md`.

## Layout
| path | what |
|---|---|
| `brand/images/pdp/` | the 9 PDP gallery images (v11), 3 tier flat lays, 3 tier packshots, bottle front, transparent duo PNG |
| `brand/images/lifestyle/` | bathroom-at-night render |
| `brand/images/samples_illustrative/` | 10 AI before/after samples (BANNED as results; kept for reference) |
| `brand/images/sister_meltoff/` | 2 Melt-Off images (other product; BANNED in RootOut ads) |
| `resources/site_videos/` | `rootout-1v1-root-v6.webm` (10.3 s, freezing vs oil cross-section) + its mp4 copy `shopify-3062835a.mp4`; `rootout-how-to-v3.webm` (7.1 s, File/Brush/Cover macro loop) + its mp4 copy `shopify-ff701bf4.mp4`; posters. All 1080x1080, silent |
| `resources/site_snapshot/` | page text of the PDP and home page, `product.json` (Shopify product data) as read on 2026-11-21 |
| `resources/` | `vs learn` files: `ATLAS.md`, `atlas_full.json`, `inventory.json`, `sources.json`, `usage.json` (sheets not committed) |

## Sources
| added | source | provider | files | sampled | described |
|---|---|---|---|---|---|
| 2026-11-21 | https://trywillomd.com/products/rootout (official PDP) + home page | web (`vs learn`) + Shopify JSON | 49 listed (42 images incl. size duplicates, 4 videos = 2 unique, 3 HLS segments) | 46 | **all 46 by eye**; 21 unique images + 2 unique videos |

Re-read the site: `vs learn scan RootOut` (new files only get sampled), and re-pull `https://trywillomd.com/products/rootout.js`
to check price/offer changes.

## Open-internet stock (`stock/`, started 2026-11-21)
- Searched 42 queries by ad beat (problem, failed fixes, life, routine, science) on YouTube (Creative Commons only),
  Internet Archive, Wikimedia and Openverse; no paid stock keys. ~380 results, title-filtered to 291, 79 picked by hand.
- `stock/youtube_candidates/YOUTUBE_CANDIDATES.md`: 77 YouTube CC videos looked at frame by frame and graded
  (8 A clean b-roll, 21 B usable part, 10 BANNED competitor brands, 38 C rejected), with the one command that downloads
  the A+B set. **Not downloaded:** YouTube blocks this cloud server; run it on a normal computer.
- `stock/assets/photo/`: CC photos downloaded with licences in `stock/assets/credits.json` / `CREDITS.md` (Wikimedia
  rate-limited the rest). Media files are git-ignored; the ledger and catalogue are committed.
- Weak spots on the free internet: corns (results were food/moths), kids with warts, freeze-spray use without a brand,
  bedtime routine b-roll. Plan to fill these with Higgsfield (`WilloMd`) or real shoots.

## Higgsfield account (generation for RootOut)
- Use **only** the `WilloMd` connection (`https://mcp.higgsfield.ai/mcp?willomd`, connected in Claude): tools
  `mcp__WilloMd__*`. Never the plugin's `higgsfield` or `higgsfield-Spin360` connections for RootOut work.
- Checked 2026-11-21: private workspace `ab6cddcc-4e64-4d4a-96e5-18b040dffc7d` (owner, no team workspace), Ultra plan,
  8,496.67 credits.
- **House models (owner, 21 Nov):** images = **Higgsfield Soul** (`soul_2`, ~0.12–1 credit per frame) · video =
  **Seedance 2.5 at 720p** (`seedance_2_5`, mode `omni_reference`, 7 credits/second, 4–30 s; talking clips lip-sync to an
  `audio_references` voice file) · voice = **ElevenLabs inside Higgsfield** (`elevenlabs_v4`, preset voices from
  `list_voices`, ~1 credit per 45 words). Don't switch models without asking.
- Before every billable call: `mcp__WilloMd__list_workspaces` (private workspace selected), `mcp__WilloMd__balance`, say the
  account + credits, and get the person's yes on the cost. `vs higgsfield use` can't name this connector (it only knows
  `higgsfield-<name>`), so this README is the record.

## Open questions for the client
- Logo: the site uses a text wordmark only. Vector logo / packaging files?
- Real footage: product B-roll, UGC creators, real customer before/afters and reviews (the site's are illustrative)?
- Claim sign-off: "soaks down to the root", timelines, "no tears"/kids, "no blisters or scars", the 8x test report.
- Which formula is sold and shown, adult or Kids 4+? Is the kids oil a separate SKU?
- Past ads, winners, performance data; target platforms; any competitor-mention rules.
- Brand accounts: Higgsfield workspace and any API keys for this brand (to be added with `vs keys` / environment secrets).
