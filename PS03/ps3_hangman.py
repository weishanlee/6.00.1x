# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/Users/andrewmarmion/Google Drive/Python/6.00.1x/PS03/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

 

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
 
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    secret = list(secretWord)
    for element in lettersGuessed:
        while element in secret:
            secret.remove(element)
    if len(secret) == 0:
        return True
    else:
        return False 


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    secret = list(secretWord)
    guess = []

    for letter in secret:
        guess.append('_')
    
    for element in lettersGuessed:
        n = 0
        while n < len(secret):
            if element == secret[n]:
                guess[n] = element
            n += 1
    
    clue = '' 
    for each in guess:
        clue += each
        clue += ' '
    return clue 


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for element in lettersGuessed:
        if element in alphabet:
            alphabet.remove(element)
        
    letterRemaining = ''
    for each in alphabet:
        letterRemaining += each

    return letterRemaining    

    
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word " + str(len(secretWord)) + " letters long."
    print "-------------"
    n = 8 
    lettersGuessed =[]
    while True:
        print "You have " + str(n) + " guesses left."
        print "Available Letters: " + str(getAvailableLetters(lettersGuessed)); guess = raw_input("Please guess a letter: ")
        guess = guess.lower()
        if guess in lettersGuessed:
            print "Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed))
            print "-----------"
        else:
            lettersGuessed.append(guess)    
            #print lettersGuessed 
        
            if guess in list(secretWord):
                print "Good guess: " + str(getGuessedWord(secretWord, lettersGuessed))
                print "-----------"
            else:
                n -= 1
                print "Oops! That letter is not in my word: " + str(getGuessedWord(secretWord, lettersGuessed))
                print "-----------"
            if n == 0:
                print "Sorry, you ran out of guesses. The word was " + str(secretWord) +"."
                break
        
        if isWordGuessed(secretWord, lettersGuessed):
            print "Congratulations, you won!"
            break
    





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
#secretWord = 'zzz'
hangman(secretWord)
