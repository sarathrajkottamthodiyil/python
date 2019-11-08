from random import randint

options = ["rock", "paper", "scissor"]

player1 = options[randint(0, 2)]
player2 = options[randint(0, 2)]



if player1 == player2:
    print("!!!play again!!!")
elif player1 == "rock":
    if player2 == "paper":
        print("player2 !!!win!!!", player2, "covers", player1)
    else:
        print("player2 !!!loss!!!", player1, "broken", player2)
elif player1 == "paper":
    if player2 == "scissor":
        print("player2 !!!win!!!", player2, "cut", player1)
    else:
        print("player2 !!!loss!!!", player1, "cover", player2)
elif player1 == "scissor":
    if player2 == "rock":
        print("player2 !!!win!!!", player2, "broken", player1)
    else:
        print("player2 !!!loss!!!", player1, "cut", player2)

'''
player1_choice = choice[randint(0, 2)]
player2_choice = choice[randint(0, 2)]
if player1_choice == player2_choice:
    print("you both selected same option !! tie")
elif player1_choice == "rock":
    if player2_choice == "paper":
        print("player2 win!! paper covers the rock")
elif player1_choice == "rock":
    if player2_choice == "scissor":
        print("player1 win!! rock broken the scissor")
elif player1_choice == "paper":
    if player2_choice == "rock":
        print("player1 win! paper covers the rock")
elif player1_choice == "paper":
    if player2_choice == "scissor":
        print("player2 win!!scissor cut the paper")
elif player1_choice == "scissor":
    if player2_choice == "paper":
        print("player1 win!! scissor cur the paper")
elif player1_choice == "scissor":
    if player2_choice == "rock":
        print("player2 win!! rock broken scissor")
else:
    print("please enter a valid option!")
'''
