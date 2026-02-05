from turtle import *

shape("turtle")
speed(1)
left(90)
pensize(2)

def tree(length, level, angle):
    if level == 0:
        color("green")
        dot(length)
        color("brown")
        return


    color("brown")
    forward(length)
    right(angle)

    tree(length * 0.8, level - 1, angle)

    left(angle * 2)
    tree(length * 0.8, level - 1, angle)

    right(angle)
    backward(length)

tree(80, 7, 30)