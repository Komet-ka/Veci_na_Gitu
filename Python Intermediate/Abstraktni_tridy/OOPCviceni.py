class MOCNINA:
    def __init__(self,a):
        self.cislo = a

    def mocnina(self):
        return self.cislo ** 2
    pass

a = MOCNINA(5)
print(a.mocnina())

a = MOCNINA(2)
print(a.mocnina())