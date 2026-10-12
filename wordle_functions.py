#Mason Chandler
#Level 06/07 Assignment

# Functions: choose_word(), get_guess(), evaluate_guess(), display_guess(), has_won()
import random

def choose_word():
    word = ["about", "above", "adult", "alone", "angel",
    "baker", "beach", "blind", "bring", "brush",
    "chair", "climb", "crane", "dance", "dream",
    "earth", "faith", "flame", "ghost", "glove",
    "grape", "habit", "house", "ideal", "jolly",
    "knife", "lemon", "light", "magic", "money",
    "night", "ocean", "party", "phone", "plant",
    "queen", "quick", "radio", "river", "salty",
    "smile", "stone", "table", "tiger", "uncle",
    "voice", "water", "wheat", "young", "zebra",]

    answer = random.choice(word)

    return answer

# get_guess() – Gets and validates the player’s guess.

def get_guess():
    player_guess = input("Enter your 5 letter guess here: ")
    if player_guess 
