# 149 : Exercise: Lambda Expressions

# Square list (x * x)
my_list = [5, 4, 3]

print(list(map(lambda item: item * item, my_list)))  # [25, 16, 9]
print(list(map(lambda item: item**2, my_list)))  # [25, 16, 9]

# List Sorting (sort is built-in function)
a = [(0, 2), (4, 3), (10, -2), (9, 9)]  # list of tuples

a.sort(key=lambda x: x[0])  # TODO: sorted by first element of tuple
print(a)
a.sort(key=lambda x: x[1])  # TODO: sorted by second element of tuple
print(a)
a.sort(
    key=lambda x: x[0] + x[1], reverse=True
)  # TODO: sorted by sum of elements of tuple, and revered (descending)
print(a)
