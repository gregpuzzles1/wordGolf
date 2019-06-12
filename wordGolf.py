import random
from nltk.corpus import words

wordList = words.words()
wordSet = set(wordList) # use sets for membership lookup
threeLetter = []
fourLetter = []
fiveLetter = []
sixLetter = []

path = []

for word in wordSet:
    if len(word) == 3:
        threeLetter.append(word)
    if len(word) == 4:
        fourLetter.append(word)
    if len(word) == 5:
        fiveLetter.append(word)
    if len(word) == 6:
        sixLetter.append(word)

def levenshteinSubs(w1, w2):
    # length of w1 will always equal w2
    previous_row = range(len(w2) + 1)

    for i, c1 in enumerate(w1):
        current_row = [i + 1]
        for j, c2 in enumerate(w2):
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(substitutions)
        previous_row = current_row

    return previous_row[-1]

def wordLookup(word):
    if word in wordSet:
        return True
    else:
        return False

def verifyWord(nextWord, startingWord):
    # verify that nextWord is a word & that nextWord is one step away from startingWord (Levenshtein Dist. with only subs)
    if(wordLookup(nextWord) == True and levenshteinSubs(nextWord, startingWord) == 1):
        return True
    else:
        return False


def gameLoop(startingWord, endingWord):
    print("Current Word: " + startingWord + " Ending Word: " + endingWord)
    nextWord = input("Next Word: ")
    if verifyWord(nextWord, startingWord):
        path.append(nextWord)
        if nextWord == endingWord:
            print("wow, great job!")
            print("Path: " + str(path))
        else:
            gameLoop(nextWord, endingWord)
    else:
        print("Invalid word, try again.")
        gameLoop(startingWord, endingWord)


def setUp():
    wordSize = int(input("Word Size: "))
    if wordSize == 3:
        startingWord = random.choice(threeLetter).lower()
        path.append(startingWord)
        endingWord = random.choice(threeLetter).lower()
    if wordSize == 4:
        startingWord = random.choice(fourLetter).lower()
        path.append(startingWord)
        endingWord = random.choice(fourLetter).lower()
    if wordSize == 5:
        startingWord = random.choice(fiveLetter).lower()
        path.append(startingWord)
        endingWord = random.choice(fiveLetter).lower()
    if wordSize == 6:
        startingWord = random.choice(sixLetter).lower()
        path.append(startingWord)
        endingWord = random.choice(sixLetter).lower()

    gameLoop(startingWord, endingWord)

setUp()
