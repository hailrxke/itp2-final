from models.transactions import Transaction, Income

class FinanceAnalyzer:
    def init(self, transactions: list[Transaction]):
        self.transactions = transactions

    def get_balance(self):
        balance = 0
        for t in self.transactions:
            if isinstance(t, Income):
                balance += t.amount
            else:
                balance -= t.amount
        return balance