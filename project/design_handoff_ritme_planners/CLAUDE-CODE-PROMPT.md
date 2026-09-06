# Paste this into Claude Code

> Copy everything between the rules below into your first Claude Code message, with this folder open
> as the working directory.

---

I'm building **Het Ritme**, a digital planner shop for neurodivergent (ADHD-focused) customers. This
folder is a complete design handoff. Read these files first, in this order, before writing anything:

1. `README.md` — what the business is and what gets built
2. `BRAND.md` — name, mark, voice
3. `DESIGN-SYSTEM.md` — both aesthetic editions, exact hex values, type, components
4. `PLANNER-SPEC-BUDGET.md` — the nine-screen architecture and every formula
5. `BUILD-GUIDE.md` — how to construct the .xlsx and the Notion template
6. `ANTI-AI-CHECKLIST.md` — **read this twice; it is the difference between shippable and generic**
7. `design-references/` — open both .html canvases in a browser; they are the visual source of truth

**Ask me the clarifying questions in `CLARIFYING-QUESTIONS.md` before you start building.** Do not
guess your way past them.

## What I need built

### A. Brand artifacts (`/brand`)
The Focus Ring mark and HET RITME wordmark as clean, hand-written SVG — geometric primitives only
(circles, rects, real type), no traced or generated illustration:

- `het-ritme-mark.svg` — ring + dot, ink `#262119`, dot in the edition accent. Stroke = 1/10 of diameter,
  dot = 1/4 of diameter. Include a 24px-optimised variant with the stroke bumped for legibility.
- `het-ritme-lockup-horizontal.svg`, `het-ritme-lockup-stacked.svg`
- Colour variants of each: Calm accent `#4A6250`, Loud accent `#D65A34`, all-ink, reversed on ink,
  reversed on colour
- `favicon.svg` + PNG exports at 16/32/64/180/512
- `/brand/exports/` — PNG at 1x/2x/3x for Etsy and social
- `/brand/README.md` — clear-space rule (0.5 x mark diameter), minimum sizes, the below-20px
  wordmark-drop rule, what never to do

### B. Product prototype (`/prototype`)
A working, clickable prototype of the **whole shop** — this is how I review the product line before any
spreadsheet is built. Plain HTML/CSS/JS, or React + Vite if you prefer; no CSS framework, no component
library, no Tailwind. Inline or a single hand-written stylesheet.

Two things it must contain:

**1. The shop** — a browsable storefront of all 6 planners, each showing its two editions and two
formats. Real copy from `SEO-AND-MARKETING.md` and canvas artboard `3d`. Not lorem ipsum, not
invented features.

**2. The Budget planner, fully interactive, in both editions** — all nine screens from
`PLANNER-SPEC-BUDGET.md`, wired with real working formulas over a small seeded dataset in
localStorage:
- `1 Set up`, `2 Accounts`, `3 Add spending`, `4 This month` (default), `5 Bills calendar`,
  `6 Year overview`, `7 Goals & savings`, `8 Debt`, `9 Net worth`
- The numbered 1–2–3 phase rail, with the three-state cell legend on every screen
- A working month switcher — all twelve months behind it, never twelve separate screens
- A **Calm / Loud toggle in the top bar** that reskins the entire prototype live. Same DOM, same
  numbers, different theme — that switch is the whole business model, so it has to feel effortless.
- Loud only: the four celebration mechanics (badge tiers, confetti moment, colour shift + quote,
  streak counter that keeps your best and never resets)
- Calm only: no celebration graphics at all — a met goal reads *goal met*. The restraint is a feature.
- Currency driven by one setup value. Never hardcode € or $ anywhere.

Then stub the other five planners at one screen each, enough to show their structure and voice:
Dopamine Budget, Debt Buster, Meal Prep for Kids, Home Cleaning Planner, Single Girl Meal Planner.

### C. The real deliverables (`/build`)
Once I've signed off the prototype:
- `het-ritme-budget-calm.xlsx` and `het-ritme-budget-loud.xlsx` per `BUILD-GUIDE.md` — nine sheets, frozen
  rail in column A, protected sheets with only the intended cells unlocked, `SUMIFS`/`INDEX+MATCH`
  only (no `LAMBDA`, `LET`, `XLOOKUP`, dynamic arrays, macros, pivot tables, or merged cells, so the
  file survives Excel → Google Sheets → Apple Numbers)
- `/build/notion/` — the page tree, database schemas, property formulas, and a written import
  procedure
- The `customer-docs/` markdown rendered to print-ready PDF in each edition's theme

## Working rules
- **Match the hex values, type sizes, and copy exactly.** They are final, not suggestions.
- If the target format genuinely cannot do something (rounded corners in Excel, animation in Notion),
  use the documented degradation in `BUILD-GUIDE.md`. Do not invent a substitute and do not fake it.
- Never write copy in your own voice — use the voice rules in `BRAND.md`. If a string is missing, ask.
- No emoji anywhere in the product. No AI-generated imagery. No hand-drawn SVG illustration.
- Read `ANTI-AI-CHECKLIST.md` before you commit, and self-review against it.

Start by asking me the clarifying questions.

---
