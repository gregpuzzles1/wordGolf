from nltk.corpus import words

wordList = words.words()
wordSet = set(wordList) # use sets for membership lookup

def wordLookup(word):
    if word in wordSet:
        return True
    else:
        return False

print(wordLookup("chronicalizing"))
