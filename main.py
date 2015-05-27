import random
import sys
import os

dictionary = ["PIZZA", "PANCAKES", "GOLF","JASPER","ISAAC","SCOTT"] #Add words here, make sure they're all caps
randomWord = dictionary[random.randrange(0, len(dictionary))]
usedArray = []
global lives
lives = 0

blankArray = []

def cls():
    clear = "\n" * 100
    print(clear)

def startup(time, incorrect):
    cls()
    if time == "initial":
        for i in range(1, len(randomWord) + 1):
            blankArray.append("_")
        amountOfLives = input("Amount of lives: ")
        cls()
        global lives
        lives = amountOfLives
    else:
        if incorrect:
            print(lives)
            print("Incorrect!")
            lives = lives - 1
            if lives == 0:
                cls()
                print("Game Over! You ran out of lives!")
                sys.exit()
        used = " ".join(usedArray)
        print("You have " + lives.__str__() + " live(s) left")
        print("You have used: %s" % used)
        print(" ".join(blankArray))
    typeOfGuess = raw_input("Letter | Word ")
    if typeOfGuess == "Letter" or typeOfGuess == "letter":
        letterToGuess = raw_input("Pick one letter: ").upper()
        guessLetter(letterToGuess)
    if typeOfGuess == "Word" or typeOfGuess == "word":
        wordToGuess = raw_input("Type a word: ").upper()
        guessWord(wordToGuess)

def guessLetter(letter):
    global letterExists
    letterExists = False
    for i in range(0, len(list(randomWord))):
        if letter == randomWord[i]:
		    #Replacing the blanks with letters
            blankArray[i] = letter
            letterExists = True
    usedArray.append(letter)
    if randomWord == "".join(blankArray):
		#When the user wins
        cls()
        print("You Win!")
        print("The word was: %s" % " ".join(blankArray))
        sys.exit()
    else:
        for i in range(0, len(list(randomWord))):
            if randomWord[i] == "_":
                break
            else:
                if letterExists:
                    startup("", False)
                else:
                    startup("", True)

def guessWord(word):
    if word == randomWord:
        winWord = " ".join(list(randomWord.upper()))
        cls()
        print("You Win!")
        print("The word was: " + winWord)
        sys.exit()
    else:
        print("%s is not the word!" % word)
        startup("", True)

startup("initial", False)

