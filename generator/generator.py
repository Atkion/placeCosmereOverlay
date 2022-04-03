from io import BytesIO
from PIL import Image, ImageOps

from os import listdir
from os.path import isfile, join, splitext


PIXELART_FOLDER = "./pixelart/"

FIELD_WIDTH = 6000
FIELD_HEIGHT = 3000

def parse_coordinates(filename):
    name = splitext(filename)[0]
    return name.split("x")

def normalize_coordinates(coordinates):
    return (int(coordinates[0]) * 3, int(coordinates[1]) * 3)

def process_image(filename):
    image = Image.open(f"{PIXELART_FOLDER}/{filename}")
    width = image.size[0]
    height = image.size[1]
    image = image.resize((width * 3, height * 3), Image.Dither.NONE)
    return image

def get_pixelart():
    pixelart = [f for f in listdir(PIXELART_FOLDER) if isfile(join(PIXELART_FOLDER, f))]
    return pixelart

def open_mask():
    mask_i = Image.open("mask.png")
    mask = Image.new("1", (FIELD_WIDTH, FIELD_HEIGHT), 0)
    mask.paste(mask_i)
    return mask

def create_blank_image():
    return Image.new('RGBA', (FIELD_WIDTH, FIELD_HEIGHT))

def generate_template():
    canvas = create_blank_image()

    pixelart = get_pixelart()
    print(f"Found {pixelart=}")

    for filename in pixelart:
        print(f"Processing {filename}")

        image = process_image(filename)

        coordinates = parse_coordinates(filename)
        print(f"{coordinates=}")
        canvas.paste(image, normalize_coordinates(coordinates))

    mask = open_mask()
    template = Image.composite(create_blank_image(), canvas, mask)
    template.save("./template.png")

    # tl = (1710 * 3, 2 * 3)
    #
    # final_img = Image.new('RGBA', (6000, 3000))
    # unmasked_img = Image.new('RGBA', (6000, 3000))
    # unmasked_img.paste(img, tl)
    # final_img = Image.composite(final_img, unmasked_img, mask)
    # final_img.save("generated_template.png")


generate_template()


# #img = Image.open("stormlight.png")
#
# #width = int(img.size[0] / 8)
# #height = int(img.size[1] / 8)
#
# #print(width, " " , height)
# #print(int(width), " " , int(height))
# #img = img.resize(( width, height), Image.NEAREST)
#
# img = Image.open("rwot.png")
#
# width = int(img.size[0])
# height = int(img.size[1])
#
# print(width, " " , height)
# print(int(width), " " , int(height))
# img = img.resize(( width, height), Image.NEAREST)
#
# img = img.resize(( width * 3 , height * 3), Image.NEAREST)
#
# img.save("intermediary.png")
#
#
# tl = (1710 * 3, 2 * 3)
#
# final_img = Image.new('RGBA', (6000, 3000))
# unmasked_img = Image.new('RGBA', (6000, 3000))
# unmasked_img.paste(img, tl)
# final_img = Image.composite(final_img, unmasked_img, mask)
# final_img.save("generated_template.png")
