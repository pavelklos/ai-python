# 056 : Dictionary Methods

dictionary = {"basket": [1, 2, 3], "greet": "Hello", "age": 25}
print(dictionary["basket"])  # [1, 2, 3]
print(dictionary.get("age"))  # 25
print(dictionary.get("price"))  # None
print(
    dictionary.get("price", "There is no such key")
)  # TODO: default value 'There is no such key'

dictionary = dict(
    name="Joe", age=25, city="New York"
)  # TODO" another way to create a dictionary
print(dictionary)  # {'name': 'Joe', 'age': 25, 'city': 'New York'}

# TODO: [pyflakes] is a Python static code analysis tool that helps you find errors in your code.
