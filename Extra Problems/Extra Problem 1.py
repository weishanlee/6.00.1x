from math import tan, pi
def funsum(n, s):
    '''
    n,  int, number of sides
    s, float, length of each side
    '''

    area = 0.25 * (s**2) * n / tan(pi/n)
    perimeter_squared = (n * s)**2
    
    return round(area + perimeter_squared, 4)

print funsum(7,3)