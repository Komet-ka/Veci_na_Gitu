from dataclasses import dataclass
import pickle

@dataclass
class User:
    name: str
    surname: str

f = open('user.data', 'wb')
pickle.dump(User("Pavel", "Rusnok"), f)
f.close()

f = open('user.data', 'rb')
a = pickle.load()