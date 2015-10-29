'''
def isVowel(char):
    char = char.lower()
    print char
    
    if char in 'aeiou':
        True
    else:
        False
test = raw_input('type a letter: ')
isVowel(test)
'''
def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    char = char.lower()
    #print char
    
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        return True
    else:
        return False