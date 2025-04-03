# 050 : List Unpacking
# - is a way to split the values of a list into separate variables

basket = [1, 2, 3]  # [1, 2, 3]
a, b, c = [1, 2, 3]  # 1 2 3
print(a, b, c)  # 1 2 3

basket = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
a, b, c, *other = basket  # 1 2 3 [4, 5, 6, 7, 8, 9] TODO: *other at the end of the list
print(a, b, c, other)  # 1 2 3 [4, 5, 6, 7, 8, 9]
print(other)  # [4, 5, 6, 7, 8, 9]

a, b, c, *other, d = (
    basket  # 1 2 3 [4, 5, 6, 7, 8] 9 TODO: *other in the middle of the list
)
print(a, b, c, other, d)  # 1 2 3 [4, 5, 6, 7, 8] 9
print(other)  # [4, 5, 6, 7, 8]
