# Stage 7/8: Error!

import random

# Write your code here
print("H A N G M A N")

words = ['python', 'java', 'kotlin', 'javascript']
choice_word = random.choice(words)

word = len(choice_word) * '-'
tries = 0
win = False
user_letter = set({})

while tries  < 8:
    
    print('\n' + word)
    if choice_word == word:
        win = True
        break
    letter = input('Input a letter:')
    
    if len(letter) != 1:
        print('You should input a single letter')
        
    elif not letter.islower():
        print('Please enter a lowercase English letter')
        
    elif letter in user_letter:
        print('You\'ve already guessed this letter')
        
    elif letter in choice_word:
        w = list(word)
        i = 0
        while i < len(choice_word):
            if choice_word[i] == letter:
                w[i] = letter
            i += 1
        word = ''.join(w) 
        user_letter.add(letter)
    
    else:
        print("That letter doesn't appear in the word")
        user_letter.add(letter)
        tries  += 1
        

if win:
    print(f'You guessed the word {choice_word}!')
    print('You survived!')
else:
    print('You lost!')