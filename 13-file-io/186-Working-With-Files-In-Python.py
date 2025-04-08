# 186 : Working With Files In Python
# TODO: FILE I/O: Input/Output (reading/writing) files
# TODO: built-in functions: open(), read(), write(), close()
from os import write

# TODO: [test4.txt] created in the same directory as this script
my_file = open("test4.txt", "w").close()  # create an empty file
print(my_file)  # TODO: None

my_file = open("test.txt")  # open the file
print(my_file)  # TODO: <_io.TextIOWrapper name='test.txt' mode='r' encoding='cp1250'>
print(my_file.read())  # TODO: 'TEST TEXT 3' ...
print(
    my_file.read()
)  # TODO: '' (empty string, because the cursor is at the end of the file)
my_file.seek(0)  # move the cursor to the beginning of the file
print(my_file.read())  # TODO: 'TEST TEXT 3'
print(my_file.readline())  # TODO: 'TEST TEXT 3\n'
print(
    my_file.readline()
)  # TODO: '' (empty string, because the cursor is at the end of the file)
my_file.seek(0)  # move the cursor to the beginning of the file
print(my_file.readlines())  # TODO: ['TEST TEXT 3\n'] (list of lines)
my_file.close()  # close the file

# TODO: GitHub Copilot ---------------------------------------------------------

# Open a file for writing
with open("example.txt", "w") as file:  # 'w' mode will overwrite the file
    print(type(file))  # TODO: <class '_io.TextIOWrapper'>
    file.write("Hello, world!")

# Open a file for reading
with open("example.txt", "r") as file:  # 'r' mode is the default mode to read a file
    content = file.read()
    print(content)

# Open a file for appending
with open("example.txt", "a") as file:  # 'a' mode will append to the file

    # append the current date and time
    from datetime import datetime, timezone

    # get the current date and time with timezone information
    current_time = datetime.now(timezone.utc)
    file.write("\n" + current_time.isoformat())

    # format the datetime object to include the timezone
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")
    file.write("\n" + formatted_time)

    # append a new line
    file.write("\nAppending a new line.")

# Open a file for reading line by line
with open("example.txt", "r") as file:  # 'r' mode is the default mode to read a file
    for line in file:
        print(line.strip())

# Open and Close a file
# file = open('example.txt', 'r')  # 'r' is the default mode
# content = file.read()
# print(content)
# file.close()
