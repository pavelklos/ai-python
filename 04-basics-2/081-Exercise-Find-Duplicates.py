# 081 : Exercise: Find Duplicates

# [Exercise]
# check for duplicates in list

# [Solution]
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:  # TODO: number of occurrences of value in list
        if value not in duplicates:  # TODO: check if value is not already in duplicates
            duplicates.append(value)  # TODO: add value to duplicates

print(type(duplicates))  # <class 'list'>
print(len(duplicates))  # 2
print(duplicates)  # ['b', 'n']

# easier solution by using set
duplicates = set([value for value in some_list if some_list.count(value) > 1])
print(duplicates)  # {'b', 'n'}
