def findDivisors(n1, n2):
    divisors = ()
    for i in range(1, min(n1, n2) + 1):
        if n1%i == 0 and n2%i == 0:
            divisors = divisors + (i,)
    return divisors
    
    
listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']

animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
animals['d'] = 'donkey'