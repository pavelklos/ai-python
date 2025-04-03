# 060 : Sets
# - are unordered collections of unique elements (are not indexed)
# - are defined by curly braces {}
# - are mutable, iterable

my_set = {1, 2, 3, 4, 5}  # set of integers
print(my_set)  # {1, 2, 3, 4, 5}
print(type(my_set))  # <class 'set'>
my_set2 = {1, 2, 3, 4, 5, 5}  # set of integers, 5 is repeated
print(my_set2)  # {1, 2, 3, 4, 5} TODO: 5 is not repeated
my_set3 = {1, 2, 3, 4, 5, "hello"}  # set of integers and string
print(my_set3)  # {1, 2, 3, 4, 5, 'hello'}
# my_set4 = {1, 2, 3, 4, 5, [6, 7]}     # set of integers and list TODO: TypeError: unhashable type: 'list'
# print(my_set4)                        # TypeError: unhashable type: 'list'

my_set.add(100)  # add element to set
my_set.add(2)  # add element to set, 2 is repeated
my_set.add(6)  # add element to set
print(my_set)  # {1, 2, 3, 4, 5, 100, 6} TODO: unordered

my_list = [6, 5, 2, 3, 1, 4, 6, 5]  # list of integers TODO: 5 is repeated
my_set5 = set(my_list)  # convert list to ordered set TODO: 5 is not repeated
print(my_list)  # [6, 5, 2, 3, 1, 4, 6, 5]
print(my_set5)  # {1, 2, 3, 4, 5, 6} TODO: ordered set
# print(my_set[0])  # TODO: TypeError: 'set' object is not subscriptable
print(1 in my_set)  # True
print(10 in my_set)  # False
print(len(my_set))  # 7
print(my_set)  # {1, 2, 3, 4, 5, 100, 6}
print(list(my_set))  # [1, 2, 3, 4, 5, 100, 6]
new_set = my_set.copy()  # copy set
print(new_set)  # {1, 2, 3, 4, 5, 100, 6}
