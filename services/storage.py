import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'transactions.json')

def load_raw_data() -> list:
    if not os.path.exists(DB_PATH):
        return []
    try:
        with open(DB_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_raw_data(data: list) -> bool:
    try:
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        with open(DB_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print(f"Recording Error: {e}")
        return False

def add_transaction_to_storage(transaction_dict: dict):
    current_data = load_raw_data()
    current_data.append(transaction_dict)
    save_raw_data(current_data)

def get_transactions_by_category() -> dict:
    transactions = load_raw_data()
    category_map = {}
    for t in transactions:
        cat = t.get("category", "income")
        if cat not in category_map:
            category_map[cat] = []
        category_map[cat].append(t)
    return category_map

