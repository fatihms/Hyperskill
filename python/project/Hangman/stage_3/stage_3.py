# Stage 3/8: Make your choice

import random

# Write your code here
print("H A N G M A N")

words = ['python', 'java', 'kotlin', 'javascript']
choice_word = random.choice(words)

print("Guess the word: ")
word = input()
if word == choice_word:
	print("You survived!")
else:
	print("You lost!")
