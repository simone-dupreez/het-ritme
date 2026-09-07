# Het Ritme Budget — Notion Template Setup

## Instructions
1. Create a new Notion page
2. Duplicate this database structure into your workspace
3. Add your data following the same logic as the Excel version

## Pages to Create

### 1 Set up (Database)
Properties:
- Name (title)
- Value (text)
- Type (select): Currency, Locale, Year, Month, Method

Sample entries:
- Currency: €
- Locale: EU
- Year: 2026
- Start Month: January
- Method: Zero-based

### 2 Accounts (Database)
Properties:
- Account Name (title)
- Type (select): Checking, Savings, Cash, Credit Card
- Opening Balance (number)
- Current Balance (formula): =Opening Balance + Income - Spending

### 3 Add Spending (Database)
Properties:
- Date (date)
- Category (relation to Categories DB)
- Amount (number)
- Account (relation to Accounts DB)
- Bucket (select): Need, Want, Save
- Note (text)

### 4 This Month (Database)
Properties:
- Month (title)
- Category (relation)
- Planned (number)
- Actual (formula): Sum from Add Spending
- Left (formula): Planned - Actual
- Progress (formula): Actual / Planned

### 5 Bills Calendar (Database)
Properties:
- Date (date)
- Bill Name (title)
- Amount (number)
- Category (relation)
- Account (relation)
- Is Fixed (checkbox)

### 6 Year Overview (Database)
Properties:
- Month (title)
- Category (relation)
- Budgeted (number)
- Actual (formula)
- Difference (formula)

### 7 Goals & Savings (Database)
Properties:
- Goal Name (title)
- Target Amount (number)
- Saved So Far (number)
- Progress (formula): Saved / Target
- Target Date (date)

### 8 Debt (Database)
Properties:
- Debt Name (title)
- Balance (number)
- APR (number)
- Minimum Payment (number)
- Strategy (select): Snowball, Avalanche, Custom
- Payoff Date (formula)

### 9 Net Worth (Database)
Properties:
- Date (date)
- Total Assets (number)
- Total Liabilities (number)
- Net Worth (formula): Assets - Liabilities

## Formulas (Notion equivalent)
- Totals: Use rollup properties
- Sums: Use formula or rollup
- Calculations: Use Notion's @-formula syntax

## Views
- Create 9 child pages, one per database
- Each page has database embedded
- Use filtered views for each month, category, etc.
