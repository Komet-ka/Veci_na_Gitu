import pickle
import time

with open('DataVelka', 'r') as f:
    DataTXTvelka = f.readlines()

with open('DataMala', 'r') as f:
    DataTXTmala = f.readlines()

t = time.time()
with open('DataVelkaPickle', 'wb') as f:
    pickle.dump(DataTXTvelka, f)

print(f"velky object trvalo ulozit {time.time() - t} sekund")

r = time.time()
with open('DataMalaPickle', 'wb') as f:
    pickle.dump(DataTXTmala, f)

print(f"maly object trvalo ulozit {time.time() - r} sekund")
