# 173 : Different Ways To Import

import project.shopping.shopping_cart
from project.shopping import (
    shopping_cart,  # better way to import a function from a module
)
from project.shopping.shopping_cart import (
    buy,  # better way to import a function from a module
)

# TODO: it's not recommended to import all functions from a module
from project.utility import *  # not recommended

print(project.shopping.shopping_cart.buy("apple"))  # ['apple']
print(shopping_cart.buy("apple"))  # ['apple']
print(buy("apple"))  # ['apple']

# TODO: name collision: if we have two functions with the same name in two different modules
