from io import BytesIO
from PIL import Image, ImageOps

#img = Image.open("stormlight.png")

#width = int(img.size[0] / 8)
#height = int(img.size[1] / 8)

#print(width, " " , height)
#print(int(width), " " , int(height))
#img = img.resize(( width, height), Image.NEAREST)

img = Image.open("rwot.png")

width = int(img.size[0])
height = int(img.size[1])

print(width, " " , height)
print(int(width), " " , int(height))
img = img.resize(( width, height), Image.NEAREST)

img = img.resize(( width * 3 , height * 3), Image.NEAREST)

img.save("intermediary.png")

mask_i = Image.open("mask.png")
mask = Image.new("1", (6000, 3000), 0)
mask.paste(mask_i)

tl = (1710 * 3, 2 * 3)

final_img = Image.new('RGBA', (6000, 3000))
unmasked_img = Image.new('RGBA', (6000, 3000))
unmasked_img.paste(img, tl)
final_img = Image.composite(final_img, unmasked_img, mask)
final_img.save("generated_template.png")
