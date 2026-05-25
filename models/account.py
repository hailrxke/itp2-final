from models.transactions import Transaction
from models.categories import Category
from models.interface import Accountable


class Account(Accountable):
    def __init__(self, balance):
        self.__balance = balance
        self.__categories = {}
        self.__transactions = []

    def deposit(self, amount):
        if amount < 0:
            raise ValueError(...)
        self.__balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError(...)
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def get_transactions(self):
        return self.__transactions

    def add_transaction(self, transaction: Transaction):
        transaction.apply()
        self.__transactions.append(transaction)

    def get_categories(self):
        return self.__categories.values()

    def add_category(self, category: Category):
        self.__categories[category.get_name()] = category
