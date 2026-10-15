#Mason Chandler
#Level 06/07 Assignment

# Functions: choose_word(), get_guess(), , display_guess(), has_won()
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

def get_guess():
    while True:
        try:
            player_guess = input("Please enter a 5 letter word:")
            if not (player_guess.isalpha and len(player_guess) == 5):
                raise ValueError
            print ("Good guess!")
            return(player_guess)
        except ValueError:
            print("Invalid Guess. Enter a 5 letter word.")

#evaluate_guess() Compares the guess with the secret word and returns feedback, pass #1, find greens, pass #2 find yellows
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
    #Display Guess
    guess = guess.upper()
    guess = " ".join(guess)
    #Display Result
    result = " ".join(result)
    return guess + "\n" + result

#has_won Determines whether the player has guessed the word

def has_won(guess, answer):
    guess = guess.lower()
    answer = answer.lower()
    if guess == answer :
        print("You guessed it! God job!")
    else:
        print ("Not quite, keep guessing!")

guess = "trail"
answer = "audio"

won = has_won(guess, answer)
print(won)



