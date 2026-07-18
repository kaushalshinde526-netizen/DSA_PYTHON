class Calculator:

    @staticmethod
    def add():
        a1 = int(input("Enter Number 1: "))
        b1 = int(input("Enter Number 2: "))
        result = a1 + b1
        print("Addition of two numbers is:", result)

    @staticmethod
    def sub():
        c1 = int(input("Enter Number 1: "))
        c2 = int(input("Enter Number 2: "))
        result = c1 - c2
        print("Subtraction of two numbers is:", result)

    @staticmethod
    def mult():
        c1 = int(input("Enter Number 1: "))
        c2 = int(input("Enter Number 2: "))
        result = c1 * c2
        print("Multiplication of two numbers is:", result)

    @staticmethod
    def div():
        c1 = int(input("Enter Number 1: "))
        c2 = int(input("Enter Number 2: "))

        if c2 == 0:
            print("Division by zero is not possible.")
        else:
            result = c1 / c2
            print("Division of two numbers is:", result)


print("______________ ADDITION ______________")
Calculator.add()

print("\n______________ SUBTRACTION ______________")
Calculator.sub()

print("\n______________ MULTIPLICATION ______________")
Calculator.mult()

print("\n______________ DIVISION ______________")
Calculator.div()