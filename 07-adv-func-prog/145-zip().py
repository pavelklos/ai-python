# 145 : zip()
# TODO: Functional programming: use pure functions as much as possible
# useful built-in pure functions: TODO: map(), filter(), zip(), reduce()
# TODO: zip()
# built-in function that takes in two or more sequences
# - aggregates elements from each sequence
# - returns new list with tuples of elements from each sequence # TODO: there is no side effect
# zip(sequence1, sequence2, ...)
# - sequence: list, tuple, etc.
# - returns list of tuples
# - stops at the shortest sequence
# - can be used with map() and filter()

my_list = [1, 2, 3]
my_tuple = (10, 20, 30)
my_set = {5, 4, 3}  # after initialization, sets are unordered  # {3, 4, 5}

res = zip(my_list, my_tuple, my_set)
print(res)  # <zip object at 0x000002711FABD800>
print(type(res))  # <class 'zip'>
print(
    list(res)
)  # [(1, 10, 3), (2, 20, 4), (3, 30, 5)] # TODO: list of tuples  # convert zip object to list

print(my_list)  # [1, 2, 3] # TODO: my_list is unchanged
print(my_tuple)  # (10, 20, 30) # TODO: my_tuple is unchanged
print(my_set)  # {3, 4, 5} # TODO: my_set is unchanged

# Example: Using zip() with unequal length sequences
list1 = [1, 2, 3, 4]
list2 = ["a", "b", "c"]

zipped = zip(list1, list2)
print(list(zipped))  # [(1, 'a'), (2, 'b'), (3, 'c')] # stops at the shortest sequence

# Example: Unzipping a zipped object
zipped = zip(my_list, my_tuple)
unzipped = list(zip(*zipped))
print(unzipped)  # [(1, 2, 3), (10, 20, 30)]
