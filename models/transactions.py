from abc import abstractmethod, ABC
# from models.account import Account
from datetime import datetime


class Transaction(ABC):
    def __init__(self, amount, category, account: "Account"):
        self.amount = amount
        self.date = datetime.now()
        self.category = category
        self.account = account

    @abstractmethod
    def apply(self):
        pass


class Income(Transaction):
    def __init__(self, amount, category, account: "Account"):
        if amount < 0:
            raise ValueError(...)
        super().__init__(amount, category, account)

    def apply(self):
        self.account.deposit(self.amount)


class Expense(Transaction):
    def __init__(self, amount, category, account: "Account"):
        if amount < 0:
            raise ValueError(...)
        super().__init__(amount, category, account)

    def apply(self):
        self.account.withdraw(self.amount)
