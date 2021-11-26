import random
from words import words
from hangman_visual import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    """letters in the word"""
    word_letters = set(word)  
    alphabet = set(string.ascii_uppercase)
    """letters guessed by user"""
    used_letters = set()  
    lives = 7

    """getting user input"""
    while len(word_letters) > 0 and lives > 0:
        """Tell user the lives lefft and the letters that were used"""
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        """Current word"""
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        """User Guesses"""
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                """Removes a life if wrong"""
                lives = lives - 1  
                print('\nSorry, your letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nSorry, you have already used that letter. Please guess another letter.')

        else:
            print('\nSorry, that is not a valid letter.')

   """ Get here when len(word_letters) == 0 OR when lives == 0"""
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('Yahoo! You guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()