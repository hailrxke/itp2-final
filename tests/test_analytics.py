from models.transactions import Income, Expense
from models.account import Account
from models.categories import Category
from services.analytics import FinanceAnalyzer

def test_category_expenses():
    user = Account(0)
    phone = Category("Phone", 500)
    exp = Expense(200, phone, user)
    user.add_transaction(exp)
    user.add_category(phone)
    analyzer = FinanceAnalyzer(user)
    
    result = analyzer.category_expenses()
    assert result == {"Phone": 200}

def test_monthly_summary():
    user = Account(0)
    phone = Category("Phone", 500)
    exp = Expense(200, phone, user)
    user.add_category(phone)
    user.add_transaction(exp)
    analyzer = FinanceAnalyzer(user)
    
    result = list(analyzer.monthly_summary())
    assert len(result) > 0

def test_detect_overspending():
    user = Account(0)
    phone = Category("Phone", 500)
    exp = Expense(600, phone, user)
    user.add_category(phone)
    user.add_transaction(exp)
    analyzer = FinanceAnalyzer(user)
    
    result = analyzer.detect_overspending()
    assert "Phone" in result

def test_large_expenses():
    user = Account(0)
    phone = Category("Phone", 500)
    exp1 = Expense(200, phone, user)
    exp2 = Expense(800, phone, user)
    user.add_transaction(exp1)
    user.add_transaction(exp2)
    analyzer = FinanceAnalyzer(user)
    
    result = analyzer.large_expenses(500)
    assert len(result) == 1
    assert result[0].amount == 800