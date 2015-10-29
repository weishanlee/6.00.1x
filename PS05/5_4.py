'''
=========================
Problem 2: findBestShifts
=========================

1. Set the maximum number of real words found to 0.
2. Set the best shift to 0.
3. For each possible shift from 0 to 26:
	4. Shift the entire text by this shift.
	5. Split the text up into a list of the individual words.
	6. Count the number of valid words in this list.
	7. If this number of valid words is more than the largest number of
	   real words found, then:
		8. Record the number of valid words.
		9. Set the best shift to the current shift.
	10. Increment the current possible shift by 1. Repeat the loop
	   starting at line 3.
11. Return the best shift.
'''
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
        

    