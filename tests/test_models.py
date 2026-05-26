from models.transactions import Income, Expense
from models.categories import Category
from models.account import Account
import pytest


class TestCategory:
    def test_create(self):
        c = Category("food", 10000)
        assert c.get_name() == "food"
        assert c.get_limit() == 10000
        assert c.get_spent() == 0

    def test_negative_limit_raises(self):
        with pytest.raises(ValueError):
            Category("food", -1)

    def test_add_spent(self):
        c = Category("food", 10000)
        c.add_spent(500)
        c.add_spent(300)
        assert c.get_spent() == 800

    def test_set_limit(self):
        c = Category("food", 10000)
        c.set_limit(5000)
        assert c.get_limit() == 5000

    def test_set_negative_limit_raises(self):
        c = Category("food", 10000)
        with pytest.raises(ValueError):
            c.set_limit(-100)

    def test_set_name(self):
        c = Category("food", 10000)
        c.set_name("groceries")
        assert c.get_name() == "groceries"


class TestAccount:
    def test_initial_balance(self):
        acc = Account(1000)
        assert acc.get_balance() == 1000

    def test_deposit(self):
        acc = Account(1000)
        acc.deposit(500)
        assert acc.get_balance() == 1500

    def test_withdraw(self):
        acc = Account(1000)
        acc.withdraw(300)
        assert acc.get_balance() == 700

    def test_deposit_negative_raises(self):
        acc = Account(1000)
        with pytest.raises(ValueError):
            acc.deposit(-100)

    def test_withdraw_negative_raises(self):
        acc = Account(1000)
        with pytest.raises(ValueError):
            acc.withdraw(-100)

    def test_add_category(self):
        acc = Account(1000)
        food = Category("food", 5000)
        acc.add_category(food)
        assert "food" in acc.get_categories()

    def test_add_category_stored_by_name(self):
        acc = Account(1000)
        food = Category("food", 5000)
        acc.add_category(food)
        assert acc.get_categories()["food"] is food

    def test_transactions_initially_empty(self):
        acc = Account(1000)
        assert acc.get_transactions() == []


class TestIncome:
    def test_apply_increases_balance(self):
        acc = Account(1000)
        inc = Income(500, acc)
        acc.add_transaction(inc)
        assert acc.get_balance() == 1500

    def test_negative_amount_raises(self):
        acc = Account(1000)
        with pytest.raises(ValueError):
            Income(-100, acc)

    def test_get_name(self):
        acc = Account(1000)
        inc = Income(500, acc)
        assert inc.get_name() == "income"

    def test_stored_in_transactions(self):
        acc = Account(1000)
        inc = Income(500, acc)
        acc.add_transaction(inc)
        assert inc in acc.get_transactions()

    def test_date_set(self):
        acc = Account(1000)
        inc = Income(500, acc)
        assert inc.date is not None


class TestExpense:
    def test_apply_decreases_balance(self):
        acc = Account(1000)
        food = Category("food", 5000)
        exp = Expense(300, food, acc)
        acc.add_transaction(exp)
        assert acc.get_balance() == 700

    def test_apply_updates_category_spent(self):
        acc = Account(1000)
        food = Category("food", 5000)
        exp = Expense(300, food, acc)
        acc.add_transaction(exp)
        assert food.get_spent() == 300

    def test_negative_amount_raises(self):
        acc = Account(1000)
        food = Category("food", 5000)
        with pytest.raises(ValueError):
            Expense(-100, food, acc)

    def test_get_name(self):
        acc = Account(1000)
        food = Category("food", 5000)
        exp = Expense(300, food, acc)
        assert exp.get_name() == "expense"

    def test_stored_in_transactions(self):
        acc = Account(1000)
        food = Category("food", 5000)
        exp = Expense(300, food, acc)
        acc.add_transaction(exp)
        assert exp in acc.get_transactions()

    def test_multiple_expenses_accumulate_spent(self):
        acc = Account(5000)
        food = Category("food", 5000)
        acc.add_transaction(Expense(300, food, acc))
        acc.add_transaction(Expense(200, food, acc))
        assert food.get_spent() == 500


class TestMixed:
    def test_income_and_expense(self):
        acc = Account(1000)
        food = Category("food", 5000)
        acc.add_transaction(Income(2000, acc))
        acc.add_transaction(Expense(500, food, acc))
        assert acc.get_balance() == 2500

    def test_multiple_transactions_stored(self):
        acc = Account(1000)
        food = Category("food", 5000)
        inc = Income(500, acc)
        exp = Expense(200, food, acc)
        acc.add_transaction(inc)
        acc.add_transaction(exp)
        assert len(acc.get_transactions()) == 2
