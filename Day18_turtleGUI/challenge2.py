from turtle import Turtle, Screen
import random

# Create a list of 10 random colors:

corners = 10
arc_length = 100
color_list = ["#%06x" % random.randint(0, 0xFFFFFF) for i in range(10)]

timmy = Turtle()
screen = Screen()

for idx, shape in enumerate(range(3, corners + 1)):

#     # Calculate angle
    angle = round(360 / shape, 5)

    # Set new color
    timmy.pencolor(color_list[idx])

    # Start Drawing
    for _ in range(shape):
        timmy.right(angle)
        timmy.forward(arc_length)
        timmy.pendown()

screen.bye()