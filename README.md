# itp2-final        Personal Finance Tracker

## Participants:
1. Bolat Mubarak - Models ('transaction.py', 'categories.py', 'accounts.py' and interface Accountable)
2. Seitmukhambetov Alikhan - Analytic Block (Class Finance Analyzer with 'monthly_summary', 'category_expenses', 'detect_overspending', and 'large_expenses' methods), Tests for Finance Analyzer
3. Yesenaliev Arystanali - Storage Block ('storage.py', 'transactions.json')
4. Tselichshev Maxim - Utils Module ('@log_execution' decorator, 'validators.py')

## Project Structure:
itp2-final-1/
├── main.py              # CLI Menu
├── models/
│   ├── account.py
│   ├── categories.py
│   ├── interface.py     # Accountable
│   └── transactions.py  
├── services/
│   ├── storage.py       # JSON
│   └── analytics.py     # FinanceAnalyzer
├── utils/
│   ├── validators.py    
│   └── decorators.py    # @log_execution
├── data/
│   └── transactions.json
└── tests/
    ├── test_validators.py
    └── test_analytics.py

## Example of Program Execution


'=== Personal Finance CLI ===
1) Add transaction
2) Show balance
3) Show JSON records (storage)
4) Monthly report (analytics)
5) Category breakdown (analytics)
6) Detect overspending (analytics)
7) Large expenses (analytics)
8) Set category limit
0) Exit
Choose action: 2
[LOG] Start: show_balance
Current balance: 134006
[LOG] Done: show_balance (0.0001s)

=== Personal Finance CLI ===
1) Add transaction
2) Show balance
3) Show JSON records (storage)
4) Monthly report (analytics)
5) Category breakdown (analytics)
6) Detect overspending (analytics)
7) Large expenses (analytics)
8) Set category limit
0) Exit
Choose action: 3
[LOG] Start: show_json_records
Records in JSON: 15
{'amount': 41898, 'category': 'stipend', 'type': 'income', 'date': '2026-01-12'}
{'amount': 4500, 'category': 'food', 'type': 'expense', 'date': '2026-01-15'}
{'amount': 90, 'category': 'transport', 'type': 'expense', 'date': '2026-01-16'}
{'amount': 15000, 'category': 'freelance', 'type': 'income', 'date': '2026-01-20'}
{'amount': 12000, 'category': 'entertainment', 'type': 'expense', 'date': '2026-01-25'}
{'amount': 3200, 'category': 'food', 'type': 'expense', 'date': '2026-02-02'}
{'amount': 41898, 'category': 'stipend', 'type': 'income', 'date': '2026-02-12'}
{'amount': 3400, 'category': 'health', 'type': 'expense', 'date': '2026-02-14'}
{'amount': 500, 'category': 'transport', 'type': 'expense', 'date': '2026-02-18'}
{'amount': 15000, 'category': 'food', 'type': 'expense', 'date': '2026-02-23'}
{'amount': 3500, 'category': 'entertainment', 'type': 'expense', 'date': '2026-03-01'}
{'amount': 80000, 'category': 'freelance', 'type': 'income', 'date': '2026-03-05'}
{'amount': 1200, 'category': 'other', 'type': 'expense', 'date': '2026-03-10'}
{'amount': 950, 'category': 'food', 'type': 'expense', 'date': '2026-03-12'}
{'amount': 450, 'category': 'transport', 'type': 'expense', 'date': '2026-03-15'}
[LOG] Done: show_json_records (0.0026s)

=== Personal Finance CLI ===
1) Add transaction
2) Show balance
3) Show JSON records (storage)
4) Monthly report (analytics)
5) Category breakdown (analytics)
6) Detect overspending (analytics)
7) Large expenses (analytics)
8) Set category limit
0) Exit
Choose action: 1
[LOG] Start: add_transaction
Amount: 4000
Category: freelance
Type (income/expense): income
Date YYYY-MM-DD (Enter = skip): 
Transaction added. Balance: 138006.0
[LOG] Done: add_transaction (11.1142s)

=== Personal Finance CLI ===
1) Add transaction
2) Show balance
3) Show JSON records (storage)
4) Monthly report (analytics)
5) Category breakdown (analytics)
6) Detect overspending (analytics)
7) Large expenses (analytics)
8) Set category limit
0) Exit
Choose action: 8
[LOG] Start: set_category_limit
Category name: food
Spending limit: 250
Limit for 'food' set to 250.0
[LOG] Done: set_category_limit (12.7677s)

=== Personal Finance CLI ===
1) Add transaction
2) Show balance
3) Show JSON records (storage)
4) Monthly report (analytics)
5) Category breakdown (analytics)
6) Detect overspending (analytics)
7) Large expenses (analytics)
8) Set category limit
0) Exit
Choose action: 1
[LOG] Start: add_transaction
Amount: 490
Category: food
Type (income/expense): expense
Date YYYY-MM-DD (Enter = skip): 
Transaction added. Balance: 137516.0
[LOG] Done: add_transaction (11.1732s)

=== Personal Finance CLI ===
1) Add transaction
2) Show balance
3) Show JSON records (storage)
4) Monthly report (analytics)
5) Category breakdown (analytics)
6) Detect overspending (analytics)
7) Large expenses (analytics)
8) Set category limit
0) Exit
Choose action: 6
[LOG] Start: show_overspending
Overspent categories: food, transport, entertainment, health, other
[LOG] Done: show_overspending (0.0002s)

=== Personal Finance CLI ===
1) Add transaction
2) Show balance
3) Show JSON records (storage)
4) Monthly report (analytics)
5) Category breakdown (analytics)
6) Detect overspending (analytics)
7) Large expenses (analytics)
8) Set category limit
0) Exit
Choose action: 4
[LOG] Start: show_monthly_report
2026-05: income=182796.0, expenses=45280.0
[LOG] Done: show_monthly_report (0.0003s)

=== Personal Finance CLI ===
1) Add transaction
2) Show balance
3) Show JSON records (storage)
4) Monthly report (analytics)
5) Category breakdown (analytics)
6) Detect overspending (analytics)
7) Large expenses (analytics)
8) Set category limit
0) Exit
Choose action: 5
[LOG] Start: show_category_breakdown
food: 24140.0
transport: 1040
entertainment: 15500
health: 3400
other: 1200
[LOG] Done: show_category_breakdown (0.0002s)

=== Personal Finance CLI ===
1) Add transaction
2) Show balance
3) Show JSON records (storage)
4) Monthly report (analytics)
5) Category breakdown (analytics)
6) Detect overspending (analytics)
7) Large expenses (analytics)
8) Set category limit
0) Exit
Choose action: 6
[LOG] Start: show_overspending
Overspent categories: food, transport, entertainment, health, other
[LOG] Done: show_overspending (0.0001s)

=== Personal Finance CLI ===
1) Add transaction
2) Show balance
3) Show JSON records (storage)
4) Monthly report (analytics)
5) Category breakdown (analytics)
6) Detect overspending (analytics)
7) Large expenses (analytics)
8) Set category limit
0) Exit
Choose action: 7
[LOG] Start: show_large_expenses
Minimum amount for large expense: 15000
No expenses greater than 15000.0.
[LOG] Done: show_large_expenses (7.9769s)

=== Personal Finance CLI ===
1) Add transaction
2) Show balance
3) Show JSON records (storage)
4) Monthly report (analytics)
5) Category breakdown (analytics)
6) Detect overspending (analytics)
7) Large expenses (analytics)
8) Set category limit
0) Exit
Choose action: 7
[LOG] Start: show_large_expenses
Minimum amount for large expense: 3500
food: 4500
entertainment: 12000
food: 15000
[LOG] Done: show_large_expenses (3.3966s)'
