# 052 : Dictionaries
# - is a collection of key-value pairs (unordered, mutable, indexed)
# - keys are unique (must be immutable)
# - values can be any data type (mutable or immutable)
# - is written with curly brackets {}

dictionary = {"a": 1, "b": 2, "c": 3}  # dictionary with 3 key-value pairs
print(dictionary)  # {'a': 1, 'b': 2, 'c': 3}
print(dictionary["a"])  # 1
# print(dictionary['z'])                        # KeyError: 'z'
print(dictionary.get("z"))  # None
print(dictionary.get("z", "Key not found"))  # Key not found
dictionary["d"] = 4  # add a new key-value pair
print(dictionary)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dictionary["a"] = 0  # update the value of an existing key
print(type(dictionary))  # <class 'dict'>
print(dictionary.keys())  # dict_keys(['a', 'b', 'c', 'd'])
print(dictionary.values())  # dict_values([0, 2, 3, 4])
print(dictionary.items())  # dict_items([('a', 0), ('b', 2), ('c', 3), ('d', 4)])
dictionary.pop("a")  # remove a key-value pair
print(dictionary)  # {'b': 2, 'c': 3, 'd': 4}
dictionary.clear()  # remove all key-value pairs
print(dictionary)  # {}
del dictionary  # delete the dictionary
# print(dictionary)  # NameError: name 'dictionary' is not defined

other_dictionary = dict(
    a=[1, 2, 3], b="Hello", c=3.14, d=True
)  # dictionary with different data types
print(other_dictionary)  # {'a': [1, 2, 3], 'b': 'Hello', 'c': 3.14, 'd': True}
