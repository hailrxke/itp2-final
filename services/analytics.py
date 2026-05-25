from models.account import Account
from models.transactions import Expense, Income

class FinanceAnalyzer:
    def __init__(self, account: Account):
        self.__account = account

    def get_transactions(self):
        return self.__account.get_transactions()
    def get_categories(self):
        return self.__account.get_categories()

    
    #if there 100000 transactions regular function load all to memory, generator gives one month at time and doesn't store rest
    def monthly_summary(self):
        monthes = {}
        for t in self.get_transactions():
            month = t.date.strftime("%Y-%m")
            if month not in monthes:
                monthes[month] = {"income": 0, "expenses": 0}
            if isinstance(t, Income):
                monthes[month]["income"] += t.amount
            else:
                monthes[month]["expenses"] += t.amount
        for month, summary in monthes.items():
            yield month, summary

    def category_expenses(self):
        expenses = {}
        for t in self.get_transactions():
            if isinstance(t, Expense):
                name = t.category.get_name()
                if name not in expenses:
                    expenses[name] = 0
                expenses[name] += t.amount
        return expenses
    
    def detect_overspending(self):
        expenses = self.category_expenses()
        result = []
        for c in self.get_categories():
            name = c.get_name()
            if name in expenses:
                if expenses[name] > c.get_limit():
                    result.append(name)
        return result
    
    #you can find expenses that exceed a certain amount
    def large_expenses(self, expense):
        return list(filter(lambda t: isinstance(t, Expense) and t.amount > expense, self.get_transactions()))
