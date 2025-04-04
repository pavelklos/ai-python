# 083 : Parameters and Arguments
# parameters: variables that are used in function definition to represent those arguments
# arguments: actual values that are passed to function when it is called


# TODO: define, declare, create function
# name, emoji are parameters (variables) in
def say_hello(name, emoji):
    print(f"Hello, {name}{emoji}!")


# TODO: call, invoke, execute, run, apply function
# name, emoji are arguments (actual values) that are passed to function
say_hello("John", "😊")  # Hello, John😊!
say_hello("Jane", "🤗")  # Hello, Jane🤗!
say_hello("Jack", "😎")  # Hello, Jack😎!
