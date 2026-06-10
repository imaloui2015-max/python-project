

import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    all_alphabet = set(string.ascii_uppercase)
    used_letters = set()


    lives = 10

    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]

        print(f" Current word: ", ' '.join(word_list))

        user_let = input('Guess the letter: ').upper()

        if user_let in all_alphabet - used_letters:
            used_letters.add(user_let)
            if user_let in word_letters:
                word_letters.remove(user_let)
                print('')

            else:
                lives -= 1
                print('\nYour Letter', user_let, 'is not in word anymore')

            
        elif user_let in used_letters:
            print("You Already used This Letter")

        else:
            print(f"{user_let} isn't a valid letter")

    
    if lives == 0:
        print('You have', lives , 'lives and the word was', word )

    else:
        print('Wooow!! you gussed the right word' , word, 'that s amazing your so smart.')


if __name__ == '__main__':
    hangman()