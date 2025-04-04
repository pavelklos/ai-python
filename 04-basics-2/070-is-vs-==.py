# 070 : is vs ==
# difference between is and ==
# is : checks if both variables point to the same object (location in memory)
# == : checks if values of two variables are the same
# == : check equality of values (we should check the same type of values)

# checks if values of two variables are the same
# check equality of values (we should check the same type of values)
print(True == 1)  # True
print("" == 1)  # False
print("1" == 1)  # False
print([] == 1)  # False
print(10 == 10.0)  # True
print([] == [])  # True
print([1] == [2])  # False
print([1, 2, 3] == [1, 2, 3])  # True
print({} == [])  # False

# check if both variables point to the same object (location in memory)
# print(True is 1)  # False     # TODO: SyntaxWarning
# print("" is 1)  # False       # TODO: SyntaxWarning
# print("1" is 1)  # False      # TODO: SyntaxWarning
# print([] is 1)  # False       # TODO: SyntaxWarning
# print(10 is 10.0)  # False    # TODO: SyntaxWarning
print([] is [])  # False
print([1] is [2])  # False
print([1, 2, 3] is [1, 2, 3])  # False
print({} is [])  # False

# check if both variables point to the same object (location in memory)
dict_1 = {"name": "John", "age": 25}
dict_2 = dict_1  # dict_2 is a reference to dict_1
print(dict_1 is dict_2)  # True

# TODO: booleans, strings, numbers, tuples are immutable objects
# print(True is True)             # True
# print('1' is '1')               # True      # TODO: SyntaxWarning
# print(1 is 1)                   # True      # TODO: SyntaxWarning
# print((1, 2) is (1, 2))         # True      # TODO: SyntaxWarning
a = (1, 2)
b = (1, 2)
print(a is b)  # True      # TODO: (True) the same location in memory (tuple)

# TODO: lists, dictionaries, sets are mutable objects
print([] is [])  # False        # TODO: (False) different locations in memory
print({} is {})  # False        # TODO: (False) different locations in memory
print(set() is set())  # False  # TODO: (False) different locations in memory

# TODO: difference between tuple and set in Python?
# tuple : ordered, immutable, allows duplicate elements
# set   : unordered, mutable, does not allow duplicate elements
tuple_1 = (1, 2, 3, 4, 5, 5)  # tuple
tuple_2 = (5, 5, 4, 3, 2, 1)  # tuple
set_1 = {1, 2, 3, 4, 5, 5}  # set
set_2 = {5, 5, 4, 3, 2, 1}  # set
print(tuple_1)  # (1, 2, 3, 4, 5, 5)
print(tuple_2)  # (5, 5, 4, 3, 2, 1)
print(set_1)  # {1, 2, 3, 4, 5}
print(set_2)  # {1, 2, 3, 4, 5}
print(tuple_1 is tuple_2)  # False
print(set_1 is set_2)  # False
print(tuple_1 == tuple_2)  # False
print(set_1 == set_2)  # True
print(type(tuple_1))  # <class 'tuple'>
print(type(set_1))  # <class 'set'>
