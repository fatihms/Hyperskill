# Stage 5/8: Keep trying

import random

# Write your code here
print("H A N G M A N")

words = ['python', 'java', 'kotlin', 'javascript']
choice_word = random.choice(words)

word = len(choice_word) * '-'
tries = 0
while tries  < 8:
    print('\n' + word)
    letter = input('Input a letter:')
    if letter in choice_word:
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

print("\nThanks for playing!")
print("We'll see how well you did in the next stage")