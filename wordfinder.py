"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Class to pull words from a file and choose a random word.
    
    >>> wordfinder = WordFinder("./words.txt")

    >>> wordfinder.random()

    """

    def __init__(self, filename):
        "Creates WordFinder list from words in file and prints numbers of words read"
        with open(filename) as f:
            self.content = f.readlines()

        print(f"{len(self.content)} words read")

    def random (self):
        "Picks and prints a random word"
        word = random.choice(self.content)
        print (word.rstrip())

class SpecialWordFinder(WordFinder):
    """Special Word Finder that doesn't include blank lines or commented out lines"""

    def __init__(self, filename):
        super().__init__(filename)

    def get_words (self): 
        return [word.strip() for word in self.content if word.strip() and not word.startswith("#")]