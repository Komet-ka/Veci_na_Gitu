import time
def casovac(func):
    def wrapper(*args, **kvargs):
        t1 = time.time()
        return_of_func = func(*args, **kvargs)
        t_delta = time.time() - t1
        print(f"Provadeni funkce {func} trvalo: {round(t_delta, 4)} sekund")
        return(return_of_func)
    return wrapper

def casovac_n(a):
    def casovac(func):
        def wrapper(*args, **kvargs):
            t1 = time.time()
            return_of_func = func(*args, **kvargs)
            t_delta = time.time() - t1
            for i in range(a):
                print(f"Provadeni funkce {func} trvalo: {round(t_delta, 4)} sekund")
            return (return_of_func)

        return wrapper
    return casovac

@casovac
def nejaka_funkce():
    a = []
    for i in range(10000):
        a.append("a")
    return(a)


def vymazlena_funkce():
    a = 2
    time.sleep(3)
    return(a)

nejaky_seznam = nejaka_funkce()

#nejake_cislo = vymazlena_funkce()