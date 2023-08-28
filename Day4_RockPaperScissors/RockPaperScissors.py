rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

game = True

hands = [rock, paper, scissors]

your_choice = int(input('Welcome to an exiting game of Rock, Paper, Scissor! Pick "0" for Rock, "1" for Paper and "2" for Scissors. | '))

while game:

    if your_choice not in [0, 1, 2]:
        your_choice = int(input('Oops! I do not recognise that answer. Pick "0" for Rock, "1" for Paper and "2" for Scissors. | '))

    else:
        computers_choice = random.randint(0, 2)

        print('\nMy choice: ')
        print(your_choice)
        print(hands[your_choice])
        print('The computer\'s choice: ')
        print(computers_choice)
        print(hands[computers_choice])

        if your_choice == computers_choice:
            your_choice = int(input('It is a tie.. Pick again! Pick "0" for Rock, "1" for Paper and "2" for Scissors. | '))
            continue;

        if (your_choice == 0) & (computers_choice == 2):
            print('You win!')
        elif (your_choice == 1) & (computers_choice == 0):
            print('You win!')
        elif (your_choice == 2) & (computers_choice == 1):
            print('You win!')
        else:
            print('The computer wins!')

        game = False


    # done