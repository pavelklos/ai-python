# 147 : Exercises: map, filter, zip, reduce

from functools import reduce

# 1 Capitalize all the pet names and print the list ------------------------------------------------
my_pets = ["sisi", "bibi", "titi", "carla"]


def capitalize(string):
    return string.upper()


print(list(map(capitalize, my_pets)))
# TODO: ['SISI', 'BIBI', 'TITI', 'CARLA']

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest -------------
my_strings = ["a", "b", "c", "d", "e"]
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))
# TODO: [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

# 3 Filter the scores that pass over 50% -----------------------------------------------------------
scores = [73, 20, 65, 19, 76, 100, 88]


def is_smart_student(score):
    return score > 50


print(list(filter(is_smart_student, scores)))
# TODO: [73, 65, 76, 100, 88]

# 4 Combine all the numbers that are in a list on this file using reduce (my_numbers and scores) ----
#   What is the total?


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, (my_numbers + scores)))
# TODO: 456
