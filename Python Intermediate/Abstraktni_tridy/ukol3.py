from dataclasses import dataclass
import pickle

@dataclass
class User:
    name: str
    surname: str

with open('uzivatel.pickle', 'wb') as f:
    pickle.dump(User("Lenka", "Otrubova"), f)

with open('uzivatel.pickle', 'rb') as f:
    a = pickle.load(f)

print(a)
b = User("Petr", "Vyborny")
print(b)
