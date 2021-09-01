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
        #     Call 
        #       find the difference between the PokerGame.highest_bet and player.current_bet[0]
        #       subtract the result from player.current_cash
        #       and add the result to player.current_bet[0] and pokergame.pot
        #
        #     Raise 
        #       ask for input on how much they would like to raise the highest_bet by
        #             (screen input)
        #       add this amount to the PokerGame.highest_bet 
        #       remove (PokerGame.highest_bet - current_bet[0]) from player.current_cash and add it to PokerGame.pot
        #       increase current_bet[0] to match highest_bet
        #
        #     Stay 
        #       leave the everything as is
        #       
        #     Fold 
        #       change current_bet[1] to "F"
        #
        if(action=="C"):
            self.__call(PokerGame)
        elif(action=="R"):
            self.__raise(PokerGame)
        elif(action == "S"):
            return
        else:
           self.__fold()
        
    
    #private helper method to call within make_action method
    def __call(self, PokerGame):
        #       Call 
        #       find the difference between the PokerGame.highest_bet and player.current_bet[0]
        #       subtract the result from player.current_cash
        #       and add the result to player.current_bet[0] and pokergame.pot
        result = PokerGame.highest_bet - self.current_bet[0]
        if self.current_cash - result < 0:
            print("You don't have enough chips to Call. You have to fold.")
            self.__fold(self)
            return
        self.current_cash -= result
        self.current_bet[0] += result
        PokerGame.pot += result


    def __raise(self, PokerGame):
        #       Raise 
        #       ask for input on how much they would like to raise the highest_bet by
        #             (screen input)
        #       add this amount to the PokerGame.highest_bet 
        #       remove (PokerGame.highest_bet - current_bet[0]) from player.current_cash and add it to PokerGame.pot
        #       increase current_bet[0] to match highest_bet

        print("Enter how much you would like to raise?")
        raise_amount = int(input())
        temp = PokerGame.highest_bet + raise_amount
        cash_needed = self.current_cash - (temp - self.current_bet[0])
        while(cash_needed < 0):
            print("You don't have enough chips to raise that much. You have " + str(self.current_cash) + " chips.")
            print("Enter raise amount:")
            raise_amount = int(input())
            temp = PokerGame.highest_bet + raise_amount
        PokerGame.highest_bet += raise_amount
        self.current_cash -= PokerGame.highest_bet - self.current_bet[0]
        PokerGame.pot += PokerGame.highest_bet - self.current_bet[0]
        self.current_bet[0] = PokerGame.highest_bet

        pass

    def __fold(self):
        #     Fold 
        #       change current_bet[1] to "F"
        self.current_bet[1] = "F"

#not sure if this class is sopposed to go in a seperate .py file
#nor do I know how to do that
class PokerGame:
    def __init__(self, num_of_players):
        self.players = [Player(input("Input Player" + (num+1) + "'s Name: ")) for num in range(num_of_players)]
        self.highest_bet = 0
        self.round = 0
        self.pot = 0  # the sum of all player's bets that goes to the winner at the end of the hand
        
   
        
