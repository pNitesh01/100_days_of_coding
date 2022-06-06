import pandas as pd

FILE_PATH = 'nato_phonetic_alphabet.csv'

nato_df = pd.read_csv(FILE_PATH)

nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}

username = input("Enter your name: ").upper()

nato_code = [nato_dict[letter] for letter in username]
print(nato_code)