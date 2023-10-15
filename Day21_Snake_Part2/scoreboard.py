from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, canvas_width, canvas_height):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(x = 0, y=(canvas_height / 2) - 20)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f'Score = {self.score}', move=False, align='center', font=('Courier', 15, 'normal'))

    def game_over(self):
        self.home()
        self.write(arg=f"GAME OVER.", move=False, align='center', font=('Courier', 20, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
