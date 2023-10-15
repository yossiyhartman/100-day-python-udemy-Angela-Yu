import time
from turtle import Turtle, Screen
from snake import Snake

CANVAS = dict(width=500, height=600)  # (Width, Height)

# Initialize world
world = Screen()
world.setup(width=CANVAS['width'], height=CANVAS['height'])
world.bgcolor('#2f3133')
world.title('SNAKE 🐍')
world.tracer(0)

# initialize snake
snake = Snake()

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

# Make sure the screen don't close
world.exitonclick()
