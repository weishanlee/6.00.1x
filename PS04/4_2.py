hand = {'a':1, 'p':2, 'l':1, 'e':1, 's':1, 'x':1}
#print sum(hand.values())
word = "apple"

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    handCopy = hand.copy()
    for c in word:
        handCopy[c] = handCopy.setdefault(c, 0) - 1
    return handCopy
    
print updateHand(hand, word)
