# 044 : List Slicing
# - is a way to extract a subset of elements from a list
# - list[start:stop:step]

li = [1, 2, 3, 4, 5]
print(li[0:3])  # [1, 2, 3]
print(li[1:4])  # [2, 3, 4]
print(li[::-1])
li[0] = 10  # [10, 2, 3, 4, 5]
li[0:3] = [10, 20, 30]  # [10, 20, 30, 4, 5]
li2 = li[0:3]  # [10, 20, 30]  # slicing creates a new list
print(li2)  # [10, 20, 30]
li2 = li  # [10, 20, 30, 4, 5]  # assignment creates a reference to the original list

# Copying vs Modifying
# - slicing creates a new list
# - assignment creates a reference to the original list

# String Slicing
# - is a way to extract a subset of characters from a string
# - string[start:stop:step]
# - string are immutable
string = "Hello, World!"
print(string[0:5])  # Hello
# string[0] = "h"  # TypeError: 'str' object does not support item assignment

# Exercise: List Slicing
# What is the output of this code?
# Before you click RUN, guess the output of each print statement!
new_list = ["a", "b", "c"]  # ['a', 'b', 'c']
print(new_list[1])  # b
print(new_list[-2])  # b
print(new_list[1:3])  # ['b', 'c']
new_list[0] = "z"  # ['z', 'b', 'c']
print(new_list)  # ['z', 'b', 'c']

my_list = [1, 2, 3]  # [1, 2, 3]
bonus = my_list + [5]  # [1, 2, 3, 5]
my_list[0] = "z"  # ['z', 2, 3]
print(my_list)  # ['z', 2, 3]
print(bonus)  # [1, 2, 3, 5]

# TODO: copying vs modifying
# - assignment creates a reference to the original list
# - slicing creates a new list
old_list = [1, 2, 3, 4, 5]
new_list = old_list  # reference (1 place in memory)
new_list = old_list[:]  # copy (2 different places in memory)
