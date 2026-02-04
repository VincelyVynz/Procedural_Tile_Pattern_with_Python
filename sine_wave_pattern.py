from PIL import Image
import math

SIZE = 1024
freq = 8
image = Image.new("L", (SIZE, SIZE))
pixels = image.load()

for y in range(SIZE):
    for x in range(SIZE):
        nx = x/SIZE
        ny = y/SIZE

        value = math.sin(nx * math.pi * 2 * freq) * math.sin(ny*math.pi * 2 * freq)
        height = int((value*0.5 + 0.5) * 255)
        pixels[x,y] = height

image.save("sin_pattern.png")