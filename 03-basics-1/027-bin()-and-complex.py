# 027 : bin() and complex
# extra data types

# complex
complex(real=0, imag=0)  # complex number
complex(1, 2)  # 1 + 2j
complex("1+2j")  # 1 + 2j
print(complex(1, 2))  # (1+2j)
print(complex("1+2j"))  # (1+2j)
print(complex(1, 2) == complex("1+2j"))  # True
print(complex(1, 2) == 1 + 2j)  # True
print(1 + 2j)  # (1+2j)
print(type(1 + 2j))  # <class 'complex'>

# bin
bin(5)  # 0b101     0b is a prefix for binary numbers, 101 is 5 in binary
print(bin(5))  # 0b101
print(bin(5)[2:])  # 101
print(0b101 + 0b100)  # 5+4 = 9
print(bin(5 + 4))  # 0b1001
print(bin(5 + 4)[2:])  # 1001
print(type(bin(5)))  # <class 'str'>
print(type(0b101))  # <class 'int'>
print(0b101)  # 5

# int
int("0b101", 2)  # 5         0b is a prefix for binary numbers, 101 is 5 in binary
print(int("0b101", 2))  # 5
print(int("101", 2))  # 5
print(int("101", base=2))  # 5
print(type(int("101", base=2)))  # <class 'int'>
