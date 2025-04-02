# 024 : Operator Precedence

print(20 + 3 * 4)  # 32    multiply evaluated first
print((20 + 3) * 4)  # 92    parentheses evaluated first
print((20 - 3) + 2**2)  # 21    parentheses first, power of second, plus last

#   ()            parentheses
#   **            power of
#   * / // %      multiply, divide, floor division, rest of division (modulo)
#   + -           plus, minus
