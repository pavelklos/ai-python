# 183 : Useful Modules 2
# - Python has a lot of built-in modules that you can use directly.
# - You can also install third-party modules using pip.

# TODO: built-in modules -------------------------------------------------------
# - datetime: module supplies classes for manipulating dates and times.

import datetime

print(datetime.time())  # 00:00:00
print(datetime.time(5, 45, 2))  # 05:45:02

print(datetime.date.today())  # 2025-04-08
print(datetime.datetime.now())  # 2025-04-08 10:22:09.759876
print(datetime.datetime.now().year)  # 2025

# TODO: built-in modules -------------------------------------------------------
# - time: module provides various time-related functions.

import time

print(time.time())  # 1744100529.7608745 (seconds since from: 1970-01-01 00:00:00)

# TODO: built-in modules -------------------------------------------------------
# - array: module defines an object type that can compactly represent an array of basic values.
# TODO: Python list vs array module
# - list can store different data types TODO: (more memory, slower)
# - array can store only one data type TODO: (less memory, faster)

from array import array

arr1 = array("i", [1, 2, 3, 4, 5])  # 'i' = integer (type code as first argument)
arr2 = array(
    "d", [1.1, 2.2, 3.3, 4.4, 5.5]
)  # 'd' = double (type code as first argument)
arr3 = array(
    "u", ["a", "b", "c", "d", "e"]
)  # 'u' = unicode (type code as first argument)
print(arr1[0])  # 1
print(arr2[0])  # 1.1
print(arr3[0])  # a
print(arr1)  # TODO: array('i', [1, 2, 3, 4, 5])
print(list(arr1))  # TODO: [1, 2, 3, 4, 5]
