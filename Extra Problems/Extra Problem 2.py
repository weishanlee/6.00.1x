'''
These are two recursive functions. The first I found tricky but when I realised 
that I could set sharp(n) as the base it became really easy to do.

ndigits() was difficult as I wasn't sure how I could pass a counter inside a 
recurive function. A quick search brought up the a function that was almost 100%
the same as I was requiring but not quite. With a slight modification it worked for
my purposes. 
'''

def sharp(n):
    # n: int. 
    if n == 2:
        return 2
    else:
        return sharp(n-1) ** n
        

def ndigits(x, count = 0):
    # x, int. 
    if x == 0:
        return count
    return ndigits(x/10, count + 1)

ans = ndigits(sharp(7), count = 0) + 2*ndigits(sharp(6),count=0) + ndigits(sharp(5), count = 0) + ndigits(sharp(4), count = 0)
print ans

