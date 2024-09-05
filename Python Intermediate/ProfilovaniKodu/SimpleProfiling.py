import time
a = []

time_1 = time.time()
for i in range(10000000):
  a.append(i)
print(time.time() - time_1)