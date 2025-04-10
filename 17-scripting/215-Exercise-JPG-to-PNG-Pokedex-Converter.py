# 215 : Exercise: JPG to PNG Pokedex Converter

# TODO: [JPGtoPNGconverter.py]
# - script for 2 arguments (path, directory)	        # convert all images in path
#   img = Image.open('./Pokedex/pikachu.jpg')		    # ./Pokedex/pikachu.jpg
#   img.save("./Pokedex/new/pikachu.png", "png")		# ./Pokedex/new/pikachu.png
# [terminal]
# > python JPGtoPNGconverter path directory

import os  # TODO: we can use os or pathlib module

# TODO: import modules
import sys

from PIL import Image

# TODO: version with hardcoded path and directory
# path = 'Pokedex/'
# directory = 'new/'
# if not os.path.exists(directory):
#     os.makedirs(directory   )
# for filename in os.listdir(path):
#     img = Image.open(f'{path}{filename}')
#     clean_name = os.path.splitext(filename)[0]
#     img.save(f'{directory}{clean_name}.png', 'png')
#     print(filename)
#     # print(img.filename, img.size)
#     # print(clean_name)
# print('all done!')

# TODO: grab first and second argument
path = sys.argv[1]  # image folder (from)
directory = sys.argv[2]  # output folder (to)

# TODO: check if 'directory' exists, if not create it
if not os.path.exists(directory):
    os.makedirs(directory)

# TODO: loop through 'path', convert images to PNG, save to 'directory'
# TODO: convert images to PNG
for filename in os.listdir(path):
    clean_name = os.path.splitext(filename)[0]  # remove extension
    img = Image.open(f"{path}{filename}")
    # added the / in case user doesn't enter it
    # you may want to check for this and add or remover it
    # img.save(f'{directory}/{clean_name}.png', 'png')
    img.save(f"{directory}{clean_name}.png", "png")
    print("all done!")

# [Terminal]
# > python .\17-scripting\215-Exercise-JPG-to-PNG-Pokedex-Converter.py 'Pokedex/' 'new/'
