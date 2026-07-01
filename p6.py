# Multilevel Inheritance --> Person -> Teacher -> HOD

class Person:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def show(self):
        print("ID :", self.id)
        print("Name :", self.name)


class Teacher(Person):

    def __init__(self, id, name, salary):
        super().__init__(id, name)
        self.salary = salary

    def show(self):
        super().show()
        print("Salary :", self.salary)


class HOD(Teacher):

    def __init__(self, id, name, salary, department):
        super().__init__(id, name, salary)
        self.department = department

    def show(self):
        super().show()
        print("Department :", self.department)


p = Person(1, "Amit")
p.show()

t = Teacher(2, "Neha", 50000)
t.show()

h = HOD(3, "Rahul", 80000, "Computer Science")
h.show()