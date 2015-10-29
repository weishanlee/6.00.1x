print "Prime generator"
def genPrimes():
    primes = []
    last = 1
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last

primeList = genPrimes()

for i in range(1,11):
    print primeList.next()

# -------------------- #
print ""     
print "Fibonacci Generator" 

def genFib():
    fibn_1 = 1
    fibn_2 = 0
    while True:
        next_f = fibn_1 + fibn_2
        yield next_f
        fibn_2 = fibn_1
        fibn_1 = next_f
        
# Do not run this code as it is an infinite loop 
# printing out every possible fibonacci number. 
# however it may be useful in some situations
#for n in genFib():
#    print n
       
fibList = genFib()
for i in range(1,11):
    print fibList.next()


# -------------------- # 
print ""  
print "powers of two generator"        
def powerTwo():
    answer = 1
    while True:
       answer *= 2
       yield answer

power = powerTwo()
for i in range(1,11):
    print power.next()
    