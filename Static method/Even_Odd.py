class Number:
    @staticmethod
    def check(num):
        if num%2==0:
            print("Event")
        else:
            print("Odd")
Number.check(15)