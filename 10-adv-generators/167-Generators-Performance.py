# 167 : Generators Performance
# TODO: generator is memory efficient (one item at time)
# TODO: list is not memory efficient (all items in memory)

# generators are much more performant than lists. (i.e., range > list in performance.)
# so generators are really, really useful when calculating large sets of data

from time import time


# decorator
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, *kwargs)
        t2 = time()
        # print(f'took {t2 - t1} s')
        # convert to ms and round to 2 decimal places
        # print(f'took {round((t2 - t1) * 1000, 2)} ms')
        print(f"took {(t2 - t1) * 1000:.2f} ms")
        return result

    return wrapper


@performance
def long_time(stop=10000000):
    print(f"1 ({stop}) by range")
    for i in range(stop):  # TODO: it took less time (generator is memory efficient)
        i * 5


@performance
def long_time2(stop=10000000):
    print(f"2 ({stop}) by list")
    for i in list(range(stop)):  # TODO: it took longer (list is not memory efficient)
        i * 5


long_time()
long_time2()

long_time(20000000)
long_time2(20000000)
