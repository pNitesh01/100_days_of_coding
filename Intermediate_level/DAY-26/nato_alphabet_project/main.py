import pandas as pd

FILE_PATH = 'nato_phonetic_alphabet.csv'

nato_df = pd.read_csv(FILE_PATH)

nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}

is_input_valid = False

while not is_input_valid:
    username = input("Enter your name: ").upper()
    
    try:
        nato_code = [nato_dict[letter] for letter in username]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        is_input_valid = True


print(nato_code)