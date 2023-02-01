from termcolor import colored

wordle = 'apple'
index = 0
tries = 6
print('guess the word in 6 tries')
for x in range(6):
  word_guess = input('guess a word ')
  if len(word_guess) == 5:
    tries -=1
    if word_guess == wordle:
      print(colored(word_guess, 'green'))
      print('you won!')
      break
    else:
      for char in word_guess:
        if char == wordle[index]:
          print(colored(char, 'green'))
        elif char in wordle:
          print(colored(char, 'yellow'))
        else:
          print(colored(char, 'grey'))
        
        index += 1
      index = 0
      print(f'you have {tries} tries remaining')
  else:
    print('5 letters')
    
if tries == 0:
  print('you lost')