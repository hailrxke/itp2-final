from __future__ import annotations

from typing import Callable, Dict, Optional

from models.account import Account
from models.transactions import Expense, Income
from services import storage
from utils.decorators import log_execution
from utils.validators import validate_transaction_payload

account = Account(0)


def _build_transaction(data: dict):
    amount = data["amount"]
    category = data["category"]
    tx_type = data["type"]

    if tx_type == "income":
        return Income(amount, category, account)
    return Expense(amount, category, account)


def _read_transaction_input() -> dict:
    amount = input("Amount: ").strip()
    category = input("Category: ").strip()
    tx_type = input("Type (income/expense): ").strip()
    date = input("Date YYYY-MM-DD (Enter = today): ").strip()

    payload = {"amount": amount, "category": category, "type": tx_type}
    if date:
        payload["date"] = date
    return payload


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
    # TODO: подключить FinanceAnalyzer.monthly_summary() Alikhan
    print("Monthly report: waiting for analytics module.")


@log_execution
def show_category_breakdown() -> None:
    # TODO: подключить FinanceAnalyzer.category_breakdown() Alikhan
    print("Category breakdown: waiting for analytics module.")


@log_execution
def show_overspending() -> None:
    # TODO: подключить FinanceAnalyzer.detect_overspending()
    print("Overspending check: waiting for analytics module.")


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