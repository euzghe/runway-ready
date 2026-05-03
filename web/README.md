# Runway Ready — Web Edition (Week 3 Playable)

Single-file browser game. **No internet, no install, no dependencies.** Double-click `index.html` and play.

---

## How to launch (in class, tomorrow)

1. Open Finder → `~/Desktop/Runway-Ready-Week3/web/`.
2. Double-click `index.html`.
3. It opens in your default browser (Safari / Chrome — both work).
4. If Safari blocks JavaScript: Safari menu → Settings → Advanced → tick "Show Develop menu" → Develop → Disable JavaScript (uncheck).

If you want to be safe before class: run it once at home tonight, leave the browser tab open, and use that same tab tomorrow.

## How to play (60-second briefing for the playtesters)

> "Each of you runs a fashion house. To send outfits down the runway, you produce the same paper trail a software test team produces — strategy, plan, design, cases. **Half of the Outfit cards have planted ISO defects.** During Inspection, the non-active players hunt for those defects and tap the field they think is wrong. If a defect escapes Inspection, the Outfit fails on the runway and you must trace which ISO field caused it. The dice cannot save bad documentation."

## Game flow

1. **Welcome** — choose 3 or 4 players, type names, click Start.
2. **Each player's turn** runs through 6 phases automatically:
   - PLAN → pick a Runway Roadmap (Project Test Plan)
   - DESIGN → pick a Collection Theme (Test Design Spec)
   - SPECIFY → pick 3 Outfits (Test Case Specs)
   - INSPECTION → 60-sec rival flag-spotting
   - EXECUTION → d6 per outfit, automatic outcomes
   - RESOLUTION → click the originating ISO field on each failed outfit
3. **Turn-end summary** — Rehearsal Summary table appears, click Next Player.
4. **Game-end leaderboard** — full per-player Rehearsal Summary + flaw debrief.

Total time for 3-4 players: **~10 minutes**.

## Scoring (auto-tracked)

| Action | Points |
|---|---|
| Outfit walks cleanly | +3 |
| Inspection: caught a real flaw | +2 to flagger |
| Inspection: false flag | −1 to flagger |
| Resolution: correctly named originating ISO field | +2 |
| Resolution: wrong field or timeout | −4 |
| Outfit lost (flawed defect) | −2 |
| Bad-luck failure (clean outfit, dice 1–2) | −1 |

## What if something breaks

| Symptom | Fix |
|---|---|
| Browser tab feels stuck | Hit Refresh (⌘R). Game restarts cleanly from welcome screen. |
| Modal won't close | Click outside the modal or refresh. |
| Timer shows 0 but nothing advances | Click "Done inspecting →" in inspection, or any field in resolution. |
| Screen too small | Layout is built for ≥ 1200 px width. Plug into a projector or a larger display. |
| Play with only 2 testers? | The welcome screen shows 3/4 only. For 2 players, type the same name twice — works but Inspection has only 1 inspector. |

## What the playtesters should answer afterwards (verbal — 30 sec each)

1. Did the game make any **ISO concept** clearer than reading the standard would?
2. Was there a moment a defect that *looked* like bad luck turned out to be a documentation flaw?
3. What is the **single biggest thing** to fix for Week 4?

Their answers feed straight into the Week 4 improvement plan. Capture them on paper or in your phone notes — the game itself doesn't record them.

## How the educational design works (for the grader, in case they ask)

- **Concept Accuracy (20 pts):** every card in the game labels its ISO field name in italics; the cards in `02_Cards/` are the source of truth.
- **Learning Objectives (15 pts):** each of the 4 Week-2 objectives maps to a specific in-game mechanic — see `../05_Playtesting/Learning_Outcome_Checklist.md`.
- **Educational Effectiveness (20 pts):** the game makes misconceptions visible by (a) Structural Gating in phases, (b) the 60-sec Inspection rivalry, (c) deterministic failure on unflagged flaws, (d) named originating fields on every defect, (e) the post-game Rehearsal Summary table.
- **Prototype Quality (35 pts):** runs in a browser in 10 minutes, click-to-play, no setup time, automatic scoring.
- **Reflection (10 pts):** the per-player Rehearsal Summary on the end screen IS the reflection artefact — it shows each player exactly which ISO fields they failed on.

## Files in this folder

- `index.html` — the game. The only file you need.
- `README.md` — this file.

## Backup plan if the laptop dies

The physical card game also exists. See `../02_Cards/` for printable card content and `../01_Rulebook/` for the full rules. The web version is a re-implementation of the same rules — anything you learn from the web playtest applies to the cardboard game and vice versa.
