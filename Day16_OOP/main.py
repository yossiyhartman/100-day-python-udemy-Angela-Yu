from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMachine = CoffeeMaker()
moneyMachine = MoneyMachine()
coffeeMenu = Menu()

turned_on: bool = True


while turned_on:

    choice: str = input(f"What would you like? [{coffeeMenu.get_items()}..] : ")

    if choice == 'off':
        turned_on = False

    elif choice == 'report':
        coffeeMachine.report()
        moneyMachine.report()

    else:
        drink = coffeeMenu.find_drink(choice)
        if drink is not None and coffeeMachine.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeeMachine.make_coffee(drink)