# 151 : Set and Dictionary Comprehension

# TODO: Set comprehension -------------------------------------------------------
# without set comprehension
my_set = set()
for char in "hello":
    my_set.add(char)
print(my_set)  # TODO: CHECK unordered {'l', 'o', 'e', 'h'}  # {'h', 'e', 'o', 'l'} ...

# with set comprehension
my_set = {char for char in "hello"}  # {'h', 'e', 'l', 'o'}

# set comprehension and TODO: operation
# Syntax: TODO: {expression for item in iterable}
{num * 2 for num in range(0, 5)}  # {0, 2, 4, 6, 8}
{num**2 for num in range(0, 5)}  # {0, 1, 4, 9, 16}

# set comprehension and TODO: operation, condition (if)
# Syntax: TODO: {expression for item in iterable if condition}
{num**2 for num in range(0, 5) if num % 2 == 0}  # {0, 4, 16}
{num**2 for num in range(0, 5) if num % 2 != 0}  # {1, 9}

# set comprehension and TODO: operation, condition (if-else)
# Syntax: TODO: {expression if condition else expression for item in iterable}
{num**2 if num % 2 == 0 else num * 2 for num in range(0, 5)}  # {0, 2, 4, 9, 16}

# TODO: Dictionary comprehension ------------------------------------------------
# without dictionary comprehension
simple_dict = {"a": 1, "b": 2}
my_dict = {}
for key, value in simple_dict.items():
    my_dict[key] = value * 2
print(my_dict)  # {'a': 2, 'b': 4}

# with dictionary comprehension
my_dict = {key: value * 2 for key, value in simple_dict.items()}  # {'a': 2, 'b': 4}

# dictionary comprehension and TODO: operation
# Syntax: TODO: {key: expression for item in iterable}
{num: num * 2 for num in [1, 2, 3]}  # {1: 2, 2: 4, 3: 6}
{num: num**2 for num in [1, 2, 3]}  # {1: 1, 2: 4, 3: 9}

# dictionary comprehension and TODO: operation, condition (if)
# Syntax: TODO: {key: expression for item in iterable if condition}
{num: num**2 for num in [1, 2, 3] if num % 2 == 0}  # {2: 4}

# dictionary comprehension and TODO: operation, condition (if-else)
# Syntax: TODO: {key: expression if condition else expression for item in iterable}
{num: num**2 if num % 2 == 0 else num * 2 for num in [1, 2, 3]}  # {1: 2, 2: 4, 3: 6}

# TODO: other examples ----------------------------------------------------------
{num for num in [1, 2, 3, 1]}  # {1, 2, 3} TODO: set removes duplicates
[num for num in [1, 2, 3, 1]]  # [1, 2, 3, 1] TODO: list does not remove duplicates
simple_dict = {"a": 0, "b": 1}
{key: value**2 for key, value in simple_dict.items()}  # {'a': 0, 'b': 1}
{key: value**2 for key, value in simple_dict.items() if value % 2 == 0}  # {'a': 0}
{
    key: value**2 if value % 2 == 0 else value * 2 for key, value in simple_dict.items()
}  # {'a': 0, 'b': 2}
# create simple_dict with zip() and range()
{key: value**2 for key, value in zip(["a", "b"], range(2))}  # {'a': 0, 'b': 1}
{key: value**2 for key, value in zip(["a", "b"], range(2, 4))}  # {'a': 4, 'b': 9}
