class Wallet:
    def __init__(self):
        self.__money = 500

    def spend(self, amount):
        self.__money -= amount

    def show(self):
        print(self.__money)

w = Wallet()
w.spend(100)
w.show()