# 048 : List Methods 3

# - sort is a Python method (sorts the list)
basket = ["a", "b", "c", "d", "e", "d"]  # ['a', 'b', 'c', 'd', 'e', 'd']
basket.sort()  # TODO: changes the list in place, does not produce a new list
print(basket.sort())  # None
print(basket)  # ['a', 'b', 'c', 'd', 'd', 'e']

# - sorted is a Python function (returns a new list)
basket = ["a", "b", "c", "d", "e", "d"]  # ['a', 'b', 'c', 'd', 'e', 'd']
print(sorted(basket))  # ['a', 'b', 'c', 'd', 'd', 'e'] TODO: is a new list
print(basket)  # ['a', 'b', 'c', 'd', 'e', 'd'] TODO: is the original list

# - copy is a Python method (returns a copy of the list)
basket = ["a", "b", "c", "d", "e", "d"]  # ['a', 'b', 'c', 'd', 'e', 'd']
new_basket = basket.copy()  # TODO: is a new list
new_basket.reverse()  # ['d', 'e', 'd', 'c', 'b', 'a']
print(basket)  # ['a', 'b', 'c', 'd', 'e', 'd']
print(new_basket)  # ['d', 'e', 'd', 'c', 'b', 'a']

# - reverse is a Python method (reverses the list)
basket = ["a", "b", "c", "d", "e", "d"]  # ['a', 'b', 'c', 'd', 'e', 'd']
basket.reverse()  # TODO: changes the list in place, does not produce a new list
print(basket.reverse())  # None
print(basket.reverse())  # None
print(basket)  # ['d', 'e', 'd', 'c', 'b', 'a']

new_basket = basket[
    ::-1
]  # ['a', 'b', 'c', 'd', 'e', 'd'] TODO: produce a new reversed list
print(new_basket)  # ['a', 'b', 'c', 'd', 'e', 'd']

basket = ["a", "x", "b", "c", "d", "e", "d"]  # ['a', 'x', 'b', 'c', 'd', 'e', 'd']
basket.sort()  # ['a', 'b', 'c', 'd', 'd', 'e', 'x']
basket.reverse()  # ['x', 'e', 'd', 'd', 'c', 'b', 'a']
print(basket)  # ['x', 'e', 'd', 'd', 'c', 'b', 'a']
print(basket[::-1])  # ['a', 'b', 'c', 'd', 'd', 'e', 'x']
