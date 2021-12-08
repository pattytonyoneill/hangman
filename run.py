import os
from os import system, name
import random
from words import words
from visual_hangman import lives_dict
import string

# letters guessed by user
used_letters = set()
# have input of user changed to uppercase for better readablility
alphabet = set(string.ascii_uppercase)
lives = 0


def clear():
    """
    Simple clear function that will clear the terminal.
    This is to avoid clogging-up the screen.
    """
    os.system("cls" if os.name == "nt" else "clear")


def get_word(words):
    """
    Get valid words from my list of word
    """
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    """
    The hangman game
    """
    global lives
    global word
    clear()
    word = get_word(words)
    # letters in the word
    word_letters = set(word)
    lives = 9
    print('Welcome to Hangman!')
    print('You have 9 lives. Please choose a letter.')
    print('If wrong loose a life and see the hangman go up.')
    print('Good Luck!')
    print(' ')



    # user input
    while len(word_letters) > 0 and lives > 0:
        # Tell user the lives left and the letters that were used
        print(
            'You have', lives, 'lives left and you have used these letters: ',
            ' '.join(used_letters))

        # Current word
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print(lives_dict[lives])
        print('Current word: ', ' '.join(word_list))
        handle_input(word_letters)
        print(len(word_letters))
    update_game()


def handle_input(word_letters):
    """
    Handle User input
    """
    # User Guesses
    print(word)
    global alphabet
    global used_words
    global lives
    user_letter = input('Please, guess only one letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            clear()
            word_letters.remove(user_letter)
            print('')

        else:
            # Removes a life if wrong
            lives = lives - 1
            clear()
            print(
                '\nSorry, that letter,', user_letter,
                'is not in the word.')

    elif user_letter in used_letters:
        clear()
        print(
            '\nSorry, you already used that letter. Please guess again.'
            'Please guess another letter.')

    else:
        clear()
        print('\nSorry, that is not a valid letter.  Please guess again!')
    

def update_game():
    """
    Update game information if solved or lost
    """
    global lives
    global word
    # Here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_dict[lives])
        print('You died, sorry. The correct word was', word)
        print("\U0001F571")
    else:
        print('Yahoo! You guessed correctly', word, '!!')
        print("\U0001f44D")
    play_again()

def play_again():
    """Play Hangman game again or end game"""
    user_play_again = input('Do you want to play again? (Y/N) ').upper()
    if user_play_again == 'Y':
        reset_game()
        hangman()

    else:
        clear()
        print('Thanks for playing hangman!')


def reset_game():
    """
    Reset Hangman Game after done a game
    """
    used_letters.clear()
    lives = 0

if __name__ == '__main__':
    hangman()
