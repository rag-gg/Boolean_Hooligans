from random import randrange
import random

recyc_items = ['PAPER', 'CARDBOARD', 'GLASS' , 'WOOD' , 'ALUMINIUM' , 'COPPER', 'CEMENT', 'LEATHER', 'RUBBER']
nonrecyc_items = ['STYROFOAM','PLASTIC','STEEL', 'CERAMIC', 'SOIL', 'COAL', 'COTTON', ]

items = recyc_items + nonrecyc_items

index = randrange(0,len(items))
actual_word = items[index]

L = list(items[index])
random.shuffle(L)
shuffled = ''.join(L)

guessed_word = ''
lives = 5
points = 0
while lives > 0:
  print(f'\nWord: {shuffled} Points: {points} Lives: {lives}\n----------')
  print("Guess the material from the scrambled word")
  guessed_word = input('Guess (Q to quit): ').upper()
  if guessed_word == 'Q':
    exit()
  elif guessed_word == actual_word:
    print('You got it! +50 Points\nIs this item recyclable?(for bonus points)')
    points+=50
    answer = input('Y or N: ').capitalize()
    if answer == 'Y':
      if actual_word in recyc_items:
        print('\nGood job! +75 Bonus points')
        points += 75
      else:
        print("\nThat's incorrect (No lives lost)")
    elif answer == 'N':
      if actual_word in nonrecyc_items:
        print('\nGood job! +75 Bonus points')
        points += 75
      else:
        print("\nThat's incorrect (No lives lost)")
    
    index = randrange(0,len(items))
    actual_word = items[index]
    
    L = list(items[index])
    random.shuffle(L)
    shuffled = ''.join(L)
    print('\nNext item...')
  else:
    lives-= 1
    print('Wrong word, try again!')


print(f'\n\nYou Lost!, Run the code to play again!\nFinal Score: {points} points')