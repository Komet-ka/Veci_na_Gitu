import requests
import time

def wo_threading_func(lsts):
    for lst in lsts:
        sqre(lst, "without_threads.txt")
def sqre(lsts, dest):
    try:
        result = [lst ** 2 for lst in lsts]
        with open(dest, "a") as f:
            f.write(result)

    except requests.exceptions.RequestException:
        print("Error!")

def with_threading_func(lsts):
    import threading

    threads = []
    for lst in lsts:
        th = threading.Thread(target=sqre, args=(lst, "with_threads.txt"))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()

a = list(range(10000000))
a1 = list(a[i] for i in range(0, 5000000))
a2 = list(a[i] for i in range(5000000, 10000000))
lsts = [a1, a2]

x = time.time()
with_threading_func(lsts)
wo_threading_func(a)

print(time.time()-x)