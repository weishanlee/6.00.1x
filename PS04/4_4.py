hand = {'a':1, 'p':2, 'l':0, 'e':1, 's':1, 'x':1}

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    return sum(hand.values())
    
print calculateHandlen(hand)
