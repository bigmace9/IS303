#Mason Chandler
#Level 06/07 Assignment

from wordle_functions import choose_word, get_guess, evaluate_guess, display_guess, has_won

#Start of Game
print ("Welcome to Wordle!")
print("\nGuess the 5 Letter Word")
print("\nG = Correct letter and placement\nY = Correct letter, wrong placement\n- = Wrong placement, wrong latter")

#Choices being made 
computer_choice = choose_word()
player_guess = get_guess()
check_guess = evaluate_guess(player_guess, computer_choice)
show_result = display_guess(player_guess, check_guess)
win = has_won (player_guess, computer_choice)

print (show_result)
print (win)
