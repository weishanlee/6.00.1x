def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    # evaluates the quadratic expression
    value = a * (x ** 2) + b * x + c 
    # returns the value
    return value

def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    '''
    # evaluates the sum of the values of two quadratics by using the evalQuadratic function
    value1 = evalQuadratic(a1, b1, c1, x1)
    value2 = evalQuadratic(a2, b2, c2, x2)
    # returns the value
    print value1 + value2
    return value1 + value2

