# 143 : map()
# TODO: Functional programming: use pure functions as much as possible
# useful built-in pure functions: TODO: map(), filter(), zip(), reduce()
# TODO: map()
# built-in function that takes in two arguments:
# - function and sequence iterable
# - applies the function to all elements in sequence
# - returns new list with changed elements by function # TODO: there is no side effect
# map(function, sequence)
# - sequence: list, tuple, etc.
# - function: built-in or custom function
# lambda: anonymous function

# map(function, sequence)
map(lambda x: x * 2, [1, 2, 3, 4])  # [2, 4, 6, 8]
map(lambda x: x.upper(), ["a", "b", "c", "d"])  # ['A', 'B', 'C', 'D']
map(lambda x: x.title(), ["hello", "world"])  # ['Hello', 'World']

my_list = [1, 2, 3]  # TODO: immutable list (unchanged) by map()


def multiply_by2(item):
    return item * 2


res = map(multiply_by2, my_list)  # <map object at 0x0000019309D662F0>
print(res)  # <map object at 0x7f8b1c1b5d90>
print(type(res))  # <class 'map'>
print(list(res))  # [2, 4, 6]

# optimized version with lambda
res = map(lambda x: x * 2, my_list)  # <map object at 0x0000019309D662F0>
print(type(res))  # <class 'map'>
print(list(res))  # [2, 4, 6] # TODO: convert map object to list

print(my_list)  # [1, 2, 3] # TODO: my_list is unchanged
