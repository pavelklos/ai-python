# 033 : Type Conversion
# - is the process of converting the value of one data type
#   (integer, string, float, etc.) to another data type

str(100)  # '100'
int("100")  # 100
float("100")  # 100.0
int(100.5)  # 100
int("110", 2)  # 6 (base = 2)
int("110", 8)  # 72 (base = 8)
int("110", 10)  # 110 (base = 10)
int("110", 16)  # 272 (base = 16)

print(type(str(100)))  # <class 'str'>
print(type(int("100")))  # <class 'int'>
print(type(float("100")))  # <class 'float'>
print(type(int(100.5)))  # <class 'int'>
print(type(int("110", 2)))  # <class 'int'>

a = str(100)
b = int(a)
c = type(b)
print(c)  # <class 'int'>
print(type(c))  # <class 'type'>
# - type conversion is also known as type casting
