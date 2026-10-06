# Mason Chandler
# Level 05 Assignment

#Start of the Game
import random
intro = input("Welcome to Rock, Paper, Scissors!\n How many rounds would you like to play: ")

#Filtering to valid inputs
while not intro.isdigit() or int(intro) % 2 == 0 :
    print ("Invalid. Please enter an odd NUMBER: ")
    intro = input("How many rounds would you like to play: ")

print ("Let's play!")

#Choice
player_choice = input("Pick Rock, Paper, Scissors: ")
options = ("Rock", "Paper", "Scissors" )
computer_choice = random.choice(options)

#Computing the Answer


print (f'The computer chose: {computer_choice}')
print (f'Your choice: {player_choice}')
