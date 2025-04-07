# 172 : Packages in Python
# TODO: package is simply a directory that contains multiple modules.
# packages are a way of structuring Python’s module namespace by using “dotted module names”.
# directory must contain a file named __init__.py in order for Python to consider it as a package.
# this file can be left empty but we generally place the
#   initialization code for that package in this file.

# TODO: package is directory, module is file
# TODO: [PyCharm - New - Python Package] add file __init__.py (can be empty)
# import mypackage.mymodule
import project.shopping.shopping_cart as cart  # as cart: alias for the module
import project.shopping.shopping_cart as cart2  # as cart2: alias for the module

# TODO: __name__ is a built-in variable that returns the name of the current module.
print(__name__)  # __main__

print(cart.buy("apple"))  # ['apple']
print(cart2.buy("apple"))  # ['apple']

st_shop = cart.st_shop
print(st_shop)  # <project.shopping.shopping_cart.Student object at 0x0000029147CB6540>
print(type(st_shop))  # TODO: <class 'project.shopping.shopping_cart.Student'>
