from turtle import Turtle


class Snake:
    BODY_PART_SIZE = 20

    def __init__(self):
        self.body = self._init()
        self.head = self.body[0]

    def _init(self) -> list:
        """ Create the snake """
        body = []
        for _ in range(3):
            s = Turtle(shape='square')
            s.color('white')
            s.penup()
            s.back(_ * self.BODY_PART_SIZE)
            body.append(s)

        return body

    def move(self) -> None:
        """ Move the snake forward """

        for body_part_idx in range(len(self.body) - 1, 0, -1):
            # Get position of next body part in line
            new_x = self.body[body_part_idx - 1].xcor()
            new_y = self.body[body_part_idx - 1].ycor()

            # Move body part to the position of the body part in front
            self.body[body_part_idx].goto(x=new_x, y=new_y)

        self.head.forward(self.BODY_PART_SIZE)