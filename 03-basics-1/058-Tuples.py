# 058 : Tuples
# - is a collection of items which is ordered and unchangeable (immutable list).
# - allows duplicate members.
# - is written with round brackets.
# - can have any data type.
# - can have nested tuples.
# - can have one item.
# - can have no items.

age_items = (25, 35, 45, 55)  # tuple
print(age_items)  # (25, 35, 45, 55)
print(type(age_items))  # <class 'tuple'>

# dictionary can have a tuple as a key
dictionary = {
    "basket": [1, 2, 3],
    "greet": "Hello",
    "age": 25,
    (1, 2): [1, 2, 3],
}  # TODO: key is tuple
print(dictionary[(1, 2)])  # [1, 2, 3]
print(dictionary.keys())  # dict_keys(['basket', 'greet', 'age', (1, 2)])

print(
    dictionary
)  # {'basket': [1, 2, 3], 'greet': 'Hello', 'age': 25, (1, 2): [1, 2, 3]}
