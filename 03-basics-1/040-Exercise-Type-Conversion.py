# 040 : Exercise: Type Conversion
# - type conversion is the process of converting the value of one data type to another data type
# Python Types:
# Numbers, Strings, Boolean, Lists, Tuples, Sets, Dictionaries, None

name = "John Doe"
age = 55
relationship_status = "single"
relationship_status = "it's complicated"
print(relationship_status)  # it's complicated

birth_year = input("what year were you born? ")  # 1969
# age = 2024 - birth_year  # TypeError: unsupported operand type(s) for -: 'int' and 'str'
age = 2024 - bool(birth_year)  # 2023
age = 2024 - int(birth_year)  # 55
age = 2024 - float(birth_year)  # 55.0
print(type(birth_year))  # <class 'str'>
print(age)  # 55.0
print(type(age))  # <class 'float'>
print(f"your age is {age}")  # your age is 55.0

# Python data types
print(bool(True))  # True
print(int(4))  # 4
print(float(4))  # 4.0
print(complex(4))  # (4+0j)
print(str(4))  # 4
print(list((1, 2, 3)))  # [1, 2, 3]
print(tuple([1, 2, 3]))  # (1, 2, 3)
print(set([1, 2, 3]))  # {1, 2, 3}
print(dict(a=1, b=2, c=3))  # {'a': 1, 'b': 2, 'c': 3}

print(type(4e2))  # <class 'float'>
print(bin(512))  # 0b1000000000
print(hex(512))  # 0x200
print(oct(512))  # 0o1000
print(int(0b1000000000))  # 512
print(int(0x200))  # 512
print(int(0o1000))  # 512
