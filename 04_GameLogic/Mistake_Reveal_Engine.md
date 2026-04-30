# The Mistake Reveal Engine

> This document explains *operationally* how *Runway Ready* satisfies the project brief's
> "Educational Effectiveness" criterion: **misconceptions become visible**.

## 1. Definition of "visible"

A misconception is **visible** in this game when:

1. The player produces a card play that physically embodies the misconception, **and**
2. Some game-state mechanism (an opponent, a card text, a roll outcome, or the post-round summary) **forces the misconception to be named out loud and pointed at**.

Mere "you lost a point" is not visibility. Visibility requires verbalisation.

## 2. The four misconception classes this game targets

Drawn from Week 1 §5 and from common 29119-3 teaching observations:

| # | Misconception                                                         | Visibility mechanism                                       |
|---|-----------------------------------------------------------------------|------------------------------------------------------------|
| M1| "Test cases are simple input → output pairs."                         | Outfit Detail card has 7 ISO fields; flaw deck includes missing-field, ambiguous-field, untestable-field variants. Each forces the player to name *which field* is wrong. |
| M2| "Documentation is unnecessary / can be skipped."                      | Structural gating: any phase skip is a −2 hierarchy violation **and** is undone publicly at the table. |
| M3| "A defect is a random unlucky event."                                 | Every Wardrobe Malfunction names its originating ISO field. There is no card titled "just bad luck". |
| M4| "Strategy and Plan are the same thing."                               | Brand Identity is global and persistent across rounds; Roadmap is round-scoped. Different cards, different zones, different rule scope. The 'Lite' variant still requires both. |

## 3. The five reveal mechanisms

The game uses five mechanisms, applied at different points in the turn:

### Mechanism 1 — Structural Gating (constant)

Every phase requires a card from the layer above to be present. Trying to play an Outfit without a Theme is *physically blocked* at the table — opponents will point and the rules require the play to be undone with a −2 penalty. **This makes M2 visible at the moment of attempted skip.**

### Mechanism 2 — Read-Aloud (every Rehearsal)

Before any dice are rolled, the active player must **read aloud** every Outfit's Pre-conditions and Expected Result. The act of reading often surfaces the player's own flaw to themselves before opponents see it. (We observed in informal tests that ~30 % of self-caught flaws come from the read-aloud alone.)

### Mechanism 3 — Inspection (60-second rival-spotting)

Opponents have 60 seconds to point at and **name** a flaw. They earn +2 Inspection Points per correct call. This converts every player into a peer reviewer for every other player. Crucially, the call must include the **field name** (e.g., "Pre-conditions"), not just "this looks wrong" — that converts the reveal from intuition to formal articulation. **Primary mechanism for M1 and M3 visibility.**

### Mechanism 4 — Deterministic Failure for Unflagged Flaws

This is the design's unusual move. The d6 roll is *not* the source of truth. If an Outfit has an unflagged planted flaw, **the roll is treated as a 1 regardless of the actual face**. This guarantees:

- A flaw that escapes Inspection still reveals itself at execution.
- Players cannot hide behind "I got lucky".
- The defect that follows always points to a real, named field — not chance.

In other words: **the dice can hurt good documentation (a 1–2 roll on a clean Outfit), but they cannot save bad documentation**. This asymmetry is intentional. Real testing has the same property: a flaky test can fail a working build, but a passing test cannot vindicate broken code that was never exercised.

### Mechanism 5 — Post-Round Rehearsal Summary

At round-end, every player fills a Rehearsal Summary pad with one line per Outfit:

```
Outfit ID | Pass / Fail | Originating Doc Field (if Fail)
SS26-001  |    Pass     |  —
SS26-101  |    Fail     |  Expected Result (blank)
SS26-104  |    Fail     |  Objective (out of scope of Theme)
```

This pad is the test status report. Reviewing it after the round forces the player to **see the pattern** — e.g., "I lost three rounds to Expected Result issues; my problem is non-falsifiable expected outcomes". **Primary mechanism for M4 visibility** (and for instructor-led debrief).

## 4. What is *not* in this game (and why)

We deliberately excluded several features that would have undermined visibility:

- **No "draw a random misfortune" cards.** Every negative outcome is traceable to a doc field.
- **No private rolls.** All execution rolls are public.
- **No "skip a phase for a cost" option.** The hierarchy is non-negotiable; that is the lesson.
- **No win-by-most-outfits.** That would reward volume over rigour.

## 5. Mapping to the grading criteria

| Grading criterion (Brief)                                    | Engine mechanism                                              |
|--------------------------------------------------------------|---------------------------------------------------------------|
| 1. Concept Accuracy (20)                                      | Every card carries the ISO field name in italics; ISO_Terminology_Map.md is the source of truth. |
| 2. Learning Objectives (15)                                   | Each of the 4 stated learning objectives maps to a specific mechanism — see `Learning_Outcome_Checklist.md`. |
| 3. Educational Effectiveness (20) — *misconceptions visible* | This document, sections 2–3, describes 5 mechanisms across 4 misconception classes. |
| 4. Prototype Quality (35) — *fully playable, clear rules*    | Rulebook + QuickReference + 10-min Lite variant + Playtest Script. |
| 5. Reflection (10)                                            | Rehearsal Summary pads are the structured artefact players walk away with. |
