# 059 : Tuples 2
# - count() method returns the number of times a specified value occurs in a tuple.
# - index() method searches the tuple for a specified value and returns the position of where it was found.

my_tuple = (1, 2, 3, 4, 5)  # tuple
new_tuple = my_tuple + (6, 7, 8)  # (1, 2, 3, 4, 5, 6, 7, 8) TODO: concatenate
new_tuple2 = my_tuple[1:2]  # (2,) TODO: slice
new_tuple3 = my_tuple[1:3]  # (2, 3) TODO: slice
print(new_tuple)  # (1, 2, 3, 4, 5, 6, 7, 8)
print(new_tuple2)  # (2,)
print(new_tuple3)  # (2, 3)
print(my_tuple.count(3))  # 1
print(my_tuple.index(3))  # 2
print(my_tuple.index(3, 2))  # 2
print(len(my_tuple))  # 5
# print(my_tuple.index(3, 5))           # ValueError: tuple.index(x): x not in tuple
# print(my_tuple.index(10))             # ValueError: tuple.index(x): x not in tuple
x = my_tuple[0]  # 1  TODO: access
y = my_tuple[1]  # 2  TODO: access
x, y, z, *other = my_tuple  # 1 2 3 4 5 TODO: unpack
print(x, y, z, other)  # 1 2 3 [4, 5]
