# 171 : Modules in Python
# TODO: Modules refer to a file containing Python statements and definitions.
# A file containing Python code, for example: example.py,
#   is called a project, and its project name would be example.
# We use modules to break down large programs into small manageable and organized files.
# Modules provide reusability of code.
# We can define our most used functions in a project and import it,
#   instead of copying their definitions into different programs.


# Create new function.
def greeting(name):
    return "Hello, " + name


print(greeting("John"))  # result: 'Hello, John'

# Save this code in a file named [mymodule.py]
# - Open a new file in text editor.
# - Copy the code above and paste it in the new file.
# - Save the file as mymodule.py.
# - Now, we have a project named mymodule.

# Use the project (Import the project named mymodule, and call the greeting function.
# import mymodule
# mymodule.greeting("Jonathan")       # result: 'Hello, Jonathan'
# mymodule.greeting("Jane")           # result: 'Hello, Jane'
# mymodule.greeting("John")           # result: 'Hello, John'

import mymodule

print(mymodule.greeting("Jonathan"))  # result: 'Hello, Jonathan'

# TODO: Python code in:
# - file: mymodule.py
# - function: greeting(name)
# - class: Dog, bark()
# - project: mymodule
# - package: mypackage, mymodule
# - library: math, random()
# - framework: Django, Flask
# - project: MyProject

# TODO: function | class | file | project | package | library | framework | project
# - function: block of code that performs a specific task.
# - class: blueprint for creating objects.
# - file: collection of code.
# - project: collection of functions, classes, and variables.
# - package: collection of modules.
# - library: collection of packages.
# - framework: collection of libraries.
# - project: collection of frameworks.

# TODO: divide up code into separate files for:
# - imports
# - functions
# - classes
# - variables
# - constants
# - main program
# - Each file should have a specific purpose.
# - Each file should be named according to its purpose.

# TODO: other ways to divide code:
# utility.py: functions (very simple, common)
# model.py: classes
# config.py: variables, constants
# main.py: main program

# TODO: [.venv] directory
# is a virtual environment directory that contains all the necessary files and directories
#   to create a virtual environment in Python.
# - It is created using the command python -m venv .venv.
# - It is used to manage dependencies and isolate projects.
