# 129 : Private vs Public Variables
# TODO: are used to indicate the access level of the variable.
# private:      __variable
# protected:     _variable
# public:         variable
# __, _ means that the variable is private or protected and don't touch it (only convention)


class PlayerCharacter:
    def __init__(self, name, age):
        if age > 18:
            self._name = name  # TODO: protected (only convention & get warning)
            self._age = age  # TODO: protected (only convention & get warning)
            self.__private_name = name  # TODO: private (only convention & get warning)
            self.__private_age = age  # TODO: private (only convention & get warning)

    def speak(self):
        print(f"My name is {self._name}, and I am {self._age} years old.")


player1 = PlayerCharacter("Tom", 20)
player1.speak()

# TODO: it's not a good practice to change (overwrite) variable directly
# player1._name = '!!!'
# print(player1._name)                # !!!
# TODO: it's not a good practice to change (overwrite) method to variable directly
# player1.speak()                     # My name is Tom, and I am 20 years old.
# player1.speak = 'BOO'
# print(player1.speak)                # BOO

player1._name = "!!!"
print(player1._name)  # !!!
# TODO: Access to a protected member _name of a class

player1.__private_name = "!!!"
print(player1.__private_name)  # !!!
# TODO: Unresolved attribute reference '__private_name' for class 'PlayerCharacter'


# GitHub Copilot: --------------------------------------------------------------
class MyClass:
    def __init__(self, value):
        self.__private_attribute = value  # Private attribute

    def __private_method(self):  # Private method
        return f"The value is {self.__private_attribute}"

    def public_method(self):
        return self.__private_method()  # Accessing private method within the class


# Example usage
obj = MyClass(10)
print(obj.public_method())  # The value is 10

# Accessing private attribute and method from outside the class will raise an AttributeError
# print(obj.__private_attribute)  # AttributeError
# print(obj.__private_method())  # AttributeError
