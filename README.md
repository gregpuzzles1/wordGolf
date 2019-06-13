# wordGolf
Python implementation of Word Golf (aka Word Ladder), described by Lewis Carroll as "a puzzle that begins with two words, and to solve the puzzle one must find a chain of other words to link the two, in which two adjacent words (that is, words in successive steps) differ by one letter."

Utilized the NLTK to generate words, and a modified Levenshtein distance to verify that each success word is one step away.

Example:

COLD → CORD → CARD → WARD → WARM

Requires NLTK Corpus
