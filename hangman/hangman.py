import random
from words import words
import string

def hangman():
    animal = random.choice(words)
    animal_letters = set(animal)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()


# THIS IS SHIT!