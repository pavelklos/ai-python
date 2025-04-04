# 082 : Functions
# built-in functions: https://docs.python.org/3/library/functions.html
# TODO: def is keyword to define function
# TODO: 2 types of functions:
# - built-in functions
# - user-defined functions
# TODO: 2 blink lines after class or function definition (PEP 8)
# - [PEP 8] https://peps.python.org/pep-0008/
# def function_name(parameters):
#     statement(s)
#     return value

# say_hello()  # TODO: NameError: name 'say_hello' is not defined


# function definition
def say_hello():
    """
    This function prints 'Hello!' to the console.
    """
    print("Hello!")


# location in memory (memory address)
print(say_hello)  # <function say_hello at 0x00000226B438A340>
print(type(say_hello))  # <class 'function'>

# function call (3 times)
say_hello()  # Hello!
say_hello()  # Hello!
say_hello()  # Hello!

# easier solution by using for loop
for _ in range(3):
    say_hello()  # Hello!
