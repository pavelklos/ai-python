# 180 : Virtual Environments
# is a way to create isolated environments for your projects
# - to manage dependencies
# - to isolate projects
# - to avoid conflicts between different projects

# TODO: get last version of pyjokes
# pip uninstall pyjokes
# pip install pyjokes               # last version
# pip install pyjokes==0.8.3        # specific version 0.8.3
# pip install pyjokes>=0.8.3        # version 0.8.3 or higher

# TODO: pipenv (virtual environment manager)
# - we can have different versions of the same package in different projects
# - we can have different versions of Python in different projects
# - we can have different dependencies in different projects

# TODO: by command prompt (terminal)
# > pip install pipenv
# > pipenv --version
# > pipenv install pyjokes

# TODO: by PyCharm
# - .venv directory in the project
# - Settings - Project - Python Interpreter - [+] - search: pyjokes - Install Package
# TODO OR:
# - New Project - Interpreter type:
#   [Project venv] [Base conda] [Custom environment]]
# TODO: file [pyvenv.cfg] in [.venv] directory
# home = C:\Users\Pavel\AppData\Local\Programs\Python\Python312
# implementation = CPython
# version_info = 3.12.2.final.0
# virtualenv = 20.24.5
# include-system-site-packages = false
# base-prefix = C:\Users\Pavel\AppData\Local\Programs\Python\Python312
# base-exec-prefix = C:\Users\Pavel\AppData\Local\Programs\Python\Python312
# base-executable = C:\Users\Pavel\AppData\Local\Programs\Python\Python312\python.exe
