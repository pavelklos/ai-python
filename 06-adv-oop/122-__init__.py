# 122 : __init__


class PlayerCharacter:
    membership = True  # TODO: class object attribute

    def __init__(self, name="anonymous", age=0):  # TODO: default values
        if age > 18:
            self.name = name
            self.age = age

    def shout(self):
        print(f"My name is {self.name}")


player1 = PlayerCharacter("Tom", 20)
print(player1.shout())

player2 = PlayerCharacter("Jill", 10)
# print(player2.shout()) # TODO: AttributeError: 'PlayerCharacter' object has no attribute 'name'
