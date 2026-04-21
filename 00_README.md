# Runway Ready — Week 3 Playable Prototype

**Group:** SunShine
**Standard:** ISO/IEC 29119-3 (Test Documentation)
**Format:** Physical Card Game (3–4 players, 10–15 min)
**Status:** Week 3 Deliverable — Prototype Version 1

---

## What this folder contains

This folder is the **complete, testable Version 1** of *Runway Ready*. It is designed so that another group can sit down, print the cards, read the Quick Reference, and play within 5 minutes of opening the box.

```
Runway-Ready-Week3/
├── 00_README.md                 ← you are here
├── 01_Rulebook/                 Full rules + 1-page quick reference + ISO glossary
├── 02_Cards/                    All printable card content (organized by deck)
├── 03_GameBoard/                Tabletop layout / play zones
├── 04_GameLogic/                Turn flow, traceability logic, mistake-reveal engine, scoring
├── 05_Playtesting/              10-min playtest script + structured feedback form
└── 06_PrintAssets/              Physical card template + print-and-cut guide
```

## Reading order (for the playtester)

1. `01_Rulebook/QuickReference.md` — 1 page, get the gist
2. `04_GameLogic/Turn_Flow_Diagram.md` — see the loop
3. `01_Rulebook/Rulebook.md` — full rules when something is unclear
4. `05_Playtesting/Playtest_Script.md` — guided 10-minute first session

## Reading order (for the instructor / grader)

1. `00_README.md` (this file)
2. `04_GameLogic/Mistake_Reveal_Engine.md` — **how the game makes misconceptions visible** (Criterion 3)
3. `01_Rulebook/ISO_Terminology_Map.md` — **terminology accuracy** (Criterion 1)
4. `05_Playtesting/Learning_Outcome_Checklist.md` — **measurable objectives → mechanics** (Criterion 2)
5. `01_Rulebook/Rulebook.md` — **playability and structured flow** (Criterion 4)

## Design north star

> **The game does not punish bad luck. It punishes bad documentation.**

Every defect in *Runway Ready* is **traceable to a specific field in a specific document the player wrote, drew, or accepted**. There are no random failures. If a Wardrobe Malfunction triggers, a real, named flaw exists somewhere on the table — and the player must find it before they can re-execute. This is the operational meaning of "reveals mistakes" for our prototype.

## Mapping summary (full version in `01_Rulebook/ISO_Terminology_Map.md`)

| ISO/IEC 29119-3 Document       | Game Card               | Function in play              |
|--------------------------------|-------------------------|-------------------------------|
| Organizational Test Strategy   | Brand Identity Card     | Sets global constraints       |
| Project Test Plan              | Runway Roadmap Card     | Unlocks specification phase   |
| Test Design Specification      | Collection Theme Card   | Groups related test cases     |
| Test Case Specification        | Outfit Detail Card      | Individual testable unit      |
| Test Procedure Specification   | Runway Instructions     | Execution sequence            |
| Test Execution                 | Rehearsal Phase (mech.) | Resolve unit on the runway    |
| Defect Report                  | Wardrobe Malfunction    | Names the failed doc field    |
| Test Status Report             | Rehearsal Summary       | End-of-show traceability log  |
