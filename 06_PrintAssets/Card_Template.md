# Physical Card Template (Print-Ready Spec)

## Standard card dimensions

- **Size:** 63 mm × 88 mm (standard poker card — fits commercial sleeves).
- **Bleed:** 3 mm on every side (final cut size 69 mm × 94 mm).
- **Print resolution:** 300 dpi minimum.
- **Paper:** 300 gsm cardstock, matte finish to keep ink legible under classroom lighting.

## Common card layout (front face)

```
┌──────────────────────────────────────┐  ← 88 mm tall
│  ╔════════════════════════════════╗  │
│  ║ [DECK ICON]   ID: <CARD-ID>   ║  │  ← 8 mm header strip
│  ║ <CARD TYPE>                    ║  │     (deck colour-coded)
│  ╚════════════════════════════════╝  │
│                                      │
│  <CARD TITLE — large bold>           │  ← 6 mm title
│                                      │
│  ─────────────────────────────────   │
│                                      │
│  *<ISO field name>:* <content>       │
│  *<ISO field name>:* <content>       │  ← body — ALL ISO field names
│  *<ISO field name>:* <content>       │     in italics, mandatory
│  *<ISO field name>:* <content>       │
│  *<ISO field name>:* <content>       │
│                                      │
│  ─────────────────────────────────   │
│                                      │
│  <Flavour line — fashion analogy>    │  ← 1 line max (flavour, optional)
│                                      │
│  ╔════════════════════════════════╗  │
│  ║ Maps to: <ISO/IEC 29119-3 doc> ║  │  ← 8 mm footer (always present)
│  ╚════════════════════════════════╝  │
└──────────────────────────────────────┘  ← 63 mm wide
```

## Deck colour palette

A consistent colour code lets a glance at the table tell you what document hierarchy each card represents.

| Deck                        | Header colour     | Hex      | Rationale                                     |
|-----------------------------|-------------------|----------|-----------------------------------------------|
| Brand Identity              | Magenta           | `#D81E5B`| Highest layer; brand is loud                  |
| Runway Roadmap              | Indigo            | `#3B3F8F`| Project planning is structural / blueprint    |
| Collection Theme            | Sage green        | `#6FAE6E`| Design / creative growth layer                |
| Outfit Detail               | Lavender          | `#9D8BD9`| Atomic, individual                             |
| Runway Instructions         | Slate             | `#5F6B7A`| Procedural, mechanical                        |
| Wardrobe Malfunction        | Crimson           | `#C0392B`| Defect / alarm                                 |
| Event / Action              | Goldenrod         | `#E0A823`| Risk / environment                             |

## Back face (optional — recommended for print)

A single back-face design per deck, showing only the deck icon and the 29119-3 layer name. Keeps shuffling and dealing fast.

## Outfit Detail card — special note for the FLAWED variant

The flawed cards (OD-F-01 … OD-F-15) **must look identical to the clean cards**. No watermark, no asterisk, no "FLAWED" label visible to the player. The whole point of the Inspection mechanic is that flaws are caught by *reading*, not by spotting a visual marker.

The **Answer Key** lives separately in the moderator's notes (see `02_Cards/04_Outfit_Detail_Cards.md`, "Answer Key — Originating Field" lines).

## Sample — printable text for OD-C-01

```
┌──────────────────────────────────────┐
│  ╔════════════════════════════════╗  │
│  ║ [👗] ID: SS26-001              ║  │
│  ║  OUTFIT DETAIL                  ║  │
│  ╚════════════════════════════════╝  │
│                                      │
│  Mediterranean Breeze — Opener       │
│                                      │
│  ─────────────────────────────────   │
│  *Identifier:* SS26-001              │
│  *Objective:* Showcase the opening   │
│    look of the Mediterranean Breeze  │
│    theme.                            │
│  *Pre-conditions:* Model size 38;    │
│    sandals fitted; hair in low       │
│    chignon.                          │
│  *Inputs:* Linen slip dress, off-    │
│    white; raffia belt; gold hoops.   │
│  *Expected Result:* Model walks 12   │
│    steps without tripping; dress     │
│    drapes evenly at hip.             │
│  *Post-conditions:* Returned         │
│    undamaged.                        │
│  *Traceability:* REQ-FASHION-MB-01   │
│  ─────────────────────────────────   │
│  An outfit is a test case.           │
│  ╔════════════════════════════════╗  │
│  ║ Maps to: Test Case Specification║  │
│  ╚════════════════════════════════╝  │
└──────────────────────────────────────┘
```
