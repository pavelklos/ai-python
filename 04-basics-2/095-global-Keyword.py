# 095 : global Keyword
# use the global keyword to change a global variable inside a function
# we can use dependency injection by passing variable to function as parameter

a = 10


def confusion(b):  # TODO: parameter 'b' is local variable in function
    print(b)
    a = 90


confusion(300)  # 300

total = 0


def count():
    # total = 0
    global total  # TODO: global keyword is used to access global variable
    total += 1
    return total


print(count())  # 1
print(count())  # 2
print(count())  # 3

total_2 = 0


def count_2(total_2):  # TODO: dependency injection of variable
    total_2 += 1
    return total_2


print(count_2(count_2(count_2(total_2))))  # 3
print(total_2)  # 0
total_2 = 100
print(count_2(count_2(count_2(100))))  # 103
