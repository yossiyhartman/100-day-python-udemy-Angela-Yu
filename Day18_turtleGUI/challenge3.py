# imports
import random
from turtle import Turtle, Screen


timmy = Turtle()
screen = Screen()

# increase the thickness of the lines
timmy.pensize(10)


def generateColor() -> str:
    return "#%06x" % random.randint(0, 0xFFFFFF)


def generateDistance() -> int:
    return random.randint(20, 50)


def generateAngle(tim: Turtle):
    angles = [0, 90, 180, 270]
    no_backwards = int((tim.heading() + 180) % 360)
    angles.remove(no_backwards)

    return random.choice(angles)


for _ in range(300):
    timmy.pencolor(generateColor())
    timmy.setheading(generateAngle(timmy))
    timmy.forward(generateDistance())
