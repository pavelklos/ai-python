# 075 : enumerate()
# function takes collection (e.g. a tuple) and returns it as enumerate object
# useful if we need index counter and value in loop

print(enumerate("abc"))  # <enumerate object at 0x0000021C35BB9670>
print(type(enumerate("abc")))  # <class 'enumerate'>

for char in "abc":  # TODO: we get values
    print(char)  # a b c
for char in enumerate("abc"):  # TODO: we get tuples (index, value)
    print(char)  # (0, 'a') (1, 'b') (2, 'c')
for i, char in enumerate("abc"):  # TODO: we can unpack tuples
    print(i, char)  # 0 a 1 b 2 c

for number in enumerate([1, 2, 3]):  # TODO: we can unpack tuples
    print(number)  # (0, 1) (1, 2) (2, 3)
for i, number in enumerate([1, 2, 3]):  # TODO: we can unpack tuples from (list)
    print(i, number)  # 0 1 1 2 2 3
for i, number in enumerate((1, 2, 3)):  # TODO: we can unpack tuples from (tuple)
    print(i, number)  # 0 1 1 2 2 3
for i, number in enumerate({1, 2, 3}):  # TODO: we can unpack tuples from (set)
    print(i, number)  # 0 1 1 2 2 3

for i, number in enumerate(list(range(100))):
    if number == 0:
        print(f"index of 0 is: {i}")  # index of 0 is: 0
    if number == 50:
        print(f"index of 50 is: {i}")  # index of 50 is: 50
