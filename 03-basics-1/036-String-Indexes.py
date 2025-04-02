# 036 : String Indexes
# - str is ordered sequence of characters
# - each character in the sequence has an index
# - index starts from 0
# - index can be positive or negative
# - positive index starts from the beginning of the string
# - negative index starts from the end of the string
# - index can be used to access string elements
# - index can be used to access string slices
# - index can be used to access string slices with a step
# - index can be used to access string slices with a negative step
# - is a string index a valid index for the string?

python = "I am PYTHON"

# [start:stop:step]     # TODO: [start:stop] [start:] [:stop] [:] [start::step] [::step] [::-step]

print(python[1:4])  # am
print(python[1:])  # am PYTHON
print(python[:])  # I am PYTHON
print(python[1:100])  # am PYTHON
print(python[-1])  # N
print(python[-4])  # T
print(python[:-3])  # I am PYT
print(python[-3:])  # HON
print(python[::-1])  # NOHTYP ma I

number = "01234567"

print(number[0:8])  # 01234567
print(number[0:8:1])  # 01234567
print(number[0:8:2])  # 0246
print(number[0:8:3])  # 036
print(number[0:8:4])  # 04
print(number[::-2])  # 7531

# [::1] = [0:0:1] = [0:0] = [0]
# [start:stop] - from start to stop
# [start:stop:step] - from start to stop with a step
# [start:stop:-step] - from start to stop with a negative step
# [start:] - from start to the end
# [:stop] - from the beginning to stop
# [:] - the whole string
# [start::step] - from start to the end with a step
# [::step] - the whole string with a step
# [::-step] - the whole string with a negative step

# Guess the output of each print statement before you click RUN!
# python = 'I am PYTHON'

print(python[1:4])
print(python[1:])
print(python[:])
print(python[1:100])
print(python[-1])
print(python[-4])
print(python[:-3])
print(python[-3:])
print(python[::-1])
