# Images and Python
# Author: Aishani
# 11 Dec 2023

from PIL import Image

# open up kid green
with Image.open("./images/kid-green.jpg") as in:
    # create variables that store the width and height
    image_height = im.height
    image_width = im.width

    # starting at the top and working our way down
    # visit the pixels from left to right
    for y in range(image_height):
        for x in range(image_width):
            # print this pixel's information