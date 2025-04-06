# 135 : Object Introspection
# TODO: dir(object) returns all the attributes and methods of the object
# TODO: dir(object) introspects the object during runtime
# TODO: dir(object) show attributes of an object


class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("logged in")


# Sub Class/ Child Class/ Derived Class
class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        # same as:: User.__init__(self, email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")


wizard1 = Wizard("Merlin", 60, "merlin@gmail.com")
print("-" * 100)
print(dir(wizard1))
print("-" * 100)
print(dir(Wizard))
print("-" * 100)
print(dir(User))
print("-" * 100)
print(dir(object))
print("-" * 100)
print(dir(list))
print("-" * 100)
