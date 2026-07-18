class Grade:
    @staticmethod
    def Calculate(marks):
        if marks>=90:
            print("A Grade ")
        elif marks>=75:
            print("B Grade ")
        elif marks>=50:
            print("C Grade ")
        else:
            print("Fail ")
Grade.Calculate(92)