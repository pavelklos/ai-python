# 090 : *args and **kwargs
# arguments and keyword arguments
# TODO: *args and **kwargs are mostly used in function definitions.
# TODO: *args and **kwargs allow you to pass a variable number of arguments to a function.
# What does variable mean here is that you do not know before hand that how many arguments
# can be passed to your function by the user so in this case you use these two keywords.
# TODO: *args: Non-Keyword Arguments
# TODO: **kwargs: Keyword Arguments
# TODO: Order rules: func(parameters, *args, default parameters, **kwargs)


# *args
def super_func(*args):
    print(*args)  # 1 3.14 'a' True [1, 2, 3] # TODO: get unpacked tuple (values)
    print(args)  # (1, 3.14, 'a', True, [1, 2, 3]) # TODO: get tuple
    print(len(args))
    print(type(args))
    for item in args:
        print(item)


# *args: Non-Keyword Arguments (tuple)
super_func(1, 3.14, "a", True, [1, 2, 3])  # TODO: <class 'tuple'>


# **kwargs
def super_func2(*args, **kwargs):
    print(args)
    print(kwargs)
    print(len(kwargs))
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)


# **kwargs: Keyword Arguments (dictionary)
super_func2(
    1, 3.14, "a", True, [1, 2, 3], a=1, b=3.14, c="a", d=True, e=[1, 2, 3]
)  # TODO: <class 'dict'>


def super_func_3(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


result = super_func_3(1, 2, 3, 4, 5, num1=5, num2=10)
print(result)  # 30


# Order rules: func(parameters, *args, default parameters, **kwargs)
def super_func_4(name, *args, i="hi", **kwargs):
    print(name)  # parameter
    print(args)  # *args
    print(i)  # default parameter
    print(kwargs)  # **kwargs


super_func_4("Andy", 1, 2, 3, 4, 5, i="hello", num1=5, num2=10)
