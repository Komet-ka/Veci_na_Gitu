import multiprocessing
import time
def vynasob_2(x):
    a = []
    for i in range(10 ** 7):
        a.append(i)
    return x * 2

if __name__ == "__main__":
    input_list = list(range(10))

    t1 = time.time()
    with multiprocessing.Pool(processes=5) as pool:
        vynasobeny_list = pool.map(vynasob_2, input_list)
    print(time.time()-t1)

    t1 = time.time()
    vynasobeny_list = list(map(vynasob_2, input_list))
    print(time.time() - t1)