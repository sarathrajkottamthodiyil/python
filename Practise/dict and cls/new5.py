from random import randint

options = ["rock", "paper", "scissor"]

oponent = options[randint(0, 2)]

player = input("rock, paper, scissor:?")
if player == oponent:
    print("skip to next turn")
elif player == "rock":
    if oponent == "paper":
        print("You lose!", oponent, "covers", player)
    else:
        print("you win!", player, "broken", oponent)
elif player == "paper":
    if oponent == "scissor":
        print("you lose!", oponent, "cut", player)
    else:
        print("you win!", player, "covers", oponent)
elif player == "scissor":
    if oponent == "rock":
        print("you lose!", oponent, "broken", player)
    else:
        print("you win!", player, "cut", oponent)
else:
    print("please enter valid input")

