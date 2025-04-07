# TODO: __name__ is a built-in variable that returns the name of the current module.
print(__name__)  # __main__

import utility                                              # project/utility.py
# # TODO: import * is not recommended (name collision)
# from utility import *                                     # from project.utility import all functions
from utility import divide, multiply, add, subtract         # from project.utility import functions
# TODO: Packages in Python
import shopping.shopping_cart                               # import module
import shopping.shopping_cart as cart                       # as cart: alias for module
# TODO: Different Ways To Import (nested packages)
import shopping.more_shopping.more_shopping_cart            # import module
from shopping.more_shopping.more_shopping_cart import buy   # from module import function
from shopping.more_shopping import more_shopping_cart       # import module

utility.divide(10, 2)       # 5.0
utility.multiply(10, 2)     # 20
utility.add(10, 2)          # 12
utility.subtract(10, 2)     # 8

print(utility)              # <project 'utility' from 'C:\...\utility.py'>
type(utility)               # <class 'project'>
print(utility.__doc__)      # None
print(utility.__file__)     # C:\...\utility.py
print(utility.__name__)     # utility

# TODO: Packages in Python
print(shopping.shopping_cart)                   # <module 'shopping.shopping_cart' from 'C:\...\shopping_cart.py'>
print(shopping.shopping_cart.buy('apple'))      # ['apple']
print(cart.buy('apple'))                        # ['apple']

# TODO: Different Ways To Import (nested packages)
divide(10, 2)                                                   # 5.0
multiply(10, 2)                                                 # 20
add(10, 2)                                                      # 12
subtract(10, 2)                                                 # 8
print(shopping.more_shopping.more_shopping_cart.buy('apple'))   # ['apple']
print(buy('apple'))                                             # ['apple']
print(more_shopping_cart.buy('apple'))                          # ['apple']
utility.divide(10, 2)                                           # 5.0
utility.multiply(10, 2)                                         # 20
utility.add(10, 2)                                              # 12
utility.subtract(10, 2)                                         # 8

# TODO: file which is executed is set: __name__ = '__main__'

# TODO: we can check if the file is executed as a main program
if __name__ == '__main__':
    print('This is the main program.')
    print(shopping.shopping_cart.buy('apple'))      # ['apple']
    print(divide(10, 2))                            # 5.0
    print(multiply(10, 2))                          # 20
    print(max(1, 2, 3))                             # 3

class Student:
    pass

# TODO: Student from main.py
st_main = Student()
print(type(st_main))            # TODO: <class '__main__.Student'>

# TODO: Student from utility.py
st_util = utility.Student()
print(type(st_util))            # TODO: <class 'project.utility.Student'>

# TODO: Student from shopping_cart.py
st_shop = shopping.shopping_cart.Student()
print(type(st_shop))            # TODO:
