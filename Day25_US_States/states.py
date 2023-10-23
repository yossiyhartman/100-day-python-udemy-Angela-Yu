from turtle import Turtle, Screen
import pandas as pd
from StatesManager import StatesManager

# Read csv
states = pd.read_csv(filepath_or_buffer='./50_states.csv')

# Create Classes
screen = Screen()
states_manager = StatesManager(states=states['state'].values)

# initialize world
screen.title('Guess the states. 🇺🇸')
screen.bgpic('./blank_states_img.gif')
screen.setup(width=725, height=491)

print(states)

game = True
score = 0

while game:
    guess = screen.textinput(title="Guess the state",
                             prompt=f"Guess any of the states {score}/{states.shape[0]}").title()

    if guess == 'Exit':
        break

    if states_manager.state_exists(guess):
        # Turn into dict for easy access of the values
        state = states.loc[states['state'] == guess]

        # Write state on map
        states_manager.write_state(guess, int(state.x), int(state.y))

        # Increase score
        if not states_manager.already_guessed(guess):
            states_manager.check_state(guess)
            score += 1

# keep the remaining states
remaining_states = states[~states['state'].isin(states_manager.guessed)]
remaining_states.to_csv('remaining_states.csv', index=False)
print(remaining_states)
screen.mainloop()
