from turtle import Turtle, Screen

t: Turtle = Turtle()
s: Screen = Screen()

SQUARE = 300


for _ in range(4):

    for _ in range(0, SQUARE, 10):
        t.forward(10)
        if _ % 20:
            t.pendown()
        else:
            t.penup()


    t.right(90)


s.bye()