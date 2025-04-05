# 121 : Attributes and Methods


class PlayerCharacter:
    membership = True  # class object attribute

    def __init__(self, name, age):
        # if PlayerCharacter.membership:  # or self.membership
        if self.membership:  # or PLayerCharacter.membership
            self.name = name  # class attribute
            self.age = age  # class attribute

    def shout(self):  # method
        print(f"My name is {self.name}")

    def run(self, hello):  # method
        print(f"{hello} {self.name}")

    def print(self):  # method
        print(self.membership, "\t", self.name, "\t", self.age)

    # define __str__ method
    # Returns a human-readable, or informal, string representation of an object.
    # This method is called by the built-in print(), str(), and format() functions.
    def __str__(self):  # method
        return f"{self.name} is {self.age} years old."


player1 = PlayerCharacter("Cindy", 44)
player1.shout()
player1.run("Hi")
# print(player1.membership, '\t', player1.name, '\t', player1.age)
player1.print()

player1.membership = False
player1.print()

# TODO: shows all attributes and methods of object
# help(player1)
# help(list)

# define __str__ method
# Returns a human-readable, or informal, string representation of an object.
# This method is called by the built-in print(), str(), and format() functions.
print(player1)  # Cindy is 44 years old.
print(str(player1))  # 'Cindy is 44 years old.'
print(format(player1))  # 'Cindy is 44 years old.'
