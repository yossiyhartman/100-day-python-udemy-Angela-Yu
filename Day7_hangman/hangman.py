# Challenge's
from hangman_art import stages, logo
from hangman_words import word_list
import random

print(logo)
word = random.choice(word_list)
display = ['_']*len(word)
current_stage = stages.pop()

game = True

while game:
    guess = input('Guess a letter ').lower()

    if guess in display:
        print("You've already guessed this letter")

    if guess not in word:
        print("Your guess is wrong")
        current_stage = stages.pop()
    else:
        for idx, character in enumerate(word):
            if character == guess:
                display[idx] = guess

    print(display)
    print(current_stage)

    if '_' not in display:
        print('You win!')
        game = False
    elif not stages:
        print('You Lose!')
        game = False
