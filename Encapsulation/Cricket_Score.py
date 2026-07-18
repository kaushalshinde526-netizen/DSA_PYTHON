class Cricket:
    def __init__(self):
        self.__score = 0

    def add_run(self):
        self.__score += 4

    def show(self):
        print(self.__score)

c = Cricket()
c.add_run()
c.show()