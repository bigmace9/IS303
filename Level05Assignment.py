# Mason Chandler
# Level 05 Assignment

#Custom Functions
def get_player_choice () :
    player = input("\nPick Rock, Paper, or Scissors: ").lower()
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
print ("\nLet's play!")

wins = 0 
losses = 0

#Gameplay
rounds = int(intro)
while wins + losses < rounds:
    player = get_player_choice()
    computer = random.choice(options)
    print(f'Computer chose: {computer}')
    result = determine_winner(player,computer)
    if result == "win" :
        print("You won!")
        wins += 1
    elif result == "loss" :
        print("You lost! Bummer!")
        losses += 1
    else:
        print ("Tie, Try Again!")


#Final Output
print (f'\nEnding score - You won: {wins}| Computer won: {losses}')
if wins > losses:
    print ("You won!")
else:
    print ("You lost!")
print("Thanks for playing - play again!")

