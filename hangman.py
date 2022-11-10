import string
from words import words
import random

def get_valid_word(words):
    word = random.choice(words) #Get a random word from list
    while '-' in word or '' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letter in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user guessed

    lives = 6

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        print('You have',lives,'lives left','You have used these letters: ',' '.join(used_letters))
        print('Current word: ', ''.join(word_list))

        #what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives = lives - 1
                print('Letter is not in word')
        elif user_letter in used_letters:
            print('You have already used that Character. Please Try Again')
    
        else:
            print('Invalid Character, Please Try Again')
    if lives == 0:
        print("Oops, you died, The word was", word)
    else:
        print('You guessed the word',word,'')


hangman()
