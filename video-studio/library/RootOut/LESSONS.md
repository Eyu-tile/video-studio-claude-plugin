# Lessons: RootOut

Learned from feedback. Apply before planning; `vs qa --brand` checks the ones marked checked.

## assets
- [L12] Shared Higgsfield library: before generating any clip, image or voice, search library/RootOut/higgsfield/catalog.py (every WilloMd generation from all sessions, with prompt, references and download URL) and reuse a fitting one first (0 credits). Right after every new generation, add it: catalog.py add <job_id> --type video --name <short> --set 'Set N' --notes '<what it shows>' [--verdict use|backup|reject], then commit and push to rootout-library so every session sees it. To pick up generations a session forgot to log, page mcp__WilloMd__show_generations (type video/image/audio, size 100) into files and run catalog.py build <files>.  (MUST)
- [L8] Mechanism animations move: 3D skin cross-sections like the Amoils #004 reference (hard top, wart, root; drops, door, root dissolving), never flat static diagrams. Reuse the shared clips first (library/RootOut/ads/set18_build/REUSE.md and the other sets' jobs.json, 0 credits) before generating.  (MUST)
- [L9] Web screenshots only from real public pages (AAD, NHS, Cleveland Clinic, PubMed, the WilloMD site), text quoted unchanged with the line highlighted, no third-party logos; log the source. Never fake reviews, Reddit posts or comments.  (MUST)

## brand
- [L1] The product on screen is always the real RootOut bottle (small amber bottle, tall glossy white cap, white label with navy 'RootOut', blue band). Never an AI bottle with a garbled or different label. Make product shots with Seedance 2.5 using the real bottle as image_references (WilloMd media 2c52c56e-9f2f-4f40-9fda-4caa813e7578), or use the real PDP photos; Soul cannot hold the label.  (MUST)

## captions
- [L5] Captions run through the whole video (bold word-by-word, active word highlighted), kept clear of the product, graphics, web cards and the hook title.  (MUST)

## cuts
- [L2] Every b-roll shot is about 3 s (1.5-4 s), one shot per spoken phrase, cut on her words (get word timings with vs transcribe on the VO). Never one long clip under several lines.  (MUST)
- [L3] Each b-roll shot shows exactly what is being said at that moment (dandelion on 'dandelion', file on 'file', brush on 'brush', root under the skin on 'root'). Check every shot against the word timings before rendering; replace any shot that only fits the mood.  (MUST)
- [L4] Each b-roll source is used once per ad; no freeze frames; no slow motion below 0.75x.  (MUST)

## delivery
- [L11] Deliver to the WilloMD Drive folder (vs deliver --to willomd) only after the person says approved, and only the newest _vN of each hook; never drafts or raw renders; verify every size in Drive.  (MUST)

## framing
- [L10] Kids' faces are never in frame: feet, hands, pajama legs, backs of heads only.  (MUST)

## music
- [L6] Background music runs to the last frame and stays clearly audible on the offer and end cards: lift the bed where nobody speaks, and skip any near-silent bar in the track. Only a short fade on the final frame.  (MUST)

## sound
- [L7] No room tone or sound effects in the mix unless the client asks for them (client notes on Sets 5 and 18): voice and music only.
