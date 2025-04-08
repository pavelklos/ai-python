# 189 : File IO Errors
# TODO: we can use try-except block to handle errors
# - we can use specific exception types
# - we can use 'as' keyword to access the error message
# - we can use 'else' block to execute code when no errors occur
# - we can use 'finally' block to execute code regardless of the result
# - we can raise our own exceptions
# - we can use 'assert' statement to raise an AssertionError
# TODO: FileNotFoundError: raised when a file or directory is requested but doesn't exist
# TODO: IOError: raised when an input/output operation fails

# TODO: [try-except block]
try:
    with open("data.txt", "r") as file:
        print(file.read())
# except FileNotFoundError as e:
# except IOError as err:
except Exception as err:
    print(type(err))  # <class 'FileNotFoundError'>
    print(err)  # [Errno 2] No such file or directory: 'data.txt'
    # raise err  # re-raise the exception
