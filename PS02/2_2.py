balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate / 12
rate = 10

'''
The first while statement will keep running until the condition in the if statement has been met
The second while statement runs for only 12 loops and updates the currentBalance
The idea is to have the currentBalance reduce to zero. 
After the second while statement completes and if the if condition has not been met, the 
the rate is increased by a preset amount.The currentBalance is returned to its original value 
and n is set to zero
'''

while True:
    currentBalance = balance
    n = 0 
    while n < 12:
        currentBalance -= rate
        interest = (currentBalance) * (monthlyInterestRate)
        currentBalance = interest + currentBalance
        n += 1
        
    if currentBalance <= 0:
        print "Lowest Payment: " + str(rate)
        break
    
    rate += 10
        
    