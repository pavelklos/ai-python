# TODO: __name__ is a built-in variable that returns the name of the current module.
print(__name__)  # __main__


def multiply(num1, num2):
    """Multiply two numbers"""
    return num1 * num2


def divide(num1, num2):
    """Divide two numbers"""
    return num1 / num2


def add(num1, num2):
    """Add two numbers"""
    return num1 + num2


def subtract(num1, num2):
    """Subtract two numbers"""
    return num1 - num2


class Student:
    pass


st_util = Student()
print(type(st_util))  # TODO: <class '__main__.Student'>
