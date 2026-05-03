# What to Print — Week 3 In-Class Demo

Open each `.html` file below in a browser (Safari / Chrome), then **File → Print** with these settings:
- Paper: **A4**
- Scale: **100% (no shrink-to-fit)**
- Margins: **Default**
- Headers/Footers: **OFF**
- Background graphics: **ON** (so the colored deck headers print)

| File | Pages | Copies | Who gets it |
|---|---|---|---|
| `AllCards.html` | 11 (9 cards each) | 1 | Cut into 96 cards. The deck. |
| `StudioMat.html` | 1 (A4 landscape) | 4 | One per player |
| `PlaytesterHandout.html` | 2 | 1 per playtester (≈ 4) | Hand out at start of session |
| `ModeratorPacket.html` | ~5 | 1 | SunShine team member running the table — keep private |

Total: ~19 A4 pages.

## After printing AllCards.html

1. Cut along card edges (paper trimmer recommended — straight edges matter).
2. Sleeve in standard poker-size sleeves (63 × 88 mm) — optional but extends life.
3. Sort into 7 stacks by deck (header colour makes this trivial):
   - BRAND IDENTITY: 8 cards
   - RUNWAY ROADMAP: 12 cards
   - COLLECTION THEME: 10 cards
   - OUTFIT DETAIL: 30 cards
   - RUNWAY INSTRUCTIONS: 8 cards
   - WARDROBE MALFUNCTION: 16 cards
   - EVENT / ACTION: 12 cards
4. Place each stack in its own ziplock or with a paper clip, labelled with the deck code.

## What to bring on demo day

- The 96-card deck, sorted into 7 stacks
- 4 printed Studio Mats
- 4–6 Playtester Handouts + pens
- 1 Moderator Packet (your copy only)
- 1 d6 die
- 1 phone timer (for the 60-second Inspection)

## Build time

Print + cut + sleeve + sort = **~90 minutes** for a 3-person team (30 min each).

## Regenerating after card edits

If you change the markdown in `../02_Cards/`, re-run:

```bash
python3 build_prototype.py
```

That's it — the HTML rebuilds from the markdown source of truth.
