from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, screen_width, screen_height):
        super().__init__()

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.color('white')
        self.penup()
        self.hideturtle()
        self.player_1_score = 0
        self.player_2_score = 0

        self.update_scoreboard()

    def update_score(self, player):
        if player == 1:
            self.player_1_score += 1
        elif player == 2:
            self.player_2_score += 1

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=100,  y=self.screen_height/2 - 50)
        self.write(self.player_1_score, align='center', font=('Courier', 35, 'normal'))
        self.goto(x=-100,  y=self.screen_height/2 - 50)
        self.write(self.player_2_score, align='center', font=('Courier', 35, 'normal'))