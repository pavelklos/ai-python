# 125 : Reviewing What We Know So Far


class NameOfClass:  # TODO: class
    class_attribute = "value"  # TODO: class attribute

    def __init__(self, param1, param2):  # TODO: constructor
        self.param1 = param1
        self.param2 = param2

    def method(self):  # TODO: instance method
        return self.param1 + self.param2

    @classmethod
    def cls_method(cls, param1, param2):  # TODO: class method
        return cls(param1, param2)

    @staticmethod
    def stc_method(param1, param2):  # TODO: static method
        return param1 + param2


obj = NameOfClass("a", "b")
print(obj.param1)
print(obj.param2)
print(obj.method())

cls_obj = NameOfClass.cls_method("c", "d")
print(cls_obj.param1)
print(cls_obj.param2)
print(cls_obj.method())

stc_obj = NameOfClass.stc_method("e", "f")
print(stc_obj)

# help(NameOfClass.method)
# help(NameOfClass.cls_method)
# help(NameOfClass.stc_method)
