import random, os
from art import logo, vs
from game_data import data

def get_choice_b(choice_a):
    choice_b = random.choice(data)
    while choice_a == choice_b:
        choice_b = random.choice(data)    
    return choice_b
   
def play_game():
    print(logo)

    score = 0
    is_game_over = False
    choice_a = random.choice(data)
    choice_b = get_choice_b(choice_a)
        
    while not is_game_over:
        print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}")
        print(vs)
        print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}")
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if (choice == 'a' and choice_a['follower_count'] > choice_b['follower_count']) or (choice == 'b' and choice_b['follower_count'] > choice_a['follower_count']):
            score += 1
            os.system('cls')
            print(logo)
            print(f"You're right, current score: {score}")
            choice_a = choice_b
            choice_b = get_choice_b(choice_a)

        else:
            os.system('cls')
            print(logo)
            print(f"You're wrong, final score: {score}")
            is_game_over = True
            

play_game()