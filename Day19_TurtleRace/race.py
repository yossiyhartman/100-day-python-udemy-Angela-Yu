import random
import turtle
from turtle import Turtle, Screen

s = Screen()

# world parameters
padding_x = 50
padding_y = 150
canvas_size = 500
number_of_turtles = 6

# setup world
s.setup(width=canvas_size,  height=canvas_size)

# declare the colors
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# create the turtles
turtles = [Turtle(shape='turtle') for _ in range(number_of_turtles)]

user_bet = s.textinput(title = 'betting', prompt=f'On what turtle would you like to bet? {colors}')

def prepTurtles():
    """ Gives the turtles a color and places them in the start position """
    gap_space = (s.window_height() - (2 * padding_y)) / (number_of_turtles + 1)
    cur_y = padding_y + gap_space

    for color, turtle in zip(colors, turtles):
        turtle.penup()
        turtle.color(color)
        turtle.goto(padding_x - (s.window_width() / 2), cur_y - (s.window_height() / 2))
        cur_y += gap_space

def randomPace():
    """ Generates a random pace speed """
    return random.randint(0, 10)


start_race = finished = False

if user_bet:
    start_race = True

prepTurtles()

while not finished and start_race:

    for turtle in turtles:
        if turtle.xcor() >= s.window_width()/2 - 20:

            if user_bet == turtle.pencolor():
                print(f"You've won! The winner is {turtle.pencolor()}")
            else:
                print(f"You've lost! The winner is {turtle.pencolor()}")

            finished = True

        turtle.forward(randomPace())

s.mainloop()
