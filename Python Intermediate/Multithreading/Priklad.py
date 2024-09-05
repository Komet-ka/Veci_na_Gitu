import threading


def iterovany_zapis(iter):
    for item in iter:
        print(item)


if __name__ == "__main__":
    t1 = threading.Thread(target=iterovany_zapis, args=(range(5),))
    t2 = threading.Thread(target=iterovany_zapis, args=("Python",))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")