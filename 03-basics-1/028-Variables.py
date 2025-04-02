# 028 : Variables
#  - are used to store data, and their values can be changed
#  - important concept, first important term in programming

# store and retrieve data by using variables
iq = 190  # store result of IQ test, iq is variable name (value bind to name is 190)
print(iq)  # 190

# rules for variable names
# - snake_case (lowercase with underscores)
# - start with lowercase or underscore
# - letters, numbers, underscores
# - case-sensitive
# - don't overwrite keywords
user_iq: int = 190  # snake_case & type hinting (variable type is int)
print(user_iq)  # 190
user_age = user_iq / 4  # user_age is descriptive
user_iq = user_age * 4  # overwrite variable, reassign value
print(user_iq, user_age)  # 190.0 47.5
_user_iq = 190  # private variable (start with underscore)
a, b, c = 1, 2, 3  # multiple assignment to multiple variables

# 2 gotchas
# constants (variables that should not change)
PI = 3.14159  # uppercase with underscores
PI = 0  # don't change value of constant
# dunder variables (variables) don't create variables with double underscores
__iq__ = 190  # dunder variable (double underscore)

# Python Keywords (reserved words)
# https://www.w3schools.com/python/python_ref_keywords.asp
# print = 190  # don't overwrite built-in functions, keywords

# Copilot rules for variable names
# - must start with letter or underscore
# - can contain letters, numbers, and underscores
# - case-sensitive
# - cannot be a keyword
# - cannot contain spaces
# - should be descriptive
# - should not start with a number
# - should not start with uppercase letter
# - should not contain special characters
