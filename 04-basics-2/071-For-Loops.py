# 071 : For Loops
# can iterate over sequence (list, tuple, dictionary, set or string)
# can iterate over sequence of numbers using the range() function
# items are iterable : object that can be iterated over
# iteration : process of looping through items

import random

# TODO: item is created variable for each iteration in block of code
for item in "123":  # string
    print(item)
for item in [1, 2, 3]:  # list
    print(item)
for item in {1, 2, 3}:  # set
    print(item)
for item in (1, 2, 3):  # tuple
    print(item)
for item in {"name": "John", "age": 30}:  # dictionary
    print(item)

# nested loops
for item in range(3):  # range(0, 3)
    for char in "abc":  # string
        print(item, char)

# loop over range of numbers (3 random numbers from 1 to 100)
numbers1 = [random.randint(1, 100) for i in range(3)]  # integer
print(numbers1)
for number in numbers1:
    print(number)

# loop over range of numbers (3 random numbers from 1 to 100)
numbers2 = [round(random.random(), 2) for i in range(3)]  # float
print(numbers2)
for number in numbers2:
    print(number)

# for item in 50:
#     print(item)# TODO: TypeError: 'int' object is not iterable
