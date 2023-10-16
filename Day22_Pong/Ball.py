from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.setheading(0)
        self.color('white')
        self.penup()
        self.speed('normal')
        self.move_x = 10
        self.move_y = 10

    def move (self) -> None:
        self.goto(x = self.xcor() + self.move_x, y = self.ycor() + self.move_y)

    def wall_bounce(self):
        self.move_y *= -1

    def paddle_bounce(self):
        self.move_x *= -1

    def reset_position(self):
        self.home()
        self.paddle_bounce()
