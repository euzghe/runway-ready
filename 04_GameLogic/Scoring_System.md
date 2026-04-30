# Scoring System

## 1. Scoring table (canonical)

| # | Action                                                | Points          | Educational signal                                                |
|---|-------------------------------------------------------|-----------------|-------------------------------------------------------------------|
| 1 | Outfit walks cleanly                                  | +3 per outfit   | Documentation produced an executable test case                    |
| 2 | Procedure dependency held                             | +1 per case     | The Procedure Spec actually constrained execution                 |
| 3 | Named originating doc field correctly (Traceability)  | +2 per defect   | The player can articulate the root cause                          |
| 4 | Inspection Point — spotted a rival's planted flaw     | +2 per flag     | The player can read someone else's documentation critically       |
| 5 | Hierarchy Catch — called a rival's out-of-order play  | +1 per call     | The player has internalised the hierarchy                         |
| 6 | Used a Revision (mid-turn correction)                 | −1 per use      | Revisions are healthy but not free                                |
| 7 | Wardrobe Malfunction unresolved (no field named)      | −4 per case     | Failed traceability — the canonical 29119-3 sin                   |
| 8 | Out-of-hierarchy play attempt                         | −2 per attempt  | Skipped a documentation phase                                     |
| 9 | Carry-Over Defect (per round it remains)              | −1 per round    | Open defects accumulate cost                                      |

## 2. Worked example (one player, one round)

Player Aysel runs *Maison Solère* (Brand Identity §sustainable materials).

- Phase 1 — Plays "SS26 Capsule Drop" Roadmap → 0 pts.
- Phase 2 — Plays "Mediterranean Breeze" Theme → 0 pts.
- Phase 3 — Plays 3 Outfits:
  - **OD-C-01** (clean linen slip dress)
  - **OD-F-03** (planted flaw: polyester foil gown — violates Brand Identity)
  - **OD-C-13** (clean linen kaftan)
- Phase 4 — Plays "Linear Walk" procedure → 0 pts.
- Phase 5 — Rehearsal:
  - Read aloud: rival catches OD-F-03's polyester (Inputs field) during Inspection.
    - Aysel: −0 (no penalty for being caught — Inspection is a discount on a worse fate)
    - Rival: +2 Inspection Point.
  - Aysel uses a Revision to swap OD-F-03 for OD-C-08 (foil-finish — sustainable variant). −1.
  - Rolls d6 for each of the 3 (now-clean) Outfits: 4, 5, 2.
    - OD-C-01: 4 → walks. +3.
    - OD-C-08: 5 → walks. +3.
    - OD-C-13: 2 → Wardrobe Malfunction. Draws WM-03 ("Train caught on rig"). Originating field: *Post-conditions / Expected Result*. Aysel verbalises: "My Expected Result didn't specify train clearance against the lighting rig" → +2 for naming, −2 for losing the Outfit.

**Round total: +3 +3 +2 −2 −1 = +5 points.**

## 3. Why no positive score for "having lots of cards on the table"

A common card-game design instinct is to reward volume. We deliberately do not. *Runway Ready* rewards:

- **Documentation that survives execution** (lines 1–2 in the table)
- **Articulation of cause** (line 3)
- **Critical reading of others' work** (lines 4–5)

It penalises:

- **Failure to articulate cause** (line 7 — the −4 is the largest single penalty in the game)
- **Skipping documentation steps** (line 8)

The point distribution itself is the lesson. A player who optimises for points has, by construction, optimised for ISO 29119-3 documentation discipline.

## 4. Tie-breakers

If two players have equal scores at game end:

1. Fewer **unresolved defects** wins.
2. If still tied, more **Inspection Points** wins (rewards the better peer reviewer).
3. If still tied, more **named-originating-field** points wins (rewards the better root-cause analyst).
