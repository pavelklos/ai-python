# 201 : Exercise: Testing

# TODO: [Exercise] -------------------------------------------------------------
# while cycle

import sys
from random import randint

# generate a number 1~10
answer = randint(1, 10)

# input from user?
# check that input is a number 1~10
# while True:
#     try:
#         guess = int(input('guess a number 1~10:  '))
#         if 0 < guess < 11:
#             if guess == answer:
#                 print('you are a genius!')
#                 break
#         else:
#             print('hey bozo, I said 1~10')
#     except ValueError:
#         print('please enter a number')
#         continue

# TODO: [Solution] -------------------------------------------------------------
# while cycle rewritten as a pure function

import random


def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print("you are a genius!")
            return True
    else:
        print("hey bozo, I said 1~10")
        return False


# run this code only if it is run directly
if __name__ == "__main__":
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input("guess a number 1~10:  "))
            if run_guess(guess, answer):
                break
        except ValueError:
            print("please enter a number")
            continue

"""
we test a function at a time.
that is why it is called unit testing.
hence we try to make pure functions and test them.
"""
