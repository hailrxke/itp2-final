from abc import abstractmethod, ABC
from account import Account
from datetime import datetime


class Transaction(ABC):
    def __init__(self, amount, category):
        self.amount = amount
        self.date = datetime.now()
        self.category = category

    @abstractmethod
    def apply(self):
        pass


class Income(Transaction):
    def __init__(self, amount, category):
        if amount < 0:
            raise ValueError(...)
        super().__init__(amount, category)

    def apply(self, account: Account):
        account.deposit(self.amount)


class Expence(Transaction):
    def __init__(self, amount, category):
        if amount > 0:
            raise ValueError(...)
        super().__init__(amount, category)

    def apply(self, account: Account):
        account.withdraw(self.amount)
