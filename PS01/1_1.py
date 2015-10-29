s = 'azcbobobegghakl'

# count the number of letters in the the word
# for each letter, check if it belongs to the list of vowels
# if it contains a vowel add one to the vowels count
# print the number of vowels

vowel_cnt = 0
for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'u' or letter == 'o':
        vowel_cnt += 1
print 'Number of vowels: ' + str(vowel_cnt)

print '-----'

bob_cnt = 0
n = 0
word = 'bob'
o = 0
max_length = len(s) - len(word) + 1
while n < max_length:
    m = 0
    name = ''
    while m < len(word) and o < max_length:
        name += s[o] 
        m += 1
        o += 1
    o -= len(word) + 1
    if name == word:
        bob_cnt += 1
    n += 1
print 'Number of times bob occurs is: ' + str(bob_cnt)

print '-----'
'''
set the variables n = 0, we will iterate through the length of the the word using n
the current_longest = '' is set empty as we have not found the most current longest
testing is the most recent string of consequtive letters
the_longest is the longest string we have found, this is set to the first letter in the string

we loop through the length of the string to len(s) - 1 as our if statement will will use n + 1
this is to avoid domain errors

the first if statement checks the letters in turn and appends them to the variable testing
if the next letter is smaller than the current it breaks out of the if statement. 
in case it has iterated all the way through the the string, the final if statement protects
against a null return

the elif kicks in when the next letter is smaller that the current. An if statement checks to see
if the length of the current longest is longer than the the longest. if it is the longest's value is 
updated. the current value is updated to the value of testing, and testing has its value changed
to the next letter in the string, as there is no longer consequtive letters

finally n is increased by one and then we print out the value of the longest string


'''
s = 'nagdibecenezrlhwq'
n = 0
current_longest = ''
testing = s[n]
the_longest = s[n]
while n < len(s) - 1:
    
    if s[n] <= s[n+1]:      
        testing += s[n+1]
        #print testing
        
        
    elif s[n] > s[n+1]:
        
        #print 'current: ' + str(current_longest)
        #print 'longest: ' + str(the_longest)
        if len(current_longest) > len(the_longest):
            the_longest = current_longest
    
        current_longest = testing
        testing = s[n+1]
    
    if len(testing) > len(the_longest):
            the_longest = testing
            
    n += 1
print 'Longest substring in alphabetical order is: ' + str(the_longest)
        
        
        
    
        
        
        
