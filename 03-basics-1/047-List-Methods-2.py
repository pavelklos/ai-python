# 047 : List Methods 2

# Index (is a way to access an element in a list)
basket = [1, 2, 3, 4, 5]
basket.index(2)  # 1
basket.index(5)  # 4
basket.index(3, 0, 3)  # 2
# basket.index(100)  # ValueError: 100 is not in list
basket = ["a", "b", "c", "d", "e"]  # ['a', 'b', 'c', 'd', 'e']
basket.index("d")  # 3
# basket.index("d", 0, 3)  # ValueError: 'd' is not in list
# basket.index("z")  # ValueError: 'z' is not in list

# check if an item exists in a list
# - in is a Python keyword (check True or False)
print("x" in [1, 2, 3])  # False
print("x" in ["x", "y", "z"])  # True
print("a" in "Hello, World!")  # False
# - count is a Python method (check the number of occurrences)
print(basket.count("d"))  # 1
print("Hello, World!".count("l"))  # 3

# Exercise List Methods
# using this list
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# 1. Remove the Banana from the list
basket.remove("Banana")  # ['Apples', 'Oranges', 'Blueberries']
# 2. Remove "Blueberries" from the list.
basket.remove("Blueberries")  # ['Apples', 'Oranges']
# 3. Put "Kiwi" at the end of the list.
basket.append("Kiwi")  # ['Apples', 'Oranges', 'Kiwi']
# 4. Add "Apples" at the beginning of the list
basket.insert(0, "Apples")  # ['Apples', 'Apples', 'Oranges', 'Kiwi']
print(basket)  # ['Apples', 'Apples', 'Oranges', 'Kiwi']
# 5. Count how many apples in the basket
basket.count("Apples")  # 2
print(basket.count("Apples"))  # 2
# 6. Empty the basket
basket.clear()  # []
print(basket)
