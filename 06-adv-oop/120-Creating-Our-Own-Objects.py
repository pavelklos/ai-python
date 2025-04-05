# 120 : Creating Our Own Objects


class PlayerCharacter:
    def __init__(self, name, age):  # constructor method
        self.name = name
        self.age = age

    def run(self):
        print("Run")
        # return 'done'


player1 = PlayerCharacter("Cindy", 44)
player2 = PlayerCharacter("Tom", 21)
player2.attack = 50  # dynamically add attribute to object

# TODO: different memory locations
print(player1)  # <__main__.PlayerCharacter object at 0x7f8b1b3b5d30>
print(player2)  # <__main__.PlayerCharacter object at 0x7f8b1b3b5d60>

print(player1.name)  # Cindy
print(player2.name)  # Tom
print(player1.age)  # 44
print(player2.age)  # 21
player1.run()  # Run
# print(player1.attack)  # TODO: AttributeError: 'PlayerCharacter' object has no attribute 'attack'
print(player2.attack)  # 50

help(player2)  # TODO: shows all attributes and methods of object

print(player2.__dict__)  # {'name': 'Tom', 'age': 21, 'attack': 50}
print(player2.__weakref__)  # None
