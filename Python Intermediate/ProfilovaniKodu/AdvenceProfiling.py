import cProfile


def long_time():
    a = []
    for i in range(10**7):
        a.append(i)


def short_time():
    a = []
    for i in range(10**3):
        a.append(i)


def f():
    for i in range(10**4):
        short_time()
    for i in range(1):
        long_time()


cProfile.run('f()')