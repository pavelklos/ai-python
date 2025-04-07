# 165 : Generators
# TODO: are iterators that generate values on the fly (over time)
# - TODO: generator uses yield keyword
# - range() function is a generator
# - list is not a generator
# - generator is an iterator
# - generator is a function that returns an iterator
# - generator is a memory efficient
# TODO: to use item generator (one by one) is more efficient than  list (all items in memory)

# TODO: range() function is a generator
print(range(10))  # generates (creates) 10 items one by one
print(list(range(10)))  # list with 10 items located in memory


def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 2)
    return result


my_list = make_list(10)
print(my_list)  # list with 100 items located in memory
# print(list(range(1000000)))  # list with 1000000 items located in memory
print(list(range(10)))  # list with 10 items located in memory
