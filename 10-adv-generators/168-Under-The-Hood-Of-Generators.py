# 168 : Under The Hood Of Generators
# TODO: iter() is function that is used to convert iterable to iterator
# TODO: next() is function that is used to iterate over iterator
# TODO: yield keyword: is used to pause function and return value


# TODO: custom for loop --------------------------------------------------------
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)  # TODO: <list_iterator object at 0x00000200D98B6800>
            # iterator * 5
            # next(iterator)
            print(next(iterator))  # 1 2 3
        except StopIteration:
            break


special_for([1, 2, 3])


# TODO: custom generator (custom range() function) -----------------------------
class MyGen:
    current = 0  # class object attribute

    def __init__(self, first, last):
        self.first = first
        self.last = last
        MyGen.current = (
            self.first
        )  # this line allows us to use the current number as the starting point for the iteration

    # dunder methods (__iter__ & __next__)
    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(1, 10)
print(gen)  # <__main__.MyGen object at 0x00000200D98B6810>
for i in gen:
    print(i)
