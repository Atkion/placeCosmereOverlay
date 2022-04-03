from io import BytesIO
from PIL import Image, ImageOps

from os import listdir
from os.path import isfile, join, splitext


PIXELART_FOLDER = "./generator/pixelart/"
MASK_FILE = "./generator/mask.png"

FIELD_WIDTH = 2000
FIELD_HEIGHT = 1000

def parse_coordinates(filename):
    name = splitext(filename)[0]
    return name.split("x")

def normalize_coordinates(coordinates):
    return (int(coordinates[0]), int(coordinates[1]))

def process_image(filename):
    image = Image.open(f"{PIXELART_FOLDER}/{filename}")
    width = image.size[0]
    height = image.size[1]
    image = image.resize((width, height), Image.Dither.NONE)
    return image

def get_pixelart():
    pixelart = [f for f in listdir(PIXELART_FOLDER) if isfile(join(PIXELART_FOLDER, f))]
    return pixelart

def open_mask():
    mask_i = Image.open(MASK_FILE)
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

    canvas.save("1to1.png")


generate_template()
