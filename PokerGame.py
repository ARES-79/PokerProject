from StarterCode import Player

import time 

class PokerGame:

    def __init__(self, num_of_players):
        self.players = [Player(input(f"Input Player {num + 1}\'s Name: ")) for num in range(num_of_players)]
        self.highest_bet = 0
        self.round = 0
        self.pot = 0  # the sum of all player's bets that goes to the winner at the end of the hand

    def __repr__(self) -> str:
        s = " Player:    "
        for player in self.players:
            s += player.name + "     "
        s += "\n Cash:      "
        for player in self.players:
            s += str(player.current_cash) + "     "
        s += "\n Bet:       "
        for player in self.players:
            s += str(player.current_bet) + "     "

        return s

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
    #time.sleep(5)
    print("Player Actions While Betting- ")
    print("* Not all actions will be available in every situation *")
    print("1. Call (match the highest bet *if your bet is lower than the highest bet*)")
    print("2. Raise (increase the highest bet)")
    print("3. Stay (leave the highest bet as is *if your bet already matches the highest bet*)")
    print("4. Fold (forfeit the round and all the money you have already bet)")
    print("")
    #time.sleep(5)
    print("Let the game begin!")
    return game

def game_play(game):
    print(game)


game_play(game_start())