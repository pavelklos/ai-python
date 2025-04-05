# 091 : Exercise: Functions

# Exercise Functions
# Highest Even: Write a function to find the highest even number from the list.


def highest_even(li):
    # evens = []
    # for item in li:
    #     if item % 2 == 0:
    #         evens.append(item)
    # if evens:  # return max(evens) if evens else None
    #     return max(evens)
    # else:
    #     return None

    evens = [item for item in li if item % 2 == 0]
    # odds = [item for item in li if item % 2 != 0]
    # print(evens)
    # print(odds)
    return max(evens) if evens else None  # TODO: check if evens is empty


print(highest_even([10, 2, 3, 4, 8, 11]))  # 10
print(highest_even([1, 3, 5, 7, 9]))  # None
