class Mobile:
    def __init__(self):
        self.__pin = 1234

    def verify(self, pin):
        if pin == self.__pin:
            print("Correct PIN")
        else:
            print("Wrong PIN")

m = Mobile()
m.verify(1234)