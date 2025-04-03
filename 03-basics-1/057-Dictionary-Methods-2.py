# 057 : Dictionary Methods 2

dictionary = {"basket": [1, 2, 3], "greet": "Hello", "age": 25}
dictionary = dict(basket=[1, 2, 3], greet="Hello", age=25)

print("i" in "Hi")  # True
print("i" in "Hello")  # False
print("greet" in dictionary)  # True
print("city" in dictionary)  # False

print(dictionary.keys())  # dict_keys(['basket', 'greet', 'age'])
print(dictionary.values())  # dict_values([[1, 2, 3], 'Hello', 25])
print(
    dictionary.items()
)  # dict_items([('basket', [1, 2, 3]), ('greet', 'Hello'), ('age', 25])
# TODO: method items() returns a list of tuples

dictionary2 = dictionary.copy()  # creates a copy of the dictionary
dictionary.clear()  # clears the dictionary
print(dictionary)  # {}
print(dictionary2)  # {'basket': [1, 2, 3], 'greet': 'Hello', 'age': 25}
dictionary2.pop("basket")  # removes the key and returns the value
print(dictionary2)  # {'greet': 'Hello', 'age': 25}
dictionary2.popitem()  # removes some key-value pair and returns it (not the last one)
# TODO: from Python 3.7 onwards, it removes the last key-value pair
print(dictionary2)  # {'greet': 'Hello'}
dictionary2.update({"city": "New York"})  # adds a key-value pair
print(dictionary2)  # {'greet': 'Hello', 'city': 'New York'}
dictionary2.update({"city": "Prague"})  # updates the value of the key
print(dictionary2)  # {'greet': 'Hello', 'city': 'Prague'}

# Exercise Dictionary Methods
# 1 Create a user profile for your new game.
#   This user profile will be stored in a dictionary with keys:
#   'age', 'username', 'weapons', 'is_active' and 'clan'
# 2 iterate and print all the keys in the above user.
# 3 Add a new weapon to your user
# 4 Add a new key to include 'is_banned'. Set it to false
# 5 Ban the user by setting the previous key to True
# 6 create a new user2 by copying the previous user and update the age value and username value.

# ANSWERS BELOW:
# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys:
# 'age', 'username', 'weapons', 'is_active' and 'clan'
user_profile = {
    "age": 0,
    "username": " ",
    "weapons": None,
    "is_active": False,
    "clan": None,
}
# 2 iterate and print all the keys in the above user.
print(user_profile.keys())
# 3 Add a new weapon to your user
user_profile["weapons"] = "Katana"
# 4 Add a new key to include 'is_banned'. Set it to false
user_profile.update({"is_banned": False})
# 5 Ban the user by setting the previous key to True
user_profile["is_banned"] = True
# 6 create a new user2 by copying the previous user and update the age value and username value.
user2 = user_profile.copy()
user2.update({"age": 50, "username": "User2"})
print(user_profile)
print(user2)
