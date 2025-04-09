# 191 : Regular Expressions
# are a powerful tool for various kinds of string manipulation
# are a domain specific language for matching patterns in strings
# are used in search engines, search and replace dialogs of word processors and text editors

# TODO: re: module provides support for regular expressions
# - https://docs.python.org/3/library/re.html

import re

# > pip install jupyter-core
from jupyter_core.version import pattern

string = "search inside of this text please!"

# TODO: searching for a string inside another string
print("search" in string)  # True

# TODO: searching by regular expressions is more powerful than the above method
# TODO: - return None or re.Match object
a = re.search("thIs", string)
print(a)  # None

a = re.search("this", string)
print(a)  # <re.Match object; span=(17, 21), match='this'>

# the below 4 commands will give error if the searching string does not exist
print(a.span())  # (17, 21)     # start and end index
print(a.start())  # 17          # start index
print(a.end())  # 21            # end index
print(a.group())  # this        # the string that was found

# TODO: create Pattern object
pattern = re.compile("this")
print(type(pattern))  # <class 're.Pattern'>
print(pattern)  # re.compile('this')

b = pattern.search(string)
c = pattern.findall(string)
d = pattern.fullmatch(string)
e = pattern.match(string)

print(f"b: {b}")  # <re.Match object; span=(17, 21), match='this'>
print(f"c: {c}")  # ['this']
print(f"d: {d}")  # None
print(f"e: {e}")  # None
