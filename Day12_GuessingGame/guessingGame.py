#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

print(logo)
print(f"Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between 1 and 100")

RANDOM_NUMBER = random.randint(1,100)
difficulty = input(f"Choose a difficulty. Type 'easy' or 'hard' : ")
attempts = 5 if difficulty == 'hard' else 10
guess = 0

while (attempts > 0) and (guess != RANDOM_NUMBER):
    print(f"You've {attempts} attempts remaining to guess the number.")

    guess = int(input(f"Make a guess: "))

    if guess > RANDOM_NUMBER:
        print(f"Too high.")
    elif guess < RANDOM_NUMBER:
        print(f"Too low.")

    attempts -= 1

if guess == RANDOM_NUMBER:
    print(f"That's it! You win!")
else:
    print(f"That's not it! Better luck next time")

print(f"The number of was {RANDOM_NUMBER}.")
