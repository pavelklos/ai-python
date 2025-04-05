# 092 : Walrus Operator
# is a new operator in Python 3.8
# := is called the walrus operator
# It is used to assign values to variables as part of an expression
# It is useful for reducing code duplication
# It is useful for improving readability

a = "helloooooooooo"

# without walrus operator
# TODO: len(a) is used twice
# if (len(a) > 10):
#     print(f"too long {len(a)} elements")

# with walrus operator
if (n := len(a)) > 10:
    print(f"too long {n} elements")

# without walrus operator
# TODO: len(a) is used twice
# while (len(a) > 1):
#     print(len(a))
#     a = a[:-1]  # TODO: remove the last character
#
# print(a)

# with walrus operator
while (n := len(a)) > 1:
    # print(n)
    print(n, a)
    a = a[:-1]  # TODO: remove the last character

print(a)  # finally
