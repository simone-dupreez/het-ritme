# Het Ritme Budget — Notion page tree

Source of truth for structure: `PLANNER-SPEC-BUDGET.md` (fields, per screen) and `BUILD-GUIDE.md`
section B (page tree, database list). Where this document adds detail beyond BUILD-GUIDE's one-line
tree, that detail is derived from PLANNER-SPEC-BUDGET.md field-by-field — nothing below is invented
that isn't traceable to one of those two files, except where explicitly marked **Spec gap** or
**Build note**.

## One structure, two editions

Per BUILD-GUIDE.md: *"Same architecture for both editions... only theming and voice differ."* That is
true of Notion specifically as well as of the spreadsheet — **the page tree, the databases, the
properties, the views and the formulas below are identical for Calm and Loud.** Build the tree once per
edition (two separate duplicatable master pages, because cover image, icon colour and callout copy
differ), from the same instructions.

Everywhere the two diverge, it is theming or voice only, and it is called out inline as:

> **Loud only:** ...

Nothing in this document adds or removes a page, a database, or a property between editions.

## Legend blocks used throughout

Every page in the tree opens with a **cell-language legend callout** (see full text in
`IMPORT-PROCEDURE.md` — do not retype it per page, copy it once and duplicate the block). Its icon is
the Focus Ring image, never Notion's default emoji.

Where a page needs a Loud celebration callout, the tint follows the fixed colour-job mapping from
`DESIGN-SYSTEM.md` / `BUILD-GUIDE.md`:

| Colour job | Hex | Notion tint |
|---|---|---|
| Spend — coral | `#D65A34` | Orange background |
| Save — teal | `#2E7D74` | Green background |
| Reward — gold | `#E8B23C` | Yellow background |
| Debt — grape | `#6B4E9B` | Purple background |
| Income — lime | `#5F8C33` | *(no distinct Notion tint — see note below)* |

> **Spec gap:** Notion's built-in callout/tag backgrounds are Gray, Brown, Orange, Yellow, Green, Blue,
> Purple, Pink, Red. There is no tint distinct from "Green" for lime, so income and savings would
> collide on the same background. Income has no callout or celebration requirement anywhere in
> PLANNER-SPEC-BUDGET.md (it only appears as a plain list on **1 Set up**), so this collision never
> actually triggers in practice — noted for completeness, not treated as a blocker.

---

## Top level

```
Het Ritme Budget — Calm            (cover image, Focus Ring page icon)
Het Ritme Budget — Loud            (cover image, Focus Ring page icon)
├── Start here
├── 1 Set up
├── 2 Accounts
├── 3 Add spending
├── 4 This month                   ← default/landing page
├── 5 Bills calendar
├── 6 Year overview
├── 7 Goals & savings
├── 8 Debt
└── 9 Net worth
```

Two separate top-level pages (one per edition), not one page with a toggle — a buyer duplicates the
edition they bought, not both. Page icon on both top-level pages: the stacked Focus Ring + wordmark
lockup (BRAND.md: *"Stacked lockup ... for square frames: avatars, Notion page icon, planner covers"*),
from the square/stacked variant of `/home/claude/repo/brand/het-ritme-mark-*.svg` (filename set by the
brand-asset lane; pick the stacked SVG, reversed-colour version if the cover is dark). Sub-pages 1–9 use
the mark alone (ring + dot, no wordmark — BRAND.md: below 20px, drop the wordmark), since Notion renders
page icons small in the sidebar.

> **Build note — Notion sidebar has no group dividers.** BUILD-GUIDE's rail groups pages by phase with a
> label. Notion's sidebar cannot hold a non-clickable label between sibling pages, so phase grouping is
> carried entirely by the leading number (1–2 = Phase 1, 3–5 = Phase 2, 6–9 = Phase 3) plus the written
> phase headers on **Start here**. This matches BUILD-GUIDE's tree exactly — no extra page invented to
> fake a divider.

> **Build note — fonts.** Notion pages offer only three page-wide font choices: Default (sans), Serif,
> Mono — no custom font upload, so Bricolage Grotesque and Lora cannot be loaded. Set every page's font
> to **Serif** (closest register to Lora) via the `···` menu → Font. Heading hierarchy comes from
> Notion's built-in H1/H2/H3 sizes, not from Bricolage Grotesque weight/tracking.

---

## Start here

Per BUILD-GUIDE: *"the 4-step card, callout blocks."* Content, pulled from the existing
`customer-docs/WELCOME.md` four-step structure (same copy source used for the spreadsheet's welcome
doc, so the two products read the same):

1. A cover callout: title + tagline (*Planning is a rhythm, not a rule.*)
2. Four numbered callouts, one per step: pick currency & start month → name income & categories → enter
   account balances → add fixed bills once
3. A closing line: *"Then: five minutes, once a week. Add what you spent, look at This month, close the
   page."*
4. The cell-language legend (same block as every other page)
5. A link block to each of the 9 numbered pages, in order (Notion inline page links, not a database)

No database here — this page is static content only.

---

## 1 Set up

**Purpose (spec):** four decisions and two lists, then never opened again.

Contents, top to bottom:

1. Cell-language legend callout
2. **Config** — a database with exactly one row (see `DATABASE-SCHEMAS.md`), showing every `CFG_*`
   value from PLANNER-SPEC-BUDGET.md's "Global setup values" table: currency, locale, year, start
   month, budget method, people, week start, edition. Shown as a **table view with only that one row
   visible** — no "New" affordance needed beyond the one row already there.
3. **Who spends** — the `CFG_PEOPLE` property on the Config row (multi-select, 1–4 names). Not a
   separate database; PLANNER-SPEC-BUDGET.md doesn't ask for one.
4. **Income sources** — a small database (Name *, Amount *, Frequency *, Owner). See "Income sources"
   note in `DATABASE-SCHEMAS.md` — it is not one of the 9 databases this build formally schemas/CSVs,
   because it stays a flat list with no relations or rollups elsewhere in the build.
5. **Categories** — the Categories database (full schema in `DATABASE-SCHEMAS.md`), default view: table,
   grouped by Group, showing Name, Bucket, Monthly target.
6. The copy: *"Ten is plenty. You can add more in month three when you know better."* — keep verbatim,
   it's called out in PLANNER-SPEC-BUDGET.md as deliberate.

> **Build note — the 20-row cap doesn't apply.** PLANNER-SPEC-BUDGET.md caps visible category rows at
> 20 in the spreadsheet with an expandable block. Notion database views scroll natively; there is no
> equivalent cap to build, and none is needed. Keep the "ten is plenty" copy as guidance, not as an
> enforced limit.

Validation ("if any `*` field is empty, show one plain sentence naming it") has no equivalent in Notion
— Notion doesn't support custom validation messages on empty required properties. See
`IMPORT-PROCEDURE.md` for the closest available approximation (a filtered view surfacing incomplete
rows), flagged there as a platform gap, not solved here.

---

## 2 Accounts

**Purpose (spec):** opening balances and where money physically sits.

- **Accounts database** — table view, default sort: Name ascending. Properties per
  `DATABASE-SCHEMAS.md`: Name *, Type, Opening balance *, Last checked, Current balance (formula).
- **Transfers database** — table view, default sort: Date descending. Properties: Date *,
  From account *, To account *, Amount *, Note.

Both databases live on this one page as two separate full-database blocks (not linked views of a
database that lives elsewhere) — Accounts and Transfers are native here.

> The spec's line *"Credit-card payments are recorded here, not as expenses"* is a **process note for
> the buyer**, not a schema element — there is no separate "Credit card payment" type. A credit-card
> payment is simply a Transfers row (from a checking account, to the credit-card account). Repeat this
> exact sentence in the page's intro text so it survives the handoff to Notion, since nothing in the
> schema encodes it structurally.

---

## 3 Add spending

**Purpose (spec):** the one screen touched most; enterable in under 60 seconds.

Per BUILD-GUIDE: one **Transactions** database drives this page (not two separate tables as in the
spreadsheet — see `DATABASE-SCHEMAS.md` for why fixed bills and variable spending share one database in
Notion, with `Fixed` as the switch). Two linked views of it, side by side or stacked:

1. **Fixed bills** view — filter `Fixed = true`, sort by Date ascending, shows Category, Amount,
   Frequency, Date, End date, Account, Bucket, Owner, Paid.
2. **Everything else** view — filter `Fixed = false` (or empty), sort **Date descending** (newest row
   effectively "on top" of the view — see build note below), shows Date, Amount, Category, Account,
   Bucket, Owner, Note.

This is the page's **default view when a buyer opens the duplicated template** — BUILD-GUIDE marks
Transactions' default view as "This week" — so a third, pinned view exists:

3. **This week** (the page-opening default) — filter Date is within the past week, sort Date
   descending, both Fixed and variable rows included, table view.

A toggle for **paycheck view** (period between paydays) is a fourth, buyer-created saved view once they
know their pay dates — PLANNER-SPEC-BUDGET.md describes it as *"a toggle on this screen,"* which in
Notion is most simply a filtered view switch (view tabs across the top of the database block), not a
new database.

> **Build note — "newest row always the entry row" doesn't map to Notion.** The spreadsheet's rule
> (*"the entry row is always the first visible row, no scrolling to the bottom"*) depends on Excel's
> row-insertion behaviour. Notion always adds a new database row at the position the current sort
> implies, and a form/"+New" click doesn't jump the view. Sorting **Date descending** gets newest-dated
> rows to the top, but a row entered today for **today's date** while other rows share today's date will
> land wherever Notion's stable sort puts equal dates, not guaranteed literally first. Flag this as a
> fidelity loss versus the spreadsheet's promise, not something to fake.

> **Build note — fixed-bill recurrence has no native Notion equivalent.** "Entered once, repeat all
> year" is a real spreadsheet mechanic (one row + date maths) with no direct Notion database feature.
> The closest real mechanism: Notion **database templates** support a "Repeat" schedule (e.g. monthly,
> weekly) so that opening/using a template auto-inserts a new page on that cadence. Recommended build:
> create one Transactions template per fixed bill, pre-filled with Category/Amount/Account/Bucket/Owner
> and `Fixed = true`, `Paid` unchecked, with the template's Repeat setting matching that bill's
> Frequency. This is **buyer setup work**, not something the owner's master template can pre-populate,
> since each buyer's actual bills differ. Ship the master page with one worked example template so the
> pattern is visible, documented step by step in `IMPORT-PROCEDURE.md`.

---

## 4 This month  ← the default landing page

**Purpose (spec):** answer "am I okay?" above the fold. Layout must follow PLANNER-SPEC-BUDGET.md's four
sections in order.

**1. Month switcher.** No native Notion widget does this. Build it as a linked view of Transactions (or
of Categories, depending which figure you're driving) with its date filter set to **"Date is within →
This month"** (Notion's relative-date filter), which self-advances every calendar month with no manual
action. This reproduces "one switcher, twelve months behind it" in spirit — the buyer doesn't touch
anything month to month — but there is no literal `< March 2026 >` control to click through history the
way the spreadsheet has. To look at a past month, the buyer temporarily edits that one view's date
filter to a fixed range.

> **Spec gap:** PLANNER-SPEC-BUDGET.md's month switcher is an *interactive* control ("drives every
> figure on the screen"). Notion's relative filters give a **self-updating current month**, not a
> browsable one. Flagging this rather than pretending Notion has month-scrubbing — it doesn't, short of
> the buyer manually editing filters.

**2. Three summary figures** — Left to spend / Spent so far / Saved. Build each as a callout block
whose text is a formula-driven number:
- *Left to spend* and *Spent so far*: rollups off the "This month" Transactions view aren't directly
  quotable inside a callout's static text — Notion callouts don't embed live database values as text.
  Build these instead as a small linked view of a single aggregate: a one-row table (or the Config
  database extended — see `DATABASE-SCHEMAS.md`'s note) is not workable either, since Notion has no
  cross-database single-cell reference. The practical construction: show these two figures as the
  **Sum** shown in the group/footer of the "This month" Transactions linked view itself (Notion table
  views can show a Sum in the column footer), labelled directly above the view rather than inside a
  callout. Do not fake a callout number that cannot actually update.
- *Saved*: same approach — the Sum footer of a Transactions view filtered `Bucket = Save` AND
  `Date is within → This month`.

> **Spec gap — this is a real fidelity loss vs. the spreadsheet.** PLANNER-SPEC-BUDGET.md's "three
> summary figures" are meant to read as three big standalone numbers above the fold (ANTI-AI-CHECKLIST
> even singles this exact layout out: *"kept only on This month, where those three numbers are the
> actual product"*). Notion cannot put a live database aggregate inside free-standing display text or a
> callout — only inside a database view's own footer/rollup. Build the three figures as three small
> single-column linked-database views side by side (each just showing its Sum footer, headers hidden),
> which is the closest visual approximation to three big numbers Notion allows. This is noted explicitly
> rather than silently accepted as "the same," because it isn't — it's a workaround.

- Loud only: the extra line *"17 days — that's €X/day"* and the streak pill under Left to spend are
  **not buildable as live text** for the same reason (no cross-database or computed free text tied to a
  rollup). Show the daily-allowance figure the same way (a linked-view Sum-of-remaining ÷ a manually
  entered "days remaining" number would need its own formula database — out of scope; simplest honest
  build is to omit the per-day figure in Notion and keep it as an xlsx-only feature, flagged here).
  Streak tracking (a weekly logged-transaction streak) has no Notion equivalent database in this build's
  scope either — flagged, not built.

**3. Category breakdown table.** A **linked view of the Categories database**, filtered to none (all
categories always shown, since Notion rollups aren't per-view-filterable to "this month" without the
month-scoping caveat below), columns: Name, Group, Bucket, Planned *(the `Monthly target *` property)*,
Actual, Left, Progress (shown as a Bar). Progress uses Notion's built-in `Show as: Bar` on the formula
property — per BUILD-GUIDE, do not build a fake bar from characters.

> **Spec gap — "Planned" per PLANNER-SPEC-BUDGET.md is described as editable per selected month**
> (*"planned = user input (the only editable column in the table), per category, for the selected
> month"*). BUILD-GUIDE's own Notion schema, by contrast, defines Categories with a single evergreen
> `Monthly target` property, with no month dimension. This document follows BUILD-GUIDE (the
> Notion-specific authority) rather than re-deriving a month-by-category junction database that neither
> source file asks for. **Practical consequence, stated plainly for the owner:** editing "Planned" for
> one category in Notion changes that category's target for every month, past and future — there is no
> per-month override. If the owner wants true per-month planned values in Notion, that needs a new
> junction database (Category × Month) not specified anywhere in the source material — flagged, not
> built silently.

> **Spec gap — "Actual" is a straight rollup (BUILD-GUIDE: "rollup Actual (sum of Transactions)") with
> no month scoping stated.** As written it sums a category's transactions **all-time**, not "for the
> selected month." Two ways to close this, neither confirmed by source material, so both are documented
> rather than one being silently chosen:
> 1. If the buyer's Notion plan supports filtering a rollup itself with a relative-date condition
>    ("Date is within → This month" on the *related* Transactions' Date, inside the rollup's own filter
>    UI), configure the rollup that way — it then self-scopes to the current month with no other action.
> 2. If not available, fall back to a **grouped linked view** of Transactions (group by Category, filter
>    Date within this month, Sum shown per group) placed directly under the Categories table as the
>    real per-month Actual figures, and treat the Categories database's own `Actual` rollup as an
>    **all-time** total instead (relabel its column header "Actual (all-time)" so it isn't misread).
>
> Verify which of the two your Notion workspace supports before committing to the build; do not assume.

**4. Two cards** — Savings goal progress + "One thing to do next."

- *Savings goal progress*: PLANNER-SPEC-BUDGET.md doesn't say which fund shows here if the buyer has
  more than one. Simplest, no-invented-field option: a callout showing the **combined** progress across
  all funds (Sum of Funds.Saved-to-date ÷ Sum of Funds.Target, via the same view-footer technique as
  section 2). If the owner wants a single featured fund instead, that needs a new boolean property on
  Funds (e.g. "Featured") not present in any source file — flagged as an option, not built.
- *"One thing to do next"*: PLANNER-SPEC-BUDGET.md wants a **dynamically generated sentence** — find the
  single largest overspend, phrase it as a suggestion, or fall back to the next unpaid bill. **This
  cannot be built in Notion.** Notion formulas run per-row; nothing in Notion can scan sibling rows,
  find the maximum, and emit a natural-language sentence naming that specific category and amount — that
  requires spreadsheet-style `INDEX/MATCH`/`MAX` cross-row logic with no Notion analogue.
  > **Spec gap, explicitly not built:** the card is instead a **linked view** of Categories, sorted by
  > `Left` ascending (most-negative first), showing only the top row (Name + Left), captioned with the
  > static instruction text below rather than a generated sentence. If that top row's Left is ≥ 0
  > (nobody is over), swap to a second saved view: Transactions filtered `Fixed = true AND Paid = false`,
  > sorted Date ascending, top row only (the next unpaid bill) — the buyer manually checks which of the
  > two views currently applies, since Notion can't conditionally switch views by data either.
  >
  > Calm caption (static, voice-checked): *"The category most over budget is shown below, if any is.
  > Move money toward it, or leave it — both are fine."*
  > Loud caption (static, voice-checked, no emoji, ≤1 exclamation on this screen budget already spent
  > on nothing else, so none used here either): *"Whoever's most over is sitting right below. Shift
  > something their way, or don't — your budget, your call."*

---

## 5 Bills calendar

**Purpose (spec):** see the shape of the month.

- A **Calendar view of Transactions**, filtered `Fixed = true`, per BUILD-GUIDE. Week start follows
  `CFG_WEEK_START` — Notion calendar views start weeks on Sunday or Monday per the workspace's own
  locale setting, not per a value read from the Config database; there is no per-database "week starts
  on" property in Notion. Flag: the buyer sets their **Notion account's** week-start preference to match
  `CFG_WEEK_START` manually; the two aren't linked.
- **Toggle for fixed/variable**: a second calendar view (or the same view's filter switched off) showing
  all Transactions, not only Fixed ones. Two saved calendar views, switched via the view tabs.
- **Right rail**: per PLANNER-SPEC-BUDGET.md, a per-week summary of income, bills, subscriptions, debt,
  left to spend. Build as a column next to the calendar (Notion supports side-by-side columns) holding
  small linked-view Sum footers, one per figure, each filtered to the current week
  (`Date is within → This week`). "Subscriptions" isn't a field anywhere in the schema — categorise
  subscriptions under the existing Category/Group structure (e.g. a "Subscriptions" category inside the
  Life group) rather than inventing a new property; flagged since PLANNER-SPEC-BUDGET.md names
  "subscriptions" as a rail line item without ever defining it as a distinct tagged field.
- **Optional starting-amount input**: a plain number typed directly by the buyer at the top of the rail
  — this is genuinely just a scratch number the buyer keys in each week, not tied to any database; build
  it as a one-line editable text/number block, not a property anywhere.
- **Print-friendly, one month per page**: Notion pages print via the browser's print dialog; there is no
  Notion-native "page break per month" control, since this is a live calendar view, not month-per-sheet
  as in the spreadsheet. No equivalent to build — flagged as an xlsx-only capability.

---

## 6 Year overview

**Purpose (spec):** 12-month × category matrix, budgeted vs. actual toggle, row/column totals, annual
average, plus three optional collapsed panels.

> **Spec gap — Notion has no two-axis pivot/matrix view.** A board, table, calendar, gallery, list,
> timeline, and (where available) chart view all group by **one** property into columns or rows — none
> cross-tabulates category × month with a value in each cell the way a spreadsheet pivot or a grid of
> `SUMIFS` does. This is a genuine Notion ceiling, not a build oversight. The closest honest
> approximation, in order of fidelity:
> 1. A **Board view of Transactions grouped by Category**, with a second, separate **Board view grouped
>    by Month** (a formula property extracting month-year from Date) — two one-dimensional views placed
>    one above the other, each showing per-group Sum. This shows category totals and month totals, but
>    never a single cell for "Food in March."
> 2. For actual category-by-month numbers, twelve small linked views (one per month, grouped by
>    Category, Sum shown) stacked down the page — usable, but visually nothing like a compact matrix,
>    and heavy to maintain.
> Document this limitation for the owner rather than shipping something that looks like a matrix but
> isn't one. Recommend keeping the true year-matrix experience as an xlsx-only capability and describing
> Notion's Year overview as "totals and trends," not "the same grid."

- **Budgeted vs. actual toggle**: two saved views (one summing `Monthly target *`, one summing `Actual`)
  switched via view tabs — buildable, unlike the matrix itself.
- **Row totals / column totals / annual average**: view footers (Sum, Average) on the grouped views
  above — buildable per-group, not as a single combined grid.
- **Three optional panels**, collapsed by default — build each as a Notion **toggle block** (native
  collapse/expand), placed below the main views:
  - *50/30/20 check*: a small linked view of Categories grouped by `Bucket`, Sum of Actual per group,
    compared by eye against the 50/30/20 targets (no automatic pass/fail computed — PLANNER-SPEC-BUDGET
    doesn't specify one).
  - *Income/expense distribution by person*: a linked view of Transactions grouped by `Owner`, Sum shown.
  - *No-spend challenge tracker*: **not specified anywhere in PLANNER-SPEC-BUDGET.md or BUILD-GUIDE.md**
    beyond its name in the "collapsed from 29 tabs" mapping table. No field list, no mechanic, no
    win/loss condition is given.
    > **Spec gap, explicitly unbuilt:** flagging rather than guessing at rules for a challenge tracker
    > that has never been specified. Ship the toggle block as an empty labelled placeholder
    > ("No-spend challenge — mechanic not yet specified") rather than inventing scoring logic.

---

## 7 Goals & savings

- **Funds database** (sinking funds) — table view. Properties per `DATABASE-SCHEMAS.md`.
- **Contributions database** — table view, default sort Date descending, linked to Funds by relation.
- Each Fund row, when opened, shows its related Contributions inline (Notion's relation + linked-view
  pattern) so logging a contribution and seeing the fund's progress happen on one page.

> **Loud only — badge tiers.** Per BUILD-GUIDE: *"Badge images uploaded as image blocks; three per fund,
> the earned ones above the dashed one."* Build: on each Fund's own page, an image block row of three
> badge PNGs (earned-gold, earned-teal, dashed-outline), with the `Tier` formula property (0–3, see
> `DATABASE-SCHEMAS.md`) telling the buyer *which* image should currently be visible — Notion cannot
> conditionally show/hide a static image block based on a formula value, so this is a **manual swap**:
> the buyer (or the owner's master template, per SKU refresh) replaces the image block by hand as tiers
> are earned. Flag this plainly rather than implying it updates itself — BUILD-GUIDE's Excel version
> uses conditional formatting to reveal the right badge automatically; Notion has no equivalent
> conditional-visibility mechanism for blocks.

> **Loud only — celebration on 100%.** A callout block (Yellow/gold tint, per the colour-job mapping),
> containing one line from the celebration copy bank.
> > **Spec gap:** BUILD-GUIDE.md references *"the celebration copy bank"* as the source for this text
> > (also DESIGN-SYSTEM.md section 4: *"one line drawn from the celebration copy bank"*). No such file
> > exists anywhere in this repo at the time of writing. The one confirmed Loud-voice line for a
> > completed savings goal, taken verbatim from `BRAND.md`'s own voice example, is used here as the
> > shipped default: **"Savings goal: done. Go be a person."** If/when the celebration copy bank is
> > produced elsewhere in this project, swap this line for the fund-specific one from that bank.
> This callout is placed **inside the Fund's own page**, revealed (again, manually — same limitation as
> badges) once `Tier = 3`.

**Calm equivalent** (same page, same fund pages, no callout, no badges): per DESIGN-SYSTEM.md, the
Progress formula shown as a Bar reaching 100%, plus the plain words *goal met* as static text placed
next to the bar once it's full — the buyer/owner types this in, since Notion can't conditionally reveal
text either. No colour shift, no confetti, no badges — that restraint is the point, not a build gap.

---

## 8 Debt

- **Debts database** — table view, sorted by the `Order *`-equivalent property (see
  `DATABASE-SCHEMAS.md` — Order is not asterisked in the source spec, kept unasterisked here).
- **Strategy choice** (Snowball / Avalanche / Custom) and **extra monthly payment** are single global
  inputs, not one-per-debt — build as two plain properties on the page itself (a small non-relational
  settings block: a Select and a Number, entered directly as page content, e.g. inside a callout or a
  simple 2-row table), matching how `1 Set up`'s Config row holds single global values. This isn't one
  of the 9 named databases, so it is documented here rather than schema'd separately.

> **Spec gap — "show both payoff dates before the user commits," per-debt payoff month, and total
> interest saved cannot be built as Notion formulas.** Snowball/avalanche payoff dates depend on the
> *cascade*: once one debt is cleared, its payment rolls onto the next debt in Order, which is
> inherently a cross-row, iterative amortization calculation. Notion's formula language has no loops, no
> way for one row's formula to depend on the settled outcome of every row before it, and no way to
> compare two whole-table strategies side by side inside a single property. This is a genuine ceiling,
> not a missing formula.
>
> What **is** buildable per debt, in isolation (ignoring the snowball/avalanche cascade — i.e. as if this
> debt were paid alone with only its own minimum): standard loan-amortization months-to-payoff,
> expressible in Notion formula syntax (Notion's formula language supports `ln`, `pow`, `ceil`):
> ```
> if(
>   prop("APR *") = 0,
>   ceil(prop("Balance *") / prop("Minimum *")),
>   ceil(
>     -ln(1 - (prop("Balance *") * (prop("APR *") / 100 / 12)) / prop("Minimum *"))
>     / ln(1 + (prop("APR *") / 100 / 12))
>   )
> )
> ```
> Label this property **"Months to clear (this debt alone, no snowball)"**, not "Payoff month," so it
> isn't mistaken for the real cross-debt calculation the spreadsheet's Debt Calculator performs.
> Recommend the owner keep the real Snowball-vs-Avalanche comparison and total-interest-saved figure in
> the companion xlsx Debt Calculator sheet, and treat this Notion page as a **tracker and log**, not a
> calculator — stated to the buyer in the page's own intro text.

> **Loud only — cleared-debt celebration.** Per PLANNER-SPEC-BUDGET.md: *"each cleared debt gets a
> celebration moment; grape is the debt colour."* Build: a callout (Purple tint) on each Debt row's own
> page, shown once `Balance * = 0` (manually revealed — same conditional-visibility limitation noted
> above), with one line from the celebration copy bank.
> > **Spec gap:** same missing celebration-copy-bank file noted under Goals & savings. No confirmed
> > debt-specific line exists in any source document. Drafted here, voice-checked against BRAND.md
> > (warm, self-aware, no emoji, no exclamation used since the fund celebration on this build already
> > allows for one and this is a different screen budget), explicitly labelled as a draft pending the
> > real copy bank: *"That one's done. Whatever's next gets the payment it was waiting on."*

---

## 9 Net worth

- **Assets database** — table view. Properties: Name *, Value *, Category.
- **Liabilities database** — table view. Properties: Name *, Balance *.
- A **Net worth** figure: Notion cannot combine two separate databases' sums into one live number
  without a relation between them. Build as two view-footer Sums (Total assets, Total liabilities)
  placed side by side, with the subtraction done as a third, small manually-updated number, OR — cleaner
  — as a one-row helper database identical in shape to Config, holding two rollup-fed relations. Given
  the modest payoff for a single number, the simpler, explicitly-flagged approach is: show both totals
  side by side and let the buyer read the difference, rather than build another cross-database relation
  scaffold for one subtraction.

> **Spec gap — "monthly snapshot log + trend" is required by PLANNER-SPEC-BUDGET.md (screen 9) but is
> not one of the 9 databases this build's task scope names**, so no `net-worth-snapshots.csv` is
> produced and no formal schema is written for it in `DATABASE-SCHEMAS.md`. Flagging rather than
> silently dropping it: Assets and Liabilities as specified hold **current** values only (Notion rollups
> are always live, never historical), so there is no way to see last March's net worth from these two
> databases alone. A real snapshot log needs a small additional database the owner should add if they
> want the trend view — one row per month, with Date, Total assets (typed in, not rolled up — it's a
> point-in-time copy), Total liabilities (typed in), and Net worth (formula: subtraction of the two).
> This is a manual monthly ritual (type in the two current totals once a month), not automatic. Left as
> a recommendation for the owner's own follow-up build, not built here, since it sits outside the task's
> named database list.

- **Optional investment forecast panel**: per spec, *"clearly labelled forecast, not a tracker."* Build
  as a collapsed toggle block containing a plain text/number scratch area (not a database — nothing in
  PLANNER-SPEC-BUDGET.md gives this panel fields to schema), headed literally **"Forecast — not a
  tracker"** so the labelling requirement is met verbatim.
