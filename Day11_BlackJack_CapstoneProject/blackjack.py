from art import logo
from utils import showCards, drawCard, checkHand

# Simulate a deck

print(logo)


def checkWinner(p_cards: list[int], d_cards: list[int]):
    print('\nTable Outcome:')
    showCards(p_cards=p_cards, d_cards=d_cards, dealer_showing_cards=True)

    p_total, d_total = sum(p_cards), sum(d_cards)

    if (21 < p_total) or (p_total < d_total <= 21):
        print("You lose!")
    elif (21 < d_total) or (d_total < p_total <= 21):
        print("You win!")
    else:
        print("It's a draw.")


def dealers_turn(d_cards: list[int]) -> list[int]:
    while sum(d_cards) < 17:
        d_cards.append(drawCard())

    return d_cards


def play_round(p_cards: list[int], d_cards: list[int]):
    continue_turn = True

    while continue_turn:
        choice = input("Type 'hit' to get another card, 'stand' to pass ")
        if choice == 'stand':
            continue_turn = False
            d_cards = dealers_turn(d_cards)
            checkWinner(p_cards=p_cards, d_cards=d_cards)

        elif choice == 'hit':
            p_cards.append(drawCard())
            showCards(p_cards=p_cards, d_cards=d_cards, dealer_showing_cards=False)

            if checkHand(p_cards) == 'bust':
                continue_turn = False
                checkWinner(p_cards=p_cards, d_cards=d_cards)


def start_game():
    print("\nLet's Play! No more bets .. ")
    players_cards = [drawCard(), drawCard()]
    dealers_cards = [drawCard(), drawCard()]

    showCards(p_cards=players_cards, d_cards=dealers_cards, dealer_showing_cards=False)
    play_round(p_cards=players_cards, d_cards=dealers_cards)

    if input("Type 'y' to play another round or any character to exit ") == 'y':
        start_game()
    else:
        print('Thanks for playing')


start_game()
