# 079 : Our First GUI

# [Exercise]
# Display the image below to the right hand side where
# the 0 is going to be ' ', and the 1 is going to be '*'.
# This will reveal an image!
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

# [Solution]
fill = "*"
empty = " "
for row in picture:
    for pixel in row:
        if pixel:  # pixel == 1
            print(fill, end=empty)  # TODO: ends with empty string
        else:
            print(empty, end=empty)  # TODO: ends with empty string
    # print(end="\n")  # TODO: ends with new line (default)
    print("")  # TODO: ends with new line (default)
