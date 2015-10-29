# high value = 100 low value =0
# ask user if 50 is bigger or smaller than their number
# 

print 'Please think of a number between 0 and 100!'

lowest = 0
highest = 100
result = 0

while True:
    result = (highest + lowest)/2
    print 'Is your secret number ' + str(result) + '?'
    response = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if response.upper() == 'C':
        print 'Game over. Your secret number was: ' + str(result)
        break
    elif response.upper() == 'H':
        #lowest = lowest
        highest = result
    elif response.upper() == 'L':
        #highest = highest
        lowest = result
    else:
        print 'Sorry, I did not understand your input.'
        
        