from turtle import Turtle


class StatesManager(Turtle):

    STATES = 50
    FONT = ('Arial', 11, 'normal')

    def __init__(self, states):
        super().__init__()
        self.hideturtle()
        self.penup()

        self.states = states
        self.guessed = []

    def write_state(self, state, x, y):
        """ write the name of a state on the correct location """
        self.goto(x=x, y=y)
        self.write(arg=state, move=False, align='center', font=self.FONT)

    def state_exists(self, state) -> bool:
        """ Return true if state name exists """
        return state in self.states

    def check_state(self, state) -> None:
        """ Checks off a state name """
        self.guessed.append(state)

    def already_guessed(self, state):
        """ check if a state is already guessed """
        return state in self.guessed

