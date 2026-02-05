from turtle import *
import colorsys

bgcolor("black")
speed(0)

angle_between_shapes = 5
loop_count = int(360 / angle_between_shapes)



def triangle():
    for _ in range(3):
        forward(200)
        right(120)

for i in range(loop_count):

    hue = i / loop_count

    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    colormode(1.0)
    pencolor(r, g, b)

    triangle()
    right(angle_between_shapes)


mainloop()
