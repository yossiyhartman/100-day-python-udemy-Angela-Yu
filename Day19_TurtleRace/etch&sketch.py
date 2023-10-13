
from turtle import Turtle, Screen

t = Turtle()
s = Screen()

pace = 10

def forward():
    t.forward(pace)

def clockwise():
    t.right(pace)

def anti_clockwise():
    t.left(pace)

def backwards():
    t.backward(pace)

def clearScreen():
    s.reset()

s.listen()
s.onkey(key='w', fun=forward)
s.onkey(key='s', fun=backwards)
s.onkey(key='d', fun=clockwise)
s.onkey(key='a', fun=anti_clockwise)
s.onkey(key='c', fun=clearScreen)

s.mainloop()