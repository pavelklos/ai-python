# 063 : Conditional Logic

# True, False are boolean values
is_old = False
is_licensed = True

# keywords: if, elif, else
# is_old is expression that produces a value
# we can control the flow of our program based on conditions
# column ':' and indentation (4 spaces) are used to define block of code
if is_old and is_licensed:
    print("You can drive now!")
elif not is_old:
    print("You are not old enough to drive!")
elif not is_licensed:
    print("You are not licensed to drive!")
else:
    print("You cannot drive!")
print("new line after if block")
