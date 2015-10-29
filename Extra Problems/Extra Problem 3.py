def nfruits(x, y):
    '''
    x, dictionary   A dictionary containing type of fruit and its quantity initially with Python when he leaves home
    y, string       A string pattern of the fruits eaten by Python on his journey as observed by Cobra.
    
    Returns the maximum of the quantities of the fruits. 
    '''
    list_of_keys = x.keys()                                     # makes a list of the key
    count = 0
    while count < len(y):
        x[y[count]] = x.setdefault(y[count], 0) - 1             # Python eats the fruit, reduces the fruit in x by one                
        if count < len(y) - 1:                                  # we only add fruit len(y)-1 times
            list_of_keys_copy = list_of_keys[:]                 # makes a copy of the list_of_keys so we don't mutate it
            list_of_keys_copy.remove(y[count])                  # removes the value of the fruit from the list_of_keys so that we can select the new fruit
            for c in list_of_keys_copy: 
                x[c] = x.setdefault(c, 0) + 1                   # adds the fruit to x, all the remaining fruits go up by one
        count += 1
    return x[max(x, key=x.get)]                                 # returns the maximum of the quantities of the fruits. 
    
print nfruits({'A': 1, 'B': 2, 'C': 3}, 'AC')
print nfruits({'A': 5, 'B': 7, 'C': 8, 'D': 11, 'E': 4}, 'AAABBBEECAAABBAACCAADDBBAACDCAAABBBAEACCAEADABCB')
