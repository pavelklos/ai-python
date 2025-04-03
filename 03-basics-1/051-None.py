# 051 : None
# - None is a special constant in Python that represents the absence of a value or a null value.
# - None is the only value of the NoneType data type.
# - None is not the same as False.
# - None is not 0.
# - None is not an empty string.
# - Comparing None to anything other than None will always return False.

from types import NoneType

a = None  # a is a variable that is assigned None
print(a)  # None
print(type(a))  # <class 'NoneType'>
print(a == None)  # True
print(a is None)  # True

print(None == False)  # False
print(None == 0)  # False
print(None == "")  # False

print(None)  # None
print(NoneType)  # <class 'NoneType'>
