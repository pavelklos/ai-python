# 157 : Decorators 3
# TODO: we can add arguments
# TODO: we can add arguments using *args, **kwargs


def my_decorator(func):  # TODO: Higher Order Function (HOF)
    def wrap_func(x, y):  # TODO: add arguments to wrap_func()
        print("**********")  # added functionality
        func(x, y)  # TODO: add arguments to func()
        print("**********")  # added functionality

    return wrap_func  # TODO: don't call function, just return it


@my_decorator  # add extra functionality to hello()
def hello(greeting, emoji):  # TODO: add argument to hello()
    print(greeting, emoji)  # TODO: print argument


hello("hi", "😊")
# **********
# hi 😊
# **********

# TODO: how it works behind the scenes
# hello2 = my_decorator(hello)
# hello2("hi", "😊")  # TODO: equivalent to @my_decorator
# my_decorator(hello)("hi", "😊")  # TODO: equivalent to @my_decorator


# TODO: better way to add arguments by using *args, **kwargs -------------------
def my_decorator2(func):
    def wrap_func(*args, **kwargs):
        print("**********")
        func(*args, **kwargs)
        print("**********")

    return wrap_func


@my_decorator2
def hello2(greeting, emoji="😊"):
    print(greeting, emoji)


hello2("hi")
# **********
# hi 😊
# **********

hello2("hi", "😎")
# **********
# hi 😎
# **********

hello2("hi", emoji="🙈🙉🙊")
# **********
# hi 🙈🙉🙊
# **********
