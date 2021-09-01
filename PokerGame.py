from StarterCode import Player

import time 

class PokerGame:

    def __init__(self, num_of_players):
        self.players = [Player(input(f"Input Player {num + 1}\'s Name: ")) for num in range(num_of_players)]
        self.highest_bet = 1
        self.round = 0
        self.pot = 0  # the sum of all player's bets that goes to the winner at the end of the hand

    def __repr__(self) -> str:
        s = "\n Player:    "
        for player in self.players:
            s += player.name + "     "
        s += "\n Cash:      "
        for player in self.players:
            s += str(player.current_cash) + "     "
        s += "\n Bet:       "
        for player in self.players:
            s += str(player.current_bet) + "     "
        s+= "\n"
        return s
        #currently a poor excuse for a table of values
        #would like to go back and perfect this using strng formating

    def bets_match(self) -> bool:
        for player in self.players:
            if player.current_bet[0] != self.highest_bet and player.current_bet[1] != "F":
                return False
        return True

    def winners_pot(self) -> int:
        print("Who won the hand?" )
        for index in range(len(self.players)):
            print("(", index +1, ")", " ", self.players[index].name, sep = "", end = "  ")
        print("")
        winner = input("Please input the number to the left of the player's name: ")
        valid_input = False
        while not valid_input:
            try:
                val_winner = int(winner)
                if val_winner < 0 or val_winner > len(self.players):
                    raise ValueError
                valid_input = True
            except ValueError:
                print("Invalid winner. Try again.")
                winner = input("Please input the number to the left of the player's name: ")


        return val_winner

    def reset(self):
        self.pot = 0
        self.highest_bet = 1
        for player in self.players:
            player.current_bet = [0, "B"]

def game_start():
    print("")
    print("Welcome to the Poker Project.")
    print("")
    game = PokerGame(int(input("How many people are playing?: ")))
    print("Players:", *[player.name for player in game.players] )
    print("")
    time.sleep(1)
    print("Basic Rules - ")
    print("Each hand has three rounds of betting where each player bets. At the end of each round, ")
    print("each player's bet must match the highest bet or they must have folded.")
    print("At the end of the last round, the winner recieves the pot.")
    print("")
    time.sleep(3)
    print("Player Actions While Betting- ")
    print("* Not all actions will be available in every situation *")
    print("1. Call (match the highest bet *if your bet is lower than the highest bet*)")
    print("2. Raise (increase the highest bet)")
    print("3. Stay (leave the highest bet as is *if your bet already matches the highest bet*)")
    print("4. Fold (forfeit the round and all the money you have already bet)")
    print("")
    time.sleep(1)
    print("Let the game begin!")
   
    return game

def game_play(game):
    time.sleep(1)
    print(game)
    keep_playing = True
    while keep_playing:
        print(f"\nRound {game.round % 3 +1} of betting - ")
        print(f"The highest bet is currently {game.highest_bet}.")
        print(f"The pot is currently {game.pot}. \n")
        bets_match = False
        while not bets_match:
            for player in game.players:
                player.make_action(player.get_action(game), game)
                print(game)
            bets_match = game.bets_match()
        if game.round % 3 == 2:
            print("Betting has ended.")
            game.players[game.winners_pot()-1].current_cash += game.pot
            game.reset()
            print(game)
            if input("Would you like to continue playing? (Y) Yes (N) No\n") == "N":
                keep_playing = False
        game.round += 1
        time.sleep(2)
        
    # use % 3 for the pattern of rounds

game_play(game_start())