# 039 : Booleans
# - are a data type that can only have one of two values: True or False
# - are used to test whether an expression is True or False
# - are used to make decisions in code
# - are used to compare values
# - are used to evaluate the truthiness of values

name = "John"
is_cool = False
print(type(is_cool))  # <class 'bool'>
print(bool(1))  # True
print(bool(0))  # False
print(bool("True"))  # True
print(bool("False"))  # True
print(bool(""))  # False
print(bool([]))  # False
print(bool({}))  # False
print(bool(()))  # False
print(bool(None))  # False
