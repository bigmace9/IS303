# Mason Chandler
# Level 03 Assignment 

import random

playing = True

# Number generation and validation
while playing:
    print("I'm thinking of a number between 1 and 100")
    iNumber = random.randint(1, 100)
    iCount = 0
    iGuess = None

    while iGuess != iNumber:
        iGuess = int(input("Enter your guess: "))

        if iGuess < 1 or iGuess > 100:
            print("Please enter a number between 1 and 100.")
            continue  

        iCount += 1

        # Number Guessing Algorithm
        if iGuess > iNumber:
            print("Guess Lower")
        elif iGuess < iNumber:
            print("Guess Higher")
        else:
            print("Congratulations! You got it!")

    print(f"You got it in {iCount} tries!")

# Response based on number of tries
    if iCount <= 3:
        print("Amazing!")
    elif iCount <= 5:
        print("Impressive!")
    elif iCount <= 7:
        print("Good job!")
    elif iCount <= 9:
        print("Took a little longer, but you got there!")
    else:
        print("You need to lock in.")

    sAgain = input("Would you like to play again? Y/N: ")
    if sAgain.upper() != "Y":
        playing = False

        #change for git