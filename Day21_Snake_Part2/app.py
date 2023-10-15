import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

CANVAS = dict(width=500, height=600)  # (Width, Height)

# Initialize world
world = Screen()
world.setup(width=CANVAS['width'], height=CANVAS['height'])
world.bgcolor('#2f3133')
world.title('SNAKE 🐍')
world.tracer(0)

# initialize Snake
snake = Snake()

# Initialize Food
food = Food(canvas_width=CANVAS['width'], canvas_height=CANVAS['height'])

# Initialize Scoreboard
scoreboard = Scoreboard(canvas_width=CANVAS['width'], canvas_height=CANVAS['height'])

# Listen to events
world.listen()
world.onkey(key='Up', fun=snake.up)
world.onkey(key='Down', fun=snake.down)
world.onkey(key='Left', fun=snake.left)
world.onkey(key='Right', fun=snake.right)

# Running the game
game_over = False

while not game_over:
    world.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    x_cond = (-CANVAS['width'] / 2) < snake.head.xcor() < (CANVAS['width'] / 2)
    y_cond = (-CANVAS['height'] / 2) < snake.head.ycor() < (CANVAS['height'] / 2)

    if not (x_cond and y_cond):
        game_over = True
        scoreboard.game_over()

    for body_parts in snake.body[1:]:
        if snake.head.distance(body_parts) < 10:
            game_over = True
            scoreboard.game_over()

# Make sure the screen don't close
world.exitonclick()
