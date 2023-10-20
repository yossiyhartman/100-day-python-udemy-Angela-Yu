from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, name: str):
        super().__init__()

        self.name = name

        self.penup()
        self.goto(x=STARTING_POSITION[0], y=STARTING_POSITION[1])
        self.setheading(0)
        self.shape('turtle')

    def up(self) -> None:
        """ Move the turtle up if not yet reached the finish line """
        self.forward(MOVE_DISTANCE)

    def finished(self) -> bool:
        """ When reached the finish line, move to starting position """
        cur_y = self.ycor()
        if cur_y == FINISH_LINE_Y:
            self.goto(x=0, y=STARTING_POSITION[1])
            return True

