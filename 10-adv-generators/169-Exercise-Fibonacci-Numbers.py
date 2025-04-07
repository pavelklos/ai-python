# 169 : Exercise: Fibonacci Numbers
# TODO: Fibonacci Numbers are the numbers in the following integer sequence:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# TODO: rule: Xn = Xn-1 + Xn-2
# Write a generator function that yields the next Fibonacci Number each time it is called.


# TODO: solution by generator --------------------------------------------------
def fib_gen(number):
    n1 = 0
    n2 = 1
    for i in range(number):
        yield n1
        temp = n1
        n1 = n2
        n2 = temp + n2


# for x in fib_gen(10000):
for x in fib_gen(100):
    print(x)


# TODO: solution by list -------------------------------------------------------
def fib_list(number):
    result = []
    n1 = 0
    n2 = 1
    for i in range(number):
        result.append(n1)
        temp = n1
        n1 = n2
        n2 = temp + n2
    return result


# print(fib_list(10000))
print(fib_list(100))
