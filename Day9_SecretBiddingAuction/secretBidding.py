from art import logo

def printHighestBidder(bidders: []) -> None:
    highest_bidder = {'name': 'John Doe', 'amount': 0}

    for person in bidders:
        if highest_bidder['amount'] < person['amount']:
            highest_bidder = person

    print(f"The winner is {highest_bidder['name']} with a bid of €{highest_bidder['amount']}")


# Start program

active_auction = True
bidders = []

print(logo, '\nWelcome to the secret auction program!')

while active_auction:

    person = {
        'name': input('What is your name?: '),
        'amount': int(input('What is your bid?: €'))
    }

    bidders.append(person)

    if input("Are there more bidders? Type 'Yes' or 'No' ").lower() == 'no':
        active_auction = False
        printHighestBidder(bidders)

    print('\n' * 30) # Keeps the console clear
