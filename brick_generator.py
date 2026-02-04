from PIL import Image

SIZE = 1024

image = Image.new("L", (SIZE, SIZE))
pixels = image.load()

BRICKS_X = 3
BRICKS_Y = 8

MARGIN_X = 0.005 * BRICKS_X
MARGIN_Y = 0.005 * BRICKS_Y

for y in range(SIZE):
    for x in range(SIZE):
        nx = x / SIZE
        ny = y / SIZE

        brick_x = nx * BRICKS_X
        brick_y = ny * BRICKS_Y

        row = int(brick_y)
        if row % 2 == 1:
            brick_x += 0.5

        local_x = brick_x % 1.0
        local_y = brick_y % 1.0

        inside = (
            MARGIN_X < local_x < 1 - MARGIN_X and
            MARGIN_Y < local_y < 1 - MARGIN_Y
        )

        pixels[x, y] = 255 if inside else 0

image.save("bricks.png")
