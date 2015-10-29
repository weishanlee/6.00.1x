str1 = 'exterminate!'
str2 = 'number one - the larch'

print str1.upper()
print str1.isupper()

str2 = str2.capitalize()

str2 = str2.swapcase()


#print str2.index('!')
print str2.find('!')

print str1.count('e')
str1 = str1.replace('e', '*')
print str1

print str2.replace('one', 'seven')