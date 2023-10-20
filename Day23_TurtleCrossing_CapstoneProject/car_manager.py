from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


def generate_position() -> tuple[int, int]:
    """ Generate a random position on the y-axis """
    return 300, randint(-260, 280)


class CarManager:
    def __init__(self):
        # Active cars
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE
        self.speed_incr = MOVE_INCREMENT

    def generate_cars(self):
        """ Generate a random number of cars """
        prob_dist = [0, 0, 0, 0, 1, 1]

        for _ in range(choice(prob_dist)):
            car = Turtle()

            car.shape('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(choice(COLORS))
            car.penup()
            car.goto(generate_position())
            car.setheading(270)

            self.cars.append(car)

    def move_cars_forward(self) -> None:
        """ Move cars forward """
        [car.forward(self.move_speed) for car in self.cars]

    def increase_speed(self) -> None:
        """ increase the speed by a certain amount """
        self.move_speed += self.speed_incr

    def remove_cars(self) -> None:
        """ remove cars that are outside the screen """

        # Since only one car is generated per time instance, we only have to look at the first element
        if self.cars and self.cars[0].xcor() < -300:
            car = self.cars.pop(0)
            car.reset()
            car.ht()
            del car


