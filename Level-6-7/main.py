#Mason Chandler
#Level 06/07 Assignment

from wordle_functions import choose_word, get_guess, evaluate_guess, display_guess, has_won

#Start of Game
print ("\nWelcome to Wordle!")
print("\nGuess the 5 Letter Word\nYou have 6 tries!")
print("\nG = Correct letter and placement\nY = Correct letter, wrong placement\n- = Wrong placement, wrong letter\n") 


game_play = True

#Game Loop
while game_play:
    computer_choice = choose_word()
    previous_guess = []
    win = False

    #Actual Gameplay Interacting Loop
    for i in range(6) :
            print(f"\nAttempt {i + 1} of 6")
            player_guess = get_guess(previous_guess)
            check_guess = evaluate_guess(player_guess, computer_choice)
            show_result = display_guess(player_guess, check_guess)
            print(show_result)
            if has_won(player_guess, computer_choice):
                 win = True
                 break

    if win == True:
        print ("You guessed it!")
    else:
         print (f'Close! The answer was {computer_choice}')


    #Input to Repeat Loop
    play_again = input("Great job! Play Again? (Yes/No): ")
    play_again = play_again.strip().lower()

    if play_again == "yes":
        print("Let's do this!")
    elif play_again == "no":
         print("Thanks for playing!")
         game_play = False
    else:
         print("We'll take that as a no, thanks for playing!")
         game_play = False











