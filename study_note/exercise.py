class BankAccount(object):
    interest_rate = 0.3
    def __init__(self, name, number, balance):
        self.__name = name
        self.__number = number
        self.__balance = balance
        return
    def deposit(self):
        self.__balance+=self.__number
    def withdraw(self):
        self.__balance-=self.__number