# 069    : Exercise: Logical Operators
is_magician = True
is_expert = False

# check if magician AND expert: "You are a master magician"
# check if magician but not expert: "At least you're getting there"
# if you're not a magician: "You need magic powers"

if is_magician and is_expert:
    print("You are a master magician")

# elif is_magician or is_expert:
elif (
    is_magician and not is_expert
):  # TODO: better to use 'and' instead of 'or' (more readable)
    print("At least you're getting there")

# else:
elif not is_magician:  # TODO: better to use 'not' instead of else (more readable)
    print("You need magic powers")

# it's possible write code in many ways, but it's better to write it
# in a way that is more readable and understandable
