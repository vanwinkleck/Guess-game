lowestPossible = 1
highestPossible = 100
print('Pick a number from 1 to 100 and let me guess it')
found = False
numberOfGuesses = 0
while not found:
  guess = (lowestPossible + highestPossible)//2
  print('\nIs it', str(guess) + '?')
  print('Or is my guess too low or too high?')
  answer = input('Enter correct, low or high: ')
  numberOfGuesses += 1
  if answer == 'low':
    lowestPossible = guess + 1
  elif answer == 'high':
    highestPossible = guess - 1
  elif answer == 'correct':
    found = True
print('\I found it in', numberOfGuesses, 'guesses!')

