from PIL import Image

SIZE = 1024
image = Image.new("L", (SIZE, SIZE))
pixels = image.load()

left, right = 0.3,0.7
top, bottom = 0.3,0.7

for y in range(SIZE):
    for x in range(SIZE):
        nx = x/SIZE
        ny = y/SIZE

        inside = (
            left <= nx <= right and
            top <= ny <= bottom
        )

        pixels[x,y] = 255 if inside else 0

image.save("square.png")