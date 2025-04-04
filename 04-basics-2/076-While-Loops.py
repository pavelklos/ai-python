# 076 : While Loops
# can iterate over sequence (list, tuple, dictionary, set or string)
# is used when we don't know number of iterations
# can be used with else block

i = 0
while i < 50:
    print(i)
    i += 1
    # break
else:
    print(
        "done with all the work"
    )  # TODO: if we use break, else block will not execute

# i = 0  # TODO: infinite loop until program crashes or we stop it
# while i < 50:
#     print(i)
