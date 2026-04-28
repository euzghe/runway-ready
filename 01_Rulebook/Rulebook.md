# RUNWAY READY — Official Rulebook (Prototype v1)

> A card game that teaches **ISO/IEC 29119-3 Test Documentation** by running a fashion house.
> 3–4 players · 10–15 minutes · One 10-minute round = one playable demo.

---

## 1. Educational premise (read this first)

Every player runs a small fashion house preparing for a runway show. To send outfits down the runway, you must produce **the same hierarchy of documents that a software test team produces**. The fashion words are flavour; the **bracketed terms in italics on every card are the actual ISO/IEC 29119-3 fields** and they are what the game scores you on.

You do **not** win by luck. You win by writing documentation that another player cannot poke a hole in.

## 2. Components

| Qty | Component                          | Maps to ISO/IEC 29119-3        |
|-----|------------------------------------|--------------------------------|
| 8   | Brand Identity cards               | Organizational Test Strategy   |
| 12  | Runway Roadmap cards               | Project Test Plan              |
| 10  | Collection Theme cards             | Test Design Specification      |
| 30  | Outfit Detail cards (½ have planted flaws) | Test Case Specification |
| 8   | Runway Instructions cards          | Test Procedure Specification   |
| 16  | Wardrobe Malfunction cards         | Defect Report                  |
| 12  | Event / Action cards               | Test environment / risks       |
| 4   | Studio Mat (player board)          | Workspace                      |
| 1   | Six-sided die                      | Execution randomiser           |
| 4   | Rehearsal Summary pads (paper)     | Test Status Report             |
| 1   | Quick Reference card               | —                              |

## 3. Setup (≈ 2 minutes)

1. Each player takes a **Studio Mat**. The mat has 5 zones, top to bottom:
   `Brand Identity` → `Runway Roadmap` → `Collection Theme` → `Outfit Slots ×3` → `Procedure / Runway`.
2. Shuffle each deck separately and place face-down within reach.
3. Each player draws **1 Brand Identity** card and places it face-up in the top zone of their mat. Read it aloud.
4. Each player draws a starting hand of **5 Outfit Detail cards** + **1 Collection Theme** + **1 Runway Roadmap**.
5. Place the Wardrobe Malfunction deck and Event deck in the centre of the table, face-down.
6. Pick a starting player (the most recent person to wear something patterned). Play passes clockwise.

## 4. Turn structure

A round consists of every player taking **one turn**. Each turn has **5 phases, in this order**. Skipping a phase is illegal — that is the structural gate that teaches the hierarchy.

### Phase 1 — Plan (Project Test Plan)

- If you do not have a Runway Roadmap on your mat, place one from your hand now.
- The Roadmap states a **Scope** (e.g., "≤ 4 outfits this round"), a **Schedule** (turn limit), and a **Resource cap** (e.g., "≤ 1 accessory per outfit").
- These constraints apply to every Outfit you play this round. **If your Outfits violate them, you have already accumulated a latent defect** — opponents can flag it during inspection.

### Phase 2 — Design (Test Design Specification)

- Place a Collection Theme card on top of your Roadmap. The Theme groups your outfits under a shared **Test Condition** (e.g., "all outfits must read as evening-wear").
- A Theme without a Roadmap is illegal — the Roadmap defines what Themes are even allowed.

### Phase 3 — Specify (Test Case Specification)

- Play **at least 3 Outfit Detail cards** into your Outfit Slots.
- Each Outfit must satisfy the active Brand Identity, Runway Roadmap and Collection Theme. Reading the card aloud and checking it against the three layers above is the **Specification Review**.
- Half of the Outfit deck contains **planted flaws** — a missing Expected Result, a contradictory Pre-condition, an Outfit that breaks the Brand Identity, etc. You may keep flawed Outfits in hand. Playing one is risky but legal.

### Phase 4 — Procedure (Test Procedure Specification)

- Decide the **order** in which your Outfits will walk. Place a Runway Instructions card to the right of your Outfits.
- The Procedure card declares the sequence and any inter-outfit dependencies (e.g., "Outfit 2 only walks after Outfit 1 is on the catwalk").

### Phase 5 — Rehearsal (Test Execution + Defect Reporting)

This is the **mistake-reveal phase**. Run it in this exact sub-order:

1. **Read-aloud.** The active player reads each Outfit's Pre-conditions and Expected Result aloud.
2. **Inspection (60 seconds).** Opponents may call out a flaw they spot. Anyone who correctly identifies a planted flaw scores **+2 Inspection Points** and the active player must Revise (see §6) **before** rolling.
3. **Execution roll.** The active player rolls the d6 once per Outfit:
   - **1–2:** Failure. Draw a Wardrobe Malfunction card. Resolve via Traceability (§5).
   - **3–6:** The Outfit walks. **However**, if the Outfit had an unflagged planted flaw, treat the roll as a 1 regardless of the number rolled. (See `04_GameLogic/Mistake_Reveal_Engine.md` for why.)
4. **Score.** +3 points per Outfit that walked cleanly. +1 bonus if the Procedure card declared an inter-outfit dependency that actually held.

After every player has rehearsed, fill in your **Rehearsal Summary** pad (1 line per Outfit: ID / Pass / Fail / Originating Doc Field). The round ends.

## 5. Traceability — resolving a Wardrobe Malfunction

When you draw a Malfunction card, it **names the ISO doc field that caused the failure**, e.g.:

> **WM-07 — "Heel snapped on the runway"**
> Originating field: *Pre-conditions* on the Outfit Detail card.

To resolve:

1. Find the doc on your mat whose named field is at fault.
2. **Read aloud what is wrong** — e.g., "My Pre-condition said size 38 but the Outfit specified a size-36 corset." This sentence is what you score on.
3. Discard the faulty Outfit (or, if the malfunction names the Roadmap or Brand Identity, all Outfits under it) and lose 2 points.
4. If you cannot identify the originating field within 30 seconds, you lose 4 points and the malfunction stays on your mat as a **Carry-Over Defect** for the next round.

**This is the heart of the educational design.** A defect is never "bad luck" — it always points back to a real document field, which the player must name.

## 6. Revision

A Revision is a mid-turn correction: you discard a flawed card and replace it from your hand or the deck. A Revision costs you 1 point but is almost always cheaper than a Malfunction.

## 7. Event cards

At the start of every player's turn, draw and resolve 1 Event card from the centre. Events represent ISO 29119-3 environment / risk factors:

- Resource cuts ("Budget reduced — discard 1 accessory from your Roadmap.")
- Schedule pressure ("This round you have 2 minutes total.")
- Auditor visit ("Reveal your Brand Identity card to all players and re-read it aloud.")

## 8. End of game and scoring

- A standard prototype game lasts **2 rounds** (≈ 10–12 min). Tournament play is 4 rounds.
- At the end, total each player's score:

| Source                                     | Points         |
|--------------------------------------------|----------------|
| Outfit walks cleanly                       | +3 per outfit  |
| Procedure dependency held                  | +1 per case    |
| Correctly named originating doc field      | +2 per defect  |
| Inspection Point (you flagged a rival flaw)| +2 per flag    |
| Revision used                              | −1 per use     |
| Wardrobe Malfunction unresolved            | −4 per case    |
| Played a card out of hierarchy             | −2 per attempt |

Highest score wins. Ties are broken by **fewest unresolved defects** — the test lead with the cleanest paper trail wins, not the one with the prettiest clothes.

## 9. The 'Lite' variant (10-minute classroom demo)

For the Week 3 in-class demo, use this trim:
- 1 round only.
- 3 Outfits per player (no more, no less).
- Skip Event cards.
- Skip Runway Instructions (procedure phase merges into Specify).

The Lite variant still preserves the full hierarchy and the full mistake-reveal mechanic. It just shortens the loop.

## 10. Win condition phrased in ISO terms

> The player whose **test documentation set most accurately predicts execution outcomes** wins. Not the player with the most outfits. Not the luckiest dice roll. The one whose paper trail held up under inspection and execution.

---

*See `QuickReference.md` for the 1-page table version of this rulebook.*
