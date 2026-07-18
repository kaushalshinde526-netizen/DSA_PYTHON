class Student:
    def __init__(self):
        self.__marks=80
    def get_marks(self):
        return self.__marks
obj=Student()
print(obj.get_marks())