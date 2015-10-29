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


def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    encoded_text = ''
    for char in text:
        if char in coder:
            encoded_text += coder.values()[coder.keys().index(char)]
        else:
            encoded_text += char
                
    return encoded_text
    
coder = buildCoder(8)
text = "Hello, world!"
    
print applyCoder(text, coder)
print applyCoder('Pmttw, ewztl!', buildCoder(18))    

