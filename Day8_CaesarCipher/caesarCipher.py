from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

encrypting = True

def caesar(text: str, shift: int, directions: str):
    if directions == 'decode':
        shift *= -1

    output_message = ''

    for character in text:

        if character not in alphabet: # Think of symbols, numbers and/or spaces
            output_message += character
        else:

            # get the current index of the character
            alphabet_idx = alphabet.index(character)

            # Calculate the new index after shifting.
            shift_value = (alphabet_idx + shift) % 26

            # in case of negative, add length of alphabet
            if shift_value < 0:
                shift_value += 26

            # add to encrypted message
            output_message += alphabet[shift_value]

    print(output_message)



print(logo)

while encrypting:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text=text, shift=shift, directions=direction)

    keep_encrypting = input("Would you like to continue encrypting? 'yes' or 'no' ")

    if keep_encrypting == 'no':
        print('Goodbye')
        encrypting = False