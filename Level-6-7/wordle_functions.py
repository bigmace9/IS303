#Mason Chandler
#Level 06/07 Assignment

import random

#Computer chooses random word
def choose_word():
    word = ["about", "above", "adult", "alone", "angel",
    "baker", "beach", "blind", "bring", "brush",
    "chair", "climb", "crane", "dance", "dream",
    "earth", "faith", "flame", "ghost", "glove",
    "grape", "habit", "house", "ideal", 
    "knife", "lemon", "light", "magic", "money",
    "night", "ocean", "party", "phone", "plant",
    "quick", "radio", "salty",
    "smile", "stone", "table", "tiger", "uncle",
    "voice", "water", "wheat", "young", "zebra",]

    answer = random.choice(word)

    return answer

# get_guess() – Gets and validates the player’s guess. Require each guess to contain exactly five letters.
# Reject guesses that have already been used.

def get_guess(previous_guess):
    while True:
            player_guess = input("Please enter a 5 letter word:")
            player_guess = player_guess.strip().lower()
            if not (player_guess.isalpha() and len(player_guess) == 5):
                print("Invalid guess. Enter a 5 LETTER word.")
            elif player_guess in previous_guess:
                print("You already guessed that word, try again!")
            else:
                previous_guess.append(player_guess)
                return player_guess

#evaluate_guess() Compares the guess with the secret word and returns feedback
def evaluate_guess(guess, answer):
    guess = guess.lower()
    answer = answer.lower()
    result = []

    for i in range (5):
        if guess[i] == answer [i] :
            result.append("G")
        elif guess[i] in answer:
            result.append("Y")
        else:
            result.append("-")
    return result

#Display Guess, Displays the guess and its feedback.
def display_guess(guess, result ): 
    guess = guess.upper()
    guess = " ".join(guess)
    #Display Result
    result = " ".join(result)
    return "Guess:" + "\t" + guess + "\n" + "Feedback:" + result

#has_won Determines whether the player has guessed the word
def has_won(guess, answer):
    guess = guess.lower()
    answer = answer.lower()
    if guess == answer :
        result = True
    else:
        result = False
    return result


