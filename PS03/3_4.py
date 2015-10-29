lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
      
      it starts with all the letters of the alphabet as list.
      
    it then loops through for each element in lettersguessed and removes it from 
    the possible selections that can be made
    
    it then returns the alphabet list as a string
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for element in lettersGuessed:
        alphabet.remove(element)
        
    letterRemaining = ''
    for each in alphabet:
        letterRemaining += each

    return letterRemaining
print getAvailableLetters(lettersGuessed)
