class Vote:
    @staticmethod
    def eligible(age):
        if age>=18:
            print("Eligible")
        else:
            print("Not Eligible")
Vote.eligible(20)