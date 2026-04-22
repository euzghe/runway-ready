# ISO/IEC 29119-3 Terminology Map

This map is the **source of truth** for terminology in *Runway Ready*. Every card, rule, and feedback prompt in this prototype refers back to a row in this table. If a playtester ever asks "what does this card *really* mean?", the answer lives here.

## 1. Document hierarchy (per ISO/IEC 29119-3, Clauses 5–7)

| Layer            | ISO/IEC 29119-3 Document            | Runway Ready Card        | ISO Field Set Preserved on Card                                              |
|------------------|-------------------------------------|--------------------------|------------------------------------------------------------------------------|
| Organizational   | Organizational Test Strategy        | **Brand Identity**       | Test policy reference, scope of applicability, generic risks, global rules   |
| Project          | Project Test Plan                   | **Runway Roadmap**       | Scope, references, schedule, resourcing, risks, approach                     |
| Process — design | Test Design Specification           | **Collection Theme**     | Feature set ID, test conditions, traceability to requirements                |
| Process — case   | Test Case Specification             | **Outfit Detail**        | ID, objective, pre-conditions, inputs, expected results, post-conditions     |
| Process — proc.  | Test Procedure Specification        | **Runway Instructions**  | Procedure ID, ordered steps, dependencies, resumption requirements           |
| Execution        | Test Execution (activity, not doc)  | *Rehearsal Phase* (mech.)| —                                                                            |
| Reporting        | Defect Report (Incident Report)     | **Wardrobe Malfunction** | Defect ID, severity, description, status, impact, **originating doc field**  |
| Reporting        | Test Status / Completion Report     | **Rehearsal Summary**    | Run summary, pass/fail counts, outstanding defects, completion criteria      |

**Note for Criterion 1 (Concept Accuracy):** the bracketed phrasing on every card preserves the ISO field name in italics, e.g. `Pre-conditions:` on an Outfit Detail card is the ISO 29119-3 field, not just a fashion flavour line.

## 2. Activity-to-mechanic map

| ISO Activity            | Card / mechanic that performs it                            |
|-------------------------|-------------------------------------------------------------|
| Plan testing            | Place a Runway Roadmap on your studio mat                   |
| Design test conditions  | Place a Collection Theme on top of the Roadmap              |
| Specify test cases      | Draft / draw Outfit Detail cards under the active Theme     |
| Specify procedures      | Order your Outfits and add a Runway Instructions card       |
| Execute tests           | Rehearsal Phase: read aloud → opponent inspection → dice    |
| Report defects          | Resolve a Wardrobe Malfunction by naming the originating field|
| Report status           | End-of-round Rehearsal Summary card                         |

## 3. Documentation dependency rules (enforced by the game)

These dependencies come **directly** from ISO/IEC 29119-3 §5–7 and are enforced as **structural gates** in the rules. A player who attempts an action out of order is reminded of the rule and the action is undone — this is the point at which the misconception "I can just write a test case" becomes visible.

```
Brand Identity (mandatory, 1 active)
    └── enables → Runway Roadmap (mandatory, 1 active per round)
              └── enables → Collection Theme (≥1 per Roadmap)
                        └── enables → Outfit Detail (≥3 per Theme to send to runway)
                                  └── enables → Runway Instructions (1 per show)
                                            └── enables → Rehearsal Phase
                                                      └── may produce → Wardrobe Malfunction
                                                                    └── traced to → an originating field in any of the above
```

## 4. Misconceptions this map directly attacks

| Misconception (from Week 1, §5)                          | How the table above contradicts it                                  |
|----------------------------------------------------------|---------------------------------------------------------------------|
| "Test cases are just input → output pairs."              | Outfit Detail card has 6 ISO fields; missing any one blocks play.   |
| "Documentation is unnecessary in Agile."                 | Even the 'Lite' tournament variant requires Roadmap + 3 Outfits.    |
| "Documentation is only for big projects."                | The 10-minute prototype is small AND requires the full hierarchy.   |
| "A defect is a random unlucky event."                    | Every Malfunction card names the doc field that caused it.          |
| "Strategy and Plan are the same thing."                  | Brand Identity = global rule; Roadmap = round-specific scope.       |
