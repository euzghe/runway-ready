# Traceability Logic

This is the formal rule for resolving a Wardrobe Malfunction. It is the single most important game mechanic for satisfying the brief's "reveals mistakes" requirement.

## The traceability rule, formally

When a Wardrobe Malfunction card is drawn:

```
1. Read the Originating Field line on the Malfunction card.
   e.g.,  "Originating field: Pre-conditions"

2. Locate every card on your mat that contains a field of that name.
   (Possible owners: Brand Identity, Roadmap, Theme, Outfit, Procedure)

3. Identify which specific instance of that field caused the failure.
   This requires explaining the inconsistency.

4. Verbalise the inconsistency, in the form:
       "On <Card Name>, the field <Field Name> said <X>,
        but <Y> on <Other Card> required <Z>.
        That mismatch is why the Outfit failed."

5. Once verbalised correctly:
   - Discard the faulty Outfit (or, for Brand-Identity-rooted defects,
     all Outfits under it that round)
   - Lose 2 points
   - Score +2 for "Named originating doc field correctly"

6. If you cannot verbalise within 30 seconds:
   - Lose 4 points
   - The Malfunction stays on your mat as a Carry-Over Defect
   - Carry-Over Defects accumulate −1 point per round until resolved
```

## Why verbalisation matters

The educational design depends on the player **producing the explanation**, not just acknowledging the defect. Consider the difference:

| Weak resolution                                              | Strong resolution (what this game requires)                                                                |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| "Yeah, my outfit failed."                                     | "On Outfit SS26-101, the Expected Result field was blank, so the rehearsal could not declare pass or fail." |
| "I got unlucky."                                              | "On Outfit AW26-101, my Pre-condition said size 36 but my Inputs listed a size-40 blazer. The size-mismatch is the defect." |
| "The dice screwed me."                                        | "The dice rolled a 4, but my Outfit had an unflagged planted flaw, so it failed. The flaw was the self-referential Expected Result." |

## Traceability matrix (which field can produce which Malfunction)

| Originating field        | Possible owner cards                            | Example Malfunction cards |
|--------------------------|-------------------------------------------------|---------------------------|
| Identifier               | Outfit Detail                                   | WM-09                     |
| Objective                | Outfit Detail                                   | WM-10                     |
| Pre-conditions           | Outfit Detail                                   | WM-01, WM-06, WM-13       |
| Inputs                   | Outfit Detail                                   | WM-02, WM-04, WM-11       |
| Expected Result          | Outfit Detail                                   | WM-07                     |
| Post-conditions          | Outfit Detail                                   | WM-03, WM-12              |
| Traceability ID          | Outfit Detail                                   | WM-08                     |
| Coverage criteria        | Collection Theme                                | WM-14                     |
| Resources                | Runway Roadmap                                  | WM-13                     |
| Scope                    | Runway Roadmap                                  | WM-10                     |
| Ordered steps            | Runway Instructions                             | WM-05                     |
| Dependencies             | Runway Instructions                             | WM-15                     |
| Global rule              | Brand Identity                                  | WM-16, WM-04              |

## Why this matrix is the actual learning artefact

After playing the game, a learner has *physically handled* every row in this table. They have seen, with their own hands, that:

- A defect can originate at **any layer** of the documentation hierarchy.
- A high-layer defect (Brand Identity) **cascades** down: WM-16 invalidates an entire Outfit set, not just one card.
- A low-layer defect (Identifier collision) is **localised**: WM-09 only invalidates one Outfit.
- The originating field is **always nameable** — there is no "magic failure" in this game.

This is the practical, hands-on equivalent of an ISO/IEC 29119-3 traceability matrix.
