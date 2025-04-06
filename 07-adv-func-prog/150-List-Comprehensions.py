# 150 : List Comprehensions
# TODO: list [], set {}, dictionary {} Comprehensions
# TODO: list [] vs set {}: set removes duplicates (list does not)
# TODO: Provide concise way to create lists.
# Common applications are to make new lists where each element is the result of
# some operation applied to each member of another sequence or iterable, or
# to create a subsequence of those elements that satisfy a certain condition.
# Syntax:
# TODO: [expression for item in iterable]
# Syntax with condition:
# TODO: [expression for item in iterable if condition]
# Syntax with condition (if-else):
# TODO: [expression if condition else expression for item in iterable]
# - expression: operation applied to each item
# - item: element in iterable
# - iterable: list, tuple, etc.
# - condition: filter applied to each item
# - list comprehension: returns new list
# - set comprehension: returns new set
# - dictionary comprehension: returns new dictionary

# without list comprehension
my_list = []
for char in "hello":
    my_list.append(char)
print(my_list)  # ['h', 'e', 'l', 'l', 'o']

# with list comprehension
my_list = [char for char in "hello"]  # ['h', 'e', 'l', 'l', 'o']

# list comprehension and TODO: operation
# Syntax: TODO: [expression for item in iterable]
print([num * 2 for num in range(0, 5)])  # [0, 2, 4, 6, 8]
print([num**2 for num in range(0, 5)])  # [0, 1, 4, 9, 16]

# list comprehension and TODO: operation, condition (if)
# Syntax: TODO: [expression for item in iterable if condition]
print([num**2 for num in range(0, 5) if num % 2 == 0])  # [0, 4, 16]

# list comprehension and TODO: operation, condition (if-else)
# Syntax: TODO: [expression if condition else expression for item in iterable]
print([num**2 if num % 2 == 0 else num * 2 for num in range(0, 5)])  # [0, 2, 4, 6, 16]
# 0: 0**2 = 0
# 1: 1 * 2 = 2
# 2: 2**2 = 4
# 3: 3 * 2 = 6
# 4: 4**2 = 16
