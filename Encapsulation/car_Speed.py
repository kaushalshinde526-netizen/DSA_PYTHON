class Car:
    def __init__(self):
        self.__speed = 0

    def accelerate(self):
        self.__speed += 20

    def show(self):
        print(self.__speed)

c = Car()
c.accelerate()
c.show()