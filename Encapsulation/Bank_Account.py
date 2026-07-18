class Bank:
    def __init__(self):
        self.__balance=5000
    def deposit(self,amount):
        self.__balance+=amount
    def show_balance(self):
        print(self.__balance)
obj=Bank()
obj.deposit(1000)
obj.show_balance()