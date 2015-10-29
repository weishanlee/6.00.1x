
count = 0
def count7(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    global count
    if N <= 0:
        answer = count
        count = 0
        return answer
    else: 
        check = N % 10
        N /= 10
        if check  == 7:
            count += 1
    return count7(N)
            
print count7(717)            
print count7(1237123)         
      