# 174 : __name__
# TODO: __name__ is a built-in variable that returns the name of the current module.

# TODO: concept of __main__ in Python
# when the Python interpreter reads a source file, it defines a few special variables.
# __name__ is one of these special variables.
# if the Python interpreter is running that module (the source file) as the main program,
#   it sets the special __name__ variable to have a value "__main__".
# if this file is being imported from another module, __name__ will be set to the module’s name.

# TODO: [main.py]
# \project\main.py
print(__name__)  # TODO: write it at the top of the file
# __main__
# utility                       # TODO: because of import utility
# shopping.shopping_cart        # TODO: because of import shopping.shopping_cart

print(__name__)  # TODO: write it at end of the file
# __main__

# TODO: file which is executed is set: __name__ = '__main__'

# TODO: we can check if the file is executed as a main program
if __name__ == "__main__":
    print("This is the main program.")


class Student:
    pass


st = Student()
print(type(st))  # TODO: <class '__main__.Student'>
print(type(Student()))  # TODO: <class '__main__.Student'>
