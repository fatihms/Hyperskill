# Stage 6/8: The value of life

import random

# Write your code here
print("H A N G M A N")

words = ['python', 'java', 'kotlin', 'javascript']
choice_word = random.choice(words)

word = len(choice_word) * '-'
tries = 0
win = False
while tries  < 8:
    print('\n' + word)
    if choice_word == word:
        win = True
    letter = input('Input a letter:')
    if letter in word:
        print('No improvements')
        tries  += 1
    elif letter in choice_word:
        w = list(word)
        i = 0
        while i < len(choice_word):
            if choice_word[i] == letter:
                w[i] = letter
            i += 1
        word = ''.join(w)    
    else:
        print("That letter doesn't appear in the word")
        tries  += 1



if win:
    print('You survived!')
else:
    print('You lost!')