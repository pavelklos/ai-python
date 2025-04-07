# 159 : Exercise: @authenticated

# Create an @authenticated decorator that only allows
# the function to run if user1 has 'valid' set to True
user1 = {
    "name": "Sorna 1",
    "valid": True,  # changing this will either run or not run the message_friends function.
}
user2 = {
    "name": "Sorna 2",
    "valid": False,  # changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    # code here
    def wrapper(*args, **kwargs):
        if args[0]["valid"]:
            return fn(*args, **kwargs)
        else:
            return print("invalid user")

    return wrapper


@authenticated
def message_friends(user):
    print("message has been sent")


# valid user
message_friends(user1)  # message has been sent

# invalid user
message_friends(user2)  # invalid user
