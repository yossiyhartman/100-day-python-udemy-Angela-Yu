import random

import math
from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    reps = 0
    root.after_cancel(timer)

    canvas.itemconfig(canvas_ct, text=f'{00:02d}:{00:02d}')
    UI_label.config(text='POMODORO\nTIMER', fg=PINK)
    update_checkmarks()


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    if reps == 8:
        UI_label.config(text='LONG\nBREAK', fg=PINK)
        countdown(LONG_BREAK_MIN*60)
        reps = 0
    elif reps % 2 == 0:
        UI_label.config(text='SHORT\nBREAK', fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)
    else:
        UI_label.config(text='WORK\nTIME', fg=GREEN)
        countdown(WORK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(total_seconds):
    global timer
    minutes = int(math.floor(total_seconds / 60))
    seconds = int(total_seconds % 60)

    canvas.itemconfig(canvas_ct, text=f'{minutes:02d}:{seconds:02d}')

    if total_seconds > 0:
        timer = root.after(1000, countdown, total_seconds - 1)
    else:
        start_timer()
        update_checkmarks()


# ---------------------------- UI SETUP ------------------------------- #

def update_checkmarks():
    global reps
    marks = ''
    for _ in range(math.floor(reps/2)):
        marks += '✓'
    checks.config(text=marks)


##### Widget creations
root = Tk()
canvas = Canvas(root)
UI_label = Label(root)
start_button = Button(root)
reset_button = Button(root)
checks = Label(root)

##### Styles
# Root
root.title('Pomodoro 🍅')
root.config(padx=100, pady=50, bg=YELLOW)

# Title (label)
UI_label.config(text='POMODORO\nTIMER', font=(FONT_NAME, 50, 'normal'), bg=YELLOW, fg=GREEN, width=8)

# canvas
canvas.config(width=200, height=223, bg=YELLOW, highlightthickness=0)
bg_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 111, image=bg_img)
canvas_ct = canvas.create_text(100, 130, text= "00:00", font=(FONT_NAME, 35, 'bold'))

# buttons
start_button.config(text='Start', width='7', height=2, highlightbackground=YELLOW,
                    font=(FONT_NAME, 15, 'normal'), command=start_timer)

reset_button.config(text='Reset', width='7', height=2, highlightbackground=YELLOW,
                    font=(FONT_NAME, 15, 'normal'), command=reset_timer)

# checks
checks.config(text='', font=(FONT_NAME, 25, 'bold'), bg=YELLOW, fg=GREEN)


###### positions
# row 1
UI_label.grid(row=1, column=2, sticky='ew')

# row 2
canvas.grid(row=2, column=2)

# row 3
start_button.grid(row=3, column=1)
reset_button.grid(row=3, column=3)

# row 4
checks.grid(row=4, column=2)


#### Events

# prevents the screen from closing
root.mainloop()
