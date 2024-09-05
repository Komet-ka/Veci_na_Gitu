import pickle
from pympler import asizeof
import time
import sys



a = {'b': list(range(100000000))}

t = time.time()
f = open('velky_soubor.bin', 'wb')
pickle.dump(a, f)
f.close()
print(f"velky object trvalo ulozit {time.time() - t} sekund")

b = [(1, 2), (3, 4)]

t = time.time()
f = open('maly_soubor.bin', 'wb')
pickle.dump(b, f)
f.close()
print(f"maly object trvalo ulozit {time.time() - t} sekund")

t = time.time()
f = open('maly_soubor.txt', 'w')
f.write(str(b))
f.close()
print(f"maly object do textu trvalo ulozit {time.time() - t} sekund")

t = time.time()
f = open('velky_soubor.txt', 'w')
f.write(str(a))
f.close()
print(f"velky object do txt trvalo ulozit {time.time() - t} sekund")

print(sys.getsizeof(a))
print(sys.getsizeof(b))