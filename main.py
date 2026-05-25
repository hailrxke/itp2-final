from __future__ import annotations

from typing import Callable, Dict, Optional

from models.account import Account
from models.categories import Category
from models.transactions import Expense, Income
from services import storage
from services.analytics import FinanceAnalyzer
from utils.decorators import log_execution
from utils.validators import validate_transaction_payload

DEFAULT_CATEGORY_LIMIT = 10_000

account = Account(0)


def _get_or_create_category(name: str) -> Category:
    for cat in account.get_categories():
        if cat.get_name().lower() == name.lower():
            return cat

    category = Category(name, DEFAULT_CATEGORY_LIMIT)
    account.add_category(category)
    return category


def _build_transaction(data: dict):
    amount = data["amount"]
    tx_type = data["type"]

    if tx_type == "income":
        return Income(amount, account)

    category = _get_or_create_category(data["category"])
    return Expense(amount, category, account)


def _read_transaction_input() -> dict:
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
def add_transaction() -> None:
    try:
        validated = validate_transaction_payload(_read_transaction_input())
        tx = _build_transaction(validated)
        account.add_transaction(tx)
        print(f"Transaction added. Balance: {account.get_balance()}")
    except ValueError as exc:
        print(f"Validation error: {exc}")


@log_execution
def show_balance() -> None:
    print(f"Current balance: {account.get_balance()}")


@log_execution
def show_json_records() -> None:
    records = storage.load_raw_data()
    print(f"Records in JSON: {len(records)}")
    for item in records:
        print(item)


@log_execution
def show_monthly_report() -> None:
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
def show_category_breakdown() -> None:
    analyzer = _analyzer()
    breakdown = analyzer.category_expenses()

    if not breakdown:
        print("No expenses by category yet.")
        return

    for name, total in breakdown.items():
        print(f"{name}: {total}")


@log_execution
def show_overspending() -> None:
    analyzer = _analyzer()
    overspent = analyzer.detect_overspending()

    if not overspent:
        print("No overspending detected.")
        return

    print("Overspent categories:", ", ".join(overspent))


def print_menu() -> None:
    print("\n=== Personal Finance CLI ===")
    print("1) Add transaction")
    print("2) Show balance")
    print("3) Show JSON records (storage)")
    print("4) Monthly report (analytics)")
    print("5) Category breakdown (analytics)")
    print("6) Detect overspending (analytics)")
    print("0) Exit")


def main() -> None:
    handlers: Dict[str, Callable[[], None]] = {
        "1": add_transaction,
        "2": show_balance,
        "3": show_json_records,
        "4": show_monthly_report,
        "5": show_category_breakdown,
        "6": show_overspending,
    }

    while True:
        print_menu()
        choice = input("Choose action: ").strip()

        if choice == "0":
            print("Bye!")
            break

        handler: Optional[Callable[[], None]] = handlers.get(choice)
        if handler is None:
            print("Invalid choice. Try again.")
            continue

        handler()


if __name__ == "__main__":
    main()
