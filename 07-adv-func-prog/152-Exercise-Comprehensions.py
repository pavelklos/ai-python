# 152 : Exercise: Comprehensions

# [Exercise Ripl] TODO: without list comprehension ------------------------------
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)

# [Solution Ripl] TODO: with list comprehension ---------------------------------
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

# res = [x for x in some_list if some_list.count(x) > 1]      # ['b', 'b', 'n', 'n']
# res = set(res)                                              # {'b', 'n'}
# res = list(res)                                             # ['b', 'n']
# duplicates = res
# print(duplicates)

duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))  # ['b', 'n']
duplicates = list({x for x in some_list if some_list.count(x) > 1})  # ['b', 'n']
print(duplicates)
