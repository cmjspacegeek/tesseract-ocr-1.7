import os
from PIL import Image


for images in os.listdir("/home/cmjspacegeek/PycharmProjects/MTG_Card/image"):

    if (images.endswith(".png") or images.endswith(".jpg")
            or images.endswith(".jpeg")):
        print(images)
        im = Image.open(r"image/" + images)

        width, height = im.size

        left = 22
        top = 22
        right = 370
        bottom = 60

        im1 = im.crop((left, top, right, bottom))

        im1 = im1.convert("L")

        im1 = im1.save("image/cropped.jpg")

        command = ('tesseract image/cropped.jpg title')
        print(command)
        os.system(command)
        with open('title.txt') as f:
            title = f.readline()

        output = open("output.txt", "a")
        output.write(title.replace("\n", "") + "\n")
        output.close()


