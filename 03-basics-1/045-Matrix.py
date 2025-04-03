# 045 : Matrix
# - is a way to describe a 2D lists or multidimensional lists
# - has a fixed number of rows and columns (rectangular array)
# - is a collection of numbers arranged in rows and columns (rectangle, grid, table)
# - is a way to organize data in columns and rows

matrix = [[1, 2, 3], ["a", "b", "c"], [1.0, 2.0, 3.0]]
print(matrix[0])  # [1, 2, 3]
print(matrix)  # [[1, 2, 3], ['a', 'b', 'c'], [1.0, 2.0, 3.0]]
print(matrix[0][0])  # 1
print(matrix[1][1])  # b
print(matrix[2][2])  # 3.0

# Exercise: Matrix
# using this list:
basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]]
print(basket)  # ['Banana', ['Apples', ['Oranges'], 'Blueberries']]

# access "Oranges" and print it:
print(basket[1])  # ['Apples', ['Oranges'], 'Blueberries']
print(basket[1][1])  # ['Oranges']
print(basket[1][1][0])  # Oranges
