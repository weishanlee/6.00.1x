import string
    
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




if buildCoder(9) == {'A': 'J', 'C': 'L', 'B': 'K', 'E': 'N', 'D': 'M', 'G': 'P', 'F': 'O', 'I': 'R', 'H': 'Q', 'K': 'T', 'J': 'S', 'M': 'V', 'L': 'U', 'O': 'X', 'N': 'W', 'Q': 'Z', 'P': 'Y', 'S': 'B', 'R': 'A', 'U': 'D', 'T': 'C', 'W': 'F', 'V': 'E', 'Y': 'H', 'X': 'G', 'Z': 'I', 'a': 'j', 'c': 'l', 'b': 'k', 'e': 'n', 'd': 'm', 'g': 'p', 'f': 'o', 'i': 'r', 'h': 'q', 'k': 't', 'j': 's', 'm': 'v', 'l': 'u', 'o': 'x', 'n': 'w', 'q': 'z', 'p': 'y', 's': 'b', 'r': 'a', 'u': 'd', 't': 'c', 'w': 'f', 'v': 'e', 'y': 'h', 'x': 'g', 'z': 'i'}:
    print True