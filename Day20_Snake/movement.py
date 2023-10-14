from turtle import Turtle

def left(segment: Turtle) -> None:
    """moves the segment heading to the west"""
    print('left')
    segment.setheading(to_angle=270)

def right(segment: Turtle) -> None:
    """moves the segment heading to the east"""
    print('right')
    segment.setheading(to_angle=90)

def up(segment: Turtle) -> None:
    """moves the segment heading to the north"""
    print('up')
    segment.setheading(to_angle=0)

def down(segment: Turtle) -> None:
    """moves the segment heading to the south"""
    print('down')
    segment.setheading(to_angle=90)