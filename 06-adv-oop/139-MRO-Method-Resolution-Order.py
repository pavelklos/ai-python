# 139 : MRO - Method Resolution Order
# TODO: is the order in which Python looks for a method in a hierarchy of classes
# TODO: mro(), __mro__ are methods that returns a list of class objects
#   in the order that Python will use to search for a method, attribute
# TODO: Depth First Search (DFS) algorithm
#   is used to search for a method in a hierarchy of classes


class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(D.num)  # TODO: 1

print("-" * 100)
print(D.mro())  # TODO: D, B, C, A, object
print(M.mro())  # TODO: M, B, A, X, Y, Z, object
print(M.__mro__)  # TODO: M, B, A, X, Y, Z, object
print("-" * 100)

# TODO: D.mro()
# [
#   <class '__main__.D'>,
#   <class '__main__.B'>,
#   <class '__main__.C'>,
#   <class '__main__.A'>,
#   <class 'object'>
# ]

# TODO: M.mro()
# [
#   <class '__main__.M'>,
#   <class '__main__.B'>,
#   <class '__main__.A'>,
#   <class '__main__.X'>,
#   <class '__main__.Y'>,
#   <class '__main__.Z'>,
#   <class 'object'>
# ]

print(list.mro())
