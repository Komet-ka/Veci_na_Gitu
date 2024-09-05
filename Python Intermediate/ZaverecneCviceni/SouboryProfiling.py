import os
import time
print(os.getcwd())

downloads = os.listdir("../../../../Downloads")
california = [x for x in downloads if "california_housing" in x]
os.chdir("../../../../Downloads")
print(california)
print(os.getcwd())

t = time.time()
f = open(california[0], 'r')
a = f.readlines()
print(len(a))
f.close()
print(f"{time.time() - t}")

t = time.time()
f = open(california[1], 'r')
a = f.readlines()
print(len(a))
f.close()
print(f"{time.time() - t}")