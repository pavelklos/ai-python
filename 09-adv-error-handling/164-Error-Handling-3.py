# 164 : Error Handling 3
# TODO: we can raise exceptions (errors), bult-in or custom


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("b cannot be zero")  # raise built-in exception
    return a / b


try:
    print(divide(10, 0))
except ZeroDivisionError as e:
    print(e)
    print("Please don't divide by zero")  # TODO: we can add custom message
