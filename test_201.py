# test_201

import importlib
import unittest

# _201 = importlib.import_module("201 - Exercise - Testing")
_201 = importlib.import_module("15-testing.201-Exercise-Testing")


# TODO: standard way to work with unittest
# run_guess(guess, answer)
# - guess: int(input('guess a number 1~10:  '))
# - answer: random.randint(1, 10)
class testGame(unittest.TestCase):

    def test_game(self):  # correct guess = answer
        result = _201.run_guess(5, 5)
        self.assertTrue(result)

    def test_game2(self):
        result = _201.run_guess(0, 5)  # guess < 1
        self.assertFalse(result)

    def test_game3(self):
        result = _201.run_guess(5, 11)  # answer > 10
        self.assertFalse(result)

    def test_game4(self):
        result = _201.run_guess(5, "5")  # answer is a string
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
