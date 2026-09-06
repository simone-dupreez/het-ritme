# Het Ritme — dual-aesthetic design system

Two editions share one structure. Only surface treatment and voice change: corner radius, fill vs.
rule, colour count, bar weight. Nothing structural. This is what makes 24 SKUs maintainable.

---

## 1. Calm edition

### Colour
| Role | Hex | Use |
|---|---|---|
| Canvas | `#CFC7BA` | Outer background (presentation only, not in-file) |
| Paper | `#EDE8DE` | Primary screen background |
| Paper alt | `#E4DFD3` | Alternating screen background |
| Card | `#F6F2E9` | Cards, blocks, table rows |
| Cell white | `#FFFFFF` | Editable cells |
| Rule | `#DCD5C6` | Hairlines, borders |
| Quiet ink | `#8A8474` | Calculated values, captions |
| Body ink | `#4E4740` | Body copy |
| Ink | `#262119` | Headings, wordmark |
| Accent — sage | `#4A6250` | Progress fills, accent blocks, mark dot |

Accent alternates approved in review (pick one per product line, never mix): navy `#3D4A5C`,
terracotta `#B4694E`, charcoal `#3A3A38`. Debt Buster Calm uses navy `#3D4A5C`.

Rules: one accent per screen. Zero gradients. Zero shadows on flat UI (photo cards may carry
`0 20px 44px rgba(38,33,25,.16)`). Every Calm screen must remain legible printed in greyscale —
accent never carries meaning alone.

### Type
- Display / headings: **Bricolage Grotesque** 600, `letter-spacing: -.035em`, line-height .96–1.0
- Body, captions, figures, quotes: **Lora** 400 / italic
- Spreadsheet fallback (fonts not installed on customer machines): **Arial** everywhere; keep sizes
- Scale: display 56–62 / section head 30–34 / lead 21 / body 18 / caption 17 italic / figure 16

### Components
- **Button primary**: accent fill, paper text, square corners, padding 12/22
- **Button secondary**: 1px ink border, transparent fill, ink text
- **Table row**: 44px min height, hairline `#DCD5C6` separator, no zebra fill
- **Progress bar**: 3px track `#E4DED0`, accent fill, square ends
- **Status**: text only — *on track* / *needs review* / *goal met* in ink; never a coloured pill
- Corner radius: **0** everywhere. Spacing: 8pt base; screen padding 58px, card padding 30–34px

---

## 2. Loud edition

### Colour
| Role | Hex | Use |
|---|---|---|
| Cream base | `#F6E8D2` | Primary screen background |
| Card cream | `#FFFBF2` | Cards, rows |
| Track | `#F3E4CC` | Progress bar tracks |
| Ink | `#262119` | All headings and body |
| Body ink | `#574A38` | Secondary copy |
| Coral | `#D65A34` | Spending, primary action, mark dot |
| Teal | `#2E7D74` | Saving, positive state |
| Gold | `#E8B23C` | Reward, badges, warnings |
| Grape | `#6B4E9B` | Debt, streaks |
| Lime | `#5F8C33` | Income, meal planners |

**Colour has a fixed job** across all six planners: coral = spend, teal = save, gold = reward,
grape = debt, lime = income. Never decorative reassignment.

Rules: **one saturated fill per block** — two touching saturated fills is the line between playful and
chaotic. Ink is always `#262119`; colour never carries body copy. Loudness ceiling was set at 6/10 by
the owner: colour blocking and voice, not stickers and doodles.

### Type
- Display / headings: **Bricolage Grotesque** 800, `letter-spacing: -.04em`, line-height .94–.98
- Body, figures, asides: **Lora** 400 / italic
- Spreadsheet fallback: **Arial Bold** for headings, **Arial** for body
- Scale: display 60–66 / section head 30 / lead 21 / body 17.5 / figure 16

### Components
- **Button primary**: coral fill, cream text, radius 999px, padding 13/24
- **Button secondary**: 2px teal border, white fill, teal text, radius 999px
- **Button reward**: gold fill, ink text, radius 999px
- **Card**: radius 18–22px, cream fill, shadow `0 22px 46px rgba(38,33,25,.18)` on floating cards only
- **Table row**: 44px min height, radius 12px, alternating `#FFFFFF` / transparent
- **Progress bar**: 12px track `#F3E4CC` radius 999px, fill in the category's assigned colour
- **Status pill**: filled, radius 999px, 12px 600 weight — *on track* (lime) / *check in* (track fill) /
  *goal smashed* (gold)

---

## 3. Cell language (both editions)

Three states, learned in four seconds, legend repeated on every screen. This replaces a page of
warnings about protected cells.

| State | Calm | Loud | Meaning |
|---|---|---|---|
| Yours to fill in | white fill, 1px ink border | white fill, 2px teal border, radius 10 | The only cells the user touches |
| Works itself out | `#E4DFD3` fill, `#DCD5C6` border, quiet ink text | `#F3ECE0` fill, 2px dashed `#DCCDB6` | Protected + calculated |
| Needed for the maths | header label with ` *` suffix | same, or coral pill in Loud | Required for formulas to resolve |

If a required column is empty, the screen shows a single plain sentence naming it. **Never** show a
broken total, `#DIV/0!`, or a red error.

---

## 4. Celebration mechanics (Loud only, static-safe)

All four must work as **static states** so they survive Excel and Notion.

1. **Badge unlock** — three tiers per goal. Filled circle = earned (gold, then teal), dashed outline =
   next up. Never more than three per goal.
2. **Confetti moment** — 5–7 shapes (square, rectangle, circle) in coral/teal/gold/grape/lime, one
   rotation each, inside a white rounded panel. Excel: image revealed by conditional formatting at 100%.
   Notion: callout block.
3. **Colour shift + quote** — on completion the goal card inverts: cream-on-colour becomes
   colour-on-cream. One line drawn from the celebration copy bank.
4. **Streak counter** — big Lora figure in grape + a row of 22px rounded squares, filled for logged
   weeks. **A broken streak never resets to zero** — it displays "best: N" alongside.

Calm equivalent: no celebration graphics. A completed goal shows the accent bar at 100% and the plain
words *goal met*. That restraint is the feature.

---

## 5. Scaling across platforms

**Excel / Sheets / Numbers**
- Navigation rail = frozen column A of named-range hyperlinks, numbered 1–2–3 by phase
- Progress bars = data bars, single colour per category
- Badges = static images revealed by conditional formatting
- Fonts degrade to Arial; keep the size hierarchy
- Radius and shadow simply do not exist — do not fake them with borders

**Notion**
- Rail = sidebar of nine numbered sub-pages
- Cell states = locked vs. editable database properties
- Celebration = callout blocks + badge images (no emoji)
- Colour maps to Notion's nearest built-in tint, not custom hex

**Etsy**
- Image 1 hero, 2 nine-screen map, 3 cell language, 4 real screenshot, 5 formats/currency
- Thumbnail grid: mark top-left, edition aside top-right, product name bottom-left 34–36px, one
  progress bar, format line. Only palette and radius change across all 24 SKUs.
