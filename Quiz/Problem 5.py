from math import sqrt

def primesList(N):
    '''
    N: an integer
    '''
    N = N + 1
    sieve = [True] * (N / 2)  # Half Sieve

    for i in xrange(3, int(sqrt(N)) + 1, 2):  # Possible Prime Numbers
        if sieve[i / 2]:  # If i is Prime
            sieve[i * i / 2::i] = [False] * ((N - i * i - 1) / (2 * i) + 1)

    return [2] + [2 * i + 1 for i in xrange(1, N / 2) if sieve[i]]
    
print primesList(11)