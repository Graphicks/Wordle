import random

def generate_word():
  f = open("word.txt","r")
  all_words = f.read().splitlines()
  correct_word = [random.choice(all_words)]
  return correct_word


def checkMatch(correct_word, user_guess, repeat, match_results, guesses):
  if user_guess[0] == correct_word[0]:
    print(f"\033[1;32;40m{user_guess[0]} is the correct word!")
    repeat = False
    

  else:
    for i in range(0,len(correct_word[0])):
      
      if user_guess[0][i] == correct_word[0][i]:
        word = (f"\033[1;32;40m{user_guess[0][i]}")
        
        
        

      elif user_guess[0][i] in correct_word[0]:
        word = (f"\033[1;33;40m{user_guess[0][i]}")
        
        
  
      else:
        word =(f"\033[1;31;40m{user_guess[0][i]}")

      match_results.append(word)
        
    str1 = ''.join(match_results) 
    match_results.clear()
    print(f"\n{str1}")
    print(f"\033[1;37;40m{guesses} guesses reamin!")
    
    
  return repeat