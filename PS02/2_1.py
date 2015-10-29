balance = 4211
annualInterestRate = 0.18
monthlyPaymentRate = 0.06

monthlyInterestRate = annualInterestRate/12
currentBalance = balance
totalPaid = 0
n = 1
m = 13

while n < m:
    print "Month: " + str(n)
    thisMonthsPayment = currentBalance * monthlyPaymentRate
    totalPaid += thisMonthsPayment
    print "Minimum monthly payment: " + str(format(thisMonthsPayment, '.2f'))
    new_balance = (currentBalance - thisMonthsPayment) * (1 + monthlyInterestRate)
    
        
    print "Remaining balance: " + str(format(new_balance, '.2f'))
    currentBalance = new_balance    
    n +=1
print "Total paid: " + str(format(totalPaid, '.2f'))
print "Remaining balance: " + str(format(new_balance, '.2f'))