# 185 : How To Debug Code
# TODO: debugging: is the process of finding and fixing errors in code
# - syntax errors: are detected by the Python interpreter
# - logical errors: are detected by you

# TODO: [pdb — The Python Debugger]
# - https://docs.python.org/3/library/pdb.html
# - pdb: is a built-in module, interactive source code debugger for Python programs.

# TODO: tips
# - use linting tools (e.g. pylint, flake8)
# - use debugger (e.g. pdb)
# - use print statements
# - use logging module
# - use unit tests
# - use version control system (e.g. git)
# - use code review tool (e.g. GitHub)
# - use IDE (e.g. PyCharm, Visual Studio Code)
#   or text editor (e.g. Sublime Text, Atom)
# - use online editor (e.g. Repl.it, Jupyter Notebook)
# - use code formatter (e.g. black, autopep8)
# - read error messages
# - read documentation
# - read source code

# TODO: use [pdb - Python Debugger] --------------------------------------------

import pdb


def add(num1, num2):
    print(num1, num2)
    print(type(num1), type(num2))
    pdb.set_trace()
    print("code after pdb.set_trace()")
    return num1 + num2


print(add(5, "7"))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# TODO: run code (will stop at the pdb.set_trace(), then you can debug the code)
# > c:\users\pavel\projects\ai-python\12-debugging\185-how-to-debug-code.py(35)add()
# -> print("code after pdb.set_trace()")
# (Pdb) num1                # 5
# (Pdb) num2                # '7'
# (Pdb) a                   # list all arguments
# (Pdb) help                # list available commands
# (Pdb) list                # show the current line of the code
# (Pdb) clear               # clear all breakpoints
# (Pdb) step                # step into the function
# (Pdb) p num1 + num2       # '57'
# (Pdb) p int(num2)         # 7

# TODO: usefull commands
# - h(elp): list available commands
# - w(here): print the stack trace
# - n(ext): execute the current line
# - s(tep): step into the function
# - r(eturn): continue execution until the current function returns
# - c(ontinue): continue execution until the next breakpoint
# - q(uit): exit the debugger and the program
# - l(ist): show the current line of the code
# - p(rint): print variables
