import random
import sys

dictionary = ["PIZZA", "PANCAKES", "GOLF"]
randomWord = dictionary[random.randrange(0, len(dictionary))]

blankArray = []

def startup(time):
    if time == "initial":
        for i in range(1, len(randomWord) + 1):
            blankArray.append("_")
    print(" ".join(blankArray))
    letterToGuess = raw_input("Pick one letter: ").upper()
    guess(letterToGuess)

def guess(letter):
    for i in range(0, len(list(randomWord))):
        if letter == randomWord[i]:
            blankArray[i] = letter
    if randomWord == "".join(blankArray):
        print("You Win!")
        print("The word was: %s" % " ".join(blankArray))
        sys.exit()
    else:
        for i in range(0, len(list(randomWord))):
            if randomWord[i] == "_":
                break
            else:
                startup("")

startup("initial")

