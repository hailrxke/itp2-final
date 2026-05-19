class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError(...)
        self.balance += amount

    def withdraw(self, amount):
        if amount > 0:
            raise ValueError(...)
        self.balance -= amount
