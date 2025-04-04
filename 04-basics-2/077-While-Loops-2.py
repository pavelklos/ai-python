# 077 : While Loops 2
# when use for loop and when to use while loop?
# for loop is used when we know number of iterations
# while loop is used when we don't know number of iterations
# TODO: for loop is more simpler and readable
# TODO: while loop is more powerful
# TODO: while loop can be used with else block
# TODO: while loop can be used with break statement

# TODO: for loop
for i in range(3):
    print(i)  # 0 1 2
# TODO: while loop
i = 0
while i < 3:
    print(i)  # 0 1 2
    i += 1

my_list = [1, 2, 3]
# TODO: for loop
for item in my_list:
    print(item)  # 1 2 3
# TODO: while loop
i = 0
while i < len(my_list):
    print(my_list[i])  # 1 2 3
    i += 1

# TODO: while loop with input
while True:  # TODO: infinite loop
    response = input("say something: ")  # TODO: prompt user to say something
    if response == "bye":
        break
    print(response)
