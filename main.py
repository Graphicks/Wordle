from functions import generate_word, checkMatch
print("\033[1;34;40mWordle 2022")

######### ---------- VARIABLES

correct_word = generate_word()

guesses = 6
repeat = True

user_guess = []
match_results = [] #### basically joins all the check match iterations so its not on each different lines, didn't know what to call it tho 



# --------------- RUN GAME
while guesses >= 0 and repeat == True:
  
  guess = input("\033[1;34;40m\nGuess the word:  \033[1;37;40m").lower()

  if len(guess) == 5 and guesses > 0:
    
    guesses-=1 
    user_guess.append(guess)
    repeat = checkMatch(correct_word, user_guess, repeat, match_results, guesses)
    user_guess.pop(0)
   
  elif len(guess) != 5:
    print("\033[1;31;40m\nPlease input a 5 letter word!\n")

  else:
    print(f"\nNice try! The correct word was {''.join(correct_word)}!")
    repeat = False
  