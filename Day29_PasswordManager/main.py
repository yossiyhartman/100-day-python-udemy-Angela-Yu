import json
from tkinter import messagebox
from tkinter import *
import random
from string import ascii_letters, digits, punctuation

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """ generate a random password of length 25"""
    password = []

    [ password.append(random.choice(ascii_letters)) for _ in range(13) ]
    [ password.append(random.choice(digits)) for _ in range(6) ]
    [ password.append(random.choice(punctuation)) for _ in range(6) ]

    random.shuffle(password)

    entry_password.delete(0, END)
    entry_password.insert(0, ''.join(password))

# ---------------------------- SAVE PASSWORD ------------------------------- #

def collect_values() -> tuple[str, str, str]:
    """ Collects the values of entries """
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    return website, username, password


def password_already_exists(file, website, username) -> tuple[bool, int]:
    """ Loops through the file and checks if the website/username combination exists """
    for i, pw in enumerate(file):
        if website == pw['website'] and username == pw['username']:
            return True, i

    return False, 0

def clear_entries():
    entry_website.delete(0, END)
    entry_password.delete(0, END)


def update_passwords(file, index, password):
    """ Update a existing website/username combination with a new password """
    file[index]['password'] = password


def add_password(file, website, username, password):
    """ Add a new website/username combination to the file """
    file.append({
        "website" : website,
        "username": username,
        "password": password
    })


def save_password() -> None:
    """ Save the passwords to a JSON file """
    with open('passwords.json', 'r') as f:
        passwords = json.load(f)

    w, u, p = collect_values()

    if '' in [w, u, p]:
        messagebox.showwarning(title='empty fields', message="You haven't filed in all the input fields")
    else:
        pw_exists, index = password_already_exists(passwords, w, u)

        if pw_exists:
            if messagebox.askokcancel(title='update website/username combination',
                                   message= f"""
                                    this website & username combination already exists. Would you like
                                    to update the values to the following combination:
                                     website: {w}, username: {u}, new password: {p} 
                                    """):

                update_passwords(passwords, index, p)
        else:
            if messagebox.askokcancel(title='add website/username combination',
                                   message= f"""
                                    Would you like add the values of the following combination:
                                     website: {w}, username: {u}, new password: {p} 
                                    """):
                add_password(passwords, w, u, p)

        with open('passwords.json', 'w') as f:
            json.dump(passwords, f, indent=4)

        clear_entries()




# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title('Password Manager 🔐')
root.config(padx=20, pady=50)

canvas = Canvas(root, width=200, height=200)
background_img = PhotoImage(file='./logo.png')
canvas.create_image(0, 0, image=background_img, anchor=NW)
canvas.grid(row=1, column=2)

label_website = Label(text='Website')
entry_website = Entry(width=10)
entry_website.focus()
label_website.grid(row=2, column=1, sticky='e', pady=5)
entry_website.grid(row=2, column=2, columnspan=2, padx=(15, 0), sticky='nsew')

label_username = Label(text='username/email')
entry_username = Entry(width=10)
entry_username.insert(index = 0, string='joh.doe@gmail.com')
label_username.grid(row=3, column=1, sticky='e', pady=5)
entry_username.grid(row=3, column=2, columnspan=2, padx=(15, 0), sticky='nsew')

label_password = Label(text='password')
entry_password = Entry(width=10)
button_generate = Button(text='generate password', command=generate_password)
label_password.grid(row=4, column=1, sticky='e', pady=5)
entry_password.grid(row=4, column=2, columnspan=1, padx=(15, 0), sticky='nsew')
button_generate.grid(row=4, column=3, padx=(15, 0), pady=0)

button_add = Button(text='Add', command=save_password)
button_add.grid(row=5, column=2, columnspan=2, padx=(15, 0), sticky='ew')

root.mainloop()
