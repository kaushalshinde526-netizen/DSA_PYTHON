class Employee:
    def __init__(self):
        self._salary =25000
    def get_salary(self):
        return self._salary
obj=Employee()
print(obj.get_salary())