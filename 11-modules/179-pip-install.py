# 179 : pip install
# TODO: pip: package installer for Python
# TODO: pip usage:
# - pip install package_name
# - pip install package_name==version
# - pip install package_name>=version
# - pip install package_name<=version

# TODO: find pyjokes package on PyPI
# https://pypi.org/project/pyjokes/
# [pyjokes 0.8.3]

# TODO: install by PyCharm terminal
# - Settings - Project - Python Interpreter - [+] search: pyjokes - Install Package
import pyjokes

print(pyjokes.get_joke())  # 'JOKE'
print(pyjokes.get_joke(category="chuck"))  # 'CHUCK-JOKE'
print(pyjokes.get_joke(category="neutral"))  # 'NEUTRAL-JOKE'

# TODO: install by command prompt (terminal)
# > python -V                           # Python 3.12.8
# > pip -V                              # pip 25.0.1
# > pip install pyjokes
# > python3 -V                          # Python was not found
# > pip3 -V                             # pip 25.0.1
# > pip3 install pyjokes

# TODO: use pyjokes in Python shell
# > python                              # Python 3.12.8
# >>> import pyjokes
# >>> pyjokes.get_joke()                 # 'JOKE'

# TODO: upgrade pip
# > pip install --upgrade pip

# TODO: uninstall pyjokes
# > pip uninstall pyjokes

# TODO: list all installed packages
# > pip list
# Package Version
# ------- -------
# pip     25.0.1
# pyjokes 0.8.3
