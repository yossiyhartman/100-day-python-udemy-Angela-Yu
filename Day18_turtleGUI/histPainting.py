
# imports
import random
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def generateColor() -> str:
    return "#%06x" % random.randint(0, 0xFFFFFF)


dots_shape = (10, 10)

# make timmy invisible
timmy.hideturtle()
timmy.penup()
timmy.speed('fastest')

# move timmy to corner
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

for _ in range(dots_shape[1]):
    for _ in range(dots_shape[1]):
        timmy.dot(15, generateColor())
        timmy.forward(50)

    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(50*dots_shape[1])
    timmy.right(180)


timmy.screen.mainloop()