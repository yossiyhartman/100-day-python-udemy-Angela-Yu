import pandas as pd
import datetime as dt
import random
import smtplib

EMAIL_HANDLER = {
    'email': 'testyossiyanou@gmail.com',
    'password': 'shumsjssynjcxbew',
    'smtp': 'smtp.gmail.com',
    'port': 587
}


def pick_letter():
    try:
        with open(f'./letter_templates/letter_{random.randint(1,3)}.txt', mode='r') as f:
            letter = f.read()
    except FileNotFoundError:
        print(f'There are no letter templates')
    else:
        return letter


def adjust_letter(file:str, name: str):
    return file.replace("[NAME]", name)


def email_letter(letter, email):
    with smtplib.SMTP(EMAIL_HANDLER['smtp'], port=EMAIL_HANDLER['port']) as connection:
        connection.starttls()
        connection.login(user=EMAIL_HANDLER['email'], password=EMAIL_HANDLER['password'])
        connection.sendmail(
            from_addr=EMAIL_HANDLER['email'],
            to_addrs=email,
            msg=f'f"Subject:Happy Birthday!/n/n{letter}'
        )


def send_birthday_letter(name: str, email: str) -> None:
    named_letter = adjust_letter(pick_letter(), name)
    email_letter(named_letter, email)


def check_birthdays():
    """ Retrieves a csv with contacts, and check if their birthday is due """
    today = dt.datetime.today()

    try:
        birthdays = pd.read_csv("./data/birthdays.csv", parse_dates=['DOB'], dayfirst=True)

    except FileNotFoundError:
        pass

    else:
        for idx, row in birthdays.iterrows():
            if today.month == row['DOB'].month & today.day == row['DOB'].day:
                print("go shawty, it's your birthday")
                send_birthday_letter(row['name'], row['email'])


if __name__ == '__main__':
    check_birthdays()
