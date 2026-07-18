class Hospital:
    def __init__(self):
        self.__patient_id = 101

    def get_id(self):
        print(self.__patient_id)

h = Hospital()
h.get_id()