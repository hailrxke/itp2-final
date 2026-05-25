from abc import abstractmethod, ABC
from datetime import datetime
from models.categories import Category
from models.interface import Accountable


class Transaction(ABC):
    def __init__(self, amount, account: Accountable):
        self.amount = amount
        self.date = datetime.now()
        self.account = account
        if amount < 0:
            raise ValueError(...)

    @abstractmethod
    def apply(self): pass


class Income(Transaction):
    def __init__(self, amount, account: Accountable):
        super().__init__(amount, account)

    def apply(self):
        self.account.deposit(self.amount)


class Expense(Transaction):
    def __init__(self, amount, category: Category, account: Accountable):
        super().__init__(amount, account)
        self.category = category
        category.add_spent(amount)

    def apply(self):
        self.account.withdraw(self.amount)
