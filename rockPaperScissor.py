#6.Make a two - player Rock - Paper - Scissors game.(Hint: Ask for player plays(using input), compare them,
# print out a message of congratulations to the winner, and ask if the players want to start a new game)
# Remember the rules:  Rock beats scissors
#Scissors beats paper
#Paper beats rock


def game():
    player1 = (input(" player 1"))
    player2 = (input(" player 2"))

    if (player1.lower == "rock") and (player2.lower == "scissor"):
        print("player 1 wins")
    elif (player1.lower == "scissor") and (player2.lower == "paper"):
        print("player 1 wins")
    elif (player1.lower == "paper") and (player2.lower == "rock"):
        print("player 1 wins")
    elif (player1.lower == player2.lower):
        print("tie")
    else:
        print("player 2 wins")


game()
