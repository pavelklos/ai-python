# 043 : Lists
# - a list is a collection of items in a particular order
# - is ordered sequence of elements, can store any type of data
# - is a data structure (indexed from 0, zero-based) is a way of organizing and storing data
# - is mutable, can be changed
# - in other languages (array, vector, sequence, collection, container, etc.)

li1 = [1, 2, 3, 4, 5]  # [1, 2, 3, 4, 5]
li2 = ["a", "b", "c"]  # ['a', 'b', 'c']
li3 = [1, "a", True]  # [1, 'a', True]
print(type(li3))  # <class 'list'>

# Accessing Elements
li3[0]  # 1
li3[1]  # 'a'
li3[2]  # True

print(sum(li1))  # 15
print(len(li1))  # 5
