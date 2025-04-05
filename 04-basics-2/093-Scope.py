# 093 : Scope
# TODO: where a variable is accessible in code
# - local: inside a function
# - enclosing: inside a function (nested function)
# - global: at the top level of a project
# - built-in: provided by the builtins project

total = 100  # global variable
if True:
    total = 200  # TODO: global variable in if block
    print(total)  # 200


def some_func():
    total = 10  # TODO: local (function) variable in function
    return total


print(total)  # 200
print(some_func())  # 10
