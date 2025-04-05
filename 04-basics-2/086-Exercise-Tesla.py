# 086 : Exercise: Tesla
# It's time for a little exercise! You just got employed by Tesla,
# and you need to solve a problem for their self driving car:


age = input("What is your age?: ")

if int(age) < 18:
    print("Sorry, you are too young to drive this car. Powering off")
elif int(age) > 18:
    print("Powering On. Enjoy the ride!")
elif int(age) == 18:
    print("Congratulations on your first year of driving. Enjoy the ride!")


# 1. Wrap the above code in a function called checkDriverAge().
#    Whenever you call this function, you will get prompted for age.
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

# 2. Instead of using the input().
#    Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#    checkDriverAge(92);


# 1. Solution
def checkDriverAge_1():
    age = input("What is your age?: ")
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


# 2. Solution
def checkDriverAge_2(age=0):
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


checkDriverAge_1()
checkDriverAge_2()  # default parameter value is 0
checkDriverAge_2(55)
