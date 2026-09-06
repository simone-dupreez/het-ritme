# Build guide — how to construct the deliverables

## A. Spreadsheet (.xlsx for Excel / Sheets / Numbers)

### Sheet structure
Nine visible sheets, named exactly:
`1 Set up`, `2 Accounts`, `3 Add spending`, `4 This month`, `5 Bills calendar`,
`6 Year overview`, `7 Goals`, `8 Debt`, `9 Net worth`
Plus two hidden sheets: `_config` (named ranges, lists, theme values) and `_calc` (month lookups,
helper aggregates). Hide, do not delete.

### Navigation rail
- Column A, width ~26, **frozen** (freeze at B2)
- Rows grouped by phase with the phase label in Lora italic, quiet ink
- Each screen name is a hyperlink to that sheet (`=HYPERLINK("#'4 This month'!B2","This month")`)
- Current screen: Calm = accent fill, paper text; Loud = coral fill, cream text, no radius (radius does
  not exist in Excel — do not fake it)
- Bottom of the rail: the three-state cell legend, on **every** sheet

### Cell states
- Editable: white fill, thin ink border, **unlocked**
- Calculated: `#E4DFD3` (Calm) / `#F3ECE0` (Loud) fill, quiet-ink font, **locked**
- Protect every sheet with a blank password, allowing selection of unlocked cells only
- Required headers carry a literal ` *` in the header text
- Never let an error surface: wrap every division `=IFERROR(…, "")` and every lookup
  `=IFNA(…, "")`. A blank cell is always better than `#DIV/0!`

### Data validation
- Dropdowns pull from named ranges on `_config` (categories, accounts, buckets, people, months)
- Amounts: decimal >= 0, custom message in plain language ("This needs to be a number.")
- Dates: within `CFG_YEAR`, warning not blocker

### Number formats
Build from `CFG_LOCALE`:
- EU: `#.##0,00` with `.` thousands, `,` decimal; dates `DD-MM-YYYY`
- US: `#,##0.00`; dates `MM-DD-YYYY`
Prefix with `CFG_CURRENCY` via custom format or concatenation. Two decimal places everywhere money
appears. Percentages: whole numbers, no decimals.

### Progress bars
Conditional-format data bars, solid fill, no border, single colour:
- Calm: accent sage `#4A6250` (or the product's accent)
- Loud: category colour per the fixed colour jobs (coral spend / teal save / gold reward / grape debt /
  lime income)
- Over 100%: Calm switches to quiet ink `#8A8474`; Loud switches to coral `#D65A34`

### Loud reward mechanics in Excel
- **Badges**: three small PNGs per tier (earned gold, earned teal, dashed outline). Place all three
  stacked in the same cell area; use conditional formatting on the wrapper cells' fill to reveal the
  correct one, or place them side by side and grey the unearned via a semi-transparent overlay image.
  Simplest robust approach: three cells, one visible via conditional font/fill.
- **Confetti**: one PNG panel, revealed when the goal hits 100% (conditional format on a wrapper range).
- **Colour shift**: conditional formatting flips card fill from cream to the goal colour and the text
  from ink to cream at 100%.
- **Streak**: a row of 52 narrow cells; conditional fill when the week has a logged transaction.
  A separate `best_streak` cell uses `MAX` over the run lengths and is **never** reset.

### Fonts
Bricolage Grotesque and Lora will not be installed on customers' machines. Ship with **Arial**
throughout (bold Arial for Loud headings) and keep the size hierarchy from `DESIGN-SYSTEM.md`.
Do not embed fonts — it breaks Google Sheets import.

### Cross-app compatibility checklist
- No `LAMBDA`, `LET`, `XLOOKUP`, dynamic arrays, or `TEXTJOIN` with arrays — Numbers and older
  Excel choke. Use `SUMIFS`, `INDEX/MATCH`, `IFERROR`.
- No macros. No pivot tables (they degrade badly in Sheets and Numbers).
- No merged cells anywhere (they break sorting and Numbers import).
- Test the round trip: open in Excel → upload to Sheets → open in Numbers. Verify frozen rail,
  protection, data bars, dropdowns, and number formats each time.
- Print setup per sheet: fit to one page wide, landscape, margins 0.5".

## B. Notion template

### Page tree
```
Het Ritme Budget — Calm            (cover image, Focus Ring icon)
├── Start here                 (the 4-step card, callout blocks)
├── 1 Set up                   (config as a simple database, one row)
├── 2 Accounts                 (DB: Accounts) + (DB: Transfers)
├── 3 Add spending             (DB: Transactions — default view "This week", newest first)
├── 4 This month               (linked views + rollups; the landing page)
├── 5 Bills calendar           (calendar view of Transactions where Fixed = true)
├── 6 Year overview            (grouped-by-month board + toggle panels)
├── 7 Goals & savings          (DB: Funds + DB: Contributions)
├── 8 Debt                     (DB: Debts)
└── 9 Net worth                (DB: Assets + DB: Liabilities)
```

### Databases and key properties
- **Transactions**: Date, Amount (number), Category (relation → Categories), Account (relation),
  Bucket (select: Need/Want/Save), Owner (select), Fixed (checkbox), Paid (checkbox), Note
- **Categories**: Name, Group (select), Monthly target (number), rollup Actual (sum of Transactions),
  formula Left, formula Progress
- **Funds**: Name, Target, Saved (rollup), Progress (formula), Tier (formula → 0/1/2/3)
- **Debts**: Name, Balance, APR, Minimum, Order, Payoff month (formula)

### Cell language in Notion
Editable = database properties the user edits. Calculated = formula and rollup properties (Notion
already renders these as non-editable). Required = property name ends in ` *`. Add a short callout at
the top of each page repeating the three-state legend.

### Loud theming in Notion
- Callout blocks in the nearest Notion tint (orange = coral, green = teal, yellow = gold,
  purple = grape)
- Badge images uploaded as image blocks; three per fund, the earned ones above the dashed one
- **No emoji in headings.** Page icons use the Focus Ring image, not an emoji
- Celebration = a callout block whose text comes from the celebration copy bank

### Progress display
Notion cannot theme progress bars. Use the built-in bar/ring on number properties with
`Show as: Bar` and pick the closest tint. Do not build fake bars from text characters.

## C. Per-SKU export checklist
For each of the 24 SKUs:
1. Correct edition theme applied throughout (no mixed palettes)
2. Currency cell blank-but-validated, defaulting to `€`
3. Sample data removed; 3 example rows left in Add spending, clearly labelled *example — delete me*
4. Every sheet protected; only intended cells unlocked
5. Opens clean in Excel, Sheets, Numbers (spreadsheet SKUs) — no error values anywhere
6. `WELCOME` + `HOW-TO-NAVIGATE` PDFs bundled, matching the edition's theme
7. Filename: `HET-RITME-<product>-<edition>-<format>-v1.0.xlsx`
