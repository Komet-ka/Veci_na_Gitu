import time

def mocnina(seznam):
    return [x**2 for x in seznam]

t1 = time.time()
a = list(range(10000000))
b = [x**2 for x in a]
print(time.time()-t1)