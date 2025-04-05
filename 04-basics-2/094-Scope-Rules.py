# 094 : Scope Rules
# TODO: where a variable is accessible in code
# - local: inside a function
# - enclosing: inside a function (nested function)
# - global: at the top level of a project
# - built-in: provided by the builtins project

# TODO: Scope: what variables do I have access to?
a = 1


def confusion():
    a = 5  # TODO: global variable wasn't changed by local variable
    return a


def parent():
    a = 10

    def confusion():
        return a  # TODO: parent local variable was returned

    return confusion()


def return_sum():
    return sum  # TODO: built-in Python function was returned


print(a)  # 1
print(confusion())  # 5
print(parent())  # 10

print(parent())  # 10
print(confusion())  # 5
print(a)  # 1

if True:
    a = 10  # TODO: global variable was changed by if block

print(a)  # 10
print(confusion())  # 5
print(parent())  # 10
print(return_sum())  # <built-in function sum>

# Rules:
# 1. Start with local
# 2. Parent local
# 3. Global
# 4. Built-in Python functions  # sum(), print(), etc.
