MENU: dict = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

COINS: dict = {
    'pennies': 0.01,
    'nickles': 0.05,
    'dimes': 0.10,
    'quarters': 0.25
}

resources: dict = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    'money': 0
}


def printReport() -> None:
    """ Prints a report of the current status of the resources + money in the machine """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}gr")
    print(f"Money: ${resources['money']}")


def checkResources(recipe: str) -> bool:
    """ Checks if the coffee machine has enough resources to make the recipe. Print error statement otherwise. """

    for ingredient, value in MENU[recipe]['ingredients'].items():
        if (resources[ingredient] - value) < 0:
            print(f"Sorry there is not enough {ingredient}")
            return False

    return True


def updateResources(recipe: str) -> None:
    """ Updates the resources of the machine according to the recipe """
    for ingredient, value in MENU[recipe]['ingredients'].items():
        resources[ingredient] -= value


def collectPayment(recipe: str) -> bool:
    """ Ask user to insert coins. Subsequently, checks if total value matches the order costs."""

    total: float = 0

    print('Please insert coins: ')
    for coin, value in COINS.items():
        total += int(input(f"how many {coin}? : ")) * value
    if total >= MENU[recipe]['cost']:
        change = round(total - MENU[recipe]['cost'], 2)
        print(f"Here is  ${change} in change.")
        return True
    else:
        print(f"You didn't inserted enough money. You will be refunded. ")
        return False


def processPayment(recipe: str) -> None:
    """ Add inserted coins to the machine """
    resources['money'] += MENU[recipe]['cost']


def coffeeMachine() -> None:
    """ Starts the coffee machine """

    turned_on: bool = True

    while turned_on:

        choice: str = input(f"What would you like? Type ('espresso'/'latte'/'cappuccino'): ")

        if choice == 'off':
            turned_on = False
        elif choice == 'report':
            printReport()
        elif choice in ['espresso', 'latte', 'cappuccino']:

            if checkResources(choice) and collectPayment(choice):
                processPayment(choice)
                updateResources(choice)

                print(f"Processing order")
                print(f"..."*3)
                print(f"Enjoy your {choice} ☕️")


coffeeMachine()