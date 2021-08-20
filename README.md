# PokerProject
The project goal is to create a program that keeps track of bets and money amounts of players for poker

Usefulness: This project is to help elimante the need for poker chips

What I forsee the project will need:

  A Player class with the following attributes:
    name
    current_bet
    current_cash (money player has if they lose the round)
    
  Player Actions:
    Call (match the highest bet)
    Raise (increase the highest bet)
    Stay (leave the highest bet where it is)
    Fold (forfeit the round and all the money you have already bet)

  Game:
  Each hand has three rounds of betting:
    at the end of each round, each player's bet must match or they must have folded
      must keep track of the highest bet and check that player's have either matched the bet or folded
    at the end of the last round, the winner recieves the pot

