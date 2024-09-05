import time
import multiprocessing
import threading

def odpocitavej(_od, _do):
    while _od >= _do:
        _od -= 1

def wo_threading_func():
    odpocitavej(40000000, 0)


def with_threading_func():
    t1 = threading.Thread(target=odpocitavej, args=(40000000, 20000000))
    t2 = threading.Thread(target=odpocitavej, args=(20000000, 0))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

def with_multiprocessing_func():

    p1 = multiprocessing.Process(target=odpocitavej, args=(40000000, 20000000))
    p2 = multiprocessing.Process(target=odpocitavej, args=(20000000, 0))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    t1 = time.time()
    wo_threading_func()
    print(f"wo_threading_func: {time.time()-t1}")

    t1 = time.time()
    with_threading_func()
    print(f"with_threading_func: {time.time() - t1}")

    t1 = time.time()
    with_multiprocessing_func()
    print(f"with_multiprocessing_func: {time.time() - t1}")