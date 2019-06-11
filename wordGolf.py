import random
from nltk.corpus import words

wordList = words.words()
wordSet = set(wordList) # use sets for membership lookup
threeLetter = []
fourLetter = []
fiveLetter = []
sixLetter = []

for word in wordSet:
    if len(word) == 3:
        threeLetter.append(word)
    if len(word) == 4:
        fourLetter.append(word)
    if len(word) == 5:
        fiveLetter.append(word)
    if len(word) == 6:
        sixLetter.append(word)

def wordLookup(word):
    if word in wordSet:
        return True
    else:
        return False

def gameLoop(startingWord, endingWord, wordSize):
    print("Current Word: " + startingWord + " Ending Word: " + endingWord)
    nextWord = input("Next Word: ")
    # TODO: check if the nextWord is valid, assuming it is
    if nextWord == endingWord:
        print("wow, great job!")
    else:
        gameLoop(nextWord, endingWord, wordSize)

def setUp():
    wordSize = int(input("Word Size: "))
    if wordSize == 3:
        startingWord = random.choice(threeLetter)
        endingWord = random.choice(threeLetter)
    if wordSize == 4:
        startingWord = random.choice(fourLetter)
        endingWord = random.choice(fourLetter)
    if wordSize == 5:
        startingWord = random.choice(fiveLetter)
        endingWord = random.choice(fiveLetter)
    if wordSize == 6:
        startingWord = random.choice(sixLetter)
        endingWord = random.choice(sixLetter)

    gameLoop(startingWord, endingWord, wordSize)

setUp()
