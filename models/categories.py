class Category:
    def __init__(self, name, limit):
        self.__name = name
        if limit < 0:
            raise ValueError(...)
        self.__limit = limit
        self.__spent = 0

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_limit(self):
        return self.__limit

    def set_limit(self, limit):
        if limit < 0:
            raise ValueError(...)
        self.__limit = limit

    def add_spent(self, amount):
        self.__spent += amount
