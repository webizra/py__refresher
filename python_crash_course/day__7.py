wordList = ["ardverk", "baboon", "camel"]

import random
chosenWord = random.choice(wordList)
guess = input("guess a letter: ").lower()

for letter in chosenWord:
    if letter == guess:
        print("right")
    else:
        print("wrong")
print(chosenWord)