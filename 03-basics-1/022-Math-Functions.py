# 022 : Math Functions

import math

# basic operations (actions)
print(2 + 4)
print(2 - 4)
print(2 * 4)
print(2 / 4)
print(type(2 / 4))  # <class 'float'> for 0.5

print(2**3)  # 2^3 = 8           double multiply = power of
print(9 // 2)  # 9/2 = 4.5, 4      double slash = floor division
print(9 % 2)  # 9/2 = 4.5, 1      percent sign = rest of division

# math functions (actions)
print(round(3.141592))  # 3         down to 0th decimal
print(round(3.141592, 2))  # 3.14      down to 2nd decimal
print(round(3.141592, 4))  # 3.1416    up to 4th decimal
print(abs(-3))  # 3         absolute value

print(pow(2, 3))  # 2^3 = 8
print(max(2, 3))  # 3
print(min(2, 3))  # 2
print(sum([1, 2, 3, 4, 5]))  # 15
print(sum([1, 2, 3, 4, 5], 10))  # 25
print(sum([1, 2, 3, 4, 5], -10))  # 5
print(math.pi)  # π = 3.141592653589793 (ludolf's number)
print(math.tau)  # τ = 6.283185307179586 (tau's number)
print(math.e)  # e = 2.718281828459045 (euler's number)
