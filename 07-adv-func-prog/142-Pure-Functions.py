# 142 : Pure Functions
# TODO: functions that given the same input, will always return the same output.
# two main benefits:
# 1. given the same input, will always return the same output
# 2. do not produce side effects (e.g. changing global variables)
#    side effect affects the outside world (e.g. print to screen, write to file, etc.)

# TODO: Functional programming: use pure functions as much as possible

glob_var = 0


# pure function
def multiply_by2(li):
    # new_list = []
    # for item in li:
    #     new_list.append(item*2)
    # return new_list

    # TODO: print() is side effect (like changing global variables)
    # print('hello')
    # glob_var += 1

    # optimized version
    return [item * 2 for item in li]


res1 = multiply_by2([1, 2, 3])  # [2, 4, 6]
res2 = multiply_by2([2, 4, 6])  # [4, 8, 12]
print(res1)
print(res2)
