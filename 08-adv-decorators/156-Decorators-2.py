# 156 : Decorators 2


def my_decorator(func):  # TODO: Higher Order Function (HOF)
    def wrap_func():
        print("**********")  # added functionality
        func()
        print("**********")  # added functionality

    return wrap_func  # TODO: don't call function, just return it


@my_decorator  # add extra functionality to hello()
def hello():
    print("hello")


def bye():  # no extra functionality in bye()
    print("bye")


hello()
# **********
# hello
# **********

bye()  # bye

# TODO: how it works behind the scenes
hello2 = my_decorator(hello)
hello2()  # TODO: equivalent to @my_decorator
my_decorator(hello)()  # TODO: equivalent to @my_decorator
