# 175 : Python Built-in Modules
# Python is extremely useful through its external modules and packages (built-in modules).

# TODO: [Python Modules index]
# - https://docs.python.org/3/py-modindex.html
# TODO: they are built-in modules, but we have to import them to use them
# for example (email, math, random, datetime, calendar, os, sys, json, turtle, tkinter, etc.)
# TODO: random is module (file)
# TODO: email is package (directory with files and __init__.py)

# file: C:\Users\pavel\AppData\Local\Programs\Python\Python312\Lib\email\__init__.py
import email

# file: C:\Users\pavel\AppData\Local\Programs\Python\Python312\Lib\random.py
# [random.py] 35.679 bytes
import random
import random as rd  # we can import module with alias
from random import (
    shuffle,  # we can import specific function from module with alias; we can import specific function from module
)
from random import shuffle as sh

# TODO: info about module/package, file, name
print(random)  # <module 'random' from 'C:\...\random.py'>
print(email)  # <module 'email' from 'C:\...\email\__init__.py'>
print(random.__file__)  # C:\...\random.py
print(email.__file__)  # C:\...\email\__init__.py
print(random.__name__)  # random
print(email.__name__)  # email

# TODO: help, docstring, dir
# help(random)                # print help message for module
# help(email)                 # print help message for package
# print(random.__doc__)       # print docstring
# print(email.__doc__)        # print docstring
print("=" * 100)
print(dir(random))  # list of attributes
print("-" * 100)
print(dir(email))  # list of attributes
print("-" * 100)

# TODO: use random module
print(random.random())  # 0.0 <= x < 1.0
print(random.randint(1, 10))  # 1 <= x <= 10
print(random.choice([1, 2, 3, 4, 5]))  # random element from list
print(random.choices([1, 2, 3, 4, 5], k=3))  # list of random elements
# TODO: in-place function (function that modifies the object it is called on)
random.shuffle(li1 := [1, 2, 3, 4, 5])  # None, we use walrus operator ':='
rd.shuffle(li2 := [1, 2, 3, 4, 5])  # TODO: we've imported random as rd
shuffle(li3 := [1, 2, 3, 4, 5])  # TODO: we've imported shuffle from random
sh(li4 := [1, 2, 3, 4, 5])  # TODO: we've imported shuffle from random as sh
print(li1)  # [3, 1, 5, 2, 4]
print(li2)  # [1, 4, 2, 3, 5]
print(li3)  # [4, 2, 1, 5, 3]
print(li4)  # [5, 4, 1, 3, 2]
