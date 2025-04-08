# 187 : Read, Write, Append
# TODO: r = read, w = write, a = append
# 'r':  cursor is at the beginning of the file (default mode)
# 'r+': cursor is at the beginning of the file (read and write to the file)
# 'w':  cursor is at the beginning of the file (overwrite the file)
# 'w':  TODO: create a new file if it does not exist
# 'a':  cursor is at the end of the file (append to the file)

# TODO: better way to open, read, write, append, close a file
# TODO: with: this statement will automatically close the file

# TODO: read a file
# with open('test4.txt', mode='r') as my_file:
# with open('test4.txt', 'r') as my_file:

with open("test.txt") as my_file:  # 'r' is the default mode
    content = my_file.read()  # read the file (entire content)
    print(content)

# TODO: write to a file
with open("test.txt", "w") as my_file:  # 'w' will overwrite the file
    my_file.write("TEST TEXT 1\nTEST TEXT 2\n")  # write to the file

# TODO: read and write to a file
with open("test.txt", "r+") as my_file:  # 'r+' will read and write to the file
    my_file.write("TEST TEXT 3\nTEST TEXT 4\n")  # write to the file
    print(my_file.readlines())  # read the file (list of lines)

# TODO: append to a file
with open("test.txt", "a") as my_file:  # 'a' will append to the file
    my_file.write("TEST TEXT 5\nTEST TEXT 6\n")  # append to the file

# TODO: other example (not fixed)
with open("test2.txt", "w") as my_file:  # 'w' will overwrite the file
    text = my_file.write("hi it's me!")  # write to the file
    print(text)  # TODO: number of characters written to the file (11)
    text = my_file.write(":)")  # write to the end of the file (cursor is at the end)
    print(text)  # TODO: number of characters written to the file (2)
    print(
        my_file
    )  # TODO: <_io.TextIOWrapper name='test2.txt' mode='w' encoding='cp1250'>
    # TODO: check some properties of the file
    print(my_file.closed)  # TODO: False
    print(my_file.name)  # TODO: test2.txt
    print(my_file.mode)  # TODO: w
    print(my_file.encoding)  # TODO: cp1250
    print(my_file.writable())  # TODO: True
    print(my_file.readable())  # TODO: False
    print(my_file.seekable())  # TODO: True

# TODO: other example (fixed by append mode)
with open("test2.txt", "a") as my_file:  # 'w' will overwrite the file
    text = my_file.write("hi it's me!")  # write to the file
    print(text)  # TODO: number of characters written to the file (11)
    text = my_file.write(":)")  # write to the end of the file (cursor is at the end)
    print(text)  # TODO: number of characters written to the file (2)

# create a new file that does not exist
with open("test3.txt", "w") as my_file:  # 'w' will create a new file
    text = my_file.write(":(")  # write to the file
    print(text)  # TODO: number of characters written to the file (2)
