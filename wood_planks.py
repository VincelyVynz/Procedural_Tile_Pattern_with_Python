from PIL import Image

SIZE = 1024
PLANK_X = 9
PLANK_Y = 2

plank_px_w = SIZE/PLANK_X
plank_px_h = SIZE/PLANK_Y

gap_factor = 0.02
min_gap = min(plank_px_w, plank_px_h)
plank_gap = gap_factor * min_gap

MARGIN_X = plank_gap / plank_px_w
MARGIN_Y = plank_gap / plank_px_h

image = Image.new("L", (SIZE, SIZE))

pixels = image.load()

for y in range(SIZE):
    for x in range(SIZE):
        nx = x/SIZE
        ny = y/SIZE

        plank_x = nx * PLANK_X
        plank_y = ny * PLANK_Y

        row = int(plank_x)
        if row % 2 == 1:
            plank_y += 0.5

        local_x = plank_x % 1.0
        local_y = plank_y % 1.0

        inside = (
            MARGIN_X < local_x < 1 - MARGIN_X and
            MARGIN_Y < local_y < 1 - MARGIN_Y
        )

        pixels[x,y] = 255 if inside else 0

image.save("planks.png")