# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "/Users/andrewmarmion/Google Drive/Python/6.00.1x/PS05/words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShift(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("/Users/andrewmarmion/Google Drive/Python/6.00.1x/PS05/story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    alphabet_shifted = {}
    # makes a list of uppercase letters shifted by a specific value
    upper_alphabet = string.ascii_uppercase
    upper_shifted = upper_alphabet
    letter_up = upper_shifted[0:shift]
    upper_shifted += letter_up
    upper_shifted = upper_shifted[shift:]

    #makes a list of lowercase letters shifted by a specific value
    lower_alphabet = string.ascii_lowercase
    lower_shifted = lower_alphabet
    letter_low = lower_shifted[0:shift]
    lower_shifted += letter_low
    lower_shifted = lower_shifted[shift:]

    # creates a dictionary of the original alphabet mapped to the shifted alphabet
    for lower_value, shifted_value in zip(lower_alphabet, lower_shifted):
        alphabet_shifted[lower_value] = shifted_value
    
    for upper_value, shifted_value in zip(upper_alphabet, upper_shifted):
        alphabet_shifted[upper_value] = shifted_value 
    
    
    return alphabet_shifted

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    
    This takes each character in the text, if it is in the coder then it is stored in a string encoded
    If the value is not in the coder then it is just stored in the string as it is. 
    """
    encoded_text = ''
    for char in text:
        if char in coder:
            encoded_text += coder.values()[coder.keys().index(char)]
        else:
            encoded_text += char
                
    return encoded_text

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    
    This is a wrapper function that contains the functions buildCoder and applyCoder
    The returns the text after it has been shift.
    """
    coder = buildCoder(shift)
    encoded_text = applyCoder(text, coder)
    
    return encoded_text 

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    real_words_max = 0                              # stores the value for the maximum number of real words found
    best_shift = 0                                  # stores the value for the best shift 

    for i in range(0,26):
        count = 0                                   # stores the number of words found to compate with real_words_max
        shifted_word = applyShift(text, i)          # shifts the text i places
        split_word = shifted_word.split(' ')        # splits the text into a list of words
        for word in split_word:                     # for each word in the list see if it is a real word, if it is increase the count by one
            if isWord(wordList, word): 
                 count += 1
        if count > real_words_max:                  # check to see if we have found the biggest number of real words
            real_words_max = count                  # if we have then set the real_words_max to count and the best_shift to i
            best_shift = i 
    
    return best_shift          
        
        


def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    wordList = loadWords()                      # loads the word list
    story = getStoryString()                    # loads the story to unencode
    shift = findBestShift(wordList, story)      # finds the best shift
    unencoded_text = applyShift(story, shift)   # finds the unencoded text
    
    return unencoded_text

#
# Build data structures used for entire session and run encryption
#





if __name__ == '__main__':
    # To test findBestShift:
    #wordList = loadWords()
    #s = applyShift('Hello, world!', 8)
    #bestShift = findBestShift(wordList, s)
    #assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    print decryptStory()

