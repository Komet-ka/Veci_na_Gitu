import threading
import time


class ThreadWithReturnValue(threading.Thread):
    def __init__(self, target, args=(), kwargs={}):
        self.target = target
        self.args = args
        self.kwargs = kwargs
        super().__init__()

    def run(self):
        self.result = self.target(*self.args, **self.kwargs)

    def join(self, timeout=None):
        super().join(timeout)
        return self.result


def print_cube(num):
    time.sleep(5)
    print(f"Cube: {num * num * num}")


def square(num):
    time.sleep(2)
    return num * num


if __name__ == "__main__":
    t1 = ThreadWithReturnValue(target=square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    t1.start()
    t2.start()

    t2.join()
    a = t1.join()
    print(a)



    print("Done!")