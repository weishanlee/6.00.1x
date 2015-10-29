'''
bob_cnt:    int, counts the number of times the word appears in the string
word:       string, the chosen word to look for
n:          int, used for looping up to the max_length of the string
max_length: int, this is the length of the string minus the length of the word that that we are looking for
o:          int, used for looping through the generated string 
m:          int, used for looping through the word
'''

s = 'azcbobobegghakl'
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
        print name
        m += 1
        o += 1
    o -= len(word)  #helps to iterate through the string s by returning the start of the iterate to the next letter 
    o += 1
    if name == word:
        bob_cnt += 1
    n += 1
print 'Number of times ' + str(word) + ' occurs is: ' + str(bob_cnt)
