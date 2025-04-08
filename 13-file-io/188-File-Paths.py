# 188 : File Paths
# are used to specify the location of a file or directory
# TODO: we can use both relative and absolute paths
# - relative paths are relative to the current working directory
# - absolute paths are the full path from the root directory
# TODO: [Pathlib]
# - https://docs.python.org/3/library/pathlib.html
#   - Windows path:     C:\Users\Pavel\file.txt
#   - Mac path:         /Users/pavel/file.txt
#   - Linux path:       /home/pavel/file.txt

# TODO: [terminal] commands
# pwd: print working directory          # C:\Users\Pavel\PycharmProjects\ZTM
# ls: list files in the directory
# cd: change directory
# cd .      stay in the current directory (do nothing)
# cd ..     move up one directory
# cd ~      move to the home directory
# cd /      move to the root directory

# TODO: read a file from directory 'files' using relative path -----------------
with open("files/test4.txt") as my_file:  # relative path
    content = my_file.read()
    print(content)


# TODO: read a file from absolute path -----------------------------------------
# with open('C:\\Windows\\System32\\drivers\\etc\\hosts') as my_file:  # absolute path
with open("C:/Windows/System32/drivers/etc/hosts") as my_file:  # absolute path
    content = my_file.read()
    print(content)

# TODO: get the current working directory --------------------------------------
import os

print(os.getcwd())  # C:\Users\pavel\projects\ai-python

# TODO: pathlib: module from Python 3.4 ----------------------------------------
# - we can work with any operating system (Windows, Mac, Linux)
# - https://docs.python.org/3/library/pathlib.html
from pathlib import Path

print(Path.cwd())  # C:\Users\pavel\projects\ai-python
print(Path.home())  # C:\Users\pavel
print(Path("files/test4.txt").is_file())  # True
print(Path("files").is_dir())  # True
print(Path("files").exists())  # True
path = Path("files/test4.txt")  # TODO: set specific path
print(path.name)  # test4.txt
print(path.suffix)  # .txt
print(path.parent)  # files
print(path.parent.parent)  # .
