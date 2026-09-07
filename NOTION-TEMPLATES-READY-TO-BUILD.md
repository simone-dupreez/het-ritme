# Het Ritme Notion Templates — Ready to Build & Duplicate

## Quick Start: Copy-Paste Method

These templates are designed to be built in Notion in ~15-20 minutes per planner.

---

## 1. BUDGET PLANNER (Calm & Loud)

### Step 1: Create Main Page
1. Create new page: "Het Ritme Budget — Calm" (or Loud)
2. Add cover image: Use `brand/het-ritme-lockup-stacked-calm.svg` (or loud)
3. Add icon: Use mark (the ring)
4. Add intro text:
   > "Planning is a rhythm, not a rule. Nine screens, one system. Your rhythm."

### Step 2: Create Child Databases

#### Database 1: Setup
- Create child database called "Setup"
- Properties:
  - Name (title)
  - Value (text)
  - Type (select): Currency, Locale, Year, Month, Method

Entries:
```
Currency: €
Locale: EU
Year: 2026
Start Month: January
Budget Method: Zero-based
```

#### Database 2: Accounts
- Create child database called "Accounts"
- Properties:
  - Account Name (title)
  - Type (select): Checking, Savings, Cash, Credit Card
  - Opening Balance (number)
  - Current Balance (formula): =prop("Opening Balance") + 5000 - 3000

Entries:
```
Checking | Checking | 2000
Savings | Savings | 5000
Cash | Cash | 300
```

#### Database 3: Categories
- Create child database called "Categories"
- Properties:
  - Name (title)
  - Group (select): Housing, Food, Transport, Life, Savings, Debt
  - Bucket (select): Need, Want, Save
  - Monthly Target (number)

Entries:
```
Rent | Housing | Need | 1200
Groceries | Food | Need | 400
Transport | Transport | Need | 200
Entertainment | Life | Want | 300
Savings | Savings | Save | 500
```

#### Database 4: Transactions
- Create child database called "Transactions"
- Properties:
  - Date (date)
  - Category (relation to Categories)
  - Amount (number)
  - Account (relation to Accounts)
  - Bucket (select): Need, Want, Save
  - Note (text)

Sample entries:
```
2026-03-01 | Groceries | 45 | Checking | Need
2026-03-02 | Transport | 15 | Cash | Need
2026-03-03 | Entertainment | 30 | Checking | Want
```

#### Database 5: Monthly Summary
- Create child database called "Monthly Summary"
- Properties:
  - Month (title, date)
  - Category (relation to Categories)
  - Planned (number)
  - Actual (rollup: sum of amounts from Transactions)
  - Left (formula): =prop("Planned") - prop("Actual")
  - Progress (formula): =prop("Actual") / prop("Planned")

#### Database 6: Savings Goals
- Create child database called "Savings Goals"
- Properties:
  - Goal Name (title)
  - Target Amount (number)
  - Saved So Far (number)
  - Progress % (formula): =prop("Saved So Far") / prop("Target Amount")
  - Target Date (date)

Sample:
```
Emergency Fund | 10000 | 5000
Holiday | 2000 | 500
```

#### Database 7: Debts
- Create child database called "Debts"
- Properties:
  - Debt Name (title)
  - Balance (number)
  - APR % (number)
  - Minimum Payment (number)
  - Payoff Months (formula): =prop("Balance") / prop("Minimum Payment")

Sample:
```
Credit Card | 5000 | 18.9 | 150
Student Loan | 15000 | 4.5 | 250
```

#### Database 8: Net Worth
- Create child database called "Net Worth"
- Properties:
  - Date (date)
  - Assets (rollup: sum from Accounts where type = savings/checking)
  - Liabilities (rollup: sum from Debts)
  - Net Worth (formula): =prop("Assets") - prop("Liabilities")

### Step 3: Create Views
For each database, create:
1. Table view (default)
2. Calendar view (for dates if applicable)
3. Grouped view (by category/status)

---

## 2. DEBT PAYOFF PLANNER (Calm & Loud)

### Step 1: Create Main Page
- Page name: "Het Ritme Debt — Buster" (Calm) or "Crusher" (Loud)
- Tagline: "One payoff date, recalculated every time"

### Step 2: Create Databases

#### Database 1: Your Debts
- Name (title)
- Balance (number)
- APR (number)
- Minimum Payment (number)
- Status (select): Active, Paid Off

#### Database 2: Payment Log
- Date (date)
- Debt (relation to Your Debts)
- Payment Amount (number)
- New Balance (number)
- Interest Paid (formula)

#### Database 3: Payoff Comparison
- Debt (relation)
- Snowball Months (formula)
- Avalanche Months (formula)
- Interest Saved (formula)

#### Database 4: Milestones
- Date (date)
- Milestone (select): Debt cleared, Interest saved X
- Amount/Impact (text)
- Celebrated? (checkbox) ← *For Loud edition*

---

## 3. MEAL PLANNER (Calm & Loud)

### Step 1: Create Main Page
- Page name: "Meal Planner for One" (Calm) or "Cooking, Actually" (Loud)
- Tagline: "4 nights planned, 3 free"

### Step 2: Create Databases

#### Database 1: Weekly Plan
- Day (date)
- Meal Name (title)
- Ingredients (text)
- Cost (number)
- Prep Time (text)
- Notes (text)

Entries:
```
Monday | Lemon Orzo | Pasta, lemon, veg | 8
Tuesday | Leftovers | From Monday | 0
Wednesday | Miso Salmon | Salmon, miso, rice | 12
Thursday | Out | Restaurant | 15
```

#### Database 2: Shopping List
- Item (title)
- Quantity (text)
- Cost (number)
- Bought? (checkbox)
- Category (select): Produce, Protein, Pantry, Dairy

#### Database 3: Recipes
- Recipe Name (title)
- Ingredients (text)
- Cook Time (text)
- Difficulty (select): Easy, Medium, Hard
- Rating (select): ⭐ to ⭐⭐⭐⭐⭐
- Notes (text)

#### Database 4: Meal History
- Date (date)
- Meal (relation to Recipes)
- Rating (select)
- Notes for Next Time (text)

---

## Customization for Calm vs Loud

### Calm Edition
- Minimal colors: Use ink `#262119` for text, paper `#F6F2E9` background
- No emojis in database titles
- Clean, minimal callouts
- Focus on data clarity
- Quiet language in descriptions

### Loud Edition
- Add celebration callouts:
  - At 25%, 50%, 75%, 100% progress
  - When a debt clears
  - When weekly meal plan is complete
- Use accent color `#D65A34` for highlights
- Add emoji to titles: 🎯 Goals, 🎉 Milestones, 🍽️ Meals
- Warmer language in descriptions
- Add "Streak" property to track consecutive weeks

---

## Sharing & Duplicating

To share these templates with customers:

1. Build each planner completely
2. In Notion, click **Share** → **Copy link**
3. Select **Duplicate** option
4. Share the link with customers
5. They click → Notion opens → "Duplicate to workspace" button
6. Template appears in their Notion workspace ready to use

---

## Files to Reference While Building

- `design-tokens.json` — Colors and settings
- `project/design_handoff_ritme_planners/BRAND.md` — Voice guidelines
- `project/design_handoff_ritme_planners/PLANNER-SPEC-BUDGET.md` — Complete spec

