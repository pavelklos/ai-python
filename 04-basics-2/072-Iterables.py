# 072 : Iterables
# iterable : object that can be iterated over
# iteration : process of looping through items
# we can iterate over sequence (list, tuple, dictionary, set or string)

for item in range(3):  # range(0, 3)
    for char in "abc":  # string
        print(item, char)

# dictionary is special case of sequence
# dictionary has keys and values
# dictionary is iterable over keys and not values
user = {"name": "John", "age": 30, "can_swim": False}
print(user)  # {'name': 'John', 'age': 30, 'can_swim': False}

for item in user:  # dictionary (iterate over keys) default
    print(item)

for item in user.items():  # dictionary (iterate over items)
    # key, value = item  # it's destructuring
    # print(key, value)
    print(item, type(item))

for key, value in user.items():  # dictionary (iterate over items)
    print(key, value)
    type(key)  # <class 'str'>
    type(value)  # <class 'str'> <class 'int'> <class 'bool'>
for item in user.keys():  # dictionary (iterate over keys)
    print(item)
for item in user.values():  # dictionary (iterate over values)
    print(item)

type(user)  # <class 'dict'>
type(user.items())  # <class 'dict_items
type(user.keys())  # <class 'dict_keys'>
type(user.values())  # <class 'dict_values'>

print(bool(user))  # True by user.__bool__
print(len(user))  # 3 by user.__len__
