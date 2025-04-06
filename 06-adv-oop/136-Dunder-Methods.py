# 136 : Dunder Methods
# TODO: are special methods that are surrounded by double underscores
# TODO: are also called magic methods


# By reading the python documentation, add 3 more magic/dunder methods of your choice to this Toy class.
class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            "name": "Yoyo",
            "has_pets": False,
        }

    # TODO: custom defined dunder methods (magic methods)
    def __str__(self):  # TODO: str(object) = object.__str__()
        return f"{self.color}"

    def __len__(self):  # TODO: len(object) = object.__len__()
        return 5

    def __del__(self):  # TODO: del object = object.__del__()
        print("deleted!")
        return "deleted!"

    def __call__(self):  # TODO: object() = object.__call__()
        return "yes??"

    def __getitem__(self, i):  # TODO: object[i] = object.__getitem__(i)
        return self.my_dict[i]


action_figure = Toy("red", 0)  # action_figure is an instance of the Toy class
print(dir(action_figure))  # attributes and methods of the object

# action_figure.__str__()
print(action_figure.__str__())  # red
print(str(action_figure))  # red
print(action_figure)  # red

# action_figure.__len__()
print(len(action_figure))  # 5

# action_figure.__call__()
print(action_figure())  # yes??

# action_figure.__getitem__()
print(action_figure["name"])  # Yoyo

# action_figure.__del__()
del action_figure  # deleted

# action_figure  # NameError: name 'action_figure' is not defined
