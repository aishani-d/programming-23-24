# Functions and Turtle
# Author: Aishani
# 28 November 2023

import turtle

hello = turtle.Turtle()

hello.color("lightgreen")
hello.shape("turtle")

def squared(num: float) -> float:
    """Returns the given number squared"""
    return num ** 2

def draw_square(sidelength: float) -> None:
    for _ in range (4):
        hello.forward(sidelength)
        hello.left(90)

def draw_tree(level: int, height: int) -> None:
    """A recursive function that draws a tree with initial given length
    
    Params:
    
    level - number representing levels of branches
    height - height of the main trunk in pixels
    """

    if level > 0:
        # 1. Draw the branch
        hello.forward(height)
        # 2. Turn to the left
        hello.left(39)
        # 3. Draw a smaller tree(current level - 1)
        draw_tree(level-1, height/1.5)

        # 4. Turn to the right
        hello.right(39*2)

        # 5. Draw a smaller tree(current level - 1)
        draw_tree(level-1, height/1.5)

        # 6. Move back to beginning
        hello.left(39)
        hello.back(height)
    else:
        # Create a level 0 tree, which is a leaf
        original_colour = hello.color()
        hello.color("green")
        hello.stamp()
        hello.color(original_colour[0])

def draw_fancy_tree(level: int, height: int) -> None:
    """A recursive function that draws a tree with initial given length
    
    Params:
    
    level - number representing levels of branches
    height - height of the main trunk in pixels
    """

    if level > 0:
        # 1. Draw the branch
        hello.forward(height)

        # Draw a smaller tree pointing right up
        draw_fancy_tree(level - 1, height/1.5)

        # 2. Turn to the left
        hello.left(39)
        # 3. Draw a smaller tree(current level - 1)
        draw_fancy_tree(level-1, height/1.5)

        # 4. Turn to the right
        hello.right(39*2)

        # 5. Draw a smaller tree(current level - 1)
        draw_fancy_tree(level-1, height/1.5)

        # 6. Move back to beginning
        hello.left(39)
        hello.back(height)
    else:
        # Create a level 0 tree, which is a leaf
        original_colour = hello.color()
        hello.color("green")
        hello.stamp()
        hello.color(original_colour[0])

hello.seth(90)
hello.color("brown")
hello.width(4)
hello.shape("arrow")
hello.speed(0)

draw_fancy_tree(10, 150)

turtle.done()