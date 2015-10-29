# 6.00x Problem Set 6
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    if aStr == "":
        return aStr
    else:
        return reverseString(aStr[1:]) + aStr[0]
    
    
#
# Problem 4: X-ian
#
def x_ian(name, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if len(name) >= 0:
        if len(name) == 0:
            return True
        elif name[0] in word:
            return x_ian(name[1:], word)         
        else: 
            return False
     
#print x_ian('john', 'cerium')

#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately.
    
    Very similar to problem 3 above. Having completed problem 3 it made this problem much easier.
    """
    if len(text) < lineLength:
        return text
    
    return str(text[:lineLength]) + "\n" +str(insertNewlines(text[lineLength:],lineLength ))

    
text = "Jack Florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack. He has been registered for classes at MIT twice before, but has reportedly never passed a class. It has been the tradition of the residents of East Campus to become Jack Florey for a few nights each year to educate incoming students in the ways, means, and ethics of hacking."
                
print insertNewlines(text, 40)
