# 067 : Short Circuiting
# is way to optimize our code by checking the most likely condition first
# keywords: and, or

is_friend = True
is_user = True
print(is_user and is_friend)  # True

if is_friend and is_user:  # TODO: is_user is not checked if is_friend is False
    print("Best friend and user")

if is_friend or is_user:  # TODO: is_user is not checked if is_friend is True
    print("Best friend or user or both")
