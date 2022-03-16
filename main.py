import random

guesses = 0
print("Wordle 2022")


f = open("word.txt","r")
all_words = f.read().splitlines()


correct_word = [random.choice(all_words)]


user_guess = []
repeat = True

def checkMatch(correct_word, user_guess, repeat):
  if user_guess[0] == correct_word[0]:
    print(f"\033[1;32;40m{user_guess[0]} you guessed correct!")
    repeat = False
    

  else:
    for i in range(0,len(correct_word[0])):
  
      if user_guess[0][i] == correct_word[0][i]:
        print(f"\033[1;32;40m{user_guess[0][i]}")
        

      elif user_guess[0][i] in correct_word[0]:
        print(f"\033[1;33;40m{user_guess[0][i]}")
      
      else:
        print(f"\033[1;31;40m{user_guess[0][i]}")

  return repeat


while guesses <= 5 and repeat == True:
  
  guess = input("\033[1;37;40mGuess the word:  ").lower()
  user_guess.append(guess)
  

  if len(guess) == 5:
    
    repeat = checkMatch(correct_word, user_guess, repeat)
    user_guess.pop(0)
    guesses+=1 
  else:
    print("Please input a 5 letter word!")
    


  
  