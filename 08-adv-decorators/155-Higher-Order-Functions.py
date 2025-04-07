# 155 : Higher Order Functions (HOF)
# TODO: are functions that take other functions as arguments, or return them as results
# - map(), filter(), reduce()
# - list comprehensions
# - lambda functions
# - decorators


# TODO: (HOF) can be function that take other function as argument
def greet(func):
    func()


# TODO: (HOF) can be function that return other function
def greet2():
    def func():
        return 5

    return func


print(greet)  # <function greet at 0x000002D4659BA3E0>
print(greet2())  # <function greet2.<locals>.func at 0x000002D465C5D120>
print(greet2()())  # 5
