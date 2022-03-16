from functions import generate_word, checkMatch
print("\033[1;34;40mWordle 2022")

######### ---------- VARIABLES

correct_word = generate_word()
print(correct_word)

guesses = 0
repeat = True

user_guess = []
match_results = [] #### basically joins all the check match iterations so its not on each different lines, didn't know what to call it tho 



# --------------- RUN GAME
while guesses <= 5 and repeat == True:
  
  guess = input("\033[1;34;40mGuess the word:  \033[1;37;40m").lower()
  
  

  if len(guess) == 5:
    
    user_guess.append(guess)
    repeat = checkMatch(correct_word, user_guess, repeat, match_results)
    user_guess.pop(0)
    
    guesses+=1 
  else:
    print("\033[1;31;40m\nPlease input a 5 letter word!\n")
  