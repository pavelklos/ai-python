# 068 : Logical Operators
# [and, or, not]                        # TODO: Logical Operators
#  and  both conditions must be true
#  or   at least one condition must be true
#  not  negates the condition

# [>, <, >=, <=, ==, !=]                # TODO: Logical (Comparison) Operators
#  >    greater than
#  <    less than
#  >=   greater than or equal to
#  <=   less than or equal to
#  ==   equal to
#  !=   not equal to

4 > 5  # False
4 < 5  # True
4 == 5  # False # TODO: '==' comparison operator
a = 5  # TODO: '='  assignment operator
"hello" == "hello"  # True
"a" > "b"  # False # TODO: because 'a' is less than 'b' in ASCII table
"a" > "A"  # True  # TODO: because 'a' is greater than 'A' in ASCII table
[] == {}  # False # TODO: empty list is not equal to empty dictionary
[a] == {a: 1}  # False # TODO: list is not equal to dictionary
1 < 2 < 3 < 4  # True  # TODO: multiple comparison operators
1 > 2 < 3 < 4  # False # TODO: multiple comparison operators
1 >= 0  # True
1 <= 0  # False
1 != 0  # True
not True  # False
not False  # True
not (True)  # False # TODO: not() is not function, it is keyword + missing whitespace
not (False)  # True  # TODO: not() is not function, it is keyword + missing whitespace
not (1 == 1)  # False # TODO: not() is not function, it is keyword + missing whitespace
not (1 == 0)  # True  # TODO: not() is not function, it is keyword + missing whitespace
