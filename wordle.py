import string
import random
import urllib.request
import random

green = '\u001b[32m'
yellow = '\x1B[33m'
end_color = '\x1B[0m'

def load_words():
    '''
    return: list of valid words; words are strings of lowercase letters and are 5 letters in length. 
    '''

    URL = 'https://gist.githubusercontent.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b/raw/5d752e5f0702da315298a6bb5a771586d6ff445c/wordle-answers-alphabetical.txt'


    with urllib.request.urlopen(URL) as response:
        word_list = response.read().splitlines()

    return word_list

def choose_word(word_list):
    '''
    word_list: list of words (strings)
    return: a string, a random word from word_list
    '''
    return random.choice(word_list).decode('utf-8')

def display_guess(guess, word, available_letters):
    '''
    guess: string, the word the user guesses
    word: string, the correct word
    available_letters: string, all unused letters
    return: the guessed word. correctly placed letters will be green, correct letters in the wrong place are yellow, incorrect letters are gray. 
    '''

    guess_display = ''
    for index, letter in enumerate(guess):
        if guess[index] == word[index]:
            guess_display += f"{green}{letter}{end_color}"
        elif letter in word:
            guess_display += f"{yellow}{letter}{end_color}"
        else:
            guess_display += letter
            if letter in available_letters:
                available_letters.remove(letter)
    return guess_display

word_list = load_words()
word = choose_word(word_list)
# print(word_list)
    
def wordle(word):
    '''
    word: string 5 letters in length. randomly chosen from a list of words.
    count: number, the number of guesses you have to get the word correctly. 
    avialable_letters: list, all of the letters in the alphabet that have not been guessed yet.

    '''

    count = 6
    available_letters = list(string.ascii_lowercase)

    while count > 0:
        guess = input('Guess a 5 letter word ').strip()

        if len(guess) != 5:
            print('Word must be 5 letters in length. Try again ')
            continue

        print(f'\n{display_guess(guess, word, available_letters)}\n')
        if guess == word:
            print("Correct!")
            return
        count-= 1
        print(f'''Remaining available letters:\n {' '.join(available_letters)}''')
        print(f'You have {count} guesses left. \n')

    print(f'Out of guesses. The correct answer was {word}')


wordle(word)

# print(word_list)
