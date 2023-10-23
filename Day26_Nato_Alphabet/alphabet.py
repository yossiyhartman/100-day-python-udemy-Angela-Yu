import pandas as pd


nato_alphabet = pd.read_csv('nato_phonetic_alphabet.csv')
alphabet = dict(zip(nato_alphabet.letter, nato_alphabet.code))

text_input = input().upper()

output = [alphabet[letter] for letter in text_input]

print(output)