# Turn Flow Diagram

The game enforces the ISO/IEC 29119-3 documentation hierarchy as a **strict, non-skippable phase order** within each turn.

## Macro flow (one round)

```
                     ┌──────────────────────────────────┐
                     │     GAME SETUP (≈ 2 min)        │
                     │  - 1 Brand Identity per player  │
                     │  - Decks shuffled & placed      │
                     │  - Starting hand dealt          │
                     └────────────────┬─────────────────┘
                                      │
                                      ▼
            ┌────────────────────────────────────────────┐
            │  PLAYER 1 TURN  (≈ 2–3 min)                │
            │  Phases 1 → 5, in order                    │
            └────────────────┬───────────────────────────┘
                             │
                             ▼
            ┌────────────────────────────────────────────┐
            │  PLAYER 2 TURN  (≈ 2–3 min)                │
            └────────────────┬───────────────────────────┘
                             │
                             ▼
                          (… etc …)
                             │
                             ▼
            ┌────────────────────────────────────────────┐
            │  ROUND END                                 │
            │  - Rehearsal Summary pads filled           │
            │  - Scores totalled                         │
            │  - Lite variant: GAME ENDS HERE            │
            │  - Full variant: next round                │
            └────────────────────────────────────────────┘
```

## Micro flow (one player turn — the 5 phases)

```
┌─────────────────────────────────────────────────────────────┐
│ PHASE 1 — PLAN                                              │
│   ISO doc:  Project Test Plan                               │
│   Action:   Place a Runway Roadmap on your mat              │
│   Gate:     Brand Identity must already be active           │
│   Reveal:   Roadmap constraints become public               │
└────────────────────────────┬────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────┐
│ PHASE 2 — DESIGN                                            │
│   ISO doc:  Test Design Specification                       │
│   Action:   Place a Collection Theme on the Roadmap         │
│   Gate:     Roadmap must be active                          │
│   Reveal:   Coverage criteria become public                 │
└────────────────────────────┬────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────┐
│ PHASE 3 — SPECIFY                                           │
│   ISO doc:  Test Case Specification                         │
│   Action:   Play ≥ 3 Outfit Detail cards under the Theme    │
│   Gate:     Theme must be active                            │
│   Reveal:   Each Outfit's 7 ISO fields become public        │
│             (this is where planted flaws enter play)        │
└────────────────────────────┬────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────┐
│ PHASE 4 — PROCEDURE                                         │
│   ISO doc:  Test Procedure Specification                    │
│   Action:   Place a Runway Instructions card                │
│   Gate:     ≥ 3 Outfits must be specified                   │
│   Reveal:   Inter-outfit dependencies declared              │
└────────────────────────────┬────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────┐
│ PHASE 5 — REHEARSAL                                         │
│   ISO doc:  Test Execution + Defect Reports                 │
│   Sub-step 5a: Read aloud each Outfit's Pre/Expected        │
│   Sub-step 5b: Inspection (60 sec rival-spotting)           │
│   Sub-step 5c: d6 execution per Outfit                      │
│   Sub-step 5d: Resolve any Wardrobe Malfunctions            │
│                via Traceability (name the field)            │
│   Sub-step 5e: Score, fill Rehearsal Summary line           │
└─────────────────────────────────────────────────────────────┘
```

## Gate logic (what "non-skippable" means in practice)

If a player attempts an action whose gate is unmet:

1. The action is **physically undone** at the table (card returned to hand).
2. Player loses **−2 points** for the attempted out-of-hierarchy play.
3. The opponent who calls the violation gains **+1** Inspection-style point (called a *Hierarchy Catch*).
4. Play resumes from the correct phase.

This makes the "I'll just skip writing the plan" move both **visible** and **costly** at exactly the moment it is attempted.
