# 166 : Generators 2
# TODO: iterable: is object that can be iterated over (looped over)
# TODO: iterate: is to access each item in iterable
# TODO: iteration: is process of looping through items
# - list, string, dictionary, range, tuple, set, file (are iterable)
# TODO: __iter__() method: returns an iterator
# - list.__iter__(), string.__iter__(), dictionary.__iter__(), etc.
print([1, 2, 3].__iter__())  # <list_iterator object at 0x000002270A553460>

# TODO: generators are iterators, but not all iterators are generators
# - generator is subset of iterator
# TODO: generator vs iterator is in the way they are implemented
# - generator uses yield keyword & next() function
# - generator held only one item in memory at time
# - generator is more memory efficient
# - iterator uses __iter__() and __next__() methods


# TODO: Create list ------------------------------------------------------------
def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 2)
    return result


my_list = make_list(10)
print(my_list)  # list with 10 items located in memory

# TODO: Create generator -------------------------------------------------------
# yield keyword: is used to pause function and return value
# next() function: is used to resume function


def generator_function(num):
    for i in range(num):
        # return  # we don't use return keyword in generator, we use yield keyword
        yield i * 2  # TODO: yield keyword is used to pause function and return value


for item in generator_function(10):
    print(item)  # 0 2 4 6 8 10 12 14 16 18

g = generator_function(10)
print(g)  # <generator object generator_function at 0x000002270A3E6400>
print(next(g))  # 0 # TODO: next() function is used to resume function
print(next(g))  # 2
print(next(g))  # 4

g = generator_function(1)
print(next(g))  # 0
# print(next(g))  # TODO: StopIteration (error): is raised when there is no more value to return
