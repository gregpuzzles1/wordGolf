import nltk
from nltk.corpus import words
from collections import deque

nltk.download("words")

word_list = set(word.lower() for word in words.words() if len(word) == 4)


def one_letter_words(word, word_set):
    return {
        word[:i] + c + word[i + 1 :]
        for i in range(len(word))
        for c in "abcdefghijklmnopqrstuvwxyz"
        if c != word[i] and (word[:i] + c + word[i + 1 :]) in word_set
    }


# Get all words one letter away from 'ngai'
neighbors = one_letter_words("ngai", word_list)
print("Valid one-letter transformations from 'ngai':", neighbors)
