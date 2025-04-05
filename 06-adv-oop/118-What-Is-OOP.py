# 118 : What Is OOP?
# TODO: [OOP] Object Oriented Programming
# OOP is a programming paradigm that relies on the concept of classes and objects.
# Classes are like blueprints for objects.
# Objects are instances of classes.
# Classes define the properties and behaviors of objects.
# Properties are like data.
# Behaviors are like functions.
# Properties are called attributes.
# Behaviors are called methods.
# TODO: Object has attributes and methods.
# Everything in Python is an object.


# TODO: class is blueprint
class BigObject:  # TODO: naming convention: CamelCase
    # attributes        # data
    # methods           # functions
    # constructor       # __init__ method
    # self              # reference to the object itself
    def __init__(self):
        # print("self is", self)
        print("BigObject created")

    pass


# TODO: create objects (instances of class), instanciate class
obj1 = BigObject()
obj2 = BigObject()
obj3 = BigObject()

print(type(None))  # <class 'NoneType'>
print(type(True))  # <class 'bool'>
print(type(5))  # <class 'int'>
print(type(5.5))  # <class 'float'>
print(type("hi"))  # <class 'str'>
print(type([]))  # <class 'list'>
print(type(()))  # <class 'tuple'>
print(type({}))  # <class 'dict'>
print(type(BigObject))  # TODO: <class 'type'>
print(
    type(obj1)
)  # TODO: <class '__main__.BigObject'> # __main__ is the name of the file

print(type(BigObject), type(BigObject()))  # <class 'type'> <class '__main__.BigObject'>
print(
    BigObject, BigObject()
)  # <class '__main__.BigObject'> <__main__.BigObject object at 0x00000226B438A340>
