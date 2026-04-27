# Deck 5 — Runway Instructions Cards (×8)

**ISO/IEC 29119-3 mapping:** Test Procedure Specification
**ISO fields preserved on every card:** *Procedure ID · Ordered steps · Dependencies · Resumption requirements*
**Function in play:** Declares the order in which Outfits walk and the inter-outfit dependencies. A correctly-honoured dependency is worth +1 bonus point at scoring.

---

## RI-01 — "Linear Walk"

- *Procedure ID:* RI-01
- *Ordered steps:* Outfit 1 → Outfit 2 → Outfit 3, single file, 8 sec gap.
- *Dependencies:* None.
- *Resumption requirements:* Restart from Outfit 1 if interrupted.

## RI-02 — "Crescendo"

- *Procedure ID:* RI-02
- *Ordered steps:* Lowest-impact Outfit → mid → signature piece last.
- *Dependencies:* The signature piece may only walk after at least 2 prior Outfits walked cleanly.
- *Resumption requirements:* If signature piece fails, do not retry — discard.

## RI-03 — "Paired Walk"

- *Procedure ID:* RI-03
- *Ordered steps:* Outfits 1+2 walk together, then Outfit 3 solo, then Outfits 4+5 together.
- *Dependencies:* Paired Outfits must share the same active Theme.
- *Resumption requirements:* If a pair fails, both fail.

## RI-04 — "Mirror Sequence"

- *Procedure ID:* RI-04
- *Ordered steps:* Outfit 1 walks, returns, then Outfit 2 walks the reverse path.
- *Dependencies:* Outfit 2's Pre-conditions must mirror Outfit 1's (same model size).
- *Resumption requirements:* If mirror condition broken, restart from Outfit 1.

## RI-05 — "Static Pose"

- *Procedure ID:* RI-05
- *Ordered steps:* Each Outfit holds a 5-sec pose at the runway midpoint before continuing.
- *Dependencies:* Pose duration depends on Outfit's structure — sculptural Outfits hold 8 sec.
- *Resumption requirements:* Pose failure → restart that Outfit only.

## RI-06 — "Press-Friendly Loop"

- *Procedure ID:* RI-06
- *Ordered steps:* Each Outfit walks, pauses 3 sec at photographer pit, then continues.
- *Dependencies:* Each Outfit must have a unique selling point declared.
- *Resumption requirements:* No restart — press already photographed.

## RI-07 — "Interleaved Themes"

- *Procedure ID:* RI-07
- *Ordered steps:* Alternate between Themes (A, B, A, B, A).
- *Dependencies:* Requires at least 2 active Themes on the mat.
- *Resumption requirements:* Restart from the start of the failed Theme's segment.

## RI-08 — "Finale Burst"

- *Procedure ID:* RI-08
- *Ordered steps:* All Outfits walk simultaneously for the closing tableau.
- *Dependencies:* All Outfits must have non-overlapping spatial Pre-conditions.
- *Resumption requirements:* No retry — tableau only happens once.

---

## Why these matter (educational intent)

A Test Procedure Specification is the document that turns isolated test cases into a **runnable test execution plan**. By making Procedure cards declare both order and dependencies, the game teaches that procedures are not just "the order you do things in" — they are formal artefacts that constrain valid execution and define resumption behaviour after failure.
