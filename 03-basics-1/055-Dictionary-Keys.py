# 055 : Dictionary Keys
# - can be strings, numbers, boolean
# - can be mixed
# - has to be immutable, unique
# - are case-sensitive

dict1 = {1: "One", 2: "Two", 3: "Three"}  # dictionary with integer keys
print(dict1)  # {1: 'One', 2: 'Two', 3: 'Three'}
dict2 = {"one": 1, "two": 2, "three": 3}  # dictionary with string keys
print(dict2)  # {'one': 1, 'two': 2, 'three': 3}
dict3 = {True: "Yes", False: "No"}  # dictionary with boolean keys
print(dict3)  # {True: 'Yes', False: 'No'}

# TODO: Duplicate keys 1: "One" <- True: "Yes" = 1: "Yes"
dict4 = {1: "One", "one": 1, True: "Yes"}  # dictionary with mixed keys
print(dict4)  # {1: 'One', 'one': 1, True: 'Yes'} TODO: ??? {1: 'Yes', 'one': 1}

dict5 = {
    1: "One",
    1: "Uno",
}  # TODO: duplicate key is not error, only the last one is used
print(dict5)  # {1: 'Uno'}
