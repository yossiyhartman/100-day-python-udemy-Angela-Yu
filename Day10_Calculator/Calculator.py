from utils import *
from art import  logo

operations = {
    '+': add,
    '-': divide,
    '*': multiply,
    '/': divide
}

prev_answer = None
calculating = True

print(logo)

while calculating:

    # Get input
    first_value = float(input("What's the first number?: ")) if prev_answer is None else prev_answer
    operation = input("+ \n- \n* \n/ \nPick an operation: ")
    second_value = float(input("What's the next number?: "))

    # Calculate answer
    answer = operations[operation](first_value, second_value)

    # Print Answer
    print(f'{first_value} {operation} {second_value} = {answer}')

    continue_calculating = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

    if continue_calculating == 'y':
        prev_answer = answer
    elif continue_calculating == 'n':
        prev_answer = None
    else:
        calculating = False
