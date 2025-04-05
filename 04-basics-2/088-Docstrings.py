# 088 : Docstrings
# string that occurs as the first statement in
# project, class, method or function definition.
# - Used to document the purpose and usage of the code.
# - Access using the __doc__ attribute.
# - Can be single or multi-line.
# TODO: 3x single quotes or double quotes (before and after the docstring)
"""
This is docstring.
"""


def test(a):
    """
    This is a test function.
    :param a:
    :return:
    """
    print(a)
    return a


test(10)
test("Hello")

help(test)  # TODO: access docstring using help() function
help(len)  # TODO: access docstring using help() function
print(test.__doc__)  # TODO: access docstring using __doc__ attribute
