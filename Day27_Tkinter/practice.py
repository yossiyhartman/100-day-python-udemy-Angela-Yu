from tkinter import Tk, Label, Button

# functions

def button_click():
    return 'clicked'

# Screen
screen = Tk()

# Initialising
screen.title(f'Practice window')
screen.minsize(height=400, width=800)

# Label
label = Label(text="My first Label", font=('Arial', 21, 'bold'))
button = Button(text='click me')

label.pack()
button.pack()

screen.mainloop()


# Practise Exercise 1
"""
    *args : allows for infinite positional arguments
"""

def add(*numbers):
    """ sum a infinite list of numbers """
    return sum(numbers)

# Practise Exercise 2
"""
    **kwargs : allows for infinite positional arguments
"""

print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

def calculate(**kwargs):
    """ sum a infinite list of numbers """
    return kwargs

print(calculate(add = 4, multiply = 23, divide = 30))

