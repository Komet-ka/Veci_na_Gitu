import DedicnostVicenasobna

os2 = DedicnostVicenasobna.Zamestnanec("Jack", 36, 20, 160)
os3 = DedicnostVicenasobna.Student("Agatha", 22, 1000)


def check_finance(obj):
    print(obj.vrat_vydelek())


check_finance(os2)  # an instance of the Employee class
check_finance(os3)

def secti(x, y):
    return x + y

print(secti(2, 3))
print(secti([2, 2], [3, 3]))