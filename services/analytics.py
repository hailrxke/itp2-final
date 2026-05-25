from models.transactions import Transaction, Income, Expense

class FinanceAnalyzer:
    def __init__(self, transactions: list[Transaction]):
        self.__transactions = transactions

    def get_transactions(self):
        return self.__transactions
    def set_transactions(self, transactions):
        self.__transactions = transactions

    
    #if there 100000 transactions regular function load all to memory, generator gives one month at time and doesn't store rest
    def monthly_summary(self):
        monthes = {}
        for t in self.get_transactions():
            month = t.date[:7]
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