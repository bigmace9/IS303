#Mason Chandler
#Level 06/07 Assignment

from wordle_functions import choose_word, get_guess, evaluate_guess, display_guess, has_won

#Start of Game
print ("\nWelcome to Wordle!")
print("\nGuess the 5 Letter Word\nYou have 6 tries!")
print("\nG = Correct letter and placement\nY = Correct letter, wrong placement\n- = Wrong placement, wrong latter\n")

#Choices being made 
game_play = True

while game_play:
    computer_choice = choose_word()
    previous_guess = set()
    win = False

    for i in range(6) :
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



    play_again = input("Great job! Play Again? (Yes/No): ")
    play_again = play_again.strip().lower()

    if play_again == "yes":
        print("Let's do this!")
    else:
        print("Thanks for playing!")
        game_play = False










