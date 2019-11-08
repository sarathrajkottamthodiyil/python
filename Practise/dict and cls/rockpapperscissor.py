from random import randint

class Game:
    player1_wins = 0
    player2_wins = 0

    def players_option(self):
        choice = ["rock", "paper", "scissor"]
        player1_choice = choice[randint(0, 2)]
        player2_choice = choice[randint(0, 2)]


        if player1_choice == player2_choice:
            print("you both selected same option !! tie")
        elif player1_choice == "rock":
            if player2_choice == "paper":
                print("player2 win!! paper covers the rock")
                self.player2_wins += 1

        # elif player1_choice == "rock":
            elif player2_choice == "scissor":
                print("player1 win!! rock broken the scissor")
                self.player1_wins += 1

        elif player1_choice == "paper":
            if player2_choice == "rock":
                print("player1 win! paper covers the rock")
                self.player1_wins += 1

        # elif player1_choice == "paper":
            elif player2_choice == "scissor":
                print("player2 win!!scissor cut the paper")
                self.player2_wins += 1

        elif player1_choice == "scissor":
            if player2_choice == "paper":
                print("player1 win!! scissor cut the paper")
                self.player1_wins += 1

        # elif player1_choice == "scissor":
            if player2_choice == "rock":
                print("player2 win!! rock broken scissor")
                self.player2_wins += 1

a = Game()
# for i in range(0, 10):
a.players_option()

print("player1:"' ' + str(a.player1_wins))
print("player2:"' ' + str(a.player2_wins))