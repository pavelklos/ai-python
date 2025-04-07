# 161 : Error Handling
# - by TODO: try-except-else-finally block
# - we can raise our own exceptions
# - we can create custom exceptions
# - we can handle exceptions with logging
# - we can use assert statement
# - we can use with statement
# - we can use context manager
# - we can use decorators

# from babel.messages.jslexer import division_re

# age = int(input("What is your age: "))
# print(age)

# TODO: 'abc': ValueError: invalid literal for int() with base 10: 'abc'
# TODO: we can use try-except block to handle this error

while True:
    # noinspection PyBroadException # TODO: CHECK PyBroadException
    try:
        age = int(input("What is your age: "))
        # if age < 0:
        #     raise ValueError("Age cannot be negative")
        division = 10 / age
        print(age)
        # break
    # except:
    #     print("Please enter a number")
    except ValueError:
        print("Please enter a number")
    except ValueError:
        print("!!!")  # TODO: this except block will never be executed
    except ZeroDivisionError:
        print("Please enter a number other than zero")
    except Exception as e:
        print(e.__class__.__name__ + ": " + str(e))
    else:
        print("Thank you!")
        break

# Error Handling with logging
import logging

logging.basicConfig()
try:
    raise RuntimeError("Bad stuff happened.")
except Exception as e:
    logging.error("Failed.", exc_info=e)
