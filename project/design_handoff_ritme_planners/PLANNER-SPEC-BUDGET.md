# Spec: Het Ritme Budget planner (Calm + Loud)

Nine screens in three phases. Twelve months live behind **one month switcher**, not twelve tabs.
Same architecture for both editions and both formats; only theming and voice differ.

Reference architecture came from a 29-tab competitor workbook. Mapping of what was collapsed is at the
end of this document.

---

## Global setup values (drive everything)

| Name | Type | Notes |
|---|---|---|
`CFG_CURRENCY` | text | Symbol only, e.g. `€`, `$`, `R`, `kr`, `zł`. **Every** display format references this. |
`CFG_LOCALE` | choice | `EU` (1.234,56 / DD-MM-YYYY) or `US` (1,234.56 / MM-DD-YYYY). Drives number + date formats. |
`CFG_YEAR` | int | Budget year |
`CFG_START_MONTH` | choice | Month the plan begins |
`CFG_METHOD` | choice | `Zero-based` or `Carry-over` |
`CFG_PEOPLE` | list | 1–4 names ("spender") |
`CFG_WEEK_START` | choice | Mon / Sun |
`CFG_EDITION` | choice | `Calm` / `Loud` — controls which theme block is active |

Never hardcode a currency symbol anywhere. Number format pattern:
`=CFG_CURRENCY & " " & TEXT(value, chosen_pattern)` or a custom format string built from `CFG_LOCALE`.

---

## PHASE 1 — START (once)

### Screen 1 — Set up
**Purpose:** four decisions and two lists, then never opened again.

Sections, in order:
1. **Basics** — currency `*`, locale, year `*`, start month `*`, budget method `*`
2. **Who spends** — 1–4 names
3. **Income sources** `*` — name, amount, frequency (monthly / 4-weekly / weekly / one-off), owner
4. **Categories** `*` — group (Housing, Food, Transport, Life, Savings, Debt), category name,
   50/30/20 bucket (Need / Want / Save), default monthly target

Constraints: cap the visible category rows at **20** with an expandable block for more. The copy says
"Ten is plenty. You can add more in month three when you know better." — that guidance is deliberate
ADHD design, keep it.

Validation: if any `*` field is empty, the screen shows one plain sentence naming the first missing
field. No error codes.

### Screen 2 — Accounts
**Purpose:** opening balances and where money physically sits.

- **Accounts table**: name `*`, type (Checking / Savings / Cash / Credit card), opening balance `*`,
  last checked date, current balance *(calculated)*
- **Transfers table**: date `*`, from account `*`, to account `*`, amount `*`, note.
  Credit-card payments are recorded here, not as expenses.

Formulas:
```
current_balance = opening_balance
  + SUMIFS(income.amount, income.account, account_name)
  - SUMIFS(spend.amount, spend.account, account_name)
  + SUMIFS(transfers.amount, transfers.to, account_name)
  - SUMIFS(transfers.amount, transfers.from, account_name)
```

---

## PHASE 2 — EVERY WEEK (five minutes)

### Screen 3 — Add spending
**Purpose:** the one screen a user touches most. Must be enterable in under 60 seconds.

Two tables on one screen:

**Fixed bills** (entered once, repeat all year): category `*`, amount `*`, frequency `*`,
first date `*`, end date, account, bucket, owner, paid checkbox per occurrence.

**Everything else** (variable): date `*`, amount `*`, category `*`, account, bucket, owner, note.

Rules:
- Newest row at the top; the entry row is always the first visible row (no scrolling to the bottom)
- 15 blank rows visible; expandable block for more
- Paycheck view = a toggle on this screen (period between paydays), not a separate screen

### Screen 4 — This month  ← the default screen on open
**Purpose:** answer "am I okay?" above the fold.

Layout, top to bottom:
1. **Month switcher** — `< March 2026 >`; drives every figure on the screen
2. **Three summary figures** — Left to spend / Spent so far / Saved
   - Loud additionally shows *"17 days — that's €24/day"* under Left to spend, and a streak pill
3. **Category breakdown table** — Category | Planned `*` | Actual | Left | Progress
4. **Two cards** — Savings goal progress + **One thing to do next**

Formulas (per category, for the selected month):
```
planned         = user input (the only editable column in the table)
actual          = SUMIFS(all_transactions.amount, category, cat, month, sel_month)
left            = planned - actual
progress        = MIN(1, actual / planned)          // guard planned = 0
left_to_spend   = SUM(planned) - SUM(actual)        // Zero-based
                = SUM(planned) - SUM(actual) + prior_month_left   // Carry-over
daily_allowance = left_to_spend / days_remaining_in_month
saved           = SUMIFS(transactions.amount, bucket, "Save", month, sel_month)
```

**One thing to do next** — pick the single largest overspend and phrase it as a suggestion with an
opt-out. Calm: *"Fun money is €41 over. Move it from Transport, or leave it."*
Loud: *"Fun money went €41 over. Honestly? Fine."* + a *Move it from Transport* button.
If nothing is over, show the next unpaid bill instead. Never show an empty card.

### Screen 5 — Bills calendar
**Purpose:** see the shape of the month.

- Month grid, week starts per `CFG_WEEK_START`
- Each day cell lists bills due; toggles for fixed / variable
- Right rail: per-week summary — income, bills, subscriptions, debt, left to spend
- Optional starting amount input at the top of the rail
- Print-friendly: one month per page

---

## PHASE 3 — THE BIG PICTURE (optional)

### Screen 6 — Year overview
- 12-month x category matrix, budgeted vs. actual toggle
- Row totals, column totals, annual average
- **Optional panels** (collapsed by default): 50/30/20 check, income/expense distribution by person,
  no-spend challenge tracker

### Screen 7 — Goals & savings
- **Sinking funds**: goal name `*`, target `*`, monthly target, saved to date, progress, target date
- Contributions log: date `*`, fund `*`, amount `*`
- Loud: badge tiers at 33% / 66% / 100% per fund; celebration card on 100%
- Calm: bar at 100% plus the words *goal met*

### Screen 8 — Debt
- Debts table: name `*`, balance `*`, APR `*`, minimum `*`, custom order
- Strategy choice: Snowball / Avalanche / Custom — **show both payoff dates before the user commits**
- Extra monthly payment input; per-debt payoff month; total interest saved
- Headline: payoff date, recalculated on every payment
- Loud: each cleared debt gets a celebration moment; grape is the debt colour

### Screen 9 — Net worth
- Assets table: name `*`, value `*`, category
- Liabilities table: name `*`, balance `*`
- Monthly snapshot log + trend
- Optional panel: investment forecast (clearly labelled *forecast, not a tracker*)

---

## Collapsed from the 29-tab reference

| Reference tabs | Becomes |
|---|---|
| INSTRUCTIONS | Ships as WELCOME + HOW-TO-NAVIGATE docs, plus a 4-step card on Set up |
| SETUP | Screen 1 |
| BANK ACCOUNTS | Screen 2 |
| RECURRING, PAYMENTS, VARIABLE | Screen 3 (two tables + paid checkboxes) |
| JAN…DEC (12 tabs), PAYCHECK | Screen 4 + month switcher + paycheck toggle |
| CALENDAR | Screen 5 |
| DASHBOARD, ANNUAL TOTALS, 503020, DISTRIBUTION, CHALLENGE | Screen 6 (+ optional panels) |
| SINKING FUNDS | Screen 7 |
| DEBT CALCULATOR | Screen 8 |
| NET WORTH, INVESTMENT | Screen 9 (+ forecast panel) |

Nothing was deleted — everything is reachable, nothing is in the way.
