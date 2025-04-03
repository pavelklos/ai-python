# 049 : Common List Patterns
# - are patterns that are commonly used when working with lists

basket = ["a", "x", "b", "c", "d", "e", "d"]  # ['a', 'x', 'b', 'c', 'd', 'e', 'd']
basket.sort()  # ['a', 'b', 'c', 'd', 'd', 'e', 'x']
basket.reverse()  # ['x', 'e', 'd', 'd', 'c', 'b', 'a']
print(basket[::-1])  # ['a', 'b', 'c', 'd', 'd', 'e', 'x'] TODO: produce a new list
print(len(basket))  # 7
print(list(range(1, 7)))  # [1, 2, 3, 4, 5, 6]

sentence = " "
sentence.join(
    ["hi", "my", "name", "is", "Joe"]
)  # 'hi my name is Joe' TODO: create a new string
print(sentence)  # ''
new_sentence = " ".join(["hi", "my", "name", "is", "Joe"])  # 'hi my name is Joe'
print(new_sentence)  # 'hi my name is Joe'

# fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
friends = ["Simon", "Patty", "Joy", "Carrie", "Amira", "Chu"]
new_friend = ["Stanley"]
# print(friends.sort() + new_friend)

# Solution: (keep in mind there are multiple ways to do this, so your answer may vary.
# As long as it works that's all that matters!)
friends.extend(
    new_friend
)  # ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu', 'Stanley']
print(sorted(friends))  # ['Amira', 'Carrie', 'Chu', 'Joy', 'Patty', 'Simon', 'Stanley']
