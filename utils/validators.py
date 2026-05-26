from __future__ import annotations

from datetime import datetime
from decimal import Decimal, InvalidOperation
from typing import Any, Dict, Iterable, Mapping

ALLOWED_TYPES = {"income", "expense"}
MAX_AMOUNT = Decimal("1000000000")  # safety limit


def _to_decimal(value: Any) -> Decimal:
    try:
        return Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError) as exc:
        raise ValueError("Amount must be a valid number.") from exc


def validate_amount(value: Any) -> Decimal:
    """
    Validate that amount is positive and within a safe range.
    Returns Decimal for precise money operations.
    """
    amount = _to_decimal(value)

    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    if amount > MAX_AMOUNT:
        raise ValueError(f"Amount is too large (>{MAX_AMOUNT}).")

    return amount


def validate_category(value: Any, allowed_categories: Iterable[str] | None = None) -> str:
    if not isinstance(value, str):
        raise ValueError("Category must be a string.")

    category = value.strip()
    if not category:
        raise ValueError("Category cannot be empty.")

    if allowed_categories is not None:
        normalized_allowed = {c.strip().lower() for c in allowed_categories if str(c).strip()}
        if category.lower() not in normalized_allowed:
            raise ValueError(f"Category '{category}' is not allowed.")

    return category


def validate_transaction_type(value: Any) -> str:
    if not isinstance(value, str):
        raise ValueError("Transaction type must be a string.")

    tx_type = value.strip().lower()
    if tx_type not in ALLOWED_TYPES:
        raise ValueError(f"Transaction type must be one of: {sorted(ALLOWED_TYPES)}.")

    return tx_type


def validate_date(value: Any, fmt: str = "%Y-%m-%d") -> datetime:
    if not isinstance(value, str):
        raise ValueError("Date must be a string.")

    try:
        return datetime.strptime(value.strip(), fmt)
    except ValueError as exc:
        raise ValueError(f"Date must match format {fmt}.") from exc


def validate_transaction_payload(
    payload: Mapping[str, Any],
    allowed_categories: Iterable[str] | None = None,
) -> Dict[str, Any]:
    """
    Expected payload keys:
      - amount: number-like
      - category: str
      - type: "income" | "expense"
      - date: optional str in YYYY-MM-DD (if absent, caller can set current date)
    """
    if not isinstance(payload, Mapping):
        raise ValueError("Payload must be a mapping/dict.")

    required_fields = ("amount", "category", "type")
    missing = [field for field in required_fields if field not in payload]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}.")

    validated: Dict[str, Any] = {
        "amount": float(validate_amount(payload["amount"])),
        "category": validate_category(payload["category"], allowed_categories),
        "type": validate_transaction_type(payload["type"]),
    }

    if "date" in payload and payload["date"] is not None:
        validated["date"] = validate_date(payload["date"]).strftime("%Y-%m-%d")

    return validated