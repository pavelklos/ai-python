# 162 : Error Handling 2


def sum(num1, num2):
    try:
        return num1 + num2
    # except TypeError as err:
    #     print(f"Please enter numbers only: {err}")
    except (ValueError, TypeError) as err:  # TODO: we can combine multiple exceptions
        print(err)


print(sum(1, 2))  # 3 TODO: (number addition)
print("1", "2")  # 12 TODO: (string concatenation)
print(
    sum("1", 2)
)  # Please enter numbers only: can only concatenate str (not "int") to str
print(
    sum(1, "2")
)  # Please enter numbers only: unsupported operand type(s) for +: 'int' and 'str
