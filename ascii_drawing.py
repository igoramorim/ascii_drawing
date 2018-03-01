from PIL import Image, ImageDraw, ImageFont
import random
import sys


def get_char(value_color):
    dark = ['@', 'M', 'W', 'B', '#', '&', '*', '%', '$']
    mid = ['x', 'i', 'v', 'o', 'd', 'p', 'o']
    light = [',', '.', ';']

    if value_color < 255 and value_color > 200:
        return random.choice(light)
    elif value_color < 200 and value_color > 100:
        return random.choice(mid)
    else:
        return random.choice(dark)


file_name = sys.argv[1]
original_image = Image.open(file_name).convert('L')

output_image = Image.new('RGB', original_image.size, (255, 255 ,255))

x_size = original_image.size[0]
y_size = original_image.size[1]

pixels = original_image.load()

draw = ImageDraw.Draw(output_image)
font_size = int(sys.argv[2])
font = ImageFont.truetype('arial.ttf', font_size)

offset = int(sys.argv[3])

for i in range(0, x_size, offset):
    for j in range(0, y_size, offset):
        value_color = pixels[i, j]
        print(i, j, value_color)
        if value_color < 255:
            draw.text((i, j), get_char(value_color), font=font, fill=(0, 0, 0))

output_image.save('output_'+file_name)
