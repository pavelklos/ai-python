# 087 : Methods vs Functions
# method: TODO: function that is associated with an object
# function: TODO: piece of code that is called by name, is independent of any object.
# - It can be passed data to operate on (i.e. the parameters) and
#   can optionally return data (the return value).


# TODO: functions are independent of objects/classes.
# TODO: [built-in functions]
# functions: list(), print(), max(), min(), input(), etc.
# TODO: [custom functions]
def say_hello():
    print("Hello!")


# TODO: methods are associated with objects/classes.
# TODO" [built-in methods]
# methods: append(), insert(), remove(), pop(), clear(), count(), index(), sort(), etc.
"hello".capitalize()  # method of object string # result: 'Hello'
[1, 2, 3].append(4)  # method of object list   # result: [1, 2, 3, 4]
{1: "one", 2: "two"}.clear()  # method of object dict   # result: {}
(1, 2, 3).count(2)  # method of object tuple  # result: 1
# TODO: [custom methods]


# object/class definition
class Dog:
    def bark(self):
        print("Woof!")


# object/class method call
Dog().bark()
