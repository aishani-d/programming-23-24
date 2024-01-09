# Functions and Turtle
# Author: Aishani
# 28 November 2023

import turtle

hello = turtle.Turtle()

hello.color("lightgreen")
hello.shape("turtle")

def squared(num: float) -> float:
    """Returns the given number squared"""
    return ** 2

def draw_square(sidelength: float) -> float:
    for _ in range (4):
        hello.forward(sidelength)
        hello.left(90)

# draw_square(25)
# draw_square(squared(25))

# Create a squares that get bigger and bigger
for i in range(30):
    draw_square(squared(i))


turtle.done