import random
import rock, paper, scissors, winning_logic

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print("You chose:")
if player == 0:
    print(rock.rock)
elif player == 1:
    print(paper.paper)
elif player == 2:
    print(scissors.scissors)
else:
    print(quit)

    
computer = random.randint(0, 2)

print("Computer chose:")
if computer == 0:
    print(rock.rock)
elif computer == 1:
    print(paper.paper)
else:
    print(scissors.scissors)

# Game Logic
winning_logic.game_logic(computer, player)