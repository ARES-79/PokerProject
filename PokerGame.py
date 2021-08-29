class PokerGame:
    def __init__(self, num_of_players):
        self.players = [Player(input("Input Player" + (num+1) + "'s Name: ")) for num in range(num_of_players)]
        self.highest_bet = 0
        self.round = 0
        self.pot = 0  # the sum of all player's bets that goes to the winner at the end of the hand