# 198 : Unittest
# - is a unit testing framework for Python, based on
#   Erich Gamma's JUnit and Kent Beck's Smalltalk testing framework.

# TODO: unittest: standard built-in module for testing
# - https://docs.python.org/3/library/unittest.html

# def do_stuff(num=0):
#     return int(num) + 5


def do_stuff(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return "please enter number"
    except ValueError as err:
        return None
        # raise(err)
        # return err


do_stuff(5)  # 10
do_stuff("10")  # 15
# do_stuff('text')  # ValueError: invalid literal for int() with base 10: 'text'
do_stuff("text")  # None
# do_stuff(None)  # TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
