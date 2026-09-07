# Het Ritme — All Notion Templates

## 1. Budget Planner (Calm & Loud)

### Databases to Create
- **Accounts** (Setup): Currency, Locale, Budget method
- **Income Sources**: Name, Amount, Frequency
- **Categories**: Name, Group, Bucket, Target
- **Transactions**: Date, Category, Amount, Account, Note
- **Monthly Summary**: Month, Category, Planned, Actual, Left
- **Savings Goals**: Name, Target, Saved, Progress
- **Debts**: Name, Balance, APR, Payment
- **Net Worth**: Assets, Liabilities

## 2. Debt Payoff Planner (Calm & Loud)

### Databases to Create
- **Setup**: Currency, Strategy preference
- **Debts**: Name, Balance, APR, Min payment, Status
- **Payoff Strategies**: Snowball vs Avalanche comparison
- **Payment Log**: Date, Debt, Payment amount, New balance
- **Milestones**: Debt cleared, Interest saved

## 3. Meal Planner (Calm & Loud)

### Databases to Create
- **Weekly Plan**: Day, Meal name, Ingredients, Cost, Prep time
- **Shopping List**: Item, Quantity, Cost, Bought (checkbox)
- **Recipes**: Name, Ingredients, Time, Rating, Notes
- **Budget Tracker**: Week, Budget, Spent, Left
- **Meal History**: Date, Meal, Notes for next time

## Setup Instructions

### For Each Planner:
1. Create a new Notion page with the planner name
2. Create each database as a child page
3. Add properties as listed above
4. Create views:
   - Table view (default)
   - Calendar view (for dates)
   - Grouped view (by category/status)
5. Set up formulas for calculations:
   - Sum totals
   - Progress percentages
   - Balance calculations

### Formulas
```
Progress: prop("Saved") / prop("Target")
Left: prop("Planned") - prop("Actual")
Total: sum(prop("Amount"))
```

### For Loud Edition:
- Add celebration callouts for milestones
- Add progress badges at 25%, 50%, 75%, 100%
- Add streak tracking

### For Calm Edition:
- Minimal visual elements
- Focus on data clarity
- Quiet color palette

