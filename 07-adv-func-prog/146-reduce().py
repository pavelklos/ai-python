# 146 : reduce()
# TODO: Functional programming: use pure functions as much as possible
# useful built-in pure functions: TODO: map(), filter(), zip(), reduce()
# TODO: reduce()
# built-in function that takes in three arguments:
# - function and sequence iterable
# - applies the function to all elements in sequence
# - returns single value TODO: there is no side effect
# reduce(function, sequence, initial = 0)
# - sequence: list, tuple, etc.
# - function: built-in or custom function
# - initial: initial value of accumulator
# - lambda: anonymous

# reduce(function, sequence, initial = 0)
from functools import reduce  # TODO: reduce is function in functools project

my_list = [1, 2, 3, 4]


def accumulator(acc, item):
    print(acc, item)
    return acc + item


res = reduce(accumulator, my_list)
print(res)  # 10 # TODO: 1+2+3+4=10
print(type(res))  # <class 'int'>
print(my_list)  # [1, 2, 3, 4] # TODO: my_list is unchanged

# with initial value of accumulator
res = reduce(accumulator, my_list, 0)
print(res)  # 10 # TODO: 0+1+2+3+4=10
print(type(res))  # <class 'int'>
print(my_list)  # [1, 2, 3, 4] # TODO: my_list is unchanged

# optimized version with lambda
res = reduce(lambda x, y: x + y, my_list, 10)  # TODO: 10 is initial value of acc
print(res)  # 20 # TODO: 10+1+2+3+4=20
print(type(res))  # <class 'int'>
print(my_list)  # [1, 2, 3, 4] # TODO: my_list is unchanged

# other examples
res1 = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 0)  # 15 # TODO: 0+1+2+3+4+5=15
res2 = reduce(accumulator, [1, 2, 3, 4, 5])  # 15 # TODO: 1+2+3+4+5=15
res3 = sum([1, 2, 3, 4, 5])  # 15 # TODO: 1+2+3+4+5=15

print(res1, res2, res3)  # 15 15 15

# using reduce to find the product of all elements in a list
product = reduce(lambda x, y: x * y, my_list, 1)  # 1 is the initial value
print(product)  # 24 # TODO: 1*1*2*3*4=24
print(type(product))  # <class 'int'>

# using reduce to find the maximum element in a list
maximum = reduce(lambda x, y: x if x > y else y, my_list)  # 4 # 1<2<3<4
print(maximum)  # 4
print(type(maximum))  # <class 'int'>

# using reduce to find the minimum element in a list
minimum = reduce(lambda x, y: x if x < y else y, my_list)  # 1 # 1<2<3<4
print(minimum)  # 1
print(type(minimum))  # <class 'int'>

# using reduce to find the average of all elements in a list
average = reduce(lambda x, y: x + y, my_list) / len(my_list)  # 2.5 # 1+2+3+4=10/4=2.5
print(average)  # 2.5
print(type(average))  # <class 'float'>
