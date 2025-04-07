# TODO: __name__ is a built-in variable that returns the name of the current module.
print(__name__)  # __main__


def buy(item):
    cart = []
    cart.append(item)
    return cart


class Student:
    pass


st_shop = Student()
print(type(st_shop))  # TODO: <class '__main__.Student'>
