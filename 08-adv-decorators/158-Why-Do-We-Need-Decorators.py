# 158 : Why Do We Need Decorators?

from time import time  # import time module


# performance decorator
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        # convert seconds to milliseconds and round to 2 decimal places
        print(f"took {((t2 - t1) *1000):.2f} ms")
        return result

    return wrapper


@performance
def long_time(num=1000):
    # for i in range(1000):
    for i in range(num):
        i * 5


long_time(1000)  # took 0.00 ms      # 1 thousand
long_time(10000)  # took 1.00 ms      # 10 thousand
long_time(100000)  # took 5.96 ms      # 100 thousand
long_time(1000000)  # took 48.00 ms     # 1 million
long_time(10000000)  # took 542.00 ms    # 10 million
long_time(100000000)  # took 5237.00 ms   # 100 million
