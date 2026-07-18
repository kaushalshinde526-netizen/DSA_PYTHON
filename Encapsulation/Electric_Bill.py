class Bill:
    def __init__(self):
        self.__amount = 60000

    def show_bill(self):
        print(self.__amount)

b = Bill()
b.show_bill()