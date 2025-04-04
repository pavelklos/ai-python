# 074 : range()
# function that generates sequence of numbers from start to stop
# function takes three argument
# mostly used in for loops, we can iterate over range (sequence of numbers)
# range(start, stop, step)
# start : optional (default is 0)
# stop  : required
# step  : optional (default is 1)

rng = range(10)  # range(0, 10)  # range(0, 10, 1)
print(range(10) == range(0, 10) == range(0, 10, 1))  # True
print(type(rng))  # <class 'range'> is special iterable type of object

# for number in range(0, 10, 1):
# for number in range(0, 10):
# for number in range(10):
for number in rng:
    print(number)  # 0 1 2 3 4 5 6 7 8 9
for _ in rng:  # _ is a convention for unused variable
    # print(_)
    print("do something")  # do something TODO: 10 times

for number in range(0, 10, 2):
    print(number)  # 0 2 4 6 8
for number in range(10, 0):
    print(number)  # empty TODO: we need to use negative step
for number in range(0, 10, -2):
    print(number)  # empty TODO: we need to change start and stop
for number in range(10, 0, -2):
    print(number)  # 10 8 6 4 2

for _ in range(2):
    print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] TODO: 2 times
