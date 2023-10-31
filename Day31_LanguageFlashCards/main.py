import random
from tkinter import *
from typing import Tuple, List

import pandas as pd
from pandas import DataFrame


# --------------- Functions -----------------

def load_data() -> tuple[DataFrame, list[dict]]:
    """ loads either the full data set, or continues on the progress of the user """
    file: pd.DataFrame = pd.DataFrame()

    try:
        with open(file="./data/words_to_learn.csv", mode='r') as f:
            file = pd.read_csv(f)

    except FileNotFoundError:
        with open(file="./data/freq_dict_es_to_en.csv", mode='r') as f:
            file = pd.read_csv(f)

    return file, file.to_dict(orient='records')


def update_data_file() -> None:
    """ Write an updated version of the words to a file called 'words_to_learn """
    global words_csv
    words_csv.to_csv('./data/words_to_learn.csv', header=True, index=False)


def generate_word() -> dict:
    """ picks a random word from the 1000 most frequent spanish words """
    global words_list

    return random.choice(words_list)


def next_card() -> None:
    """ First generates a new word, then updates the UI with the new word """
    global current_word, translate_timer
    root.after_cancel(translate_timer)

    current_word = generate_word()
    update_card()
    translate_timer = root.after(3000, func=show_translation)


def show_translation() -> None:
    """ Updates the UI and show the translation"""
    global current_word

    card.itemconfig(card_image, image=CARD_BACK)
    card.itemconfig(card_language, text='English', fill='white')
    card.itemconfig(card_word, text=current_word['en_translate'], fill='white')


def update_card() -> None:
    """ Updates the UI with a newly picked word """
    global current_word

    card.itemconfig(card_image, image=CARD_FRONT)
    card.itemconfig(card_language, text='Español', fill='black')
    card.itemconfig(card_word, text=current_word['es_words'], fill='black')


def remove_word() -> None:
    """ If the user already knows the word, remove from list and generate new word """
    global current_word, words_csv, words_list

    print(words_csv.shape[0])
    # remove words from both csv, and list
    words_csv = words_csv.loc[words_csv['es_words'] != current_word['es_words']]
    words_list.remove(current_word)
    print(words_csv.shape[0])
    # Write to file
    update_data_file()

    # Pick next card
    next_card()


# ------------------ Data -------------------

words_csv, words_list = load_data()
current_word: dict = {}


# --------------- Appearance ----------------

# colors
BACKGROUND_COLOR = "#B1DDC6"

# -------------------- UI --------------------

root = Tk()

root.title('Flashcard Language app 🇪🇸󠁧󠁿')
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images
CARD_BACK = PhotoImage(file='./images/card_back.png', width=800, height=526)
CARD_FRONT = PhotoImage(file='./images/card_front.png', width=800, height=526)
BUTTON_CHECK = PhotoImage(file='./images/right.png')
BUTTON_WRONG = PhotoImage(file='./images/wrong.png')

# Card
card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = card.create_image(0, 0, image=CARD_FRONT, anchor=NW)
card_language = card.create_text(400, 150, text='', font=('Arial', 40, 'italic'), fill='black')
card_word = card.create_text(400, 263, text='', font=('Arial', 50, 'bold'), fill='black')
card.grid(row=1, column=1, columnspan=2)

# Buttons
button_wrong = Button(root, image=BUTTON_WRONG, width=96, height=96, borderwidth=0, highlightthickness=0,
                      command=next_card)
button_check = Button(root, image=BUTTON_CHECK, width=96, height=96, borderwidth=0, highlightthickness=0,
                      command=remove_word)

button_wrong.grid(row=2, column=1)
button_check.grid(row=2, column=2)

# pre-run next_card to fill up the card
translate_timer = root.after(3000, show_translation)
next_card()

# Do not close the window
root.mainloop()
