import threading
import re
import os
import time
f_names = []
for i in range(1, 1001):
    file_name = "text" + str(i)
    f_names.append(file_name)
    f = open(file_name, "w")
    f.close()


file_names = os.listdir()
print(len(file_names))
file_names = [f for f in os.listdir() if "text" in f]
file_names = [x for x in os.listdir() if re.match("text",x)]
file_names = [x for x in os.listdir() if x.startswith("text")]
print(len(file_names))
print([x for x in os.listdir() if x.endswith(".py")])


def pridej(x):
    f = open(x, "a")
    for i in range(10):
        f.write("Ahoj byl jsem tady fantomas.\n")
    f.close()

print("cas jednoho souboru")
t1 = time.time()
pridej("text1")
print(time.time()-t1)

def pridej_seznam(seznam):
    for s in seznam:
        pridej(s)

print("cas vsech souboru")
t1 = time.time()
pridej_seznam(file_names)
print(time.time()-t1)

index = int(len(file_names)/3)
file_names1 = file_names[:index]
file_names2 = file_names[index:(index*2)]
file_names3 = file_names[(index*2):]
print(len(file_names))
print(len(file_names1))
print(len(file_names2))
print(len(file_names3))

def with_threading_func():
    t1 = threading.Thread(target=pridej_seznam, args=(file_names1,))
    t2 = threading.Thread(target=pridej_seznam, args=(file_names2,))
    t3 = threading.Thread(target=pridej_seznam, args=(file_names3,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

print("cas vsech souboru 2 thready")
t1 = time.time()
with_threading_func()
print(time.time()-t1)

def with_threading_10000(seznam):
    threads = []
    for nazev_souboru in seznam:
        th = threading.Thread(target=pridej, args=(nazev_souboru,))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()

print("cas vsech souboru 1000 threadu")
t1 = time.time()
with_threading_10000(file_names)
print(time.time()-t1)