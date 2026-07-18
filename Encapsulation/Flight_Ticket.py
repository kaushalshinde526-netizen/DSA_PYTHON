class Flight:
    def __init__(self):
        self.__ticket = "AI101"

    def ticket(self):
        print(self.__ticket)

f = Flight()
f.ticket()