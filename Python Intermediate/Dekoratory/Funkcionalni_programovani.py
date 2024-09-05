print(len("asdf"))
moje_len = len

print(moje_len("asdf"))

def druha_mocnina(x):
    return x**2

def treti_mocnina(x):
    return x**3

print(druha_mocnina(3))
print(treti_mocnina(4))

print("********************")
print("chytrá mocnina")
print("********************")

def x_mocnina(n):
    def mocnina(x):
        return x**n
    return mocnina

moje_mocnina = x_mocnina(2)
print(moje_mocnina(3))

moje_mocnina = x_mocnina(8)
print(moje_mocnina(3))

print(x_mocnina(1/2)(16))
