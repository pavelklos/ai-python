# 130 : Inheritance
# TODO: We have parent class (User) and child classes (Wizard and Archer).
# TODO: Sometimes child classes are called subclasses or derived classes.


# Parent Class
class User:
    def sign_in(self):
        print("logged in")


# Sub Class/ Child Class/ Derived Class
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"Attacking with arrows: Arrows left- {self.num_arrows}")


user1 = User()
wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robbin", 100)
wizard1.attack()
archer1.attack()

# TODO: isinstance() is built-in function in Python
# TODO: isinstance() function is used to check if an object belongs to a particular class.
print(isinstance(wizard1, Wizard))  # True
print(isinstance(wizard1, User))  # True
print(isinstance(wizard1, object))  # True
print(isinstance(wizard1, Archer))  # False

print(type(User))  # <class 'type'>
print(type(user1))  # <class '__main__.User'>
print(type(wizard1))  # <class '__main__.Wizard'>
print(type(archer1))  # <class '__main__.Archer'>

# TODO: we can use the sign_in() method from the User class (parent class)
user1.sign_in()  # logged in
wizard1.sign_in()  # logged in
archer1.sign_in()  # logged in

help(user1)  # Help on User in module __main__ object
help(wizard1)  # Help on Wizard in module __main__ object
help(archer1)  # Help on Archer in module __main__ object
