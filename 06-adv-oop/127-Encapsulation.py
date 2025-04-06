# 127 : Encapsulation
# OOP concept that restricts direct access to some of the objects components.


class PlayerCharacter:
    def __init__(self, name, age):
        if age > 18:
            self.name = name
            self.age = age

    def speak(self):
        print(f"My name is {self.name}, and I am {self.age} years old.")


player1 = PlayerCharacter("Tom", 20)
name1 = player1.name  # Tom
age1 = player1.age  # 20
player1.speak()  # My name is Tom, and I am 20 years old.

# TODO: if we don't have actions in class, we can use dictionary instead of class
player2 = {"name": "Tom", "age": 20}
name2 = player2["name"]  # Tom
age2 = player2["age"]  # 20
print(f'My name is {player2["name"]}, and I am {player2["age"]} years old.')
# My name is Tom, and I am 20 years old.
