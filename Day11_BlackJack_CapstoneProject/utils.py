import random


def showCards(p_cards: list[int], d_cards: list[int], dealer_showing_cards: bool):

    dealers_cards = d_cards if dealer_showing_cards else d_cards[:1]
    p_total, d_total = sum(p_cards), sum(dealers_cards)

    print(f"\nPlayer's cards: {p_cards} /- Total {p_total}")
    print(f"Dealer's cards: {dealers_cards} /- Total {d_total}")


def drawCard() -> int:
    deck: list[int] = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    return random.choice(deck)


def calculate_score(cards: list[int]) -> int:
    """Take a list of cards and return the score calculated from the cards"""

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)



def checkHand(cards: list[int]):
    total = sum(cards)

    if total > 21:
        return 'bust'
    elif total == 21:
        return 'blackjack'
    else:
        return total
