import os
from os import system, name
import random
from words import words
from hangman_visual import lives_visual_dict
import string


def clear():
    """
    Simple clear function that will clear the terminal.
    This is to avoid clogging-up the screen.
    """
    os.system("cls" if os.name == "nt" else "clear")


def get_valid_word(words):
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
    clear()
    word = get_valid_word(words)
    # letters in the word
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    # letters guessed by user
    used_letters = set()
    lives = 7
    print('Welcome to Hangman!')
    print('You have 7 lives. Please choose a letter.')
    print('If wrong loose a life and see the hangman go up.')
    print('Good Luck!')
    print(' ')

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # Tell user the lives lefft and the letters that were used
        print(
            'You have', lives, 'lives left and you have used these letters: ',
            ' '.join(used_letters))

        # Current word
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        # User Guesses
        print(word)
        user_letter = input('Guess a letter: ').upper()
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
                    '\nSorry, your letter,', user_letter,
                    'is not in the word.')

        elif user_letter in used_letters:
            clear()
            print(
                '\nSorry, you have already used that letter. '
                'Please guess another letter.')

        else:
            clear()
            print('\nSorry, that is not a valid letter.')

    # Get here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
        print("\U0001F571")
    else:
        print('Yahoo! You guessed the word', word, '!!')
        print("\U0001F923")
    play_again()


def play_again():
    """Play Hangman game again """
    user_play_again = input('Do you want to play again? (Y/N) ').upper()
    if user_play_again == 'Y':
        hangman()
    else:
        clear()
        print('Thanks for playing hangman!')


if __name__ == '__main__':
    hangman()
