import random
from words import words

"""
Get a valid word
"""
def get_valid_word(words):
    """ 
    Randomly choose a word
    """
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.uppercase()

def hangman():
    word=get_valid_word(words)
    """ 
    letters in the word
    """
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    """ 
    letters guessed by user
    """
    guessed_letters = set()  
    
