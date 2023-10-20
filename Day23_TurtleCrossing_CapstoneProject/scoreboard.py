from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        # counter for score
        self.score = 0

        self.penup()
        self.goto(x=-250, y=230)
        self.hideturtle()
        self.refresh_scoreboard()

    def increase_score(self) -> None:
        """ Increases the score on the scoreboard """
        self.score += 1
        self.refresh_scoreboard()

    def refresh_scoreboard(self) -> None:
        """ refreshes the values presented on the scoreboard """
        self.clear()
        self.write(font=FONT, align='left', move=False, arg=f'Level: {self.score}')


    def game_over(self):
        self.clear()
        self.home()
        self.write(font=FONT, align='center', move=False, arg=f'GAME OVER!')