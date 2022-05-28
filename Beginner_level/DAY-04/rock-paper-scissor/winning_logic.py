def game_logic(computer, player):
    if computer == player:
        print("It's a Draw.")
    
    else:
        if computer == 0:
            if player == 1:
                print("You Won!")
            else:
                print("You Lose!")

        elif computer == 1:
            if player == 0:
                print("You Lose!")
            else:
                print("You Won!")

        else:
            if player == 0:
                print("You Won!")
            else:
                print("You Lose!")