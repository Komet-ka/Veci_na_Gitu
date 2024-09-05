import random
import string
import time

def generuj_text():
    znaky = string.ascii_letters
    nahodny_retezec = "".join(random.choice(znaky) for _ in range(15))
    return nahodny_retezec

t = time.time()

with open('DataVelka', 'a') as file:
    for i in range(5000):
        text = generuj_text()
        retezec = f'{i}: {text}\n'
        file.write(retezec)
print(f"Data velka txt trvalo ulozit {time.time() - t} sekund")