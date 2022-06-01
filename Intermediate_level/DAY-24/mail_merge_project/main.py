PLACEHOLDER = '[name]'
NAMES_FILE = './Input/Names/invited_names.txt'
LETTER_FILE = './Input/Letters/starting_letter.txt'
COMPLETED_LETTER = './Output/ReadyToSend'

with open(NAMES_FILE) as names_file:
    names = names_file.readlines()
    

with open(LETTER_FILE) as letter_file:
    letter_contents = letter_file.read()

    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

        with open(f"{COMPLETED_LETTER}/letter_for_{stripped_name}.txt", 'w') as completed_letter:
            completed_letter.write(new_letter)