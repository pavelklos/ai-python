# 037 : Immutability
# - is the property of an object that it cannot be changed after it is created
# - Python strings are immutable

number = "01234567"
# number[0] = '7'       # TypeError: 'str' object does not support item assignment
#                         - we cannot reassign a part of a string
number = number + "8"  # number is a new string
print(number)  # 012345678
number = 100  # but it is possible to assign a new value to the variable
print(number)  # 100

# [Immutable objects]
# - Python strings are immutable
# - Python integers are immutable
# - Python floats are immutable
# - Python booleans are immutable
# - Python None is immutable
# - Python bytes are immutable
# - Python tuples are immutable

# [Mutable objects]
# - Python objects are mutable
# - Python arrays are mutable
# - Python lists are mutable
# - Python sets are mutable
# - Python dictionaries are mutable
# - Python functions are mutable
# - Python classes are mutable
# - Python modules are mutable
# - Python packages are mutable
# - Python libraries are mutable
# - Python frameworks are mutable
# - Python applications are mutable
# - Python operating systems are mutable
# - Python hardware is mutable
# - Python universe is mutable

# [function vs method]
# - function: a piece of code that is called by name
# - method:   a piece of code that is called by name that is associated with an object
