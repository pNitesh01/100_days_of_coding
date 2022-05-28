from random import randint
from os import system
from art import logo

system('cls')
system('color 0e')

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if level == "easy":
    lives = 10
elif level == "hard":
    lives = 5
    
actual_number = randint(1, 100)

got_it_right = False

while lives > 0 and not got_it_right:
    print(f"You have {lives} attempts remaining to guess the number.")
    guessed_number = int(input("Make a guess: "))
    
    if actual_number == guessed_number:
        got_it_right = True
        print("Yay! You got it right.")
    else:
        lives -= 1
        
        if actual_number > guessed_number:
            print("Too low.\nGuess again.")
        else:
            print("Too high.\nGuess again.")

    if lives == 0:
        print("Oops. Out of lives.")

system('color 0f')
