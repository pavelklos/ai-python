# 134 : super()
# TODO: is used to call the __init__ method of the parent class


class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("logged in")


# Sub Class/ Child Class/ Derived Class
class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email)
        super().__init__(email)  # TODO: we don't need to pass self
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")


wizard1 = Wizard("Merlin", 60, "merlin@gmail.com")
wizard1.sign_in()
print(wizard1.name, wizard1.power, wizard1.email)
wizard1.attack()
