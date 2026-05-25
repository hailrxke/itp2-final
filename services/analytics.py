from models.transactions import Transaction, Income

class FinanceAnalyzer:
    def __init__(self, transactions: list[Transaction]):
        self.__transactions = transactions

    def get_transactions(self):
        return self.__transactions

    
    #if there 100000 transactions regular function load all to memory, generator gives one month at time and doesn't store rest
    def monthly_summary(self):
        monthes = {}
        for t in self.get_transactions():
            month = t.date[:7]
            if month not in monthes:
                monthes[month] = {"income": 0, "expenses": 0}
            if t.type == Income:
                    monthes[month]["income"] += t.amount
            else:
                    monthes[month]["expenses"] += t.amount
        for month, summary in monthes.items():
            yield month, summary
