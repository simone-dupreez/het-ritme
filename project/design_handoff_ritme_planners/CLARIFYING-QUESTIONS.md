# Ask these before building

Claude Code: ask the owner these four questions and wait for answers. Each one changes the build
materially, and guessing wrong means rework.

---

## 1. Build target for the prototype
Plain HTML/CSS/JS in one folder, or React + Vite?

- **Plain HTML** — opens by double-clicking, easiest for the owner to review and hand to anyone, no
  build step. Recommended default.
- **React + Vite** — better if this prototype later becomes a real web app or a paid web version of
  the planner.

*Do not use a CSS framework or component library either way.* Tailwind, Bootstrap, MUI and shadcn all
carry a recognisable house style that fights this brand.

## 2. Notion delivery mechanism
How is the Notion version actually delivered to a buyer?

- A **duplicatable public page** (owner maintains one master, buyer clicks Duplicate) — simplest, and
  the industry norm
- A **Markdown/CSV import bundle** the buyer imports themselves — more control, more support burden
- **Both**

This changes whether `/build/notion/` is a written construction procedure for the owner to execute by
hand, or a set of importable files.

## 3. Currency and locale defaults
The brand is European-born but must exclude nobody.

- What ships as the **default** in the file — `€` with EU number/date formats, or blank and prompted?
- Should the locale switch (EU `1.234,56` / DD-MM-YYYY vs US `1,234.56` / MM-DD-YYYY) be a single
  dropdown the buyer sets, or two separate SKUs?
- Any currencies needing special handling — ZAR, symbols that sit after the number, no-decimal
  currencies like JPY?

## 4. Scope of this pass
Which of these is the actual finish line for this session?

- **A only** — brand artifacts, nothing else
- **A + B** — brand plus the clickable prototype (recommended first pass; the owner reviews the whole
  product line before any spreadsheet work)
- **A + B + C** — everything, including the .xlsx and Notion builds

And: build **both editions** in this pass, or Calm first and Loud after sign-off?

---

## Also worth confirming if unclear
- Is the shop name final at **Het Ritme**? (The brand-system canvas is still titled ORDO — the name was
  changed after it was drawn.)
- Are there real screenshots or product photos available yet, or should every image slot stay a
  labelled placeholder?
