balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12
low = balance / 12
high = (balance * (1 + monthlyInterestRate)**12)/12.0

guess = (low + high) / 2.0
epsilon = 0.01

def findValue(rate, balance, annualInterestRate):
    '''
    n:          int, allows us to iterate through the months
    rate:       float, the amount that we are paying each month
    balance:    float, the initial amount borrowed
    annualInterestRate:     float, the interest rate
    
    this method returns the value after 12 payments have been made
    this value can be +ve or -ve, 
    when the correct payment has been found it should return an answer of zero
    or close to this value
    '''
    n = 0 
    monthlyInterestRate = annualInterestRate / 12
    while n < 12:
        balance -= rate
        interest = (balance) * (monthlyInterestRate)
        balance = interest + balance
        n += 1
    return (balance) 

#find the inital value returned after the first guess
y = findValue(guess, balance, annualInterestRate)

'''
use the initial value of the returned balance to start the proccess of bisection
if the absolute value of the remaining balance is bigger than the tollerance 
then it it will continue bisecting until it reaches a point where it is smaller
than the tollerance

if the returned balance is positive, that means the guess was too small so our
guess must become the low value while the high remains the high value, 
else if the returned balance is negative, that means the guess was too high so our
guess becomes the high value while the low remains the low

after this has been perform and we have worked out the new guess,
the new guess is then checked to see what balance is left. 

This process is then repeated until tollerance is reached. 

'''
while abs(y) >= epsilon:
    if  y > 0:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    y = findValue(guess, balance, annualInterestRate) 
    
print "The lowest payment is: " + str(format(guess, '.2f'))





'''
What was important to do for this task was to find a way to decide when the while statement
would finish.

I struggled for a bit trying to think of how I could calculate the total cost of the loan
without working it out. Because if I knew the total cost, then I could just divide it by 
12 and I would have the optimum payment. However, this was a chicken and egg situation.
I needed two things to compare. In fact I originally ran the while statement for 20 iterations
however I felt that this wasn't good enough as some problems may require more iterations than that

by writing a method to find the remaining balance after 12 payments had been made
meant that I had something to compare. Ideally we would want a balance of zero after
all payments had been made. However, that wasn't going to be possible so by comparing
the remaining balance with the tollerance it was possible to construct the correct while statement
and then create the corresponding if statement so that the low and high values would be changed accordingly.
'''