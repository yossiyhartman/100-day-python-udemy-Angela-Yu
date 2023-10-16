from turtle import Turtle, Screen, mode
from Paddle import Paddle
from Ball import Ball
from Scoreboard import Scoreboard
import time

# Constants
BODY_PART_SIZE = 20
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 400
PADDING = 50
BG_COLOR = '#2f3133'

# initialize screen
mode('logo')

s = Screen()
s.setup(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
s.bgcolor(BG_COLOR)
s.title('PONG 🏓')
s.tracer(0)

# Create players / Paddles
player_1 = Paddle(name='Computer 👾', player=1)
player_2 = Paddle(name='Yossi 🥷🏻', player=2)

player_1.go_to_starting_position(x=(CANVAS_WIDTH / 2) - PADDING, y=0)
player_2.go_to_starting_position(x=PADDING - (BODY_PART_SIZE / 2 + CANVAS_WIDTH / 2), y=0)

# Listen to events
s.listen()
s.onkey(key='Up', fun=player_1.up)
s.onkey(key='Down', fun=player_1.down)
s.onkey(key='w', fun=player_2.up)
s.onkey(key='s', fun=player_2.down)

# Create Bal
ball = Ball()

# Create Scoreboard
scoreboard = Scoreboard(screen_width=CANVAS_WIDTH, screen_height=CANVAS_HEIGHT)

game_over = False

while not game_over:
    time.sleep(0.05)
    s.update()
    ball.move()

    if not (BODY_PART_SIZE / 2 - CANVAS_HEIGHT / 2 < ball.ycor() < CANVAS_HEIGHT / 2 - BODY_PART_SIZE / 2):
        ball.wall_bounce()

    cond_1 = (player_1.distance(ball.pos()) < 35 and ball.xcor() < 345 and ball.move_x > 1)
    cond_2 = (player_2.distance(ball.pos()) < 35 and ball.xcor() > -345 and ball.move_x < -1)

    if cond_1 or cond_2:
        ball.paddle_bounce()

    # out of bounds
    if not (-CANVAS_WIDTH / 2 < ball.xcor() < CANVAS_WIDTH / 2):
        if ball.xcor() > 0:
            print('player 2 scores a points!')
            scoreboard.update_score(player=2)
        else:
            print('player 2 scores a points!')
            scoreboard.update_score(player=1)

        ball.reset_position()

s.exitonclick()
