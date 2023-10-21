

with open(file='./Input/Letters/starting_letter.txt', mode='r') as file_starting_letter:
    starting_letter = file_starting_letter.read()

    with open(file='./Input/Names/invited_names.txt', mode='r') as file_names:

        for name in file_names.readlines():
            n = name.strip()
            invite = starting_letter.replace('[name]', n)

            with open(file=f'./Output/ReadyToSend/letter_to_{n.replace(" ", "_")}.txt', mode='w') as letter:
                letter.write(invite)