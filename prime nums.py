'''
c=2
primes = []

while c<2001:
    r=0
    for i in range(1,c+1):
        if c%i == 0: r+=1
        
    if r==2: primes.append(c)
    c+=1

print(primes)
'''

c=2
primes = []

while c<2001:
    a=1
    r=0
    while a<c+1:
        if c%a == 0: r+=1
        a+=1
        
    if r==2: primes.append(c)
    c+=1

print(primes)
