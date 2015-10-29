# create random letter lists to test PS1
import random
import string



def test(tests,a,b):
    '''
    tests: int, the number of tests to perform
    a:     int, the length of the shortest string allowed
    b:     int, the length of the maximum string allowed
    '''
    n = 0
    while n < tests:
        s = generate_string(a,b)
        word = longest_string(s)
        print s
        print 'Longest substring in alphabetical order is: ' + str(word)
        n += 1
    return
    

def generate_string(a,b):
    '''
    total:        int, the maximum number of letters in the string
    new_string:    string, will hold the new string for testing
    n:            int:      
    '''
    new_string = ''
    n = 0
    total = random.randrange(a,b)
    #print 'the total number of letters are: ' + str(total)
    if total == 26:
        new_string = 'abcdefghijklmnopqrstuvwxyz'
    elif total == 5:
        new_string = 'zyxwvutsrqponmlkjihgfedcba'
    else:
        while n < total:
            letter = random.choice(string.letters)
            new_string += letter
            n += 1
    #print new_string.lower()
    return new_string.lower()
    

def longest_string(s):
    '''
    current longest:    string
    testing:            char
    the_longest:        string
    '''
    n = 0
    current_longest = ''
    testing = s[n]
    the_longest = s[n]
    while n < len(s) - 1:
    
        if s[n] <= s[n+1]:      
            testing += s[n+1]
            #print testing
               
        elif s[n] > s[n+1]:
        
            #print 'current: ' + str(current_longest)
            #print 'longest: ' + str(the_longest)
            if len(current_longest) > len(the_longest):
                the_longest = current_longest
    
            current_longest = testing
            testing = s[n+1]
    
        if len(testing) > len(the_longest):
                the_longest = testing
            
        n += 1
    #print 'Longest substring in alphabetical order is: ' + str(the_longest)
    return the_longest
test(5,5,26)
