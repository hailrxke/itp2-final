import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'transactions.json')

import json
import os

from models.account import Account
from models.categories import Category
from models.transactions import Income, Expense

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'transactions.json')

def load_raw_data() -> list:
    if not os.path.exists(DB_PATH):
        return []
    try:
        with open(DB_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def load_account_transactions(account: Account) -> None:
    for transaction in load_raw_data():
        account.add_category(Category(transaction.get('category'), 0))
        if transaction.get('type') == 'income':
            account.add_transaction(Income(transaction.get('amount'), account))
        elif transaction.get('type') == 'expense':
            account.add_transaction(Expense(transaction.get('amount'), account.get_categories()[transaction.get('category')], account))


