
def getSublists(L, n):
    '''
    L, list     a non-empty list
    n, int      the number of elements in the sublist
    
    returns a list of sublists of length n
    '''
    new_list = []
    max_length = len(L) - n + 1
    for i in range(0, max_length):
        short_list = []
        for j in range(0,n):
            short_list.append(L[i+j])
        new_list.append(short_list)
    return new_list
            
L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]

#print getSublists(L, 4)

L = [1, 1, 1, 1, 4]

#print getSublists(L, 2)


def longestRun(L):
    '''
    L, list     a non-empty list
    
    returns the length of a list of monotonically increasing integers
    '''
    saved = []
    max_len = len(L) -1
    longest = 0
    if len(L) == 1:
        return len(L)
    for i in range(max_len):
        if len(saved) == 0:
            saved.append(L[i])
        if L[i+1] >= L[i]:
            saved.append(L[i+1])
        if len(saved) > longest:
                longest = len(saved)
        elif L[i+1] < L[i] or i == max_len-1:
            saved = []
   
    return longest

L = [0]
print longestRun(L)
L = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print longestRun(L)
L = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
print longestRun(L)
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print longestRun(L)