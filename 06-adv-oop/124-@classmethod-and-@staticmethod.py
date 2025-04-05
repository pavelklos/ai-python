# 124 : @classmethod and @staticmethod
# TODO: @classmethod and @staticmethod are decorators that are used to define methods inside a class.
# @classmethod is used when you want to return the class itself.
# @staticmethod is used when you don't want to return the class itself.
# TODO: we can call them without instantiating the class.
# TODO: @classmethod has access to the class itself (using cls) while @staticmethod does not.


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod  # TODO: class method (cls)
    def adding_things(cls, num1, num2):
        # print(type(cls))  # <class 'type'>
        return cls("Teddy", num1 + num2)  # TODO: Instantiating the class

    @staticmethod  # TODO: static method (no cls or self)
    def adding_things2(num1, num2):
        return num1 + num2


player3 = PlayerCharacter.adding_things(
    2, 3
)  # TODO: Instantiated class using @classmethod
print(player3)  # <__main__.PlayerCharacter object at 0x000001E3D3D3A4C0>
print(player3.name)  # Teddy
print(player3.age)  # 5

print(PlayerCharacter)  # <class '__main__.PlayerCharacter'>
print(player3)

print(
    PlayerCharacter.adding_things2(5, 9)
)  # TODO: using @staticmethod by calling the class itself
