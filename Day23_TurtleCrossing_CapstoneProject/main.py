import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Fix coordinate such that north is at angle 0.
screen.mode('logo')

# Turtle Initializing
player = Player(name='Yossi Y 😶‍🌫')

# Scoreboard Initializing
scoreboard = Scoreboard()

# Car Manager Initializing
car_manager = CarManager()

# Events
screen.listen()
screen.onkey(key='Up', fun=player.up)

# Game logic
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_cars()

    car_manager.move_cars_forward()

    car_manager.remove_cars()

    for car in car_manager.cars:

        # Check if the turtle is on the line of a car
        cor_players_head = player.ycor() + 15
        cor_players_tail = player.ycor() - 15
        cor_car_top = car.ycor() + 10
        cor_car_bottom = car.ycor() - 10

        if (cor_car_bottom < cor_players_head < cor_car_top) or (cor_car_bottom < cor_players_tail < cor_car_top):
            if player.distance(car) < 30:
                game_is_on = False
                scoreboard.game_over()

    if player.finished():

        car_manager.increase_speed()

        scoreboard.increase_score()

screen.mainloop()