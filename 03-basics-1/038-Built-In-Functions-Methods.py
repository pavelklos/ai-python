# 038 : Built-In Functions + Methods
# - methods are functions that are associated with an object
# - [Built-in Functions]    https://docs.python.org/3/library/functions.html
# - [String Methods]        https://www.w3schools.com/python/python_ref_string.asp

# [Built-in Functions]
str(100), int("100"), float("100"), bool(0)  # ('100', 100, 100.0, False)
type(bool(1))  # <class 'bool'>
print(type(None))  # <class 'NoneType'>
print(type(b"100"))  # <class 'bytes'>
print(type((1, 2)))  # <class 'tuple'>
len("100")  # 3
len([1, 2, 3])  # 3
len({1, 2, 3})  # 3
len({"a": 1, "b": 2, "c": 3})  # 3

# [Built-in Methods]
# - [String Methods]
"string {}".format(1)  # 'string 1'
"string".capitalize()  # 'String'
"to be or not to be".upper()  # 'TO BE OR NOT TO BE'
"to be or not to be".lower()  # 'to be or not to be'
"to be or not to be".find("be")  # 3
"to be or not to be".count("be")  # 2
"to be or not to be".replace("be", "me")  # 'to me or not to me'
"to be or not to be".split()  # ['to', 'be', 'or', 'not', 'to', 'be']

quote = "to be or not to be"
print(quote)  # to be or not to be
print(quote.replace("be", "me"))  # to me or not to me
print(quote)  # to be or not to be, not changed because strings are immutable

# - are functions that are built into Python that perform a task
# - are functions that are associated with an object
# - are functions that are associated with a class
# - are functions that are associated with a project
# - are functions that are associated with a package
# - are functions that are associated with a library
# - are functions that are associated with a framework
# - are functions that are associated with an application
# - are functions that are associated with an operating system
