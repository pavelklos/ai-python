# 148 : Lambda Expressions
# - TODO: are used to create anonymous functions, without a name.
# - they are small functions usually not more than a line.
# - they can have any number of arguments but only one expression.
# - they are used when you need a short function for a short period of time.
# - TODO: they are used with built-in functions like filter(), map(), reduce(), sorted(), etc.
# - they are not as readable as regular functions.

# TODO: lambda parameter: expression
# lambda x: x*2
# lambda x, y: x + y
# lambda x, y, z: x + y + z
# lambda x, y=2, z=3: x + y + z
# lambda x, *args, y, **kwargs: x + sum(args) + y + sum(kwargs.values())

from functools import reduce

my_list = [1, 2, 3]


def multiply_by2(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    # print(acc, item)
    return acc + item


# TODO: by function
print(list(map(multiply_by2, my_list)))  # [2, 4, 6]
print(list(filter(only_odd, my_list)))  # [1, 3]
print(reduce(accumulator, my_list, 0))  # 6

# TODO: by lambda
print(list(map(lambda item: item * 2, my_list)))  # [2, 4, 6]
print(list(filter(lambda item: item % 2 != 0, my_list)))  # [1, 3]
print(reduce(lambda acc, item: acc + item, my_list, 0))  # 6

print(my_list)  # [1, 2, 3]  # my_list is unchanged

# Sorting a list of dictionaries by a specific key
users = [
    {"name": "John", "age": 32},
    {"name": "Alex", "age": 25},
    {"name": "Sarah", "age": 29},
]

# Sort by age
sorted_by_age = sorted(users, key=lambda user: user["age"])
print(
    sorted_by_age
)  # [{'name': 'Alex', 'age': 25}, {'name': 'Sarah', 'age': 29}, {'name': 'John', 'age': 32}]

# Sort by name length
sorted_by_name_length = sorted(users, key=lambda user: len(user["name"]))
print(
    sorted_by_name_length
)  # [{'name': 'John', 'age': 32}, {'name': 'Alex', 'age': 25}, {'name': 'Sarah', 'age': 29}]

# Using lambda with conditional logic
numbers = [-5, -3, 0, 2, 6]
abs_and_square = list(map(lambda x: x**2 if x >= 0 else abs(x), numbers))
print(abs_and_square)  # [5, 3, 0, 4, 36]

# Combining multiple operations
rng = range(1, 6)  # range(1, 6)
print(list(rng))  # [1, 2, 3, 4, 5]
transform = list(map(lambda x: (x**2 if x % 2 == 0 else x * 3) + 1, range(1, 6)))
print(transform)  # [4, 5, 10, 17, 16]
# 1: 1*3+1 = 4
# 2: 2**2+1 = 5
# 3: 3*3+1 = 10
# 4: 4**2+1 = 17
# 5: 5*3+1 = 16
