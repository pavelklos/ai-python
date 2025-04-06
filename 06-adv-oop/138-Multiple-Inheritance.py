# 138 : Multiple Inheritance
# TODO: ability of a class to derive properties and methods from more than one parent class.


class User:
    def sign_in(self):
        print("logged in")


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

    def check_arrows(self):
        print(f"{self.num_arrows} remaining")

    def run(self):
        print("Ran really fast.")


class HybridBorg(Wizard, Archer):  # TODO: Multiple Inheritance
    def __init__(self, name, power, arrows):  # constructor
        Archer.__init__(self, name, arrows)  # TODO: constructor of Archer
        Wizard.__init__(self, name, power)  # TODO: constructor of Wizard


hb1 = HybridBorg("Borgie", 50, 100)  # instance of HybridBorg
hb1.sign_in()  # logged in # TODO: method of User
hb1.attack()  # Attacking with power of 50 # TODO: method of Wizard
hb1.check_arrows()  # 100 remaining # TODO: method of Archer
hb1.run()  # Ran really fast. # TODO: method of Archer
