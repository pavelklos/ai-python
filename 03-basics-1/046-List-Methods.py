# 046 : List Methods
# - methods are functions that belong to an object
basket = [1, 2, 3, 4, 5]
len(basket)  # 5
# TODO: fix this

# Iterable
# - is an object that can be iterated over

# Adding (append, insert, extend)
new_list1 = basket.append(
    100
)  # TODO: changes the list in place, does not produce a new list
print(new_list1)  # None
print(basket)  # [1, 2, 3, 4, 5, 100]
new_list2 = basket.insert(
    2, 200
)  # TODO: changes the list in place, does not produce a new list
print(new_list2)  # None
print(basket)  # [1, 2, 200, 3, 4, 5, 100]
new_list3 = basket.extend(
    [300, 400]
)  # TODO: changes the list in place, does not produce a new list
print(new_list3)  # None
print(basket)  # [1, 2, 200, 3, 4, 5, 100, 300, 400]

# Removing (pop, remove, clear)
new_list4 = basket.pop()  # TODO: changes the list in place, returns the removed item
print(new_list4)  # 400
print(basket)  # [1, 2, 200, 3, 4, 5, 100, 300]
new_list5 = basket.pop(0)  # TODO: changes the list in place, returns the removed item
print(new_list5)  # 1
print(basket)  # [2, 200, 3, 4, 5, 100, 300]
new_list6 = basket.remove(
    300
)  # TODO: changes the list in place, does not return anything
print(new_list6)  # None
print(basket)  # [2, 200, 3, 4, 5, 100]
new_list7 = basket.clear()  # TODO: changes the list in place, does not return anything
print(new_list7)  # None
print(basket)  # []

# Python has a set of built-in methods that you can use on lists/arrays:
# [Method] 	    [Description]
# append()	    Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop()	        Removes the element at the specified position
# remove()  	Removes the first item with the specified value
# reverse()	    Reverses the order of the list
# sort()	    Sorts the list

# Other built-in methods:
# [Method] 	    [Description]
# len(object)   Returns the number of items in an object (list, tuple, set, dictionary, etc.)

print(basket)  # []
print(len(basket))  # 0

print(len([1, 2, 3, 4, 5]))  # 5
