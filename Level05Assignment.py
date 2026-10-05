# Mason Chandler
# Level 05 Assignment

#Start of the Game
import random
intro = float(input("Welcome to Rock, Paper, Scissors!\n How many rounds would you like to play: "))

if intro % 2 == 0 :
    print("Invalid. Please enter an odd number ")
    intro = input("How many rounds would you like to play: ")
else :
    print ("Let's play!")

#Gameplay
player_choice = input("Pick Rock, Paper, Scissors: ")
options = ("Rock", "Paper", "Scissors" )
computer_choice = random.choice(options)

print (computer_choice)
print (player_choice)