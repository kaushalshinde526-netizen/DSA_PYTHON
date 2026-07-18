class ATM:
    def __init__(self):
        self.__balance = 10000

    def withdraw(self, amount):
        self.__balance -= amount

    def balance(self):
        print(self.__balance)

a = ATM()
a.withdraw(2000)
a.balance()