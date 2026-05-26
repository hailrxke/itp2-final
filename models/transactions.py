from abc import abstractmethod, ABC
from datetime import datetime
from models.categories import Category
from models.interface import Accountable


class Transaction(ABC):
    def __init__(self, amount, account: Accountable):
        self.amount = amount
        self.date = datetime.now().strftime('%Y-%M-%D')
        self.account = account
        if amount < 0:
            raise ValueError(...)

    @abstractmethod
    def apply(self): pass


class Income(Transaction):
    def __init__(self, amount, account: Accountable):
        super().__init__(amount, account)
        self.__name = 'income'

    def apply(self):
        self.account.deposit(self.amount)

    def get_name(self):
        return self.__name


class Expense(Transaction):
    def __init__(self, amount, category: Category, account: Accountable):
        super().__init__(amount, account)
        self.category = category
        category.add_spent(amount)
        self.__name = 'expense'

    def apply(self):
        self.account.withdraw(self.amount)

    def get_name(self):
        return self.__name