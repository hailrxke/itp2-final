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