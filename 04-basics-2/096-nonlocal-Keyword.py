# 096 : nonlocal Keyword
# use the nonlocal keyword to change a variable inside a nested function


# Scope - what variables do I have access to?
def outer():
    x = "local"

    def inner():
        nonlocal x  # nonlocal keyword is used to access variable in outer function
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()  # inner: nonlocal, # outer: nonlocal

# Rules:
# 1. Start with local
# 2. Parent local
# 3. Global
# 4. Built-in Python functions  # sum(), print(), etc.
