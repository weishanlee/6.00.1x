def f(s):
    return 'a' in s
      
L = ['c', 'b', 'c']


def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    # create a copy of the list so the we can use it to iterate across the  list without problems from mutation
    L_copy = L[:]
    for c in L_copy:
        if not f(c):
            L.remove(c)
    return len(L)
    
    
print satisfiesF(L)
print L

#run_satisfiesF(L, satisfiesF)

