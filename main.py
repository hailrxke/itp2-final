from models.transactions import Income, Expense
from models.account import Account
from models.categories import Category


muba = Account(0)
food = Category("food", 1000)
inc1 = Income(100, muba)
inc2 = Income(1000, muba)
exp1 = Expense(500, food, muba)
muba.add_transaction(inc1)
muba.add_transaction(inc2)
muba.add_transaction(exp1)
print(muba.get_balance())
