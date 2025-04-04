# 065 : Truthy vs Falsy
# Truthy:   True, non-zero number, non-empty string,
#           non-empty (list, dict, tuple, set)
# Falsy:    False, 0, '', [], {}, (), set()
# bool()    function can be used to convert values to boolean

# boolean_true = bool(True)
# boolean_false = bool(False)
boolean_true = True
boolean_false = False
print(boolean_true, boolean_false)  # True False

number_true = bool(1)
number_false = bool(0)
print(number_true, number_false)  # True False

string_true = bool("hello")
string_false = bool("")
print(string_true, string_false)  # True False

list_true = bool([1, 2, 3])
list_false = bool([])
print(list_true, list_false)  # True False

dict_true = bool({"a": 1})
dict_false = bool({})
print(dict_true, dict_false)  # True False

tuple_true = bool((1, 2, 3))
tuple_false = bool(())
print(tuple_true, tuple_false)  # True False

set_true = bool({1, 2, 3})
set_false = bool(set())
print(set_true, set_false)  # True False

# [all values are considered "truthy" except for the following, which are "falsy"]
# - None
# 	- False
# 	- Numbers that are numerically equal to zero, including:
#     	0
#     	0.0
#     	0j
#     	decimal.Decimal(0)
#     	fraction.Fraction(0, 1)
# 	- Empty sequences and collections, including:
#     	[] - an empty list
#     	{} - an empty dict
#     	() - an empty tuple
#     	set() - an empty set
#     	'' - an empty str
#     	b'' - an empty bytes
#     	bytearray(b'') - an empty bytearray
#     	memoryview(b'') - an empty memoryview
#     	an empty range, like range(0)
# 	- objects for which
#     	obj.__bool__() returns False
#     	obj.__len__() returns 0, given that obj.__bool__ is undefined

user = "Admin"
password = "1234"
print(bool(user), bool(password))  # True True

if user and password:  # TODO: variables are converted to boolean
    print("You are logged in!")
else:
    print("You are not logged in!")
