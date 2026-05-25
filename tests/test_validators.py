import pytest

from utils.validators import (
    validate_amount,
    validate_category,
    validate_date,
    validate_transaction_payload,
    validate_transaction_type,
)


def test_validate_amount_ok():
    assert validate_amount("100") == pytest.approx(100, rel=1e-9) or validate_amount("100") == 100


def test_validate_amount_negative():
    with pytest.raises(ValueError, match="greater than zero"):
        validate_amount(-5)


def test_validate_category_empty():
    with pytest.raises(ValueError, match="empty"):
        validate_category("   ")


def test_validate_transaction_type_invalid():
    with pytest.raises(ValueError, match="Transaction type"):
        validate_transaction_type("transfer")


def test_validate_date_format():
    dt = validate_date("2026-05-20")
    assert dt.year == 2026 and dt.month == 5 and dt.day == 20


def test_validate_payload_full():
    result = validate_transaction_payload(
        {"amount": "50", "category": "food", "type": "expense", "date": "2026-01-15"}
    )
    assert result["amount"] == 50.0
    assert result["category"] == "food"
    assert result["type"] == "expense"
    assert result["date"] == "2026-01-15"