# imports
import random
from turtle import Turtle, Screen


timmy = Turtle()
screen = Screen()

# increase the thickness of the lines
timmy.pensize()
timmy.speed('fastest')

circles = 100
radius = 150

def generateColor() -> str:
    return "#%06x" % random.randint(0, 0xFFFFFF)


for _ in range(circles):
    angle = 360 / circles
    timmy.pencolor(generateColor())
    timmy.left(angle)
    timmy.circle(radius=radius)
