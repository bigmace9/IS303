# Mason Chandler
# Level 05 Assignment

#Custom Functions
def get_player_choice () :
    player = input("Pick Rock, Paper, or Scissors: ").lower()
    while player not in ["rock", "paper", "scissors"] : 
        print ("Invalid, Please try again")
        player = input("Pick Rock, Paper, or Scissors: ").lower()
    return player

def determine_winner(player, computer) :
    if player == computer:
        return "tie"
    beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    if beats[player] == computer: 
        return "win"
    return "loss"

#Start of the Game
import random
options = ("rock", "paper", "scissors" )
intro = input("Welcome to Rock, Paper, Scissors!\n How many rounds would you like to play: ")

#Filtering to valid inputs
while not intro.isdigit() or int(intro) % 2 == 0 :
    print ("Invalid. Please enter an odd NUMBER: ")
    intro = input("How many rounds would you like to play: ")
print ("Let's play!")

#Choice
player = get_player_choice()
computer = random.choice(options)

result = determine_winner(player,computer)

print(result)


#Computing the Answer
