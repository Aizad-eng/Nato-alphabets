import pandas as pd

name = input("Enter Your Name: ").upper()

data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

individual_words = []
for char in name:
    for letter, code in phonetic_dict.items():
        if char == letter:
            individual_words.append(code)
nato_alphabet_converted = " ".join(individual_words)
print(nato_alphabet_converted)
