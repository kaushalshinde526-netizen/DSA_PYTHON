class Laptop:
    def __init__(self):
        self.__password = "admin123"

    def login(self, pwd):
        print("Login Success" if pwd == self.__password else "Wrong Password")

l = Laptop()
l.login("admin123")