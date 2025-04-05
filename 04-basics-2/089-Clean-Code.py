# 089 : Clean Code
# # - Readability is important.
# # - Use meaningful names.
# # - Use whitespace properly.
# # - Use comments.
# # - Use docstrings.


def is_even(num):
    """
    This function returns whether the number is odd or even.
    :param num: int
    :return: bool
    """

    # TODO: before
    # if num % 2 == 0:        # modulo operator
    #     return True         # 'Even' 0, 2, 4, 6, 8, 10, etc.
    # elif num % 2 == 1:
    #     return False        # 'Odd'  1, 3, 5, 7, 9, 11, etc.

    # TODO: before
    # if num % 2 == 0:        # modulo operator
    #     return True         # 'Even' 0, 2, 4, 6, 8, 10, etc.
    # return False            # 'Odd'  1, 3, 5, 7, 9, 11, etc.

    # TODO: after
    return num % 2 == 0


print(is_even(10))  # True
print(is_even(11))  # False
