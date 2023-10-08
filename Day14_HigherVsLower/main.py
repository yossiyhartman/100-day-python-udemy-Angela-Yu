import random
from game_data import data
from art import logo, vs


def chooseContender(option: dict) -> dict:
    contender: dict = random.choice(data)

    while contender == option:
        contender = random.choice(data)

    return contender


def checkAnswer(choice: str, option_a: dict, option_b: dict) -> bool:
    if option_a['follower_count'] > option_b['follower_count']:
        return choice == 'A'
    elif option_a['follower_count'] < option_b['follower_count']:
        return choice == 'B'


def game():
    game_running: bool = True
    score: int = 0
    option_a: dict = random.choice(data)
    print(logo)

    while game_running:

        option_b: dict = chooseContender(option=option_a)

        print(f"\n{option_a['name']}, a {option_a['description']}, from {option_a['country']}")
        print(vs)
        print(f"{option_b['name']}, a {option_b['description']}, from {option_b['country']}")

        choice = input(f"Who has more followers? Type 'A' or 'B': ")

        correct_choice = checkAnswer(choice=choice, option_a=option_a, option_b=option_b)

        print('\n' * 50)

        if correct_choice:
            score += 1
            option_a = option_b
            print(f"You're Right! Your current score is {score}")
        else:
            game_running = False
            print(f"That's incorrect. Your final score is {score}")


game()
