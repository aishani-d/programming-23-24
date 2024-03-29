# Turtle Example
# Author: Aishani
# 21 November 2023

import turtle

TURTLE_MAGNITUDE = 20
# Create a turtle
michaelangelo = turtle.Turtle()

# Get some instructions from the user
print("""To give commands, type:
F - to go forward
L - to go left
R - to go right
B - to go backward""")

# Repeat the below code INDEFINITELY
done = False

while not done:
    command = input("Where should I go? ").strip(",.?! ").lower()

    # Based on those instructions. move the turtle on the screen
    if command in ["f", "forward"]:
        michaelangelo.forward(TURTLE_MAGNITUDE)
    elif command in ["l", "left"]:
        michaelangelo.left(90)
    elif command in ["r", "right"]:
        michaelangelo.right(90)

turtle.done()