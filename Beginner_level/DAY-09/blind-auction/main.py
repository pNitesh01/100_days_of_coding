from art import logo
import os

bidders = {}

print(logo + "\nWelcome to the secret auction program.\n")

more_to_go = True

while more_to_go:
    
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    choice = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if choice == 'yes':
        os.system('cls')
        more_to_go = True
    else:
        more_to_go = False

def get_winner():
    person = ''
    amount = 0
    
    for name in bidders:
        if bidders[name] > amount:
            person = name
            amount = bidders[name]
    return person
    
os.system('cls')
       
print(f"The winner is {get_winner()} with a bid of ${bidders[get_winner()]}.")