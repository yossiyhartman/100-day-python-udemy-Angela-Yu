import json
from turtle import Turtle
import datetime as dt

class Scoreboard(Turtle):

    def __init__(self, canvas_width, canvas_height):
        super().__init__()
        self.score = 0
        self.highscore = self.read_highscore()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(x = 0, y=(canvas_height / 2) - 20)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Score = {self.score}, Highscore: {self.highscore}', move=False, align='center', font=('Courier', 15, 'normal'))

    def update_highscore(self):
        """ If the score of the current game is higher than all previous games, update the highscore """
        if self.score > self.highscore:
            self.highscore = self.score

        self.save_highscore()

    def reset(self):
        """ resets the scoreboard, and updates the high score """
        self.update_highscore()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def save_highscore(self):

        value = {
            'date': str(dt.date.today()),
            'highscore': self.highscore
        }

        with open(file='highscores.json', mode='w') as f:
            json.dump(value, f)

    def read_highscore(self):
        with open(file='highscores.json', mode='r') as f:
            score = json.load(f)
            return score['highscore']