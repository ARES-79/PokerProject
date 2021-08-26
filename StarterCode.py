# PokerProject
# The project goal is to create a program that keeps track of bets and money amounts of players for poker

# Usefulness: This project is to help elimante the need for poker chips

# What I forsee the project will need:

#   A Player class with the following attributes:
  
#     name
#     current_bet
#     current_cash (money player has if they lose the round)
    
#   Player Actions:
  
#     Call (match the highest bet)
#     Raise (increase the highest bet)
#     Stay (leave the highest bet where it is)
#     Fold (forfeit the round and all the money you have already bet)

#   Game:

#   Each hand has three rounds of betting
  
#     at the end of each round, each player's bet must match or they must have folded
#       must keep track of the highest bet and check that player's have either matched the bet or folded
#     at the end of the last round, the winner recieves the pot

class Player:
    def __init__(self, name):
        self.name = name
        self.current_cash = 50 #each player starts with $50
        self.current_bet = [0, "B"] 
          # index 0 for bet amount
          #index 1 for whether they continue betting "B" or stop betting "F"
        
    def get_action(self, PokerGame):
        #     Call (match the highest bet)
        #     Raise (increase the highest bet)
        #     Stay (leave the highest bet where it is)
        #     Fold (forfeit the round)
        
        valid_act = False
        player_act = None
        
        #if they have already folded
        if self.current_bet[1] == "F":
            print(f"{self.name} has already folded. \n")
            return player_act
        
        #if their current bet is less than the highest_bet
        elif self.current_bet[0] < PokerGame.highest_bet:  
            while not valid_act:
                print(f"{self.name} must Call (C), Raise (R), or Fold (F).")
                player_act = input("Enter C, R, or F: ")
                try:
                    if player_act not in ["C", "R", "F"]:
                        raise ValueError
                    valid_act = True
                 except ValueError:
                    print("Invalid action. Try again.")
        
        #if their current bet matches the highest_bet
        elif self.current_bet[0] == PokerGame.highest_bet:
            while not valid_act:
                print(f"{self.name} must Stay (S), Raise (R), or Fold (F).")
                player_act = input("Enter S, R, or F: ")
                try:
                    if player_act not in ["S", "R", "F"]:
                        raise ValueError
                    valid_act = True
                 except ValueError:
                    print("Invalid action. Try again.")      
       
        return player_act
        
    def make_action(self, action, PokerGame):
        #     Call (match the highest bet)
        #     Raise (increase the highest bet)
        #     Stay (leave the highest bet where it is)
        #     Fold (forfeit the round)if
        pass
        
        
#not sure if this class is sopposed to go in a seperate .py file
#nor do I know how to do that
class PokerGame:
    def __init__(self, num_of_players):
        self.players = [Player(input("Input Player" + (num+1) + "'s Name: ")) for num in range(num_of_players)]
        self.highest_bet = 0
        self.round = 0
        self.pot = 0
        
   
        