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

# get_guess() – Gets and validates the player’s guess. Require each guess to contain exactly five letters.
# Reject guesses that have already been used.

def get_guess(guessed):
    while True:
        player_guess = input("Enter your 5 letter guess here: ").strip().lower()
        if len(player_guess) != 5 or not player_guess.isalpha():
            print("Invalid. Your guess needs to be 5 letters")
        elif player_guess in guessed:
            print("You've already guessed that, try again.")
        else:
            return player_guess


value = get_guess()
print (value)
