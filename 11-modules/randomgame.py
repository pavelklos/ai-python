# 177 : Exercise: Guessing Game
# 1. generate a number 1~10
# 2. input from user (by argv)
# 3. check that input is a number 1~10
# 4. check if the number is the right guess, otherwise ask again
# 5. if correct, print "You're a genius!"

# TODO: you have to run this file from the terminal with the following command:
# - python randomgame.py 1 10
# - 1 10 are range (from 1 to 10)

import sys
from argparse import ArgumentError
from random import randint

# TODO: check if user run this file with correct arguments
print(sys.argv)
if len(sys.argv) != 3:
    print("Usage: randomgame.py [first number] [second number]")
    # sys.exit(1)
    raise ArgumentError(None, "Usage: randomgame.py [first number] [second number]")

random_number = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        number = int(
            input(
                "Please choose a number that falls between those two you just chose: "
            )
        )
        # if number >= int(sys.argv[1]) and number <= int(sys.argv[2]):
        if int(sys.argv[1]) <= number <= int(sys.argv[2]):
            if number == random_number:
                print("You're a genius!")
                break
    except ValueError:
        print("Please enter a number")
        continue
