import random
import string
programming_language = ["PYTHON", "JAVA", "GO", "CPP", "C", "JAVASCRIPT", "ASSEMBLY", "PHP"]

def select_random_language(programming_language):
    chosen_elm = random.choice(programming_language)
    word_display = ["_" for i in chosen_elm]
    lives = 6


    while "_" in word_display and lives > 0:
        print("\n" + ' '.join(word_display))
        user_input = input("\n\n\nGuess The Letter: ")
        if validation(user_input):
            if user_input in chosen_elm:
                for idx, i in enumerate(chosen_elm):
                    if user_input == i:
                        word_display[idx] = user_input
            else:
                lives -= 1
                print(f"\n {user_input} ist't in the word anymore")

    if lives == 0:
        print(f"You lost all your lives the word was: {chosen_elm}")



    print("congratualtion you won")



def validation(guess):
    all_alphabet = set(string.ascii_uppercase)
    return guess in all_alphabet



def main():
    print("Welcome to our guessing game try to guess the word")
    select_random_language(programming_language)
    print("Good bye")
    


if __name__=='__main__':
    main()
    
