# 084 : Default Parameters and Keyword Arguments
# TODO: default parameters: parameters that have default values
# TODO: keyword arguments: arguments that are passed to function using parameter names
# TODO: positional arguments: arguments are passed to function in order


# TODO: define, declare, create function
# name, emoji are parameters (variables) in function definition
# def say_hello(name, emoji):
#     print(f'Hello, {name}{emoji}!')
# TODO: default parameters
def say_hello(name="John", emoji="😊"):
    print(f"Hello, {name}{emoji}!")


# TODO: call, invoke, execute, run, apply function
# name, emoji are arguments (actual values) that are passed to function
say_hello("John", "😊")  # Hello, John😊!
say_hello("Jane", "🤗")  # Hello, Jane🤗!
say_hello("Jack", "😎")  # Hello, Jack😎!

# TODO: positional arguments
say_hello("John", "😊")  # Hello, John😊!

# TODO: keyword arguments
say_hello(emoji="🤗", name="Jane")  # Hello, Jane🤗!

# TODO: default parameters
say_hello()  # Hello, John😊!
say_hello("Jane")  # Hello, Jane😊!
say_hello(emoji="😎")  # Hello, John😎!
