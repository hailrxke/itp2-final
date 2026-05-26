from models.account import Account
from models.categories import Category
from models.transactions import Expense, Income
from services import storage
from services.analytics import FinanceAnalyzer
from services.storage import load_account_transactions, save_transaction
from utils.decorators import log_execution
from utils.validators import validate_amount, validate_transaction_payload

DEFAULT_CATEGORY_LIMIT = 10_000

account = Account(0)

load_account_transactions(account)
def _get_or_create_category(name):
    categories = account.get_categories()
    if name in categories:
        return categories[name]
    for key, cat in categories.items():
        if key.lower() == name.lower():
            return cat

    category = Category(name, DEFAULT_CATEGORY_LIMIT)
    account.add_category(category)
    return category


def _build_transaction(data):
    amount = data["amount"]
    tx_type = data["type"]

    if tx_type == "income":
        return Income(amount, account)

    category = _get_or_create_category(data["category"])
    return Expense(amount, category, account)


def _read_transaction_input():
    amount = input("Amount: ").strip()
    category = input("Category: ").strip()
    tx_type = input("Type (income/expense): ").strip()
    date = input("Date YYYY-MM-DD (Enter = skip): ").strip()

    payload = {"amount": amount, "category": category, "type": tx_type}
    if date:
        payload["date"] = date
    return payload


def _analyzer() -> FinanceAnalyzer:
    return FinanceAnalyzer(account)


@log_execution
def add_transaction():
    try:
        validated = validate_transaction_payload(_read_transaction_input())
        tx = _build_transaction(validated)
        account.add_transaction(tx)
        print(f"Transaction added. Balance: {account.get_balance()}")
        save_transaction(account)
    except ValueError as exc:
        print(f"Validation error: {exc}")


@log_execution
def show_balance():
    print(f"Current balance: {account.get_balance()}")


@log_execution
def show_json_records():
    records = storage.load_raw_data()
    print(f"Records in JSON: {len(records)}")
    for item in records:
        print(item)


@log_execution
def show_monthly_report():
    analyzer = _analyzer()
    rows = list(analyzer.monthly_summary())

    if not rows:
        print("No transactions yet.")
        return

    for month, summary in rows:
        print(
            f"{month}: income={summary['income']}, "
            f"expenses={summary['expenses']}"
        )


@log_execution
def show_category_breakdown():
    analyzer = _analyzer()
    breakdown = analyzer.category_expenses()

    if not breakdown:
        print("No expenses by category yet.")
        return

    for name, total in breakdown.items():
        print(f"{name}: {total}")


@log_execution
def show_overspending():
    analyzer = _analyzer()
    overspent = analyzer.detect_overspending()

    if not overspent:
        print("No overspending detected.")
        return

    print("Overspent categories:", ", ".join(overspent))

@log_execution
def show_large_expenses():
    raw = input("Minimum amount for large expense: ").strip()
    try:
        threshold = float(validate_transaction_payload(
            {"amount": raw, "category": "x", "type": "expense"}
        )["amount"])
    except ValueError as exc:
        print(f"Validation error: {exc}")
        return

    analyzer = _analyzer()
    large = analyzer.large_expenses(threshold)

    if not large:
        print(f"No expenses greater than {threshold}.")
        return

    for tx in large:
        print(f"{tx.category.get_name()}: {tx.amount}")

@log_execution
def set_category_limit():
    name = input("Category name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        limit = float(validate_amount(input("Spending limit: ").strip()))
    except ValueError as exc:
        print(f"Validation error: {exc}")
        return

    categories = account.get_categories()
    if name in categories:
        categories[name].set_limit(limit)
        print(f"Limit for '{categories[name].get_name()}' set to {limit}")
        return
    for key, cat in categories.items():
        if key.lower() == name.lower():
            cat.set_limit(limit)
            print(f"Limit for '{cat.get_name()}' set to {limit}")
            return

    category = Category(name, limit)
    account.add_category(category)
    print(f"Category '{name}' created with limit {limit}")


def print_menu():
    print("\n=== Personal Finance CLI ===")
    print("1) Add transaction")
    print("2) Show balance")
    print("3) Show JSON records (storage)")
    print("4) Monthly report (analytics)")
    print("5) Category breakdown (analytics)")
    print("6) Detect overspending (analytics)")
    print("7) Large expenses (analytics)")
    print("8) Set category limit")
    print("0) Exit")


def main():
    actions = {
        "1": add_transaction,
        "2": show_balance,
        "3": show_json_records,
        "4": show_monthly_report,
        "5": show_category_breakdown,
        "6": show_overspending,
        "7": show_large_expenses,
        "8": set_category_limit,
    }

    while True:
        print_menu()
        choice = input("Choose action: ").strip()

        if choice == "0":
            save_transaction(account)
            print("Bye!")
            break

        if choice not in actions:
            print("Invalid choice. Try again.")
            continue
        actions[choice]()


if __name__ == "__main__":
    main()
