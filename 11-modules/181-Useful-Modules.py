# 181 : Useful Modules
# - Python has a lot of built-in modules that you can use directly.
# - You can also install third-party modules using pip.

# TODO: built-in modules -------------------------------------------------------
# TODO: Specialized data types
# - collections (package)
#   - Counter, defaultdict, OrderedDict      # classes, functions

from collections import Counter, OrderedDict, defaultdict

li = [1, 2, 3, 4, 5, 6, 7, 7]
sentence = "This is sentence"
print(Counter(li))  # Counter({7: 2, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})
print(
    Counter(sentence)
)  # Counter({' ': 2, 'e': 3, 's': 3, 'i': 2, 'T': 1, 'h': 1, 'n': 1, 't': 1, 'c': 1})

dict1 = {"a": 1, "b": 2}
print(dict1["a"])  # 1
# print(dict1['c'])                                       # TODO: KeyError: 'c'
dict2 = defaultdict(int, dict1)  # TODO: int = int() = 0
print(dict2["a"])  # 1
print(dict2["c"])  # 0
dict3 = defaultdict(lambda: 5, dict1)  # TODO: lambda: 5 = lambda: return 5
print(dict3["a"])  # 1
print(dict3["c"])  # 5

# OrderDict: remembers the order in which the items were inserted
d = OrderedDict()
d["a"] = 1
d["b"] = 2
d2 = OrderedDict()  # change the order of the insertion
d2["b"] = 2
d2["a"] = 1
print(d == d2)  # False (they are not equal)

print(type(Counter(li)))  # <class 'collections.Counter'>
print(type(defaultdict(int, dict1)))  # <class 'collections.defaultdict'>
print(type(OrderedDict()))  # <class 'collections.OrderedDict'>
