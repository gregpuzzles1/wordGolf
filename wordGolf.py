import random
from nltk.corpus import words
from typing import List

# Load dictionary
word_list = words.words()
word_set = set(word_list)  # Use sets for fast lookup

# Categorize words by length
word_buckets = {
    3: [],
    4: [],
    5: [],
    6: []
}

for word in word_set:
    word_len = len(word)
    if word_len in word_buckets:
        word_buckets[word_len].append(word.lower())

# Track the path through the word ladder
path: List[str] = []


def levenshtein_subs(w1: str, w2: str) -> int:
    """Calculate Levenshtein distance using substitutions only."""
    return sum(c1 != c2 for c1, c2 in zip(w1, w2))


def is_valid_word(word: str) -> bool:
    return word in word_set


def is_valid_step(current: str, next_word: str) -> bool:
    return (
        is_valid_word(next_word) and
        len(current) == len(next_word) and
        levenshtein_subs(current, next_word) == 1
    )


def game_loop(current_word: str, target_word: str):
    print(f"Current Word: {current_word} → Target Word: {target_word}")
    next_word = input("Next Word: ").strip().lower()

    if is_valid_step(current_word, next_word):
        path.append(next_word)
        if next_word == target_word:
            print("\n🏁 Success! You reached the target word.")
            print("🛤️  Path taken:", " → ".join(path))
        else:
            game_loop(next_word, target_word)
    else:
        print("❌ Invalid word. Try again.\n")
        game_loop(current_word, target_word)


def setup_game():
    try:
        word_size = int(input("Enter word length (3-6): ").strip())
        if word_size not in word_buckets:
            raise ValueError

        start = random.choice(word_buckets[word_size])
        end = random.choice(word_buckets[word_size])
        while end == start:
            end = random.choice(word_buckets[word_size])

        path.clear()
        path.append(start)
        game_loop(start, end)
    except ValueError:
        print("❌ Please enter a valid number between 3 and 6.")
        setup_game()


if __name__ == "__main__":
    setup_game()
