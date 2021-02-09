# Stage 4/8: Help is on the way

import random

# Write your code here
print("H A N G M A N")

words = ['python', 'java', 'kotlin', 'javascript']
choice_word = random.choice(words)

if choice_word == 'python':
    print('Guess the word pyt---:')
elif choice_word == 'java':
    print('Guess the word jav-:')
elif choice_word == 'kotlin':
    print('Guess the word kot---:')
elif choice_word == 'javascript':
    print('Guess the word jav-------:')

word = input()
if word == choice_word:
	print("You survived!")
else:
	print("You lost!")