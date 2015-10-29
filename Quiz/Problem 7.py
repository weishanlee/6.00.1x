'''
Write a Python function that returns a list of keys in aDict that map to integer values 
that are unique (i.e. values appear exactly once in aDict). 
The list of keys you return should be sorted in increasing order. 
(If aDict does not contain any unique values, you should return an empty list.)

This function takes in a dictionary and returns a list.
'''

a = {'a':1, 'b':1, 'c':2, 'd':3, 'e':4}

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # This removes all the dictionary values that are the same. Stores the remaining keys and values in a dictionary
    nondups = {k:v for k,v in aDict.items() if aDict.values().count(v)==1}
    # takes each key and stores it in a list called dict_list
    dict_list = []
    for key in nondups:
        if key not in dict_list:
            dict_list.append(key)
    dict_list.sort()
    return dict_list
    
print uniqueValues(a)

# an even faster way of solving the problem. 
# change the nondups so that it is a set instead of a dictionary
# 

def unique2(aDict):
    '''
    Create a set called nondups to hold all the non-duplicate values
    Store the key in the list nondups, For each key and value, if that value only appears once, 
    '''
    nondups = [k for k,v in aDict.items() if aDict.values().count(v)==1]
    # don't forget to sort the list
    nondups.sort()
    # returns the sorted list 
    return nondups
    
print unique2(a)
