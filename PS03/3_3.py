secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
      
      It starts by converying the secretword to a list and by creating an empty
      list with underscores for the word that they are trying to find.
      
      Then it loops through for each element in the lettersGuessed list looking to see
      if it is in each of the positions of the secret list. 
      
      each time it finds a letter that is in both it updates the guess with the letter
      in the correct position
      
      it then returns the clue with spaces between each letter to make it more readabile. 
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
print getGuessedWord(secretWord, lettersGuessed)