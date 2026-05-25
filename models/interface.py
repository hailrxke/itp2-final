from abc import ABC, abstractmethod


class Accountable(ABC):
    @abstractmethod
    def deposit(self, amount: float): pass

    @abstractmethod
    def withdraw(self, amount: float): pass
