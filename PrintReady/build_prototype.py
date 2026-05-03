#!/usr/bin/env python3
"""
Runway Ready — Print-Ready Prototype Builder
=============================================
Reads the card markdown files in ../02_Cards/ and the rulebook materials in
../01_Rulebook/ + ../05_Playtesting/ and produces print-ready HTML you can open
in any browser and "File > Print" (or Save as PDF) onto A4 paper.

Outputs (into the same directory as this script):
    AllCards.html             96 cards, 9-up A4, color-coded by deck
    StudioMat.html            One A4 landscape playmat (print 4 copies)
    PlaytesterHandout.html    Quick reference + feedback form (per playtester)
    ModeratorPacket.html      Answer key + 10-min script (one copy, moderator only)
    PRINT_INSTRUCTIONS.md     How many copies of each, in what order
"""

import re
import random
from collections import defaultdict
from pathlib import Path

ROOT       = Path(__file__).resolve().parent.parent
CARDS_DIR  = ROOT / "02_Cards"
RULE_DIR   = ROOT / "01_Rulebook"
PLAY_DIR   = ROOT / "05_Playtesting"
OUT_DIR    = Path(__file__).resolve().parent

# ─── Deck metadata ──────────────────────────────────────────────────────────────
# (filename_prefix, css_class, header_label, iso_doc_label, header_hex, suppress_title)
# suppress_title=True for Outfit Detail so flawed and clean cards are visually
# identical — the markdown headers describe the flaw for the moderator only.
DECKS = [
    ("01_Brand_Identity",        "deck-bi",  "BRAND IDENTITY",        "Organizational Test Strategy",   "#D81E5B", False),
    ("02_Runway_Roadmap",        "deck-rr",  "RUNWAY ROADMAP",        "Project Test Plan",              "#3B3F8F", False),
    ("03_Collection_Theme",      "deck-ct",  "COLLECTION THEME",      "Test Design Specification",      "#6FAE6E", False),
    ("04_Outfit_Detail",         "deck-od",  "OUTFIT DETAIL",         "Test Case Specification",        "#9D8BD9", True),
    ("05_Runway_Instructions",   "deck-ri",  "RUNWAY INSTRUCTIONS",   "Test Procedure Specification",   "#5F6B7A", False),
    ("06_Wardrobe_Malfunction",  "deck-wm",  "WARDROBE MALFUNCTION",  "Defect Report",                  "#C0392B", False),
    ("07_Event_Cards",           "deck-ev",  "EVENT / ACTION",        "Risk / Environment Factor",      "#E0A823", False),
]

# ─── Markdown parser ────────────────────────────────────────────────────────────

CARD_HEADER_RE = re.compile(r'^(##+) +([A-Z]{2,3}-[A-Z0-9-]+)( +[—-] +(.+))?$')
FIELD_RE       = re.compile(r'^- \*([^*]+):\*\s*(.*)$')
RULE_RE        = re.compile(r'^- \*\*([^*]+):\*\*\s*(.*)$')

def parse_card_file(path: Path):
    """Return list of cards: each is dict {id, title, fields:[(name,val)], rules:[(name,val)], answer_key:str|None, prose:str|None}."""
    cards = []
    current = None
    body_lines = []

    def flush():
        nonlocal current, body_lines
        if current is None:
            return
        # Walk body lines, extract fields and rules
        prose_buf = []
        for line in body_lines:
            stripped = line.strip()
            if not stripped:
                continue
            m = FIELD_RE.match(stripped)
            if m:
                current["fields"].append((m.group(1).strip(), m.group(2).strip()))
                continue
            m = RULE_RE.match(stripped)
            if m:
                name = m.group(1).strip()
                val  = m.group(2).strip()
                if name.lower().startswith("answer key"):
                    current["answer_key"] = val
                else:
                    current["rules"].append((name, val))
                continue
            # Heading inside body? skip "Why these matter" sections
            if stripped.startswith("##") or stripped.startswith("---"):
                break
            # Plain prose (Event cards)
            if stripped.startswith("- "):
                prose_buf.append(stripped[2:])
            else:
                prose_buf.append(stripped)
        if prose_buf and not current["fields"] and not current["rules"]:
            current["prose"] = " ".join(prose_buf)
        cards.append(current)
        current = None
        body_lines = []

    for raw in path.read_text().splitlines():
        m = CARD_HEADER_RE.match(raw)
        if m:
            flush()
            cid = m.group(2)
            title = (m.group(4) or "").strip().strip('"').strip("'")
            current = {"id": cid, "title": title, "fields": [], "rules": [], "answer_key": None, "prose": None}
        elif current is not None:
            # Stop collecting if we hit a section header
            if raw.startswith("## ") and not CARD_HEADER_RE.match(raw):
                flush()
                continue
            if raw.startswith("---"):
                flush()
                continue
            body_lines.append(raw)
    flush()

    # Filter out "cards" with no fields/rules/prose (e.g., section headers caught accidentally)
    cards = [c for c in cards if c["fields"] or c["rules"] or c["prose"]]
    return cards


# ─── HTML rendering ────────────────────────────────────────────────────────────

CARD_CSS = """
@page { size: A4; margin: 5mm; }
* { box-sizing: border-box; }
body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; margin: 0; color: #222; }
.page {
    display: grid;
    grid-template-columns: repeat(3, 63mm);
    grid-template-rows: repeat(3, 88mm);
    gap: 2mm;
    page-break-after: always;
    justify-content: center;
    align-content: start;
}
.card {
    width: 63mm; height: 88mm;
    border: 0.4mm solid #333;
    border-radius: 2mm;
    padding: 0;
    overflow: hidden;
    position: relative;
    background: white;
    display: flex; flex-direction: column;
}
.card .header {
    color: white;
    font-weight: 700;
    font-size: 6.5pt;
    padding: 1.4mm 2.5mm;
    letter-spacing: 0.3pt;
    display: flex; justify-content: space-between; align-items: center;
}
.card .body {
    padding: 2mm 2.5mm 2mm 2.5mm;
    font-size: 6.8pt;
    line-height: 1.25;
    flex: 1;
    overflow: hidden;
}
.card .title {
    font-size: 9pt;
    font-weight: 700;
    margin-bottom: 1.5mm;
    color: #111;
}
.card .field {
    margin-bottom: 0.8mm;
}
.card .field .name {
    font-style: italic;
    color: #555;
}
.card .rule {
    margin-top: 1mm;
    padding: 1mm 1.5mm;
    background: #fff5d6;
    border-left: 1mm solid #e0a823;
    font-size: 6.5pt;
}
.card .rule .name { font-weight: 700; }
.card .prose { font-size: 7pt; }
.card .footer {
    border-top: 0.2mm solid #ccc;
    padding: 1mm 2.5mm;
    font-size: 5.5pt;
    color: #666;
    text-align: center;
}

/* Color theming via deck class on .card */
.deck-bi  .header { background: #D81E5B; }
.deck-rr  .header { background: #3B3F8F; }
.deck-ct  .header { background: #6FAE6E; }
.deck-od  .header { background: #9D8BD9; }
.deck-ri  .header { background: #5F6B7A; }
.deck-wm  .header { background: #C0392B; }
.deck-ev  .header { background: #E0A823; }

/* Print only — hide the on-screen instructions */
@media print {
    .screen-only { display: none; }
}
.screen-only {
    background: #f4f4f4;
    padding: 12pt;
    font-size: 10pt;
    margin: 8pt;
    border-left: 4pt solid #3B3F8F;
}
"""

def render_card(card, deck_class, deck_label, iso_label, suppress_title=False):
    title = "" if suppress_title else (card["title"] or "")
    chip_id = card.get("display_id") or card["id"]
    fields_html = "".join(
        f'<div class="field"><span class="name">{name}:</span> {val if val else "&nbsp;"}</div>'
        for name, val in card["fields"]
    )
    rules_html = "".join(
        f'<div class="rule"><span class="name">{name}:</span> {val}</div>'
        for name, val in card["rules"]
    )
    prose_html = f'<div class="prose">{card["prose"]}</div>' if card["prose"] else ""
    title_html = f'<div class="title">{title}</div>' if title else ""
    return f"""
    <div class="card {deck_class}">
      <div class="header"><span>{deck_label}</span><span>{chip_id}</span></div>
      <div class="body">
        {title_html}
        {fields_html}
        {rules_html}
        {prose_html}
      </div>
      <div class="footer">Maps to: {iso_label}</div>
    </div>
    """

def chunked(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]


def build_all_cards():
    pages_html = []
    answer_keys = []
    deck_card_counts = {}
    total = 0
    for prefix, css, label, iso, _hex, suppress_title in DECKS:
        path = next((p for p in CARDS_DIR.iterdir() if p.name.startswith(prefix)), None)
        if path is None:
            print(f"WARN: deck file missing for prefix {prefix}")
            continue
        cards = parse_card_file(path)

        # Anti-leak treatment for Outfit Detail deck:
        #   - Group by season prefix (SS26, AW26, PF26, CR26)
        #   - Shuffle deterministically within each season
        #   - Renumber sequentially within season so clean and flawed Identifiers
        #     are interleaved (kills the "100+ = flawed" pattern in markdown)
        #   - Use the new identifier as the printed chip ID (kills OD-C / OD-F)
        if prefix == "04_Outfit_Detail":
            rng = random.Random(20260503)  # fixed seed: reproducible across builds
            by_season = defaultdict(list)
            for c in cards:
                ident = next((v for k, v in c["fields"] if k == "Identifier"), "XX-000")
                season = ident.split("-")[0]
                by_season[season].append(c)
            renumbered_order = []
            for season in sorted(by_season):
                bucket = by_season[season]
                rng.shuffle(bucket)
                for i, c in enumerate(bucket, start=1):
                    new_ident = f"{season}-{i:03d}"
                    c["display_id"] = new_ident
                    c["fields"] = [
                        (k, new_ident if k == "Identifier" else v)
                        for k, v in c["fields"]
                    ]
                    renumbered_order.append(c)
            cards = renumbered_order

        deck_card_counts[label] = len(cards)
        total += len(cards)
        # Collect answer keys (Outfit Detail flawed cards) — preserve old + new ID for moderator
        for c in cards:
            if c["answer_key"]:
                display = c.get("display_id") or c["id"]
                answer_keys.append((c["id"], display, c["title"], c["answer_key"]))
        # Render in pages of 9
        for chunk in chunked(cards, 9):
            page = '<div class="page">'
            page += "".join(render_card(c, css, label, iso, suppress_title) for c in chunk)
            page += "</div>"
            pages_html.append(page)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Runway Ready — All Cards (Print Ready)</title>
<style>{CARD_CSS}</style>
</head>
<body>
<div class="screen-only">
  <strong>Runway Ready — printable card deck.</strong><br>
  Total: {total} cards. Use your browser's Print (Cmd-P) → A4, no scaling, no headers/footers.<br>
  Each page is 9 cards (3×3). Cut along card edges. Sleeve in poker-size sleeves (63 × 88 mm).<br>
  Decks: {", ".join(f"{k} ({v})" for k, v in deck_card_counts.items())}.
</div>
{''.join(pages_html)}
</body>
</html>"""
    (OUT_DIR / "AllCards.html").write_text(html)
    return total, deck_card_counts, answer_keys


# ─── Studio Mat ────────────────────────────────────────────────────────────────

STUDIO_MAT_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Runway Ready — Studio Mat</title>
<style>
@page { size: A4 landscape; margin: 8mm; }
body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; margin: 0; color: #222; }
.mat {
  width: 281mm; height: 197mm;
  border: 0.6mm solid #333;
  border-radius: 4mm;
  padding: 5mm 7mm;
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: auto auto auto auto auto auto;
  gap: 3mm;
  background: #fafafa;
}
.title { font-size: 18pt; font-weight: 700; margin: 0; }
.sub { font-size: 9pt; color: #666; margin: 0 0 2mm 0; }
.zone {
  border: 0.3mm dashed #888;
  border-radius: 2mm;
  padding: 3mm 4mm;
  background: white;
  position: relative;
}
.zone .label {
  position: absolute; top: 2mm; right: 4mm;
  font-size: 7pt; color: #888; font-style: italic;
}
.zone .name { font-size: 11pt; font-weight: 700; }
.zone .iso { font-size: 8pt; color: #555; }
.zone.outfits { display: grid; grid-template-columns: repeat(4, 1fr); gap: 3mm; padding: 6mm 4mm; }
.zone.outfits .slot { border: 0.3mm dashed #aaa; border-radius: 2mm; min-height: 16mm; padding: 2mm; font-size: 7pt; color: #888; text-align: center; }
.summary {
  border: 0.3mm solid #888;
  padding: 3mm 4mm;
}
.summary table { width: 100%; border-collapse: collapse; font-size: 8pt; }
.summary th, .summary td { border-bottom: 0.2mm solid #ccc; padding: 1.5mm 2mm; text-align: left; }
.summary th { background: #f0f0f0; }
.zone-bi { border-left: 2mm solid #D81E5B; }
.zone-rr { border-left: 2mm solid #3B3F8F; }
.zone-ct { border-left: 2mm solid #6FAE6E; }
.zone-od { border-left: 2mm solid #9D8BD9; }
.zone-ri { border-left: 2mm solid #5F6B7A; }
</style>
</head>
<body>
<div class="mat">
  <div>
    <div class="title">RUNWAY READY — Studio Mat</div>
    <div class="sub">Player: ____________________________   ·   ISO/IEC 29119-3 Test Documentation Hierarchy</div>
  </div>

  <div class="zone zone-bi">
    <div class="label">Zone 1</div>
    <div class="name">BRAND IDENTITY</div>
    <div class="iso">Organizational Test Strategy · place 1 card here at game start</div>
  </div>

  <div class="zone zone-rr">
    <div class="label">Zone 2 — Phase 1: PLAN</div>
    <div class="name">RUNWAY ROADMAP</div>
    <div class="iso">Project Test Plan · 1 active per round</div>
  </div>

  <div class="zone zone-ct">
    <div class="label">Zone 3 — Phase 2: DESIGN</div>
    <div class="name">COLLECTION THEME</div>
    <div class="iso">Test Design Specification · 1 active per Roadmap</div>
  </div>

  <div class="zone zone-od outfits">
    <div style="grid-column: 1 / -1;">
      <div class="label">Zone 4 — Phase 3: SPECIFY</div>
      <div class="name">OUTFIT DETAIL CARDS</div>
      <div class="iso">Test Case Specification · place ≥ 3 cards before Rehearsal</div>
    </div>
    <div class="slot">Outfit Slot 1</div>
    <div class="slot">Outfit Slot 2</div>
    <div class="slot">Outfit Slot 3</div>
    <div class="slot">Outfit Slot 4 / 5 (optional)</div>
  </div>

  <div class="zone zone-ri">
    <div class="label">Zone 5 — Phase 4: PROCEDURE</div>
    <div class="name">RUNWAY INSTRUCTIONS</div>
    <div class="iso">Test Procedure Specification · declares walk order &amp; dependencies</div>
  </div>

  <div class="summary">
    <strong style="font-size: 10pt;">REHEARSAL SUMMARY</strong> &nbsp;
    <span style="font-size: 8pt; color: #666;">Phase 5 · Test Status / Completion Report · fill 1 row per Outfit at end of round</span>
    <table>
      <thead><tr><th style="width: 25%;">Outfit ID</th><th style="width: 15%;">Pass / Fail</th><th>Originating Doc Field (if Fail)</th></tr></thead>
      <tbody>
        <tr><td>&nbsp;</td><td></td><td></td></tr>
        <tr><td>&nbsp;</td><td></td><td></td></tr>
        <tr><td>&nbsp;</td><td></td><td></td></tr>
        <tr><td>&nbsp;</td><td></td><td></td></tr>
        <tr><td>&nbsp;</td><td></td><td></td></tr>
      </tbody>
    </table>
  </div>
</div>
</body>
</html>"""

def build_studio_mat():
    (OUT_DIR / "StudioMat.html").write_text(STUDIO_MAT_HTML)


# ─── Playtester Handout (QuickRef + Feedback Form) ─────────────────────────────

def md_to_simple_html(md_text: str) -> str:
    """Tiny markdown-to-HTML converter (only what we use in our docs)."""
    lines = md_text.splitlines()
    out, in_table, in_list, in_code = [], False, False, False
    for raw in lines:
        line = raw.rstrip()
        if line.startswith("```"):
            if in_code:
                out.append("</pre>")
            else:
                out.append("<pre>")
            in_code = not in_code
            continue
        if in_code:
            out.append(line.replace("<", "&lt;").replace(">", "&gt;"))
            continue
        # Headers
        m = re.match(r'^(#{1,4}) +(.+)$', line)
        if m:
            level = len(m.group(1))
            out.append(f"<h{level}>{inline_md(m.group(2))}</h{level}>")
            continue
        # Tables
        if "|" in line and re.match(r'^\s*\|', line):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(re.match(r'^:?-+:?$', c) for c in cells):
                continue  # separator row
            if not in_table:
                out.append("<table>")
                in_table = True
            tag = "th" if (out and out[-1] == "<table>") else "td"
            out.append("<tr>" + "".join(f"<{tag}>{inline_md(c)}</{tag}>" for c in cells) + "</tr>")
            continue
        elif in_table:
            out.append("</table>")
            in_table = False
        # Lists
        if re.match(r'^\s*- ', line):
            if not in_list:
                out.append("<ul>")
                in_list = True
            content = line.lstrip()[2:]
            out.append(f"<li>{inline_md(content)}</li>")
            continue
        elif in_list and not line.strip():
            out.append("</ul>")
            in_list = False
            out.append("")
            continue
        # Horizontal rule
        if line.strip() == "---":
            out.append("<hr>")
            continue
        # Blockquote
        if line.startswith("> "):
            out.append(f"<blockquote>{inline_md(line[2:])}</blockquote>")
            continue
        # Plain paragraph
        if line.strip():
            out.append(f"<p>{inline_md(line)}</p>")
        else:
            out.append("")
    if in_table: out.append("</table>")
    if in_list: out.append("</ul>")
    if in_code: out.append("</pre>")
    return "\n".join(out)

def inline_md(s: str) -> str:
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', s)
    return s


HANDOUT_CSS = """
@page { size: A4; margin: 14mm; }
body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #222; font-size: 10pt; line-height: 1.4; max-width: 180mm; margin: 0 auto; }
h1 { font-size: 18pt; border-bottom: 0.6mm solid #3B3F8F; padding-bottom: 2mm; }
h2 { font-size: 13pt; color: #3B3F8F; margin-top: 8mm; }
h3 { font-size: 11pt; }
table { width: 100%; border-collapse: collapse; margin: 3mm 0; font-size: 9pt; }
th, td { border: 0.2mm solid #999; padding: 1.5mm 2mm; text-align: left; vertical-align: top; }
th { background: #eee; }
ul { padding-left: 5mm; }
code { background: #f3f3f3; padding: 0 1mm; border-radius: 1mm; }
hr { border: none; border-top: 0.2mm solid #999; margin: 6mm 0; }
blockquote { border-left: 2mm solid #6FAE6E; padding-left: 4mm; margin-left: 0; color: #444; }
.section { page-break-after: always; }
.section:last-child { page-break-after: auto; }
"""

def build_handout():
    qr = (RULE_DIR / "QuickReference.md").read_text()
    fb = (PLAY_DIR / "Feedback_Form.md").read_text()
    body = (
        '<div class="section">' + md_to_simple_html(qr) + "</div>"
        '<div class="section">' + md_to_simple_html(fb) + "</div>"
    )
    html = f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8">
<title>Runway Ready — Playtester Handout</title>
<style>{HANDOUT_CSS}</style>
</head><body>{body}</body></html>"""
    (OUT_DIR / "PlaytesterHandout.html").write_text(html)


def build_moderator(answer_keys):
    script = (PLAY_DIR / "Playtest_Script.md").read_text()
    rb     = (RULE_DIR / "Rulebook.md").read_text()

    ak_html = ['<h1>Moderator Answer Key — DO NOT SHOW PLAYERS</h1>',
               '<p>The 15 flawed Outfit Detail cards and their planted defects. The "Card ID on table" column is what is actually printed on the card chip — use this to locate cards during play. Keep this sheet face-down beside you during play. Reveal only during post-game debrief.</p>',
               '<table><tr><th>Card ID on table</th><th>(internal markdown ID)</th><th>Flaw class</th><th>Originating field</th></tr>']
    # Sort by displayed Card ID for moderator lookup convenience
    for old_id, display_id, title, ak in sorted(answer_keys, key=lambda r: r[1]):
        ak_html.append(f'<tr><td><strong>{display_id}</strong></td><td><code>{old_id}</code></td><td>{title}</td><td>{ak}</td></tr>')
    ak_html.append('</table>')

    body = (
        "".join(ak_html) +
        '<hr><div class="section">' + md_to_simple_html(script) + "</div>" +
        '<hr><div class="section">' + md_to_simple_html(rb) + "</div>"
    )
    html = f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8">
<title>Runway Ready — Moderator Packet</title>
<style>{HANDOUT_CSS}</style>
</head><body>{body}</body></html>"""
    (OUT_DIR / "ModeratorPacket.html").write_text(html)


# ─── Print instructions ────────────────────────────────────────────────────────

PRINT_INSTRUCTIONS_TEMPLATE = """# What to Print — Week 3 In-Class Demo

Open each `.html` file below in a browser (Safari / Chrome), then **File → Print** with these settings:
- Paper: **A4**
- Scale: **100% (no shrink-to-fit)**
- Margins: **Default**
- Headers/Footers: **OFF**
- Background graphics: **ON** (so the colored deck headers print)

| File | Pages | Copies | Who gets it |
|---|---|---|---|
| `AllCards.html` | {pages_cards} (9 cards each) | 1 | Cut into 96 cards. The deck. |
| `StudioMat.html` | 1 (A4 landscape) | 4 | One per player |
| `PlaytesterHandout.html` | 2 | 1 per playtester (≈ 4) | Hand out at start of session |
| `ModeratorPacket.html` | ~5 | 1 | SunShine team member running the table — keep private |

Total: ~{total_pages} A4 pages.

## After printing AllCards.html

1. Cut along card edges (paper trimmer recommended — straight edges matter).
2. Sleeve in standard poker-size sleeves (63 × 88 mm) — optional but extends life.
3. Sort into 7 stacks by deck (header colour makes this trivial):
{deck_summary}
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
"""

def write_print_instructions(total_cards, deck_counts):
    pages_cards = (total_cards + 8) // 9  # ceil division
    total_pages = pages_cards + 1 + 2 + 5  # cards + mat + handout + moderator
    deck_summary = "\n".join(f"   - {label}: {count} cards" for label, count in deck_counts.items())
    (OUT_DIR / "PRINT_INSTRUCTIONS.md").write_text(
        PRINT_INSTRUCTIONS_TEMPLATE.format(
            pages_cards=pages_cards,
            total_pages=total_pages,
            deck_summary=deck_summary,
        )
    )


# ─── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("Building Runway Ready printable prototype...")
    total, deck_counts, answer_keys = build_all_cards()
    build_studio_mat()
    build_handout()
    build_moderator(answer_keys)
    write_print_instructions(total, deck_counts)

    print(f"\n  AllCards.html            {total} cards across {sum(1 for _ in deck_counts.items())} decks")
    for label, n in deck_counts.items():
        print(f"     · {label}: {n}")
    print(f"  StudioMat.html           1 mat (print 4 copies)")
    print(f"  PlaytesterHandout.html   QuickRef + FeedbackForm")
    print(f"  ModeratorPacket.html     {len(answer_keys)} answer-key entries + script + rulebook")
    print(f"  PRINT_INSTRUCTIONS.md    print/cut/sort guide")
    print(f"\nOutput dir: {OUT_DIR}")

if __name__ == "__main__":
    main()
