from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, canvas_width, canvas_height, padding=50):
        super().__init__()

        # Information on the screen
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.padding = padding

        # initialize food style
        self.shape('circle')
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.penup()
        self.color('blue')

        # Initialize food location
        self.refresh()

    def refresh(self):
        x = random.randint(self.padding - int(self.canvas_width / 2), int(self.canvas_width / 2) - self.padding)
        y = random.randint(self.padding - int(self.canvas_height / 2), int(self.canvas_height / 2) - self.padding)
        self.goto(x=x, y=y)
