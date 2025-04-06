# 144 : filter()
# TODO: Functional programming: use pure functions as much as possible
# useful built-in pure functions: TODO: map(), filter(), zip(), reduce()
# TODO: filter()
# built-in function that takes in two arguments:
# - function and sequence iterable
# - applies the function to all elements in sequence
# - returns new list with elements that return True by function # TODO: there is no side effect
# filter(function, sequence)
# - sequence: list, tuple, etc.
# - function: built-in or custom function
# lambda: anonymous

# filter(function, sequence)
filter(lambda x: x % 2 == 0, [1, 2, 3, 4])  # [2, 4]
filter(lambda x: x % 2 != 0, [1, 2, 3, 4])  # [1, 3]
filter(lambda x: x.isupper(), ["a", "B", "c", "D"])  # ['B', 'D']
filter(lambda x: x.istitle(), ["hello", "World"])  # ['World']

my_list = [1, 2, 3, 4]  # TODO: immutable list (unchanged) by filter()


def is_even(item):
    return item % 2 == 0  # evaluate to True or False (bool)


res = filter(is_even, my_list)

# optimized version with lambda
res = filter(lambda x: x % 2 == 0, my_list)
print(res)  # <filter object at 0x00000238BD7F63B0>
print(type(res))  # <class 'filter'>
print(list(res))  # [2, 4]  # convert filter object to list

print(my_list)  # [1, 2, 3, 4] # TODO: my_list is unchanged
