# Runway Ready — Quick Reference (1 page)

## Goal
Send outfits down the runway by producing **valid ISO/IEC 29119-3 documentation** at every layer. The player whose paper trail survives execution wins.

## Setup
1 Brand Identity face-up · Hand of 5 Outfits + 1 Roadmap + 1 Theme · Wardrobe Malfunction & Event decks in centre.

## Turn — 5 phases, in order

| # | Phase     | ISO doc                   | Required action                                                |
|---|-----------|---------------------------|----------------------------------------------------------------|
| 1 | Plan      | Project Test Plan         | Place Runway Roadmap (Scope / Schedule / Resources)            |
| 2 | Design    | Test Design Specification | Place Collection Theme on Roadmap                              |
| 3 | Specify   | Test Case Specification   | Play ≥3 Outfit Detail cards under the Theme                    |
| 4 | Procedure | Test Procedure Spec       | Place Runway Instructions (sequence + dependencies)            |
| 5 | Rehearsal | Execution + Defects       | Read aloud → Inspection 60 s → Roll d6 per outfit → Score      |

**You may not skip a phase.** Skipping is the misconception this game refuses to let you have.

## Rehearsal sub-steps

1. Read each Outfit's *Pre-conditions* and *Expected Result* aloud.
2. Opponents have **60 seconds** to call out a flaw → +2 to the spotter, you must Revise.
3. Roll d6 per Outfit:
   - 1–2 → Wardrobe Malfunction (resolve via Traceability).
   - 3–6 → Walks cleanly **unless an unflagged planted flaw exists** — then it always fails.
4. Fill your Rehearsal Summary pad.

## Resolving a Wardrobe Malfunction

1. The card names the **originating ISO field** (e.g., *Pre-conditions*).
2. Find the doc on your mat at fault.
3. **Say out loud** what was wrong with that field.
4. Discard / lose 2 pts. Cannot identify in 30 s → −4 pts and Carry-Over Defect.

## Scoring (per round)

| Action                                           | Pts  |
|--------------------------------------------------|------|
| Outfit walks cleanly                             | +3   |
| Procedure dependency held                        | +1   |
| Named originating doc field correctly            | +2   |
| Spotted a rival's planted flaw (Inspection)      | +2   |
| Used a Revision                                  | −1   |
| Unresolved Wardrobe Malfunction                  | −4   |
| Out-of-hierarchy play attempt                    | −2   |

## Lite (10-min demo) variant

1 round · exactly 3 Outfits per player · skip Events · merge Procedure into Specify.

## Memory hooks (the only fashion-flavour bit you need)

| Card                 | Brain hook                       | ISO doc                       |
|----------------------|----------------------------------|-------------------------------|
| Brand Identity       | "the house style — never breaks" | Organizational Test Strategy  |
| Runway Roadmap       | "this season's plan"             | Project Test Plan             |
| Collection Theme     | "this collection's idea"         | Test Design Specification     |
| Outfit Detail        | "one outfit on one model"        | Test Case Specification       |
| Runway Instructions  | "who walks when"                 | Test Procedure Specification  |
| Wardrobe Malfunction | "the broken zipper"              | Defect Report                 |
| Rehearsal Summary    | "post-show recap"                | Test Status / Completion Rep. |
