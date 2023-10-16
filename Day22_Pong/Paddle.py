from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, name: str, player: int):
        super().__init__()
        self.name = name
        self.player = player
        self.location = []
        self.setup()

    def setup(self) -> None:
        """ Create the Paddle """
        self.shape('square')
        self.color('white')
        self.setheading(0)
        self.penup()
        self.turtlesize(stretch_len=3, stretch_wid=1)

    def go_to_starting_position(self, x, y) -> None:
        """ places the paddle to it's starting position """
        self.goto(x, y)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)
