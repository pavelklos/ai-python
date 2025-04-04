# 073 : Exercise: Tricky Counter
# my_list [] contains 10 numbers (1 to 10)
# we need to count the sum of all items in my_list
# use looping to iterate over my_list and sum all items

# Solution:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0  # TODO: counter must be outside of loop

# TODO: Using for loop
for item in my_list:
    counter = counter + item
print(counter)

# TODO: Using sum() function
counter = sum(my_list)
print(counter)

# TODO: Using list comprehension and sum() function
# counter = [item for item in my_list]  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = sum([item for item in my_list])
print(counter)
