# 085 : return
# TODO: keyword that is used to return a value from a function.
# The value that is returned can be of any data type.
# The return keyword is followed by the value that is to be returned.
# If the return keyword is followed by no value, then the function will return None.

# TODO: function modifies or returns something
# TODO: we should return something from a function


def my_sum(num1, num2):
    """
    This function returns the sum of two numbers.
    :param num1: Any number
    :param num2: Any number
    :return: The sum of num1 and num2
    """
    return num1 + num2  # TODO: it exits the function
    return "unreachable code"  # TODO: unreachable code
    print("unreachable code!")  # TODO: unreachable code


print(
    [1, 2, 3].clear()
)  # TODO: return None (automatically) if there is no return statement
print(my_sum(3, 5))  # TODO: return 8 (there is a return statement)

# TODO: assign the return value to a variable
total = my_sum(3, 5)  # total = 8
print(total)  # 8
print(my_sum(10, total))  # 18
print(my_sum(10, my_sum(3, 5)))  # 18


# TODO: return None if there is no return statement
def my_sum_2(num3, num4):
    def another_func(num3, num4):  # TODO: nested function definition
        return num3 + num4

    return another_func


total_2 = my_sum_2(3, 5)
print(total_2)  # <function my_sum_2.<locals>.another_func at 0x000001403F978B80>
print(total_2(10, 20))  # 30
print(my_sum_2(3, 5)(10, 20))  # 30


def my_sum_3(num5, num6):
    def another_func(n5, n6):  # TODO: nested function definition
        return n5 + n6

    return another_func(num5, num6)


total_3 = my_sum_3(10, 20)
print(total_3)  # 30
