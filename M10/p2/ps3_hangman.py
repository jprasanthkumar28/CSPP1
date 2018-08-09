'''Hangman game'''
import string
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadwords():
    '''Hangman game'''
    print("Loading word list from file...")
    # inFile: file
    infile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = infile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseword(wordlist):
    '''Hangman game'''
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadwords()

def iswordguessed(secretword, lettersguessed):
    '''Hangman game'''
    # FILL IN YOUR CODE HERE...
    _ = 0
    for index in secretword:
        if index in lettersguessed:
            _ += 1
    if len(secretword) == _:
        return True
    return False

def getguessedword(secretword, lettersguessed):
    '''Hangman game'''
    # FILL IN YOUR CODE HERE...
    result = ''
    for index in secretword:
        if index in lettersguessed:
            result += index
        else:
            result += '_'
    return result


def getavailableletters(lettersguessed):
    '''Hangman game'''
    values = string.ascii_lowercase
    result = ''
    for index in values:
        if index in lettersguessed:
            continue
        else:
            result += index
    return result

def testinput(guess):
    '''Hangman game'''
    if len(guess) > 1 or (guess <= 'a' and guess >= 'z'):
        print("Invalid Input...")
        return False
    return True

    #lettersGuessed.append(guess)

def hangman(secretword):
    '''Hangman game'''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game Hangman")
    lettersguessed = []
    print("Iam thinking of a word which is ", len(secretword), "Letters word")
    print("------------------------------")
    flag = False
    maxguessletters = len(secretword) + 5
    print(getguessedword(secretword, lettersguessed))
    while maxguessletters != 0:
        print("You have", maxguessletters, "Left")
        print("Available letters: ", getavailableletters(lettersguessed))
        guess = input("Please guess a letter: ")
        maxguessletters -= 1

        if not testinput(guess):
            continue
        lettersguessed.append(guess)
        flag = iswordguessed(secretword, lettersguessed)
        if flag:
            break
        print(getguessedword(secretword, lettersguessed))
    if flag:
        print("Congratulations you guessed the correct word")
    else:
        print("Try again....")

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()
#hangman(secretWord)
def main():
    '''Hangman-Game'''
    secretword = chooseword(wordlist).lower()
    hangman(secretword)
if __name__ == "__main__":
    main()
