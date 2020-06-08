import sys
import scrabble


def valid_word(word, rack):
    # make a copy of the rack for every new workd, so we can manipulate it
    # with compromising the original rack.
    avaialable_letters = rack[:]
    for letter in word:
        if letter not in avaialable_letters:
            return False
        avaialable_letters.remove(letter)
    return True


def compute_score(word):
    # Calculate the Scrabble score for the word.
    score = 0
    for letter in word:
        score = score + scrabble.scores[letter]
    return score


if len(sys.argv) < 2:
    print("Usage: scrabble.py [RACK]")
    exit(1)

rack = list(sys.argv[1].lower())
valid_words = []

for word in scrabble.wordlist:
    if valid_word(word, rack):
        score = compute_score(word)
        valid_words.append([score, word])

valid_words.sort()
for play in valid_words:
    score = play[0]
    word = play[1]
    print(word + ": " + str(score))
