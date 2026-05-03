# Print-and-Cut Guide (Build a Physical Prototype in 90 Minutes)

> Use this guide to physically build the Week 3 prototype. Total cost: ≈ ₺ 80 (paper + sleeves + 1 die).

## Materials checklist

| Item                              | Qty       | Notes                                                  |
|-----------------------------------|-----------|--------------------------------------------------------|
| A4 cardstock 300 gsm matte        | 12 sheets | Each A4 holds 9 cards (3×3). 96 cards → 11 sheets + 1 spare. |
| Standard A4 paper 80 gsm          | 4 sheets  | For Studio Mats and Rehearsal Summary pads.            |
| Card sleeves (poker size)         | 100       | Optional but recommended for repeated playtesting.     |
| 1× d6 die                         | 1         | Any standard 6-sided die.                               |
| Paper trimmer or scissors         | 1         | Trimmer is faster and gives straight edges.             |
| Permanent fine-tip marker         | 1         | Black, for handwritten corrections only.                |

## Step 1 — Generate printable PDFs

For each deck file in `02_Cards/`:

1. Open the markdown file in a markdown-to-PDF converter (e.g., VSCode + "Markdown PDF", or a quick script using `pandoc`).
2. Apply the layout from `06_PrintAssets/Card_Template.md`.
3. Use the deck colour palette for the header strip (one consistent colour per deck — see template).
4. Export as A4, 3×3 cards per page, with 3 mm bleed and crop marks.

If you do not have time for full formatting, a **plain-text print** of each card (one card per slip, hand-cut) is acceptable for the in-class demo. The educational mechanics do not depend on visual polish — they depend on the ISO field labels being legible.

## Step 2 — Print

| File                                          | Pages (A4, 9-up) |
|-----------------------------------------------|------------------|
| `01_Brand_Identity_Cards.md` (8 cards)        | 1                |
| `02_Runway_Roadmap_Cards.md` (12 cards)       | 2                |
| `03_Collection_Theme_Cards.md` (10 cards)     | 2                |
| `04_Outfit_Detail_Cards.md` (30 cards)        | 4                |
| `05_Runway_Instructions_Cards.md` (8 cards)   | 1                |
| `06_Wardrobe_Malfunction_Cards.md` (16 cards) | 2                |
| `07_Event_Cards.md` (12 cards)                | 2                |
| **Total**                                     | **14 sheets**    |

Plus:
- 4× Studio Mat (1 page each, A4 landscape) — see `03_GameBoard/Board_Layout.md`.
- 4× Rehearsal Summary pad (printed grid on A4).
- 1× Quick Reference card (1 page) — see `01_Rulebook/QuickReference.md`.

## Step 3 — Cut

- Use a paper trimmer for straight edges. Cut along the crop marks.
- A 9-up A4 sheet of poker-size cards yields 9 cards per sheet with negligible offcut.

## Step 4 — Sleeve (optional but recommended)

- Sliding the printed cards into clear poker sleeves makes them last across multiple playtests and lets you mark them temporarily with a dry-erase marker if you discover a typo mid-session.

## Step 5 — Sort and label decks

Bind each deck with a small clip or place in a small ziplock. Label:

- **B.I.** Brand Identity (8)
- **R.R.** Runway Roadmap (12)
- **C.T.** Collection Theme (10)
- **O.D.** Outfit Detail (30) — *includes 15 flawed cards, do NOT separate*
- **R.I.** Runway Instructions (8)
- **W.M.** Wardrobe Malfunction (16)
- **EV.** Event (12)

## Step 6 — Print the moderator's Answer Key

A single A4 sheet listing the 15 flawed Outfit IDs and their planted defects (lifted from the "Answer Key — Originating Field" lines in `02_Cards/04_Outfit_Detail_Cards.md`). **This sheet stays with the moderator only**.

## Step 7 — Time-budget for build

| Task                                | Time   |
|-------------------------------------|--------|
| Generate PDFs                       | 20 min |
| Print 14 sheets + mats + reference   | 15 min |
| Cut to size                         | 25 min |
| Sleeve                              | 20 min |
| Sort, label, package                | 10 min |
| **Total**                           | **90 min** |

A 3-person team can split this into 30 min each.
