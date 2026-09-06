# Handoff: Het Ritme digital planner shop

## Overview
Het Ritme is a digital planner shop for neurodivergent (ADHD-focused) customers. Every planner ships in
**two file formats** (spreadsheet + Notion) and **two aesthetic editions** (Calm + Loud), so one product
line serves opposite sensory needs without forcing anyone into a single look.

Product lineup (6 planners x 2 formats x 2 editions = 24 SKUs):

| # | Planner | Category |
|---|---------|----------|
| 1 | Dopamine Budget | Budget |
| 2 | Minimalist Budget | Budget |
| 3 | Debt Buster / Debt Crusher | Budget |
| 4 | Meal Prep for Kids | Lifestyle |
| 5 | Home Cleaning Planner | Lifestyle |
| 6 | Single Girl Meal Planner | Lifestyle |

**This handoff covers the Budget planner in full** (screens, formulas, styling, both editions, both
formats). The other five reuse the same nine-screen architecture and design system; specs for those
follow the same template and can be derived from `PLANNER-SPEC-BUDGET.md`.

## About the design files
The files in `design-references/` are **design references created in HTML** — prototypes showing the
intended look, layout, and voice. They are **not production code to copy**. The build target here is
not a web app: it is

1. an **.xlsx workbook** (opens in Excel, Google Sheets, Apple Numbers), and
2. a **Notion template** page tree,

each produced in a Calm and a Loud variant. Use the HTML only as the visual and copy source of truth.
If you also build a marketing site later, recreate the HTML designs in that site's own framework
rather than shipping these files.

## Fidelity
**High-fidelity.** Colors, type, spacing, copy, and states in the reference files are final. Match hex
values and copy exactly. Where a spreadsheet cannot reproduce something (custom fonts, rounded corners,
animation), use the documented degradation in `BUILD-GUIDE.md` — do not invent a substitute.

## What to build, in order
1. `het-ritme-budget-calm.xlsx` — spreadsheet, Calm edition
2. `het-ritme-budget-loud.xlsx` — same workbook, Loud theming + reward mechanics
3. Notion template, Calm — page tree + databases
4. Notion template, Loud — same structure, Loud theming
5. Customer-facing `WELCOME.md` / PDF per SKU (source in `customer-docs/`)

## Documents in this bundle
| File | What it is |
|------|-----------|
| `CLAUDE-CODE-PROMPT.md` | **Start here** — the prompt to paste into Claude Code |
| `CLARIFYING-QUESTIONS.md` | Four questions to ask the owner before building |
| `ANTI-AI-CHECKLIST.md` | What was rejected for feeling machine-made, and the rules that replaced it |
| `BRAND.md` | Name, logo, voice, taglines, do/don't |
| `DESIGN-SYSTEM.md` | Both editions: color, type, components, cell language, celebration mechanics |
| `PLANNER-SPEC-BUDGET.md` | The nine screens, every field, every formula |
| `BUILD-GUIDE.md` | How to actually construct the .xlsx and the Notion template |
| `customer-docs/WELCOME.md` | Ships with the product — the 4-minute start |
| `customer-docs/HOW-TO-NAVIGATE.md` | Ships with the product — screen-by-screen guide |
| `SEO-AND-MARKETING.md` | Etsy SEO, listing copy, launch plan, content calendar |
| `design-references/` | The HTML design files |

## Non-negotiables
- **Nine screens, three phases.** Never 29 tabs. The reference workbook it replaces had 29; that is the
  problem being solved.
- **Twelve months behind one month switcher**, not twelve month tabs.
- **Three cell states only** (yours / automatic / required) with the legend visible on every screen.
- **Currency-agnostic.** One setup cell drives every currency symbol. Never hardcode € or $.
- **No emoji in the Calm edition.** Loud may use shape-based badges, still no emoji in headings.
- **Nothing resets a user's progress.** Broken streaks retain "best", missed weeks are data, not failure.
