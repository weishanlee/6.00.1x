secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
      
    This code starts by converting the secret word to a list
    then for each of the letters in the lettersGuessed it looks to see if it
    appears in the list secret
    if that letter appears, every instance is removed. 
    Once all letters are checked then an if statement checks the length of the 
    secret list. If that length is 0 then it has been guessed and the fuction 
    returns true, otherwise it returns false
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
    
        

print isWordGuessed(secretWord, lettersGuessed)      

