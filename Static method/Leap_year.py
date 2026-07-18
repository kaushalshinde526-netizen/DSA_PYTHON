class Year:
    @staticmethod
    def leap(year):
        if year%4==0:
            print("Leap Year ")
        else:
            print("Not a Leap Year ")
Year.leap(2022)
