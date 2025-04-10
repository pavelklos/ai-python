# 212 : Images With Python
# TODO: Pillow: is a Python Imaging Library (PIL), which adds
#       image processing capabilities to your Python interpreter.
# - https://pillow.readthedocs.io/en/stable/
# > pip install pillow

# [image.py] + [Pokedex] 4x images
from PIL import Image, ImageFilter
from win32cred import CRED_MAX_VALUE_SIZE

# TODO: open image
img = Image.open("./Pokedex/pikachu.jpg")
print(
    img
)  # <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=640x640 at 0x2B57CBE18E0>
print(img.format)  # JPEG
print(img.size)  # (640, 640)
print(img.mode)  # RGB
print(img.filename)  # ./Pokedex/pikachu.jpg

img_png = Image.open("./Pokedex/pokemons.png")
print(
    img_png
)  # <PIL.PngImagePlugin.PngImageFile image mode=P size=900x411 at 0x2B57E454D10>
print(img_png.format)  # PNG
print(img_png.size)  # (900, 411)
print(img_png.mode)  # P
print(img_png.filename)  # ./Pokedex/pokemons.png

print(dir(img))  # all methods and attributes that we can use with image object

# TODO: show image (open image in default player)
img.show()

# TODO: add filters and do some image processing (convert, rotate, crop, resize, thumbnail)
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("./Pokedex/pikachu-blur.png", "png")

filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save("./Pokedex/pikachu-smooth.png", "png")

filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save("./Pokedex/pikachu-sharpen.png", "png")

filtered_img = img.filter(ImageFilter.EDGE_ENHANCE)
filtered_img.save("./Pokedex/pikachu-edge-enhance.png", "png")

# TODO: convert image to grey scale, that is Black and White. Similarly RGB = Red Green Blue
filtered_img = img.convert("L")
filtered_img.save("./Pokedex/pikachu-grey.png", "png")

rotated_img = img.rotate(45)
rotated_img.save("./Pokedex/pikachu-rotated.png", "png")

box = (100, 100, 400, 400)
cropped_img = img.crop(box)
cropped_img.save("./Pokedex/pikachu-cropped.png", "png")

# TODO: this can ruin aspect ratio hence we use thumbnail method
astro_img = img.resize((100, 50))  # it will resize image to 100*50 pixels
astro_img.save("./Pokedex/pikachu-resized.png", "png")

# TODO: it will keep max. 50*50 aspect ratio, it can be like 30*50, but it won't exceed 50 pixels
img.thumbnail((100, 50))
img.save("./Pokedex/pikachu-thumbnailed.png", "png")

# TODO: [astro.jpg]   5.611 x 5.339   3,57 MB
astro = Image.open("./Pokedex/astro.jpg")
print(
    astro
)  # <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=5611x5339 at 0x2B57E4C1C40>
print(astro.size)  # (5611, 5339)
print(astro.mode)  # RGB

astro_img = astro.resize((400, 400))  # it will resize image to 400*400 pixels
astro_img.save("./Pokedex/astro-resized.png", "png")

astro.thumbnail((400, 400))
astro.save("./Pokedex/astro-thumbnailed.png", "png")
