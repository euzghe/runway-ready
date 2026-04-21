# Runway Ready

> **A 10-minute card game that teaches ISO/IEC 29119-3 Test Documentation by running a fashion house.**
> The dice cannot save bad documentation — only paper trails that survive Inspection win the runway.

**[▶ Play in your browser](https://euzghe.github.io/runway-ready/)** · Group **SunShine** · ISO/IEC 29119-3 (Test Documentation) · Week 3 Prototype

---

## Team

| Member | GitHub | Role on this project |
|---|---|---|
| Bilge Küçükçakmak | [@bilgekucukcakmak](https://github.com/bilgekucukcakmak) | ISO concept analysis, terminology mapping, card content authoring |
| Nisa Konur | [@niisakonur](https://github.com/niisakonur) | Game rules, mechanics, mistake-reveal engine, scoring system |
| Özge Altınok | [@euzghe](https://github.com/euzghe) | Playtest kit, web prototype implementation, deployment |

## What this is

The brief asked us to teach an abstract international standard (ISO/IEC 29119-3 Test Documentation) by **designing a game** that someone else can learn it from. Our central design idea:

> The game does not punish bad luck. It punishes **bad documentation**.

Every defect in *Runway Ready* is traceable to a specific ISO field on a specific card the player wrote, drew, or accepted. There are no random failures. If a runway show goes wrong, a real, named flaw exists somewhere on the table — and the player must find it before they can re-execute. That is the operational meaning of the brief's "reveals mistakes" requirement.

## Two ways to play

### 1. Browser (recommended for the demo)
Open [the live site](https://euzghe.github.io/runway-ready/) or, locally, double-click `web/index.html`. No install, no internet, no setup. 3–4 players gather around one screen.

### 2. Physical card game
Print everything in `02_Cards/` using the templates in `06_PrintAssets/` and the `PrintReady/build_prototype.py` script. Roughly 90 minutes to print + cut + sleeve.

Both versions implement the same rules and the same educational design.

## Repository layout

```
.
├── 00_README.md                       Prototype index (for the playtester)
├── 01_Rulebook/                       Full rules, 1-page quick reference, ISO terminology map
├── 02_Cards/                          7 card decks: Brand Identity, Roadmap, Theme, Outfit, etc.
├── 03_GameBoard/                      Studio mat layout
├── 04_GameLogic/                      Turn flow, mistake-reveal engine, traceability, scoring
├── 05_Playtesting/                    10-minute playtest script, feedback form, learning outcome checklist
├── 06_PrintAssets/                    Card template + print-and-cut guide
├── PrintReady/                        Generated print-ready HTML (run build_prototype.py)
├── web/                               Single-file browser game (deployed via GitHub Pages)
└── README.md                          this file
```

## How the educational design maps to the grading criteria

| Brief criterion | Where to look |
|---|---|
| 1. Concept Accuracy (20 pts) | `01_Rulebook/ISO_Terminology_Map.md` — every card carries its ISO field name |
| 2. Learning Objectives (15 pts) | `05_Playtesting/Learning_Outcome_Checklist.md` — 5 measurable objectives mapped to mechanics |
| 3. Educational Effectiveness (20 pts) | `04_GameLogic/Mistake_Reveal_Engine.md` — five mechanisms that make misconceptions visible |
| 4. Prototype Quality (35 pts) | `01_Rulebook/Rulebook.md` + `web/index.html` — fully playable in 10 minutes |
| 5. Reflection & Team Understanding (10 pts) | The Rehearsal Summary tables produced at game end |

## License

MIT — see `LICENSE`.
