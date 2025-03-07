# A pangram is a sentence that contains every letter of the alphabet at least once
#eg : "The quick brown fox jumps over the lazy dog."

import string

def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    sentence_letters = set(sentence.lower())  # Convert to lowercase and store unique letters
    return alphabet.issubset(sentence_letters)


# Example Usage
sentence = input("Enter a sentence: ")
if is_pangram(sentence):
    print("The sentence is a pangram.")
else:
    print("The sentence is NOT a pangram.")
