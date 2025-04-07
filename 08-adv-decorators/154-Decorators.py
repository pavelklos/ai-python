# 154 : Decorators
# in section about classes TODO: @classmethod and @staticmethod
# - TODO: Decorator Patterns are used all over the programming world
# - TODO: decorators are functions, they have prefix @
# - decorators wrap other functions and enhance their behavior
# - decorators are examples of higher order functions (HOF)
# - decorators have their own syntax, using "@" (pie syntax)
# - decorators are commonly used in web frameworks
# - decorators can be used to make code more readable

# functions in Python are TODO: first-class citizens
# - they can be passed as arguments to other functions
# - they can be returned from other functions
# - they can be assigned to variables
# - they can be defined inside other

# TODO: Decorators are only possible because of these features,
#   this ability of functions to act like variables,
#   act as first-class citizens in Python
#   and be passed around
# TODO: @decorator supercharge our function
#   (add extra functionality, features, etc.)


# TODO: functions can be assigned to variables ---------------------------------
def hello():
    print("hello")


greet = hello  # TODO: assign function hello to variable greet
print(greet)  # <function hello at 0x7f8b1b3b7d30>
greet()  # hello
# del hello
# print(greet)  # <function hello at 0x7f8b1b3b7d30>
# print(greet())  # hello, None # TODO: greet() is still working, but hello() is not
# hello()  # NameError: name 'hello' is not defined. Did you mean: 'help'?

greet = hello()  # TODO: assign return value of function hello to variable greet
print(greet)  # None

del hello  # delete the function hello
# hello()  # NameError: name 'hello' is not defined
# greet()  # TypeError: 'NoneType' object is not callable
print(greet)  # None


# TODO: functions can be passed as arguments to other functions ----------------
def hello(func):
    func()


def greet():
    print("HELLO")


a = hello(greet)
print(a)  # HELLO, None
