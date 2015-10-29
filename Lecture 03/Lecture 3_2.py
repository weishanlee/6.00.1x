# Lecture 3
# Square a number up iterating up
# to iterate down, itersLeft = x, itersLeft != 0, itersLeft = itersLeft - 1

x = 3
ans = 0
itersLeft = 0 
while (itersLeft != x):
    ans = ans + x
    itersLeft = itersLeft + 1
print(str(x) + '*' + str(x) + ' = ' + str(ans))

print '-------------'

count = 2
while count < 12:
   print count
   count +=2
print 'Goodbye!'

print '-------------'

count = 12

while count > 2:
    if count > 10:
        print 'Hello!'
    count -= 2
    print count
    
print '-------------'

# sum all the numbers up to an end point
total = 7
score = 0
while total != 0:
    score = total + score
    total -= 1
print score    
    
    
    